**Verifier report, round 1: Chandravadia et al. 2020 on DANDI:000004 v0.220126.1852**

The claims file has 25 claims. The notebook tests 24 and treats one as blocked. My outcomes: 10 reproduced, 10 partially reproduced, 4 not reproduced, 1 blocked.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| counts-neurons-subjects | reproduced | Cell 15: 1864 unit rows (+1) and 59 subjects, both within tolerance under reading (a). Reading (b) gives 1798, also within tolerance. |
| counts-sessions | reproduced | Cell 17: the 87 (subject, session) pairs in the files equal the 87 in Online-only Table 1. The Methods' 89 is 2 more. |
| table1-demographics | partially_reproduced | Cell 19: age and sex match for 56 of 59 subjects. C24 and H33 differ in age; H48 differs in age and sex. The table's 25 F / 34 M is confirmed; the files give 26 / 33. I checked the three table rows against `paper/`. |
| task-structure | partially_reproduced | Cell 21: the recognition and category parts hold in 87 of 87 sessions, the encoding part in 79. Seven sessions have 50 encoding trials and one (CS53_123) has 97. |
| new-old-label-coding | not_reproduced | Cell 23: under the stated coding both tests fail in all 87 sessions (no label-0 image is in the encoding block). With the labels reversed both hold in 86, or 78 under the strict image test. That is "most" either way. |
| ttl-codes | partially_reproduced | Cell 25: lengths and timestamps match in 87 of 87 files. Only listed codes and correct per-trial order hold in 78 of 87. The other 9 contain codes 0, 4, 22, 23, 98 or 99. |
| experiment-ids | partially_reproduced | Cell 27: 83 of 87 files are in the sets. CS33_77, CS39_100, H42_55 and H51_105 use 81/82 or 82/83. |
| session-dates | partially_reproduced | Cell 29: 86 of 87 files are dated the 1st of a month. H28_48 is dated 2010-03-13, and H44_68 is dated 2000, outside the span of the recordings. |
| units-table | partially_reproduced | Cell 31: all columns are present (IsolDist is stored as IsolationDist), there is one electrode per unit, and the waveform rate of 98.4 kHz is within tolerance. But 568 units have NaN or infinite SNR or IsolationDist. |
| electrodes-table | not_reproduced | Cell 33: `imp` is empty for all 887 electrodes, which is the criterion's not-reproduced case. x, y and z are also missing for 99 electrodes in 8 files. |
| isi-criterion | partially_reproduced | Cell 35: with spike times sorted, 1858 of 1864 units (99.68%) are below 3%, so at least 95% but not all. Two H27_58 units have about 50% of intervals under 3 ms. |
| fig5a-mtl-locations | reproduced | Cell 37: all 1864 units are in the amygdala or hippocampus. |
| fig5c-auc-all | reproduced | Cell 39: mean AUC 0.753 (0.74 ± 0.10) and SD 0.094 (0.10 ± 0.01). |
| fig5c-auc-sites | reproduced | Cell 41: CS 0.760, SD 0.085; TWH 0.688, SD 0.138. All four values are within tolerance. Welch p = 0.16. |
| fig5b-roc-asymmetric | reproduced | Cell 43: mean z-ROC slope 0.782 over 82 sessions, t-test against 1 gives p = 4.3e-9. Five sessions are left out because they have no slope. Wilcoxon and pooled-slope variants agree. |
| fig5d-confidence-accuracy | reproduced | Cell 45: fixed split, 84 sessions, 80.1% vs 60.9%, paired p = 3.2e-16. The dynamic split also gives p < 0.001. |
| vs-cells-proportion | reproduced | Cell 49: 332 of 1864 (17.81%) in the Methods' window, within both tolerances. The shuffled null is 4.83%. The paper states no chance level. |
| ms-cells-proportion | not_reproduced | Cell 51: 110 of 1864 (5.90%) under the paper's stated reading (1 s window, all 50/50 trials, which the text gives explicitly). Expected 146 ± 14.6 and 7.8 ± 0.78%; seeds 1 to 4 give 109 to 111. Only the code's choices (correct trials, 1.5 s window) give 147 (7.89%). The null is 4.35%. |
| dual-cells-proportion | not_reproduced | Cell 53: 12 cells (0.64%) under the main tests, against 26 ± 2.6. The code's choices give 26. |
| fig5f-site-proportions | partially_reproduced | Cell 55, main reading: no Fisher test is significant (p = 0.36, 0.46, 1.0), but only 1 of 6 values is within tolerance. Only one of the two conditions holds. The code's choices give 6 of 6. |
| twh-sessions | reproduced | Cell 57: 9 T-labelled sessions, all with institution "Toronto Western Hospital". |
| previous-release-link | partially_reproduced | Cell 59: 64 of 65 earlier sessions are found and agree (98.5%). H48 session 98 (variant 2) is absent. |
| previous-release-additions | partially_reproduced | Cell 61: 23 new sessions and 17 new subjects match. The new sessions hold 325 neurons, outside 288 ± 28.8. |
| fig4-example-vs-neuron | reproduced | Cell 63: CS58_132, electrode row 4, channel 177, Right Amygdala. ANOVA p = 1.2e-22, animals highest (6.75 Hz). The code's window agrees. |
| fig3-example-vs-neuron | blocked (data_missing) | Session 144 is in no file. I checked the archive: draft and both published versions hold the same 87 assets, and the latest session date is 2019-04 (session 136). Online-only Table 1 has no session 144 either. No part can be tested. |

