import pandas as pd,numpy as np,json,os
from scipy.special import logsumexp,expit
from scipy.optimize import brentq,minimize,minimize_scalar
from scipy.stats import chi2
from itertools import product
x=pd.read_excel('AutocraticRulingPartiesDataset.xlsx')
base=x[x.Party.notna() & x.Party.ne('N')].copy()
base['source_row']=base.index+2
base['country']=base.Country.str.strip()
base['start']=pd.to_numeric(base['Year in Power'])
base['last']=pd.to_numeric(base['Last Year of Power'],errors='coerce')
base['event']=base['last'].notna().astype(int)
base['exit']=base['last'].add(1).fillna(2016)
base['rev']=base['How Power Gained'].str.contains('Revolution',na=False)
base['marx']=base['Marxist?'].eq(1)
base['episode_id']='source_'+base.source_row.astype(str)
base['coding_note']='Original source spell; only annual boundary conversion'
base=base[~base.Party.eq('Communist Party of China') & (base.exit>np.maximum(base.start,1940))].copy()
def replace_episode(z,ids,start,end,event,note,country=None,newid=None,rev=None):
 anchor=z[z.source_row.eq(ids[-1])].iloc[0].copy();z=z[~z.source_row.isin(ids)].copy()
 anchor['start']=start;anchor['exit']=end;anchor['event']=event;anchor['coding_note']=note;anchor['episode_id']=newid or 'joined_'+'_'.join(map(str,ids))
 if country is not None:anchor['country']=country
 if rev is not None:anchor['rev']=rev
 return pd.concat([z,pd.DataFrame([anchor])],ignore_index=True)
def build(moz='continuous',sov_start=1918,sov_end=1990,mong_start=1921,nk_start=1948,mex_end=1997,eth_start=1991,sudan='1989',syria='continuous',kaz='omit',nic_start=1979,nic_end=1990,nic_new=2012,zam='2001',review_old=True,corrected=False):
 z=base.copy();z=z[~z.source_row.eq(28)].copy()
 z=replace_episode(z,[466,467],1954,2016,0,'Vietnam continuous across reunification',country='Vietnam',rev=True)
 z=replace_episode(z,[161,162],eth_start,2016,0,'EPRDF continuity across Eritrean separation',country='Ethiopia',rev=True)
 if sudan in ['1989','1998']:z=replace_episode(z,[400,401],int(sudan),2016,0,'NIF-NCP continuity; '+sudan+' accession; no secession event',country='Sudan',rev=False)
 else:
  z=replace_episode(z,[400,401],1989,2005,1,'NIF-NCP alternative loss at power sharing',country='Sudan',newid='Sudan_first',rev=False)
  rr=z[z.episode_id.eq('Sudan_first')].iloc[0].copy();rr['start']=2011;rr['exit']=2016;rr['event']=0;rr['episode_id']='Sudan_reacquired';rr['coding_note']='Sudan alternative reacquisition after secession';z=pd.concat([z,pd.DataFrame([rr])],ignore_index=True)
 if syria!='split1966':
  end=1970 if syria=='military1970' else 2016;z=replace_episode(z,[414,415],1963,end,int(end<2016),'Integrated Baath continuity' if end==2016 else 'Alternative military displacement in1970',country='Syria',rev=False)
 if kaz=='omit':z=z[~z.source_row.isin([245,246,247])].copy()
 else:
  z=replace_episode(z,[246,247],int(kaz),2016,0,'Conditional Otan-NurOtan eligibility; predecessor not joined',country='Kazakhstan',rev=False);z=z[~z.source_row.eq(245)].copy()
 z.loc[z.source_row.eq(454),['start','exit','coding_note']]=[sov_start,sov_end,'Reviewed Soviet accession and loss']
 z.loc[z.source_row.eq(303),['start','coding_note']]=[mong_start,'Reviewed Mongolian accession;1990 loss']
 z.loc[z.source_row.eq(249),['start','coding_note']]=[nk_start,'Reviewed northern-state accession;end2015 censoring']
 z.loc[z.source_row.eq(302),['exit','coding_note']]=[mex_end,'Reviewed Mexican supremacy loss']
 z.loc[z.source_row.eq(316),['start','exit','coding_note']]=[nic_start,nic_end,'First FSLN supremacy episode']
 if nic_new is not None:
  rr=z[z.source_row.eq(316)].iloc[0].copy();rr['start']=nic_new;rr['exit']=2016;rr['event']=0;rr['rev']=False;rr['episode_id']='FSLN_reacquired';rr['coding_note']='Added FSLN reacquisition; not a revolutionary accession';z=pd.concat([z,pd.DataFrame([rr])],ignore_index=True)
 if moz=='continuous':z=replace_episode(z,[306,307],1975,2016,0,'FRELIMO continuous-supremacy branch',country='Mozambique',rev=True)
 else:
  z.loc[z.source_row.eq(307),['start','coding_note']]=[int(moz),'FRELIMO reacquisition branch; electoral/institutional, not revolutionary'];z.loc[z.source_row.eq(306),'coding_note']='FRELIMO first loss at1994 opening'
 if zam=='omit':z=z[~z.source_row.eq(477)].copy()
 else:z.loc[z.source_row.eq(477),['start','exit','coding_note']]=[1996,int(zam),'Provisional MMD supremacy episode']
 if corrected:z=z[~z.source_row.eq(243)&~z.episode_id.eq('FSLN_reacquired')].copy()
 z=z.reset_index(drop=True);assert (z.exit>np.maximum(z.start,1940)).all();assert z.episode_id.is_unique
 return z

