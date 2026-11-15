**Verifier report, round 1: Sohn et al. 2019 on DANDI:000130 (0.241017.1448)**

The claims file lists 23 claims. The notebook tests 20 and treats 3 as blocked. My outcomes: 10 reproduced, 3 partially reproduced, 7 not reproduced, 3 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| beh-slopes | not_reproduced | With an intercept, 6 of 8 slopes are in (0, 1); Eye Left Short is 1.011 and Eye Right Short is 1.110 (cell 12). Without an intercept, 2 of 8 are. Fails under both readings. |
| beh-overlap-prior | not_reproduced | Pooled median bias is +28.3 ms for Short (it should be negative) and +47.6 ms for Long; rank-sum p = 0.073 (cell 14). |
| beh-sigmoid-increments | reproduced | Middle increment exceeds extreme in 7 of 8; signed-rank p = 0.0156 (cell 16). I recomputed the exact p by hand. |
| beh-long-more-bias | reproduced | Long slope is below Short in 4 of 4 with an intercept (cell 18). Under the no-intercept form written in the Methods and Table S1 it is 3 of 4, which would be partial. |
| beh-bayes-model | partially_reproduced | Bias R2 ≥ 0.8 in only 2 of 4 datasets under either R2 reading (Eye Left 0.67, Eye Right 0.12). The SD correlation is positive in 4 of 4 (cell 20). |
| glm-prior-ts | not_reproduced | Prior-dependent units are 79.2% (expected 65 ± 6.5). Time-dependent units are 45.8% (expected 27 ± 2.7; 95% CI 31.4 to 60.8 excludes 27). Neither is within tolerance (cell 22). |
| dfr-overlap-support | reproduced | The largest mean RMS difference, 6.86 spikes/s, falls in the R480..640 bin and exceeds the shuffle 95th percentile of 3.09 (cell 24). The S0..160 bin is close behind at 6.0. |
| pca-dimensionality | not_reproduced | 1 of 8 values in range: estimation needs 2 PCs in all 4 datasets; production needs 2, 2, 5, 4 (cell 28). See problem 3 for the smoothing reading that was not fully run. |
| encoding-r2 | reproduced | Hand Left gives 0.994 / 0.986, and the mean over datasets gives 0.955 / 0.986; both clear the tolerance under both readings (cell 30). The test has little specificity: random axes have median R2 0.75 to 0.99, and in 7 of 8 dataset-priors at least 10% of random axes score at least as high. |
| encoding-bayes-beats-linear | not_reproduced | The Bayesian RMSE is lower in 3 of 4 datasets for each prior, so neither prior reaches 4 of 4. The weighted RMSE gives the same counts (cell 32). |
| short-in-long-control | reproduced | Signed-rank p = 0.25 ≥ 0.05 with both axis constructions (cell 34). With 4 datasets this test cannot go below p = 0.125, so it cannot fail (problem 6). |
| neural-long-more-bias | reproduced | Long slope is below Short in 4 of 4 (cell 36). Hand Right is nearly tied, 0.0504 against 0.0496. |
| speed-vs-projection | partially_reproduced | Pooled r is −0.926 (Short) and −0.834 (Long), both p < 1e-5, both outside tolerance. The variant dividing speed by the Set-to-Go time gives −0.916 and −0.908, also outside (cell 38). |
| initial-speed-biased | reproduced | The measured slope is shallower than the unbiased profile in 7 of 8; signed-rank p = 0.039, which I checked by hand (cell 40). |
| speed-predicts-tp | partially_reproduced | Pooled r is −0.720 and −0.699, p < 0.001, both outside tolerance. The divided-speed variant gives −0.850 and −0.838 (cell 42). |
| alt-speed-unmodulated | reproduced | Meets the criterion's letter only: p = 0.125 for both priors (cell 44). Every slope is positive (8 of 8), and 7 of 8 remain positive without attrition, which points against the claim (problem 7). |
| alt-transient-parallel | reproduced | Signed-rank p = 0.109 for the shortest ts and 1.0 for the longest (cell 46). The slopes are large and of mixed sign: the median for the shortest ts is +76 per s. |
| alt-threshold-monotonic | not_reproduced | Median time of the minimum distance is −230 ms at 60% variance and −200 ms at 75%. That is outside the last 200 ms, and 29 of 32 curves rise again by Go (cell 48). |
| gpfa-variance-inverted-u | not_reproduced | Quadratic coefficient is below zero in 6 of 8; one-tailed p = 0.0742, which I checked by hand (cell 50). The EM did not converge (problem 2). |
| gpfa-mean-sigmoid | reproduced | Middle increment exceeds extreme in 8 of 8, p = 0.0078; Short slope is above Long in 4 of 4, p = 0.0625 (cell 52). |
| rnn-curved-manifold | blocked (data_missing) | The archive holds 2 NWB files of one subject (Haydn) and no network data. Code is "available from the corresponding author on request". |
| rnn-perturbation | blocked (data_missing) | Same as above. No part can be tested. |
| monkey-g | blocked (data_missing) | `numberOfSubjects: 1`. Archive searches for Jazayeri, Sohn, RSG and "Bayesian computation" find no other dataset from this task. No part can be tested. |

### B. Problems

