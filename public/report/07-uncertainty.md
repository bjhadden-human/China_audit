## 7. Bootstrap, profiles and coding sensitivity

Both versions use 2,000 country-block replicates per stratum/branch in continuous and split-2004: 12,000 attempts each, 24,000 total, all successful. Root SeedSequence=20261124 spawns six streams in branch-major, then All/Revolutionary/Marxist order. Corrected runs reset the same stream allocation; changed country universes need not correspond to identical sampled countries. Percentiles condition on the chosen dataset, family and bootstrap assumptions; they are not posterior probabilities or China forecast intervals.

| spec | set | requested | successful | beta_ge0 | beta_q025 | beta_q975 | loss25_q025 | loss25_q975 | eventual_q025 | eventual_q975 |
|---|---|---|---|---|---|---|---|---|---|---|
| Corrected 2004 | All | 2000 | 2000 | 0 | -0.0272848002 | -0.00879137171 | 0.169056646 | 0.516006748 | 0.314322702 | 0.975089416 |
| Corrected 2004 | Marxist revolutionary accession | 2000 | 2000 | 1011 | -0.0421220075 | 0.0245901044 | 0.0233419237 | 0.867906276 | 0.0358666143 | 1 |
| Corrected 2004 | Revolutionary accession | 2000 | 2000 | 1875 | -0.00478774257 | 0.0347745163 | 0.375535497 | 0.997645304 | 0.990182112 | 1 |
| Corrected continuous | All | 2000 | 2000 | 0 | -0.0281741411 | -0.00892626366 | 0.157440376 | 0.505183097 | 0.28641539 | 0.970180422 |
| Corrected continuous | Marxist revolutionary accession | 2000 | 2000 | 1009 | -0.0497019442 | 0.0312987691 | 0.0130210064 | 0.897077126 | 0.0187499186 | 1 |
| Corrected continuous | Revolutionary accession | 2000 | 2000 | 1873 | -0.00551491873 | 0.0349742723 | 0.31746852 | 0.994679096 | 0.945967014 | 1 |
| Frozen 2004 | All | 2000 | 2000 | 0 | -0.0272986603 | -0.00937530326 | 0.16845315 | 0.496490992 | 0.31487698 | 0.958245872 |
| Frozen 2004 | Marxist revolutionary accession | 2000 | 2000 | 1011 | -0.0421220075 | 0.0245901044 | 0.0233419237 | 0.867906276 | 0.0358666143 | 1 |
| Frozen 2004 | Revolutionary accession | 2000 | 2000 | 1875 | -0.00478774257 | 0.0347745163 | 0.375535497 | 0.997645304 | 0.990182112 | 1 |
| Frozen continuous | All | 2000 | 2000 | 0 | -0.0289279342 | -0.00961655323 | 0.154417804 | 0.492375878 | 0.28114192 | 0.956427713 |
| Frozen continuous | Marxist revolutionary accession | 2000 | 2000 | 1009 | -0.0497019442 | 0.0312987691 | 0.0130210064 | 0.897077126 | 0.0187499186 | 1 |
| Frozen continuous | Revolutionary accession | 2000 | 2000 | 1873 | -0.00551491873 | 0.0349742723 | 0.31746852 | 0.994679096 | 0.945967014 | 1 |

Each version has 972 joint combinations, each fitted to three strata: 2,916 rows per version. The Cartesian order is Mozambique × Sudan × Syria × Kazakhstan × Zambia × first-FSLN loss × Soviet loss. These selected alternatives do not exhaust all plausible historical codings and carry no probability weights.

| version | set | fits | min_eventual | max_eventual | min_25 | max_25 |
|---|---|---|---|---|---|---|
| Corrected | All | 972 | 0.60757943 | 0.712138993 | 0.294880218 | 0.342913634 |
| Corrected | Marxist revolutionary accession | 972 | 0.999842402 | 1 | 0.354315638 | 0.429224347 |
| Corrected | Revolutionary accession | 972 | 1 | 1 | 0.752383305 | 0.797076528 |
| Frozen | All | 972 | 0.599240435 | 0.703650461 | 0.291543044 | 0.339286446 |
| Frozen | Marxist revolutionary accession | 972 | 0.999842402 | 1 | 0.354315638 | 0.429224347 |
| Frozen | Revolutionary accession | 972 | 1 | 1 | 0.752383305 | 0.797076528 |

Likelihood profiles parameterize remaining cumulative hazard R=h(77)/(-beta) for beta<0 and separately test eventual loss=1 through beta≥0. The nominal chi-square cutoff is 3.841459. Finite crossings are lower/upper endpoints when two are found; one crossing is a lower endpoint with 1 included when LR_at_one is below cutoff. This is not bootstrap-calibrated coverage; boundary behavior, extrapolation and small samples qualify interpretation.

