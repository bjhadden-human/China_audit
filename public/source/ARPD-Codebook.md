# ARPD codebook text (October 2019, v1.0)

Plain-text extraction of `ARPD-Codebook.pdf`, one section per PDF page.

## Page 1

The Autocratic Ruling Parties Dataset
Codebook
Michael K. Miller
October 2019
Note: This codebook gives further detail on the dataset described in “The Autocratic Ruling
Parties Dataset: Origins, Durability, and Death” inJournal of Conﬂict Resolution. Please cite
the article when using the data. This is Version 1.0 of the data, which will be periodically
updated. The dataset can be found atJCR’s online repository and my personal website at
sites.google.com/site/mkmtwo/data.
Overview and Sample
The Autocratic Ruling Parties Dataset (ARPD) includes a range of variables for all auto-
cratic ruling parties in the world from 1940–2015, covering 279 autocratic ruling party spells
(with 262 unique parties).1 Although non-party autocracies are not the focus, I include them
in the dataset for clarity. As a result, the data covers 479 total autocratic regime spells. This
correspondsto156countries(includingmicrostates)and133countrieswithatleastoneruling
party spell.
Two versions of ARPD are available: one with parties as the unit of analysis and one in
country-year format. The country-year version includes 6,536 observations. With a few excep-
Associate Professor of Political Science and International Aﬀairs,George Washington Univer-
sity. Send all correspondence (including proposed corrections to the data) to mkm2@gwu.edu.
I thank Aleksandr Fisher for valuable research assistance in preparing this dataset.
1 Sixteen parties had multiple spells in power, including one with three (Guinea-Bissau’s
PAIGC). This includes some parties ruling in two distinct countries (e.g., the Kuomintang for
China and Taiwan).
1

## Page 2

tions, the variables are the same in both. In addition, each type is available in multiple ﬁle
formats.
The sample includes any ruling party that had power between 1940 and 2015 within an
autocracy,withautocracydeﬁnedusingBoixetal.’s(2013)mostrecentupdate. 2 Arulingparty
isdeﬁnedasapoliticalpartythatiseitherthesupremerulingpowerorisusedasasigniﬁcant
vehicle of power by the regime and is clearly preeminent among all parties. Where there is
any ambiguity, special attention is placed on parties of the executive. The sample therefore
includes military regimes, monarchies, and personalistic regimes, as long as the rulers rely to
ameaningfuldegreeonaspeciﬁcparty.Caseswheretherearemultiplepartiesinalegislature
orlower-levelgovernment,ﬂuidcompetition,andlittletonorelianceonpartiesbyamonarchor
military dictator (e.g., modern Morocco, Japan in the 1930s) are not included. Parties founded
to compete in democratizing elections and parties of the executive in caretaker governments
before a democratic transition are also not counted.
The dataset tracks continuous party spells in power. A breakdown is recorded if there is a
transferofpowertoadistinctparty,atransitiontoanon-partyautocraticregime,ordemocra-
tization.Majorsplitsandmergersaretreatedasbreakdowns,butnotchangesinname,policy,
or when a ruling party absorbs a small party without fundamental change (e.g., the Workers’
Party of North Korea’s merger with its outlawed South Korean sibling in 1949). Where any
change occurred, the cases were checked to ensure the same organization and power structure
remained in place.
Each year in each autocracy is assigned to a ruling party or non-party government. If a
transition occurs, the regime at the year’s end is generally applied to that year. However, if
a party gains power, rules for most of the year, then loses power before the year’s end, the
year is assigned to that party to avoid omitting it entirely. In addition, if a party loses power
and there’s a short non-party transitional spell crossing into the following year, the year is
assigned to the party rather than a non-party interruption. Autocratic years without a party
are included with missing values for party characteristics and indicators for the predominant
form of regime during the period.
2 Boix,Carles,MichaelK.Miller,andSebastianRosato.2013.Acompletedatasetofpolitical
regimes, 1800–2007.Comparative Political Studies46(12): 1523-54.
2

## Page 3

As listed below, each ruling party is coded for several characteristics, including its origin,
tenure, and electoral success after democratization. The dataset is based on case studies of
each party’s history. A selected list of sources is included at the end. Country-speciﬁc sources
weresupplementedbyvariousgeneralresources,includingWikipedia, countrystudies.us,
and worldstatesmen.org, especially to conﬁrm founding and party tenure dates.
Variables
I now list the variables in ARPD. The variable names in the R/text and Stata formats are
given in square brackets. In the spreadsheet format, the columns have descriptive titles. Two
variables are included only in the country-year version. Summary statistics are in Table 1.
Country Name [Country]
COW Country Code [ccode]
Year [Year]
Note: This is included in thecountry-year version only.
Party Regime Indicator [Party_Regime]
This is 1 if the country has an autocratic ruling party and 0 otherwise. This is 1 for 58.2% of
the dataset’s party-level version and 67.3% of the country-year version.
Party Name [Party]
This is translated into English where possible. If the party’s name changes during its spell
in power, all names are listed with a / separating distinct names in chronological order. A
separate variable indicates the years the name changed. In ﬁve cases, the same party name
was used by distinct parties in diﬀerent countries (e.g., the People’s Democratic Party); these
are distinguished by the country’s name in square brackets. Note: The names are complete in
the R/text and Spreadsheet version, but abbreviated/corrupted in the Stata version.
3

## Page 4

Year Party Founded [Year_Founded]
Thisistheyearthepartywasfounded,withtherequirementofadirectinstitutionallinkageto
the ruling party. Some parties grew out of distinct types of groups, such as the Kuomintang’s
roots in an anti-monarchist society, but this dates the founding to the establishment as an
organized political party.
Party Age Since Founding [Party_Age]
Years since party founding. Note: This is included in thecountry-year version only.
Year Party Gained Power [Year_in_Power]
Last Year Party in Power [Last_Year_of_Power]
These two variables indicate the beginning and end years of the party spell. The end year is
generally the lastfull year of power, so the year of transition is the following year. If the party
is still in power at the end of 2015, the last year in power is coded as N. The country-year
dataset includes all of the party’s years in power, with these two variables ﬁxed.
Type of Power Change (Following Year) [Power_Change]
For the party-level dataset, this indicates what followed the party’s tenure, with the following
options: 0 = Still in power (at end of 2015), 1 = Transition to another ruling-party regime, 2 =
Transitiontoanon-partyautocracy,and3=Accessiontodemocracy.Casesinwhichdemocracy
follows the next year, but this was forced by an intervening power, are counted as group 2.
However,researcherscanuseothervariablestorecodethis.Forthecountry-yearversion,each
year is coded separately, indicating what followed the next year, with 0 indicating no change.
Competition [Competition]
This records by year whether the ruling party allowed multiparty competition for national
oﬃce. For the country-year dataset, this is 0 or 1 and can change within a spell. For the party-
4

## Page 5

level dataset, a 0 or 1 indicates that value for the whole spell. A positive year indicates compe-
tition was allowed starting that year. A negative year indicates competition ended that year.
Some entries combine such years (e.g., “-1981, 1992”) for multiple changes. For comparison,
this agrees with Cheibub et al.’s (2010) coding for multiple parties (de facto) in 85.7% of over-
lapping country-years.3
Party Origin [Origin]
This indicates the founding origin of the party, with the following categories:Dictator-Created
(by a sitting dictator),Revolution (organized as a violent revolutionary organization),Inde-
pendence (organized as a non-revolutionary, pro-independence organization),Communist (or-
ganized as Communist with international involvement from the Communist International),
Military (created by the military leadership, usually to represent it),Elite Coalition(founded
by non-executive elites to compete in politics, possibly in a prior regime or under colonial-
ism), Merger or Split (from previous parties/party), andDictator-Created/Mergeror Dictator-
Created/Split (forced merger or split by a sitting dictator).
How Party Gained Power [How_Power_Gained]
Thisindicateshowthepartyrosetopower,withthefollowingcategories: Dictator-Created(new
partyimposedbyasittingdictator), Dictator-Supported(dictatoranointsapre-existingparty),
Military (imposed by the military leadership),Revolution (party leads an armed takeover of
thestate), Election(partywinsanelection,possiblyuncompetitive), Coup(partyleadsacoup),
Communist-Imposed(imposed by Communists/Soviets), andForeign-Imposed(party installed
by a non-Communist foreign power). Note that the Communist-Imposed category does not in-
clude Communist parties, such as in China and the Soviet Union, that rose to power through
primarily domestic means. Five cases are coded as hybrids of these categories.
3 Cheibub, José Antonio, Jennifer Gandhi, and James Raymond Vreeland. 2010. Democracy
and dictatorship revisited.Public Choice143: 67-101.
5

