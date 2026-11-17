I checked `claims/strickland-2022.yaml` against the paper and its Source Data. After my corrections the file is fit for an attempt (`ready: true`), with three points left open.

**Checker:** `claims/strickland-2022.yaml: 30 claims, 29 quotes, 6 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim.** All are recorded under `checks`, and each rests on the paper's own Source Data.
- **Shared method, lesion shuffle:**
  - **Which clusters:** the lesion sheets (Fig. 3c, 3d, 5c, 5d middle) shuffle k1-k9, k10-k21, k1-k3 and k6-k9.
  - **Cue shuffle:** values were permuted across the 14 intervals within each regressor. This is new reading s-c.
  - **Outcome shuffle:** the shuffled rows average to about 0, which no permutation of betas gives. They fit firing shuffled across trials before regression, as the Results say. This is new reading s-d.
  - **Percentages:** PCA of the averaged shuffled matrices gives the paper's 80.0/16.8 and 61.3/29.8%. So the paper ran one PCA on the averaged matrix, not one per iteration with the results averaged.
  - The old readings s-a, s-b and per-iteration PCA are kept as variants.
- **fig5c-phasic-lesion, fig5d-tonic-lesion:** brought into line with the above. Phasic is k1-k3 only, since k1-k5 is not what Source Data shuffle.
- **fig4f-outcome-hubs:** the networks are now k1-k3 and k6-k9, as in the Results and Source Data Fig. 4f (265 and 613 units). The Methods' 1-5 and 7-10 are variants.
- **Shared mapping, fig3e-network-anatomy, fig5e-no-anatomical-bias:** the paper's differential is a region's share of one network's units minus its share of the other's (DPG: 62/505 - 83/1307 = 5.93). The file had "minus the overall proportion", which does not give the paper's values. Corrected.
- **fig2g-cue-anatomy:** the subnetwork share is 43.6%, not 46%.
- **fig4b-phasic-network:** k1-k3 no longer have to beat all 11 clusters on the phasic index, only each of k6-k9. The paper contrasts phasic with tonic clusters only, and its Methods count clusters 1-5 as phasic. The Methods' "5s following shock offset" is now named as open, with two readings.
- **fig5e-no-anatomical-bias:** results between 1 and 1.5 times the paper's largest differential had no outcome. They are now "partially reproduced".
- **cue-outcome-membership-independent:** the file said the chi-square test reproduces 2.27 and 1.17 exactly. It gives 2.30 and 1.17; the wording is corrected and a 2x2 variant is added.

All other cited numbers match: the Fig. 1c means and the repeated-measures F(2,144) = 116.2, the cluster sizes, the Fig. 2c values, the two Fig. 2d R² readings, the Fig. 2f means, the region counts, the Fig. 4g fractions, and the Supplementary Table 1 and 2 totals.

**Open:**
- **fig2c-cue-pc1-ordered, fig4c-positive-prediction-error:** standard PCA on the paper's own matrices gives 47.1% (cue) and 24.2% (outcome), against the reported 29.7% and 17.7%. None of the variants I tried gives the reported values, so the method behind them is unknown. fig2c-pc1-contribution depends on the 29.7%. The network and beta PCAs do reproduce. The analysis code in the data set may settle this.
- **fig2f-cue-hubs, fig4f-outcome-hubs:** which t-tests were significant is shown only by asterisks in the main figures, and I had no image of those figures to read them.
- **fig1c-suppression-order:** the paper does not state the ANOVA design.

I made no commit or push.