| spec | set | LR_at_half | LR_at_one | finite_crossings | cutoff |
|---|---|---|---|---|---|
| Frozen continuous | All | 0.266270388 | 14.6496115 | [0.26102003364549525, 0.9765811583505086] | 3.84145882 |
| Frozen continuous | Revolutionary accession | 4.76896394 | 0 | [0.6530920793229353] | 3.84145882 |
| Frozen continuous | Marxist revolutionary accession | 0.597690804 | 0 | [0.058911674142879775] | 3.84145882 |
| Frozen 2004 | All | 0.439587661 | 13.6892763 | [0.28020706411290996, 0.9856314906275504] | 3.84145882 |
| Frozen 2004 | Revolutionary accession | 5.08747063 | 0 | [0.696423534693671] | 3.84145882 |
| Frozen 2004 | Marxist revolutionary accession | 0.71574192 | 4.20567396e-05 | [0.07659640508491244] | 3.84145882 |
| Frozen 2009 | All | 0.435160586 | 13.7477122 | [0.27987802301093, 0.9853266087712023] | 3.84145882 |
| Frozen 2009 | Revolutionary accession | 5.08747063 | 0 | [0.696423534693671] | 3.84145882 |
| Frozen 2009 | Marxist revolutionary accession | 0.71574192 | 4.20567396e-05 | [0.07659640508491244] | 3.84145882 |
| Corrected continuous | All | 0.305408263 | 14.2852445 | [0.2654021291600072, 0.9795698818817412] | 3.84145882 |
| Corrected continuous | Revolutionary accession | 4.76896394 | 0 | [0.6530920793229353] | 3.84145882 |
| Corrected continuous | Marxist revolutionary accession | 0.597690804 | 0 | [0.058911674142879775] | 3.84145882 |
| Corrected 2004 | All | 0.489066019 | 13.3400854 | [0.28484601120210895, 0.9877698391747288] | 3.84145882 |
| Corrected 2004 | Revolutionary accession | 5.08747063 | 0 | [0.696423534693671] | 3.84145882 |
| Corrected 2004 | Marxist revolutionary accession | 0.71574192 | 4.20567396e-05 | [0.07659640508491244] | 3.84145882 |
| Corrected 2009 | All | 0.484332436 | 13.3980204 | [0.28450263472170934, 0.9874913784750755] | 3.84145882 |
| Corrected 2009 | Revolutionary accession | 5.08747063 | 0 | [0.696423534693671] | 3.84145882 |
| Corrected 2009 | Marxist revolutionary accession | 0.71574192 | 4.20567396e-05 | [0.07659640508491244] | 3.84145882 |

**All 360 one-change fit rows**

