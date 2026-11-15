**Verifier report, round 1: Sohn et al. 2019 on DANDI:000130 (version 0.241017.1448)**

The claims file lists 23 claims. 20 are tested across `reproduce_sohn_2019.ipynb` (NB1) and `gpfa_sohn_2019.ipynb` (NB2), and 3 are treated as blocked. I had no attempt record, so these counts come from the claims file and the notebooks only. My outcomes: 8 reproduced, 5 partially reproduced, 7 not reproduced, 3 blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| beh-slopes | not_reproduced | NB1 cell 8: with an intercept, 6 of 8 slopes lie in (0,1); both Eye Short slopes are above 1 (1.011, 1.107). Through the origin, 2 of 8. The criterion needs all 8 even for partial. |
| beh-overlap-prior | not_reproduced | Cell 11: pooled median tp − 800 is +27.8 ms for Short (should be negative) and +47.6 for Long. Rank-sum p = 0.068. |
| beh-sigmoid-increments | reproduced | Cell 13: the middle increment exceeds the extreme one in 7 of 8; two-sided signed-rank p = 0.0156. |
| beh-long-more-bias | reproduced | Cell 15: the Long slope is below the Short slope in 4 of 4 datasets (3 of 4 through the origin, which would be partial). |
| beh-bayes-model | partially_reproduced | Cell 17: bias R² ≥ 0.8 in only 2 of 4 datasets (Eye Left 0.67, Eye Right 0.13). The SD correlation is positive in 4 of 4. |
| glm-prior-ts | not_reproduced | Cell 19: prior-dependent 79.2% (expected 65 ± 6.5), ts-dependent 50.0% (expected 27 ± 2.7). Both are outside tolerance, but see problem 1. |
| dfr-overlap-support | reproduced | Cell 22: the largest RMS difference (6.88) falls in the 480..640 ms bin and exceeds the shuffle 95th percentile (3.13). |
| pca-dimensionality | not_reproduced | Cell 26: 0 of 8 counts in range (estimation k = 2 in all datasets; production k = 2, 2, 4, 4) with unnormalised rates, as the claims file fixes. z-scored rates would give 8 of 8 (problem 3). |
| encoding-r2 | reproduced | Cell 28: Hand Left R² = 0.996 (Short) and 0.977 (Long); the mean over 4 datasets is 0.958 and 0.982. Both readings are within tolerance, but random axes score almost as well (problem 6). |
| encoding-bayes-beats-linear | partially_reproduced | Cell 31: the Bayesian RMSE is lower in 4 of 4 datasets for Short and 3 of 4 for Long (Hand Left Long, +0.10). |
| short-in-long-control | reproduced | Cell 33: signed-rank p = 0.125 (single axis) and 0.25 (averaged axis), both ≥ 0.05. The test cannot fail with 4 datasets, and the Bayesian model is better in 4 of 4 on the single axis (problem 8). |
| neural-long-more-bias | partially_reproduced | Cell 35: the Long slope is below the Short slope in 3 of 4 datasets; Hand Right gives 0.0486 vs 0.0470. |
| speed-vs-projection | partially_reproduced | Cell 37: pooled r = −0.92 (Short) and −0.84 (Long), both p < 0.05 and both outside tolerance. The speed-per-tp variant is also outside. |
| initial-speed-biased | not_reproduced | Cell 39: the measured slope is shallower than the unbiased one in 7 of 8, but the signed-rank p = 0.0547 misses the 0.05 threshold. |
| speed-predicts-tp | partially_reproduced | Cell 41: Short r = −0.61 is within −0.58 ± 0.058; Long r = −0.63 is outside. |
| alt-speed-unmodulated | reproduced | Cell 43: p = 0.25 (Short) and 0.125 (Long), as the criterion asks. The test cannot reject, and the positive slopes it reports come mostly from attrition noise (problem 4). |
| alt-transient-parallel | reproduced | Cell 45: signed-rank p = 0.195 (shortest ts) and 1.0 (longest ts), both ≥ 0.05. |
| alt-threshold-monotonic | not_reproduced | Cell 47: at the criterion's 60% variance, the median time of the minimum is −250 ms (4 of 32 in the last 40 ms). At 75% it is −160 ms, which would be partial. |
| gpfa-variance-inverted-u | not_reproduced | NB2 cell 8: the quadratic coefficient is negative in 5 of 8; one-tailed p = 0.074 (problems 9 and 10). |
| gpfa-mean-sigmoid | reproduced | NB2 cell 10: increments p = 0.0156 (7 of 8); the Short slope is higher in 4 of 4 datasets (p = 0.0625, the same as the paper). |
| rnn-curved-manifold | blocked (data_missing) | The archive holds 2 assets (train and test NWB of sub-Haydn), with no networks or simulations. The claim has no criterion either. |
| rnn-perturbation | blocked (data_missing) | Same as above. |
| monkey-g | blocked (data_missing) | The archive lists one subject (Haydn) and 2 files; no part can be tested. |

### B. Problems

