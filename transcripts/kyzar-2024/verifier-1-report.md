**Verifier report, round 1: Kyzar et al. 2024 (doi:10.1038/s41597-024-02943-8), DANDI:000469 v0.240123.1806**

The claims file has 20 claims and the notebook tests all 20. My outcomes: 18 reproduced, 1 not_reproduced, 1 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| subjects-sessions | reproduced | Cell 10: 21 subjects, 41 sessions, 21 Sternberg, 20 screening; only subject 19 (P47HMH) has no screening session. My own API query of the pinned version agrees: 41 assets, 21 subjects, 20 ses-1 and 21 ses-2. Ages are 17 to 70, matching Table 1. |
| sternberg-unit-yield | reproduced | Cell 12: 902 units (Hipp 190, Amg 259, dACC 171, pre-SMA 250, vmPFC 32). Every count is exact. |
| screening-unit-yield | reproduced | Cell 14: 907 units, MTL 421. 421 is within 10% of both 449 and 421, so it matches the 421 reading exactly. |
| behavior-accuracy | reproduced | Cell 17: mean over sessions 88.73%. |
| behavior-rt-load | reproduced | Cell 19, correct trials: F(2,40) = 7.92, p = 0.0013, and the mean of session medians rises 1.055 → 1.130 → 1.198 s. I checked `rm_anova_load` against statsmodels AnovaRM on synthetic data and it gives the same F. |
| behavior-accuracy-load | reproduced | Cell 21: accuracy falls monotonically, 91.22 → 88.62 → 86.35%. |
| isi-violations | reproduced | Cell 25: on all units, the mean (0.428) is in tolerance but the s.d. (0.625) is not. With the code's filter (units below 4%, n = 901) the values are 0.416 and 0.498, both in tolerance. The criterion accepts either reading. |
| firing-rate | reproduced | Cell 27: mean 2.546 Hz, min 0.108 Hz, max 33.824 Hz. |
| projection-distance | reproduced | Cell 29: 13.774 ± 7.325 (734 non-zero values). |
| waveform-snr | reproduced | Cell 31: `peak_snr` gives 6.625 ± 3.632. `mean_snr` (1.65 ± 0.95) does not match, but one reading is enough. |
| cv2 | reproduced | Cell 33: 0.938 ± 0.138. |
| isolation-distance | reproduced | Cell 35: median 31.138 over the 676 non-NaN units. |
| screening-concept-mtl | reproduced | Cell 38: 140 MTL units (33.25%) under both the two-sided and one-sided readings, so the readings agree and both are in tolerance. The code's parametric test gives exactly 138 (32.78%). |
| screening-concept-mfc | reproduced | Cell 40: 27 (5.56%) under both readings, well below the MTL's 33.25%. This one is fragile: seed 46911 gives 29 (5.97%), outside tolerance (problem 2). With 20,000 permutations near p = 0.05 it gives 26 (5.35%). |
| fig4-screening-examples | reproduced | Cell 42: all 5 units pass under both readings and the parametric test. |
| sternberg-concept-mtl | reproduced | Cell 44: 96 (21.38%) two-sided and 100 (22.27%) one-sided, both in tolerance (upper bounds 103.4 and 23.03%). Parametric gives exactly 94 (20.94%). |
| persistent-activity | not_reproduced | Cell 46, maintenance window (0 to 2500 ms), under both cell readings and both trial readings: p ≤ 1.7e-7 with preferred higher, but the preferred mean is 2.57 to 3.13 Hz against 4.76 ± 0.476. No reading puts all four values in tolerance, and the trial readings agree, so the criterion gives not reproduced. The variant (Encoding 1 window, Encoding 1 mask, all-area concept cells) matches all four values and the p-value (4.63/4.64/2.59/3.58, p = 8.6e-22; parametric 4.76/4.71/2.67/3.66, p = 1.4e-21). So the paper's numbers come from the encoding window, as the claims file anticipated. |
| fig5-sternberg-examples | reproduced | Cell 48: both units are concept cells in the amygdala under every test, with maintenance rate higher on preferred-shown trials (5.05 vs 1.43 Hz; 5.73 vs 4.17 Hz). |
| maintenance-cells-mfc | reproduced | Cell 50: all permutation × non-preferred readings give 139 to 144 (30.68 to 31.79%) out of 453 MFC units, all in tolerance. |
| probe-cells-mfc | blocked (methods_underspecified) | Cell 52: the readings disagree. Label shuffling with the Encoding 1 rate gives 104 to 105 (about 23%) and fails on every seed. Sign flipping gives 111 to 124 and is in tolerance. Label shuffling with the pooled rate gives 109 on the main seed (just out) and 110 to 111 on the other three (just in). The code's t-tests give exactly 122 (26.93%). |

