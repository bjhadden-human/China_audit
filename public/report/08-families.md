## 8. Alternative hazard families and old-age diagnostics

```text
Exponential: h(a)=rate; eventual loss=1 for positive rate
Weibull: h(a)=k*a^(k-1)/scale^k; eventual loss=1 for k>0
Cure mixture: S(a)=c+(1-c)*exp(-rate*a)
  conditional eventual loss at A = 1-c/S(A)
Power-declining: h(a)=a0*(1+a/tau)^(-p)
  eventual loss=1 if p<=1; finite remaining hazard if p>1
```

Families use the same delayed-entry likelihood within each dataset. The code retains bounds, starting points, selected optimizer success and bound-contact flags. All 72 selected alternative fits report success; success is not proof of a unique/global optimum. Revolutionary power-declining fits contact a bound. AIC cannot validate the unobserved tail merely by close observed fit.

In the frozen broad continuous sample the power-declining AIC is about 1699.155 versus Gompertz 1700.781, while power-declining eventual loss is 1. The cure mixture gives about 21.63% eventual loss but materially worse AIC. Exponential has the lowest tested AIC in the narrow revolutionary strata. The conclusion near 60% is thus not the unique tail implication of reasonably fitting models.

| spec | set | model | NLL | AIC | loss25_from77 | eventual_loss_from77 | parameters | bound_contact | success |
|---|---|---|---|---|---|---|---|---|---|
| Frozen continuous | All | Exponential | 855.715057 | 1713.43011 | 0.750910217 | 1 | [0.05559767500631792] | False | True |
| Frozen continuous | All | Weibull | 852.290249 | 1708.5805 | 0.644840665 | 1 | [0.8743254298079728, 17.165884867296814] | False | True |
| Frozen continuous | All | Exponential cure mixture | 854.645105 | 1713.29021 | 0.169483925 | 0.216283038 | [0.03145707495164495, 0.06122894695306318] | False | True |
| Frozen continuous | All | Power-declining hazard | 846.577609 | 1699.15522 | 0.433165054 | 1 | [0.08422083170921495, 12.902156376273393, 0.6339981357529003] | False | True |
| Frozen continuous | Revolutionary accession | Exponential | 94.2226013 | 190.445203 | 0.457326237 | 1 | [0.02444987775061125] | False | True |
| Frozen continuous | Revolutionary accession | Weibull | 93.3881315 | 190.776263 | 0.630398899 | 1 | [1.2864367006957702, 40.5185280103701] | False | True |
| Frozen continuous | Revolutionary accession | Exponential cure mixture | 94.2226018 | 192.445204 | 0.457325354 | 0.99999942 | [8.830611181812598e-08, 0.024449832220365383] | False | True |
| Frozen continuous | Revolutionary accession | Power-declining hazard | 94.2226034 | 194.445207 | 0.457325666 | 1 | [0.024449890595749535, 98715.77101076051, 0.0024787521766663585] | True | True |
| Frozen continuous | Marxist revolutionary accession | Exponential | 49.2986292 | 100.597258 | 0.388083311 | 1 | [0.019646365422396856] | False | True |
| Frozen continuous | Marxist revolutionary accession | Weibull | 49.2985911 | 102.597182 | 0.38933028 | 1 | [1.0023489062288091, 50.875607929103055] | False | True |
| Frozen continuous | Marxist revolutionary accession | Exponential cure mixture | 49.2986295 | 102.597259 | 0.388083022 | 0.999999046 | [2.1009047225621494e-07, 0.01964637069512747] | False | True |
| Frozen continuous | Marxist revolutionary accession | Power-declining hazard | 49.2663901 | 104.53278 | 0.336379213 | 1 | [0.02279715388153163, 10.787500115321544, 0.1478650649893614] | False | True |
| Frozen 2004 | All | Exponential | 858.043191 | 1718.08638 | 0.753353049 | 1 | [0.05599189257664049] | False | True |
| Frozen 2004 | All | Weibull | 854.950733 | 1713.90147 | 0.652597861 | 1 | [0.8804505210649054, 17.08733936294895] | False | True |
| Frozen 2004 | All | Exponential cure mixture | 857.116764 | 1718.23353 | 0.184803818 | 0.236007116 | [0.028422990483778818, 0.06112232092211035] | False | True |
| Frozen 2004 | All | Power-declining hazard | 849.543375 | 1705.08675 | 0.445076899 | 1 | [0.08333580023790807, 13.185262621227295, 0.6167544663452775] | False | True |
| Frozen 2004 | Revolutionary accession | Exponential | 97.3366117 | 196.673223 | 0.482914861 | 1 | [0.026381909547738693] | False | True |
| Frozen 2004 | Revolutionary accession | Weibull | 96.3469279 | 196.693856 | 0.670094448 | 1 | [1.30362157639032, 38.070921003446905] | False | True |
| Frozen 2004 | Revolutionary accession | Exponential cure mixture | 97.3366118 | 198.673224 | 0.482914791 | 0.999999872 | [1.672295677197463e-08, 0.026381908936335963] | False | True |
| Frozen 2004 | Revolutionary accession | Power-declining hazard | 97.3366139 | 200.673228 | 0.482914274 | 1 | [0.026381923413658852, 98715.77101076051, 0.0024787521766663585] | True | True |
| Frozen 2004 | Marxist revolutionary accession | Exponential | 52.6940574 | 107.388115 | 0.43145893 | 1 | [0.022587268993839837] | False | True |
| Frozen 2004 | Marxist revolutionary accession | Weibull | 52.6832415 | 109.366483 | 0.453303288 | 1 | [1.0379163044399766, 44.13227652303394] | False | True |
| Frozen 2004 | Marxist revolutionary accession | Exponential cure mixture | 52.6940575 | 109.388115 | 0.431440448 | 0.999999691 | [5.420073487916014e-08, 0.02258597813086902] | False | True |
| Frozen 2004 | Marxist revolutionary accession | Power-declining hazard | 52.6783616 | 111.356723 | 0.391043644 | 1 | [0.02468743364878393, 18.832165915004396, 0.12510628801048845] | False | True |
| Frozen 2009 | All | Exponential | 857.763054 | 1717.52611 | 0.75379058 | 1 | [0.056062912227295786] | False | True |
| Frozen 2009 | All | Weibull | 854.673755 | 1713.34751 | 0.653172297 | 1 | [0.8805766086986611, 17.063826460214703] | False | True |
| Frozen 2009 | All | Exponential cure mixture | 856.82617 | 1717.65234 | 0.183518381 | 0.234201127 | [0.028484629883504097, 0.061223788989532346] | False | True |
| Frozen 2009 | All | Power-declining hazard | 849.244352 | 1704.4887 | 0.444762038 | 1 | [0.08341157876436732, 13.331027734554336, 0.6205687985386388] | False | True |
| Frozen 2009 | Revolutionary accession | Exponential | 97.3366117 | 196.673223 | 0.482914861 | 1 | [0.026381909547738693] | False | True |
| Frozen 2009 | Revolutionary accession | Weibull | 96.3469279 | 196.693856 | 0.670094448 | 1 | [1.30362157639032, 38.070921003446905] | False | True |
| Frozen 2009 | Revolutionary accession | Exponential cure mixture | 97.3366118 | 198.673224 | 0.482914791 | 0.999999872 | [1.672295677197463e-08, 0.026381908936335963] | False | True |
| Frozen 2009 | Revolutionary accession | Power-declining hazard | 97.3366139 | 200.673228 | 0.482914274 | 1 | [0.026381923413658852, 98715.77101076051, 0.0024787521766663585] | True | True |
| Frozen 2009 | Marxist revolutionary accession | Exponential | 52.6940574 | 107.388115 | 0.43145893 | 1 | [0.022587268993839837] | False | True |
| Frozen 2009 | Marxist revolutionary accession | Weibull | 52.6832415 | 109.366483 | 0.453303288 | 1 | [1.0379163044399766, 44.13227652303394] | False | True |
| Frozen 2009 | Marxist revolutionary accession | Exponential cure mixture | 52.6940575 | 109.388115 | 0.431440448 | 0.999999691 | [5.420073487916014e-08, 0.02258597813086902] | False | True |
| Frozen 2009 | Marxist revolutionary accession | Power-declining hazard | 52.6783616 | 111.356723 | 0.391043644 | 1 | [0.02468743364878393, 18.832165915004396, 0.12510628801048845] | False | True |
| Corrected continuous | All | Exponential | 852.546267 | 1707.09253 | 0.749769927 | 1 | [0.05541497975708502] | False | True |
| Corrected continuous | All | Weibull | 849.304548 | 1702.6091 | 0.646254664 | 1 | [0.8770673471480676, 17.24044798183858] | False | True |
| Corrected continuous | All | Exponential cure mixture | 851.521017 | 1707.04203 | 0.174096265 | 0.222624788 | [0.031025173561928965, 0.06093344219123903] | False | True |
| Corrected continuous | All | Power-declining hazard | 843.662749 | 1693.3255 | 0.434151827 | 1 | [0.08344577945614697, 13.324417805115369, 0.6366859005826353] | False | True |
| Corrected continuous | Revolutionary accession | Exponential | 94.2226013 | 190.445203 | 0.457326237 | 1 | [0.02444987775061125] | False | True |
| Corrected continuous | Revolutionary accession | Weibull | 93.3881315 | 190.776263 | 0.630398899 | 1 | [1.2864367006957702, 40.5185280103701] | False | True |
| Corrected continuous | Revolutionary accession | Exponential cure mixture | 94.2226018 | 192.445204 | 0.457325354 | 0.99999942 | [8.830611181812598e-08, 0.024449832220365383] | False | True |
| Corrected continuous | Revolutionary accession | Power-declining hazard | 94.2226034 | 194.445207 | 0.457325666 | 1 | [0.024449890595749535, 98715.77101076051, 0.0024787521766663585] | True | True |
| Corrected continuous | Marxist revolutionary accession | Exponential | 49.2986292 | 100.597258 | 0.388083311 | 1 | [0.019646365422396856] | False | True |
| Corrected continuous | Marxist revolutionary accession | Weibull | 49.2985911 | 102.597182 | 0.38933028 | 1 | [1.0023489062288091, 50.875607929103055] | False | True |
| Corrected continuous | Marxist revolutionary accession | Exponential cure mixture | 49.2986295 | 102.597259 | 0.388083022 | 0.999999046 | [2.1009047225621494e-07, 0.01964637069512747] | False | True |
| Corrected continuous | Marxist revolutionary accession | Power-declining hazard | 49.2663901 | 104.53278 | 0.336379213 | 1 | [0.02279715388153163, 10.787500115321544, 0.1478650649893614] | False | True |
| Corrected 2004 | All | Exponential | 854.879507 | 1711.75901 | 0.752224169 | 1 | [0.05580923389142567] | False | True |
| Corrected 2004 | All | Weibull | 851.961062 | 1707.92212 | 0.654044894 | 1 | [0.8832343586061688, 17.16130950660851] | False | True |
| Corrected 2004 | All | Exponential cure mixture | 853.993764 | 1711.98753 | 0.189811016 | 0.242892717 | [0.028000288420705836, 0.06083150400444779] | False | True |
| Corrected 2004 | All | Power-declining hazard | 846.622958 | 1699.24592 | 0.446068133 | 1 | [0.08256904372719434, 13.637823908604274, 0.6196315981159981] | False | True |
| Corrected 2004 | Revolutionary accession | Exponential | 97.3366117 | 196.673223 | 0.482914861 | 1 | [0.026381909547738693] | False | True |
| Corrected 2004 | Revolutionary accession | Weibull | 96.3469279 | 196.693856 | 0.670094448 | 1 | [1.30362157639032, 38.070921003446905] | False | True |
| Corrected 2004 | Revolutionary accession | Exponential cure mixture | 97.3366118 | 198.673224 | 0.482914791 | 0.999999872 | [1.672295677197463e-08, 0.026381908936335963] | False | True |
| Corrected 2004 | Revolutionary accession | Power-declining hazard | 97.3366139 | 200.673228 | 0.482914274 | 1 | [0.026381923413658852, 98715.77101076051, 0.0024787521766663585] | True | True |
| Corrected 2004 | Marxist revolutionary accession | Exponential | 52.6940574 | 107.388115 | 0.43145893 | 1 | [0.022587268993839837] | False | True |
| Corrected 2004 | Marxist revolutionary accession | Weibull | 52.6832415 | 109.366483 | 0.453303288 | 1 | [1.0379163044399766, 44.13227652303394] | False | True |
| Corrected 2004 | Marxist revolutionary accession | Exponential cure mixture | 52.6940575 | 109.388115 | 0.431440448 | 0.999999691 | [5.420073487916014e-08, 0.02258597813086902] | False | True |
| Corrected 2004 | Marxist revolutionary accession | Power-declining hazard | 52.6783616 | 111.356723 | 0.391043644 | 1 | [0.02468743364878393, 18.832165915004396, 0.12510628801048845] | False | True |
| Corrected 2009 | All | Exponential | 854.600284 | 1711.20057 | 0.752662825 | 1 | [0.05588011176022352] | False | True |
| Corrected 2009 | All | Weibull | 851.68473 | 1707.36946 | 0.654615937 | 1 | [0.8833561870643145, 17.137692262057627] | False | True |
| Corrected 2009 | All | Exponential cure mixture | 853.704292 | 1711.40858 | 0.188485179 | 0.24102543 | [0.02806491988513019, 0.06093291483484749] | False | True |
| Corrected 2009 | All | Power-declining hazard | 846.324592 | 1698.64918 | 0.445746558 | 1 | [0.08264703134021999, 13.787849328720318, 0.6235147867143424] | False | True |
| Corrected 2009 | Revolutionary accession | Exponential | 97.3366117 | 196.673223 | 0.482914861 | 1 | [0.026381909547738693] | False | True |
| Corrected 2009 | Revolutionary accession | Weibull | 96.3469279 | 196.693856 | 0.670094448 | 1 | [1.30362157639032, 38.070921003446905] | False | True |
| Corrected 2009 | Revolutionary accession | Exponential cure mixture | 97.3366118 | 198.673224 | 0.482914791 | 0.999999872 | [1.672295677197463e-08, 0.026381908936335963] | False | True |
| Corrected 2009 | Revolutionary accession | Power-declining hazard | 97.3366139 | 200.673228 | 0.482914274 | 1 | [0.026381923413658852, 98715.77101076051, 0.0024787521766663585] | True | True |
| Corrected 2009 | Marxist revolutionary accession | Exponential | 52.6940574 | 107.388115 | 0.43145893 | 1 | [0.022587268993839837] | False | True |
| Corrected 2009 | Marxist revolutionary accession | Weibull | 52.6832415 | 109.366483 | 0.453303288 | 1 | [1.0379163044399766, 44.13227652303394] | False | True |
| Corrected 2009 | Marxist revolutionary accession | Exponential cure mixture | 52.6940575 | 109.388115 | 0.431440448 | 0.999999691 | [5.420073487916014e-08, 0.02258597813086902] | False | True |
| Corrected 2009 | Marxist revolutionary accession | Power-declining hazard | 52.6783616 | 111.356723 | 0.391043644 | 1 | [0.02468743364878393, 18.832165915004396, 0.12510628801048845] | False | True |

