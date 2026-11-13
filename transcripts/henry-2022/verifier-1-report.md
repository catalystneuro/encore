**Verifier report, round 1: Henry & Kohn 2022 on CRCNS v4-2**

The claims file has 32 claims. The notebooks test 29 and mark 3 as blocked. My outcomes are 17 reproduced, 9 partially reproduced, 3 not reproduced and 3 blocked. I checked the helpers on synthetic inputs (AUC, threshold fit `fit_k`, `perm_k`, `decode`, `fit_affine`) and they behave correctly. Nothing was re-run on the real data.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| data-populations | partially_reproduced | The deposited units give 11 sessions, 22 populations per area, sizes 18.0 (V1) and 31.4 (V4), totals 396 and 691, and per-animal counts equal to Figure S7 (cell 12). The Methods' selection rule does not regenerate them: readings (a) and (b) give V1 115/133 and V4 147/174. The criterion's reproduced condition fails, but every count it states holds for the deposit. |
| fig1b-v4-rf-larger | blocked (data_missing) | The archive holds only `data.zip`, which contains two .mat files with no mapping sessions (checked below). |
| fig2a-v1-single-neuron-near | reproduced | Slope 0.580 [0.486, 0.669] against 0.60 ± 0.10, and the upper CI bound is below 1 (cell 14). |
| fig2b-v4-single-neuron-near | reproduced | Slope 0.206 [0.145, 0.269] against 0.20 ± 0.06. |
| fig2c-farthest-spacing-slopes | reproduced | V1 0.728 (needs 0.74 ± 0.08) and V4 0.437 (needs 0.44 ± 0.07). |
| fig2c-v4-worse-all-spacings | reproduced | The V4 and V1 95% CIs do not overlap at any of the four spacings (reading b). |
| fig2de-population-decoding-example | reproduced | Animal AL has 84 cases. V4 restricted to above-chance cases: p = 1.5e-15 (t) and 2.8e-11 (Wilcoxon). V1 p > 0.05 holds only without the restriction (p = 0.46 and 0.60); with it, p = 0.018 and 0.025 (problem 3). |
| fig2f-v1-threshold-elevation | not_reproduced | k = 1.69 (needs 1.31 ± 0.10) at the closest spacing and 1.67 (needs 1.15 ± 0.08) at the farthest. The only significant spacing is 2.1 under 10 folds, and none under 5 folds (cells 51–52). |
| fig2f-v4-threshold-elevation | partially_reproduced | p < 0.001 at all four spacings and V4 > V1 at every spacing both hold. The values do not: 7.30 (needs 2.52 ± 0.23) and 2.61 (needs 1.89 ± 0.19). |
| figs3-pseudo-populations | reproduced | Per the criterion: within twice the SEM at 7 of 8 area and spacing pairs, and the target-alone range is wider (SD 0.17 against 0.12). It used 10 draws per size where the claims file's standard choice is 20, and it is one pair from failing. |
| fig3ab-correlations-reduced | reproduced | V1 0.067 to 0.048 and V4 0.112 to 0.056, all within ± 0.005. Pairs 4036 and 13101. p = 2e-21 and about 0 (cell 16). Only reading (a) could be run. |
| fig3c-shuffled-threshold-elevation | reproduced | 8 of 8 pairs within twice the SEM and V4 > V1, under both shuffle readings (cell 55). The test is lenient because the SEMs are large (V4 about 2.5). |
| fig3d-v1-fano-closest | reproduced | 1.051 to 0.985, p = 3e-8 (cell 18). |
| fig3e-v4-fano-all-spacings | reproduced | 0.997 to 0.928, and p < 1e-8 at all four spacings. |
| fig4a-v1-modulation-indices | partially_reproduced | Closest spacing, two-sided test: suppression 24.5% and facilitation 26.5%, both within tolerance. No reading fits both far values: at 2.6, facilitation 2.0 and suppression 14.4, or 1.8 and 12.9 (cell 21). |
| fig4b-v4-modulation-indices | reproduced | Within-orientation pooling, two-sided, 2.6°, percentages of all neurons: all six values within tolerance. 69.8% of neurons have an index above 1. Under the log reading, the test against 1 gives p = 4.5e-17 and V4 > V1 gives p = 0.009 (the raw-index test gives 0.074). The SDs (0.379 and 0.473) match the printed ± values. |
| fig4c-modulation-strength-significant | reproduced | All eight observed values exceed the 99th percentile of the null; p = 0.001 (cell 24). |
| fig4c-v4-stronger-than-v1 | reproduced | p = 0.011 at the closest spacing, and below 1e-16 at the other three (cell 25). |
| fig4c-v4-maintained-v1-weaker-far | reproduced | V4 p = 0.40 (paired) and 0.41 (two-sample); V1 p = 9e-23 (cell 26). |
| figs4-rf-alignment | blocked (data_missing) | There is no coarse mapping of each distractor alone (see below). |
| figs5-additive-vs-multiplicative | reproduced | In V1, 90% of facilitated cases favour the additive model and 84% of suppressed cases the multiplicative one; in V4, 97% and 92%. Simulated slopes are 0.78 to 0.96, all below 1 and above the measured slopes at 4 of 4 spacings (cell 38). |
| fig5bc-tuning-model-terms | partially_reproduced | The tests hold: m < 1, V4 m smaller and V4 a larger, all p < 1e-17. Only the V4 additive term (0.907) is within tolerance; V1 m 0.405, V1 a 0.596 and V4 m 0.154 are not. Fitted counts: V1 146 (89 and 57, exact), V4 244 against 198 ± 20. |
| fit-quality | not_reproduced | V1 0.623 is within tolerance under the pooled reading, but V4 is 0.589 there (0.410 as a mean per case, 0.328 as a median). V4 fails under every reading (cell 30). |
| fig5-terms-covary | reproduced | Pearson r = −0.89 (V1) and −0.68 (V4), p < 1e-130. |
| fig5-negative-multiplicative | partially_reproduced | The V4 fraction (35%) is larger than V1 (Fisher p = 8e-7), but the V1 fraction is 23%, not below 10%. |
| fig5de-simulated-discriminability | reproduced | Recorded trial counts against all driven neurons: V4 is below V1 at every spacing, and the simulated slope is at or below the measured one at 4 of 4 (V1) and 3 of 4 (V4) spacings. |
| fig6c-tuning-correlation-near | partially_reproduced | p < 0.001 under both readings. Reading (a) has V1 0.389 within tolerance but V4 0.161 outside it; reading (b) has V4 0.238 within but V1 0.460 outside. No single reading fits both means. |
| fig6d-tuning-correlation-spacing | partially_reproduced | V4 < V1 at p ≤ 1e-6 under both readings, but both means are out of tolerance under both: V1 0.43 or 0.52 against 0.36 ± 0.02, V4 0.135 or 0.214 against 0.17 ± 0.02. |
| fig6e-tuning-correlation-configuration | reproduced | V1 0.644 and V4 0.214, both within tolerance, p = 7e-8 (cell 43). |
| fig6-well-isolated | blocked (data_missing) | The deposit has no waveforms or SNR. |
| fig7cd-fixed-decoder-generalization | partially_reproduced | The tests hold: V1 p = 0.36 and V4 p = 4.5e-4 per population. All four d′ values are far below the paper: 0.35 to 0.41, against 0.67 to 1.02 (cell 58). |
| figs6-common-neuron-pool | reproduced | The fraction still driven is 0.87 to 0.96, at least 0.8 at every spacing. The V4 top-neuron correlation is r = 0.67, p = 6e-4. The driven fractions come from only 10 of 22 populations (problem 1). |