### B. Problems

1. **[does not affect a conclusion] `perm_ttest`, `signflip_test`.** Both count exceedances with a strict `>`. With discrete spike counts that makes them anti-conservative, and identical inputs get p = 1/2001.
   - Synthetic null check (Poisson at 0.3 Hz, maintenance 2.5 s vs baseline 0.5 s, 108 trials, 3000 runs): false-positive rate is 7.1% with `>` and 6.6% with `>=` for shuffling; 7.1% vs 6.2% for flipping.
   - Shuffling follows permutationTest.m; the sign-flip test is the author's own.
   - Correcting it would lower maintenance and probe counts by a few units. Maintenance keeps a 10-unit margin. Probe stays blocked, because shuffle-Encoding 1 already fails.
2. **[does not affect a conclusion] Cell 40.** The screening MFC result depends on the seed: 27, 29, 28 and 27 across four seeds, and 29 (5.97%) is outside tolerance. The 20,000-permutation refinement (26) supports the pass, but the margin is about one unit.
3. **[does not affect a conclusion] Cell 52.** The extra seeds are printed without tolerance flags. Computed from the printed values, pooled shuffling passes on 3 of the 4 seeds. The blocked outcome rests on shuffle-Encoding 1, which fails on every seed.
4. **[does not affect a conclusion] Cell 44.** The Sternberg concept counts are not repeated across seeds. The one-sided reading (100) is 3.4 units from the upper bound.
5. **[does not affect a conclusion] Cell 5, `sternberg_rates`.** Anomalous trials are kept:
   - Subject 9 has a trial whose maintenance, probe and Encoding 1 end share one timestamp (0 s maintenance), so its maintenance window covers the probe and response.
   - One trial has 0 s from fixation to Encoding 1 (min 0.000), so its baseline window falls on the image.
   - Two trials out of 2673.
6. **[does not affect a conclusion] Cell 10.** Subjects 13 and 14 (P39CS and P39CS_2) share age, sex, year and diagnosis in Table 1. Without the "_2" suffix there are 20 native IDs, so the 21 "patients" may be 20 people. The claims file's criterion counts subject IDs, and Table 1 lists 21 rows, so the outcome stands. Neither the claims file nor the notebook says so.
7. **[does not affect a conclusion; affects interpretation] Cells 38, 40, 44, 46, 50, 52.** The paper's numbers come from the code's parametric tests: they reproduce the paper's figures exactly (138, 26, 94; 144 with the code's t-test; 122 with the code's probe test; persistent activity 4.76/4.71/2.67/3.66). Following the claims file, the notebook uses the Methods' permutation tests as the main reading. That is the stated rule, not a misreading. Note that the probe block exists only under that rule.
8. **[does not affect a conclusion] `isi_violation_pct`, `cv2`.** These run on stored spike times, which are unsorted in 1 Sternberg unit (one negative ISI). That matches the code and the effect is negligible.

**Helper checks on synthetic inputs:**
- `window_rates` uses strict bounds as documented.
- `anova_f` equals scipy `f_oneway`.
- `perm_anova` p-values agree with the parametric ones (0.023 vs 0.017).
- `cv2` with ignoreMode 1 is correct.
- `encoding_rate_pooled` and its Encoding 3-from-Encoding 2 variant are correct, provided onsets are greater than 0.
- `rm_anova_load` matches AnovaRM.

No leakage issues apply. Windows, trial selection and denominators (449, 453, 421 and 486) follow the claims file. The paper states no chance level for any selection.

The claims file does not misread the paper. The persistent-activity criterion follows the paper's text (maintenance period); the paper's own numbers appear to come from the encoding window.

### C. What I could not check

- **Blocked claims:** the notebook marks none as blocked, so step 4 does not apply. For probe-cells-mfc all the data are present; the block comes from the methods alone.
- **Effect of tie handling on real counts:** needs the maintenance and probe counts recomputed with `>=`, or the p-values printed, for units with p between 0.04 and 0.06.
- **Seed robustness of the Sternberg concept counts:** needs a seed repeat in cell 44, like those in cells 40 and 52.
- **Tolerance flags for the probe seeds:** cell 52 should print them for each extra seed.
- **The 0 s fixation-to-Encoding 1 trial:** it is not listed. Cell 5 should print trials with fixation-to-Encoding 1 under 0.5 s.
- **Encoding 2 and 3 timestamps when absent:** cell 5 should show they are 0 or NaN exactly when the load leaves them out, which `encoding_rate_pooled` relies on.
- **The RT figure in cell 19:** an image I did not inspect. It does not decide the claim.
