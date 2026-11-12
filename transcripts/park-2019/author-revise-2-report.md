I've worked through every point in the round-2 report. The entry re-ran cleanly with `python tools/entry.py all entries/park-2019`: 0 errors, the notebook passes in 187 s, and `check` passes. Nothing is committed.

**Outcomes.** None changed, as round 2 requires. I proposed one change, for a third verification round to review:
- **figs3-no-head-direction-bias:** it stays `reproduced`, with a proposed change to `not_reproduced`. The verifier was right that my reason for taking n as the sum of the weights does not hold. The weights are rescaled mean ΔIdir values, not frequencies, so their sum depends on the scaling. The cell now prints those sums: 9.2 to 26.8 across the 14 tests, against 36 bins. Taking n as the number of bins is better supported, since that is the reading the claims file checks against the paper. Under it, 1121R157 in the room frame gives p = 0.0134, and the criterion has no partial branch. I withdrew the Zar justification and updated the notes, the conclusion, the summary and the README row to say a change is proposed.

**Corrections to text the printed numbers did not support:**
- **fig5:** the Rayleigh p range now reads 2.17e-20 to 0.00459 at 660 ms, in the notebook and the record.
- **fig4:** I removed the claim that the room-arena gap "follows the passive rotation". The text now says the tracker samples explain the direction of the shift but not the size of the gap. It gives the verifier's three numbers (about three times larger, per-pair r = -0.01, the gap shrinks in the clean pairs) and says the cause of the gap's size is not established.
- **fig4c:** the occupancy and after-side variants are now described separately, with their actual patterns (p = 0.0028 at 60 s, and p = 0.0167 at 20 s).
- **Round-1 fig4c reason:** the verifier asked for one sentence to be amended. The amendment is added in brackets, marked as the verifier's.
- **README:** the run time now says about three minutes (the notebook prints 3.0 min).

**New output.** I added a data-check cell that prints the numbers behind the file problems, which no output showed before. Two of the earlier statements turned out to be wrong, so I corrected them in the notebook and in the record's findings:
- The rotating-frame mismatch is 6.9 to 13.5 px at the best constant lag, not 7 to 13.
- The arena-frame track of 1211R039 agrees with its tracker file (0.49 px, against 0.23 and 0.36 px in a good session) but does not match it exactly. Its room-frame track agrees with the room tracker file of 1212R039 (0.32 px).

The 2919 spikes for 1024R157 P9C1 and the 614 off-line spikes for 1017R035 P11C2 are now printed and match what the text said.

**Recorded.** Round 2 is under `verifications` with all 22 claims. For each, it records whether the verifier agreed, the outcome it would give, its reason in its own words, and what I changed in reply. The record has no per-claim place for the two points that bear on no claim (the data-check numbers and the README run time), so I noted them and my replies in the round's `reviewed` field.

**Not done.** I added no new questions for a reader: this report found no new misreading of the paper, and the fig5 question is still open. The fragility points for fig2, figs2, fig1c-directionality and fig4 were already disclosed, and the verifier accepted them, so I left them unchanged.
