**Verifier report: Martinez-Conde et al. 2019 on CRCNS pvc-12, round 1**

The claims file has 19 claims. My outcomes: 8 reproduced, 1 partially reproduced, 7 not reproduced, 3 blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| neuron-counts | not_reproduced | The files hold 53 cells: 22 in Square and Edge, 29 in Star, 26 in Corners. Only the three-condition count matches (7); the others are 10 vs 11 and 36 vs 40. Neither the per-condition set nor the overlap set matches fully, so the criterion's partial clause does not apply. The spreadsheet lists 58 codes, but 5 have no condition and no files. |
| spikes-per-condition | blocked (data_missing) | `image` is a rate (rate × eye time gives integers, cell 3), and eye time is stored for only 1 of 77 recordings. That one recording has 15,644 spikes, above the 10,000 floor, but the mean and STD cannot be computed. |
| s4-baseline-no-difference | not_reproduced | On the main measure all three readings find a difference: (a) Square and Edge vs Corners, BH-adjusted p = 0.009, and vs Star, p = 0.036; (b) Kruskal-Wallis p = 0.005; (c) ANOVA p = 0.001. Only the files' stored BaseActivity, present for 38 of 60 recordings, gives no difference (Kruskal-Wallis p = 0.11). |
| fig4a-above-baseline | reproduced | 86–100% of neurons lie above baseline. The distance is ordered P180 < S90 < S52 < S40 under both readings: (a) 3.85 / 8.09 / 19.04 / 26.62; (b) 0.17 / 0.30 / 0.88 / 1.04 log10 units. |
| fig4b-spike-rate-difference | partially_reproduced | The order S40 > S52 > S90 > P180 holds. S90 is 8.09, against 10.69 ± 1.94, so it is out of tolerance; the other three are within. No pooled variant brings all four within tolerance. |
| fig4b-pairwise-significance | reproduced | All three named pairs are significant under both families (BH p ≤ 0.0001 on the main measure) and under every variant. |
| fig5-average-maps | reproduced | Midpoints of the average map: 26.79 > 19.04 > 8.09 > 3.85. As the claims file says, this is not independent of fig4b. |
| table1-edge | not_reproduced | 1 of 5 values within tolerance under every reading. All values are about 3.6 spikes/s low; for example the mean is 16.82 vs 20.44. |
| table1-p180 | not_reproduced | 2 of 5 under both readings. |
| table1-s90 | not_reproduced | At most 1 of 5 under any reading. |
| table1-s52 | reproduced | 5 of 5 under reading (a ii) only; the other readings give 3–4. This rests on n = 12, against the paper's 30. |
| table1-s40 | reproduced | 5 of 5 under reading (a). |
| fig6-midpoint-representative | reproduced | 0 of 10 rank-sum tests significant (lowest p = 0.415). The signed-rank variant finds 3 significant: S40 vs block mean p = 0.015 and vs median p = 0.007, and S90 vs median p = 0.025. |
| fig7a-rms-contrast-fit | not_reproduced | Neither reading comes close. Reading (a) runs 0.96–2.11 and falls with luminance; reading (b) runs 0.014–0.48. |
| fig7c-fold-edge-equivalence | not_reproduced (borderline) | Under (a) the Edge level nearest P180 is 0%, not 50%. Under (b) the level nearest S40 is 94.3, which is 4.3 points from 90 where one step is 3.7. Both matches under (b) are just the extremes: P180 (3.85) is below every Edge response (lowest 8.34) and S40 (26.62) is above every one (highest 20.09). See problem 1. |
| fig7c-fold-edge-significance | reproduced | P180 < Edge at 0.943 and S40 > Edge at 0.610 and 0.647 under all four corrections; for example Bonferroni over all 40 tests gives 0.020, 0.018 and 0.026. |
| fig7d-nonlinear | reproduced | The order is monotonic, and 3 of 4 means lie off the least-squares line by more than their SEM (line R² = 0.78). In the variant, the 52–90 and 90–180 slopes differ by more than their propagated SEM. |
| fig7d-dog-similar | blocked (data_missing) | Needs the DOG model output of reference [3], which is outside the dataset. |
| s3-latency-peak | blocked (data_missing) | Needs spike times and eye traces, which are not deposited. |

**Archive check for the blocked claims.** The S3 listing of `pvc-12/` holds only `V1_Vasarely_data.zip`, `checksums.md5`, `filelist.txt` and two descriptor files. `filelist.txt` agrees. The notebook's count of 155 files in the zip is 77 rate maps, 77 stimuli and one spreadsheet, so there are no spike times, eye traces or eye-time maps beyond the one recording.
- spikes-per-condition: only the 10,000 floor can be checked, for that one recording.
- s3-latency-peak: nothing can be tested.
- fig7d-dog-similar: nothing can be tested from the archive.