def arr(z,threshold=0):
 t=(z.exit-z.start).to_numpy(float);e=np.maximum((1940-z.start).clip(lower=0).to_numpy(float),threshold);d=z.event.to_numpy(float);keep=t>e
 return t[keep],e[keep],d[keep]
def lji(beta,t,e):
 delta=t-e;x=beta*delta;L=np.empty_like(x);m=np.empty_like(x);near=np.abs(x)<1e-4;pos=x>50;neg=x< -50;mid=~(near|pos|neg)
 y=x[near];L[near]=y/2+y*y/24-y**4/2880;m[near]=.5+y/12-y**3/720
 y=x[pos];L[pos]=y+np.log1p(-np.exp(-y))-np.log(y);m[pos]=1/(1-np.exp(-y))-1/y
 y=x[neg];L[neg]=np.log1p(-np.exp(y))-np.log(-y);m[neg]=np.exp(y)/np.expm1(y)-1/y
 y=x[mid];L[mid]=np.log(np.expm1(y)/y);m[mid]=np.exp(y)/np.expm1(y)-1/y
 return beta*e+np.log(delta)+L,e+delta*m
def fitg_arrays(t,e,d):
 D=d.sum();T=np.dot(d,t)
 if D==0:raise ValueError('No events: finite interior Gompertz MLE not identified')
 def score(beta):
  logs,mean=lji(beta,t,e);return D*np.dot(np.exp(logs-logsumexp(logs)),mean)-T
 lo,hi=-1.,1.
 while score(lo)>=0 and abs(lo)<128:lo*=2
 while score(hi)<=0 and hi<128:hi*=2
 beta=brentq(score,lo,hi,xtol=1e-12);la=np.log(D)-logsumexp(lji(beta,t,e)[0]);nll=D-D*la-beta*T
 return la,beta,nll
def predict(la,b,A=77,u=25):
 h=np.exp(la+b*A);H=h*u if abs(b)<1e-10 else h*np.expm1(b*u)/b
 return -np.expm1(-H),1. if b>=0 else -np.expm1(h/b)
def subset(z,name):
 if name=='All':return z
 return z[z.rev] if name=='Revolutionary accession' else z[z.rev & z.marx]
sets=['All','Revolutionary accession','Marxist revolutionary accession']
specs={'ARPD benchmark':base,'Earlier Vietnam correction':replace_episode(base.copy(),[466,467],1954,2016,0,'Earlier Vietnam correction',country='Vietnam',rev=True)}
for corrected in [False,True]:
 for moz in ['continuous','2004','2009']:specs[('Corrected' if corrected else 'Frozen')+' '+moz]=build(moz=moz,corrected=corrected)
results=[]
for sn,z in specs.items():
 for group in sets:
  g=subset(z,group);t,e,d=arr(g);la,b,nll=fitg_arrays(t,e,d);p25,pe=predict(la,b)
  results.append(dict(spec=sn,set=group,n=len(t),events=int(d.sum()),country_blocks=g.country.nunique(),log_alpha=la,beta=b,NLL=nll,AIC=4+2*nll,loss25_from77=p25,eventual_loss_from77=pe,max_age=float(t.max()),exposure_years=float((t-e).sum()),hazard77=float(np.exp(la+77*b))))
