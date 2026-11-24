## 5. Frozen China bridge, arithmetic and thresholds

```text
t = years after assessment; reference age A = 77
h0 = m * exp(log_alpha + beta*77)
k = ln(2) / half_life
h_China(t) = h0 * exp(-k*t)
R_infinity = h0/k
P_loss(T) = 1-exp[-R_infinity*(1-exp(-k*T))]
P_eventual_loss = 1-exp(-R_infinity)
P_indefinite_retention = exp(-R_infinity)
central: m=0.75; half_life=50 years
```

The initial multiplier lowers the historical age-77 hazard by 25%. The 50-year half-life is slower hazard decline than the historical broad Gompertz decline, offsetting some of that discount. These are frozen elicited assumptions, not fitted China coefficients. Neither number is quantitatively estimated by the sources below. There is no scenario-count weighting, separate war-probability add-on, or independent multiplier for each correlated pressure.

The Frozen saved rows use exactly the six-decimal historical coefficients prescribed in the supplied methods. Frozen refit uses full-precision coefficients. Corrected refit uses the changed records and full precision. Tiny rounding differences are not coding effects. The 18 saved eventual probabilities and 54 saved 10/25/50-year probabilities were compared with the user-supplied grid and match at the numerical precision used. Split-2009 is historical sensitivity, not an invented third frozen China baseline.

| version | baseline | eventual_loss (%) | indefinite_retention (%) | loss_10years (%) | loss_25years (%) | loss_50years (%) |
|---|---|---|---|---|---|---|
| Frozen saved | continuous | 61.3833673 | 38.6166327 | 11.5886181 | 24.3221083 | 37.8577175 |
| Frozen saved | 2004 | 63.2549452 | 36.7450548 | 12.1553651 | 25.4153071 | 39.3823006 |
| Frozen refit | continuous | 61.3831068 | 38.6168932 | 11.5885409 | 24.3219588 | 37.857508 |
| Frozen refit | 2004 | 63.2561494 | 36.7438506 | 12.1557377 | 25.416023 | 39.3832939 |
| Corrected refit | continuous | 61.7926476 | 38.2073524 | 11.7104797 | 24.5579166 | 38.1879038 |
| Corrected refit | 2004 | 63.660631 | 36.339369 | 12.2815195 | 25.6574392 | 39.7178558 |

| version | baseline | hazard77 | half_life_tie_m075 | multiplier_tie_half50 |
|---|---|---|---|---|
| Frozen saved | continuous | 0.0175872161 | 36.4244128 | 0.546366192 |
| Frozen saved | 2004 | 0.0185054869 | 34.6169772 | 0.519254658 |
| Frozen refit | continuous | 0.0175870914 | 36.424671 | 0.546370065 |
| Frozen refit | 2004 | 0.0185060927 | 34.615844 | 0.51923766 |
| Corrected refit | continuous | 0.0177841644 | 36.0210355 | 0.540315533 |
| Corrected refit | 2004 | 0.0187106946 | 34.237319 | 0.513559784 |

At m=0.75, the saved continuous baseline switches to loss-favored above a half-life of 36.4244 years; split-2004 above 34.6170 years. At m=0.5 and 50-year half-life retention is favored. Grid cells have no probability weights. The continuous saved grid spans 27.18%–92.09%; split-2004 has a slightly wider upper endpoint. Extrema are not credible intervals. Historical parameter uncertainty, model selection and unforeseeable institutional change are not propagated into this parameter grid.

**Retained bridge specification**

```text
Target: eventual loss/relinquishment of decisive CCP authoritarian supremacy over China central political order, conditional on continued supremacy at assessment. Not leader replacement, Party disappearance, or necessarily democratization.
Frozen historical input: rounded coefficients. Continuous log(alpha)=-2.609769, beta=-0.018582; split2004 log(alpha)=-2.614083, beta=-0.017865. Age approximately 77.
Bridge: h_China(t)=m*h_reference(77)*exp(-k*t), k=ln(2)/half_life. R=m*h_reference(77)/k. Eventual loss=1-exp(-R). Finite loss(T)=1-exp[-R*(1-exp(-k*T))].
Frozen working assumptions: m=.75, half-life50 years. These are elicited assumptions, not estimated coefficients or numbers quantitatively identified by the cited evidence. The .75 represents illustrative net durability; 50 years represents slower hazard decline than the historical 37-39-year broad-fit half-life.
Central outputs: eventual loss61.4%-63.3%; next10 years11.6%-12.2%,25 years24.3%-25.4%,50 years37.9%-39.4%. Rounded approximately60% eventual loss versus40% indefinite retention.
Sensitivity: m=.5,.75,1 and half-life25,50,100. No probabilities assigned to grid cells; extrema not credible interval. Continuous range27.2%-92.1%. Historical coefficient uncertainty not propagated into this grid.
No separate multipliers for correlated pressures, no war-probability add-on, no scenario-count probabilities, no risk increase merely from opacity or observed dissent. AI local effects are not proof indefinite national control. No complete post2015 comparator update.
Sources: IMF26/44; AI-tocracy QJE2023; Laboratories of Autocracy NBER34219; Freedom House China2026; CSIS February2026; Brookings October2026; CSMonitor October29 2026. Nathan Law Carnegie essay is perspective, not measured survival evidence.
This embedded specification faithfully records the supplied numerical rules and caveats; it is not represented as a byte-identical original Markdown file.
```

