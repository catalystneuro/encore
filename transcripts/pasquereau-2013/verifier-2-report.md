**Verifier report, round 2: Pasquereau & Turner 2013 on DANDI:001636 (0.261124.1906)**

Counts come from the claims file and the attempt record. There are 28 claims and 28 outcomes: 4 reproduced, 3 partially reproduced, 3 not reproduced and 18 blocked. Cell numbers below are positions in the re-executed notebook, counted from 0.

**1. Outcomes**

I agree with all 28 stated outcomes. No outcome has `assumed: true`, so there is no assumption to check.

- **cell-counts, baseline-rate, ptn-faster-than-csn: reproduced.** Agree (cells 25, 31, 34).
- **antidromic-latency: partially reproduced.** Agree (cell 37: CSN p = 0.019, above 0.0167).
- **monkey-l-perturbations: blocked, data missing.** Agree (cells 20, 28).
- **false-positive-rate and the 15 claims that depend on it: blocked, methods underspecified.** Agree. The false-positive rate is 0.230 (cell 40). The `trial_sd` reading, shown in cells 44–58, would not reproduce torque-related-fractions either (20.0% and 18.5% of M1 cells against 75 and 68% expected, cell 44).
- **velocity-matched-magnitude: blocked.** Agree. It would also stay untestable because of the data: only 2 of 581 session-directions fall in the velocity range (cell 22).
- **trial-correlations: blocked.** Agree.
- **kinematics-slower: not reproduced.** Agree by the criterion (cell 61). The torque pulse is still about twice as large after MPTP inside the "matched" 60–250 range (cell 72: median 90.9 against 181.8 units for flexion). So the faster, larger displacements cannot be separated from stimulus size.
- **kinematic-latency-unchanged: not reproduced.** I now agree; in round 1 I had it as blocked. The causal-filter variant is a valid onset measure. It gives shorter post-MPTP latencies (F = 422.5, and 146.2 within the 60–250 range; cell 66). The deciding F = 709 still comes from a measure whose post-MPTP flexion mean (3.05 ms) falls before the command leaves rest (4 ms, cell 14). The same stimulus-size confound applies.
- **emg-m2-larger: reproduced; emg-duration-longer: partially reproduced; emg-onset-unchanged: not reproduced.** Agree by the criterion (cells 73, 75, 77), with the same confound.
- **emg-m1-weak: partially reproduced.** Agree by the criterion (cell 79). Within the 60–250 range, though, the criterion is met in both states: 94.9% with median ratio 0.10 before, 97.1% with 0.26 after (cell 72).

**2. Sentences the outputs do not support**

- **Cell 59:** "No session has a mean peak velocity in the 130 to 200 deg/s range of velocity-matched-magnitude under either reading." Cell 22 shows 2 of 581 session-directions in that range, and cell 57 shows one post-MPTP flexion response there under the claims file's detection.
- **Cell 64:** "...the increase remains (+47.0% and +40.4%), so the command's arbitrary units do not explain it." Within that range the pulses still differ about twofold (cell 72: 90.9 against 181.8), so stimulus size is not excluded.
- **Cell 67** and the kinematic-latency-unchanged notes: "The variants that avoid this still find..." / "Variants that avoid this give the same outcome". The below-threshold ("quiet") variant still puts the post-MPTP flexion onset at 3.38 ms (cell 66), before the command leaves rest at 4 ms (cell 14). It removes the onsets clipped to 0 ms, but not the spread from the forwards-backwards filter. Only the causal variant avoids that.
- **Response to my round-1 point on kinematic-latency-unchanged:** "the artifact shrinks the difference but does not create it". Cell 66 shows the opposite. The pre-minus-post difference is 4.9 and 6.6 ms with the claims file's onset and 3.3 and 4.7 ms with the causal filter, and F falls from 709 to 422. The artifact enlarges the difference.
- **README:** "the EMG results hold at matched torque commands". **Cell 84 (Summary):** "the EMG claims were repeated at matched torque commands, with the same outcomes". Both fail on two counts:
  - The commands are not matched (cell 72: about 2× apart).
  - emg-m1-weak would change from partially reproduced to reproduced in that range (cell 72: 94.9% and 97.1%).
- **Finding 3 and the README:** "about three times larger (median 181.6 against 45.7 units)". Those medians differ fourfold. The means (174.7 and 58.4) give the 3× (cell 21).
- **Cell 84:** "the counts of cells ... match the paper's monkey V table". They are within 3 cells of it, not equal (cell 25: 115 against 112).
- **Cell 84:** "The post-MPTP Leu torque command moves at task events". Only one of the 34 files was timed against task events (cell 20).
- **Cell 84:** "evoked displacements (about 3 to 4 degrees)". Cell 22 gives 2.4 to 3.8.

Everything else checks against the outputs, including every number in the outcome notes.

Two smaller points on wording:
- The kinematic-latency-unchanged notes and cell 67 give "p < 1e-100", but the notebook prints this p only as 0.0000 (cell 66). From F = 709 on 1 and 577 degrees of freedom it is about 1.5e-102, so the claim is correct but not shown.
- The torque-related-fractions notes say "Blocked ... through torque-related-fractions", which names the claim as its own gate.

**My round-1 reasons in the record.** The `verifications` entry states my reasons faithfully. They keep my round-1 cell numbers, which now point to different cells: "cell 20" is now the Leu finding, and the cell counts are in cell 25. A reader following them will land in the wrong place.

**3. Round-1 points**

Resolved:
- B1: the 15 dependent claims are now shown under the `trial_sd` reading, and the possible misreading of the t-test is passed to a reader.
- B4: the angle's scale agrees with the 20-degree targets (cell 17).
- B5: source files are listed and no trial is repeated (cell 12). The 112 against 115 count difference is still unexplained but does not bear on an outcome.
- B6: Bonferroni–Holm is noted and gives the same result.
- B7: the Leu command is printed and plotted (cell 20).

Partly resolved: B2. The causal variant settles the direction of the latency change. The quiet variant does not fix the filter's spread.

Remaining, bearing on conclusions:
- **Torque size (B3).** No analysis compares the states at equal pulse size. Even within 60–250 units the post-MPTP pulse is about 2× (cell 72). This affects kinematics-slower, kinematic-latency-unchanged and all four EMG outcomes. For emg-m1-weak, the pre-MPTP shortfall disappears within that range.
- **EMG background.** The background differs by channel and state (cell 70). For triceps longus 2 the single-trial baseline SD is 2.98 before and 19.58 after MPTP. For triceps lateralis it is larger before (16.76 against 8.02) while its m2 is far smaller. That argues against a simple gain change, but the pre-MPTP m2 values (medians 4.6–10.3 units) are still near the noise.
- **New observation.** Venus perturbations come at a near-fixed 1.696 s after the centre target appears (5–95th percentile 1.696–1.732 s, cell 8). The paper says 1–2 s at random after the target is captured, which would also add a variable reaction time. The near-fixed delay suggests `center_target_appearance_time` may be reconstructed from the onset. The analog channels and spikes do line up with the onset (cell 14), so the tested claims are not affected. The Leu timing argument in cell 20 does rely on that 1.7 s. The Leu outcome stays blocked either way, because no Leu trial marks an onset.

**4. Critical findings**

No finding in the attempt record is rated `critical`. For information: finding 3 (torque command levels) is rated `minor`. I would rate it `major`. It changes the kinematic and EMG comparisons, and it cannot be worked around, since the two states barely overlap in pulse size. It is not critical, because it is evident from the command values and from the ElbowTorque description.
