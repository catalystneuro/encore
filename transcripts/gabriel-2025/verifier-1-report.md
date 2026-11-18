**Verifier report, round 1: Gabriel et al. 2025 (doi:10.1016/j.cub.2025.01.010), DANDI:001887 version 0.260902.1724**

The claims file has 43 claims. All of the data used came from Zenodo record 13381210. The DANDI API confirms that the dandiset has 56 assets (30 NWB files and 26 AVI videos) from 16 subjects, with no imaging, footprints or cell registration.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| data-neurons | reproduced | Cell 15 gives 1394 cells from 9 shocked mice and 847 from 7 NS mice on day 1, and 1031 and 967 cells on day 2. All are exact. |
| data-registered-cells | blocked (data_missing) | The Zenodo file list (cell 16) and the dandiset have no registration. The notebook never checked whether `minian_processed.mat` holds footprints, so whether registration could be redone is unknown. |
| fig1e-platform-time | reproduced | Cell 19: under both tone readings and both Sidak families, shocked mice rise from block 1 to block 4 on day 1 (pair 1-4 p=0.0047), and shocked against NS differs on day 2 (p≤0.017). This uses 16 of the paper's 20 mice. |
| fig1f-successful-trials | reproduced | Cell 20: the criterion holds under all four combinations of tone reading and Sidak family. |
| fig1g-freezing | blocked (methods_underspecified) | Cell 21: on the clock windows the all-pairs family fails (minimum p=0.092) and the block-1 family passes (p=0.047). Both families pass on the paper windows. The two Sidak readings the criterion names disagree. |
| fig1h-latency | blocked (methods_underspecified) | Cell 22: the within-group test passes only on clock windows with all pairs, through pair 2-4 (block 2 is the highest block). It fails under the other three combinations. |
| fig1kl-overall-encoding-similar | blocked (methods_underspecified) | Cell 27: only P2-F2 meets the criterion; D1 has p<0.05 under the other three readings. With the paper's tone windows, P2-F2 D1 also fails (p=0.047, cell 55). The claims file names methods_underspecified for this case. |
| fig1kl-day1-categories-similar | not_reproduced | Cell 28: every period and frame reading has at least one category with p<0.05 (1 to 6 of 8 comparisons). |
| disc-tone-cells-baseline | blocked (methods_underspecified) | Cell 30: "BL greatest" holds only under G2 with P1-F1 and fails under the other 7 combinations. Tone-onset activity is similar (all p≥0.18). Tone-onset cell counts are 33/37 against the paper's 61/52. |
| fig1k-mixed-day2 | not_reproduced | Cells 31 and 55: under every reading shocked mice have fewer mixed cells (24 to 31%) than NS mice (31 to 34%). The paper reports 51% against 25%. |
| fig1o-tone-to-mixed | blocked (data_missing) | Depends on a registration that is not public. |
| fig1o-nonmod-to-mixed | blocked (data_missing) | Same as above. |
| fig1p-platform-exit-excited-day2 | partially_reproduced | Cell 32: shocked mice are higher (Welch p=0.044). The cell counts (77 shocked, 84 NS) fall outside the tolerance of 104±10.4 and 100±10. With the paper's tone windows, p=0.117 (cell 55). |
| fig1q-platform-exit-inhibited-day2 | reproduced | Cell 33: p=0.558. The cells selected (40 shocked, 65 NS) are far from the paper's 74 and 82. |
| fig1pq-freezing-day2 | reproduced | Cell 34: 3 of 4 tests have p<0.05. Cell counts are within 2% of the paper's. |
| fig1r-mixed-exit-day1 | blocked (methods_underspecified) | Cell 35: reading M1 fails (day 1 p=0.49) and M2 passes narrowly (day 1 p=0.049, day 2 p=0.85). |
| figs1h-exit-not-shock | reproduced | Cell 36: p=0.046, shocked higher. Only 0 to 2 exits per session were removed, so this inherits the fragility of fig1p. |
| figs2-innate-behaviors | blocked (other: not run) | The escape part can be computed from the platform labels and tone windows. Jumping and rearing could come from the DeepLabCut CSVs on Zenodo or the dandiset videos. The notebook never shows that `Behavior.mat` lacks these labels. |
| fig2-day1-tone-stronger | reproduced | Cell 39: tone exceeds ITI under H1 and H2, for both groups, for entries and exits (all p≤0.0017). |
| fig2-day2-tone-further | blocked (methods_underspecified) | Cell 40: H1 holds. Under H2 the entries comparison has p=0.086. |
| fig2e-modulation-entries | not_reproduced | Cell 41: 0.755 against 0.710, p=0.086. Only 6 shocked and 5 NS mice qualify, against the paper's 7 and 7. |
| fig2f-modulation-exits | reproduced | Cell 42: p=0.006. Only 4 and 4 mice qualify, against the paper's 6 and 7. |
| fig3a-decoding-shock-gt-ns | blocked (methods_underspecified) | Cell 45: holds only under C1/N1, the Methods' coding (pre-shock p=0.036, shock p=0.012). It fails under the other three. It also uses 9 shocked mice where the legend gives 7 (problem 1). |
| fig3a-decoding-before-tone | blocked (methods_underspecified) | Cell 46: shocked mice are higher only under C1/N1. |
| fig3a-decoding-peak-preshock | not_reproduced | Cell 47: under all four readings the peak bin is at 32.6 s and the highest epoch is shock, not pre-shock. |
| fig3b-feature-cells-enhance | blocked (methods_underspecified) | Cell 48: E1 and E2 disagree in most combinations. Under C1/N1, the only reading where the all-cell decoder separates the groups, both E1 and E2 fail for K1 and K2. |
| fig3c-nonmod-cells-worsen | blocked (methods_underspecified) | Cell 49: E1 is false and E2 true under C1/N1; E1 and E2 are false elsewhere. |
| fig4b-hybrid-model-best | reproduced (see problem 6) | Cell 51: the hybrid model is lowest under T1/T2 and S1/S2, with Greenhouse-Geisser p from 0.012 to 0.0497. Every fitted α is 1.0. |
| figs3gh-behavior-similar | reproduced | Cell 53: 0 of 12 comparisons have p<0.05 under B1, A1 and A2. |
| fig4e, fig4f, fig4g, fig4h, fig4i, fig4j, fig4k, fig4l, figs3ab, figs3cd, figs3ef, figs4ab, figs4cd (13 claims) | blocked (other: not run) | The stated reason, "CILDS is MATLAB", is not a data limit. The traces, trial outcomes and learning rates are all in hand, and CILDS is a published method. |
| zenodo-dandiset-link | partially_reproduced | Cell 13: 25 of 30 sessions match (spread under 0.04 s). F1, F2 and F6 day 1 have no trial table, F3 day 2 has 9 trials against 10 tones, and F7 day 2 was converted from M7's file. The F1 and F2 BehaviorDEPOT arrays equal Zenodo's. |

