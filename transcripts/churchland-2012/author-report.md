I've finished the blind repeat attempt on churchland-2012: 16 claims tested, 6 blocked. The entry is in `entries/churchland-2012/`, the record is `attempts/churchland-2012-02.yaml`, and the handover is in `executed/churchland-2012/handover/`. `entry.py all` passes with 0 errors and the notebook runs in 594 s. I did not come across any earlier attempt.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| array-dataset-composition | partially reproduced (108 conditions each; 192 units each, against 146 and 218) |
| fig3ef-same-direction | reproduced (95.4% and 99.1% of conditions counter-clockwise) |
| fig3-independent-of-curvature | partially reproduced, assumed (J-array clockwise reaches 88.2%, threshold 90%) |
| fig3-phase-from-prep-state | partially reproduced (R2 0.568 and 0.676; J-array falls below its shuffle median of 0.686) |
| var-captured-jpc-plane | not reproduced, assumed (14.9% and 22.9%, against 28%) |
| pc23-variance | not reproduced, assumed (mean 23.8%, against 29%) |
| suppfig4-j-array-planes | not reproduced (13.3, 13.3 and 12.2%; 38.8% together; top six PCs 51.9%) |
| suppfig4-planes-range | partially reproduced (N-array 47.7%, J-array 38.8%) |
| fig6a-angle-peak | reproduced (peaks at 0.53 pi and 0.64 pi) |
| fig6b-skew-fit | reproduced (6-D ratios 0.918 and 0.909) |
| rotation-frequency | reproduced, assumed (1.34 and 1.40 Hz) |
| suppfig3-shuffle-controls | partially reproduced, assumed (all three shuffles pass in J-array, only shuffle 1 in N-array) |
| suppfig5-areas-variance | not reproduced (21.6, 20.2, 17.7 and 27.1%) |
| suppfig5-m1-faster | reproduced |
| fig6-velocity-model | not reproduced, assumed (fit is poor as claimed, but the angle peaks at 0.42 pi and 0.64 pi) |
| fig6-complex-kinematic-model | partially reproduced, assumed, seed sensitive |
| fig1, fig2, fig3abcd, fig4, fig5, fig6cd | blocked, data_missing |

**2. What was found**

The dataset:
- The Units tables hold unsorted threshold crossings, one per electrode (192 per session), not the paper's sorted isolations. The files say this. Rated major.
- Only the paper's two array sessions are in it, plus eight further array sessions. sub-Nitschke ses-20100910 matches the "N-9-10-2010" session of Supplementary Figure 5. Rated major.
- Two sessions not used by the paper, ses-20100920 and ses-20100922, have no `maze_condition` or `correct_reach` columns. Rated major.
- There are two movement-onset columns, 25 to 52 ms apart, with no note saying which one the paper used. Rated minor.
- Checks that passed: no recording is deposited twice. Hand units and alignment are consistent. Both arrays share the trial clock, with no drift over the session. A constant M1 lag of about 25 ms in N-array cannot be told apart from a genuinely later M1 response.

Assumptions:
- The movement onset is `offline_move_onset_time`. The other column would change five outcomes.
- The firing-rate range for normalisation is taken over the analysed window. This changes nothing.
- For the two simulated models, the rates lead the hand by 100 ms, the preparatory term ends at movement onset, and the factors have uniform weights. With no lead, the velocity model would be reproduced.

Questions for the paper's authors: two `methods_unavailable` findings, one on the onset column and range window, one on the simulated-model details. I asked a reader no questions.

**3. Protocol points**
1. The protocol has no rule for a criterion whose literal reading passes a case it was not meant for. The complex-model angle peak of -0.97 pi counts as "below pi/4" but is a contraction, not rotation. I applied the criterion as written and said so in the notes.
2. The claims file names `simulate_population`, a helper from an earlier attempt that the blind checkout does not have. I wrote my own model from the Methods and gave it the same name.
3. The claims file's header refers to "the notebook" and to "clock resets of the 2010 file", both from the earlier attempt. I could not check either against that attempt, so I tested the clock myself.
4. The protocol says nothing on whether a claim that depends on another claim's shuffle runs should reuse them. I gave the phase claim its own shuffle-3 runs from its own seed and recorded this as a deviation.
5. The protocol says "the directory is empty", but `entries/churchland-2012` did not exist. I created it.

**4. Runtime and failures**
The run took about 1 h, from 23:12 to 00:12 UTC. The notebook takes 9.7 min with a peak of 3.5 GB. Nothing failed. My script that stripped extra bold from the markdown also damaged one code line (`** 2`); a diff against the development run caught it before the final run.
