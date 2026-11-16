**A. Outcomes** (38 claims in the claims file. The three notebooks cover 31 of them; the other 7 appear in no notebook output.)

| Claim | My outcome | Reason |
|---|---|---|
| data-composition | reproduced | 01 cell 6: 135 sessions (45/48/7/35). Median trials 213/253/264/222 under reading (a). 477 neurons, 41 inhibitory, 330 excitatory per session. Inhibitory fraction 0.110 under reading (b). Every value is within tolerance under one reading, which this criterion allows. |
| fig1b-psychometric | reproduced | 01 cell 8: slope is positive in all 4 mice, p ≤ 1e-98 (the 4 imaged mice only, a recorded deviation). The 16 Hz fractions printed there are not valid (problem 3). |
| figs1b-trial-history | blocked (metadata_insufficient) | Trial times are relative to each trial (start_time −0.48 to 0.21 s), so there is no ITI. Part is testable: the stimulus-strength coefficients and the previous-outcome terms without the ITI split can be fitted from the consecutive trial table. Not attempted. |
| fig1gi-inferred-spiking-differs | not_reproduced | 01 cell 10, bin −1. Reading (a) p = 0.05, 7.5e-10, 0.1, 0.031; reading (b) mouse 1 p = 0.0013. Neither reading gives p < 0.001 in every mouse. The time course reaches p < 0.001 in all bins in no mouse (best: mouse 2, 14 of 15). Inhibitory is higher everywhere. Pooled counts 44546/5530 are within tolerance. |
| fig2a-example-session | not_reproduced | 01 cell 14: exactly one session matches (mouse 4). Median selective counts are 11.5 excitatory and 1 inhibitory, against 24 ± 2.4 and 5 ± 0.5 (empirical-p variant: 28 and 2). |
| fig2bc-fraction-selective-similar | not_reproduced | 01 cell 16: medians E 0.129 and I 0.172 are within tolerance. But mouse 2 differs (p = 0.040) as well as mouse 4, and the rule needs no difference in mice 1–3. Inhibitory count per session is 6.8, outside 6 ± 0.6. |
| fig2bd-selectivity-time-course | blocked (methods_underspecified) | 01 cell 18, mouse 1: all four peaks fall in bins 1–2. Reading (b) (within 300 ms) passes, reading (a) (bin 0) fails. The claims file's rule makes differing readings blocked. |
| fig2de-selectivity-magnitude-similar | partially_reproduced | 01 cell 20: only mouse 4 differs (p = 0.021). |
| figs3d-same-spiking-selectivity | reproduced | 01 cell 22: no mouse differs in selectivity (p ≥ 0.18) or fraction selective (p ≥ 0.13); mouse 4 p = 0.55 / 0.20. Caveat: problem 9. |
| figs3c-wider-window | not_reproduced (borderline) | 01 cell 24: fractions are within tolerance under both readings. Inhibitory count per session is 9.8 under (a), outside 11 ± 1.1, and 9.9 under (b), exactly at the limit at printed precision. If (b) is ≥ 9.90, the readings differ and the claim becomes blocked (methods_underspecified). |
| figs3e-correct-error-correlation | not_reproduced | 01 cell 26: mouse 4 mean r is E 0.041 and I −0.027, so not positive for both types. E and I do not differ in any mouse, and mouse 4 is lowest. Mouse 3 has only 3 sessions. |
| fig6a-same-selectivity-correlations | reproduced | 01 cell 30, the code's pooled test: same > opposite with p < 0.05 for EI, EE and II in all mice, for noise and spontaneous correlations. The across-session variant fails in places (e.g. mouse 3 EI noise p = 0.24). |
| fig6bc-inhibitory-correlations-higher | blocked (methods_underspecified) | 01 cell 32. Reading (b) (pooled neurons): II > EE in every mouse and condition, EI always between. Reading (a) (sessions): fails for spontaneous mouse 3 (p = 0.15) and matched mice 1 and 3 (p = 0.093, 0.094). Mouse 1 counts match exactly (11867/1583). |
| fig3bc-decoding-similar | reproduced | 02 cell 5: all populations are above the shuffle in every mouse (p ≤ 0.003). Inhibitory minus excitatory ranges −1.45 to +2.23 points, p ≥ 0.17. |
| fig3b-decoding-time-course | not_reproduced | 03 cell 5: no mouse peaks in bins −1/0. Within 300 ms only mice 1 and 4 qualify; mouse 2 peaks at bin 3 (86.1 vs 86.0) and mouse 3 at bin 6. |
| fig3df-weights-similar | reproduced (bin −1 only) | 02 cell 9: no mouse differs across sessions (p ≥ 0.079). Pooled counts 42019/5172 match exactly. The per-bin "throughout the trial" part was not run (problem 6). |
| fig3hi-mixed-no-advantage | reproduced | 02 cell 7: differences are −0.10 to +0.67 points, p ≥ 0.71. |
| figs5-fluorescence-decoding | no output | Not in any notebook. API metadata lists only BehavioralTimeSeries and PlaneSegmentation, so whether denoised or ΔF/F traces exist could not be settled from metadata. |
| figs6ab-previous-choice-stimulus | no output | Not in any notebook. Testable: stimulus-aligned traces (`dFoF_stimAl_noEarlyDec`) and the trial order are in the files. |
| figs6c-outcome-decoding | no output | Not in any notebook. Testable: `dFoF_rewardAl` and `dFoF_commitIncorrAl` are in the files (helper `KEEP`). |
| figs6de-incorrect-trials | not_reproduced | 02 cell 11: incorrect-trial accuracy is not above the shuffle in mouse 3 (p = 0.12) or mouse 4, where it is below chance (44.0 vs 48.2). The reductions do not differ, and mouse 4's is largest. See problem 2. |
| fig4bd-stability-similar | reproduced | 02 cell 13: no difference across mice in any of 8 variants (p ≥ 0.51), nor per mouse. |
| figs7c-angle-stability | no output | Not in any notebook; testable from the decoders. |
| fig5a, fig5bc, figs9 (models) | no output | Simulations; no notebook among the materials. |
| fig7-noise-correlations-limit-decoding | blocked (methods_underspecified) | 02 cell 15: the change is positive in every mouse under both trial sets (+4.3 to +6.7). Correct trials with the one-sample test: p < 0.05 in all mice. The unpaired reading fails in mouse 3 (p = 0.32), and all-trials fails in mice 3 and 4. |
| fig8ab-learning-accuracy | not_reproduced | 03 cell 7: mouse 2 excitatory and inhibitory r = 0.16/0.17 (p = 0.27), mouse 4 inhibitory p = 0.08 under trial reading (a); (b) is worse. None of the reported r values is within tolerance. |
| fig8ce-choice-signal-onset | not_reproduced | 03 cell 9: only mouse 1 all-neuron (and excitatory at p < 0.05) is significantly negative. Mice 2 and 4 have r ≈ −0.07 to −0.18, not significant. |
| fig8de-learning-parallel | not_reproduced | 03 cell 11: late > early fails in mouse 2 (p = 0.35, 0.26). Under trial reading (b), mouse 2 late accuracy differs between types (p = 0.012). Early/late reading (b) gives 0–1 days. |
| figs13c-equal-trials | not_reproduced | 03 cell 13: mouse 2 p = 0.22. |
| figs12-licking-running | not_reproduced | Lick part blocked: the spout is not identified in `firstSideTryAl_lick`. The running part already fails: mouse 1 has 2 eligible sessions, accuracy vs shuffle p = 0.47 (02 cell 17). |
| fig8f-correlations-decrease | partially_reproduced | 01 cell 36, reading (a): early > late in the mean for every type and mouse, but significant only in mouse 2. Reading (b) has no days. |
| figs13ab-pseudo-learning | not_reproduced | 03 cell 15: mouse 2 all-neuron p = 0.18. |
| fig8g-fraction-selective-triples | not_reproduced | 01 cell 38: inhibitory ratio is 4.66 or 2.66 (both outside 3 ± 0.3). Late > early is not significant in mouse 2 (E and I) or mouse 4 (I). |
| figs2-temporal-dynamics-similar | blocked (other) | Not run ("not reached in the run's time"). The data exist (stimulus-, reward-, initiation-tone- and choice-aligned traces), so the claim is testable. |
| figs14-neuropil | blocked (data_missing) | Confirmed on the archive: variableMeasured has no imaging series, and files are 0.18–1.37 GB (62.6 GB total), far too small for raw movies. |
| figs15-labeling-specificity | blocked (data_missing) | Confirmed: the archive holds only the 135 session NWB files, no histology. |

