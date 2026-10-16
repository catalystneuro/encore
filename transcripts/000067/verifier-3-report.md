**Round 3 verifier report: Fujisawa et al. 2008 (doi:10.1038/nn.2134) on DANDI 000067 @ 0.250624.0419**

The claims file has 16 claims and the attempt record has 16 outcomes. Only one outcome has a proposed change: traj-diverge. I did not download any paper text this round, so nothing new is under `paper/`.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| traj-diverge | blocked (data_missing) | Yes | — | See below (cells 34, 35, 36). |

**The numbers come from the data (cell 35).** Cell 35 takes the per-side mean x1 curves from cell 34. For each session it finds where x1 reaches its minimum, measures the gap between sides at position 0.3, and measures how far x1 falls from 0 to 0.3. I recomputed every summary figure from the printed table:
- Divergence point minus x1 minimum, over the 8 sessions with a divergence point, gives -0.45, -0.03, -0.02, -0.01, -0.01, 0.00, 0.08 and 0.08. The median is -0.01, and every session except GG.149 is within 0.08.
- The x1 minimum lies between 0.47 and 0.53 in every session.
- The left-right gap at 0.3 has a median of 2.808 px over 9 sessions, matching the stated 2.8 px.
- The fall in x1 from 0 to 0.3 has a median of 243.8 px over 8 sessions, matching the stated 244 px. EE.088 has no value in its first bin.

The record's reason, the notes, the cell 36 markdown and the README row all match these outputs.

**The choice behind it was not made to reach a result.** Comparing the divergence point with the x1 minimum is a direct check of what x1 measures. It is the comparison I asked for in round 2. It also gives up the more favourable partial rating, not gains one. The curves in cell 34 show both sides falling about linearly to a minimum near 0.5 and then rising. A difference that starts at that turn marks where the path reverses in x. It does not show where the two paths separate sideways. The 2.8 px gap at 0.3 is about 1% of the roughly 244 px x1 travels by then.

**How the criterion applies.** As written, the criterion's blocked rule only fires when x1 shows no side difference over 0.5 to 1 in at least half the sessions. In cell 34, x1 differs there in 9 of 9 sessions, so the written criterion gives partially reproduced, and the record says so. The proposal does not misapply the criterion. It shows that the criterion's premise is false: the criterion assumes that a side difference in x1 means x1 carries the lateral separation. It also shows that "partially reproduced when above 0.33" would rate any x1 result past the turn as partial support, so the rating says nothing about the claim. The claim is about where left and right trajectories separate, and that would show along the y coordinate. The dandiset has no y coordinate: the second LED series is zero throughout (cell 33). Blocked (data_missing) is the correct outcome. This is the conclusion I reached independently in round 2.

The first half of the claim, that the paths overlap in the central arm, cannot be judged either. The 5 to 17 px x1 differences in 0 to 0.3 seen in 5 sessions could come from small offsets in path or camera position. They do not stand in for the two-dimensional comparison.
