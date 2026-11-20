# Round 2 verification report: pakhomov-2023-05

## 1. Outcomes

The claims file has 24 claims, and the attempt record has 24 outcomes: 10 blocked, 5 not_reproduced, 6 partially_reproduced and 3 reproduced. Two of the reproduced outcomes are marked `assumed: true`.

| Claim | Outcome | Agree? | Comment |
|---|---|---|---|
| fig3-field-simulation, four fig4 claims, fig8-cancellation-predicts-targeting | blocked, data_missing | Yes | None of the datasets holds the field maps or the single-cell time lapse (cell 15). |
| fig5a-trains-stronger | not_reproduced | Yes | Trains are not above packets at the e3 end in any reading (0/16), and the criterion has no partial outcome. My round-1 objection is met by cell 19 (see section 3). |
| fig5a-packet-center-enhanced | partially_reproduced | Yes | Reading (a) holds in 16/16 readings. "e1 end above centre" fails in 0/16. |
| fig5b-rotation-center-peak | blocked, methods_underspecified | Yes | The two supported readings differ only in O1: void p = 0.055 with one count, 0.020 with the other (cell 25). The claim would also be blocked with O8 varied, because 98% of readings hold unpaired and 71% hold paired. |
| fig5c-normalized-contrast | blocked | Yes | The claims file has `depends_on: fig5b`. Its own test holds in 32/32 readings, and the record says so. |
| fig6a-more-packets-more-uptake | partially_reproduced | Yes, with a note | The criterion's partial rule does not cover "rise at all three places, peak test fails". Reading that case as partial is an interpretation the outcome rests on. The notes state it and send it to a reader, but the outcome has no `assumed: true`. It should. |
| fig6b-peak-relative-to-periphery | partially_reproduced | Yes | 6 of 576 readings meet the partial rule. It is a thin pass. |
| fig6-trough-half-of-center | partially_reproduced | Yes | 114 of 288 readings meet the partial rule. |
| fig6-peak-narrower (assumed) | reproduced | Yes, conditionally | The assumption (half-height width) is stated and reasonable. It also rests on cc.SUPPORTED fixing O2 = a, which I question below. The notebook does not print the width result by diagonal, so I cannot tell whether the one-diagonal readings agree. |
| fig7a-amplitude-scales-uptake | partially_reproduced | Yes | 10 of 288 readings have one ratio within 10%. It meets the letter of the rule only. |
| fig7b-targeting-independent-of-amplitude | blocked, methods_underspecified | Yes | This changes my round-1 view. The claims-file rule lets the author block when the best-supported readings disagree, and they do: 1 of 4 supported readings finds no pair different. The record should still say how lopsided the evidence is: with raw intensity only 2% of readings find no pair differing (cell 47). |
| fig7cd-holds-for-large-array (assumed) | reproduced | Only partly | The assumption is stated, and the low power is stated. But "supported" fixes O2 = a, both diagonals, on the basis of the Fig. 5B legend. The claims file says that for Figs. 6 to 9 "the paper does not say". The only readings where a pair differs are on the d1 diagonal (cell 50, by o2: d1 max 1 pair). So the agreement among the supported readings depends on a basis the claims file does not give. |
| discussion-independent-of-array-size | blocked | Yes | It depends on fig7b (`depends_on`). |
| fig8a-equal-center-uptake, fig8a-more-uptake-near-electrodes, fig8b-packet2-best-targeting | not_reproduced | Yes | The values are in range in 0/576 readings. The labels are confirmed by the session descriptions (cell 64). |
| fig9a-gap-reduces-periphery-more | partially_reproduced | Yes | At most 4 of 6 ratios are within 10%. The pattern holds in 88% of readings. |
| fig9b-gap-boosts-targeting | reproduced | Yes | The 2-mm value is 541% in the main reading, inside the tolerance and the largest. The claims file's "any reading" rule for expected values applies. |
| fig9c-restricted-to-center | not_reproduced | Yes | The "highest point" part fails in 0/96 readings, so the outcome does not depend on the paired-test assumption (cell 73). |

