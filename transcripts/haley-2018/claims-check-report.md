The claims file for haley-2018 is ready for an attempt. I made 8 corrections, all taken from the paper or its code, and logged a `checks` entry at the end of `claims/haley-2018.yaml`.

**Checker result** (same before and after my edits): `claims/haley-2018.yaml: 30 claims, 30 quotes, 22 statistical values, 0 problems`

I also checked the code facts in the file's opening comment against the paper's repository (github.com/jesshaley/haley_hampton_marder_2018, commit 83f5904). They hold, including the two example preparations, the Figure 8B control columns, the 10 s bins, the Bonferroni factors, the Welch t-tests, the 480 s window bug, and the two-way ANOVA in statistics.R that has no ganglion term.

**Changes, by claim**
- **Minimum membrane potential method (opening comment, affects fig4bc-membrane-potential and intact-depolarize-in-acid):** the Methods take the minimum of the unfiltered recording between bursts, while the code uses the slow-wave troughs. The Methods reading is now the main one and the code's is a variant, because the protocol puts Methods before code.
- **Ganglion comparison method (opening comment) and fig8a-ganglion-difference:** the legend calls the ANOVA "Multivariate", while the Methods and code use the univariate test. Both are now named readings, and the criterion runs each of them with both contrast codings.
- **fig2a-stg1-traces:** the statement said the rhythm "changed at 5.5", which picked one of the two readings its own criterion leaves open. It now uses the paper's wording.
- **fig3d-stg-frequency:** "did not vary significantly" becomes the paper's "relatively invariant". The criterion still judges it as absence on the acid ANOVA.
- **fig4bc-membrane-potential:** "constant" becomes the paper's "relatively constant".
- **fig6a-cg2-less-rhythmic:** "at or near control" had no rule for "near". It is replaced by a named reading: each step from 6.1 to 9.3 is more rhythmic than at 5.5, 9.8 and 10.4.
- **gastric-like-rhythm-counts:** the definition of a gastric mill period is cited to paragraph 3 of that section, not paragraph 4.
- **intact-depolarize-in-acid:** the source is Discussion paragraph 6, not 5.

**Still open (recorded in the file)**
- **Statistics tables:** the four tables are images not in the text, and no PDF was supplied. So no F, t or exact p-value is recorded, and which ANOVAs were not significant rests on the Results wording.
- **Spike2 burst settings:** I did not check which parameter each value in the script's `BurstMake` call sets against the Spike2 manual.
- **Thresholds the paper doesn't give:** gastric-conditions-co-occur and the two control-variability claims (fig3s2, fig7s2) use thresholds the paper does not give. Each criterion says so.
- **Unclaimed observation:** the Discussion's remark that neurons with a recording electrode in them were more labile has no claim. The paper gives no measure for it, and it is not a main finding.

I read only the paper and its code, not the dataset. Nothing was committed or pushed.