## Page 6

How Party Lost Power [How_Power_Ended]
This indicates how the party lost power at the current spell’s end, with the following cate-
gories:Coup,Revolution,CivilWar (party’sendcoincides withaprolongedbreakdownofstate
authority), Protests(ousted by a popular protest movement),Election (party loses a contested
election), Dictator-Supported(sitting dictator switches support to a possibly new alternative
party), Occupation (foreign power ousts the party as part of an armed takeover of the state),
Split or Merger, Country Merger (used for South Yemen when the country merged to form
Yemen),Continued(spellendswithdemocratizationoracountrychangebutthepartyretains
power), andStill in Power(party is in power at the end of 2015). 17 cases are hybrids of two
categories, with 14 of these combining protests and an election.
Democracy Follows Party Spell [Democracy_Year_After]
This indicates whether democracy followed the year after the party’s spell in power. This is 0
in non-ﬁnal years for the country-year dataset.
Party Accedes to Democracy [Accession_to_Democracy]
This indicates whether the party acceded to democracy rather than ﬁrst being overthrown.
This can only be 1 if the previous variable is 1. If desired, this and the previous variable can
be used to recode the variable on what followed the party’s tenure.
Party Rule from Independence [Power_from_Independence]
This indicates whether the party has held power in the current spell continuously since the
country’s independence.
Party Renaming [Renaming]
This lists years (if any) that the ruling party’s name was changed. There are 45 name changes
(across 36 parties) that do not correspond to shifts in party control.
6

## Page 7

Party Evolution from Preceding Party [Evolution]
This indicates the party was founded by a continuing coalition from the previous party. Since
this was judged as more than a name change, this is treated as a new party spell, but the
variable allows researchers to code this diﬀerently. There are 19 occurrences of this in the
data, such as Juan Peron’s shift from the Labour Party to the Justicialist Party in 1947.
Party Marxist [Marxist]
This indicates whether the party is Communist, Marxist-Leninist, or radical socialist. This
does not include all left-leaning parties.
Military Regime [Military]
Monarchy [Monarchy]
Violence [Violence]
Occupation [Occupation]
Competitive Authoritarian [Compet_Auth]
These ﬁve categories are dummy variables that only apply to the non-party regimes. They in-
dicate the predominant regime type during the given spell and thus are ﬁxed in both datasets.
Non-party regimes can also satisfy multiple categories or none. Although this may be use-
ful to see what followed or preceded party regimes, I do not recommend using this to replace
country-year datasets on regime types.
Competitive Authoritarian Parties [Compet_Parties]
For competitive authoriatian regimes, this lists some of the major electoral parties. None are
referenced in the remaining data.
7

## Page 8

Future Democracy Only
The following variables are only coded if the country democratizes after the ruling party’s
spell and by 2015. Again, democracy is deﬁned by Boix et al. (2013). This speciﬁc data was
initially collected for the paper “Don’t Call It a Comeback: Autocratic Ruling Parties after
Democratization” in theBritish Journal of Political Science. For recording parties’ electoral
resultswithindemocracy,partiesarestillcountediftheybecomealteredthroughminormerg-
ers and splits, but not if they split into several pieces or are absorbed into a larger coalition as
a junior partner.
Last Party Before Democracy [Last_Before_Dem]
This indicates whether the party is the last ruling party in the autocracy spell before democ-
racy. Parties that are not last are much less likely to regain power in democracy.
Next Democratic Year [Next_Dem_Year]
This indicates the closest year of democratization following the party spell.
Party Remains in Democracy [Dem_Remains]
This indicates whether the party remains as an active political party at any point in the fol-
lowing democratic spell.
Party Competitive in Democracy [Dem_Competitive]
This indicates whether the party remains a nationally competitive political party at any point
in the following democratic spell. Generally, I use a threshold of 10% of legislative seats or the
presidential vote, but parties slightly under this that join national cabinets are counted.
8

## Page 9

Party in Power in Democracy [Dem_Power]
This indicates whether the party has a legislative plurality or control of the executive at any
point in the following democratic spell. Cases in power only due to power-sharing agreements
or caretaker executive or not counted.
Party Remains in Any Future Democracy [Dem_Remains_Any]
Party Competitive in Any Future Democracy [Dem_Competitive_Any]
Party in Power in Any Future Democracy [Dem_Power_Any]
Thesethreevariablesarethesameasthepriorthree,butcountanyfuturedemocracy,notjust
the following democratic spell.
Years Party Remains in Democracy [Dem_Years_Remains]
Years Party Competitive in Democracy [Dem_Years_Competitive]
Years Party in Power in Democracy [Dem_Years_Power]
Each variable lists the years that the ruling party satisﬁes the condition inanyfuture democ-
racy.
Party Ally of Military [Military_Ally]
For the last ruling parties before democracy, this indicates whether the party was a military
ally.
Party Style of Governance [Governance]
For the last ruling parties before democracy, this indicates the party’s style of governance.
Three broad styles are counted:Clientelist, Policy-Based, and Repressive. The variable also
allows for combinations of two of these.
9

## Page 10

Party Favors Ethnic or Other Group [Favors_Ethnic]
Note: Additional clariﬁcation was added to this description, October 2019.
Forall partieswith afuturedemocracy, thisindicates whethertheparty substantiallyfavored
aspeciﬁcethnicgroup(orotherascriptivecategorylikeareligiousorlinguisticgroup)through
exclusive or near-exclusive access to state resources or positions, signiﬁcant population-wide
repressiontargetedatrivalascriptivegroups(outsideofpoliticalopposition),ortheadoptionof
group-deﬁned legal inequalities. Generally, nationalist projects are not suﬃcient unless they
satisfy one of these requirements.
10

## Page 11

Table 1:Summary Statistics
Distinct Mean Mean
Variable Values (Parties) (Country-Year)
All parties (279 spells)
Party Name 262
Party Name Changes Years
Party Founding Year Years 1960.57
Year in Power Years 1971.41
Year Out of Power Years 1979.88
Party Duration 57 15.77 17 .35
Party Origin 10
How Party Gained Power 12
How Party Lost Power 15
Regime Change 4
Party Rule from Independence 2 0.251 0 .343
Party Marxist 2 0.244 0 .367
Competition 2 0.706 0 .462
Coalition Evolution 2 0.067
Parties followed by democracy (134 parties)
Party Survives in Democracy Years 0.612 0 .682
Party Competitive in Democracy Years 0.470 0 .564
Party in Power in Democracy Years 0.328 0 .314
Party Favors Ethnicity 2 0.224
Party Military Ally 2 0.881
Party Governing Strategy 6
Notes: The dataset covers all autocratic ruling parties from 1940–2015. Sev-
eral of the included variables are listed, with the top set covering all party
spells and the bottom set limited to parties in countries that later democra-
tized. For the latter, year ranges are included for party survival, competitive-
ness, and power within democracy. Means are shown for numerical variables,
with the average either taken over parties or their ruling country-years (ex-
ceptthedemocraticoutcomevariables,whichareaveragedovercountry-years
in the following democratic spell). The dataset includes non-party autocratic
spells, with information on regime type and competitive oligarchy.
11

## Page 12