## B. Problems

1. **[does not affect a conclusion]** `bootstrap_mean_equal` uses the raw difference of means ("mode 1, no variance correction"). Efron and Tibshirani's algorithm 16.2, which the claims file cites, uses a studentized statistic. Which mode the paper's MATLAB code calls is not shown. On synthetic Poisson data the helper's false-positive rate was 6.4% (2000 runs). A studentized variant was not run. It is unlikely to close the gap from 110 to at least 131.4, but this is unchecked.
2. **[does not affect a conclusion]** Cells 47 and 51: MS on correct trials in the Methods' window gives 132 with seed 2020 and 137 to 147 with seeds 1 to 4. That is wider than the main reading's spread and is not discussed. It is a variant only.
3. **[does not affect a conclusion]** Cell 51 shows the main MS count (5.90%) is only 1.5 points above the shuffled null (4.35%). The notebook does not comment on this. It bears on interpreting the not_reproduced outcome but not on the outcome.
4. **[does not affect a conclusion]** The cell 6 markdown says spikes "start within seconds of the first trial and end with the task". The cell 5 output contradicts this: first spike up to 2462 s before the first trial, last spike up to 2055 s after the last. The shared trains in cell 10 largely explain it, and alignment is shown properly in cell 8 (TTL-1 and start_time agree to 0 ms; selectivity rises after onset).
5. **[does not affect a conclusion]** Cell 23: the `reversed_1` flag only requires some label-1 images to be in the encoding block (`> 0`). The strict count is 78 of 87, still most. In the 7 sessions with 50 encoding trials and in CS53_123, only 52 to 98% of "old" images appear in the file's encoding block. This points to encoding trials missing from those files, and the notebook does not mention it.
6. **[does not affect a conclusion]** Cell 43: sessions with all five hit rates equal get a slope of exactly 0 (the minimum shown) and are kept. Sessions with all false-alarm rates equal are dropped. The treatment is asymmetric but does not change p < 0.05.
7. **[does not affect a conclusion]** Cell 31 takes IsolationDist as the paper's IsolDist. This is a reasonable stated assumption (the column's description is "IsolDist"). Without it, the column-presence part of units-table would fail and the outcome would still be partial at best.
8. **[does not affect a conclusion]** Cell 39's variant drops "the two sessions whose every unit repeats" from the behavioural AUC. Behaviour is not duplicated, so this variant has no meaning. It is harmless.
9. **[does not affect a conclusion]** Possible misreading in the claims file, reported here and not corrected: for fig5f-site-proportions, the paper's text says it compared "the existing and new dataset" (earlier release against the 23 new sessions). The claim tests CS against TWH, following the Figure 5f legend and the code's constants. Under the text's reading the groups differ: 14 new CS sessions belong to "new".

I tested `window_rates`, `cumulative_roc`, `auc`, `zroc_slope`, `accuracy_fixed`, `isi_fraction` and `bootstrap_mean_equal` on synthetic inputs, and all behaved as expected. For example, the z-ROC slope is 0.997 for equal variance and 0.800 for an old-item SD of 1.25, and random responses give an AUC of 0.499.

## C. What I could not check

- **The paper's code at commit 1d95162** (bootstrapMeanEqualTest mode, adjustHF, cal_auc, dynamic_split, calcZROCSlope, NO_behavior_evaluateSessionStatus) was not available to me. The helper's descriptions of these are taken on trust. An MS count with a studentized bootstrap under the main reading would settle problem 1.
- **`imp` values.** The notebook prints only a non-missing count. The raw dtype, fill value and attributes of `electrodes/imp` in one file would show whether impedance is absent or stored as a sentinel value.
- **H48 session 98.** Why it is absent from the dandiset and from Online-only Table 1. A per-session unit count for H48 against Faraut et al. would help, as would the source of the 37-neuron gap between 1539 and 1576 in cell 61.
- **Image identity.** The task-structure and label tests rely on `external_image_file` names, not image pixels. A check that the 50-trial sessions' "old" images match the encoding images would need the image arrays, which the notebook deliberately does not read.
