**Verifier report, round 1: Pasquereau & Turner 2013 on DANDI:001636 (0.261124.1906)**

The claims file has 28 claims. I re-ran the helpers `detect`, `sdf_trials` and `kinematics` on synthetic inputs and queried the archive's metadata; I did not download data or re-run the notebook.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| cell-counts | reproduced | Cell 20: 115/157 cells, 51/54 PTNs, 32/48 CSNs, 3 dual-projecting. All are within tolerance. |
| monkey-l-perturbations | blocked (data_missing) | Cell 15: all 5952 Leu trials are `not_available`. The dandiset description confirms "The Leu files contain no perturbation times". |
| baseline-rate | reproduced | Cell 24: all six means are within tolerance (PTN pre 18.49 vs 20.3±2.46). PTN p = 0.0198 (< 0.05), CSN p = 0.651 (≥ 0.05). The M1 test gives p = 0.0022, below the paper's 0.05/2. |
| ptn-faster-than-csn | reproduced | Cell 26: PTN 18.5 vs CSN 3.5 spikes/s, Mann-Whitney p = 6.3e-12. |
| antidromic-latency | partially_reproduced | Cell 28: all four means are within tolerance (CSN post 6.85 vs 6.1±0.89) and PTN p = 0.68 holds. The CSN test fails: p = 0.019, above 0.05/3 = 0.0167. The variant adding Leu units gives p = 0.0072. |
| false-positive-rate | blocked (methods_underspecified) | Cell 30: the pseudo-onset rate is 0.230, outside 0.0033–0.03. My synthetic test shows the claims file's procedure gives this rate on pure noise (B1). Only the `trial_sd` reading (0.013) falls in range. |
| torque-related-fractions | blocked (methods_underspecified) | Blocked through false-positive-rate, as the claims file's opening comment requires. For information only: under the blocked detection 2 of 6 are within tolerance (cell 32). |
| prevalence-unchanged | blocked (methods_underspecified) | Same gate. Cell 33 would give p > 0.39 for all three groups. |
| ptn-more-responsive | blocked (methods_underspecified) | Same gate. Cell 34: 70.5% vs 17.5%, χ² = 49. |
| one-direction-half | blocked (methods_underspecified) | Same gate. Cell 35: 52.8% vs 44±4.4%. |
| excitatory-majority | blocked (methods_underspecified) | Same gate (cell 36). |
| magnitude-unchanged | blocked (methods_underspecified) | Same gate. Cell 37 would be not reproduced: all 12 tests have p < 0.05. |
| venus-response-magnitudes | blocked (methods_underspecified) | Same gate (cell 38). |
| latency-shorter | blocked (methods_underspecified) | Same gate. Cell 39 shows all four KS tests p < 0.011 with post-MPTP latencies shorter, and 7 of 8 means within tolerance. |
| latency-not-training | blocked (methods_underspecified) | Same gate. Cell 40: pooled ρ = −0.26, p = 0.0016. |
| fwhm-shorter-ptn | blocked (methods_underspecified) | Same gate (cell 41). |
| dsi-reduced | blocked (methods_underspecified) | Same gate (cell 42: p = 0.09). |
| venus-dsi | blocked (methods_underspecified) | Same gate (cell 43). |
| dsi-not-baseline | blocked (methods_underspecified) | Same gate (cell 44: p = 0.31). |
| kinematics-slower | not_reproduced | Cell 48: peak velocity changes by +28.1% pooled and +29.7% flexion; amplitude by +14.8% and +11.1%. Both rise after MPTP under both readings. The matched-command variant (cell 50) also rises (+47%, +40%). |
| kinematic-latency-unchanged | blocked (other: the onset measure in `kinematics` is invalid) | Cell 52 gives F = 709, but the post-MPTP flexion mean onset (3.05 ms) comes before the command leaves rest (4 ms, cell 12). My synthetic test shows the measure finds onset at −5 to +1 ms for a true onset at 10 ms, then clips it to 0 (B2). The output does not test the claim. |
| emg-m2-larger | reproduced (by the criterion; confounded) | Cell 55: m2 is higher after MPTP in all three triceps channels, KS p ≤ 4e-15, under both inclusion rules. The torque was about 3× larger after MPTP, which this comparison does not control (B3). |
| emg-duration-longer | partially_reproduced | Cell 56: durations are longer after MPTP with KS p = 5e-33, but both means are outside tolerance: 22.2 vs 57±6 ms and 51.5 vs 79±3 ms. |
| emg-onset-unchanged | not_reproduced | Cell 57: onset 44.2 → 25.0 ms, KS p = 6e-22. Both inclusion rules give the same result. |
| emg-m1-weak | partially_reproduced | Cell 58: pre-MPTP m2 > m1 in 74.0% of channel-sessions (the criterion needs 75%; median m1/m2 = 0.14). Post-MPTP passes (98.3%, 0.25). The raw_sd rule gives 74.3% pre. |
| velocity-matched-magnitude | blocked (methods_underspecified via the gate; also data) | Only 2 of 581 session-directions have mean peak velocity in 130–200 deg/s (cell 17), leaving 0 or 1 responses (cell 45). It would stay untestable without the gate. |
| session-correlations | blocked (methods_underspecified) | Same gate. Cell 46 would be not reproduced: m2 ρ = −0.38, p = 0.0076 < 0.0125. |
| trial-correlations | blocked (methods_underspecified) | Methods (sentence 144 of the paper text) uses "trial-to-trial response latency" but never defines it. Detection is defined only on the trial-averaged SDF. |

