I've built and run the entry at `entries/pasquereau-2013`, written the record at `attempts/pasquereau-2013-03.yaml`, and built the handover. I did not verify my own work and committed nothing. The notebook says that version 0.261124.1906 was asked for; it is also the newest published version.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cell-counts | reproduced (115/157 cells, 51/54 PTNs, 32/48 CSNs, 3 dual-projecting) |
| monkey-l-perturbations | blocked, data_missing |
| baseline-rate | reproduced (all 6 means in tolerance; PTN p = 0.020, CSN p = 0.65) |
| ptn-faster-than-csn | reproduced (p = 6.3e-12) |
| antidromic-latency | partially reproduced (means hold; CSN p = 0.019, above 0.05/3) |
| false-positive-rate | blocked, methods_underspecified (measured 0.23) |
| torque-related-fractions, prevalence-unchanged, ptn-more-responsive, one-direction-half, excitatory-majority, magnitude-unchanged, venus-response-magnitudes, latency-shorter, latency-not-training, fwhm-shorter-ptn, dsi-reduced, venus-dsi, dsi-not-baseline, velocity-matched-magnitude, session-correlations | blocked, methods_underspecified (they depend on false-positive-rate); results computed and shown, not deciding |
| kinematics-slower | not reproduced (+28% velocity, +15% amplitude after MPTP) |
| kinematic-latency-unchanged | not reproduced (F = 709) |
| emg-m2-larger | reproduced |
| emg-duration-longer | partially reproduced (22 and 52 ms against 57 and 79 ms) |
| emg-onset-unchanged | not reproduced (44 to 25 ms, p = 6e-22) |
| emg-m1-weak | partially reproduced (pre-MPTP 74.0%, just under the 75% asked) |
| trial-correlations | blocked, methods_underspecified |

## 2. Dataset, assumptions and questions

**What the dataset shows:**
- **Counts match.** Cell counts by MPTP state and projection type match the paper's monkey V table to within 3 cells.
- **No duplicates.** No recording is deposited twice (spike trains, angle and EMG windows compared across files), and every unit's MPTP flag agrees with its file name.
- **Clocks are consistent.** The torque command leaves rest 4 ms after the marked onset, and spikes cross the threshold far more often after the onset than after a pseudo onset.
- **Monkey L has no perturbations.** No Leu file marks one, and the torque command is NaN in 114 of 148 files. Finding rated major.
- **Kinematics differ from the paper.** Displacements are about 3 to 4 deg, where the paper gives 10 deg. After MPTP they are faster and larger, the reverse of the paper. Finding rated major.
- **Torque pulses are about 3 times larger after MPTP** (in arbitrary units), where the paper describes one fixed 0.1 Nm pulse. This confounds the before/after comparisons of movement and EMG. Finding rated minor, because the file description notes the varying levels.

**The detection problem.** The claims file's detection crosses its threshold in 23% of cell-directions after a pseudo onset, and in 20% of trials with no torque at all. The paper implies about 1%. I ran three other readings of the Methods' t-test (47%, 35%, 1.3%). The one that matches the paper's rate finds a response in only 20% of real cell-directions, against the paper's 62 to 75% of cells. No reading gives both, so the selection-based claims are blocked.

**Questions for the paper's authors** (recorded as methods_unavailable findings):
- How was the detection t-test computed?
- How was the single-trial response latency defined?

**Assumptions:** none adopted. The two readings of the EMG channel rule give the same outcomes.

**Questions to a reader:** none.

**Earlier attempts:** I came across none. The claims file's own header says its author had seen a data check and mentions "repeated files". That is from the claims file, not an earlier attempt's results; I found no repeated files in this version.

## 3. Protocol points

1. The rule to block a claim when its false-positive rate is far from the paper's does not say what happens to a claim that is itself the false-positive rate. I blocked false-positive-rate as methods_underspecified, recorded the measured value, and blocked its dependents through `depends_on`.
2. The protocol does not say whether a claim blocked through a dependency should still show its numbers. I computed and showed them all, marked as not deciding.
3. "Break down by session when there is one subject" does not fit 291 sessions. I broke key results down by MPTP state instead.
4. archives.md says to read NWB files with pynwb. I list one file with pynwb and read the other 438 directly with h5py, because building the pynwb objects for every file is too slow. The helper's docstring says so.

## 4. Runtime and failures

- The notebook runs in 344 s from a clean environment; `entry.py all` passes with 0 errors.
- The record validates against the schema and has one outcome for each of the 28 claims.
- Nothing failed. The run finished at about 17:00 UTC.
