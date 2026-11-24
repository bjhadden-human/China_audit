## 4. Historical survival model and estimation

Observation ends in 2015; exit coordinate 2016 means right censoring at the end of that year range. For original records, a numeric last year becomes exit=last+1. Reviewed endpoints supplied directly to the code are exit coordinates: exit=1990 is not an assertion that the entire calendar year 1990 contributed exposure. Boundary choices are annual-to-continuous approximations, not exact event dates.

```text
t_i = exit_i - start_i
entry_i = max(1940 - start_i, 0)
d_i = 1 for an observed loss, 0 for censoring
h(a) = alpha * exp(beta*a)
log L = sum_i { d_i*(log(alpha)+beta*t_i)
                - integral(entry_i,t_i) h(a) da }
alpha_hat(beta) = D / sum_i integral(entry_i,t_i) exp(beta*a) da
AIC = 2*p + 2*NLL
P(loss by age A+u | survival to A) = 1-exp[-integral(A,A+u) h(a) da]
P(eventual loss | A) = 1, if beta >= 0
                     1-exp[h(A)/beta], if beta < 0
```

The likelihood conditions on survival to delayed entry; pre-1940 person-years are not treated as observed exposure. The implementation profiles alpha analytically and solves the beta score by Brent root finding, with stable series and log-sum-exp calculations. Strata use the literal source accession text containing Revolution and the source Marxist indicator; ideological intuition does not override those filters.

Country-block bootstrap accounts for repeated spells within normalized countries, not arbitrary worldwide shock dependence. Cross-national heterogeneity, shared calendar shocks, cohort effects, unobserved frailty and changes in institutional technology can generate an apparent declining age hazard. It is not automatically learning or durability improvement within the same regime. A pooled historical fit is not a validated China regression.