1. **[affects a conclusion] Claims file, header and beh-bayes-model.** The header says the supplementary tables were not available, and beh-bayes-model says "Table S3 was not available for comparison". Both are in `paper/`:
   - Table S1 states the regression as `tp = βts + ε` and tests the median slope across sessions. The claims file's added "in every condition" requirement, with per-condition confidence intervals, is stricter than the paper's test.
   - Table S3 gives monkey H wm. Eye Right is 0.027 ± 0.009 against the notebook's 0.013; Eye Left is 0.043 ± 0.016 against 0.025. The notebook's Eye values are about 1.5 SD low; Hand Right and Hand Left are within about 1.3 SD.
   - Low wm makes te nearly linear in ts for the Eye datasets, which weakens the Bayesian-versus-linear comparison in encoding-r2, encoding-bayes-beats-linear and short-in-long-control.
2. **[affects a conclusion] Cell 50, `EM_ITERS = 200`.** This is the author's own choice, not from the criterion or the paper. The log-likelihood is still rising by 7 to 11 per 10 iterations in all 4 datasets. gpfa-variance-inverted-u sits at p = 0.074, near the threshold, so it could move. gpfa-mean-sigmoid uses the same fit.
3. **[affects a conclusion] Cells 26 and 28, `rsg.smooth`.** The Methods say "Gaussian smoothing kernel width: 40 ms". Reading that as SD = 40 ms is one option; SD = 20 ms, or width as FWHM, are others. Only the unsmoothed estimation epoch was run as a variant, giving 3, 3, 4, 6 (3 of 4 in range). The production epoch was never run under another reading. pca-dimensionality could become partial (it needs 4 of 8), and every downstream projection uses the 2-PC estimation space.
4. **[does not affect a conclusion] Cell 30.** The random-axis reference shows R2 does not single out u in 2 dimensions (R2_ts ≈ R2_te as well). The paper's Figure S5 has R2 falling with angle from u; that is not seen here except in Hand Left Short. It is shown, but not discussed as a limit on encoding-r2.
5. **[affects a conclusion] Cell 44, bootstrap.** Resampling trials with replacement cuts the number of unique trials, which adds noise to the averaged rates and lengthens the steps. As a result the point estimate falls below the bootstrap interval, for example Hand Left Short 3.95 against [4.59, 16.46]. These intervals are reported as the effect size the criterion relies on, so they are not valid as confidence intervals.
6. **[affects a conclusion] Claims file, short-in-long-control and alt-speed-unmodulated.** Both are absence claims judged by a signed-rank test over 4 datasets. The smallest two-sided p is 0.125, so these criteria cannot produce "not reproduced". alt-speed-unmodulated acknowledges this; short-in-long-control does not. short-in-long-control also leaves out the paper's actual evidence, the prior × model interaction (F1,7 = 161, p < 1e-5). Here, the Short In Long ΔRMSE pattern (3 of 4 negative) resembles the Short prior's own.
7. **[affects a conclusion] Cell 44, `support_speed_slope`.** With attrition, the trials averaged per bin drop from about 130 to about 25, so step length from noise alone rises over the support. The fixed-trial variant reduces the trend but 7 of 8 slopes stay positive. The "reproduced" outcome rests only on the test's inability to fail.
8. **[does not affect a conclusion] Cell 48, `go_rates`.** Smoothing with `mode="nearest"` truncated at Go distorts the last 2 to 4 bins, exactly where the criterion looks. At 60% variance, Eye datasets keep 1 PC, so "distance" there is |x1 − x2|, and its minimum is a crossing point, not convergence. Both thresholds still give a median below −200 ms.
9. **[does not affect a conclusion] Cells 22, 26, 40 and 50.** Windows are placed at nominal ts after `ready_time`, but actual Set falls within ±24 ms of that (cell 5). The Set response starts at about 80 ms (cell 9), so contamination is small.
10. **[does not affect a conclusion] Cell 0.** It says 0.241017.1448 is "the dandiset's only published version". The archive also lists 0.220113.0407.
11. **[does not affect a conclusion] Cells 12 and 18.** The weighting matches the paper. The intercept choice is ambiguous; both readings were run, and only beh-long-more-bias depends on it (4 of 4 against 3 of 4).

Data provenance, unit selection (48 of 54) and the trial selection follow the claims file. There is no train/test leakage, since only the train file is used. Units are spikes/s and ms throughout. I recomputed the signed-rank p-values in cells 16, 40 and 50 by hand and they match. The helper functions passed synthetic tests: `bin_counts`, `encoding_axis`, `wls` against statsmodels WLS, `n_components`, `bls_estimate`/`bls_predict` against a Monte Carlo simulation, parameter recovery by `fit_bls` (wm 0.082 against a true 0.08), and the attrition counts in `estimation_rates`.

### C. What I could not check, and the output that would settle it

- **GPFA convergence.** Needed: the log-likelihood trace and the quadratic coefficients and p-values from a fit run to convergence (500 iterations or a tolerance).
- **PCA under other smoothing readings.** Needed: the number of PCs per dataset and epoch at SD = 20 ms, at FWHM = 40 ms, and unsmoothed, for both epochs.
- **Noise in speed estimates.** Needed: a noise-only speed per ts and per support bin (split-half or label-shuffle), to separate real speed changes from noise driven by trial counts. This bears on initial-speed-biased, speed-vs-projection and alt-speed-unmodulated.
- **Edge effects in alt-threshold-monotonic.** Needed: the time of the minimum when rates are smoothed over a window extending past Go and then cropped.
- **Nominal versus actual Set times.** Needed: the GLM fractions and the GPFA last-bin states with windows ending at the actual `set_time`.
- **Whether this is the paper's GPFA session.** The notebook says the 48 units match the paper's 48-unit GPFA session. Nothing in the files confirms it; the session date or unit count from the paper's Figure 6 would.
