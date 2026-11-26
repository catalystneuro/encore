I worked through every point in the round-1 report and re-ran the entry with `python tools/entry.py all entries/pasquereau-2013`. It passes with 0 errors and the notebook runs in about 11 minutes. All conclusions match the new numbers. Nothing is committed.

**Outcomes.** None changed. The only disagreement is on kinematic-latency-unchanged: the verifier would block it because the measure moves onsets early, and I kept not_reproduced and recorded the disagreement. The new outputs show the verifier is right that the forwards-backwards filter moves onsets early: 6.7% of post-MPTP onsets land at 0 ms, against 0.1% before. But every way of measuring the onset still finds shorter latencies after MPTP:
- requiring the velocity to stay below threshold for the 20 ms before onset: F = 596.5
- a causal 25 Hz filter: F = 422.5
- both again at matched torque commands: F = 214.3 and 146.2
- the unfiltered velocity also rises earlier after MPTP.

The artifact narrows the difference but does not create it.

**Added or corrected, by point in the report:**
- **B1, response detection.** The 15 blocked claims are now also shown under the `trial_sd` reading, whose false-positive rate is 0.013. They stay blocked: that reading is not the claims file's detection. It also calls only 20.0% and 18.5% of M1 cells torque-related (75% and 68% expected) and finds only increases. Whether the claims file misreads the Methods' "2-tailed t-test" is now a question for a reader in the new file `questions/pasquereau-2013.yaml`. I did not change the claim.
- **B2, movement onset.** Added the fraction of onsets at 0 ms, the velocity at torque onset, the two onset variants above and the unfiltered velocity. The variants are documented in the `pasq.py` docstring.
- **B3, EMG and torque size.** All four EMG claims were re-run on perturbations with matched command pulses (60 to 250 units). Their outcomes are the same: m2 is larger after MPTP in every channel, KS p from 7.5e-08 to 2.2e-15. Pre-MPTP m2 > m1 rises to 94.9% there, which I note but which does not decide the claim. I also added grand-average traces and the background level and SD for each channel and state. These show the background differs between states: the triceps longus 2 baseline SD is 2.98 units before MPTP and 19.58 after.
- **B4, angle scale.** The scale is correct. Voluntary movements to 20 degree targets measure 19.87 and 18.13 degrees, exactly 1.000 times `derived_movement_amplitude`. The file's `ElbowVelocity` series is 1.028 times the velocity I compute from the angle. The small, faster displacements are therefore in the data, not a scale error.
- **B5, repeated files.** 12 files each combine two lab source files. No trial repeats between the two, and no source file appears in two NWB files. Two other ways of counting cells give the same 115 and 157, so the gap from the claims file's 112 and 159 remains unexplained. It is within tolerance.
- **B6, Bonferroni–Holm.** Noted under antidromic-latency; the outcome is the same.
- **B7, monkey L torque command.** The command now has per-file counts and a plot. In the file with the most jumps, the large excursions fall at the centre target's appearance in every trial and near voluntary movement onsets. None falls 1 to 2.5 s after the centre target, where perturbations would be. I rewrote finding 1 to say this.
- **Record.** Added the round-1 `verifications` block covering all 28 claims, updated notes and deviations, and added to findings 2 and 4. The README, notebook header and summary are updated, `requirements.in` now includes matplotlib (re-locked), and `runtime_minutes` is now 11.

**Not done.** No finding is rated `critical`, so there were no finding reviews to record. I could not resolve the 112 vs 115 cell-count gap, because the claims file's data-check selection is not available.