fits=pd.DataFrame(results)


boot_rows=[]
def bootstrap_version(version):
 children=np.random.SeedSequence(20261124).spawn(6)
 for si,moz in enumerate(['continuous','2004']):
  sn=version+' '+moz
  for gi,group in enumerate(sets):
   z=subset(specs[sn],group).reset_index(drop=True);t,e,d=arr(z);cs=z.country.to_numpy();countries=pd.unique(cs);blocks_local=[np.flatnonzero(cs==c) for c in countries];rng=np.random.default_rng(children[si*3+gi])
   for rep in range(2000):
    chosen=rng.integers(0,len(blocks_local),len(blocks_local));ix=np.concatenate([blocks_local[c] for c in chosen])
    try:
     la,b,nll=fitg_arrays(t[ix],e[ix],d[ix]);p25,pe=predict(la,b);boot_rows.append(dict(spec=sn,set=group,replicate=rep,success=True,log_alpha=la,beta=b,loss25_from77=p25,eventual_loss_from77=pe,error=''))
    except Exception as err:boot_rows.append(dict(spec=sn,set=group,replicate=rep,success=False,error=str(err)))

bootstrap_version("Frozen")
bootstrap_version("Corrected")


joint_choices=list(product(['continuous','2004','2009'],['1989','1998','interruption'],['continuous','split1966','military1970'],['omit','1999','2006'],['2001','2006','omit'],[1984,1990],[1990,1991]))
joint_rows=[]
def joint_batch(version,lo,hi):
 for cid in range(lo,hi):
  moz,sudan,syria,kaz,zam,nic_end,sov_end=joint_choices[cid];z=build(moz=moz,sudan=sudan,syria=syria,kaz=kaz,zam=zam,nic_end=nic_end,sov_end=sov_end,corrected=version=='Corrected')
  for group in sets:
   t,e,d=arr(subset(z,group));la,b,nll=fitg_arrays(t,e,d);p25,pe=predict(la,b);joint_rows.append(dict(version=version,coding_id=cid,set=group,Mozambique=moz,Sudan=sudan,Syria=syria,Kazakhstan=kaz,Zambia=zam,FSLN_first_loss=nic_end,Soviet_loss=sov_end,n=len(t),events=int(d.sum()),beta=b,loss25_from77=p25,eventual_loss_from77=pe))

for version in ["Frozen","Corrected"]:
 for lo in range(0,972,243):joint_batch(version,lo,min(lo+243,972))


bo=pd.DataFrame(boot_rows)
bs=bo.groupby(['spec','set']).agg(requested=('replicate','size'),successful=('success','sum'),beta_ge0=('beta',lambda q:(q>=0).sum()),beta_q025=('beta',lambda q:q.quantile(.025)),beta_q975=('beta',lambda q:q.quantile(.975)),loss25_q025=('loss25_from77',lambda q:q.quantile(.025)),loss25_q975=('loss25_from77',lambda q:q.quantile(.975)),eventual_q025=('eventual_loss_from77',lambda q:q.quantile(.025)),eventual_q975=('eventual_loss_from77',lambda q:q.quantile(.975))).reset_index()


joint=pd.DataFrame(joint_rows)
js=joint.groupby(['version','set']).agg(fits=('coding_id','size'),min_eventual=('eventual_loss_from77','min'),max_eventual=('eventual_loss_from77','max'),min_25=('loss25_from77','min'),max_25=('loss25_from77','max')).reset_index()