1. **[affects a conclusion] NB1 cell 19 (glm-prior-ts).** The ts-dependence GLM for the Long prior uses the Short prior's windows (480–800 ms). The criterion says "that prior's 5 time indicators", and the Methods say "Since values of ts were different between the priors, we used two distinct GLMs". Both point to Long windows ending at 800–1200 ms. The markdown in cell 20 calls the same-window version variant (i), but no Long-window version was run. The ts fraction (50%) could move, and if it landed within 27 ± 2.7% the outcome would become partial.
2. **[affects a conclusion] `rsg.production_rates`, used in cells 24, 37, 39 and 41.** It groups by ts alone, so the ts = 800 production trajectory pools Short and Long trials. The speed table shows identical speed and n for Short-800 and Long-800 (e.g. Eye Left 5.875, n = 58). The Methods build 16 matrices, separate per prior, so there should be 10 production trajectories per dataset, not 9. This shifts one point per prior in speed-vs-projection and speed-predicts-tp, and the production PCA. speed-predicts-tp Long (−0.63 against a bound of −0.572) is the outcome most likely to move.
3. **[affects a conclusion] Cell 26 (pca-dimensionality), and through it the encoding claims.** The outcome depends entirely on an unstated normalisation choice. Unnormalised: 0 of 8. Soft-normalised: 6 of 8 (partial). z-scored: 8 of 8. The paper says nothing about normalisation, and the claims file's "not normalised" is one reading of that silence. Every encoding analysis also runs in a 2-PC space, where the paper had 3–4 PCs, and none was re-run in the normalised space.
4. **[affects a conclusion] Cell 43 (alt-speed-unmodulated): the measure is confounded, and the claims file misreads the paper.** The Methods compute speed "in the full neural space to avoid any potential distortion by smoothing and PCA", which means unsmoothed rates; the criterion asks for smoothed rates.
   - Separately, step distance with attrition rises as trials drop out. I simulated constant-rate Poisson units through the notebook's `support_slope` and got relative slopes of +2.3 to +2.7 per s, above the observed 0.65–0.7.
   - The bootstrap intervals are also biased upward: point estimates sit at the bottom of their intervals.
   - The "reproduced" outcome comes from a test that cannot reject, and the reported effect sizes measure noise, not speed modulation.
5. **[does not affect a conclusion] Claims file, beh-slopes.** The header says the supplement was unavailable, but `paper/` contains it. Table S1 shows the paper tested median slopes across sessions with a signed-rank test. The criterion's demand that all 8 per-condition intervals exclude 0 and 1 in one session is stricter than the paper's claim. Table S3 (monkey H wm 0.027–0.085, wp 0.077–0.086) could also have been compared with cell 17's fits (wm 0.014–0.117, wp 0.090–0.106). They roughly agree, though Eye Right wm sits low.
6. **[does not affect a conclusion] Cell 28 (encoding-r2).** In the 2-D space, random unit vectors reach a median R² of 0.72–0.99, and 1.8–42% of them match or beat u. The paper's Figure S5 reports that random axes far from u fit poorly. The criterion is met, but the result says little that is specific to u.
7. **[does not affect a conclusion] Cell 39 (initial-speed-biased).** p = 0.0547 is a borderline miss with n = 8, while the paper combined 16 dataset-priors from two animals. It also uses the pooled-800 production PCA from problem 2.
8. **[does not affect a conclusion] Claims file, short-in-long-control.** With 4 datasets the minimum two-sided p is 0.125, so the criterion cannot return "not reproduced". The notebook says so; the claims file does not acknowledge it for this claim, though it does for alt-speed-unmodulated.
9. **[affects a conclusion] NB2 cell 5.** All four final GPFA fits stopped at the 500-iteration EM cap, and the notebook neither flags non-convergence nor checks sensitivity to it. Given p = 0.074 for gpfa-variance-inverted-u, convergence could matter. Cross-validation also picked x_dim = 8 every time, the top of the allowed range.
10. **[affects a conclusion] NB2 cell 6.** The Figure 6C legend says "We z-scored Xu of all trials". The notebook z-scores within each dataset and prior. Z-scoring across both priors of a dataset rescales the 8 coefficients unequally, which can reorder the signed-rank ranks around p = 0.074. That reading was not run.
11. **[does not affect a conclusion] `rsg.glm_bic`.** It returns None when a fit fails, which turns a failure into "not dependent". Cell 19 reports 0 failed fits, so it has no effect here.
12. **[does not affect a conclusion] `rsg.estimation_rates`, cell 19.** Attrition uses the nominal ts, so for trials whose Set came up to 23.5 ms early, the last bin includes up to 23.5 ms after Set. That is shorter than the Set-evoked latency, so the effect is negligible.

Helper checks on synthetic inputs all passed:
- `wls` matches statsmodels exactly.
- `increments`, `encoding_axis` and `smooth` (constant input preserved) are correct.
- `estimation_rates` with attrition returns the true pre-Set rate, and without attrition shows the expected post-Set contamination.
- `fit_bls` recovers known (wm, wp) within about 0.01 and the offsets within about 10 ms.

### C. What I could not check

- **Figures.** Only figure objects are saved. Image outputs, or the plotted values printed, for cells 9 and 29 would let me check the plots.
- **GLM with Long-prior windows (problem 1).** Fractions from a ts model on Long trials using windows ending at 800–1200 ms.
- **Production split by prior (problem 2).** Speed tables and correlations recomputed with separate Short-800 and Long-800 trajectories.
- **Encoding claims in a normalised space (problem 3).** encoding-r2 and its RMSE and slope comparisons in z-scored and soft-normalised PC spaces, with the random-axis reference.
- **Unsmoothed speed with a null (problem 4).** alt-speed-unmodulated without smoothing, and with a matched-trial-count or shuffled-time null that removes the attrition noise trend.
- **GPFA convergence (problems 9 and 10).** Final log-likelihood per EM iteration and a refit with a higher iteration cap, plus gpfa-variance-inverted-u with Xu z-scored across both priors.
- **Data loading.** I could not confirm it without downloading. The trial and unit counts (1160 trials, 54 units, 2 assets) are consistent with the archive's file list and metadata.