**Blocked claims, checked on the archive.** The S3 listing and `filelist.txt` show only `data.zip`, the two description documents and `checksums.md5`. I read only the zip's central directory, not the data. It holds two .mat files, and the description lists their only fields: spikecounts, parameters, labels, session, animal and orientation range.

- **fig1b:** not testable as specified. The distractor-only epochs give a coarse proxy: in cell 9, V4 responds to the distractors about as strongly as to the target and V1 does not. That fits larger V4 fields but is not the criterion.
- **figs4:** the distractor-only epochs show all four distractors together, so the per-distractor 30%/80% classes cannot be formed. At most a "target but not distractor-display" proxy is possible, and only in the 10 populations with a usable baseline.
- **fig6-well-isolated:** no part can be tested.

### B. Problems

1. [affects a conclusion] In cells 9 and 10, sessions 1, 2 and 8–11 (12 of 22 populations per area) have "blank" and distractor-only epochs that fire as much as the target epochs. Spontaneous rate cannot be measured there. This is why the selection rule fails in cell 12 (data-populations), and why cell 45 (figs6) rests on 10 populations per area. The notebook flags it, but the figs6 result is not stated as covering 10 populations.
2. [affects a conclusion] `even_odd_reliability` (cell 28) splits V4 by stored order, which cell 5 shows is not the recording order. The V4 selection (244 against 198) feeds fig5bc, fit-quality, fig5-negative, fig5de and fig6c/d. A random-split variant was run only for fig6c/d (cell 42). V1 matches exactly (146; 89 and 57), which supports the reading where the order is valid.
3. [affects a conclusion] Cell 49: fig2de is reproduced only because the >0.5 restriction is applied to V4 and not V1. With the same restriction, V1 gives p = 0.018 (AL, 10 folds). The claims file allows this, but the outcome depends on it.
4. [affects a conclusion] Claims file, fig4a: a tolerance of ±0.25 points on 2.5% is ±1 neuron of 396. That is finer than the counting resolution, and the far pair fails partly on it (2.0% is 8 neurons, against 10). Reported, not corrected.
5. [does not affect a conclusion] Cells 51–55 and pseudo cell 9: the two binomial-count readings, (a) test trials and (b) all trials, give identical k by construction, because n_test = n/10 uniformly and the argmax is scale-invariant. They are not distinct readings; only the bootstrap and permutation draws differ.
6. [does not affect a conclusion] `K_GRID` is capped at 20, and V4 CA at 1.6° reaches 18.5 (10 folds) and 20 (5 folds), so those estimates are censored. The V4 values fail by a wide margin regardless.
7. [does not affect a conclusion] `fit_k` on synthetic data: with true k = 1 and noisy target-alone performance near chance, the estimate is 1.15, biased upward. The recorded V1 performances average 0.58, so part of the V1 excess may come from the method itself, which is the paper's, not from a notebook error.
8. [does not affect a conclusion] In `sig_counts` (cell 20), `nanmean(nl < mi)` counts NaN null draws as "not below", which biases results slightly toward suppression. The number of NaN draws is not reported.
9. [does not affect a conclusion] figs3 (pseudo cell 8) uses 10 draws instead of 20, as the notebook states. One more failing pair would flip the outcome; V1 at 2.6° differs by 0.50 against a 0.63 margin.
10. [does not affect a conclusion] In cell 38, figs5 judges "below 1" by the CI upper bound, which is stricter than the criterion. All point slopes are below 1.
11. [does not affect a conclusion] `extreme_order` reads "closer to 0" as the absolute axial orientation, but in the paper's −9 to +9 frame the two extremes are equidistant from 0. The lower-first variant changes slopes by 0.02 or less.

### C. What I could not check

- Whether the blank epochs in the six sessions are mislabelled. A per-session table of the contrast parameter values, and blank against distractor-only against target means per neuron, would settle it.
- fig5bc, fit-quality and fig5-negative under the random-split V4 reliability (`REL_R`). The notebook would need the fit table for that selection.
- Whether the threshold permutation null is calibrated. A median and 5–95% range of each null would show it.
- Whether the decoder underfits on the real data. The distribution of chosen C, and the fraction of folds where all coefficients are zero, would show it.
- Why the fig7cd d′ values are about half the paper's. d′ per population for the 18° pair alone, before averaging over pairs, would help.
- figs3 with 20 draws per size.