| version | baseline | historical_hazard_at77 | multiplier | half_life_years | china_initial_hazard | k | remaining_integrated_hazard | eventual_loss | indefinite_retention | loss_10years | loss_25years | loss_50years |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frozen saved | continuous | 0.0175872161 | 0.5 | 25 | 0.00879360804 | 0.0277258872 | 0.317162368 | 0.271787493 | 0.728212507 | 0.0739233202 | 0.146646318 | 0.211696236 |
| Frozen saved | continuous | 0.0175872161 | 0.5 | 50 | 0.00879360804 | 0.0138629436 | 0.634324736 | 0.469706544 | 0.530293456 | 0.0788321205 | 0.169551542 | 0.271787493 |
| Frozen saved | continuous | 0.0175872161 | 0.5 | 100 | 0.00879360804 | 0.00693147181 | 1.26864947 | 0.718788851 | 0.281211149 | 0.0814488248 | 0.182779784 | 0.310355359 |
| Frozen saved | continuous | 0.0175872161 | 0.75 | 25 | 0.0131904121 | 0.0277258872 | 0.475743552 | 0.378577175 | 0.621422825 | 0.108809759 | 0.211696236 | 0.300092898 |
| Frozen saved | continuous | 0.0175872161 | 0.75 | 50 | 0.0131904121 | 0.0138629436 | 0.951487103 | 0.613833673 | 0.386166327 | 0.115886181 | 0.243221083 | 0.378577175 |
| Frozen saved | continuous | 0.0175872161 | 0.75 | 100 | 0.0131904121 | 0.00693147181 | 1.90297421 | 0.850875568 | 0.149124432 | 0.119650675 | 0.26123102 | 0.427285671 |
| Frozen saved | continuous | 0.0175872161 | 1 | 25 | 0.0175872161 | 0.0277258872 | 0.634324736 | 0.469706544 | 0.530293456 | 0.142381983 | 0.271787493 | 0.378577175 |
| Frozen saved | continuous | 0.0175872161 | 1 | 50 | 0.0175872161 | 0.0138629436 | 1.26864947 | 0.718788851 | 0.281211149 | 0.151449738 | 0.310355359 | 0.469706544 |
| Frozen saved | continuous | 0.0175872161 | 1 | 100 | 0.0175872161 | 0.00693147181 | 2.53729894 | 0.92092029 | 0.0790797105 | 0.156263739 | 0.332151119 | 0.524390269 |
| Frozen saved | 2004 | 0.0185054869 | 0.5 | 25 | 0.00925274347 | 0.0277258872 | 0.333722178 | 0.283747255 | 0.716252745 | 0.0776292867 | 0.153682834 | 0.221426308 |
| Frozen saved | 2004 | 0.0185054869 | 0.5 | 50 | 0.00925274347 | 0.0138629436 | 0.667444356 | 0.486982005 | 0.513017995 | 0.0827730045 | 0.177568371 | 0.283747255 |
| Frozen saved | 2004 | 0.0185054869 | 0.5 | 100 | 0.00925274347 | 0.00693147181 | 1.33488871 | 0.736812536 | 0.263187464 | 0.0855143507 | 0.191347162 | 0.323606216 |
| Frozen saved | 2004 | 0.0185054869 | 0.75 | 25 | 0.0138791152 | 0.0277258872 | 0.500583267 | 0.393823006 | 0.606176994 | 0.114153941 | 0.221426308 | 0.31301131 |
| Frozen saved | 2004 | 0.0185054869 | 0.75 | 50 | 0.0138791152 | 0.0138629436 | 1.00116653 | 0.632549452 | 0.367450548 | 0.121553651 | 0.254153071 | 0.393823006 |
| Frozen saved | 2004 | 0.0185054869 | 0.75 | 100 | 0.0138791152 | 0.00693147181 | 2.00233307 | 0.864980095 | 0.135019905 | 0.125488868 | 0.272817913 | 0.443712358 |
| Frozen saved | 2004 | 0.0185054869 | 1 | 25 | 0.0185054869 | 0.0277258872 | 0.667444356 | 0.486982005 | 0.513017995 | 0.149232267 | 0.283747255 | 0.393823006 |
| Frozen saved | 2004 | 0.0185054869 | 1 | 50 | 0.0185054869 | 0.0138629436 | 1.33488871 | 0.736812536 | 0.263187464 | 0.158694639 | 0.323606216 | 0.486982005 |
| Frozen saved | 2004 | 0.0185054869 | 1 | 100 | 0.0185054869 | 0.00693147181 | 2.66977742 | 0.930732359 | 0.069267641 | 0.163715997 | 0.346080588 | 0.542491449 |
| Frozen refit | continuous | 0.0175870914 | 0.5 | 25 | 0.0087935457 | 0.0277258872 | 0.317160119 | 0.271785855 | 0.728214145 | 0.073922816 | 0.146645358 | 0.211694906 |
| Frozen refit | continuous | 0.0175870914 | 0.5 | 50 | 0.0087935457 | 0.0138629436 | 0.634320239 | 0.46970416 | 0.53029584 | 0.0788315842 | 0.169550448 | 0.271785855 |
| Frozen refit | continuous | 0.0175870914 | 0.5 | 100 | 0.0087935457 | 0.00693147181 | 1.26864048 | 0.718786322 | 0.281213678 | 0.0814482716 | 0.182778615 | 0.310353542 |
| Frozen refit | continuous | 0.0175870914 | 0.75 | 25 | 0.0131903186 | 0.0277258872 | 0.475740179 | 0.37857508 | 0.62142492 | 0.108809031 | 0.211694906 | 0.300091127 |
| Frozen refit | continuous | 0.0175870914 | 0.75 | 50 | 0.0131903186 | 0.0138629436 | 0.951480358 | 0.613831068 | 0.386168932 | 0.115885409 | 0.243219588 | 0.37857508 |
| Frozen refit | continuous | 0.0175870914 | 0.75 | 100 | 0.0131903186 | 0.00693147181 | 1.90296072 | 0.850873556 | 0.149126444 | 0.119649879 | 0.261229434 | 0.427283409 |
| Frozen refit | continuous | 0.0175870914 | 1 | 25 | 0.0175870914 | 0.0277258872 | 0.634320239 | 0.46970416 | 0.53029584 | 0.142381049 | 0.271785855 | 0.37857508 |
| Frozen refit | continuous | 0.0175870914 | 1 | 50 | 0.0175870914 | 0.0138629436 | 1.26864048 | 0.718786322 | 0.281213678 | 0.15144875 | 0.310353542 | 0.46970416 |
| Frozen refit | continuous | 0.0175870914 | 1 | 100 | 0.0175870914 | 0.00693147181 | 2.53728096 | 0.920918867 | 0.0790811329 | 0.156262722 | 0.332149208 | 0.524387764 |
| Frozen refit | 2004 | 0.0185060927 | 0.5 | 25 | 0.00925304635 | 0.0277258872 | 0.333733102 | 0.283755079 | 0.716244921 | 0.0776317265 | 0.153687457 | 0.221432687 |
| Frozen refit | 2004 | 0.0185060927 | 0.5 | 50 | 0.00925304635 | 0.0138629436 | 0.667466204 | 0.486993213 | 0.513006787 | 0.0827755986 | 0.177573634 | 0.283755079 |
| Frozen refit | 2004 | 0.0185060927 | 0.5 | 100 | 0.00925304635 | 0.00693147181 | 1.33493241 | 0.736824037 | 0.263175963 | 0.0855170267 | 0.191352784 | 0.323614873 |
| Frozen refit | 2004 | 0.0185060927 | 0.75 | 25 | 0.0138795695 | 0.0277258872 | 0.500599653 | 0.393832939 | 0.606167061 | 0.114157456 | 0.221432687 | 0.313019753 |
| Frozen refit | 2004 | 0.0185060927 | 0.75 | 50 | 0.0138795695 | 0.0138629436 | 1.00119931 | 0.632561494 | 0.367438506 | 0.121557377 | 0.25416023 | 0.393832939 |
| Frozen refit | 2004 | 0.0185060927 | 0.75 | 100 | 0.0138795695 | 0.00693147181 | 2.00239861 | 0.864988945 | 0.135011055 | 0.125492707 | 0.272825496 | 0.443723038 |
| Frozen refit | 2004 | 0.0185060927 | 1 | 25 | 0.0185060927 | 0.0277258872 | 0.667466204 | 0.486993213 | 0.513006787 | 0.149236768 | 0.283755079 | 0.393832939 |
| Frozen refit | 2004 | 0.0185060927 | 1 | 50 | 0.0185060927 | 0.0138629436 | 1.33493241 | 0.736824037 | 0.263175963 | 0.158699398 | 0.323614873 | 0.486993213 |
| Frozen refit | 2004 | 0.0185060927 | 1 | 100 | 0.0185060927 | 0.00693147181 | 2.66986482 | 0.930738412 | 0.0692615877 | 0.163720891 | 0.346089681 | 0.542503159 |
| Corrected refit | continuous | 0.0177841644 | 0.5 | 25 | 0.00889208221 | 0.0277258872 | 0.320714073 | 0.274369301 | 0.725630699 | 0.0747194185 | 0.148160403 | 0.213793308 |
| Corrected refit | continuous | 0.0177841644 | 0.5 | 50 | 0.00889208221 | 0.0138629436 | 0.641428145 | 0.473460089 | 0.526539911 | 0.0796787748 | 0.171277528 | 0.274369301 |
| Corrected refit | continuous | 0.0177841644 | 0.5 | 100 | 0.00889208221 | 0.00693147181 | 1.28285629 | 0.722755722 | 0.277244278 | 0.082322308 | 0.184624907 | 0.313219064 |
| Corrected refit | continuous | 0.0177841644 | 0.75 | 25 | 0.0133381233 | 0.0277258872 | 0.481071109 | 0.381879038 | 0.618120962 | 0.109958675 | 0.213793308 | 0.302883914 |
| Corrected refit | continuous | 0.0177841644 | 0.75 | 50 | 0.0133381233 | 0.0138629436 | 0.962142218 | 0.617926476 | 0.382073524 | 0.117104797 | 0.245579166 | 0.381879038 |
| Corrected refit | continuous | 0.0177841644 | 0.75 | 100 | 0.0133381233 | 0.00693147181 | 1.92428444 | 0.854019822 | 0.145980178 | 0.12090611 | 0.263731599 | 0.430849205 |
| Corrected refit | continuous | 0.0177841644 | 1 | 25 | 0.0177841644 | 0.0277258872 | 0.641428145 | 0.473460089 | 0.526539911 | 0.143855846 | 0.274369301 | 0.381879038 |
| Corrected refit | continuous | 0.0177841644 | 1 | 50 | 0.0177841644 | 0.0138629436 | 1.28285629 | 0.722755722 | 0.277244278 | 0.153008843 | 0.313219064 | 0.473460089 |
| Corrected refit | continuous | 0.0177841644 | 1 | 100 | 0.0177841644 | 0.00693147181 | 2.56571258 | 0.92313561 | 0.0768643898 | 0.157867654 | 0.335163457 | 0.528331946 |
| Corrected refit | 2004 | 0.0187106946 | 0.5 | 25 | 0.00935534729 | 0.0277258872 | 0.337422829 | 0.286392957 | 0.713607043 | 0.0784554362 | 0.155247348 | 0.223584234 |
| Corrected refit | 2004 | 0.0187106946 | 0.5 | 50 | 0.00935534729 | 0.0138629436 | 0.674845657 | 0.490764989 | 0.509235011 | 0.0836513736 | 0.1793493 | 0.286392957 |
| Corrected refit | 2004 | 0.0187106946 | 0.5 | 100 | 0.00935534729 | 0.00693147181 | 1.34969131 | 0.740679703 | 0.259320297 | 0.0864204184 | 0.193249418 | 0.326532429 |
| Corrected refit | 2004 | 0.0187106946 | 0.75 | 25 | 0.0140330209 | 0.0277258872 | 0.506134243 | 0.397178558 | 0.602821442 | 0.115343827 | 0.223584234 | 0.315865458 |
| Corrected refit | 2004 | 0.0187106946 | 0.75 | 50 | 0.0140330209 | 0.0138629436 | 1.01226849 | 0.63660631 | 0.36339369 | 0.122815195 | 0.256574392 | 0.397178558 |
| Corrected refit | 2004 | 0.0187106946 | 0.75 | 100 | 0.0140330209 | 0.00693147181 | 2.02453697 | 0.867945026 | 0.132054974 | 0.126788238 | 0.275382312 | 0.447318366 |
| Corrected refit | 2004 | 0.0187106946 | 1 | 25 | 0.0187106946 | 0.0277258872 | 0.674845657 | 0.490764989 | 0.509235011 | 0.150755617 | 0.286392957 | 0.397178558 |
| Corrected refit | 2004 | 0.0187106946 | 1 | 50 | 0.0187106946 | 0.0138629436 | 1.34969131 | 0.740679703 | 0.259320297 | 0.160305195 | 0.326532429 | 0.490764989 |
| Corrected refit | 2004 | 0.0187106946 | 1 | 100 | 0.0187106946 | 0.00693147181 | 2.69938263 | 0.932752984 | 0.0672470163 | 0.165372348 | 0.349153498 | 0.54644143 |