| version | Mozambique | change | set | n | beta | loss25_from77 | eventual_loss_from77 |
|---|---|---|---|---|---|---|---|
| Frozen | continuous | Soviet accession1921 | All | 269 | -0.0186006754 | 0.296051154 | 0.61093063 |
| Frozen | continuous | Soviet accession1921 | Revolutionary accession | 33 | 0.0143521934 | 0.795529927 | 1 |
| Frozen | continuous | Soviet accession1921 | Marxist revolutionary accession | 18 | 0.000467501502 | 0.397398758 | 1 |
| Frozen | continuous | Soviet loss1991 | All | 269 | -0.0185856761 | 0.296411352 | 0.611698503 |
| Frozen | continuous | Soviet loss1991 | Revolutionary accession | 33 | 0.0135877637 | 0.777288724 | 1 |
| Frozen | continuous | Soviet loss1991 | Marxist revolutionary accession | 18 | 0.00047410627 | 0.39687542 | 1 |
| Frozen | continuous | Mongolian accession1924 | All | 269 | -0.0185891812 | 0.296259162 | 0.611418045 |
| Frozen | continuous | Mongolian accession1924 | Revolutionary accession | 33 | 0.0142740203 | 0.793835731 | 1 |
| Frozen | continuous | Mongolian accession1924 | Marxist revolutionary accession | 18 | 0.000464887781 | 0.397346269 | 1 |
| Frozen | continuous | North Korean accession1946 | All | 269 | -0.0186435025 | 0.295312055 | 0.609168074 |
| Frozen | continuous | North Korean accession1946 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | North Korean accession1946 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Mexican loss1996 | All | 269 | -0.0185783535 | 0.296592817 | 0.612081648 |
| Frozen | continuous | Mexican loss1996 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Mexican loss1996 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Mexican loss2000 | All | 269 | -0.0185931218 | 0.296226117 | 0.611307796 |
| Frozen | continuous | Mexican loss2000 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Mexican loss2000 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Ethiopian accession1992 | All | 269 | -0.018567911 | 0.296816273 | 0.612575545 |
| Frozen | continuous | Ethiopian accession1992 | Revolutionary accession | 33 | 0.0137694633 | 0.78240052 | 1 |
| Frozen | continuous | Ethiopian accession1992 | Marxist revolutionary accession | 18 | 0.00046773227 | 0.397961508 | 1 |
| Frozen | continuous | Sudan NCP-only1998 | All | 269 | -0.0184745396 | 0.299002026 | 0.617266802 |
| Frozen | continuous | Sudan NCP-only1998 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Sudan NCP-only1998 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Sudan power-sharing interruption | All | 270 | -0.0182883144 | 0.303371074 | 0.626617156 |
| Frozen | continuous | Sudan power-sharing interruption | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Sudan power-sharing interruption | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Syrian split1966 | All | 270 | -0.0187033093 | 0.295219476 | 0.608107552 |
| Frozen | continuous | Syrian split1966 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Syrian split1966 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Syrian military displacement1970 | All | 269 | -0.0180123775 | 0.310757057 | 0.641725774 |
| Frozen | continuous | Syrian military displacement1970 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Syrian military displacement1970 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Kazakh eligibility1999 | All | 270 | -0.0184311842 | 0.298111011 | 0.616629809 |
| Frozen | continuous | Kazakh eligibility1999 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Kazakh eligibility1999 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Kazakh eligibility2006 | All | 270 | -0.0184294925 | 0.298593945 | 0.617370393 |
| Frozen | continuous | Kazakh eligibility2006 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | Kazakh eligibility2006 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | Nicaraguan accession1980 | All | 269 | -0.0186137116 | 0.295979174 | 0.610621556 |
| Frozen | continuous | Nicaraguan accession1980 | Revolutionary accession | 33 | 0.0135745909 | 0.778141151 | 1 |
| Frozen | continuous | Nicaraguan accession1980 | Marxist revolutionary accession | 18 | 8.33831612e-05 | 0.390320451 | 1 |
| Frozen | continuous | Nicaraguan loss1984 | All | 269 | -0.0187996784 | 0.292893021 | 0.603156573 |
| Frozen | continuous | Nicaraguan loss1984 | Revolutionary accession | 33 | 0.0125345723 | 0.757032821 | 1 |
| Frozen | continuous | Nicaraguan loss1984 | Marxist revolutionary accession | 18 | -0.00194531951 | 0.354315638 | 0.999900495 |
| Frozen | continuous | FSLN reacquisition2009 | All | 269 | -0.0185401489 | 0.297057138 | 0.613364851 |
| Frozen | continuous | FSLN reacquisition2009 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | FSLN reacquisition2009 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | FSLN reacquisition2011 | All | 269 | -0.0185660381 | 0.296722544 | 0.61246559 |
| Frozen | continuous | FSLN reacquisition2011 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | FSLN reacquisition2011 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | FSLN no reacquisition before2016 | All | 268 | -0.0186689523 | 0.295203552 | 0.608613422 |
| Frozen | continuous | FSLN no reacquisition before2016 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | FSLN no reacquisition before2016 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | MMD loss2006 | All | 269 | -0.0183966335 | 0.299605997 | 0.619380629 |
| Frozen | continuous | MMD loss2006 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | MMD loss2006 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | continuous | MMD no qualifying episode | All | 268 | -0.0184603502 | 0.298037119 | 0.616063069 |
| Frozen | continuous | MMD no qualifying episode | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Frozen | continuous | MMD no qualifying episode | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Frozen | 2004 | Soviet accession1921 | All | 270 | -0.0178787996 | 0.311054612 | 0.644321048 |
| Frozen | 2004 | Soviet accession1921 | Revolutionary accession | 33 | 0.0138654468 | 0.810674158 | 1 |
| Frozen | 2004 | Soviet accession1921 | Marxist revolutionary accession | 18 | -2.56211723e-06 | 0.431404531 | 1 |
| Frozen | 2004 | Soviet loss1991 | All | 270 | -0.0178695577 | 0.311314542 | 0.64484401 |
| Frozen | 2004 | Soviet loss1991 | Revolutionary accession | 33 | 0.0130697857 | 0.792210284 | 1 |
| Frozen | 2004 | Soviet loss1991 | Marxist revolutionary accession | 18 | -0.000131103652 | 0.42804107 | 1 |
| Frozen | 2004 | Mongolian accession1924 | All | 270 | -0.017867508 | 0.311267144 | 0.644809615 |
| Frozen | 2004 | Mongolian accession1924 | Revolutionary accession | 33 | 0.0137901188 | 0.809082784 | 1 |
| Frozen | 2004 | Mongolian accession1924 | Marxist revolutionary accession | 18 | -2.54775726e-06 | 0.431404836 | 1 |
| Frozen | 2004 | North Korean accession1946 | All | 270 | -0.0179278625 | 0.310162575 | 0.642242908 |
| Frozen | 2004 | North Korean accession1946 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | North Korean accession1946 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Mexican loss1996 | All | 270 | -0.0178595224 | 0.311557453 | 0.645355416 |
| Frozen | 2004 | Mexican loss1996 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Mexican loss1996 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Mexican loss2000 | All | 270 | -0.0178796108 | 0.311069813 | 0.644329591 |
| Frozen | 2004 | Mexican loss2000 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Mexican loss2000 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Ethiopian accession1992 | All | 270 | -0.0178504321 | 0.31176286 | 0.64579765 |
| Frozen | 2004 | Ethiopian accession1992 | Revolutionary accession | 33 | 0.0132604743 | 0.797419645 | 1 |
| Frozen | 2004 | Ethiopian accession1992 | Marxist revolutionary accession | 18 | -0.000100671723 | 0.42999222 | 1 |
| Frozen | 2004 | Sudan NCP-only1998 | All | 270 | -0.0177575464 | 0.314026508 | 0.65054637 |
| Frozen | 2004 | Sudan NCP-only1998 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Sudan NCP-only1998 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Sudan power-sharing interruption | All | 271 | -0.0175746876 | 0.318494108 | 0.659878769 |
| Frozen | 2004 | Sudan power-sharing interruption | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Sudan power-sharing interruption | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Syrian split1966 | All | 271 | -0.0179820051 | 0.310176957 | 0.641384942 |
| Frozen | 2004 | Syrian split1966 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Syrian split1966 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Syrian military displacement1970 | All | 270 | -0.017287422 | 0.326402313 | 0.67566868 |
| Frozen | 2004 | Syrian military displacement1970 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Syrian military displacement1970 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Kazakh eligibility1999 | All | 271 | -0.0177153419 | 0.313079266 | 0.649893469 |
| Frozen | 2004 | Kazakh eligibility1999 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Kazakh eligibility1999 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Kazakh eligibility2006 | All | 271 | -0.0177139119 | 0.313575962 | 0.650624079 |
| Frozen | 2004 | Kazakh eligibility2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | Kazakh eligibility2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | Nicaraguan accession1980 | All | 270 | -0.0178957891 | 0.310901403 | 0.643824611 |
| Frozen | 2004 | Nicaraguan accession1980 | Revolutionary accession | 33 | 0.0130744746 | 0.79343557 | 1 |
| Frozen | 2004 | Nicaraguan accession1980 | Marxist revolutionary accession | 18 | -0.000452334321 | 0.42260802 | 1 |
| Frozen | 2004 | Nicaraguan loss1984 | All | 270 | -0.018079364 | 0.307739861 | 0.636302885 |
| Frozen | 2004 | Nicaraguan loss1984 | Revolutionary accession | 33 | 0.0120838442 | 0.773849543 | 1 |
| Frozen | 2004 | Nicaraguan loss1984 | Marxist revolutionary accession | 18 | -0.00230257316 | 0.388085521 | 0.999846276 |
| Frozen | 2004 | FSLN reacquisition2009 | All | 270 | -0.0178231011 | 0.312005377 | 0.646591241 |
| Frozen | 2004 | FSLN reacquisition2009 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | FSLN reacquisition2009 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | FSLN reacquisition2011 | All | 270 | -0.0178487105 | 0.311662568 | 0.645682382 |
| Frozen | 2004 | FSLN reacquisition2011 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | FSLN reacquisition2011 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | FSLN no reacquisition before2016 | All | 269 | -0.0179501248 | 0.310110782 | 0.641806882 |
| Frozen | 2004 | FSLN no reacquisition before2016 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | FSLN no reacquisition before2016 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | MMD loss2006 | All | 270 | -0.0176814957 | 0.314615215 | 0.652635349 |
| Frozen | 2004 | MMD loss2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | MMD loss2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2004 | MMD no qualifying episode | All | 269 | -0.0177438427 | 0.313013985 | 0.649331046 |
| Frozen | 2004 | MMD no qualifying episode | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2004 | MMD no qualifying episode | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Soviet accession1921 | All | 270 | -0.017910487 | 0.31080147 | 0.643442058 |
| Frozen | 2009 | Soviet accession1921 | Revolutionary accession | 33 | 0.0138654468 | 0.810674158 | 1 |
| Frozen | 2009 | Soviet accession1921 | Marxist revolutionary accession | 18 | -2.56211723e-06 | 0.431404531 | 1 |
| Frozen | 2009 | Soviet loss1991 | All | 270 | -0.0179011621 | 0.311063087 | 0.64396873 |
| Frozen | 2009 | Soviet loss1991 | Revolutionary accession | 33 | 0.0130697857 | 0.792210284 | 1 |
| Frozen | 2009 | Soviet loss1991 | Marxist revolutionary accession | 18 | -0.000131103652 | 0.42804107 | 1 |
| Frozen | 2009 | Mongolian accession1924 | All | 270 | -0.0178991815 | 0.311014112 | 0.643930833 |
| Frozen | 2009 | Mongolian accession1924 | Revolutionary accession | 33 | 0.0137901188 | 0.809082784 | 1 |
| Frozen | 2009 | Mongolian accession1924 | Marxist revolutionary accession | 18 | -2.54775726e-06 | 0.431404836 | 1 |
| Frozen | 2009 | North Korean accession1946 | All | 270 | -0.0179594249 | 0.30991267 | 0.641371406 |
| Frozen | 2009 | North Korean accession1946 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | North Korean accession1946 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Mexican loss1996 | All | 270 | -0.0178911576 | 0.31130523 | 0.644478431 |
| Frozen | 2009 | Mexican loss1996 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Mexican loss1996 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Mexican loss2000 | All | 270 | -0.0179111885 | 0.310819043 | 0.643455829 |
| Frozen | 2009 | Mexican loss2000 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Mexican loss2000 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Ethiopian accession1992 | All | 270 | -0.0178820478 | 0.311510949 | 0.644921321 |
| Frozen | 2009 | Ethiopian accession1992 | Revolutionary accession | 33 | 0.0132604743 | 0.797419645 | 1 |
| Frozen | 2009 | Ethiopian accession1992 | Marxist revolutionary accession | 18 | -0.000100671723 | 0.42999222 | 1 |
| Frozen | 2009 | Sudan NCP-only1998 | All | 270 | -0.0177891148 | 0.313774612 | 0.649669958 |
| Frozen | 2009 | Sudan NCP-only1998 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Sudan NCP-only1998 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Sudan power-sharing interruption | All | 271 | -0.0176061735 | 0.3182405 | 0.658999863 |
| Frozen | 2009 | Sudan power-sharing interruption | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Sudan power-sharing interruption | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Syrian split1966 | All | 271 | -0.018013421 | 0.309929452 | 0.640521133 |
| Frozen | 2009 | Syrian split1966 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Syrian split1966 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Syrian military displacement1970 | All | 270 | -0.017318953 | 0.32614536 | 0.674783983 |
| Frozen | 2009 | Syrian military displacement1970 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Syrian military displacement1970 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Kazakh eligibility1999 | All | 271 | -0.0177467968 | 0.312827606 | 0.649016836 |
| Frozen | 2009 | Kazakh eligibility1999 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Kazakh eligibility1999 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Kazakh eligibility2006 | All | 271 | -0.0177453669 | 0.313324646 | 0.649748397 |
| Frozen | 2009 | Kazakh eligibility2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | Kazakh eligibility2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | Nicaraguan accession1980 | All | 270 | -0.0179273998 | 0.310650186 | 0.642950063 |
| Frozen | 2009 | Nicaraguan accession1980 | Revolutionary accession | 33 | 0.0130744746 | 0.79343557 | 1 |
| Frozen | 2009 | Nicaraguan accession1980 | Marxist revolutionary accession | 18 | -0.000452334321 | 0.42260802 | 1 |
| Frozen | 2009 | Nicaraguan loss1984 | All | 270 | -0.0181109459 | 0.307491808 | 0.635436659 |
| Frozen | 2009 | Nicaraguan loss1984 | Revolutionary accession | 33 | 0.0120838442 | 0.773849543 | 1 |
| Frozen | 2009 | Nicaraguan loss1984 | Marxist revolutionary accession | 18 | -0.00230257316 | 0.388085521 | 0.999846276 |
| Frozen | 2009 | FSLN reacquisition2009 | All | 270 | -0.0178546793 | 0.311753594 | 0.645715014 |
| Frozen | 2009 | FSLN reacquisition2009 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | FSLN reacquisition2009 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | FSLN reacquisition2011 | All | 270 | -0.0178803154 | 0.311410738 | 0.644806185 |
| Frozen | 2009 | FSLN reacquisition2011 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | FSLN reacquisition2011 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | FSLN no reacquisition before2016 | All | 269 | -0.0179818477 | 0.309858384 | 0.640929914 |
| Frozen | 2009 | FSLN no reacquisition before2016 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | FSLN no reacquisition before2016 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | MMD loss2006 | All | 270 | -0.0177131454 | 0.314360175 | 0.651751148 |
| Frozen | 2009 | MMD loss2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | MMD loss2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Frozen | 2009 | MMD no qualifying episode | All | 269 | -0.0177757129 | 0.312756983 | 0.648440886 |
| Frozen | 2009 | MMD no qualifying episode | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Frozen | 2009 | MMD no qualifying episode | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | continuous | Soviet accession1921 | All | 267 | -0.0183785682 | 0.299471329 | 0.619466617 |
| Corrected | continuous | Soviet accession1921 | Revolutionary accession | 33 | 0.0143521934 | 0.795529927 | 1 |
| Corrected | continuous | Soviet accession1921 | Marxist revolutionary accession | 18 | 0.000467501502 | 0.397398758 | 1 |
| Corrected | continuous | Soviet loss1991 | All | 267 | -0.0183649383 | 0.299808132 | 0.620177977 |
| Corrected | continuous | Soviet loss1991 | Revolutionary accession | 33 | 0.0135877637 | 0.777288724 | 1 |
| Corrected | continuous | Soviet loss1991 | Marxist revolutionary accession | 18 | 0.00047410627 | 0.39687542 | 1 |
| Corrected | continuous | Mongolian accession1924 | All | 267 | -0.0183671342 | 0.299680038 | 0.619954575 |
| Corrected | continuous | Mongolian accession1924 | Revolutionary accession | 33 | 0.0142740203 | 0.793835731 | 1 |
| Corrected | continuous | Mongolian accession1924 | Marxist revolutionary accession | 18 | 0.000464887781 | 0.397346269 | 1 |
| Corrected | continuous | North Korean accession1946 | All | 267 | -0.0184229739 | 0.298695472 | 0.617622776 |
| Corrected | continuous | North Korean accession1946 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | North Korean accession1946 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Mexican loss1996 | All | 267 | -0.0183570877 | 0.300001689 | 0.620586983 |
| Corrected | continuous | Mexican loss1996 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Mexican loss1996 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Mexican loss2000 | All | 267 | -0.0183728804 | 0.299611374 | 0.619762749 |
| Corrected | continuous | Mexican loss2000 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Mexican loss2000 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Ethiopian accession1992 | All | 267 | -0.0183469746 | 0.300220715 | 0.621069151 |
| Corrected | continuous | Ethiopian accession1992 | Revolutionary accession | 33 | 0.0137694633 | 0.78240052 | 1 |
| Corrected | continuous | Ethiopian accession1992 | Marxist revolutionary accession | 18 | 0.00046773227 | 0.397961508 | 1 |
| Corrected | continuous | Sudan NCP-only1998 | All | 267 | -0.0182543065 | 0.302413071 | 0.62575631 |
| Corrected | continuous | Sudan NCP-only1998 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Sudan NCP-only1998 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Sudan power-sharing interruption | All | 268 | -0.0180698607 | 0.306790114 | 0.635082052 |
| Corrected | continuous | Sudan power-sharing interruption | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Sudan power-sharing interruption | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Syrian split1966 | All | 268 | -0.0184834531 | 0.298597127 | 0.616529369 |
| Corrected | continuous | Syrian split1966 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Syrian split1966 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Syrian military displacement1970 | All | 267 | -0.0177940646 | 0.314241839 | 0.650252806 |
| Corrected | continuous | Syrian military displacement1970 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Syrian military displacement1970 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Kazakh eligibility1999 | All | 268 | -0.0182093825 | 0.301540945 | 0.625193394 |
| Corrected | continuous | Kazakh eligibility1999 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Kazakh eligibility1999 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Kazakh eligibility2006 | All | 268 | -0.0182082898 | 0.302017583 | 0.625909814 |
| Corrected | continuous | Kazakh eligibility2006 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | Kazakh eligibility2006 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | Nicaraguan accession1980 | All | 267 | -0.0183927553 | 0.299376915 | 0.619103902 |
| Corrected | continuous | Nicaraguan accession1980 | Revolutionary accession | 33 | 0.0135745909 | 0.778141151 | 1 |
| Corrected | continuous | Nicaraguan accession1980 | Marxist revolutionary accession | 18 | 8.33831612e-05 | 0.390320451 | 1 |
| Corrected | continuous | Nicaraguan loss1984 | All | 267 | -0.0185789187 | 0.29626174 | 0.611581229 |
| Corrected | continuous | Nicaraguan loss1984 | Revolutionary accession | 33 | 0.0125345723 | 0.757032821 | 1 |
| Corrected | continuous | Nicaraguan loss1984 | Marxist revolutionary accession | 18 | -0.00194531951 | 0.354315638 | 0.999900495 |
| Corrected | continuous | FSLN reacquisition2009 | All | 267 | -0.0183610769 | 0.299902635 | 0.620378128 |
| Corrected | continuous | FSLN reacquisition2009 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | FSLN reacquisition2009 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | FSLN reacquisition2011 | All | 267 | -0.0183610769 | 0.299902635 | 0.620378128 |
| Corrected | continuous | FSLN reacquisition2011 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | FSLN reacquisition2011 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | FSLN no reacquisition before2016 | All | 267 | -0.0183610769 | 0.299902635 | 0.620378128 |
| Corrected | continuous | FSLN no reacquisition before2016 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | FSLN no reacquisition before2016 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | MMD loss2006 | All | 267 | -0.0181754222 | 0.303038058 | 0.627928456 |
| Corrected | continuous | MMD loss2006 | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | MMD loss2006 | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | continuous | MMD no qualifying episode | All | 266 | -0.0182378342 | 0.301475187 | 0.624643561 |
| Corrected | continuous | MMD no qualifying episode | Revolutionary accession | 33 | 0.0137739777 | 0.782085782 | 1 |
| Corrected | continuous | MMD no qualifying episode | Marxist revolutionary accession | 18 | 0.000465363887 | 0.3973136 | 1 |
| Corrected | 2004 | Soviet accession1921 | All | 268 | -0.0176590462 | 0.314563699 | 0.652933392 |
| Corrected | 2004 | Soviet accession1921 | Revolutionary accession | 33 | 0.0138654468 | 0.810674158 | 1 |
| Corrected | 2004 | Soviet accession1921 | Marxist revolutionary accession | 18 | -2.56211723e-06 | 0.431404531 | 1 |
| Corrected | 2004 | Soviet loss1991 | All | 268 | -0.0176511891 | 0.314797935 | 0.653395608 |
| Corrected | 2004 | Soviet loss1991 | Revolutionary accession | 33 | 0.0130697857 | 0.792210284 | 1 |
| Corrected | 2004 | Soviet loss1991 | Marxist revolutionary accession | 18 | -0.000131103652 | 0.42804107 | 1 |
| Corrected | 2004 | Mongolian accession1924 | All | 268 | -0.0176478193 | 0.314776753 | 0.653421359 |
| Corrected | 2004 | Mongolian accession1924 | Revolutionary accession | 33 | 0.0137901188 | 0.809082784 | 1 |
| Corrected | 2004 | Mongolian accession1924 | Marxist revolutionary accession | 18 | -2.54775726e-06 | 0.431404836 | 1 |
| Corrected | 2004 | North Korean accession1946 | All | 268 | -0.0177097026 | 0.313632467 | 0.650773857 |
| Corrected | 2004 | North Korean accession1946 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | North Korean accession1946 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Mexican loss1996 | All | 268 | -0.0176406189 | 0.315053911 | 0.653933411 |
| Corrected | 2004 | Mexican loss1996 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Mexican loss1996 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Mexican loss2000 | All | 268 | -0.0176617439 | 0.314540784 | 0.652856253 |
| Corrected | 2004 | Mexican loss2000 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Mexican loss2000 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Ethiopian accession1992 | All | 268 | -0.0176318614 | 0.315254339 | 0.654362382 |
| Corrected | 2004 | Ethiopian accession1992 | Revolutionary accession | 33 | 0.0132604743 | 0.797419645 | 1 |
| Corrected | 2004 | Ethiopian accession1992 | Marxist revolutionary accession | 18 | -0.000100671723 | 0.42999222 | 1 |
| Corrected | 2004 | Sudan NCP-only1998 | All | 268 | -0.0175396816 | 0.317523829 | 0.659097764 |
| Corrected | 2004 | Sudan NCP-only1998 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Sudan NCP-only1998 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Sudan power-sharing interruption | All | 269 | -0.0173585822 | 0.321997719 | 0.66838721 |
| Corrected | 2004 | Sudan power-sharing interruption | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Sudan power-sharing interruption | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Syrian split1966 | All | 269 | -0.017764484 | 0.313642409 | 0.649886275 |
| Corrected | 2004 | Syrian split1966 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Syrian split1966 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Syrian military displacement1970 | All | 268 | -0.0170714926 | 0.329972225 | 0.684208656 |
| Corrected | 2004 | Syrian military displacement1970 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Syrian military displacement1970 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Kazakh eligibility1999 | All | 269 | -0.0174959232 | 0.316596114 | 0.658521244 |
| Corrected | 2004 | Kazakh eligibility1999 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Kazakh eligibility1999 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Kazakh eligibility2006 | All | 269 | -0.0174950847 | 0.317086176 | 0.659225977 |
| Corrected | 2004 | Kazakh eligibility2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | Kazakh eligibility2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | Nicaraguan accession1980 | All | 268 | -0.0176771952 | 0.314386398 | 0.652381713 |
| Corrected | 2004 | Nicaraguan accession1980 | Revolutionary accession | 33 | 0.0130744746 | 0.79343557 | 1 |
| Corrected | 2004 | Nicaraguan accession1980 | Marxist revolutionary accession | 18 | -0.000452334321 | 0.42260802 | 1 |
| Corrected | 2004 | Nicaraguan loss1984 | All | 268 | -0.0178609536 | 0.311196596 | 0.644815623 |
| Corrected | 2004 | Nicaraguan loss1984 | Revolutionary accession | 33 | 0.0120838442 | 0.773849543 | 1 |
| Corrected | 2004 | Nicaraguan loss1984 | Marxist revolutionary accession | 18 | -0.00230257316 | 0.388085521 | 0.999846276 |
| Corrected | 2004 | FSLN reacquisition2009 | All | 268 | -0.0176459144 | 0.314924592 | 0.65366247 |
| Corrected | 2004 | FSLN reacquisition2009 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | FSLN reacquisition2009 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | FSLN reacquisition2011 | All | 268 | -0.0176459144 | 0.314924592 | 0.65366247 |
| Corrected | 2004 | FSLN reacquisition2011 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | FSLN reacquisition2011 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | FSLN no reacquisition before2016 | All | 268 | -0.0176459144 | 0.314924592 | 0.65366247 |
| Corrected | 2004 | FSLN no reacquisition before2016 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | FSLN no reacquisition before2016 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | MMD loss2006 | All | 268 | -0.0174626623 | 0.318133617 | 0.66124167 |
| Corrected | 2004 | MMD loss2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | MMD loss2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2004 | MMD no qualifying episode | All | 267 | -0.0175237237 | 0.316539176 | 0.657976592 |
| Corrected | 2004 | MMD no qualifying episode | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2004 | MMD no qualifying episode | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Soviet accession1921 | All | 268 | -0.0176910586 | 0.314302708 | 0.652033928 |
| Corrected | 2009 | Soviet accession1921 | Revolutionary accession | 33 | 0.0138654468 | 0.810674158 | 1 |
| Corrected | 2009 | Soviet accession1921 | Marxist revolutionary accession | 18 | -2.56211723e-06 | 0.431404531 | 1 |
| Corrected | 2009 | Soviet loss1991 | All | 268 | -0.0176831155 | 0.314538722 | 0.652500072 |
| Corrected | 2009 | Soviet loss1991 | Revolutionary accession | 33 | 0.0130697857 | 0.792210284 | 1 |
| Corrected | 2009 | Soviet loss1991 | Marxist revolutionary accession | 18 | -0.000131103652 | 0.42804107 | 1 |
| Corrected | 2009 | Mongolian accession1924 | All | 268 | -0.0176798174 | 0.314515878 | 0.65252214 |
| Corrected | 2009 | Mongolian accession1924 | Revolutionary accession | 33 | 0.0137901188 | 0.809082784 | 1 |
| Corrected | 2009 | Mongolian accession1924 | Marxist revolutionary accession | 18 | -2.54775726e-06 | 0.431404836 | 1 |
| Corrected | 2009 | North Korean accession1946 | All | 268 | -0.0177415869 | 0.313374831 | 0.649882032 |
| Corrected | 2009 | North Korean accession1946 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | North Korean accession1946 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Mexican loss1996 | All | 268 | -0.0176725775 | 0.314793887 | 0.653036105 |
| Corrected | 2009 | Mexican loss1996 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Mexican loss1996 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Mexican loss2000 | All | 268 | -0.0176936424 | 0.314282298 | 0.651962296 |
| Corrected | 2009 | Mexican loss2000 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Mexican loss2000 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Ethiopian accession1992 | All | 268 | -0.0176637998 | 0.314994646 | 0.653465793 |
| Corrected | 2009 | Ethiopian accession1992 | Revolutionary accession | 33 | 0.0132604743 | 0.797419645 | 1 |
| Corrected | 2009 | Ethiopian accession1992 | Marxist revolutionary accession | 18 | -0.000100671723 | 0.42999222 | 1 |
| Corrected | 2009 | Sudan NCP-only1998 | All | 268 | -0.0175715722 | 0.31726415 | 0.658201328 |
| Corrected | 2009 | Sudan NCP-only1998 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Sudan NCP-only1998 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Sudan power-sharing interruption | All | 269 | -0.0173903873 | 0.321736353 | 0.667488862 |
| Corrected | 2009 | Sudan power-sharing interruption | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Sudan power-sharing interruption | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Syrian split1966 | All | 269 | -0.0177962235 | 0.313387159 | 0.649002124 |
| Corrected | 2009 | Syrian split1966 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Syrian split1966 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Syrian military displacement1970 | All | 268 | -0.0171033459 | 0.329707362 | 0.683305137 |
| Corrected | 2009 | Syrian military displacement1970 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Syrian military displacement1970 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Kazakh eligibility1999 | All | 269 | -0.0175276979 | 0.316336699 | 0.657624566 |
| Corrected | 2009 | Kazakh eligibility1999 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Kazakh eligibility1999 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Kazakh eligibility2006 | All | 269 | -0.0175268601 | 0.316827105 | 0.658330294 |
| Corrected | 2009 | Kazakh eligibility2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | Kazakh eligibility2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | Nicaraguan accession1980 | All | 268 | -0.017709129 | 0.314127404 | 0.65148682 |
| Corrected | 2009 | Nicaraguan accession1980 | Revolutionary accession | 33 | 0.0130744746 | 0.79343557 | 1 |
| Corrected | 2009 | Nicaraguan accession1980 | Marxist revolutionary accession | 18 | -0.000452334321 | 0.42260802 | 1 |
| Corrected | 2009 | Nicaraguan loss1984 | All | 268 | -0.0178928608 | 0.31094078 | 0.643928745 |
| Corrected | 2009 | Nicaraguan loss1984 | Revolutionary accession | 33 | 0.0120838442 | 0.773849543 | 1 |
| Corrected | 2009 | Nicaraguan loss1984 | Marxist revolutionary accession | 18 | -0.00230257316 | 0.388085521 | 0.999846276 |
| Corrected | 2009 | FSLN reacquisition2009 | All | 268 | -0.0176778593 | 0.314664924 | 0.652765935 |
| Corrected | 2009 | FSLN reacquisition2009 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | FSLN reacquisition2009 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | FSLN reacquisition2011 | All | 268 | -0.0176778593 | 0.314664924 | 0.652765935 |
| Corrected | 2009 | FSLN reacquisition2011 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | FSLN reacquisition2011 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | FSLN no reacquisition before2016 | All | 268 | -0.0176778593 | 0.314664924 | 0.652765935 |
| Corrected | 2009 | FSLN no reacquisition before2016 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | FSLN no reacquisition before2016 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | MMD loss2006 | All | 268 | -0.0174946325 | 0.317870782 | 0.660337514 |
| Corrected | 2009 | MMD loss2006 | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | MMD loss2006 | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
| Corrected | 2009 | MMD no qualifying episode | All | 267 | -0.0175559169 | 0.316274321 | 0.657066156 |
| Corrected | 2009 | MMD no qualifying episode | Revolutionary accession | 33 | 0.0132638268 | 0.797076528 | 1 |
| Corrected | 2009 | MMD no qualifying episode | Marxist revolutionary accession | 18 | -0.000105872509 | 0.429224347 | 1 |