### B. Problems

1. **[affects a conclusion] cell 31, `res7c["b"]`.** The criterion's "within one step of 90%" is implemented as |level − 90| ≤ 3.7. A second reading is just as natural: one level away from the level nearest 90 (90.6), which would accept 94.3. Under that reading, reading (b) passes and the claim would be reproduced. Only one interpretation was run. The test under (b) is also degenerate, since it can only pick the extreme levels.
2. **[affects a conclusion] cells 3, 5 and 10, the Square and Edge baseline.** The notebook's four squares give a baseline 1.21 times the files' stored `BaseActivity`. Cell 3 finds that the stored value is matched within 3.9% by a single 16 × 16 square, not by four. That square was never located, and it was never checked whether it lies on a 0% area. With the stored baseline:
   - s4 becomes non-significant;
   - fig4b S90 comes within tolerance (9.02);
   - table1-p180 reaches 4 of 5 values and table1-s90 reaches 3 of 5.
   The main analysis follows the paper's text, so my outcomes stand, but the low Square and Edge values and the s4 result may come from this construction.
3. **[does not affect a conclusion] cells 3–5, the Star sample.** Star uses 12 of the 29 recordings (the paper has 30), because only those 12 have a `Standard` struct. Whether these 12 are representative was not checked, for example by comparing overall rates in the full gaze-frame `image` against the 17 left out. table1-s52 and fig4a for S52 rest on n = 12.
4. **[does not affect a conclusion] `square_mean` and `box_mean`.** When a box lies wholly above or left of the frame, the slice end goes negative and Python wraps it. In a synthetic test, `square_mean(M, 0, -20, 16)` returned the mean of rows 0 to −4, i.e. most of the map, instead of NaN. The same slicing appears in cell 3's luminance check. By the geometry (ROI 337 × 151, 321 × 321, and the Corners squares at the frame edges) every box lies inside the frame, so the bug is not triggered here.
5. **[does not affect a conclusion] `load_recording`.** The docstring says the notebook checks `stim_offset=1.0` against the Edge position, but no cell does this. The sampled midpoint luminances (about 49.5%) suggest any error is at most a pixel.
6. **[does not affect a conclusion] fig7a, cell 29.** RMS on grey levels with black = 0 cannot fall below about 1 for a patch straddling a black boundary; a synthetic half-and-half patch gives exactly 1.0. So the paper's 0.61–0.943 probably used physical luminance with a non-zero black level. That reading is not in the claims file and needs monitor calibration, which the data do not hold.
7. **[does not affect a conclusion] cell 18.** In the fig5 table, `left_out` is hard-coded to 0 rather than computed.
8. **[does not affect a conclusion] cell 3, registration of Square and Edge maps.** The rate on the lit rectangle versus the black area is only weakly different from the mirrored map (p = 0.13, 16 of 22 positive), and this is not discussed. The Corners bright-vs-dark check is strong (p = 2e-6).
9. **[does not affect a conclusion] Corners baseline squares.** They sit at grey level 1.01, the darkest level of that stimulus, not 0. Their placement is the author's stated reading of Fig 2C.
10. **[does not affect a conclusion] Claims file.** Its `checks` entry says whether the Corners S40 midpoint averages the two folds is "not stated", while every criterion fixes the bright fold only. This is an internal inconsistency, not a misreading of the paper; the paper (Methods, Corners, paragraph 2) supports bright-only.

### C. What I could not check

- **Block lengths.** The fold lengths actually used (expected 150, 150, 70.7, 150 and 100 DU, giving 15, 15, 7, 15 and 10 DU blocks) are never printed. The S40 apex track from polygon 0 to 99 is the main uncertainty. Printing `np.linalg.norm(end − start)` per fold would settle it.
- **Baseline square positions and the stored value.** Positions are not printed for each condition, and neither is the location and luminance of the single square that best reproduces the stored `BaseActivity`. A printout of both, plus the baseline tests rerun with that square, would show whether problem 2 changes s4, fig4b and Table 1.
- **The 17 Star recordings without `Standard`.** No comparison of these with the 12 used, such as mean rate in the gaze-frame `image`.
- **Zip contents.** I relied on the notebook's count of 155 files rather than listing the zip myself, since that would have meant downloading it.
- **Square and Edge frame orientation.** No check that the frame is not mirrored, for example by printing the Edge and P180 luminance profiles along their blocks next to the expected 0–100% ramps.
