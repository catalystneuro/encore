**A. Outcomes** (19 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| neuron-counts | not_reproduced | Cell 6: the archive has 53 neurons. Per condition it has 22/29/26 (by folder) or 22/27/26 (by stimulus), against the paper's 25/30/28. Overlaps are 7/10/36 against 7/11/40. Only "all three = 7" matches. The spreadsheet has 58 rows, and the 5 with no condition marked account exactly for the gap (one neuron in two conditions, four in one). So this is missing data in the archive, not a contradiction of the paper. |
| spikes-per-condition | blocked (data_missing) | The archive holds only rate maps and stimuli (I listed the zip's central directory: 77 map/stimulus pairs and one xlsx). An eye time map exists for 1 of 77 files. See C about the unexamined `norm` field. |
| s4-baseline-no-difference | not_reproduced (fragile) | Cell 12, main readings: BH rank sum Edge vs Corners p = 0.044, Kruskal-Wallis p = 0.028, ANOVA p = 0.005. All three readings find a difference. With the files' BaseActivity, Corners readings (b) or (c), or zero pixels left out, the result flips to "no difference". The verdict depends on an open baseline placement, and Star has n = 12 against the paper's 30. |
| fig4a-above-baseline | reproduced | Cell 14, main: 86 to 100% of neurons are above baseline, and the distance order P180 < S90 < S52 < S40 holds under both the raw and log readings. Under three baseline variants the log order fails, but the raw order holds in all. |
| fig4b-spike-rate-difference | reproduced | Cell 16: 4.62 / 8.84 / 19.67 / 26.32 against 4.87 / 10.69 / 18.10 / 25.60. All four are within the paper's SEM and in the right order. n is 22/22/12/26, not 25/25/30/28. Under most variants 3 of 4 are within tolerance and the order always holds. |
| fig4b-pairwise-significance | reproduced | Cell 18: all three named pairs have BH p ≤ 0.0003 under both families, and they stay significant under every variant. |
| fig5-average-maps | reproduced | Cell 20: the midpoint reading orders 26.32 > 19.73 > 8.74 > 4.54. As the claims file says, this is not independent of fig4b. |
| table1-edge | partially_reproduced | Cell 22, reading (i)(a): 4 of 5 values within tolerance. The minimum is 6.13 against 7.98 ± 1.60. |
| table1-p180 | partially_reproduced | 4 of 5. The minimum is −1.29 against 0.18 ± 1.01. |
| table1-s90 | partially_reproduced | 4 of 5. The minimum is 2.96 against 4.36 ± 1.07. |
| table1-s52 | partially_reproduced | 4 of 5 under (i)(a). The minimum is 9.15 against 6.26 ± 1.33. n = 12. |
| table1-s40 | reproduced | 5 of 5 under (i)(a). |
| fig6-midpoint-representative | reproduced | Cell 24: 0 of 10 rank sum tests are significant (smallest p = 0.45). The signed rank variant gives 3 of 10 significant; this is reported only as a variant. |
| fig7a-rms-contrast-fit | not_reproduced | Cell 26. Reading (a) gives a U-shaped profile (about 1.7 to 2.3 at 0%, 0.75 at 50%) and a fit that did not converge (a = −1787, R² = −0.08). Reading (b) gives a range of 0.01 to 0.45. Neither reading matches 0.61 to 0.943. The likely cause is an RMS definition, background value or luminance scale that differs from the paper's (reference [21] is unread). |
| fig7c-fold-edge-equivalence | not_reproduced | Cell 28. Under (a), P180 (4.62) is below every Edge level, so the nearest is 0%, not 50%. Under (b), P180 meets its rule, but S40 is above every level and the nearest is 94.3, which is 4.3 from 90 against a one-step margin of 3.7. If "one step" means one level from the level nearest 90, (b) would pass (see B5). |
| fig7c-fold-edge-significance | reproduced | Cell 30: P180 < Edge(0.943) and S40 > Edge(0.610, 0.647) are significant under all four corrections, including Bonferroni over 40 tests (p = 0.027 / 0.033 / 0.045). |
| fig7d-nonlinear | reproduced | Cell 32: the order is monotonic, and 3 of 4 means lie off the least-squares line by more than their SEM. |
| fig7d-dog-similar | blocked (data_missing) | The DOG output of reference [3] is not in the archive; the file list has only maps, stimuli and the xlsx. |
| s3-latency-peak | blocked (data_missing) | The archive confirms only maps made at 60 ms. It has no spike times or eye traces. |

**B. Problems**

1. [affects a conclusion] `load_all` and `measure` in cells 3–4 drop the 15 Star neurons without `Standard`, so S52 has 12 neurons against the paper's 30. The reason given is that the Star is drawn at one orientation on screen and the aligned diagonal is therefore unknown. No output shows that, and no check shows the 12 kept neurons are representative. This weakens table1-s52, the S52 parts of fig4a/4b, and s4.
2. [affects a conclusion] Cells 9–10 and the `measure` docstring: the main baseline placement was chosen after all results had been seen, by closeness to `BaseActivity`. The notebook states this as an assumption. The rule is reasonable, but the s4 verdict flips with the placement, and the count of fig4b and Table 1 values within tolerance falls from 4/4 to 3/4 (and to 1–2 of 5 for some Table 1 folds) under the variants.
3. [affects a conclusion] Baseline squares for Star and Corners are 35–39% zero pixels (cell 3, `base_zero_frac`). These are likely unsampled screen positions at the frame edges. In the paper's definition (count divided by eye time) such pixels are undefined, not zero. The one file with an eye time map was not used to check this. The s4 outcome depends on it (`base_nz` gives no difference under reading (a)).
4. [affects a conclusion] `rms_contrast_profile` and cell 26: neither the stimulus gray scale (`stim_range` is computed but never printed) nor the luminance outside the Edge was shown, and contrast was computed on gray levels, not cd/m². The fig7a failure cannot be separated from these choices. The reading (a) fit is meaningless and should not be read as parameters.
5. [affects a conclusion] In cell 28, the one-step rule for S40 under reading (b) is applied as |level − 90| ≤ 3.7. The claims file's wording also allows "one level from the level nearest 90", which would make fig7c-equivalence reproduced under (b). The markdown says a refit variant would be run, but none was run (the markdown sentence is also garbled).
6. [does not affect a conclusion] `rect_mask` uses strict `<`. At integer centres the "8 × 8" and "16 × 16" squares hold 49 and 225 pixels. I tested this on a synthetic map; `blocks` and `midpoint` gave the exact expected means on a linear ramp.
7. [does not affect a conclusion] Cell 24 runs fig6 only under reading (i). Medians under reading (ii) for S90 and S52 were not tested; means are identical under both readings.
8. [does not affect a conclusion] Cell 6 does not point out that the 5 unmarked spreadsheet rows close the gap to 58/7/11/40. Counting the Star folder as 29 includes the two ABS files that hold Corners stimuli.
9. [does not affect a conclusion] Claims file, reported, not corrected:
   - Under fig7c reading (a), the paper's own Table 1 (Edge midpoint 22.01 against P180 4.87) rules out "P180 ≈ 50% Edge", so (a) cannot be the paper's meaning.
   - The checks block still lists "whether Corners S40 averages the two S40 folds" as open, though the criteria fix it as bright only.
   - The paper gives the Star ROI as 160 × 160 DU while the star radius is 150 DU. The claims file does not note this inconsistency.

**C. What I could not check, and the output that would settle it**

- Whether the `norm`, `smoothed_image_norm` and `original_image` fields hold spike counts or eye time. A print of their shapes, values and units for a few files would show whether spikes-per-condition can be tested; the descriptor says `smoothed_image_norm` is the eye-time-normalised map.
- Whether zeros in the baseline squares are unsampled pixels: for ABC050900J1A, a print of eye time inside each baseline square.
- That the Star screen stimulus is identical across neurons, and how the 12 registered Star neurons compare with the 15 dropped ones (for example, a stimulus difference across files and a comparison of screen map statistics).
- For fig7a: the stimulus gray range, the background value beside the Edge, and the pixel values in one 16 × 16 window at 0%, 50% and 100%.
- Star midpoint luminance (the Star stimulus was not warped) and the S40 fold length, which should be about 100 DU.
- I did not download the data or re-run the notebook; the 7 × 7 mask effect was tested only on synthetic input.