| spec | set | n | events | country_blocks | log_alpha | beta | NLL | AIC | loss25_from77 | eventual_loss_from77 | max_age | exposure_years | hazard77 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ARPD benchmark | All | 277 | 228 | 131 | -2.61747193 | -0.0167031736 | 876.112452 | 1756.2249 | 0.337800385 | 0.701052012 | 102 | 4023 | 0.0201688429 |
| ARPD benchmark | Revolutionary accession | 35 | 23 | 33 | -3.83522744 | 0.0135145849 | 103.790724 | 211.581448 | 0.837714382 | 1 | 70 | 792 | 0.0611390563 |
| ARPD benchmark | Marxist revolutionary accession | 20 | 13 | 19 | -3.57977082 | -0.00164351949 | 59.990632 | 123.981264 | 0.452145821 | 0.999999678 | 70 | 483 | 0.0245677219 |
| Earlier Vietnam correction | All | 276 | 227 | 130 | -2.60624061 | -0.0176459807 | 872.454505 | 1748.90901 | 0.318483853 | 0.658682236 | 102 | 4023 | 0.0189683948 |
| Earlier Vietnam correction | Revolutionary accession | 34 | 22 | 32 | -3.7946102 | 0.00936376413 | 100.546721 | 205.093442 | 0.728261743 | 1 | 70 | 792 | 0.0462543222 |
| Earlier Vietnam correction | Marxist revolutionary accession | 19 | 12 | 18 | -3.5280526 | -0.00747934484 | 56.2363848 | 116.47277 | 0.313667369 | 0.889973106 | 70 | 483 | 0.0165071418 |
| Frozen continuous | All | 269 | 220 | 129 | -2.60976869 | -0.018582096 | 848.390251 | 1700.7805 | 0.296499509 | 0.611884997 | 102 | 3957 | 0.0175870914 |
| Frozen continuous | Revolutionary accession | 33 | 20 | 32 | -4.03547139 | 0.0137739777 | 93.6296032 | 191.259206 | 0.782085782 | 1 | 72 | 818 | 0.05105381 |
| Frozen continuous | Marxist revolutionary accession | 18 | 10 | 18 | -3.94104232 | 0.000465363887 | 49.2982705 | 102.596541 | 0.3973136 | 1 | 72 | 509 | 0.0201367394 |
| Frozen 2004 | All | 270 | 221 | 129 | -2.61408348 | -0.0178645686 | 851.198553 | 1706.39711 | 0.31143433 | 0.645096876 | 102 | 3947 | 0.0185060927 |
| Frozen 2004 | Revolutionary accession | 33 | 21 | 32 | -3.94373805 | 0.0132638268 | 96.7488794 | 197.497759 | 0.797076528 | 1 | 72 | 796 | 0.0538031431 |
| Frozen 2004 | Marxist revolutionary accession | 18 | 11 | 18 | -3.7878645 | -0.000105872509 | 52.6940363 | 109.388073 | 0.429224347 | 1 | 72 | 487 | 0.0224600595 |
| Frozen 2009 | All | 270 | 221 | 129 | -2.6122633 | -0.0178961908 | 850.889198 | 1705.7784 | 0.311182444 | 0.644220634 | 102 | 3942 | 0.01849472 |
| Frozen 2009 | Revolutionary accession | 33 | 21 | 32 | -3.94373805 | 0.0132638268 | 96.7488794 | 197.497759 | 0.797076528 | 1 | 72 | 796 | 0.0538031431 |
| Frozen 2009 | Marxist revolutionary accession | 18 | 11 | 18 | -3.7878645 | -0.000105872509 | 52.6940363 | 109.388073 | 0.429224347 | 1 | 72 | 487 | 0.0224600595 |
| Corrected continuous | All | 267 | 219 | 128 | -2.61564394 | -0.0183610769 | 845.403645 | 1694.80729 | 0.299902635 | 0.620378128 | 102 | 3952 | 0.0177841644 |
| Corrected continuous | Revolutionary accession | 33 | 20 | 32 | -4.03547139 | 0.0137739777 | 93.6296032 | 191.259206 | 0.782085782 | 1 | 72 | 818 | 0.05105381 |
| Corrected continuous | Marxist revolutionary accession | 18 | 10 | 18 | -3.94104232 | 0.000465363887 | 49.2982705 | 102.596541 | 0.3973136 | 1 | 72 | 509 | 0.0201367394 |
| Corrected 2004 | All | 268 | 220 | 128 | -2.61992461 | -0.0176459144 | 848.209464 | 1700.41893 | 0.314924592 | 0.65366247 | 102 | 3942 | 0.0187106946 |
| Corrected 2004 | Revolutionary accession | 33 | 21 | 32 | -3.94373805 | 0.0132638268 | 96.7488794 | 197.497759 | 0.797076528 | 1 | 72 | 796 | 0.0538031431 |
| Corrected 2004 | Marxist revolutionary accession | 18 | 11 | 18 | -3.7878645 | -0.000105872509 | 52.6940363 | 109.388073 | 0.429224347 | 1 | 72 | 487 | 0.0224600595 |
| Corrected 2009 | All | 268 | 220 | 128 | -2.61809728 | -0.0176778593 | 847.901274 | 1699.80255 | 0.314664924 | 0.652765935 | 102 | 3937 | 0.0186988651 |
| Corrected 2009 | Revolutionary accession | 33 | 21 | 32 | -3.94373805 | 0.0132638268 | 96.7488794 | 197.497759 | 0.797076528 | 1 | 72 | 796 | 0.0538031431 |
| Corrected 2009 | Marxist revolutionary accession | 18 | 11 | 18 | -3.7878645 | -0.000105872509 | 52.6940363 | 109.388073 | 0.429224347 | 1 | 72 | 487 | 0.0224600595 |

AIC comparisons are meaningful between hazard families on the same observations and likelihood. Do not rank frozen versus corrected datasets merely because one has a lower AIC: their observations differ.
