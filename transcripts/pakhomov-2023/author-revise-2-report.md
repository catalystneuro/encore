Nothing in the record has changed outcome. Two outcomes now carry a proposed change to blocked (`methods_underspecified`) for a third verification round. The entry re-ran cleanly with `python tools/entry.py all entries/pakhomov-2023`: the check found 0 errors and the notebook ran in 16.5 minutes with a 7.2 GB memory peak. Every conclusion matches the new numbers.

**Proposed outcome changes**
- **The verifier's main point was correct.** The helper's set of "supported" readings, which decides a test when the readings disagree, fixed both diagonals for Figs. 6 to 9. The claims file says the paper does not state the diagonals there. Both diagonals are now fixed for Fig. 5 only, whose legend gives them, and the diagonal is varied for Figs. 6 to 9.
- **fig6-peak-narrower:** stays reproduced, with blocked proposed. The notebook now prints the width by diagonal. Of the 6 supported readings, the half-height width falls from 1Px4 to 5Px4 to 10Px4 in 4. On the d1 diagonal alone, 5Px4 is wider than 1Px4 under both ROI counts, which is the partial outcome. 10Px4 is narrower than 1Px4 in all six.
- **fig7cd-holds-for-large-array:** stays reproduced, with blocked proposed. 11 of the 12 supported readings find no pair of voltages differing. One, on d1, finds a pair at p = 0.037, and every reading where a pair differs is on d1.
- **Checked, no effect:**
  - fig7b stays blocked; now 1 of 12 supported readings finds no pair differing.
  - fig9c stays not reproduced; the paired test fails in all 12 supported readings.
  - fig6a stays partially reproduced; the peak test fails in all 6 supported readings.
  - fig5b is unchanged.

**Added or corrected**
- fig6a now has `assumed: true` and a deviation stating how the gap in its criterion is read.
- fig7b's notes and result say that with raw intensity, no pair of voltages differs in only 2% of readings.
- Text the verifier found wrong:
  - The round-1 responses on fig6a and fig9c are corrected.
  - The fig9c notes and the fig9c question in `questions/pakhomov-2023.yaml` are corrected the same way.
  - The Summary no longer concludes that the paper's a.u. scale differs. It gives both ranges (154 to 418 a.u. with background subtracted, which overlaps the paper's 215 to 235) and says the question is with a reader.
  - The README says 17 files hold a second channel.
  - The cell 19 panel titles are no longer hidden.
- The notebook's methods text now calls w1, the centre ROI choice and the paired test standard choices or assumptions, not readings from the paper.
- The question to the paper's authors (the `methods_unavailable` finding) now also asks which diagonals were measured for Figs. 6 to 9.
- Round 2 is recorded under `verifications` with the verifier's reasons and my responses.
  - For fig7cd I recorded `agrees: false`, because the verifier agreed "only partly", and gave no outcome, because it named none firmly.

**Not done**
- No new questions for a reader: the round-2 report named no new place where the claims file misreads the paper.
- Still open, as the verifier said, with no bearing on a conclusion:
  - the trough bias
  - flat-field tiling
  - values shown only in the figures, which could not be compared because there is no PDF

Nothing is committed.
