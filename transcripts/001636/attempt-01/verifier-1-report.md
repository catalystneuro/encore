# Verifier report, round 1: Pasquereau & Turner 2013 on DANDI 001636 (0.260518.1819)

The claims file has 28 claims. No attempt record was among my materials, so the tally comes from the claims file and my own outcomes: 4 reproduced, 3 partially reproduced, 4 not reproduced, 17 blocked.

The deciding fact is the false-positive check. At the pseudo onset, the main detection crosses its threshold in 0.22 of cell-directions, against an allowed 0.0033 to 0.03. The claims file's rule then blocks every claim that uses the selection of responses as methods_underspecified. That is 15 claims; for each I note what its own criterion would have given.

The paper's full text is saved under `paper/`.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| cell-counts | reproduced | Cell 18 gives exactly 112/159 cells, 49/54 PTNs, 31/48 CSNs, and 3 dual-projecting units. |
| monkey-l-perturbations | blocked (data_missing) | Cell 3 finds no monkey L perturbations. I streamed 7 monkey L files: `torque_perturbation_type` is "none" and onsets are NaN in every trial, and the pre-MPTP torque command is all NaN. The post-MPTP torque commands do hold 31 to 43 excursions per 60-trial file, but these are smooth ~100 ms commands at 0.05 s or 4 to 5 s after the center target, with 10 to 20 deg movements. They are not 50 ms hold-period impulses, so nothing can be tested. |
| baseline-rate | reproduced | Cell 21: all six means are within tolerance (M1 12.4/8.9, PTN 18.0/14.5, CSN 3.4/3.4). PTN Mann-Whitney p = 0.034 (< 0.05); CSN p = 0.73. |
| ptn-faster-than-csn | reproduced | Cell 23: 18.0 against 3.4 spikes/s, p = 1.3e-11. |
| antidromic-latency | partially_reproduced | Cell 25: all four means are within tolerance and PTN p = 0.54. The CSN increase gives p = 0.018, just above the 0.05/3 = 0.0167 threshold. |
| false-positive-rate | not_reproduced | Cell 27: the any-crossing rate over 0 to 200 ms is 0.22 (main) and 0.46 (t-test variant). Unperturbed trials (cell 28) give 0.19, and stationary Poisson spike trains through `detect` give 0.13 to 0.20 (my test). So the excess comes from the threshold procedure. A single run cannot tell whether the paper's claim is wrong or its procedure differs. |
| torque-related-fractions | blocked (methods_underspecified) | Blocked by the false-positive rule. The criterion would give not reproduced: 1 of 6 percentages in tolerance (cell 30), and CSN pre-MPTP is 16% against 45%. |
| prevalence-unchanged | blocked (methods_underspecified) | Blocked by the rule. The main detection gives all p > 0.29 (would be reproduced); the t-test variant gives M1 p = 0.0014 (cell 32). |
| ptn-more-responsive | blocked (methods_underspecified) | Blocked by the rule. Would be partial: p = 5.6e-12, but 68.9% and 16.5% are both outside tolerance (cell 34). |
| one-direction-half | blocked (methods_underspecified) | Blocked by the rule. 51.5% against 44 ± 4.4 (cell 36). |
| excitatory-majority | blocked (methods_underspecified) | Blocked by the rule. Would be partial: M1 post-MPTP 76.7% and PTN post-MPTP 59.3% are outside tolerance; the PTN test gives p = 0.47 (cell 38). |
| magnitude-unchanged | blocked (methods_underspecified) | Blocked by the rule. 11 of the 12 tests have p < 0.05 and all magnitudes are smaller after MPTP (cell 40), so the outcome would be not reproduced. |
| venus-response-magnitudes | blocked (methods_underspecified) | Blocked by the rule. At best 4 of 8 values are within tolerance, under reading (a) (cell 41). |
| latency-shorter | blocked (methods_underspecified) | Blocked by the rule. All 4 KS p < 0.05 and 8 of 8 means are within tolerance (cell 43), but the t-test variant gives no significant comparison (KS p = 0.27 to 0.87). |
| latency-not-training | blocked (methods_underspecified) | Blocked by the rule. Pooled rho = -0.26, p = 0.002, which is confounded with MPTP state; within each state p > 0.2 (cell 45). |
| fwhm-shorter-ptn | blocked (methods_underspecified) | Blocked by the rule. Would be partial: flexion p = 0.039, extension p = 0.39 (cell 47). |
| dsi-reduced | blocked (methods_underspecified) | Blocked by the rule. 7 points lower after MPTP, p = 0.10 (cell 49). |
| venus-dsi | blocked (methods_underspecified) | Blocked by the rule. 3 of 6 means are within tolerance (cell 50). |
| dsi-not-baseline | blocked (methods_underspecified) | Blocked by the rule. F = 0.58, p = 0.63 (cell 51). |
| kinematics-slower | not_reproduced | Cell 55: peak velocity rises 28.8% and amplitude 15.2% after MPTP, the opposite direction to the paper. The restricted variant (sessions with the middle command size) also rises. |
| kinematic-latency-unchanged | not_reproduced | Cell 57: MPTP F = 1032, p ≈ 0. The middle-size-only variant gives p = 0.79, but the measure itself is suspect (problem 5). |
| emg-m2-larger | reproduced | Cell 61: m2 is larger after MPTP on all three triceps channels, KS p ≤ 5e-15. This is the criterion's result, but the stimulus differs between states (problem 3). |
| emg-duration-longer | partially_reproduced | Cell 63: durations are longer after MPTP (KS p = 1.8e-39), but the means of 24.5 and 50.4 ms are outside 57 ± 6 and 79 ± 3. |
| emg-onset-unchanged | not_reproduced | Cell 63: onset 40.8 against 24.0 ms, KS p = 5.5e-21. |
| emg-m1-weak | partially_reproduced | Cell 65: post-MPTP passes (96.5%, ratio 0.22). Pre-MPTP m2 > m1 in only 73.5% (< 75%), though its median ratio is 0.10. |
| velocity-matched-magnitude | blocked (methods_underspecified) | Blocked by the rule. Even without it, the test cannot run: no pre-MPTP session reaches 130 deg/s (maximum 145, cell 67), and only 1 response falls in the window. |
| session-correlations | blocked (methods_underspecified) | Blocked by the rule. The m2 correlation gives p = 0.011 < 0.0125 when the two states are pooled, and p > 0.36 within each state (cell 69). |
| trial-correlations | blocked (methods_underspecified) | Confirmed in the paper's Methods: it names a "trial-to-trial response latency" but never defines one. Per-trial spikes, angle and EMG do exist for monkey V, so the claim could be tested under a stated definition. |

