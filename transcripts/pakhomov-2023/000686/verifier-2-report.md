# Round 2 verifier report: 000686-pakhomov-2023-01

## 1. Outcomes

I took the counts from the claims file and the attempt record. There are 20 claims and 20 outcomes. 15 are blocked as `data_missing`, 3 are `not_reproduced` and 1 is blocked as `methods_underspecified`. No outcome carries `assumed: true`.

| Claim | Record | Agree? |
|---|---|---|
| fig3-field-simulation; the four Fig. 4 claims | blocked, data_missing | Yes |
| The 11 Fig. 6–9 claims | blocked, data_missing (was `other`) | Yes |
| fig5a-trains-stronger | not_reproduced | Yes. The e3 end fails in all 8 readings under all 6 ROI geometries (cell 12, p 0.268–0.858). The criterion's "outcome all readings give" rule is met. |
| fig5a-packet-center-enhanced | not_reproduced | Yes. "e1 end > centre" fails in 16 of 16 readings in every geometry (cell 15, p 0.0533–0.231), even though all 4 dishes go the claimed way. |
| fig5b-rotation-center-peak | not_reproduced | Yes, on condition that the paired test (O6) counts as a reading that must hold (see point 1 below). |
| fig5c-normalized-contrast | blocked, methods_underspecified (my round 1 gave not_reproduced) | Yes, with a caveat (point 2 below). |

**1. fig5b: whether O6 must hold.** The fig5b criterion says "under all readings of O1, O2 and O4". It cites O6 only for the test itself. The fig5a-packet criterion, by contrast, names "paired and unpaired" outright.
- With 3- or 5-step bands, every unpaired reading holds for both comparisons (cell 18). The only failure is the paired 1T × 40 test (p up to 0.0655–0.0904).
- The record's own finding says the paper does not state paired or unpaired.
- So with wider ROIs, fig5b rests on an open detail (the test type), just as fig5c rests on the ROI width. Yet one is `not_reproduced` and the other `methods_underspecified`.
- `not_reproduced` holds only if O6 is a reading that must hold. The record should say that this is its reading of the criterion. Under the other reading, fig5b should also be `methods_underspecified`.

**2. fig5c: ROI width.** ROI width is not one of the claims file's readings, and the 5C criterion has no `methods_underspecified` clause. Even so, the outcome flips with a detail the paper leaves open:
- 27/32 readings with 1-step ROIs, under both ROI ends (failures at p 0.0512–0.0824);
- 32/32 with 3-step ROIs;
- 31/32 (measured footprint) or 32/32 (needle end) with 5-step ROIs (cell 21).

I accept the block. However, the record says "no width has a better basis than another", which I find arguable. 224 ROIs over ±3.65 mm on two diagonals gives contiguous squares of about 65 µm, and that is the 1-step geometry, which gives not_reproduced. The record should state that this is the most direct reading. It should also note that fig5c `depends_on` fig5b, which is now `not_reproduced`.

**Assumptions.** These are all stated and reasonable:
- the O3 (b) per-dish test is now labelled as an assumption;
- footprint-median background changes no outcome;
- e1 is the top-right electrode under both readings (cell 7, 8/8 dishes);
- the trough is taken on the group mean, with a leave-one-out variant;
- O2 (b) is the joined e1 + e2 end, stated as a labelling choice.

## 2. Sentences the printed outputs do not support

Almost every number in cells 13, 16, 19 and 22, the Summary (cell 26), the README and the record matches the outputs. The exceptions:

- **Cell 19 and the record's fig5b notes:** "the 1T x 40 centre is below its periphery … (4884 to 5781 against 10596 to 10989 a.u.)". The centre range covers raw values only, while the periphery range includes the background-subtracted values. With background, the centre goes down to 4570 (cell 18).
- **Cell 13:** "the e1-end difference is significant in all 8 readings (p = 0.000252 to 0.0244)". Cell 12 prints the e1-end p only for the raw reading of each geometry. The count of 8 is supported by `ok e1`, but the p range is raw-only. The record correctly says "raw p".
- **Cell 26 and the record's findings:** "The subject age is P1D" and "the assets summary gives 36 subjects". No printed output shows either. Cell 3 prints the species, the subject-id uniqueness and the counts, but not the age or the archive summary.
- **README:** "The data of Figs. 6 to 9 are in four other dandisets". The README states this flatly, but those dandisets were not opened. Elsewhere, including the README's own table, it is "apparently".
- **Record, fig5a-trains notes:** "the e3 footprint lies in the unlabelled dark half … so its position cannot be checked by eye". In the cell 5 figure, a faint dark disc is visible under the e3 circle in all four train dishes. The rest of that sentence, "near 1000 a.u. in every dish", is supported: per-dish values are 764–1391 (cell 12).
- **Record finding:** "not with the single centre ROI (p = 0.065 to 0.114)". The lowest value printed is 0.0643 (cell 18). This is a trivial rounding difference.
- **Cell 19, "clusters of round spots of cell size":** this is consistent with the cell 24 crop.

**Round-1 reasons in the record.** The verifications block restates my round-1 reasons faithfully and in my terms. The B and C cross-references are correct.

## 3. Round-1 points

**Resolved:**
- **B1:** `blocked_by` is now `data_missing` for all 11 Fig. 6–9 claims.
- **B2:** ROIs are now bands one step long and 1, 3 or 5 steps wide, run under all readings.
- **B3:** a leave-one-out trough was added, and the counts are unchanged in kind.
- **B4:** a fixed needle-based ROI end was added. The shift is at most 0.156 mm, and no outcome changes except as described for 5C.
- **B5:** the joined e1 + e2 end is stated as a labelling choice.
- **B6:** the O3 (b) test is now labelled as an assumption.
- **C, dish2 centre:** the crop shows a cluster of cells, not saturation. The 44.6% bright fraction and the regions up to 49 µm are printed.
- **C, per-dish values:** per-dish values at widths 1, 3 and 5 are printed. A paired test for 5A trains against packets correctly does not apply, since the groups are different dishes.

**Still open:**
- **Bears on a conclusion:**
  - fig5b's classification depends on treating the paired test (O6) as a required reading (point 1 above). The claims file is ambiguous on this, and I report that rather than correct it.
  - fig5c's block rests on calling every ROI width equally well founded, which is arguable (point 2 above).
- **Does not bear on a conclusion:** I still have not run synthetic tests of the helpers. I checked them by reading the code only.
