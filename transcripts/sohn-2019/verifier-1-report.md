**A. Outcomes (24 claims in `sohn-2019.yaml`; the notebooks test 21 and treat 3 as blocked)**

| claim | my outcome | reason |
|---|---|---|
| beh-slopes | not_reproduced | Main reading (with intercept), cell 13: 6 of 8 slopes lie in (0,1). Eye Left Short is 1.011 and Eye Right Short is 1.110. Through the origin, 2 of 8 do. |
| beh-overlap-prior | not_reproduced | Cell 16: the Short median tp−800 is +28.3 ms, positive when the criterion needs it negative. Pooled rank-sum p = 0.073. |
| beh-sigmoid-increments | reproduced | Cell 18: the middle increment exceeds the extreme one in 7 of 8 conditions; two-sided signed-rank p = 0.0156. |
| beh-long-more-bias | reproduced | Cell 20: Long slope below Short in 4 of 4 with intercept. Through the origin (the Methods' and Table S1's equation) it is 3 of 4, which would be partial. |
| beh-bayes-model | partially_reproduced | Cell 22: SD correlation is positive in 4 of 4, but bias R² ≥ 0.8 holds in only 2 of 4 (Eye Left 0.670, Eye Right 0.122). |
| glm-prior-ts | not_reproduced | Cell 26: prior-dependent 79.2% (tolerance 58.5 to 71.5); ts-dependent 45.8% under reading (a) and 50.0% under (b) (tolerance 24.3 to 29.7). |
| dfr-overlap-support | reproduced | Cell 28: the largest RMS difference, 6.86 spikes/s, is in the 480–640 ms bin, above the shuffle 95th percentile of 3.15. |
| pca-dimensionality | not_reproduced | Cell 32: estimation k = 2,2,2,2 and production k = 2,2,4,5, so 1 of 8 values is in range. |
| encoding-r2 | reproduced | Cell 34: Hand Left gives 0.9957 and 0.9774; the 4-dataset mean gives 0.9587 and 0.9822. Both readings are within tolerance. Random axes in the 2-PC space reach median R² 0.69–0.97, so the paper's claim that the match is specific to u (Figure S5) does not hold here. |
| encoding-bayes-beats-linear | partially_reproduced | Cell 37: Bayesian RMSE is lower in 4 of 4 for Short and 3 of 4 for Long (Hand Left Long +0.101). |
| short-in-long-control | reproduced (by criterion, uninformative) | Cell 39: p = 0.25 and 0.125. With 4 datasets a two-sided signed-rank test cannot go below 0.125. The Bayesian model is better in 3 of 4, the same direction as the Short prior. |
| neural-long-more-bias | partially_reproduced | Cell 41: Long slope below Short in 3 of 4. Hand Right is 0.0486 against 0.0470. |
| speed-vs-projection | partially_reproduced | Cell 46: r = −0.932 and −0.874, both p < 1e-6 but outside tolerance (−0.74±0.074, −0.51±0.051). |
| initial-speed-biased | not_reproduced | Cell 48: measured slope is shallower in 7 of 8, but the signed-rank p = 0.0547 is not below 0.05. |
| speed-predicts-tp | partially_reproduced | Cell 50: r = −0.719 (p = 3.5e-4) and −0.744 (p = 1.7e-4), both outside tolerance. |
| alt-speed-unmodulated | reproduced (by criterion, uninformative) | Cell 53: p = 0.25 and 0.125, which the criterion admits cannot fail. The effect size points the other way: slopes are positive in 7 of 8 (20–56% change over the support) and partly an attrition artefact (B5). |
| alt-transient-parallel | reproduced | Cell 55: p = 0.195 for the shortest ts and 1.0 for the longest. Shortest-ts distances do change, by a median of 14.5 against a median distance of 18.2 over 200 ms, with mixed sign. |
| alt-threshold-monotonic | not_reproduced | Cell 57: at the criterion's 60% variance the median time of the minimum is −230 ms, outside the last 200 ms. At 75% it is −160 ms, which would be partial. |
| gpfa-variance-inverted-u | not_reproduced (borderline) | GPFA cell 6: 6 of 8 coefficients negative, one-tailed p = 0.0547. Seed variants in cell 9 give 0.039 to 0.055; 4 latent dimensions give 0.098. |
| gpfa-mean-sigmoid | reproduced | GPFA cell 11: middle increment exceeds extreme in 7 of 8, p = 0.0156; Short slope above Long in 4 of 4 (p = 0.0625, the paper's value). |
| rnn-curved-manifold | blocked (data_missing) | The archive holds two NWB files of one subject and no network models. The paper gives code on request only. |
| rnn-perturbation | blocked (data_missing) | Same reason. |
| monkey-g | blocked (data_missing) | The API lists 1 subject (Haydn) and 2 assets. Nothing on monkey G can be tested. |

**B. Problems**

1. [affects a conclusion] Claims file, pca-dimensionality and the trajectory claims. The paper's PCA uses "firing rate matrices of all neurons": 536 units of H pooled across 17 sessions. Here the population is 48 units from one session. The claims file says datasets are "as in the paper" without noting the pooling, so the dimensionality ranges and the tolerances on correlations are compared across very different populations.
2. [affects a conclusion] `SMOOTH_SD` in rsg.py, used by `dataset_geometry`. "Gaussian smoothing kernel width: 40 ms" is read as an SD of 40 ms. In the same Methods the paper writes "standard deviation of 25 ms" when it means SD, so a narrower kernel is a valid reading, and it was not run. The unsmoothed variant in cell 43 moves the PCA counts to estimation 3,3,6,4 and production 7,6,14,15, which is 5 of 8 in range and would make pca-dimensionality partial.
3. [affects a conclusion] Claims file, which says "supplementary tables … not available". `paper/` contains Tables S1–S3. Table S1 gives the regression as tp = βts + ε, which the notebook ran anyway. Table S3 gives wm and wp for H. The fitted wm (Eye Right 0.013, Eye Left 0.025, Hand Left 0.116, Hand Right 0.073) against Table S3 (0.027±0.009, 0.043±0.016, 0.085±0.025, 0.062±0.026) is never compared. Eye Right sits near the fit's lower bound of 0.01 (`bayes_loglik`), and that low wm drives the poor Eye bias R².
4. [affects a conclusion] GPFA `projections`. The Figure 6C legend says "We z-scored Xu of all trials"; the claims file z-scores within each prior. That changes the relative scale of the 8 coefficients that enter the signed-rank test, and with p = 0.0547 the other reading could change the result. It was not run.
5. [does not affect a conclusion] alt-speed-unmodulated, `support_speed_slope`. With attrition, fewer trials are averaged later in the support, which inflates the step distance in the 48-unit space. In my noise-only simulation, step distance roughly doubled from 100 to 20 trials. The edge-renormalised smoothing in `gauss_smooth` adds noise at the last bins. Bootstrap resampling with replacement inflates it further: the point estimate falls at or below the CI's lower bound for Hand Left Long and Hand Right Short. The reported intervals are biased upward and do not measure an effect size.
6. [does not affect a conclusion] short-in-long-control and alt-speed-unmodulated. With 4 datasets these absence criteria cannot fail; the claims file flags this only for alt-speed. The paper's ANOVA interaction is not tested.
7. [does not affect a conclusion] `production_rates` and `single_trial_speed` end the production window at the shortest `tp`. `tp` exceeds go_time − set_time by up to 200.6 ms (cell 4), so a window can run past Go. The notebook's note "neural alignment uses the event times" does not apply to window length.
8. [does not affect a conclusion] alt-threshold, cell 57. At 60% variance the Eye datasets keep 1 PC. Distance in one dimension is |difference|, so minima can be zero crossings (minimum distance 0.04) and not convergence.
9. [does not affect a conclusion] speed_per_s variant (cells 46 and 50). The step mean already divides path length by the number of bins; dividing again by mean tp does it twice. It only enters a variant.
10. [does not affect a conclusion] glm-prior-ts. The ±6.5-point tolerance is narrower than the binomial interval with 48 units. The prior fraction's 95% CI (65.0 to 89.5) touches 65; the ts fraction's CI (31.4 to 60.8) excludes 27.
11. [does not affect a conclusion] Author conclusions remain in cells 14 and 23 ("Result: …"), against the setup of this round. I formed my outcomes independently.

On synthetic inputs, these all behaved correctly: `wls` (matches statsmodels), `encoding_axis`, `pca_fit`, `bin_counts`, the attrition in `estimation_rates`, the GLM's BIC parameter counts, and `fit_bayes` (wm 0.094 and wp 0.070 recovered from a true 0.08 and 0.08).

**C. What I could not check**

- `gpfa_fit`: elephant was not installed and the data were not downloaded. Its output is taken as given.
- Whether production windows pass Go. The notebook would need, per condition, min(go_time − set_time) next to the window stop.
- PCA counts and the trajectory claims with a narrower kernel (SD of 20 ms or less).
- The GPFA quadratic test with Xu z-scored over all trials.
- alt-speed-unmodulated slopes with an equal number of trials per bin (subsampled), to remove the attrition bias.
- Whether the Eye Right Bayesian fit is well determined. A log-likelihood profile over wm, and a refit with the lower bound relaxed, would show it.
- What `tp` measures. The files do not say.
