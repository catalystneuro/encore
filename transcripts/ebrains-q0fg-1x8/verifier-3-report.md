I agree with the one proposed change: figs4-object-traces should go from partially reproduced to not reproduced.

The attempt record has one `proposed` entry, under figs4-object-traces (line 285); the claims file has 57 claims. I reviewed only that entry. I used the re-executed `02_single_cell_changes.ipynb` and `objcode.py`, and I did not download the data or re-run the notebook.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| figs4-object-traces | not_reproduced (from partially_reproduced) | Yes | — | See below |

**Reason (notebook 02, cell 12; result text in cell 13):**

1. **The numbers come from the data.**
   - **Code path:** cell 12 takes the cells that change between NO and NO' from the classification in cell 4. It then finds fields in each cell's NO' map with `oc.fields` and builds a circular region of interest (ROI) per field with `oc.roi_offsets`.
   - **Overlap and shuffle:** it computes the rate overlap of each ROI in NO' and OM with `oc.roi_rate_overlap`. It compares that with 1,000 random wrap-around placements in OM (`oc.roi_rate_overlap_shuffled`) and counts a field as a trace above the 99th percentile. A cell counts if any of its fields passes.
   - **Results:** 908 and 916 cells change between NO and NO'. Between 72 and 117 cells have a trace field, which is 0.061 to 0.098 of 1,189.
   - **Binomial tests:** I recomputed the two-sided exact test against 0.183. For 72, 88, 115 and 117 cells it gives p ≈ 4.9e-35, 4.2e-27, 9.5e-17 and 4.8e-16. These agree with the printed 8.2e-35 to 6.5e-16 to within the two-sided convention, so "p at most 1.4e-16" holds.

2. **The choices are not tuned to the result.** The notebook runs all eight combinations of the two field readings, the claims file's two ROI readings and the two rate-overlap readings. No combination comes near the target:
   - The largest fraction is 0.098, against a lower bound of 0.165.
   - In every combination, "fraction ok" is False and "reproduced" is False (cell 12).

   Nothing was picked from among the readings.

3. **The criterion is applied as written.** The claims file's criterion for this claim reads: "Reproduced when, under one reading, both values are within tolerance and a two-sided binomial test … against 1% gives p < 0.05."
   - It has no partially reproduced case, unlike claims whose criteria define one (for example the claims-file criteria at lines 437 and 505).
   - The NO–NO' count is within tolerance, and the test against 1% gives p < 1e-32. The trace fraction is outside 0.183 ± 0.0183 in every combination. So no reading meets the criterion, and the outcome under it is not reproduced.
   - The round-1 and round-2 partially reproduced outcome was not available under this criterion as written.

4. **Caveat, which does not change the outcome.**
   - **The open field question:** `oc.fields` takes connected regions above 3 × MAD rather than the Methods' contour from the peak. Whether that contour splits fields is still an open question in the questions file.
   - **Fewer cells with fields:** here only 814 to 886 of the 908 to 916 changing cells have a NO' field. In the paper, all 919 do (1,252 fields; Supplementary Figure 4 legend). So the field detection probably finds fewer fields than the paper's.
   - **That accounts for only a small part of the gap:** among cells that have fields, the trace fraction here is about 10 to 14% (for example 88/881 and 115/814). The paper's is 23.7% (218/919). Even if every changing cell had fields at the same pass rate, the count would stay far below 218.
   - **If that question is answered**, it should be re-checked against this outcome.

5. **Claims file against the paper.** The claims file does not misread the paper for this claim. Its values (218/1,189 = 0.183, 919 changing cells, binomial test against 1%) and its procedure match the Methods ("Region-of-interest analysis for object traces") and the Supplementary Figure 4 legend. Its note that the ROI size is open is accurate: the Methods refer to a section on ROI analysis for object responses that the paper does not contain.
