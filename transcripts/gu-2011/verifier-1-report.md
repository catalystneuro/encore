**A. Outcomes**

The claims file has 35 claims. The notebook tests 16 of them and treats 19 as blocked.

| Claim | Outcome | Reason |
|---|---|---|
| training-group-link | reproduced | In cell 13 the eight per-monkey counts match the Figure S2B counts one to one. That gives 89 trained and 38 naive pairs and 146 and 64 units. Monkeys 2 and 5, the ones with behavioural thresholds, both fall in the trained group. The 89/38 split follows from matching by count, so only the neuron counts and the behaviour check are independent tests. |
| fig2b-trained-lower-noise-correlation | reproduced | Cell 15: trained 0.0241 ± 0.0174, naive 0.1190 ± 0.0316, both within tolerance. Student p = 0.0056 (paper 0.006), Welch p = 0.011. |
| figs2b-individual-animals | reproduced | Cell 17: the lowest naive animal mean (0.088) is above the highest mean among the trained animals shown (0.048). Counts are 35/26/18/8 and 22/11/5. There are no time courses because the data set holds no spike times. |
| fig1-example-pair | reproduced | Cell 19: one pair, m2c338r1, has all four values within tolerance (0.828, 0.786, 0.291, 0.142). The per-pair p values cannot be checked without trial counts. |
| fig1f-modality-correlated | partially_reproduced | Cell 21: Spearman R = 0.449, p = 1e-7, on n = 127, the smaller sample the criterion allows. R is outside 0.342–0.418. |
| fig1f-modality-means-equal | reproduced | Cell 23: paired p = 0.73, n = 127. The vestibular mean of 0.056 is outside the paper's 0.035 ± 0.014, but the paper's figure is from 179 pairs. |
| fig5-noise-signal-positive | reproduced | Cell 25, pooled rnoise: the rsignal slope is positive with p = 0.00017 (vestibular) and p = 0.0007 (visual). |
| fig5-slope-unchanged | reproduced | Cell 25/27: interaction p = 0.83 (vestibular) and 0.96 (visual). |
| fig5-intercept-lower-trained | partially_reproduced | Cell 29: the training main effect is significant (p = 0.018 vestibular, 0.0074 visual, pooled rnoise). The 95% intervals of the intercepts overlap under every construction: separate fits, the ANCOVA model, and the additive model. |
| fig5-regression-coefficients | partially_reproduced | Cell 31, readings (a) and (b): slopes 0.119/0.084 and 0.132/0.085, naive intercept 0.077/0.074, all within tolerance. The trained intercept is 0.003/0.002, outside 0.005 ± 0.0005, though still below the naive one. Reading (c) misses the visual slope (0.106). |
| fig6a-population-thresholds | reproduced | Cell 33: at N = 2000 the naive/independent ratio is 5.41 (within 4.5–5.5) and trained/naive is 1.000, under the claims-file reading (A30/B10) for both rsignal readings. The result is sensitive to the unstated amplitude and baseline: cell 34 gives 4.32 to 5.90. |
| fig6b-slope-not-intercept | reproduced | Cell 36: over a slope width of 0.2 the threshold changes by 1.97°, over an intercept width of 0.2 by 0.11°. The threshold falls from the trained to the naive intercept (7.251 → 7.217). It is not monotone at intercept 0 → 0.02. |
| fig7a-pair-sign-of-effect | partially_reproduced | Cell 38: all 88 pairs with positive rsignal follow the rule, and 92 of 93 with negative rsignal. The exception is at rsignal = −0.011 (pref2 = −2°), and the criterion requires every pair. |
| fig7c-narrow-preferences | partially_reproduced | Cell 40: the proportions are 48.6, 73.1 and 92.4%, all within tolerance, and the improvement grows from −0.5% to about 4.8%. The best improvement of 4.83% is far outside 8 ± 0.8. It stays at 3.6–6.0% under the amplitude and baseline variants; only dropping the trace term, which is not equation 3, reaches 8%. |
| fig8ab-choice-probability-lateral | not_reproduced | Cell 42 uses 258 CPs from two trained monkeys, a subset of the paper's 311. No preferred-heading reading gives fore-aft CP smaller with p < 0.05: spline peak 0.527 vs 0.542, p = 0.14; even-8 vector sum p = 0.69. The vector sum over all 10 headings gives the opposite sign (p = 0.0006), but that reading is biased (problem 1). Left vs right shows no difference (p = 0.27–0.56). |
| fig8cd-noise-not-preference | reproduced | Cell 44, trained pairs, as the Results specify ("in trained animals"): p = 0.43 (visual preference) and 0.17 (vestibular). Lateral rnoise is lower than fore-aft only with vestibular preferences. |
| fig2c-timecourse-naive-higher | blocked (data_missing) | I confirmed the archive listing: stc-1/live holds only MSTd.mat (65 KB, derived), VIP.mat, demo.m, docs, filelist.txt and checksums. There are no spike times. |
| figs2a-difference-decreases | blocked (data_missing) | Same: no spike times. |
| fig3-mean-response-unchanged | blocked (data_missing) | Same. |
| fig3-fano-unchanged | blocked (data_missing) | Same. |
| figs8c-renormalization | blocked (data_missing) | No trial-ordered responses. |
| discussion-stimulus-reduces-correlation | blocked (data_missing) | No prestimulus responses. |
| figs1-distance | blocked (data_missing) | No distances, and no pairs over 1 mm (all 127 are under 1 mm). |
| methods-single-vs-multiple-electrodes | blocked (data_missing) | No electrode label, and the recording structure (cell 6) cannot stand in for one. |
| fig2a-behavioral-learning | blocked (data_missing) | There are no training histories. `experiment2.behv` holds one threshold per monkey for monkeys 2 and 5 (1.2/1.2° and 3.1/3.25°), both inside 0.9–3.3°. Only the plateau part could be checked, for 2 of 5 animals, and the notebook does not report it. |
| fig4-tuning-width-visual | blocked (data_missing) | The single-unit data have no naive animals. Trained medians could be computed from the experiment1 tuning curves for a descriptive comparison only. The ANOVA selection cannot be applied to trial-averaged curves. |
| fig4-tuning-width-vestibular | blocked (data_missing) | Same. |
| fig4-amplitude-unchanged | blocked (data_missing) | Same. |
| fig4dh-lateral-more-sensitive | blocked (data_missing), wrongly | The preference-group effect could have been tested within trained animals: experiment1 tuning curves give a Fisher threshold and preference for 129 units, and experiment2 adds neuronal thresholds. The notebook used the same subset for fig8ab (problem 2). |
| fig4dh-training-no-sensitivity-change | blocked (data_missing) | Needs naive single units. |
| figs4-population-sensitivity-any-reference | blocked (data_missing) | Needs naive single units. |
| fig7b-msdt-pairs | blocked (data_missing) | Pairs carry only preferences and correlations, no tuning curves. |
| figs5-congruency | blocked (data_missing) | The congruency index needs each unit's tuning curves. A proxy from the visual–vestibular preference difference is possible but is not the paper's measure. |
| figs6-task-independent | blocked (data_missing) | No discrimination-task correlations. |
| figs8ab-eye-movements | blocked (data_missing) | No eye records. |

