**Round 2 verifier report: Semenov et al. 2026 on DANDI:001526 (0.261006.1851)**

**1. Outcomes and assumptions**

The claims file has 30 claims. The attempt record has 30 outcomes: 1 reproduced, 2 partially reproduced, 2 not reproduced and 25 blocked.

| Claim | Record | Agree? | Assumption (`assumed`) |
|---|---|---|---|
| fig2cd-nonelectroporating-stable | not_reproduced | **Yes, changed from round 1.** The criterion is binary: "not reproduced when any does". Under the adopted reading 1 of 12 comparisons is at p=0.031 (cell 19). My round-1 "partial" had no clause to rest on. The result is weak: one uncorrected test out of 12. It disappears without subtraction, and also without c3 and c4. | Stated (`assumed: true`). The background reading and the choice of cells are both stated and reasonable. |
| fig2c-1000-within-set | reproduced | Yes, but fragile. It holds only with the background recording and window (b), p=0.094. It fails with the annulus (p=0.035), the floor, no subtraction, F0 from images 2–40, and windows (a) and (c), where p ≤ 0.008 (cell 23). | Stated. But the adopted reading was switched from the annulus to the background recording in the same round that the annulus stopped meeting this claim. The reason given (a cell-free recording was made with each cell) is plausible and was argued beforehand, but the switch should be read as a forking path. |
| fig2d-lasting-reduction | partially_reproduced | Yes. One gap in the criterion: under annulus with F0 from images 2–40, the anodic-pole mean is 18.7%, inside tolerance (cell 26). So the partial clause ("size outside the tolerance under every reading") is not literally met either. The "reproduced" clause also fails there, because a pre-exposure set has p=0.029. Partial is the sensible call, and the notes explain it. Separately, `evaluate()` (cell 17) labels any significant post-exposure set "partial", which is looser than the criterion. That affects only the 165-subset counts. | Stated and reasonable. |
| fig4d-short-pulses-same-limit | not_reproduced | Yes. Both poles' maxima are out of tolerance under every reading (34.9 and 34.0% at most). The two missing cells would each need |dF| above 100% to bring the mean into range, so the outcome does not actually rest on the assumptions. | `assumed: true` is harmless but not needed. |
| fig5b-eq2-sensitivity | partially_reproduced | Yes. The 100-fold value (11.87%) matches; the 10-fold value (1.33%) does not. The criterion has no partial clause, and the notes say so. | Not assumed. Correct. |
| The 25 blocked claims (data_missing) | blocked | Yes, as in round 1. | n/a |

**2. Sentences the printed outputs do not support**

Most sentences match the printed outputs. These do not:

- **The count of 8-cell subsets meeting all three claims together.**
  - Cell 38 (Summary) says "the three are met together in 1 (background recording) and 6 (annulus)".
  - The record's second methods_unavailable finding says "met together in 1 (background recording reading)".
  - Cell 17 prints `all_three_reproduced` = **2** for the background recording and 6 for the annulus.
- **The count of 8-cell subsets meeting fig2d.**
  - Cell 27 says "in 2 of the 165 choices of 8 cells under the background recording". The fig2d notes and the round-1 response say the same.
  - Cell 17 prints `fig2d_reproduced` = **3**.
- **Cell 27 and the fig2d notes, figures for the adopted reading.** They say:
  - "p = 0.017, 0.018 and 0.019" and "23.8% … (p = 0.094)"; cells 17 and 26 print 0.017, 0.018, **0.018**, **0.092**.
  - "49.5% and 43.1%, p = 0.017 and 0.026"; cell 26 prints **0.025**.
  - "32.4% and 33.3%, p = 0.051 and 0.109"; cell 26 prints **33.4**, **0.050**, **0.107**.
  - "set reductions of 2.3 to 30.4%"; cell 26 prints **2.2**, 12.3, 30.4, 29.9.
- **Cell 24 and the fig2c notes.** They say "With per-cell pole angles it is met under the background recording (p = 0.080), not under the annulus (p = 0.028)". Cell 17 prints **0.089** and **0.033**. The direction is the same, so the conclusion stands.
- **Cell 21 and the fig2cd notes.** These are rounding slips:
  - The annulus p is given as 0.045; cell 19 prints **0.044**.
  - The within-set change is given as "at most 1.15%"; cell 19 prints a largest change of **1.14%**.
  - The smallest p without c3 and c4 is given as 0.066; cell 17 prints 0.0667, which rounds to 0.067.
- **The background deviation in the record.** It says the paper's 1000 V/cm values are "about 2.5 times the unsubtracted ones". Cell 23 prints 40/13.3 = 3.0 and 26.6/8.5 = 3.1 for window (b), and 2.4 and 3.0 for window (a). "About 2.5" really compares the subtracted and unsubtracted readings with each other, not the paper's values with the unsubtracted ones.

Several of these numbers look as if they come from an earlier run. None of them changes an outcome.

I checked everything else against the outputs and it holds. That includes the README, the rest of the Summary, cells 31, 34 and 37, the fig4d and fig5b notes, the fig3 exploratory slope, and the background levels (52–54%, 65–66 counts, 0.97–1.08). The overlay statements about c3 and c4 in the record also match the cell 10 figure, which I viewed.

**Do the round-1 reasons appear in my own words?** Yes, for all 30 claims. My problem B4 is folded into the fig2d reason and B5 into the fig4d reason. Problems B1–B3 have no `reason` field of their own; they are answered in the authors' responses. That is acceptable.

**Claims file.** My round-1 point B8 still stands but has no effect: the fig2d legend says "≤20%" while the tolerance is a symmetric 18–22%. I found no new misreading of the paper.

**3. Round-1 points**

Resolved:
- **B1 (cell selection):** criteria are now applied without c4, without c3 and c4, without all four protocol-breaking cells, and across all 165 choices of 8.
- **B2 (c4):** the trace was on internal staining and has been re-traced, and overlays are shown.
- **B3 (background):** the Summary now says no single reading gives all three Fig. 2C/D results.
- **B4 (fig2d pass):** the single anodic pass is gone (17.4%).
- **B6 (pole angle):** a per-cell angle variant is added.
- **B7 (trace spacing):** stated as a deviation.
- From my round-1 "could not check" list: the overlays and the cell-subset reruns are done.

Still open, and bearing on a conclusion:
- **The fig2cd, fig2c and fig2d outcomes rest on two unknowns: the background reading and which 8 cells the paper used.** Without c3 and c4, all three claims are met under the background recording and the annulus. With all 11 cells, no reading reproduces fig2cd and fig2c together. The record states all of this.
- **The adopted reading was changed after the results were seen** (fig2c). The record should say this plainly as well as giving the reason.
- **Camera offset.** No dark frame is given, and the darkest pixels sit at about 202–208 counts. If that floor is the true offset, fig2c fails (start 24.0%) and fig2cd fails (p=0.038).
- **Weak first-set responders.** c4, c8 and c10 have first 150 V/cm cathodic sets of only 3.4–3.8%, against later means of 5.0–15.3% (cell 20). c4 also has the weakest cosine amplitude (4.28). These cells shape the fig2cd and fig2d comparisons against the first set, and whether the nearest-centre choice picked the right responding cells is still not established.

Still open, not bearing on a conclusion:
- **B5 (Fig. 4D labels):** the record now says they were read from page 6 of the PDF. I still cannot render the PDF here (no poppler), so I could not check them. No outcome depends on them.
