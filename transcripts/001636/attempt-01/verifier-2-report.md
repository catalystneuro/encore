# Verifier report, round 2: Pasquereau & Turner 2013 on DANDI 001636 (0.260518.1819)

**Tally.** The claims file has 28 claims, and the attempt record gives an outcome for all 28:
- 4 reproduced
- 3 partially reproduced
- 3 not reproduced
- 18 blocked: 1 for missing data and 17 as methods underspecified (`false-positive-rate`, the 15 claims that depend on which responses are detected, and `trial-correlations`)

I saved the paper's full text from Europe PMC under `paper/`.

## 1. Agreement with the stated outcomes

I agree with all 28.

**`false-positive-rate`.** In round 1 I said not reproduced. I now accept blocked (methods_underspecified).
- The claim is about the paper's procedure, and this run can only measure a reconstruction of it.
- Stationary Poisson spike trains give 0.15 with the reconstructed detection (cell 37), so the rate mostly measures the reconstruction.
- A threshold calibrated to a false-positive rate of 0.01 moves the fractions of torque-related cells further from the paper's (cell 38). So the stated rate alone does not explain the gap.
- The record cites a protocol rule for this case. I could not read that protocol. The claims file itself only states the blocking rule for the claims that use the detected responses.

**Kinematics and EMG.** I agree with these outcomes on their criteria, with one caveat that the record already states. The torque command differs between the two states, so none of them can be attributed to MPTP. `emg-m2-larger` (reproduced) is the weakest. Its only same-command comparison runs the other way on triceps longus 1 (46.7 against 1.3, p = 0.013, with 40 and 6 channel-sessions; cell 87).

## 2. Statements the outputs do not support

**Cell 98.** "against 24 to 33 per group in the paper"
- The paper's counts are 24, 33, 22 and 31, so the range is 22 to 33.

**Cell 48, and the `ptn-more-responsive` notes.** "the CSN fraction is below the expected 30.4%" and "the CSN fraction is outside tolerance"
- The PTN fraction is also outside tolerance: 68.9% against 62.1 ± 6.2, whose upper bound is 68.3 (cell 47).

**Summary (cell 103), and the `methods_unavailable` finding.** "Poisson spike trains give the same"
- Poisson gives 0.15 against 0.22 observed (cells 35 and 37), so about a third of the observed rate is not explained.
- Cell 39 says the same thing more strongly: "the excess comes from the detection procedure, not from activity in the hold period". Most of the rate comes from the procedure, not all of it.

**Cell 92, and the `emg-onset-unchanged` notes.** "Pre-MPTP responses are small …, which delays their detected onset"
- Nothing tests this, and the threshold is relative (2 SD of the baseline).
- At the middle command size the post-MPTP onset is the later one (28.8 against 45.6 ms, cell 90).

**Cell 88.** "the median m2 is 0.61 at the smallest command size, 40.8 at the middle and 194.6 at the largest"
- The three medians mix states.
- The values left out work against a simple increase with command size: post-MPTP at the middle size is 1.81, and pre-MPTP at the largest is 17.09 (n = 5) (cell 87).
- The attempt record's notes give the middle-size post-MPTP value, but not the largest-size pre-MPTP one.

**Cell 80, and the `kinematics-slower` notes.** "session means 8.5 to 145.3 deg/s … lower than the paper's 130 to 200 deg/s"
- The upper end overlaps the paper's range.
- The supported statement is that the mean is 58.7 deg/s and only one response comes from a session in the window (cells 79 and 97).

**README.** "It takes a few minutes"
- Cell 104 prints 1.5 min. This is minor.

**Checked and supported.** Every other "Result:" sentence, the rest of the Summary and README, and every outcome note and finding in the attempt record matches the printed numbers.

I also checked the paper-inconsistency finding against the paper:
- The text gives 16.3 and 3.6 spikes/s, and Table 1 gives 18.3 and 3.2.
- Table 1's CSN counts are 13/13 and 10/11 against 11/13 and 8/9, and the table marks the change "## p < 0.01 (χ² test)".

**Round-1 reasons in the record.** They state my round-1 reasons faithfully and in my own words, with my problem points folded into the claims they concern. Two small gaps:
- Two points from my problem 1 are left out: the expected ~12% of false responses among those detected, and that the Methods' literal t-test reading also fails. Neither changes an outcome.
- The `velocity-matched-magnitude` reason repeats a sentence of mine that contradicts itself ("no pre-MPTP session reaches 130 deg/s (maximum 145)"). What cell 97 shows is that no pre-MPTP response comes from a session in the window. That error is mine, not the author's.

## 3. Round-1 points

**Resolved:**
- **Monkey L.** There is now a table of torque-command excursions for every file: 1 hold-window excursion in 2048 trials (cell 7).
- **Angle scale (problem 3).** Active movements are within 2% of the derived columns (cell 11), so the small torque-induced movements are in the data. The files have no torque-sensor channel.
- **Kinematic latency measure (problem 4).** The causal and not-moving variants were added, and post-MPTP latency is still shorter (F = 781 and 743, cell 82).
- **DSI categories (problem 5).** A variant classifies by DSI value (p = 0.42, cell 70).
- **First crossing as onset (problem 6).** A variant takes the first crossing overall; 6 of 202 responses have an earlier one.
- **Pooled correlations and the zero cell (problem 7).** Within-state results are reported, and the smallest expected count is given as 2.2.
- **Short pre-MPTP EMG responses (problem 8).** 63.6% of pre-MPTP durations are 10 ms or less.
- **m1/m2 ratios (problem 9).** Ratios over channel-sessions with m2 > 0 are now given.
- **Threshold diagnostics.** Example SDFs with their thresholds, and the false-positive rate split by baseline rate and by number of trials, were added (cells 37 and 38).

**Resolved as far as the data allow, but still bearing on conclusions:**
- **Detection procedure (problem 1).** The paper's procedure cannot be recovered. Every claim that uses the detected responses stays blocked.
- **Torque command differs by state (problem 2).** The outcomes of `kinematics-slower`, `kinematic-latency-unchanged`, `emg-m2-larger`, `emg-duration-longer` and `emg-onset-unchanged` all compare different stimuli. The only same-command check has 12 post-MPTP sessions, and 1 to 6 post-MPTP EMG channel-sessions per channel. Where it can be read, it removes the effect (or reverses it, for triceps longus 1 m2). The record says the differences cannot be attributed to MPTP, which is the right reading. The outcomes rest on the criteria alone.

**Still open:** I have not inspected the plotted figures. My judgements rest on the printed outputs.
