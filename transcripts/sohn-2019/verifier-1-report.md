**A. Outcomes** (23 claims in the claims file: 20 tested in the notebook, 3 treated as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| beh-slopes | not_reproduced | Cell 12: 6 of 8 slopes lie between 0 and 1. Eye Right Short is 1.110 [1.014, 1.206] and Eye Left Short is 1.011. |
| beh-overlap-prior | not_reproduced | Cell 15: the median of tp − 800 is +28.3 ms for Short and +47.6 ms for Long, so both are positive, and p = 0.073. Removing the 18 ms tp offset would not change either sign. |
| beh-sigmoid-increments | reproduced | Cell 17: the middle increment is larger in 7 of 8 conditions, two-sided signed-rank p = 0.0156. |
| beh-long-more-bias | reproduced | Cell 19: the Long slope is below the Short slope in 4 of 4 datasets (weighted and unweighted). |
| beh-bayes-model | partially_reproduced | Cell 21: the SD correlation is positive in 4 of 4, but bias R² ≥ 0.8 holds in only 2 of 4 (Eye Right 0.12, Eye Left 0.67). In the Eye datasets wm sits near its lower bound (0.013, 0.025), consistent with slopes of about 1 in the behaviour itself. |
| glm-prior-ts | not_reproduced | Cell 24: prior-dependent 75.0% (interval 61–85%) against 65 ± 6.5; ts-dependent 45.8% (interval 33–60%) against 27 ± 2.7. Neither is within tolerance. The prior interval does include 65%; the ts interval excludes 27%. |
| dfr-overlap-support | reproduced | Cell 26: the largest mean RMS, 6.86 spikes/s, is in the 480–640 ms bin and exceeds the shuffled-maximum 95th percentile of 3.11. The margin is thin: neighbouring bins reach 5.97 and 6.07, and the per-dataset peaks fall in three different bins. |
| pca-dimensionality | not_reproduced | Cell 29: 1 of 8 values is in range. The estimation epoch needs 2 PCs in all 4 datasets; production needs 2, 2, 5 and 4. |
| encoding-r2 | reproduced | Cell 31: reading (a), Hand Left, gives 0.9982 and 0.9960; reading (b), the mean of 4, gives 0.959 and 0.989. Both readings pass. The test has little specificity, though: the space has 2 PCs, random axes give median R² of 0.73–0.98, and the fraction of random axes scoring above the encoding axis is 0.03–0.48. |
| encoding-bayes-beats-linear | partially_reproduced | Cell 34: the Bayesian RMSE is lower in 4 of 4 for Long and 3 of 4 for Short (Hand Right Short +0.186). |
| short-in-long-control | reproduced, but the result carries no information | Cell 36: p = 0.25 ≥ 0.05. With 4 datasets the smallest possible p is 0.125, so this criterion cannot fail. The effect size points against the claim: Bayesian lower in 3 of 4, median dRMSE −0.108, close to the Short prior's −0.120. |
| neural-long-more-bias | reproduced | Cell 38: Long below Short in 4 of 4. Hand Right is nearly a tie (ratio 0.97). |
| speed-vs-projection | partially_reproduced | Cell 40: ρ = −0.941 (Short) and −0.878 (Long), both with p < 1e-6. Both are outside tolerance ([−0.814, −0.666] and [−0.561, −0.459]). |
| initial-speed-biased | reproduced | Cell 42: shallower than the unbiased profile in 7 of 8, p = 0.039. |
| speed-predicts-tp | partially_reproduced | Cell 44: ρ = −0.733 and −0.744, both with p < 0.001. Both are outside tolerance ([−0.638, −0.522] and [−0.572, −0.468]). |
| alt-speed-unmodulated | reproduced, but the result carries no information | Cell 47: p = 0.125 for both priors, which is the minimum possible, so the criterion cannot fail. All 8 slopes are positive and every bootstrap interval excludes 0. My synthetic null (problem 1) shows that attrition noise alone produces slopes of this size, so the data are uninformative in either direction. |
| alt-transient-parallel | not_reproduced | Cell 49: longest ts p = 0.039 (2 of 8 slopes positive); shortest ts p = 0.078. |
| alt-threshold-monotonic | not_reproduced | Cell 51: at 60% variance the median time of the minimum is −210 ms. That falls just outside the 200 ms window, since the −200 ms bin covers −220 to −200. The result depends on dimensionality: the 75% variant gives −80 ms and the full space gives −40 ms, both of which would count as partial. |
| gpfa-variance-inverted-u | not_reproduced | Cell 54: the quadratic coefficient is negative in 5 of 8, one-tailed p = 0.125. |
| gpfa-mean-sigmoid | reproduced | Cell 57: the middle increment is larger in 8 of 8 (p = 0.0078), and the Short slope is above Long in 4 of 4 (p = 0.0625). |
| rnn-curved-manifold | blocked (data_missing) | The API lists 2 assets, both NWB spike/trial files, and `wasGeneratedBy` is empty. There are no network models or code. Training new RNNs from the Methods would be a new study, not a test against this data. |
| rnn-perturbation | blocked (data_missing) | Same as above. |
| monkey-g | blocked (data_missing) | The API reports `numberOfSubjects: 1`, and the only path is `sub-Haydn/`. No part can be tested. |

Totals: reproduced 9 (2 of them carry no information), partially_reproduced 4, not_reproduced 7, blocked 3. No separate attempt record was among my materials, so these counts come from the claims file and the notebook.

**B. Problems**

1. [affects a conclusion] Cell 47, `attrition_rates` in the full space. I simulated 48 constant-rate Poisson units (mean rate about 6.6 spikes/s) with the session's trial counts and attrition. The full-space step speed over the support then has slope +1.08 ± 0.23 (Short) and +0.79 ± 0.13 (Long) per 100 ms, the same size as the observed +0.83 to +1.27 and +0.48 to +0.67. The positive slopes and the bootstrap intervals that exclude 0 are therefore what fewer trials alone produce. The bootstrap is also biased upward: for Eye Right Long the point estimate is 0.579 and the interval is 0.583–1.430. The notebook's effect-size evidence for this claim is invalid in both directions.
2. [affects a conclusion] Cells 29 and 31, the population analyses. The paper ran PCA on all units pooled across 17 sessions (536 units in H; Methods, "Analysis of single- and multi-unit activity"). Here there are 48 simultaneously recorded units from one session, with unnormalised rates, which yields 2 PCs per epoch. This likely drives the pca-dimensionality failure. It also explains why random axes in a 2-D space reach R² close to the encoding axis, which empties encoding-r2 and the Bayes-versus-linear comparison of specificity. The paper's 1000-random-axes check (Fig. S5) passes only for Hand Left (fraction above 0.025 and 0.028).
3. [affects a conclusion] short-in-long-control and alt-speed-unmodulated: with n = 4 the criterion cannot fail, so "reproduced" is guaranteed. For short-in-long, the control shows the same Bayesian advantage as the real test, which undercuts encoding-bayes-beats-linear.
4. [affects a conclusion] Cell 51: at 60% variance the Eye datasets keep 1 PC. The "distance" then becomes |x − ref|, and its minima are zero crossings (d_at_go_over_min reaches 177 and 126), not convergence. The outcome moves from not reproduced to partial depending on the number of components kept.
5. [affects a conclusion, magnitude only] Cells 40 and 44: Xu at Set rises with ts by construction (the axis runs from ts_min to ts_max), and speed falls with ts. Each within-dataset correlation is −0.75 to −1.00, so the pooled ρ mostly reflects shared dependence on ts. This probably explains why both pooled values are larger than the paper's. The paper's z-scoring per ts applies to its single-trial GPFA variant, which the notebook does not run.
6. [does not affect a conclusion] `weighted_fit` fits by weighted least squares but reports unweighted RMSE. The Methods do not specify which.
7. [does not affect a conclusion] Cell 54 / `fit_gpfa`: cross-validation picks 8 latents, the top of the (4, 8) grid, in all 4 datasets, with 100 EM iterations. The dimensionality was never really chosen, and convergence is unchecked.
8. [does not affect a conclusion] Cell 5: `tp` is a median 18 ms longer than go − set. The file's `is_outlier` flags 46 trials, while the Methods' mixture refit flags 10. The `iti` column description is inverted. The notebook documents all three. None of them changes a slope or a sign.
9. [does not affect a conclusion] Cell 24: the Long ts GLM uses the Long ts times (800–1200 ms after Ready). Eq. 3 in the paper is ambiguous on this point. Requiring ts dependence in either of two tests raises the rate, and the notebook computes no false-positive baseline.

Checks that passed:
- On synthetic inputs, `weighted_slope` (0.709 against a true 0.7), the `PCA` component count, `encoding_axis`, `increments`, and `BayesObserver.moments` (matches Monte Carlo to within 1 ms) behaved correctly. `BayesObserver.fit` recovered wm and wp (0.124/0.069 against 0.12/0.07), with offsets off by about 6 ms.
- Window indexing in cells 49 and 51 is correct.
- Every number comes from the loaded train file.
- The test file is not used, and the notebook found no duplicated recordings.

**C. What I could not check, and what output would have let me**

- Whether pca-dimensionality, encoding-r2 specificity and alt-transient depend on unnormalised rates. A variant with soft-normalised or z-scored rates (PC counts and the random-axis fraction) would settle it.
- Chance levels for glm-prior-ts. The fractions under shuffled prior and time labels are missing.
- Whether the dfr peak location is stable. A bootstrap over trials of the argmax bin is missing.
- Whether the speed decline across the support is real once attrition noise is controlled. Running cell 47 with a fixed trial count per bin (subsampled to the n at the support's end), or comparing against a shuffled-time null, would answer it.
- alt-transient-parallel in the full space and at other variance thresholds, as cell 51 does for alt-threshold-monotonic.
- GPFA convergence (log-likelihood per EM iteration) and a cross-validation grid wider than 8 latents.
- Tables S1–S3 and the supplementary figures are not in the PMC text, so I could not compare the fitted wm and wp, or the paper's random-axis R² values.
