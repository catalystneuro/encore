**Verifier report, round 2: Kim et al. 2023 (doi:10.3390/ijms241310921) on DANDI:000631 v0.231012.1508**

The claims file has 12 claims, and the attempt record gives an outcome for each of the 12. Six are tested: five on Figure 2 and one on Figure 4. Six are blocked as data_missing: four on Figure 3 and two on Figure 5.

### 1. Outcomes

| Claim | Record | Agree? | Assumptions (`assumed: true`) |
|---|---|---|---|
| fig2-180-cancellation | partially_reproduced | Yes | The pixel size, the ROI layout and the 0.5 mm background disk are all stated in the deviations, and I find them reasonable. Each layout passes a different frequency: 833 kHz holds on L2, 1 Hz holds on L1. The record says so. |
| fig2-crossover-angle | reproduced | Yes, as the criterion is written. Confidence at 1 Hz is low, and the record says so. | Stated and reasonable. The outcome is the same under both layouts, so it does not actually depend on the layout assumption. |
| fig2-facilitation-plateau | partially_reproduced | Yes | Stated. One caveat the record leaves out: the 833 kHz half, which is the only reason the outcome is "partial", depends on the background region (see point 2a). |
| fig2-frequency-dependence | reproduced | Yes | Stated. It holds under all 16 readings and every footprint region. |
| fig2-60-fold-co-counter | reproduced (low confidence) | Yes, as the criterion is written, with low confidence | Stated: L2 as the deciding layout, reading (2), the 0.5 mm disk, and the comparison of dishes imaged on different days. All are reasonable, but taken together the claim is fragile (see point 3). |
| fig4-unipolar-pattern | reproduced | Yes | Stated. Taking the base with the larger uptake as the energised one does not matter: in every single-pulse dish, under every background-(b) reading, both bases exceed the apex (cell 45). |
| fig3 (4 claims), fig5 (2 claims) | blocked: data_missing | Yes | None |

I found no place where the claims file misreads the paper. Its quotes match Results 2.1 and 2.3 and Methods 4.2 and 4.4.

### 2. Text against the printed numbers

I checked every sentence of the "**Result:**" cells (28, 32, 36, 39, 43, 47), the Summary (cell 48), the README and the notes and responses in the attempt record. Every number quoted matches the printed outputs. The exceptions:

**a. The Summary (cell 48) says the footprint regions change only the 60-fold outcome.** It reads: "The lumen alone, the wall ring alone and a 0.6 mm disk give the same outcomes except for fig2-60-fold-co-counter."
- This is literally true of the outcome labels.
- But cell 35 shows the 833 kHz part of fig2-facilitation-plateau fails under two of the regions:
  - **Lumen alone:** the levels are 13.31, 3.71, 4.52 and 3.39, none within 2.7–3.3.
  - **Wall ring alone:** the only level in tolerance (2.79) is reached at 80.2°, outside 81–110.
- So the 833 kHz half holds only with the 0.5 mm and 0.6 mm disks.
- Cell 36 ("the three-fold plateau from 90 to 100 degrees holds only at 833 kHz") and the record's plateau notes do not say this. The round-1 response ("The levels are shown under each footprint region") shows the numbers but does not draw the conclusion.

**b. The Summary table (cell 48) lists "ROI layout" as an assumption for fig2-crossover-angle and fig2-frequency-dependence.** Both outcomes are the same on L1 and L2 (cells 30 and 38). The table contradicts the Summary's own bullet, "The layouts give different outcomes for fig2-60-fold-co-counter only." This is minor and errs on the cautious side.

**c. Stale cell numbers in the attempt record.** My round-1 reason for fig2-180 cites "(cell 21)". In this notebook the 180° table is cell 25, and cell 21 is the saturation text.

**My round-1 reasons in the attempt record.** The reasons are stated faithfully and in my words, with problems 1–6 of my report folded into the per-claim reasons. The "reviewed" field correctly lists my other points: saturation, comparison across days, and the choice of 1 Hz controls.

### 3. Round-1 points

| Round-1 point | Status |
|---|---|
| 1. Background region | Resolved. The radial profile (cell 11) is flat to about 0.55 mm, and in 3 dishes the lumen holds bright material, which justifies the 0.5 mm disk over the lumen alone. The sensitivity runs are printed. Point 2a above remains. |
| 2. ROI layout | Resolved. The layout is now a stated deviation from the claims file, and the rule that L2 decides is printed. The angle at the base midpoint is 167.7–170.4°, and the 180° point is 0.84–1.03 mm beyond the midpoint (cells 13–14). |
| 3. Selection bias of the minimum | Partly resolved. The bias is quantified and disclosed (cells 27 and 42). What remains is below. |
| 4. 1 Hz crossover rests on one ROI | Resolved. It is documented, and confidence is marked low. |
| 5. P2 under angle model C | Resolved. It is now reported as untestable, and model B decides it. |
| 6. Level (1) is one ROI | Resolved. The ROI count is printed and the text says so. |
| 7. Controls and comparison across days | Resolved as far as the files allow. The comparison across days itself stays open (below). |
| Section C items | All addressed: saturation is at most 0.03% of pixels and none at 833 kHz; per-dish tables of ROIs 0–7; MemBrite levels by day; a layout test with the 180° point. |

**What remains that bears on a conclusion:**

1. **The 60-fold ratio holds only at the single lowest ROI.** The bootstrap correction does not clear this.
   - The bootstrap resamples 3 paired and 3 control dishes. Every resample keeps each dish's own ROI-to-ROI noise, so it estimates only the variation between dishes. It therefore underestimates the bias of a minimum over 32 ROIs.
   - The estimated bias is 0.4–0.8 percentage points. Over ROIs 0–7 the mean curve itself ranges from 4.5% to 9.0%, all at 164–180° (cell 22).
   - Dividing by a less selected denominator, from the printed values: with the lowest ROI and its two neighbours, plateau level 2 over it is 2.96 × 16.42 ≈ 48.6 (normalisation i) and 2.80 × 18.77 ≈ 52.6 (ii). With all ROIs above 160°, it is about 39. All are outside 60 ± 6.
   - The notebook does not print this ratio. The outcome should stay at low confidence, and the bias-removed 56.9 should not be read as resolving the bias.
2. **The 833 kHz half of the plateau claim depends on the background region** (point 2a). This bears on the basis of "partially reproduced", not on the label.
3. **The 833 kHz paired dishes and controls were imaged on different days and cannot be checked against each other.**
   - MemBrite reads about 431 counts in the controls against about 295 in the paired dishes (cell 20). YP over MemBrite gives only 7.7–13.1-fold at 180° (cell 21).
   - Every 833 kHz fold and the 60-fold ratio rest on this comparison. The record states it, and the files cannot settle it.