**B. Problems**

1. [affects a conclusion] `stc1.pref_vector_sum`, used in cell 42, takes the vector sum over the 10 unevenly spaced experiment1 headings (extra ±22.5°) with no weighting for angular spacing. On synthetic wrapped-Gaussian curves, true preferences of 30/60/90/120° come out as 16/35/59/93°, so many lateral units are labelled fore-aft (171 vs 87). This reading is the only one with a significant effect, and that effect has the opposite sign. It should be dropped or replaced by a spacing-weighted vector sum. The fig8ab outcome stays not_reproduced either way.
2. [affects a conclusion] Cell 0: fig4dh-lateral-more-sensitive is marked blocked for having "no naive animals". Its main claim is the preference-group effect, which can be tested within the two trained monkeys from experiment1 and experiment2, with the claims-file Fisher threshold on interpolated tuning curves. The notebook used exactly this subset for fig8ab. The claim should be partially tested, not blocked.
3. [affects a conclusion] fig8cd-noise-not-preference, cell 44. The claims file says to judge under the reading whose point count is closest to 328. The 127-pair variant (254 points) is closer than the 178 used, and with vestibular preference it gives p = 0.0009. I keep "reproduced" because the Results restrict the statement to trained animals, but the notebook should state this conflict with the claims-file rule.
4. [does not affect a conclusion] Cell 0 says "None of the analyses below draws random numbers"; cell 31 runs a seeded bootstrap.
5. [does not affect a conclusion] `stc1.pooled_rnoise`. I checked on synthetic data that the pooled-z-score Pearson equals the mean of the per-condition values when trial numbers are equal and there are no outliers. The match to the paper's means (0.0241/0.1190 vs 0.023/0.116) supports the assumption. Whether the stored values include outlier removal or renormalization cannot be told.
6. [does not affect a conclusion] fig6a–7c: the two rsignal readings give identical results. I confirmed that the maximum difference in rsignal is 5e-7, so the second reading adds nothing. The real open parameters are amplitude and baseline, which move fig6a across its tolerance (A35 gives 5.57) and fig7c between 3.6 and 6.0%.
7. [does not affect a conclusion] Not reported for fig2a: the plateau thresholds of the two trained monkeys in `experiment2.behv`.
8. [does not affect a conclusion] Cell 6 finds a recording with 6 pairs, against the paper's stated maximum of 5. It is noted but not explained.

Helper checks on synthetic data all passed: `tls_plane` recovers known coefficients; `threshold` with independent noise matches the analytic Fisher information; `sigma_for_fwhm` gives a width of 135.5°; `preference_group` boundaries are as documented; `pref_spline_peak` is accurate to within 1°.

**C. Not checked**

- I could not re-run the data loading. The figures are not shown in the text outputs.
- Whether `corr_noise` includes renormalization or outlier removal. Per-pair trial counts would settle this, but the data set does not hold them.
- fig5-intercept: what interval method the paper used. A bootstrap interval for the per-group intercept, added alongside the parametric ones, would help.
- fig7a: where the crossover sits. Adding the rsignal at which trained/naive equals 1 would show this.
- fig8ab: how many of the 258 CPs are in the paper's 311, and the sign convention of the CPs. A per-unit result with a spacing-weighted vector sum would have made the reading sound.
- fig4dh: the trained-only analysis of thresholds by preference group, which the notebook never ran.
