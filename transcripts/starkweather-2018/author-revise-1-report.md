No outcome changed. The verifier agreed with all 32 (20 reproduced, 12 blocked as `data_missing`), and every conclusion still holds on the new numbers. The entry re-ran cleanly with `python tools/entry.py all` in 272 s with 0 check errors, and the handover is rebuilt. Round 1 is recorded under `verifications` in `attempts/starkweather-2018-01.yaml`, with the verifier's reason and my response for each claim. Nothing is committed.

**What I added or corrected, by report point:**
- **B1, fig7ijk ("abolishes" omission responses):** I added this to the new `questions/starkweather-2018.yaml` as a question for a reader, and the claim is unchanged. The notebook now prints the mean omission response under the timing impairment with its standard error and a test against zero.
  - Odor B: −0.073 (SE 0.014, p = 6.6e-6).
  - Odor C: −0.032 (p = 0.045).
  - These are 25 to 43% of the intact dips. The conclusion, the notes and the README now say the dips are reduced, not removed, so the claim passes the criterion as written. A stricter criterion would make it partially reproduced.
- **B3, fig5f-task2-significant-slopes-shift:** the conclusion and notes now say the outcome rests on subtracting baseline trial by trial, why that reading is used, and that the other two readings fail (p = 0.239).
- **B5, the two blocked ANOVAs:** the parts that don't need the free-water response now run as a deviation that decides no outcome.
  - Interaction terms: none is significant on neuron means. All four are significant on single trials, including drug in task 1, which the paper finds not significant.
  - Unnormalized slopes: task p = 7.9e-6 and task 1 × drug p = 0.96, as in the paper. Task 2 × drug p = 0.066, where the paper has 0.032.
  - Both claims stay blocked.
- **B6 and C1, contents of `data.zip`:** the loader now returns the zip's member list and the data check prints it. It holds 173 members: the 172 neuron files and a `data/` directory entry. So no lick, free-water or mPFC file was being skipped.
- **C3, the 21 trials with no trial type:** the data check now gives their count per group (5, 1, 1 and 14) and reruns every Figure 4 ANOVA with them kept as odor A trials at the nearest delay. I also added this as a reading in every slope section. No conclusion changes; the largest shift is F 7.72 to 7.59.
- Other updates: the attempt record's findings, the README, and the runtime in `entry.yaml` (now about 5 minutes).

**What I did not do:**
- **C2, checking the model port against a MATLAB run:** neither MATLAB nor Octave is available here, so I couldn't produce a trace to compare. This is recorded in the responses for the three model claims.
- **B2, B4 and B7:** no change. The verifier marked them as not affecting a conclusion, and the notebook already reported them.
- **C4, per-mouse results:** these can't be computed, because the files have no subject IDs. This was already a finding.