**On cc.SUPPORTED.** The notebook calls these readings ones "with a basis in the paper or the claims file". For several, the basis is a convention:
- w1: the claims file calls it "a standard choice", not from the paper.
- O3 = a and O8 = paired: neither has a basis in the paper.
- O2 = a for Figs. 6 to 9: the claims file says the paper is silent there.

The w1, O3 and O8 choices are reasonable assumptions and are stated in the deviations. The O2 = a choice outside Fig. 5 misreads its own cited basis. It matters for fig7cd, and possibly for fig6-peak-narrower.

## 2. Text against outputs

Nearly every number in the Result cells, the Summary, the README and the outcome notes matches the printed output. I checked them all. The exceptions:

- **Attempt record, fig6a response:** "With the paired test the peak test fails for every treatment in all readings." Cell 31 shows the 10Px4 peak holds by the paired test in 83% of readings. Only the joint test, all three treatments together, fails in all readings. The notes elsewhere state this correctly.
- **Attempt record, fig9c response:** "with the paired test the centre-above-periphery part also fails at 2 mm." That is true only in the main reading (p = 0.051). Cell 73 shows `c>end 2 paired` holds in 92% of readings.
- **Summary, cell 75:** "the paper's a.u. values are smaller … so its scale or background differs." This inference goes beyond the numbers. With background subtracted, the Fig. 8 centres are 154 to 418 a.u. (cell 56), which overlaps the paper's 215 to 235. A real difference in the data is not ruled out.
- **README:** "Each file holds one dish, a stitched image of YO-PRO-1 uptake." 17 files also hold a second channel (cell 15 and the findings). This is minor.
- **Cell 19 figure:** the e3 panel titles are hidden behind the top row. This is cosmetic.

The verifications block gives my round-1 reasons in my own words, and accurately. For fig5a and fig9a it adds the related points from my problem list and my section C, which is fair.

## 3. Status of round-1 points

**Resolved:**
1. **e3 coverage:** Cell 19 shows every e3 ROI lies inside the image, at 2.0 to 5.0 times the cell-free level, with no pixel at or below that level. The crops show a uniformly dim monolayer. The remaining limit, that YO-PRO-1 cannot tell unaffected cells from bare glass, is stated.
3. **Group sizes:** they are printed, the 2.4 kV leave-one-out is run, and the fig7cd power calculation is shown.
4. **Protocol labels:** they are cited from the session descriptions.
5. **Paired tests:** these are now the default.
6. **ANOVA:** it now uses one value per dish.
8. **LOESS:** it is now fitted on the mirrored profile (`lowess_profile`).
9. **O3 (b):** it now uses only the half-diagonals in use (`centre_value`).

**Section C, needle-mark squares:** cell 9 shows the needle marks at the upper needles. Where the footprint fit is off by 1.2 to 1.6 mm (dishes 06, 09, 14), it is the footprint square that is visibly wrong, not the needle-mark square.

**Partly resolved:**
2. **Choosing among readings:** the PRIMARY-by-convention choice is gone. The replacement, cc.SUPPORTED, fixes O2 = a for Figs. 6 to 9 on a basis the claims file says does not exist there.

**Still open, bearing on a conclusion:**
- **fig7cd:** if O2 is treated as having no basis outside Fig. 5, the supported readings may disagree, because the readings where a pair differs are all on d1. The claim could then be blocked rather than reproduced. The same check is needed for fig6-peak-narrower, whose width result is not printed by diagonal.
- **fig6a:** the partial outcome rests on an interpretation of a gap in the criterion and should carry `assumed: true`.

**Still open, not bearing on a conclusion:**
- Trough bias (problem 7).
- Flat-field tiling was not quantified.
- Figure-only values were not compared, because no PDF was supplied.
