**Prince et al. 2025 (DANDI:001371) — verifier report, round 1**

The claims file has 52 claims. The notebook tests 33 and blocks 19 (all the LSTM and choice-decoding claims). Under my reading of the outputs: 20 reproduced, 7 partially reproduced, 6 not reproduced, 19 blocked.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| recordings | partially_reproduced | 7 animals and 66 sessions match. CA1 has 3545 units (3892 ± 389, within). PFC has 2271 (2557 ± 256, outside). 633 units in 5 sessions have no region label. The all-unit total, 6449, equals the paper's exactly (cells 3, 9). |
| trial-mix | not_reproduced | Pooled fractions are 0.737 / 0.189 / 0.074 and per-session means 0.750 / 0.181 / 0.069, all outside tolerance. The counts 7172 / 1840 / 717 equal the paper's own counts (cell 11). |
| task-timing | reproduced | Under readings (c) all trials and (a) t_delay2 to choice: 10.559, 1.403, 6.020 (switch; 6.06 pooled with stay), 21.00 and 20.88 s, all within tolerance (cell 13). |
| fig1b-above-chance | reproduced | Session reading: W = 125.5 and 48.5 equal the paper's values. p = 6.1e-10 and 3.3e-11. Means 0.649 and 0.745 (cell 15). |
| fig1b-window-performance | reproduced | With 15-trial windows the window counts are 6252 and 1002, exactly the paper's n. Means and medians are 0.678 / 0.667 and 0.775 / 0.800 (cell 17). |
| fig5a-stay-performance | reproduced | 15-trial windows: n = 117, as in the paper; mean 0.921, median 0.933 (cell 19). |
| fig1d-heading-switch | reproduced | On both sides, switch trials point toward the initial side at the cue bin (+0.198, +0.183) and toward the new side in the last bin (−0.318, −0.154). Delay only trials stay toward the initial side (+0.197, +0.217) (cell 21). |
| tuning-tiles-track | reproduced | Every track bin is some unit's peak, with no empty runs, in both regions. The 4 empty bins are the gaps between track segments (cell 25). |
| decoding-validation | reproduced | (a) Error is below the uniform null in 52/55 CA1 and 46/46 PFC sessions. (b) The confusion-matrix rule holds in 37/46 and 35/46 bins (cell 27). |
| fig2e-hpc-goal-increase | reproduced | Under both trial-type readings and both inclusion rules, the ANOVA gives p ≤ 2e-18, and switch exceeds delay only with Tukey p ≤ 4.9e-7 for each arm. Means 0.129 / 0.129 against 0.090 / 0.100 (cell 29). |
| fig2e-hpc-arms-equal | reproduced | LME p = 0.172; per-session Wilcoxon p = 0.269 and 0.436. Means −0.0001 and −0.0097 (cell 31). |
| sfig2e-goal-bias | reproduced | 0 to 1.5 s: 0.460 of bins and 0.670 of trials, both within tolerance. The 0 to 2.5 s reading is also within (cell 33). |
| sfig3c-goals-over-retrospective | not_reproduced | Initial and new arm against the retrospective zone: Tukey p = 0.365 and 0.356 (cell 35). |
| sfig3c-retrospective-unchanged | reproduced | Retrospective zone, switch against delay only: Tukey p = 0.122 (final rule), 0.318 (train rule) (cell 37). |
| sfig3ab-original-vs-update-cue | partially_reproduced | Back-half contrasts hold (z = 9.5 and 11.8). Front-half contrasts are in the right direction but not significant (p = 0.119 and 0.139). The criterion needs all four (cell 39). |
| sfig2f-all-trials-encoder | partially_reproduced | Reading (a) passes for both arms under both outcome readings. Reading (b), the 80/20 split with 269 switch trials, fails for the initial arm (p = 0.935). The criterion needs every reading (cell 41). |
| sfig5f-pfc-wider-spread | partially_reproduced | PFC is wider than CA1 (p = 3e-8). The values, 3.88 and 4.41 bins, are far outside 2.4 ± 0.25 and 3.13 ± 0.27. The spread implementation is questionable (problem 1) (cell 43). |
| sfig5g-ca1-more-goal-coding | reproduced | CA1 exceeds PFC for both arms, z = 14.1 and 12.9. Values are within tolerance (cell 45). |
| fig2g-pfc-no-goal-increase | not_reproduced | Under reading (a): ANOVA p = 0.038 and new-arm contrast p = 0.035 (train rule 0.048 and 0.043). Reading (b) passes. The criterion is not met when any test gives p < 0.05 (cell 47). |
| sfig5e-pfc-windows | not_reproduced | New-arm contrasts: p = 0.019 (0 to 1 s), 0.035 (0 to 1.5 s), 0.024 (0.5 to 1 s) (cell 49). |
| fig3c-theta-phase-segregation | not_reproduced | Under both central-zone readings, central exceeds both goal arms in the first half cycle as well, so the two first-half contrasts go the wrong way. Reading (b): 0.148 central against 0.129 goal arms. The within-location phase shifts do go in the paper's direction (cell 73). |
| fig3b-theta-pre-post | reproduced | Under all readings both arms rise (z ≥ 7) and central falls (z ≤ −16) (cell 75). |
| sfig6-theta-switch-over-delay | reproduced | All ANOVAs give p < 1e-18; all switch against delay only contrasts give p < 1e-8 with switch higher (cell 77). |
| fig3d-new-arm-theta-modulated | reproduced | New arm p = 0.0049, initial arm p = 0.145. The stored-phase and train-rule variants agree (cell 79). |
| fig5d-stay-hpc-like-delay | reproduced | Final rule: p = 0.851 and 0.063. This is fragile: under the train-rule variant the new arm gives p = 0.032 (cell 51). |
| fig5d-stay-hpc-below-switch | partially_reproduced | Initial arm: stay is lower, p = 2.3e-6. New arm: p = 0.377 (cell 53). |
| sfig10-stay-transient-new-arm | reproduced | New arm, stay higher, p = 0.0365; initial arm p = 0.999 (cell 55). Window caveat in problem 6. |
| fig6b-hpc-new-lower-incorrect | reproduced | Methods GLM: correct exceeds incorrect for the new arm, z = 3.72, p = 0.0011 (cell 59). |
| fig6b-hpc-initial-no-difference | reproduced | Methods GLM p = 0.119; code variant p = 0.061 (cell 61). |
| fig6-hpc-pre-cue-initial-higher-incorrect | reproduced | Incorrect higher, z = −4.75, p = 1.2e-5 (cell 63). |
| sfig12-delay-hpc-no-outcome-difference | not_reproduced | Methods GLM: initial arm p = 0.0123. Only the code variant, which does not decide, passes (cell 65). |
| fig7c-hpc-commitment-new-arm | partially_reproduced | rho = +0.057, p = 0.043: sign and p hold, but rho is outside 0.124 ± 0.012 (cell 67). |
| fig7c-hpc-commitment-initial-arm | not_reproduced | rho = +0.058, p = 0.040 (cell 69). |
| fig4a, fig4f ×2, fig4d, sfig7d, sfig7e, fig4h ×2, fig4g, fig5f ×3, fig6d ×3, sfig12-delay-pfc, fig7e ×2 (18 claims) | blocked (other: compute) | They all need the per-session LSTM. The notebook estimates 9.9 h of single-process compute (cell 81). The data are present: the helper streamed the velocities, position and view angle for all 66 sessions. |
| fig6e-predict-outcome | blocked as given, but partly testable | The CA1 half is an SVM on CA1 initial minus new position decoding and needs no LSTM. It was not run. |