## B. Problems

1. **[affects a conclusion]** `stretch.detect` (main method): the threshold is t × the SD over time of the trial-averaged SDF. This is not a test of trial-to-trial variance, and its family-wise false-crossing rate is 0.13 to 0.22 (cells 27 and 28, and my Poisson test). Low-rate cells are hit hardest: the 14 cell-directions with a flat baseline can never respond, and single baseline spikes inflate the SD, which plausibly explains the 16% CSN fraction. The Methods' literal reading, a 2-tailed t-test against the baseline, is closer to the "trials" variant, which also fails (0.46). In cell 27 the response rate at the pseudo onset is 0.044 against 0.37 at the true onset, so about 12% of detected responses are expected to be false. Cells 30 to 51, 67 and 69 compare results that the rule blocks.
2. **[affects a conclusion]** Cell 13 shows the torque command step differs by state: most post-MPTP sessions have a pulse 4 times the usual pre-MPTP size, with a rebound, while the paper says every impulse was 0.1 Nm. The main kinematic and EMG tests therefore compare different stimuli. The middle-size variant has only 12 post-MPTP sessions and 1 to 6 EMG channel-sessions, and it reverses or removes the effects (triceps longus 1 m2 is lower after MPTP, p = 0.013; duration and onset p > 0.18). `emg-m2-larger` is reproduced on the criterion but cannot be attributed to MPTP.
3. **[affects a conclusion]** Cells 53 and 55: torque-induced amplitudes are 2.4 to 3.8 deg and session peak velocities stay at or below 145 deg/s. The paper reports a mean displacement of 10 deg and a matched range of 130 to 200 deg/s. My test shows `stretch.kinematics` keeps peak velocity and amplitude within about 10%, so the filter is not the cause. The notebook never compares the absolute scale with the paper. This affects `kinematics-slower` and makes `velocity-matched-magnitude` untestable.
4. **[affects a conclusion]** `stretch.kinematics`: post-MPTP flexion latency averages 3.2 ms, earlier than the command step 4 to 7 ms after the labelled onset (cell 7). The zero-phase filtfilt with 101 taps smears onsets earlier, more so for fast movements (my test: a true onset at 10 ms is detected at 9 to 17 ms). The 490 trials already moving before onset are kept, and a latency of 0 is possible. The latency ANOVA in `kinematic-latency-unchanged` mainly reflects movement speed and command size.
5. **[does not affect a conclusion]** `stretch.dsi` assigns categories from which directions respond and their signs, as fixed in the claims file. The paper classifies by DSI value (> 1 reciprocal, 0.5 to 1 bidirectional, ≈ 1 unidirectional, < 0.5 non-directional). This would matter for `dsi-reduced` if it were unblocked.
6. **[does not affect a conclusion]** `detect` takes the first crossing within 20 to 60 ms even when an earlier crossing at 0 to 19 ms exists. The paper's onset is the first crossing overall.
7. **[does not affect a conclusion]** Cells 45 and 69 pool pre- and post-MPTP for correlations whose variables both shift with MPTP; within each state, nothing is significant. Cell 49 runs a 2 × 4 chi-square with a zero cell (no reciprocal cells pre-MPTP).
8. **[does not affect a conclusion]** Cell 63: the median pre-MPTP EMG duration is 9 ms, which looks like short threshold blips. The files describe the EMG as sample-hold integrated over 10 ms, where the paper says low-pass filtered at 100 Hz, which can shift onsets by up to about 10 ms. The outcomes stand on the criterion.
9. **[does not affect a conclusion]** Cell 65 computes m1/m2 ratios that include channel-sessions with m2 ≤ 0.

## C. Not checked, and the output that would settle it

- **Angle scale.** I could not tell whether the dandiset angle matches the paper's degrees. A comparison of the notebook's own active-movement amplitude and peak velocity with the trials-table columns `target_amplitude_degrees`, `derived_movement_amplitude` and `derived_peak_velocity` would settle it.
- **Whether the threshold matches Figure 3.** Example mean SDFs with their thresholds drawn, plus the pseudo-onset false-positive rate split by baseline rate and by number of trials, would show this.
- **Actual torque against command.** The files have no torque calibration, so only an archive torque-sensor channel, if one exists, could show whether the larger post-MPTP command meant larger torque.
- **Monkey L.** I streamed 7 of the 149 files. A table of the monkey L torque-command excursions relative to trial events, for every file, would confirm that none are hold-period impulses.
- **Plots.** I did not inspect the plotted figures; my judgements rest on the printed outputs.