Tally: 8 reproduced, 2 partially reproduced, 14 not reproduced, 7 blocked, 7 with no output. The attempt record was not provided, so these counts come from the claims file and the notebooks.

**B. Problems**

1. [affects a conclusion] Helper `read_trials` and notebook 01 cell 3. The crosstab shows `trial_is_good` is exactly "response is correct or incorrect". So the code's other exclusions (first trials of a session, helped trials) are not applied. The helper's stated assumption is contradicted by the notebook's own output, not confirmed by it. This touches every trial set, with plausible effects on fig2a and the fig2bc counts.
2. [affects a conclusion] figs6de-incorrect-trials, possible claims-file misreading. The S6D legend says "high" accuracy for an example animal (48 sessions). S6E and S3E describe mouse 4 as stimulus-driven, with the largest reduction. The criterion instead requires above-shuffle accuracy in every mouse; under it, mice 3 and 4 fail.
3. [does not affect a conclusion] 01 cell 8. `trial_pulse_rate` is continuous (5.33…27.05), so `{int(r): ...}` overwrites keys and the printed per-rate fractions are meaningless (e.g. mouse 3 shows only 0s and 1s). `== 16` finds 0–122 trials. The 16 Hz trials, randomly rewarded, all carry trial_type "High-rate", so their derived choice is arbitrary; they stay in all decoders and correlations (~0.5% of trials).
4. [affects a conclusion] Notebook 03, `learn_session`/`timecourse`. C is chosen at bin −1 and reused at every bin, with 25 splits and 3 excitatory subsamples instead of per-bin C, 50 splits and 50 subsamples. fig3b's mouse 2 outcome hinges on 0.1 points, and fig8ce's onsets depend on per-bin t-tests over 25 repetitions.
5. [does not affect a conclusion, but biases toward "no difference"] 02/03, NSUB = 5 or 3 excitatory subsamples instead of 50. This adds noise to the excitatory estimate in absence claims (fig3bc, fig3hi, fig4bd, fig8de). The observed p-values (≥ 0.17) make a flip unlikely.
6. [affects a conclusion] fig3df, 02 cell 9: weights are computed only at bin −1, but the claims file asks for every bin as well ("throughout the trial").
7. [does not affect a conclusion] `svm_cv`: C is chosen on the same test folds that are reported. On synthetic null data (60 trials, 80 neurons) this gives 56.1% accuracy against a 49.8% shuffle. The all-neuron shuffle is 53–56% rather than the paper's ~50%, because random 10% test sets are unbalanced. This is the specified method and every above-chance margin is far larger.
8. [does not affect a conclusion] fig4bd: the SD rule gives ~2.0–2.4 s, essentially all bins, so it is at ceiling (e.g. bin −10 at ~50% still counts as stable). Only the SE variant is informative, and it also shows no difference.
9. [could affect figs3d and fig6bc matched] `max_bin_match`: 90% of trace values are below 1e-6, so most per-neuron medians are ≈0. The "max bin" is the lowest bin and keeps most neurons (265 E, 22 I per session). That activity is actually matched is never shown.
10. [does not affect a conclusion] fig8f, fig8g, fig8de, figs13: early/late reading (b) gives 0–8 days per mouse, so it is never testable. The outcomes rest on reading (a).
11. [does not affect a conclusion] fig7, `svm_cv(shuffle_trials=...)` shuffles train and test trials together. I tested this for leakage on synthetic independent neurons: pseudo minus real was +1.1 ± 1.1 and +0.5 ± 0.7 points, so no measurable bias.
12. [does not affect a conclusion] `read_aligned` takes the event frame from the first trial's `starting_time` only, and assumes all trials share it. Not checked.

Synthetic checks that passed: `auc_matrix` matches sklearn. The normal-fit rule gives 1.8% false positives (|z| ≥ 2.45) and the empirical rule 5.4%. `early_late` and `bin3` indexing are correct.

**C. Could not check, and which output would settle it**

- figs3c: (b)'s per-session inhibitory count to 2 decimals.
- The trial-table column names, the behaviour group's keys and the processing/Ophys keys. These would settle problem 1 (whether a helped or first-trial flag exists), the figs12 lick blocking (centre vs side spout), figs1b (any session clock), and figs5 (fluorescence or ΔF/F series).
- `starting_time` across all trials of a session (problem 12).
- Mean bin −1 activity of matched E vs I neurons (problem 9).
- Per-bin weights for fig3df.
- fig3b and fig8ce rerun with per-bin C and 50 splits, at least for mice 2 and 3.
- Exact p-values in fig2bc printed for mouse 2 with 50 excitatory subsamples (n/a for ROC), and the fig2a session's trial counts compared with the paper's.
- Outputs for the 7 claims with none: figs5, figs6ab, figs6c, figs7c, fig5a, fig5bc, figs9.