### B. Problems

1. **[affects a conclusion]** `spread_bins`: the spread is measured to the outermost bins above threshold anywhere in the posterior. The Methods say it is how far from the peak the posterior "dropped below this threshold", i.e. the first crossing next to the peak. On a synthetic bimodal posterior the helper gives 26 bins where the first-crossing reading gives 2. With non-local goal codes this likely inflates the values (3.9 against 2.4). The first-crossing reading was not run, and "as the paper's code" cannot be checked from here.
2. **[affects a conclusion]** `load_session`: 633 units in 5 sessions are labelled "unknown" because the units table has no `region` column. The helper never tries the units' `electrodes`/`electrode_group` link to `electrodes/location`, even though it reads that location for the ripple channel. Since the all-unit total matches the paper exactly, recovering these labels would likely put PFC in tolerance. It would also return 5 sessions to every decoding test. Whether the labels are recoverable is unverified (section C).
3. **[affects a conclusion]** fig6e: the CA1 part (SVM on CA1 position decoding) does not depend on the LSTM, but the whole claim was blocked.
4. **[affects a conclusion]** Cell 81, LSTM block: the limit is compute time, not data size, so "too_large" fits poorly. The 9.9 h estimate is single-process; the notebook already runs 8 processes for loading, which would give about 1.3 h. fig4a could also be tested on a subset of sessions, and the 60-min limit it cites is not something I can verify. At least partial testing looks feasible.
5. **[affects a conclusion]** `track_bins` / `zone_probs`, sfig3ab: the arm masks include gap bins 35 and 43, whose posterior is NaN. The front half of each arm is therefore effectively 2 bins against 3 for the back half, and the middle bin is dropped. The half split is the author's own and unstated; the two failing front-half contrasts (p ≈ 0.12–0.14) could change under another split.
6. **[may affect sfig10 and the 0 to 0.5 s window of sfig5e]** `aligned_edges` / `window_mean`: ±2.5 s in 0.2 s bins gives 25 bins, so one bin is centred at 0 (−0.1 to 0.1 s). Its centre comes out as +4e-16, so it lands in the post window. "0 to 1.5 s" is really −0.1 to 1.5 s (sfig2e confirms 8 bins per trial), and "0 to 0.5 s" is 3 bins, one of them straddling the cue. sfig10 (p = 0.0365) is borderline.
7. **[does not affect a conclusion]** `lme`: the ANOVA is a Wald χ² test, not F with Kenward-Roger df, and Tukey uses df = 1e4. With thousands of rows this is negligible. Tukey p values bottom out near 3.5e-13 and 1.8e-12. A quick null simulation (40 runs) gave no sign of miscalibration.
8. **[does not affect a conclusion]** Cell 25: tuning-tiles reading (a) is checked over track bins only, not all 50 bins as the criterion literally says. The literal reading cannot be met because of the gaps between track segments.
9. **[does not affect a conclusion]** `process_session`: the equal-cell subsampling uses `default_rng(0)` in every session, although cell 42 says "seeded per session".
10. **[does not affect a conclusion]** Validation decoding (cell 27) includes stationary bins while the encoder uses locomotion only. Median error is 9 bins (67 units), which passes the criterion but is coarse.
11. **[does not affect a conclusion]** In one session the computed and stored theta phases disagree (min cos = −0.49, cell 71); this was never looked into. The variants agree overall.
12. **Claims-file readings (reported, not corrected)**:
    - fig3c reading (a), the whole central arm, gives central ≈ 0.66 against the paper's 0.12/0.14. It cannot be the paper's quantity. The outcome is unchanged.
    - fig1b-window and fig5a: the paper's "40-trial windows" are in fact the code's 15-trial windows (exact n matches). The claims file already handles this.
    - trial-mix expects programmed probabilities that the paper's own counts do not give.

I tested `decode` (50/50 synthetic positions within 2 bins), `theta_phase`/`phase_at` (0 at peaks, π at troughs), `spread_bins` and `lme` on synthetic inputs.

### C. Not checked

- **Unit regions:** whether the 633 units can be assigned a region from the units' `electrodes`/`electrode_group` columns. Printing the units-table column list and the electrode locations for the 5 sessions would settle it. The API metadata does not show this.
- **Paper code details:** the code's spread rule, front/back half split, `home_boundaries` and retrospective zone. Spread under the first-crossing reading, and the bin lists of each zone, would have let me check these.
- **Choice decoding:** the whole LSTM pipeline. fig4a on even a few sessions and the CA1 SVM for fig6e would help.
- **Kenward-Roger df.** A comparison with lme4/lmerTest on one model would show whether the borderline p values move.
- **Window edges:** the bin centres actually used in each window (problem 6). Printing them would confirm the effective windows.
