## Round 3 verifier report: proposed changes of outcome

I took the claims and outcomes from `pasquereau-2013.yaml` and `pasquereau-2013-03.yaml`. The attempt record has `proposed` on four outcomes: kinematic-latency-unchanged, emg-duration-longer, emg-onset-unchanged and emg-m1-weak. I agree with none of the four and would keep every outcome as verified in round 2. Cell indices below refer to the re-executed notebook.

| Claim | Proposed outcome | Agree | My outcome | Reason |
|---|---|---|---|---|
| kinematic-latency-unchanged | reproduced | No | not_reproduced (unchanged) | The criterion is applied to the session means over all perturbations: MPTP F = 709.5, p = 1.5e-102 (cell 68). The proposal decides instead on an equal-pulse subset the claims file does not define, from cell 65. That subset has 4 pre-MPTP sessions per direction at 175 to 185 units and 15 post-MPTP flexion sessions at 85 to 95 units, which is little power for an absence claim. The subset results also depend on the filter. With the claims file's onset, p = 0.16 and 0.98. With the causal filter, p = 0.0027 at 85 to 95 units, which by the criterion is not reproduced. In round 2 the author showed the claims file's onset is the measure that suffers the filter artifact. The numbers in cell 65 derive from the data as stated. |
| emg-duration-longer | not_reproduced | No | partially_reproduced (unchanged) | As written, the criterion is met at partial over all channel-sessions: 22.2 against 51.5 ms, KS p = 5.2e-33, with both means outside tolerance (cell 78). The proposal rests on the subsets in cell 75. These have 14 post-MPTP channel-sessions at 85 to 95 units and 5 pre-MPTP at 175 to 185 units. A non-significant result on so few cannot overturn the comparison the criterion specifies. The cell 75 numbers (32.4 against 24.1 ms, p = 0.32; 27.0 against 46.7 ms, p = 0.087) match the record. |
| emg-onset-unchanged | reproduced | No | not_reproduced (unchanged) | The criterion compares all the responses used for emg-duration-longer and gives 44.2 against 25.0 ms, KS p = 5.8e-22 (cell 80), so it is not reproduced. The proposal's "no difference" comes from the cell 75 subsets. At 175 to 185 units the onset is 12.5 ms earlier after MPTP with p = 0.057 on 5 pre-MPTP channel-sessions. That is a low-powered near-miss in the direction of the effect, not evidence of absence. At 85 to 95 units, 14 post-MPTP channel-sessions enter. |
| emg-m1-weak | reproduced | No | partially_reproduced (unchanged) | Over all channel-sessions, pre-MPTP m2 exceeds m1 in 151 of 204 (74.0%) under the main rule and in 74.3% under the other rule, short of the 75% the criterion asks (cell 82). The proposal says the shortfall comes from small-pulse sessions. Those are the majority of pre-MPTP sessions: 105 of 151 have a median pulse of 30 to 60 units (cell 21), and they belong to the population the claims file fixes. Leaving them out departs from the criterion. The subsets meet it on 5 pre-MPTP channel-sessions at 175 to 185 units (80.0%, which is 4 of 5) and 14 post-MPTP at 85 to 95 units (cell 75). |

### Common grounds

1. **Not tuned to the result.** The equal-pulse windows (85 to 95 and 175 to 185 units) sit at the modes of the command distribution (cell 21). The four proposals also go in both directions, one of them downward. So I do not read the subset choice as made to reach a result. The same rule also leaves kinematics-slower and emg-m2-larger unchanged.

2. **Not the criterion as written.** Each of the four criteria specifies the comparison over the full set of sessions or channel-sessions for monkey V. Restricting to command levels is a new choice made in round 3, after the all-perturbation results were known. The notebook itself labels these variants "not deciding" (cells 63 and 73), and they should stay so.

3. **Where the pulse-size confound belongs.** The confound is real: the paper gives one 0.1 Nm pulse (Methods), while the post-MPTP command is about three to four times the pre-MPTP one (cell 21). It is recorded as finding 3, now rated major. It belongs in that finding and in the notes on each outcome. It should not change the outcomes. The equal-pulse subsets are also too unbalanced to decide claims of absence.

4. **Equal command may not mean equal torque.** Whether equal command units deliver equal torque in both states is not established. The paper's single 0.1 Nm pulse does not match either state's command values directly.

### The claims file

For these four claims I found no place where the claims file misreads the paper. Its criteria follow the paper's statements and tests (Results, "Behavioral effects of MPTP", paragraphs 2 and 3). The mismatch is between the paper's single torque and the dandiset's commands. That is a data finding, not a misreading.
