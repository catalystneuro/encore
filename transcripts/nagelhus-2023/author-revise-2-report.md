I've worked through every point in the round-2 report. The entry re-ran cleanly with `python tools/entry.py all` (all six notebooks pass, 0 errors), and `check` passes. I ran it once after the analysis changes and once more after the text edits, so the executed copy matches the final notebooks. The numbers came out identical to the previous run.

**Outcomes:** none changed, as round 2 requires.
- **figs4-object-traces:** this is the one outcome the verifier disagreed with, and I think they are right. It stays `partially_reproduced`, with `not_reproduced` written under `proposed` for a third round to settle. To back the proposal, notebook 02 now tests each reading's trace count against the paper's 18.3%. The counts are 0.33 to 0.54 of the paper's 218 cells, and every reading differs from 18.3% with p at most 1.4e-16. So this miss is far outside sampling error, unlike fig1c, and the criterion has no partial case.

**Corrections and additions:**
- **figs3f:** the p bound was miscopied. It now reads "at most 1.4e-6 (NO-NO')" in both the notebook 01 conclusion and the record.
- **figs8:** the notebook 05 conclusion and the record no longer say the trends hold at every size. They now say the trends hold across sizes but not step by step, and give the exceptions the verifier named plus the tetrode slopes.
- **figs7e:** notebook 06 now prints the range of c for both subset readings: 5 to 16 under (a) and 5 to 18 under (b). The conclusion and notes give both.
- **Field detection (point 2):** I added a question to `questions/ebrains-q0fg-1x8.yaml`. The Methods apply the contour function "iteratively" from the peak; the question asks whether that splits or stops fields before the 3×MAD level. The fig1d, fig1e and figs4 notes now say their failures may depend on the answer.
- **figs2d:** the notes now say the test removes 72 to 117 traces against the paper's 218 cells.
- **README:** it now mentions the proposed change.
- **Round 2 under `verifications`:** recorded for all 57 claims. The verifier agrees on 56 and disagrees on figs4. Each entry has the verifier's reason taken from the report and my response.

**Not done:**
- **Field detection variant:** I did not run a version of the iterative contour. The claims file and the paper's code do not give a splitting rule, so any rule I chose would be my own method; it waits on the new question.
- **Points 3 and 4 (figs6 occupancy decoder, CA3 341 against 313 cells):** these were already in the notes, so nothing changed.
- **Point 6 (figs7e wording, figs2c legend order):** both were asked in the questions file after round 1 and are still open. I did not change the claims file, since that is not the author's to edit.

Nothing is committed, as instructed.