The paper states no chance level for any selection, so there was none to compare.

### B. Problems

1. **[affects a conclusion]** Cell 44, decoding cohort. All 9 shocked mice are decoded, but the Figure 3 legend gives N=7 shocked mice, and the notebook does not state this. F2 has 9 successes and 0 failures, so its decoder sees only one class. Its F1 is constant and normalises to 0 under N1 and N2. F1 has 1 failure, and NS mice F7 and M6 have 1 success each, so their leave-one-out folds are also single-class. No exclusion rule was applied or run as a reading. This affects all five Figure 3 claims.
2. **[affects a conclusion]** Cell 25 and `pma.features`, event windows. Freezing calls match the paper's counts within 1 to 3% (for example 150/198 against 150/198 for NS on day 2), so `roc_calls` appears to be correct. I also checked it on synthetic data: the auROC equals sklearn's, and the null call rate is 3%. Calls for the event-window features are far off, though: tone-onset day 1 shocked 33/37 against 61/52, platform-exit day 2 shocked 77/40 against 104/74. So the tone-onset and platform event vectors are not the paper's. This is never flagged or explored. It drives the fig1p count failure, the cells behind fig1q and disc-tone, and the mouse numbers in fig2e and fig2f (6/5 and 4/4 against 7/7 and 6/7).
3. **[affects a conclusion]** Cells 24 to 55, tone timing. The `clock` tone windows are the author's assumption. Cells 10 and 13 support them well: hand-scored mismatches in the fast-camera sessions drop from 15 to 4, and the dandiset onsets agree at a constant offset. The paper's code, however, used the `paper` windows, and that reading was run only for behaviour, the overall and mixed proportions, and fig1p, where it flips the outcome (p=0.117). It was not run for the categories, disc-tone, fig1pq, fig1q, fig1r, figs1h, Figure 2, Figure 3, fig4b or figs3gh.
4. **[affects a conclusion]** Header table, cell 0. Thirteen CILDS claims and figs2 are blocked for software-language reasons. Nothing shown blocks them on data. figs3cd and figs3ef do not even need the learning rate.
5. **[affects a conclusion]** Claims file opening comment and `pma.rw_predict`, a possible misreading of the paper. The model updates with R(t+1), but the Methods give Δv_t = α(R_t − v_t), using the outcome at trial t. With R(t+1), the prediction for trial t+1 is built from trial t+1's own observation. On synthetic data, α=q=1 gives zero residual after every success. In cell 51 every α is fitted at the bound of 1.0, so readings L1 and L2 are identical. The hybrid model's win in fig4b may be an artifact of this target leakage. I could not check whether the deposited Python script really uses R(t+1).
6. **[does not affect a conclusion]** `decode_mouse`. C and gamma are chosen by cross-validation on all nine trials, test trial included, before leave-one-out testing. This leaks test data into model selection, but it is the code's method as the claims file gives it.
7. **[does not affect a conclusion]** `block_stats`. The Sidak tests are separate paired and Student t-tests, not post hoc tests from the ANOVA error term. Day 2 between-group results are well below 0.05, so the outcomes stand. One day 1 result (p=0.0477) is borderline.
8. **[does not affect a conclusion]** `cellsets`. The Figure 3B and 3C cell sets use only BL-F1 and D1-P1-F1, not the other period and frame readings.
9. **[does not affect a conclusion]** `decode_inputs`. Bin times assume 15 frames/s, but the data run at 14.89 frames/s, so epochs shift by about 0.2 s at 28 s.
10. **[does not affect a conclusion]** The behaviour tests use 16 of the paper's 20 mice (cell 8 states this). F3 day 2 block 1 has a single trial.

### C. What I could not check, and the outputs that would have settled it

- **Contents of the Zenodo files.** A printout of the field names in `Behavior.mat` (jumping, rearing, escape) and the variable names in `minian_processed.mat` (footprints, `ta_sigfn`) would show whether figs2, registration and CILDS are testable.
- **Whether calcium and camera share a clock.** Cell 10 shows no shock response under any shift. A per-mouse event-triggered trace on a strong event, such as freezing onset, under each reading would test it.
- **The source of the event-call discrepancy.** ROC call counts under alternative tone-onset and platform-exit windows, or with vectors built on camera frames, compared with the STAR Methods counts.
- **Sensitivity of the decoding claims to the cohort.** Results with F1 and F2 left out (N=7 shocked) and with single-class training folds dropped.
- **The RW update form.** A fit using R_t (the Methods' formula) alongside R(t+1), plus the fitted α and q from a start point other than [1, 1].
- **The tone-window question.** The `paper` tone reading for every ROC, Figure 2, Figure 3 and RW claim.
- **The hand-scored outcome coding.** I inferred that `avoids` means success only from the low disagreement with the rule (26 of 358 trials). Printing its values beside the rule's per trial would confirm it.