families=[]
for sn in list(specs)[2:]:
 for group in sets:
  t,e,d=arr(subset(specs[sn],group));D=d.sum();rate=D/np.sum(t-e)
  families.append(dict(spec=sn,set=group,model='Exponential',NLL=D-D*np.log(rate),AIC=2+2*(D-D*np.log(rate)),loss25_from77=-np.expm1(-rate*25),eventual_loss_from77=1.,parameters=[rate],bound_contact=False,success=True))
  def wn(q):
   k,scale=np.exp(q);return np.sum((t/scale)**k-(e/scale)**k-d*(np.log(k)-k*np.log(scale)+(k-1)*np.log(t)))
  o=min([minimize(wn,[np.log(k),np.log(30)],bounds=[(-4,3),(-2,10)],options={'ftol':1e-12}) for k in [.5,1,2]],key=lambda o:o.fun);k,scale=np.exp(o.x);H=(102/scale)**k-(77/scale)**k
  families.append(dict(spec=sn,set=group,model='Weibull',NLL=o.fun,AIC=4+2*o.fun,loss25_from77=-np.expm1(-H),eventual_loss_from77=1.,parameters=[k,scale],bound_contact=bool(np.any(np.isclose(o.x,[-4,-2],atol=1e-4)) or np.any(np.isclose(o.x,[3,10],atol=1e-4))),success=bool(o.success)))
  def mn(q):
   cure=expit(q[0]);rate=np.exp(q[1]);lq=np.log(cure);l1=np.log1p(-cure);St=np.logaddexp(lq,l1-rate*t);Se=np.logaddexp(lq,l1-rate*e);lf=l1+q[1]-rate*t
   return -np.sum(d*lf+(1-d)*St-Se)
  o=min([minimize(mn,[q,np.log(.05)],bounds=[(-20,15),(-12,2)],options={'ftol':1e-12,'maxiter':1000}) for q in [-6,-2,0,3]],key=lambda o:o.fun);cure=expit(o.x[0]);rate=np.exp(o.x[1]);S77=cure+(1-cure)*np.exp(-rate*77);S102=cure+(1-cure)*np.exp(-rate*102)
  families.append(dict(spec=sn,set=group,model='Exponential cure mixture',NLL=o.fun,AIC=4+2*o.fun,loss25_from77=1-S102/S77,eventual_loss_from77=1-cure/S77,parameters=[cure,rate],bound_contact=bool(np.any(np.isclose(o.x,[-20,-12],atol=1e-4)) or np.any(np.isclose(o.x,[15,2],atol=1e-4))),success=bool(o.success)))
  def pn(q):
   a,tau,powr=np.exp(q);v=1-powr;le=np.log1p(e/tau);diff=np.log1p(t/tau)-le;H=a*tau*diff if abs(v)<1e-7 else a*tau*np.exp(v*le)*np.expm1(v*diff)/v
   return np.sum(H-d*(q[0]-powr*np.log1p(t/tau)))
  bounds=[(-15,2),(-4.6,11.5),(-6,6)];o=min([minimize(pn,np.log([.07,tau,powr]),bounds=bounds,options={'ftol':1e-12,'maxiter':1000}) for tau,powr in [(10,.5),(10,2),(100,2),(1000,10)]],key=lambda o:o.fun);a,tau,powr=np.exp(o.x);v=1-powr
  H25=a*tau*np.exp(v*np.log1p(77/tau))*np.expm1(v*(np.log1p(102/tau)-np.log1p(77/tau)))/v if abs(v)>1e-7 else a*tau*np.log((tau+102)/(tau+77));rem=np.inf if powr<=1 else a*tau/(powr-1)*np.exp((1-powr)*np.log1p(77/tau))
  families.append(dict(spec=sn,set=group,model='Power-declining hazard',NLL=o.fun,AIC=6+2*o.fun,loss25_from77=-np.expm1(-H25),eventual_loss_from77=-np.expm1(-rem),parameters=[a,tau,powr],bound_contact=bool(any(abs(o.x[j]-bounds[j][k])<1e-3 for j in range(3) for k in [0,1])),success=bool(o.success)))
fam=pd.DataFrame(families)


def profile_R(logR,t,e,d):
 D=d.sum();T=np.dot(d,t)
 def nll(theta):
  beta=-np.exp(theta);la=logR+theta-77*beta;logH=la+logsumexp(lji(beta,t,e)[0]);return (np.exp(logH) if logH<690 else 1e300)-D*la-beta*T
 opts=[minimize_scalar(nll,bounds=bd,method='bounded',options={'xatol':1e-11}) for bd in [(-24,-8),(-8,-2),(-2,3)]];o=min(opts,key=lambda q:q.fun);theta=o.x
 return o.fun,-np.exp(theta),logR+theta+77*np.exp(theta)
