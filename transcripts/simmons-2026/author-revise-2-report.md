I've worked through all of the verifier's round-2 points. No outcome changed and none is proposed. The entry was re-run with `python tools/entry.py all entries/simmons-2026`: the checks give 0 errors, the notebook passes in 11 min, and the text matches the new outputs. Nothing is committed.

**Outcomes**
- All 39 stay as the verifier agreed: 13 reproduced, 2 partially reproduced, 4 not reproduced, 20 blocked.
- fig4b no longer carries the `assumed` flag, as the verifier suggested. Under reading a of M1, P is 0.11 to 0.27 at every threshold, so the absence of an effect holds everywhere. The one significant result (reading b at threshold 12, P = 0.036) comes from spikes of cell 6887-2022-07-14-57 that are missed at that threshold. Two outcomes are now marked assumed: fig3b and fig7d.

**Added**
- **Cell 8979-2025-05-27-164 (round-1 point 2, still open):** the notebook now shows its time course. Its spikes shrink into the noise during SNAP-5114 (from 36 to 7–8 noise units by minute 28) while its rate falls from 17 to 2 Hz. I treat it as a failed recording and ran both fig7f claims without it:
  - fig7f decrease: P = 0.0099, a fall of 10.5%. At threshold 12 the fall is not significant (P = 0.076).
  - fig7f occlusion: Welch P ≥ 0.62.
  - Neither outcome changes.
- **Cell 8945-2025-04-16-144 (point 7, drug application time):** the notes say gabazine was applied during the file used as its control. Its rate in that file is 23.5 Hz before the end of the noted baseline window and 23.3 Hz after, so the gabazine had no effect yet. Without the cell, fig3b gives P = 0.048 under reading b, essentially the same as with it.
- **fig3b:** a deviation now names the assumption. With all 49 cells, P < 0.05 holds only at thresholds 6 and 8 under reading b of M1.

**Corrected text**
- fig7d: the reading-a increase (25.2%) is just under the tolerance, not inside it.
- fig3b:
  - The "every reading and set of cells" sentence is replaced by the actual sizes.
  - The gap-free variant is described correctly: all 49 cells with only the gap-free files windowed (P = 0.065); the gap-free cells alone give P = 0.20.
- fig7f: 14 gap-free and 5 episodic cells (it said 10 and 9).
- fig5d: 31 episodic cells (it said 32).
- fig4a: the wording of the clean-sweep limits.
- fig2c: the per-sweep variant is P = 0.11 to 0.15 (0.11 at threshold 6).
- README: fifteen claims are blocked on missing data, with fig6c counted separately as blocked through its dependency.
- fig7e: the round-1 response now says 8797-2025-03-12-123 loses its spikes 6 min into CNO (it had said "stops firing"); the notebook shows them coming back at minute 26.
- The finding about failed recordings now names 8979 as well.

**Record**
- Round 2 is added under `verifications`: all 39 claims are recorded as agreed, with the verifier's reasons in its own words and my responses.
- The verifier again found no place where the claims file misreads the paper, so I added no question to `questions/simmons-2026.yaml`.

**Not done**
- 8979 is not added to the main set of excluded recordings (`ok_cells`), so the "seven failed recordings" variants elsewhere are unchanged. It is excluded only in variants for the two fig7f claims, the only ones it belongs to.