**B. Problems**

1. [affects a conclusion] `detect`, cells 29–30. The false-positive gate could not have passed under the claims file's procedure. On stationary Poisson spike trains (3–20 spikes/s, 8–15 trials), `detect` gives an any-crossing rate of 0.14–0.22, close to the 0.230 found in the data. The paper's 0.01 is an analytic argument that ignores autocorrelation and the error in estimating the SD.
   - The `trial_sd` reading meets the gate (0.013, cell 30), but the notebook never ran the 15 dependent claims under it. The paper leaves the threshold's SD open, so this reading could change their outcome from blocked to tested. At the torque onset it flags only 20% of cell-directions, so torque-related-fractions would likely fail.
   - Possible misreading in the claims file, reported only: Methods (sentence 122) describes a "2-tailed t-test" of SDF values ms by ms against baseline. That matches the notebook's `ttest` variant, not the deciding mean ± t·SD band. The variant's rate (0.465) is worse, so the blocked outcome stands.
2. [affects a conclusion] `kinematics`, cells 48, 50 and 52. The forwards-backwards FIR spreads the velocity rise earlier in time. The 0–200 ms search has no requirement that velocity start below threshold, so early crossings are clipped to 0 ms. Larger, faster post-MPTP displacements are pulled earlier more, so the pre/post latency difference is partly a measurement artifact. Peak velocity and amplitude are not affected.
3. [affects a conclusion] Cells 16, 50 and 55–58. The torque command pulse is about 3× larger after MPTP (median 45.7 vs 181.6 a.u.). The paper reports one 0.1 Nm pulse, and the dandiset description does not mention the difference. For the kinematics a matched-command variant was run; for the EMG claims none was, so the m2, duration and onset differences cannot be separated from stimulus size. Pre-MPTP m2 is also tiny (median about 5 a.u. against 165–301 after), and many pre-MPTP channels have baseline SD below 1 a.u., which suggests the two periods may have different gain or signal quality. The notebook does not check this.
4. [affects a conclusion] Cell 17. The data's displacements (about 3 deg, 46–75 deg/s) are about a third of the paper's (mean 10 deg; 130–200 deg/s for velocity-matched sessions). The angle calibration was never compared with the file's `processing/behavior/ElbowVelocity` or the trials table's `derived_peak_velocity` and `derived_movement_amplitude`. A scale error would not flip the sign in kinematics-slower, but it does make velocity-matched-magnitude untestable.
5. [does not affect a conclusion] Cells 6 and 20. The notebook counts 115/157 cells; the claims file's data check found 112/159 exactly. The claims file says repeated files exist and should be left out of the session measures. The notebook's duplicate check (cell 10) finds none, and it loads `source_file` but never uses it. The counts are within tolerance either way.
6. [does not affect a conclusion] Cell 28 and the claims file. The paper corrects subset tests with Bonferroni–Holm (sentence 138); the criterion uses a flat 0.05/3. Under Holm, CSN would still be the smallest p tested against 0.0167, so the outcome is unchanged.
7. [does not affect a conclusion] Cell 15 and `load_meta`. The notebook computes `torque_cmd_steps` for the 34 post-MPTP Leu files that have a finite torque command but never prints it, so it is not shown whether perturbations could be recovered from the command in those files (B, C).
8. [does not affect a conclusion] Checked and correct: the `gamma_kernel` normalisation (spikes/s, causal), the offset, area and FWHM logic in `detect` (synthetic response: onset 34 ms, offset 153 ms), Yates correction in the 2×2 tables, the DSI formula and categories against Methods (sentences 134–137), and the type II ANOVA.

**C. What I could not check, and the output that would settle it**

- monkey-l-perturbations: the archive confirms no Leu perturbation times. Pre-MPTP stays blocked. Post-MPTP could be partly testable only if the torque command in the 34 Leu files shows pulses. Needed: `torque_cmd_steps` per Leu file, and one plotted command trace.
- The 15 claims blocked by the gate: needed are their results under the `trial_sd` reading (B1).
- Kinematic latency: needed are the latency distribution per state (fraction at exactly 0 ms), the velocity at t = 0, and onsets from a causal filter or with a below-threshold requirement before onset.
- Angle scale: needed is the computed per-trial peak velocity plotted against `derived_peak_velocity` or `ElbowVelocity`.
- EMG confound: needed are the EMG claims rerun on perturbations with matched command size (60–250 a.u.), and grand-average pre and post traces per channel.
- Repeated files and the 112 vs 115 discrepancy: needed are the files sharing a `source_file` value, and the units that differ from the claims file's data-check selection.