profiles=[]
for sn in list(specs)[2:]:
 for group in sets:
  t,e,d=arr(subset(specs[sn],group));la,b,nll=fitg_arrays(t,e,d);half=profile_R(np.log(np.log(2)),t,e,d);bb=max(0,b);aa=np.log(d.sum())-logsumexp(lji(bb,t,e)[0]);nn=d.sum()-d.sum()*aa-bb*np.dot(d,t)
  def cut(logR):return 2*(profile_R(logR,t,e,d)[0]-nll)-chi2.ppf(.95,1)
  grid=np.linspace(-12,15,70);vals=[cut(q) for q in grid];roots=[]
  for j in range(len(grid)-1):
   if vals[j]*vals[j+1]<0:
    rt=brentq(cut,grid[j],grid[j+1],xtol=1e-8);roots.append(float(-np.expm1(-np.exp(rt))))
  profiles.append(dict(spec=sn,set=group,LR_at_half=2*(half[0]-nll),LR_at_one=2*(nn-nll),finite_crossings=roots,cutoff=float(chi2.ppf(.95,1))))
prof=pd.DataFrame(profiles)


changes={'Soviet accession1921':{'sov_start':1921},'Soviet loss1991':{'sov_end':1991},'Mongolian accession1924':{'mong_start':1924},'North Korean accession1946':{'nk_start':1946},'Mexican loss1996':{'mex_end':1996},'Mexican loss2000':{'mex_end':2000},'Ethiopian accession1992':{'eth_start':1992},'Sudan NCP-only1998':{'sudan':'1998'},'Sudan power-sharing interruption':{'sudan':'interruption'},'Syrian split1966':{'syria':'split1966'},'Syrian military displacement1970':{'syria':'military1970'},'Kazakh eligibility1999':{'kaz':'1999'},'Kazakh eligibility2006':{'kaz':'2006'},'Nicaraguan accession1980':{'nic_start':1980},'Nicaraguan loss1984':{'nic_end':1984},'FSLN reacquisition2009':{'nic_new':2009},'FSLN reacquisition2011':{'nic_new':2011},'FSLN no reacquisition before2016':{'nic_new':None},'MMD loss2006':{'zam':'2006'},'MMD no qualifying episode':{'zam':'omit'}}
sensrows=[]
for version in ['Frozen','Corrected']:
 for moz in ['continuous','2004','2009']:
  for label,args in changes.items():
   z=build(moz=moz,corrected=version=='Corrected',**args)
   for group in sets:
    t,e,d=arr(subset(z,group));la,b,nll=fitg_arrays(t,e,d);p25,pe=predict(la,b);sensrows.append(dict(version=version,Mozambique=moz,change=label,set=group,n=len(t),beta=b,loss25_from77=p25,eventual_loss_from77=pe))
sens=pd.DataFrame(sensrows)
oldrows=[];oldrec=[]
for sn in ['ARPD benchmark','Frozen continuous','Corrected continuous']:
 z=specs[sn];g=z[(z.exit-z.start)>np.maximum((1940-z.start).clip(lower=0),60)].copy();t,e,d=arr(g,60);la,b,nll=fitg_arrays(t,e,d);p25,pe=predict(la,b);oldrows.append(dict(spec=sn,n=len(t),events=int(d.sum()),exposure_years_after60=float((t-e).sum()),log_alpha=la,beta=b,loss25_from77=p25,eventual_loss_from77=pe));g['spec']=sn;g['entry_age60']=np.maximum((1940-g.start).clip(lower=0),60);g['exit_age']=g.exit-g.start;oldrec.append(g[['spec','episode_id','country','Party','start','exit','event','entry_age60','exit_age']])
old=pd.DataFrame(oldrows);oldrecords=pd.concat(oldrec)
influence=[];tails=[]
for sn in ['Frozen continuous','Frozen 2004','Corrected continuous','Corrected 2004']:
 for group in sets:
  z=subset(specs[sn],group);t,e,d=arr(z);la,b,nll=fitg_arrays(t,e,d);_,baseline=predict(la,b)
  for row in [271,454,303,302,249]:
   m=z.source_row.eq(row)
   if not m.any():continue
   tt,ee,dd=arr(z.loc[~m]);lla,bb,nn=fitg_arrays(tt,ee,dd);p25,pe=predict(lla,bb);influence.append(dict(spec=sn,set=group,deleted_source_row=row,deleted_country=z.loc[m,'country'].iloc[0],n=len(tt),beta=bb,loss25_from77=p25,eventual_loss_from77=pe,change_eventual_pp=100*(pe-baseline)))
  L=t.max();hL=np.exp(la+b*L);pre=0 if L<=77 else np.exp(la+b*77)*np.expm1(b*(L-77))/b
  for target in ([.4,.8] if group=='All' else [.25,.75]):
   R=-np.log1p(-target);k=brentq(lambda k:pre+hL*np.exp(-k*max(0.,77-L))/k-R,1e-9,10);achieved=-np.expm1(-(pre+hL*np.exp(-k*max(0.,77-L))/k));H=np.exp(la)*np.exp(b*e)*np.expm1(b*(t-e))/b;ll_diff=np.sum(H-d*(la+b*t))-nll
   tails.append(dict(spec=sn,set=group,last_observed_age=float(L),fixed_hazard_from77_to_L=pre,target_eventual_loss=target,tail_decay_k=k,recomputed_target=achieved,observed_nll_difference=ll_diff))