The age-60 diagnostic conditions entry on max(original entry,60). Corrected and frozen continuous each have only six qualifying spells and four events, with 79 observed exposure-years after age 60. Its positive Gompertz slope contrasts with the broad all-age declining slope. Do not suppress this result, and do not turn six spells into a precise old-age China model.

| spec | n | events | exposure_years_after60 | log_alpha | beta | loss25_from77 | eventual_loss_from77 |
|---|---|---|---|---|---|---|---|
| ARPD benchmark | 6 | 5 | 90 | -4.88989436 | 0.0267980711 | 0.878596437 | 1 |
| Frozen continuous | 6 | 4 | 79 | -4.95581388 | 0.0261282878 | 0.843945741 | 1 |
| Corrected continuous | 6 | 4 | 79 | -4.95581388 | 0.0261282878 | 0.843945741 | 1 |

**Underlying age-60 records**

| spec | episode_id | country | Party | start | exit | event | entry_age60 | exit_age |
|---|---|---|---|---|---|---|---|---|
| ARPD benchmark | source_28 | Azerbaijan | Azerbaijan Communist Party | 1920 | 1992 | 1 | 60 | 72 |
| ARPD benchmark | source_249 | Korea (North) | Workers' Party of North Korea / Workers' Party of Korea | 1948 | 2016 | 0 | 60 | 68 |
| ARPD benchmark | source_271 | Liberia | True Whig Party | 1878 | 1980 | 1 | 62 | 102 |
| ARPD benchmark | source_302 | Mexico | National Revolutionary Party / Mexican Revolutionary Party / Institutional Revolutionary Party (PRI) | 1929 | 2000 | 1 | 60 | 71 |
| ARPD benchmark | source_303 | Mongolia | Mongolian People's Revolutionary Party | 1921 | 1990 | 1 | 60 | 69 |
| ARPD benchmark | source_454 | USSR | Communist Party of the Soviet Union | 1922 | 1992 | 1 | 60 | 70 |
| Frozen continuous | source_249 | Korea (North) | Workers' Party of North Korea / Workers' Party of Korea | 1948 | 2016 | 0 | 60 | 68 |
| Frozen continuous | source_271 | Liberia | True Whig Party | 1878 | 1980 | 1 | 62 | 102 |
| Frozen continuous | source_302 | Mexico | National Revolutionary Party / Mexican Revolutionary Party / Institutional Revolutionary Party (PRI) | 1929 | 1997 | 1 | 60 | 68 |
| Frozen continuous | source_303 | Mongolia | Mongolian People's Revolutionary Party | 1921 | 1990 | 1 | 60 | 69 |
| Frozen continuous | source_454 | USSR | Communist Party of the Soviet Union | 1918 | 1990 | 1 | 60 | 72 |
| Frozen continuous | joined_466_467 | Vietnam | Vietnam Workers' Party (DLDV) / Communist Party of Vietnam (DCSV) | 1954 | 2016 | 0 | 60 | 62 |
| Corrected continuous | source_249 | Korea (North) | Workers' Party of North Korea / Workers' Party of Korea | 1948 | 2016 | 0 | 60 | 68 |
| Corrected continuous | source_271 | Liberia | True Whig Party | 1878 | 1980 | 1 | 62 | 102 |
| Corrected continuous | source_302 | Mexico | National Revolutionary Party / Mexican Revolutionary Party / Institutional Revolutionary Party (PRI) | 1929 | 1997 | 1 | 60 | 68 |
| Corrected continuous | source_303 | Mongolia | Mongolian People's Revolutionary Party | 1921 | 1990 | 1 | 60 | 69 |
| Corrected continuous | source_454 | USSR | Communist Party of the Soviet Union | 1918 | 1990 | 1 | 60 | 72 |
| Corrected continuous | joined_466_467 | Vietnam | Vietnam Workers' Party (DLDV) / Communist Party of Vietnam (DCSV) | 1954 | 2016 | 0 | 60 | 62 |