12 
 
Selected Source List for Autocratic Ruling Parties Dataset 
 
Several Cases 
 
Bethell, Leslie (ed.). 1994. The Cambridge History of Latin America: Latin America since 1930 . Cambridge, 
Cambridge University Press. 
 
Bratton, Michael, and Nicolas van de Walle. 1997. Democratic Experiments in Africa: Regime Transitions in 
Comparative Perspective. Cambridge, Cambridge University Press. 
 
Cahoon, Ben. 2018. Worldstatesmen.org. Accessed at: worldstatesmen.org  
 
Collier, Ruth Berins. 1999. Paths Toward Democracy: The Working Class and Elites in Western Europe and South 
America. Cambridge, Cambridge University Press. 
 
Diamond, Larry, Juan J. Linz, and Seymour M. Lipset. 1988. Democracy in Developing Countries  (Volumes 1-4). 
Boulder, Lynne Rienner Publishers. 
 
Domínguez, Jorge I., and Marc Lindenberg (eds.). 1997. Democratic Transitions in Central America . University 
Press of Florida. 
 
Friedman, Edward, and Joseph Wong (eds.). 2008. Political Transitions in Dominant Party Systems: Learning to 
Lose. New York, Routledge. 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Murphey, Rhoads. 2014. A History of Asia (Seventh Edition). New York, Routledge. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook. Oxford, Oxford University Press 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann  (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann  (eds.). 2001 . Elections in  Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
PDBA. 2018. Political Database of the Americas . Georgetown University, Center for Latin American Studies . 
Accessed at: pdba.georgetown.edu 
 
Various authors. Country Studies/Area Handbook Series. Accessed at: countrystudies.us 
 
Afghanistan 
 
Barfield, Thomas. 2010. Afghanistan: A Cultural and Political History. Princeton, Princeton University Press. 
 
Rasanayagam, Angelo. 2005. Afghanistan: A Modern History. IB Tauris.

## Page 13

13 
 
Albania 
 
Biberaj, Elez. 1999. Albania in Transition: The Rocky Road to Democracy. Westview Press. 
 
De Waal, Clarissa. 2005. Albania Today: A Portrait of Post-Communist Turbulence. London, I.B. Tauris. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Algeria 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Stora, Benjamin. 2001. Algeria, 1830-2000: A Short History. Ithaca, Cornell University Press. 
 
Antigua 
 
Lewis, Patsy. 2002. Surviving Small Size: Regional Integration in Caribbean Ministates . University of West Indies 
Press. 
 
Political Database of the Americas . 2018. Antigua & Barbuda: Election Results . Georgetown University, Center for 
Latin American Studies. 
 
Argentina 
 
Lewis, Paul H. 2002. Guerrillas and Generals: The “Dirty War” in Argentina. Westport, CT, Praeger Publishers. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Rock, David. 1987. Argentina, 1516-1987: From Spanish Colonization to Alphonsín. Berkeley, University of 
California Press. 
 
Smith, Peter H. 1974. Argentina and the Failure of Democracy: Conflict Among Political Elites, 1904 -1955. 
Madison, University of Wisconsin Press. 
 
Armenia 
 
Payaslian, Simon. 2008. The History of Armenia: From the Origins to the Present. Springer. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Austria 
 
Keyserlingk, Robert H. 1988. Austria in World War II: An Anglo -American Dilemma . Montreal, McGill -Queen’s 
University Press. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Solsten, Eric (ed.). 1994. Austria: A Country Study. Washington, DC, Library of Congress. 
 
Azerbaijan 
 
Bolukbasi, Suha. 2013. Azerbaijan: A Political History. IB Tauris.

## Page 14

14 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Bangladesh 
 
Kabir, B huian M.M. 1999 . Politics of Military Rule and the Dilemmas of Democratization in Bangladesh . South 
Asian Publishers. 
 
Khan, Mohammad Mohabbat , and Syed Anwar  Husain. 1996. Process of democratization in Bangladesh. 
Contemporary South Asia 5(3): 319-34. 
 
Benin 
 
Allen, C hris. 1992 . ‘Goodbye to all that’: The short and sad story of socialism in Benin. Journal of  Communist 
Studies and Transition Politics 8(2): 63-81. 
 
Allen, Chris. 1992. Restructuring an authoritarian state: ‘Democratic renewal’ in Benin. Review of African Political 
Economy 19(54): 42-58. 
 
Creevey, Lucy , Paul Ngomo, and Richard Vengroff. 2005 . Party politics and different paths to democratic 
transitions: A comparison of Benin and Senegal. Party Politics 11(4): 471-93. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Riedl, Rachel B. 2014. Authoritarian Origins of Democracy Party Systems in Africa . Cambridge, Cambridge 
University Press. 
 
Bolivia 
 
Dunkerley, James. 1984. Rebellion in the Veins: Political Struggle in Bolivia, 1952-1982. Verso Books. 
 
Hudson, Rex A., and Dennis M. Hanratty. 1989. Bolivia: A Country Study. Library of Congress, Federal Research 
Division.  
 
Klein, Herbert S. 2003/2011. A Concise History of Bolivia (2nd edition). Cambridge, Cambridge University Press. 
 
Malloy, James M., and Eduardo Gamarra. 1988. Revolution and Reaction: Bolivia, 1964-1985. Transaction Books. 
 
Brazil 
 
Mainwaring, S cott. 1999 . Rethinking Party Systems in the Third Wave of Democratization: The Case of Brazil . 
Stanford University Press. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Share, Donald, and Scott Mainwaring. 1986 . Transitions through transaction: Democratization in Brazil and Spain.  
Dados-revista De Ciencias Sociais 29(2): 207-36. 
 
Bulgaria 
 
Bell, John D. 1997 . Democratization and political participation in ‘postcommunist’ Bulgaria.  In: Politics, Power, 
and the Struggle for Democracy in South -East Europe , eds. Karen Dawisha and Bruce Parrott. Cambridge, 
Cambridge University Press, pp.353-402.

## Page 15

15 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Vassilev, Rossen. 1999. Modernization theory revisited: The case of Bulgaria. East European Politics and  Societies 
13(3): 566-99. 
 
Waller, M ichael. 1995. Making and breaking: F actions in the process of party formation in Bulgaria. 
Democratization 2(1): 152-67. 
 
Burkina Faso 
 
Englebert, Pierre. 2018. Burkina Faso: Unsteady Statehood in West Africa. New York, Routledge. 
 
Rupley, Lawrence, Lamissa Bangali, and Boureima Diamitani. 2013. Historical Dictionary of Burkina Faso. 
Scarecrow Press. 
 
Burundi 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thiba ut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Reyntjens, F ilip. 2005. Briefing: Burundi: A  peaceful transition after a decade of war? African Affairs  105(418): 
117-35. 
 
Vandeginste, Stef. 2009. Power-sharing, conflict and transition in Burundi: T wenty years of trial and error. Africa 
Spectrum 44(3): 63-86. 
 
Cambodia 
 
Corfield, Justin. 2009. The History of Cambodia. ABC-CLIO. 
 
Murphey, Rhoads. 2014. A History of Asia (Seventh Edition). New York, Routledge. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Cameroon 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Cape Verde 
 
Meyns, Peter. 2002. Cape Verde: An African exception. Journal of Democracy 13(3): 153-65. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Silva Andrade, Elisa. 2002. Cape Verde. In: A History of Postcolonial Lusophone Africa , ed. Patrick Chabal. 
Bloomington, Indiana University Press, pp.264-90. 
 
Central African Republic 
 
Kalck, Pierre. 2005. Historical Dictionary of the Central African Republic. Scarecrow Press.

## Page 16

16 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Chad 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
China 
 
Dickson, Bruce J. 1997. Democratization in China and Taiwan: The Adaptability of Leninist Parties . Oxford, 
Oxford University Press. 
 
Nohlen, Dieter, Florian Grotz, and Christof Hartmann (eds.). 2001. Elections in Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
Priestland, David. 2009. The Red Flag: A History of Communism. New York, Grove Press. 
 
Colombia 
 
Mainwaring, Scott, and Timothy R. Scully ( eds.). (1995). Building Democratic Institutions: Party Systems in Latin 
America. Stanford University Press. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Roldán, Mary. 2002. Blood and Fire: La Violencia in Antioquia, Colombia, 1946 -1953. Durham, Duke University 
Press. 
 
Comoros 
 
Griffin, Michael. 1988. The politics of isolation. Africa Report 33(1): 52. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Congos 
 
Edgerton, Robert. 2002. The Troubled Heart of Africa: A History of the Congo. London, Macmillan. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press.  
 
Nzongola-Ntalaja, Georges. 2002. The Congo: From Leopold to Kabila: A People's History. Zed Books.  
 
Costa Rica 
 
Booth, John A. 1999. Costa Rica: Quest for Democracy. Boulder, Westview Press.

## Page 17

17 
 
Lehoucq, Fabrice Edouard. 1991. Class conflict, political crisis and the breakdown of democratic practices in Costa 
Rica: Reassessing the origins of the 1948 Civil War. Journal of Latin American Studies 23(1): 37-60. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Yashar, Deborah J. 1997. Demanding Democracy: Reform and Reaction in Costa Rica and Guatemala, 1870s -
1950s. Stanford University Press. 
 
Croatia 
 
Cohen, Lenard J. 1997. Embattled democracy: P ostcommunist Croatia in transition.  In: Politics, Power, and the 
Struggle for Democracy in South -East Europe , eds. Karen Dawisha and Bruce Parrott. Cambridge, Cambridge 
University Press, pp.69-121. 
 
Finlan, Alastair. 2004. The Collapse of Yugoslavia, 1991-1999. Oxford, Osprey Publishing. 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Cuba 
 
Gott, Richard. 2005. Cuba: A New History. New Haven, Yale University Press. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook. Oxford, Oxford University Press 
 
Priestland, David. 2009. The Red Flag: A History of Communism. New York, Grove Press. 
 
Cyprus 
 
Ker-Lindsay, James. 2011. The Cyprus Problem: What Everyone Needs to Know. Oxford, Oxford University Press. 
 
Mayes, Stanley. 1981. Makarios: A Biography. London, Macmillan. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Czechoslovakia 
 
Grzymala-Busse, Anna M. 2002. Redeeming the Communist Past: The Regeneration of Communist Parties in East 
Central Europe. Cambridge, Cambridge University Press. 
 
Huntington, Samuel P. 1991 . The Third Wave: Democratization in the Late Twentieth Century . Norman, University 
of Oklahoma Press. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Olson, David M. 1993 . Dissolution of the state: Political parties and the 1992 election in Czechoslovakia. 
Communist and Post-Communist Studies 26(3): 301-14. 
 
Wolchik, Sharon L. 1991 . Czechoslovakia in Transition: Politics, Economics an d Society . London, Pinter 
Publishers.

## Page 18

18 
 
Djibouti 
 
BBC News. 2018. Djibouti country profile. Located at: www.bbc.com/news/world -africa-13231761. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Dominican Republic 
 
Bethell, Leslie (ed.). 1994. The Cambridge History of Latin America: Latin America since 1930 . Cambridge, 
Cambridge University Press. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook. Oxford, Oxford University Press 
 
Ecuador 
 
Becker, Marc. 2013. Ecuador: Indigenous struggles and the ambiguities of power.  In: The New Latin American Left: 
Cracks in the Empire, eds. Jeffery R. Webber and Barry Carr. New York, Rowman & Littlefield, pp.213-32. 
 
De la Torre, C arlos. 1997. Populism and democracy: Political discourses and cultures in contemporary Ecuador. 
Latin American Perspectives 24(3): 12-24. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Egypt 
 
Brownlee, Jason. 2007. Authoritarianism in an Age of Democratization. Cambridge, Cambridge University Press. 
 
Landau, Jacob M. 2015. Parliaments and Parties in Egypt. New York, Routledge. 
 
El Salvador 
 
Ardón, Patricia. 1999. Post-War Reconstruction in Central America: Lessons from El Salvador, Guatemala, and 
Nicaragua. Oxfam GB. 
 
Holiday, David, and William  Stanley. 1993. Building the peace: Preliminary lessons from El Salvador. Journal of 
International Affairs 46(2): 415-38.  
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Wood, Elizabeth J. 2000 . Forging Democracy from Below: Insurgent Transitions in South Africa and El Salvador. 
Cambridge, Cambridge University Press. 
 
Equatorial Guinea 
 
Bratton, Michael, and Nicolas van de Walle. 1997. Democratic Experiments in Africa: Regime Transitions in 
Comparative Perspective. Cambridge, Cambridge University Press. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Eritrea/Ethiopia 
 
Marcus, Harold G. 2002. A History of Ethiopia. Berkeley, University of California Press.

## Page 19

19 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Zewde, Bahru. 2002. A History of Modern Ethiopia, 1855-1991. Ohio University Press. 
 
Fiji 
 
Lal, Brij V. 1992. Broken Waves: A History of the Fiji Islands in the Twentieth Century . Manoa, University of 
Hawaii Press. 
 
Lal, Brij V. 2014. In Frank Bainimarama’s shadow: Fiji, elections and the future. Journal of Pacific History  49(4): 
457-68. 
 
Madraiwiwi, Joni. 2015. The Fijian elections of 2014: Returning to democracy…? Journal of Pacific History 50(1): 
54-60. 
 
Gabon 
 
Aicardi De Saint-Paul, Marc. 1989. Gabon: The Development of a Nation. New York, Routledge. 
 
Meredith, Martin. 2011. The Fate of Africa: A History of the Continent Since Independence (revised ed.). New York, 
PublicAffairs. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Gambia 
 
Bratton, Michael, and Nicolas van de Walle. 1997. Democratic Experiments in Africa: Regime Transitions in 
Comparative Perspective. Cambridge, Cambridge University Press. 
 
Meredith, Martin. 2011. The Fate of Africa: A History of the Continent Since Independence (revised ed.). New York, 
PublicAffairs. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Georgia 
 
Fairbanks, Charles H. 2004. Georgia’s Rose Revolution. Journal of Democracy 15(2): 110-24. 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Germany/East Germany 
 
Merriman, John. 2009. A History of Modern Europe: From the Renaissance to the Present, Vol. 1 . W.W. Norton & 
Company. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Priestland, David. 2009. The Red Flag: A History of Communism. New York, Grove Press. 
 
Solsten, Eric (ed.). 1995. Germany: A Country Study. Washington, DC, Library of Congress.

## Page 20

20 
 
Ghana 
 
Owusu, M axwell. 1996. Tradition and transformation: Democracy and the politics of popular power in Ghana. 
Journal of Modern African Studies 34(2): 307-43. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Pinkney, Robert. 1997. Democracy and Dictatorship in Ghana and Tanzania. London, Macmillan. 
 
Riedl, Rachel B. 2014. Authoritarian Origins of Democracy Party Systems in Africa . Cambridge, Cambridge 
University Press. 
 
Grenada 
 
Meditz, Sandra W., and Dennis M. Hanratty (eds.). 1987. Caribbean Islands: A Country Study . Washington, DC, 
Library of Congress. 
 
Schoenhals, Kai P., and Richard A. Melanson. 1985. Revolution and Intervention in Grenada: The New Jewel 
Movement, the United States, and the Caribbean. Westview Press. 
 
Guatemala 
 
Gleijeses, Piero. 1991 . Shattered Hope: The Guatemalan Revolutio n and the United States, 1944 -1954. Princeton, 
Princeton University Press.  
 
Handy, Jim. 1986 . Resurgent democracy and the Guatemalan military. Journal of Latin American Studies  18(2): 
383-408. 
 
Leonard, Thomas M. 1984. The United States and Central America, 1944-1949: Perceptions of Political Dynamics . 
Tuscaloosa, The University of Alabama Press. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Schirmer, Jennifer G. 1998. The Guatemalan Military Project: A Violence Called Democracy . Philadelphia, 
University of Pennsylvania Press. 
 
Guinea 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
O’Toole, Thomas, and Janice E. Baker. 2005. Historical Dictionary of Guinea. Scarecrow Press. 
 
Guinea-Bissau 
 
Baker, B ruce. 1998 . The class of 1990: How have the autocratic leaders of sub -Saharan Africa fared under 
democratisation? Third World Quarterly 19(1): 115-27.  
 
Forrest, Joshua B. 1987. Guinea -Bissau since independence: A decade of domestic power struggles. Journal of 
Modern African Studies 25(1): 95-116. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections i n Africa: A Data Handbook . 
Oxford, Oxford University Press.

## Page 21

21 
 
Rudebeck, L ars. 2001. On Democracy’ s Sustainability: Transition in Guinea -Bissau. Swedish International 
Development Cooperation Agency. 
 
Temudo, Marina Padrão. 2008. From ‘people’ s struggle’to ‘this war of today’: Entanglements of peace and conflict 
in Guinea-Bissau. Africa 78(2): 245-63. 
 
Guyana 
 
Hinds, David. 2011. Ethno-politics and Power Sharing in Guyana: History and Discourse . New Academia 
Publishing, LLC. 
 
Ishmael, Odeen. 2013. The Guyana Story: From Earliest Times to Independence. Xlibris Corporation. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Singh, Chaitram. 2008. Re -democratization in Guyana and Suriname: Critical comparisons. European Review of 
Latin American and Caribbean Studies 84: 71-85. 
 
Haiti 
 
Coupeau, Steeve. 2008. The History of Haiti. Westport, CT, Greenwood Publishing Group. 
 
Dubois, Laurent. 2012. Haiti: The Aftershocks of History. Metropolitan Books. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Honduras 
 
Bethell, Leslie (ed.). 1994. The Cambridge History of Latin America: Latin America since 1930 . Cambridge, 
Cambridge University Press. 
 
Bowman, K irk. 2001. The public battles over militarisation and democracy in Honduras, 1954 -1963. Journal of 
Latin American Studies 33(3): 539-60. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Sieder, R achel. 1995 . Honduras: The politics of exception and military reformism (1972 -1978). Journal of Latin 
American Studies 27(1): 99-127. 
 
Hungary 
 
Bartlett, David L. 1997 . The Political Economy of Dual Transitions: Market Reform and Democratization in 
Hungary. Ann Arbor, University of Michigan Press. 
 
Grzymala-Busse, Anna M. 2002. Redeeming the Communist Past: The Regeneration of Communist Parties in East 
Central Europe. Cambridge, Cambridge University Press. 
 
Kaldor, M ary, and Ivan Vejvoda (eds.). 2002 . Democratization in Central and Eastern Europe . Bloomsbury 
Publishing. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press.

## Page 22

22 
 
Indonesia 
 
Ananta, Aris , Evi Nurvidya Arifin, and Leo  Suryadinata. 2005 . Emerging Democracy in Indonesia . Institute of 
Southeast Asian Studies.  
 
Benda, Harry J. 1964. Democracy in Indonesia. Journal of Asian Studies 23(3): 449-56.  
 
Crouch, Harold. 2000. Indonesia: Democratization and the threat of disintegration. Southeast Asian Affairs: 115-33. 
 
Honna, Jun. 2013. Military Politics and Democratization in Indonesia. London, Routledge. 
 
Tomsa, D irk. 2008 . Party Politics and Democratization in Indonesia: Golkar in the Post -Suharto Era . London, 
Routledge.  
 
Webber, D ouglas. 2006. A consolidated patrimonial democracy? Democratization in post -Suharto Indonesia. 
Democratization 13(3): 396-420. 
 
Iran 
 
Abrahamian, Ervand. 2008. A History of Modern Iran. Cambridge, Cambridge University Press. 
 
Gheissari, Ali, Vali Nasr, and Seyyed Vali Reza Nasr. 2009. Democracy in Iran: History and the Quest for Liberty . 
Oxford, Oxford University Press. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Iraq 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Tripp, Charles. 2002. A History of Iraq. Cambridge, Cambridge University Press. 
 
Italy 
 
Merriman, John. 2009. A History of Modern Europe: From the Renaissance to the Present, Vol. 1 . W.W. Norton & 
Company. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Pasquino, Gianfranco. 1986. The demise of the first fascist regime and Italy’s transition to democracy: 1943 -1948. 
In: Transitions from Authoritarian Rule: Southern Europe,  eds. Guillermo O’Donnell, Philippe Schmitter, and 
Laurence Whitehead. Baltimore, Johns Hopkins University Press, pp.45-70. 
 
Ivory Coast 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Zolberg, Aristide R. 2015. One-party Government in the Ivory Coast. Princeton, Princeton University Press. 
 
Kazakhstan 
 
Bowyer, Anthony Clive. 2008. Parliament and political parties in Kazakhstan . Working paper, Central Asia -
Caucasus Institute and Silk Road Studies Program, Johns Hopkins University - SAIS.

## Page 23

23 
 
Luong, Pauline Jones. 2002. Institutional Change and Political Continuity in Post -Soviet Central Asia: Power, 
Perceptions, and Pacts. Cambridge, Cambridge University Press. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in As ia and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Kenya 
 
Brown, S tephen. 2004. Theorising Kenya's protracted transition to democracy. Journal of Contemporary African 
Studies 22(3): 325-42. 
Murunga, Godwin R., and Shadrack W. Nasong'o (eds.). 2007. Kenya: The Struggle for Democracy. Zed Books. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Korea (North) 
 
Nohlen, Dieter, Florian Grotz, and Christof Hartmann (eds.). 2001. Elections in Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
Priestland, David. 2009. The Red Flag: A History of Communism. New York, Grove Press. 
 
Seth, Michael J. 2018. North Korea: A History. London, Red Globe Press. 
 
Korea (South) 
 
Han, Sungjoo. 1974. The Failure of Democracy in South Korea. Berkeley, University of California Press.  
 
Lee, Hong Yung. 1993. South Korea in 1992: A turning point in democratization. Asian Survey 33(1): 32-42.  
 
Nohlen, Dieter, Florian Grotz, and Christof Hartmann (eds.). 2001. Elections in Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
Sung-Joo, Han. 1988. South Korea in 1987: The politics of democratization. Asian Survey 28(1): 52-61. 
 
Kyrgyzstan 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid R egimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Luong, Pauline Jones. 2002. Institutional Change and Political Continuity in Post -Soviet Central Asia: Power, 
Perceptions, and Pacts. Cambridge, Cambridge University Press. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Laos 
 
Nohlen, Dieter, Florian Grotz, and Christof Hartmann (eds.). 2001. Elections in Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
Priestland, David. 2009. The Red Flag: A History of Communism. New York, Grove Press.

## Page 24

24 
 
Latvia 
 
Kaldor, M ary, and Ivan Vejvoda (eds.). 2002 . Democratization in Central and Eastern Europe . Bloomsbury 
Publishing. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press.  
 
Plakans, Andrejs. 1997. Democratization and political participation in postcommunist societies: the case of Latvia.  
In: The Consolidation of Democracy in East -Central Europe , eds. Karen Dawisha and Bruce Parrott. Cambridge, 
Cambridge University Press, pp.245-89. 
 
Lesotho 
 
Kabemba, Claude (ed.). 2003 . From Military Rule to Multiparty Democracy: Political Reforms and Challenges in 
Lesotho. Johannesburg, Electoral Institute of Southern Africa. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press.  
 
Venter, D enis. 2003. Democracy and multiparty politics in  Africa: R ecent elections in Zambia, Zimbabwe, and 
Lesotho. Eastern Africa Social Science Research Review 19(1): 1-39. 
 
Liberia 
 
Dennis, Peter. 2006. A brief history of Liberia. Working paper, International Center for Transitional Justice.  
 
Kumar, Krishna (ed.). 1998. Postconflict Elections, Democratization, and International Assistance . Boulder, Lynne 
Rienner. 
 
Lithuania 
 
Kaldor, M ary, and Ivan Vejvoda (eds.). 2002 . Democratization in Central and Eastern Europe . Bloomsbury 
Publishing. 
 
Krickus, Richard J. 1997 . Democratization in Lithuania. In: The Consolidation of Democracy in East -Central 
Europe, eds. Karen Dawisha and Bruce Parrott. Cambridge, Cambridge University Press, pp.291-331. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Madagascar 
 
Marcus, Richard R. 2004 . Political change in Madagascar: Populist democracy or neopatrimonialism by another 
name? Institute for Security Studies Papers. 
 
Marcus, Richard R., and Paul  Razafindrakoto. 2003 . Madagascar: A new democracy? Current History  102(664): 
215-21. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Malawi 
 
Englund, Harry (ed.). 2002 . A Democracy of Chameleons: Politics and Culture in the New Malawi . Nordic Africa 
Institute.

## Page 25

25 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Malaysia 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes Afte r the Cold War . 
Cambridge, Cambridge University Press. 
 
Means, Gordon P. 1996. Soft authoritarianism in Malaysia and Singapore. Journal of Democracy 7(4): 103-17. 
 
Pepinsky, Thomas B. 2007. Malaysia: Turnover without change. Journal of Democracy 18(1): 113-27. 
 
Pepinsky, Thomas B. 2009. Economic Crises and the Breakdown of Authoritarian Regimes: Indonesia and 
Malaysia in Comparative Perspective. Cambridge, Cambridge University Press. 
 
Maldives 
 
Bonofer, Jacob Ashik. 2010. The challenges of democracy in Maldives. International Journal of South Asian Studies 
3(2): 433-49. 
 
Robinson, John J. 2015. The Maldives: Islamic Republic, Tropical Autocracy. London, Hurst. 
 
Mali 
 
Bingen, R. James, David Robinson, and John M. Staatz (eds.). 2000. Democracy and Development in Mali. East 
Lansing, Michigan State University Press. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Wing, Susanna D. 2008. Constructing Democracy in Transitioning Societies of Africa: Constitutionalism and 
Deliberation in Mali. New York, Palgrave Macmillan. 
 
Mauritania 
 
Hochman, Dafna. 2007. Divergent democratization: The paths of Tunisia, Morocco and Ma uritania. Middle East 
Policy 14(4): 67-83. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Mexico 
 
Greene, Kenneth F. 2007. Why Dominant Parties Lose: Mexico's Democratization in Comparative Perspective . 
Cambridge, Cambridge University Press. 
 
Levitsky, Steven, and Lucan A. Way. 2010. Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Magaloni, Beatriz. 2006. Voting for Autocracy: Hegemonic Party Survival and its Demise in Mexico . Cambridge, 
Cambridge University Press. 
 
O’Neil, Shannon K. 2013. Mexico. In: Pathways to Freedom: Political and Economic Lessons from Democratic 
Transitions, eds. Isobel Coleman and Terra Lawson-Remer. New York, Council on Foreign Relations, pp.31-52.

## Page 26

26 
 
Mongolia  
 
Fish, M. Steven. 1998. Mongolia: Democracy without prerequisites. Journal of Democracy 9(3): 127-41. 
 
Fritz, Verena. 2002. Mongolia: Dependent democratization. Journal of Com munist Studies and Transition Politics  
18(4): 75-100. 
 
Fritz, Verena. 2008. Mongolia: The rise and travails of a deviant democracy. Democratization 15(4): 766-88. 
 
Mozambique 
 
Cabrita, João M. 2000. Mozambique: The Tortuous Road to Democracy. New York, Palgrave Macmillan. 
 
Manning, Carrie  L. 2002. The P olitics of Peace in Mozambique: Post -conflict Democratization, 1992 -2000. 
Greenwood Publishing Group. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Han dbook. 
Oxford, Oxford University Press. 
 
Myanmar 
 
Butwell, Richard, and Fred von der Mehden. 1960. The 1960 election in Burma. Pacific Affairs 33(2): 144-57.  
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Smith, Martin. 1991. Burma: Insurgency and the Politics of Ethnicity. Zed Books. 
 
Namibia 
 
Bauer, Gretchen. 1999. Challenges to democr atic consolidation in Namibia. In: State, Conflict, and Democracy in 
Africa, ed. Richard Joseph. Boulder, CO, Lynne Reiner, pp.429-48. 
 
Melber, Henning. 2014. Understanding Namibia. Oxford, Oxford University Press. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Nepal 
 
Hangen, Susan I. 2009. The Rise of Ethnic Politics in Nepal: Democracy in the Margins. London, Routledge. 
 
Murphey, Rhoads. 2014. A History of Asia (Seventh Edition). New York, Routledge. 
 
Nicaragua 
 
Ardón, Patricia. 1999. Post-War Reconstruction in Central America: Lessons from El Salvador, Guatemala, and 
Nicaragua. Oxfam GB. 
 
Close, David, Salvador Martí i Puig, and Shelley A. McConnell (eds.). 2012. The Sandinistas and Nicaragua Since 
1979. Boulder, Lynne Rienner. 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Williams, Philip J. 1994 . Dual transitions from authoritarian rule: Popular and electoral democracy in Nicaragua. 
Comparative Politics 26(2): 169-85.

## Page 27

27 
 
Niger 
 
Adejumobi, Said. 2000. Elections in Africa: A fading shadow of democracy? International Political Science Review 
21(1): 59-73. 
 
Davis, John Uniack, and Aboubacar B. Kossomi. 2001 . Niger gets back on track. Journal of Democracy  12(3): 80-
87.  
 
Di Lorenzo, Amanda, and Enrico  Sborgi. 2001. The 1999 presidential and legislative elections in Niger. Electoral 
Studies 20(3): 470-76. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Sandbrook, R ichard. 1996. Tran sitions without consolidation: D emocratization in six African cases.  Third World 
Quarterly 17(1): 69-88. 
 
Nigeria 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Peters, Jimi. 1997. The Nigerian Military and the State. London, I.B. Tauris. 
 
Sklar, Robert L. 2015. Nigerian Political Parties: Power in an Emergent African Nation. Princeton, Princeton 
University Press. 
 
Pakistan 
 
McGrath, Allen. 1996. The Destruction of Pakistan’s Democracy. Oxford, Oxford University Press. 
 
Nasr, Vali. 2004. Military rule, Islamism and democracy in Pakistan. Middle East Journal 58(2): 195-209. 
 
Shah, A qil. 2014 . Constraining consolidation: Military politics and democracy in Pakistan (2007 -2013). 
Democratization 21(6): 1007-33. 
 
Panama 
 
Domínguez, Jorge I., and Marc  Lindenberg (eds.). 1997 . Democratic Transitions in Central America . University 
Press of Florida. 
 
Furlong, William  L. 1993 . Panama: The difficult transition towards democracy. Journal o f Interamerican Studies 
and World Affairs 35(3): 19-64. 
 
Harding, Robert C. 2006. The History of Panama. Westport, CT, Greenwood Press. 
 
Major, John. 2003 . The United States Govern ment and the Panama Canal, 1903 -1979. Cambridge, Cambridge 
University Press.  
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Paraguay 
 
Bostrom, M ikael. 1994. Contagion of democracy in Latin America: The case of Paraguay. Latin American 
Development and Public Policy, ed. Stuart S. Nagel. London, Palgrave Macmillan, pp.186-213.

## Page 28

28 
 
Brun, Diego Abente. 1999. ‘People Power’ in Paraguay. Journal of Democracy 10(3): 93-100. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Peru 
 
Carrión, Julio F. (Ed.) 2006. The Fujimori Legacy: The Rise of Electoral Authoritarianism in Peru . Pennsylvania 
State University Press. 
 
Levitsky, Steven, and Maxwell A. Cameron. 2003. Democracy without parties? Political parties and regime change 
in Fujimori’s Peru. Latin American Politics and Society 45(3): 1-33. 
 
Masterson, Daniel M. 1991. Militarism and Politics in Latin America: Peru from Sánchez Cerro to Sendero 
Luminoso. Westport, CT, Greenwood Publishing Group. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Pike, Frederick B. 1967. The Modern History of Peru. Praeger Press.  
 
Philippines 
 
Franco, Jennifer Conroy. 2001. Elections and Democratization in the Philippines. New York, Routledge. 
 
Smith, Benjamin. 2005. Life of the party: The origins of regime breakdown and persistence under single -party rule. 
World Politics 57: 421-51. 
 
Thompson, Mark R. 2002. The Anti -Marcos Struggle: Personalistic Rule and Democratic Transition in the 
Philippines. New Haven, Yale University Press. 
 
Poland 
 
Castle, Marjorie, and Ray Taras. 2002. Democracy in Poland. Boulder, Westview Press. 
 
Grzymala-Busse, Anna M. 2002. Redeeming the Communist Past: The Regeneration of Communist Parties in East 
Central Europe. Cambridge, Cambridge University Press. 
 
Mahr, Alison, and John  Nagle. 1995 . Resurrection of the successor parties and democratization in East -Central 
Europe. Communist and Post-Communist Studies 28(4): 393-409. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Portugal 
 
Maxwell, Kenneth. 1995. The Making of Portuguese Democracy. Cambridge, Cambridge University Press. 
 
Schmitter, Philippe C. 1978. The impact and meaning of ‘non -competitive, non-free and insignificant’ elections in 
authoritarian Portugal, 1933 -74. In: Elections without Choice , eds. Guy Hermet, Richard Rose, and Alain Rouquié. 
New York, John Wiley & Sons, pp.145-68. 
 
Romania 
 
Kaldor, M ary, and Ivan Vejvoda (eds.). 2002 . Democratization in Central and Eastern Europe . Bloomsbury 
Publishing.

## Page 29

29 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Stan, Lavinia (ed.). 1997. Romania in Transition. Hanover, Dartmouth University Press. 
 
Weiner, R obert. 1997 . Democratization in Romania.  In: Romania in Transition , ed. Lavinia Stan.  Hanover, 
Dartmouth University Press, pp.3-23. 
 
Russia/USSR 
 
Levesque, Jacques. 1997. The Enigma of 1989: The USSR and the Liberation of Eastern Europe . Berkeley, 
University of California Press. 
 
Levitsky, Steven, and Lucan A. Way. 2010. Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Shevtsova, Lilia. 2010. Putin’s Russia. Washington, DC, Carnegie Endowment. 
 
Rwanda 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Prunier, Gérard. 1997. The Rwanda Crisis: History of a Genocide. New York, Columbia University Press. 
 
Reyntjens, Filip. 2011. Behind the façade of Rwanda’s elections. Georgetown Journal of International Affairs : 64-
69. 
 
Samoa 
 
Freedom House. 2013. Samoa country report. Freedom in the World 2013. Located at: freedomhouse.org. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in  Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
São Tomé and Príncipe 
 
Chabal, Patrick, and David Birmingham. 2002. A History of Postcolonial Lusophone Africa . Bloomington, Indiana 
University Press. 
 
Francisco, Albertino, and Nujoma Agostinho. 2011. Exorcising Devils from the Throne: São Tomé and Príncipe in 
the Chaos of Democratization. New York, Algora Publishing. 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Senegal 
 
Beck, Linda J. 2008. Brokering Democracy in Africa: The Rise of Clientelist De mocracy in Senegal . London, 
Palgrave Macmillan. 
 
Creevey, Lucy, Paul Ngomo, and Richard Vengroff. 2005. Party politics and different paths to democratic 
transitions: A comparison of Benin and Senegal. Party Politics 11(4): 471-93. 
 
Galvan, Dennis Charles. 2001. Political turnover and social change in Senegal. Journal of Democracy 12(3): 51-62.

## Page 30

30 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Riedl, Rachel B. 2014.  Authoritarian Origins of Democracy Party Systems in Africa . Cambridge, Cambridge 
University Press. 
 
Serbia/Yugoslavia 
 
Bunce, Valerie J., and Sharon L.  Wolchik. 2010. Defeating dictators: Electoral change and stability in competitive 
authoritarian regimes. World Politics 62(1): 43-86. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Thomas, Nigel, and Krunoslav Mikulan. 2006. The Yugoslav Wars (2): Bosnia, Kosovo And Macedonia 1992 -2001. 
Osprey Publishing. 
 
Seychelles 
 
Metz, Helen Chapin (ed.). 1994. Seychelles: A Country Study. Washington, DC, Library of Congress. 
 
Nohlen, Dieter , Michael Krennerich, and  Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Sierra Leone 
 
Gberie, Lansana. 2005. A Dirty War in West Africa: The RUF and the Destruction of Sierra Leone . Bloomington, 
IN, Indiana University Press. 
 
Hirsch, John L. 2001. Sierra Leone: Diamonds and the Struggle for Democracy. Boulder, Lynne Rienner. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Singapore 
 
Means, Gordon P. 1996. Soft authoritarianism in Malaysia and Singapore. Journal of Democracy 7(4): 103-17. 
 
Mutalib, Hussin. 2003. Parties and Politics: A Study of Opposition Parties and the PAP in Singapore . Singapore, 
Eastern Universities Press. 
 
Verweij, Marco, and Riccardo Pelizzo. 2009. Singapore: Does authoritarianism pay? Journal of Democracy 20(2): 
18-32. 
 
Solomon Islands 
 
The Commonwealth. 2018. Solomon Islands: History . Accessed at: thecommonwealth.org/our-member-
countries/ solomon-islands/history. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in  Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
Somalia 
 
Metz, Helen Chapin (ed.). 1992. Somalia: A Country Study. Washington, DC, Library of Congress.

## Page 31

31 
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
South Africa 
 
Alexander, Neville. 2003. An Ordinary Country: Issues in the Transition from Apartheid to Democracy in South 
Africa. Bergahn Books. 
 
Mattes, Robert B. 2002. South Africa: Democracy without the people? Journal of Democracy 13(1): 22-36.  
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Wood, Elizabeth J. 2000 . Forging Democracy from Below: Insurgent Transitions in South Africa and El Salvador . 
Cambridge, Cambridge University Press. 
 
Spain 
 
Grugel, Jean, and Tim Rees. 1997. Franco’s Spain. Arnold Press. 
 
Gunther, Richard, Giacomo Sani, and Goldie Shabad. 1988. Spain After Franco: The Making of a Competitive Party 
System. Berkeley, University of California Press. 
 
Nohlen, Dieter, and Philip Stöver. 2010. Elections in Europe: A Data Handbook. Oxford, Oxford University Press. 
 
Sri Lanka 
 
DeVotta, Neil. 2004. Sri Lanka: Ethnic domination, violence, and illiberal democracy.  In: Civil Society and Political 
Change in Asia: Expanding and Contracting Democratic Space , ed. Muthiah Alagappa . Stanford, Stanford 
University Press, pp.292-323. 
 
Richardson, John. 2005. Paradise Poisoned: Learning about Conflict, Terrorism, and Development from Sri 
Lanka’s Civil Wars. Kandy, Sri Lanka, International Center for Ethnic Studies. 
 
Sudan/Sudan-North/South Sudan 
 
Collins, Robert O. 2008. A History of Modern Sudan. Cambridge, Cambridge University Press. 
 
Eprile, Cecil. 1974. War and Peace in the Sudan, 1955-1972. David & Charles. 
 
Holt, P. M., and M.W. Daly. 2014. A History of the Sudan: From the Coming of Islam to the Present Day . London, 
Routledge. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Swaziland 
 
BBC News. 2018. eSwatini profile. Located at: www.bbc.com/news/world-africa-14095711. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Syria 
 
Devlin, John F. 1991. The Baath Party: Rise and metamorphosis." American Historical Review 96(5): 1396-1407.

## Page 32

32 
 
Hopwood, Derek. 1988. Syria 1945-1986: Politics and Society. London, Unwin Hyman. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001. Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Taiwan 
 
Hood, Steven J. 1997. The Kuomintang and the Democratization of Taiwan. Westview Press. 
 
Mattlin, Mikael. 2011. Politicized Society: The Long Shadow of Taiwan’s One -party Legacy . Copenhagen, NIAS 
Press. 
 
Nohlen, Dieter, Florian Grotz, and Christof Hartmann (eds.). 2001. Elections in Asia and the Pacific: A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
  
Tien, Hung Mao, and Yun-han Chu. 1996. Building democracy in Taiwan. China Quarterly 148: 1141-70. 
 
Tsang, Steve. 1999. Transforming a party state into a democracy. In: Democratization in Ta iwan: Implications for 
China, eds. Steve Tsang and Hung-mao Tien. Hong Kong, Hong Kong University Press, pp.1-22. 
 
Tajikistan 
 
Luong, Pauline Jones. 2002. Institutional Change and Political Continuity in Post -Soviet Central Asia: Power, 
Perceptions, and Pacts. Cambridge, Cambridge University Press. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Tanzania 
 
Levitsky, Steven, and Lucan A. Way. 2010 . Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Han dbook. 
Oxford, Oxford University Press. 
 
Thailand 
 
Freedman, Amy. 2006 . Political Chan ge and Consolidation: Democracy’ s Rocky Road in Thailand, Indonesia, 
South Korea, and Malaysia. London, Palgrave Macmillan. 
 
Hewison, Kevin (ed.). 1997. Political Change in Thailand: Democracy and Participation. London, Routledge. 
 
Kurlantzick, Joshua. 2013. Thailand. In: Pathways to Freedom: Political and Economic Lessons from Democratic 
Transitions, eds. Isobel Coleman and Terra Lawson-Remer. New York, Council on Foreign Relations, pp.157-80. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in  Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press. 
 
Togo 
 
Heilbrunn, John R. 1993. Social origins of national conferences in Benin and Togo. Journal of Modern African 
Studies 31(2): 277-99. 
 
Lindberg, Staffan I. 2006. Democracy and Elections in Africa. Baltimore, JHU Press.

## Page 33

33 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Tunisia 
 
Bellin, Eva. 2000. Contingent democrats: Industrialists, labor, and democratization in late -developing countries. 
World Politics 52: 175-205. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Perkins, Kenneth. 2014. A History of Modern Tunisia. Cambridge, Cambridge University Press. 
 
Turkey 
 
Ahmad, Feroz. 1977. The Turkish Experiment in Democracy, 1950-1975. Westview Press. 
 
Pope, Nicole, and Hugh Pope. 2000. Turkey Unveiled: A History of Modern Turkey . Woodstock, NY, Overlook 
Books. 
 
Zürcher, Erik J. 2004. Turkey: A Modern History (revised edition). London, I.B. Tauris, pp.278-337. 
 
Turkmenistan 
 
Luong, Pauline Jones. 2002. Institutional Change and Political C ontinuity in Post -Soviet Central Asia: Power, 
Perceptions, and Pacts. Cambridge, Cambridge University Press. 
 
Nohlen, D ieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Uganda 
 
Crook, Richard C. 1999. ‘No -party’ politics and local democracy in Africa: Rawlings’ Ghana in the 1990s and the 
‘Ugandan Model.’ Democratization 6(4): 114-38. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press.  
 
Ocitti, Jim. 2000. Political Evolution and Democratic Practice in Uganda, 1952 -1996. London, Edwin Mellen 
Press. 
 
Uruguay 
 
Di Tella, Torcuato. 2017. History of Political Parties in Twentieth-century Latin America. New York, Routledge. 
 
González, Luis E. 1991. Political Structures and Democracy in Uruguay . South Bend, University of Notre Dame 
Press. 
 
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America . Oxford, Oxford 
University Press. 
 
O’Donnell, Guillermo, Philippe Schmitter, and Laurence Whitehead (eds.). 1986. Transitions from Authoritarian 
Rule: Comparative Perspectives. Baltimore, Johns Hopkins University Press.

## Page 34

34 
 
Uzbekistan 
 
Luong, Pauline Jones. 2002. Institutional Change and Political Continuity in Post -Soviet Central Asia: Power, 
Perceptions, and Pacts. Cambridge, Cambridge University Press. 
 
Nohlen, Dieter, Florian Grotz, and  Christof Hartmann (eds.). 2001 . Elections in Asia  and the Pacific : A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Venezuela  
 
Kolb, Glen L. 1974. Democracy and Dictatorship in Venezuela, 1945-1958. Shoe String Press. 
  
Nohlen, Dieter (ed.). 2005. Elections in the Americas: A Data Handbook, Volume 2: South America. Oxford, Oxford 
University Press. 
 
Peeler, John A. 1986. Latin American Democracies: Colombia, Costa Rica, Venezuela. Chapel Hill, University of 
North Carolina Press. 
 
Vietnams 
 
Karnow, Stanley. 1994. Vietnam: A History. New York, Random House. 
 
Lawrence, Mark Atwood. 2010. The Vietnam War: A Concise International History . Oxford, Oxford University 
Press. 
 
Malesky, Edmund, Regina Abrami, and Yu Zheng. 2011. Institutions and inequality in single -party regimes: A 
comparative analysis of Vietnam and China. Comparative Politics 43(4): 409-27. 
 
Nohlen, Dieter, Florian Grotz, and Christof Hartmann (eds.). 2001. Elections in Asia and the Pacific: A Data 
Handbook, Volume 2: Southeast Asia, East Asia and the South Pacific. Oxford, Oxford University Press.  
 
Yemens 
 
Dresch, Paul. 2000. A History of Modern Yemen. Cambridge, Cambridge University Press. 
 
Nohlen, Dieter, Florian Grotz, and Christof Hartmann (eds.). 2001. Elections in Asia and the Pacific: A Data 
Handbook, Volume I: Middle East, Central Asia, and South Asia. Oxford, Oxford University Press. 
 
Schwedler, Jillian. 2006. Faith in Moderation: Isl amist Parties in Jordan and Yemen . Cambridge, Cambridge 
University Press. 
 
Zambia 
 
Cheeseman, Nic, and Marja Hinfelaar. 2009 . Parties, platforms, and political mobilization: The Zambian 
Presidential election of 2008. African Affairs 109(434): 51-76.  
 
Nohlen, Dieter , Michael Krennerich, and Bernhard Thibaut (eds.). 1999 . Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Riedl, Rachel B. 2014. Authoritarian Origins of Democracy Party Systems in Africa . Cambridge, Cambridge 
University Press. 
 
Simutanyi, Neo. 2010. The 2008 presidential elections in Zambia: Incumbency, political contestation and failure of 
political opposition. Paper presented at IESE/CMI Conference on “Election Processes, Liberation Movements and 
Democratic Change in Africa,” Maputo, Zambia.

## Page 35

35 
 
Zimbabwe 
 
Levitsky, Steven, and Lucan A. Way. 2010. Competitive Authoritarianism: Hybrid Regimes After the Cold War . 
Cambridge, Cambridge University Press. 
 
Nohlen, Dieter, Michael Krennerich, and Bernhard Thibaut (eds.). 1999. Elections in Africa: A Data Handbook . 
Oxford, Oxford University Press. 
 
Raftopoulos, Brian, and Alois Mlambo (eds.). 2008. Becoming Zimbabwe. A History from the Pre-colonial Period to 
2008: A History from the Pre-colonial Period to 2008. African Books Collective.