inf=pd.DataFrame(influence);tail=pd.DataFrame(tails)
bridge_rows=[];precision_rows=[];threshold_rows=[]
for version in ['Frozen saved','Frozen refit','Corrected refit']:
 for moz in ['continuous','2004']:
  sn=('Corrected' if version=='Corrected refit' else 'Frozen')+' '+moz;q=fits[(fits.spec==sn)&(fits['set']=='All')].iloc[0];la,b=q.log_alpha,q.beta
  if version=='Frozen saved':la,b=(-2.609769,-.018582) if moz=='continuous' else (-2.614083,-.017865)
  h=np.exp(la+77*b);threshold_rows.append(dict(version=version,baseline=moz,hazard77=h,half_life_tie_m075=np.log(2)**2/(.75*h),multiplier_tie_half50=np.log(2)**2/(50*h)))
  for m in [.5,.75,1.]:
   for half in [25,50,100]:
    k=np.log(2)/half;R=m*h/k;row=dict(version=version,baseline=moz,historical_hazard_at77=h,multiplier=m,half_life_years=half,china_initial_hazard=m*h,k=k,remaining_integrated_hazard=R,eventual_loss=-np.expm1(-R),indefinite_retention=np.exp(-R))
    for T in [10,25,50]:row['loss_'+str(T)+'years']=-np.expm1(-R*(-np.expm1(-k*T)))
    bridge_rows.append(row)
bridge=pd.DataFrame(bridge_rows);thresholds=pd.DataFrame(threshold_rows)


from scipy.integrate import quad
likcheck=[]
for sn in list(specs)[2:]:
 for group in sets:
  t,e,d=arr(subset(specs[sn],group));la,b,nll=fitg_arrays(t,e,d);H=np.array([quad(lambda age:np.exp(la+b*age),ee,tt)[0] for tt,ee in zip(t,e)])
  likcheck.append(dict(spec=sn,set=group,nll_difference=float(np.sum(H-d*(la+b*t))-nll)))
likcheck=pd.DataFrame(likcheck)


stress_rows=[]
for moz in ['continuous','2004','2009']:
 for omit_zam,interrupt_sudan,military_syria in product([False,True],repeat=3):
  z=build(moz=moz,corrected=True,zam='omit' if omit_zam else '2001',sudan='interruption' if interrupt_sudan else '1989',syria='military1970' if military_syria else 'continuous')
  t,e,d=arr(z);la,b,nll=fitg_arrays(t,e,d);h=np.exp(la+77*b);pc=-np.expm1(-.75*h/(np.log(2)/50))
  stress_rows.append(dict(Mozambique=moz,omit_MMD=omit_zam,Sudan_interruption=interrupt_sudan,Syria_military1970=military_syria,n=len(t),events=int(d.sum()),hazard77=h,china_eventual=pc))
stress=pd.DataFrame(stress_rows)

os.makedirs('reproduced',exist_ok=True)
tables={'primary_fits':fits,'bootstrap_summary':bs,'bootstrap_replicates':bo,'joint_coding_summary':js,'joint_coding_results':joint,'alternative_families':fam,'likelihood_profiles':prof,'one_change_sensitivity':sens,'age60_diagnostic':old,'age60_records':oldrecords,'selected_record_influence':inf,'identical_fit_tail_constructions':tail,'china_bridge':bridge,'bridge_thresholds':pd.DataFrame(threshold_rows),'strict_rule_stress_test':stress,'likelihood_quadrature_checks':likcheck}
for name,table in tables.items():table.to_csv('reproduced/'+name+'.csv',index=False)
for name,z in specs.items():z.to_csv('reproduced/records_'+name.replace(' ','_')+'.csv',index=False)
