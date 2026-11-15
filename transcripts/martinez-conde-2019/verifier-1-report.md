**A. Outcomes** (all 19 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| neuron-counts | not_reproduced | The files hold 53 neurons, split 22 / 29 (27 with a Star stimulus) / 26 by condition, with overlaps 7 / 10 / 36. The paper gives 58 neurons, 25 / 30 / 28, and 7 / 11 / 40 (cell 12). Only "all three = 7" matches. The xlsx sheet lists 58 cells, but 5 have no condition and the data description says the dataset holds 53 neurons. The gap fits 5 cells missing from the archive (4 tested in one condition, 1 in two), not a wrong count in the paper. |
| spikes-per-condition | blocked (data_missing) | There are no spike count maps or spike times. Eye time is stored in only one file (ABC050900J1A, 15,644 spikes, which is at least 10,000). I confirmed from the archive's zip directory that it holds only the SpikeRateMap/Stimulus .mat files and the xlsx. |
| s4-baseline-no-difference | not_reproduced | With the claims-file baseline, all three readings find a difference: BH-corrected rank sum p = 0.016 / 0.008 / 0.66, Kruskal-Wallis p = 0.004, ANOVA p = 0.001. The centred-square variant gives the same result (cell 15). Only the stored `BaseActivity` on smaller subsets (n = 9 / 10 / 19) is not significant, and its medians keep the same order (5.6 / 2.7 / 1.3). |
| fig4a-above-baseline | reproduced | 91%, 91%, 100% and 100% of neurons lie above baseline. Distances from the unit line run 3.9 < 8.2 < 19.0 < 26.5 under reading (a) and 0.18 < 0.30 < 0.91 < 1.04 under reading (b) (cell 17). S52 has only 12 neurons. |
| fig4b-spike-rate-difference | partially_reproduced | The order S40 > S52 > S90 > P180 holds: 26.48, 19.01, 8.19, 3.88. S90 is 8.19 against 10.69 ± 1.94 (outside). The centred baseline gives 8.57, still outside (cell 19). |
| fig4b-pairwise-significance | reproduced | All 3 named pairs have BH p ≤ 0.0001 under both the 6-pair and 3-pair families (cell 21). |
| fig5-average-maps | reproduced | Midpoints of the average maps are 26.48 > 19.14 > 8.22 > 3.79 (cell 23). This is not independent of fig4b, as the claims file notes. |
| table1-edge | partially_reproduced (notebook: 2/5) | With the "inside" baseline, readings (a) and (b) each get 2/5. The centred placement, which the paper also allows, raises every Square and Edge difference by the same 0.38 spikes/s (cell 19: diffc − diff = 0.38 for both P180 and S90). That gives (a) 5.89 / 30.24 / 17.30 / 17.16 / 19.10, and 3/5 within tolerance (max, mean, midpoint). See problem 2. |
| table1-p180 | partially_reproduced | 3/5 under (a) and (b) (cell 29). With the centred baseline it is 4/5. |
| table1-s90 | partially_reproduced (notebook: at most 1/5) | With the inside baseline the best reading is 1/5. With the centred baseline, (a)(i) becomes 2.68 / 13.81 / 7.84 / 7.88 / 8.57, which is 3/5 (max, mean, median). See problem 2. |
| table1-s52 | reproduced | Reading (a)(ii) is 7.46 / 28.71 / 17.11 / 16.43 / 19.01, all 5 within tolerance (cell 33). This rests on 12 of 30 neurons and on picking the best of 4 readings. |
| table1-s40 | reproduced | Reading (a) is 10.22 / 34.36 / 23.04 / 23.06 / 26.48, 5/5 (cell 35). |
| fig6-midpoint-representative | reproduced | 0 of 10 rank sum tests have p < 0.05; the smallest p is 0.43 (cell 37). The paired signed-rank variant is significant in 3 of 10 (S90 median, S40 mean and median). |
| fig7a-rms-contrast-fit | not_reproduced as run, but the test is invalid | Under neither reading is any value within tolerance (cell 39: rms_a ≈ 1.06 flat; rms_b at most 0.47). The input does not follow the criterion, though (problem 1). With a non-zero background, reading (a) plausibly gives the paper's curve, so the evidence does not support a negative outcome. |
| fig7c-fold-edge-equivalence | not_reproduced | Edge responses span only about 8.6 to 21 spikes/s, so P180 (3.88) falls below every Edge level and S40 (26.48) above them. No reading meets both conditions (cell 41). It uses the paper's fit parameters, as the criterion asks. |
| fig7c-fold-edge-significance | reproduced | P180 is below the Edge at 0.943, and S40 is above it at 0.610 and 0.647, under every correction (cell 43). With Bonferroni over 40 tests, exactly 0.610 and 0.647 are significant for S40, matching the paper's "<68%". |
| fig7d-nonlinear | reproduced | The means fall monotonically with angle. 3 of 4 points lie off the least-squares line by more than their SEM. In the slope variant, 2 of 3 slope pairs differ (cell 45). |
| fig7d-dog-similar | blocked (data_missing) | The DOG output of reference [3] is external. The zip holds no model files (I checked its directory). |
| s3-latency-peak | blocked (data_missing) | Only maps at 60 ms are present, with no spike times or eye traces (zip directory and data description confirm this). Nothing about it can be tested. |

**B. Problems**

1. [affects a conclusion] `vasarely.rms_profile` / `edge_luminance`, cell 39: luminance comes from counting polygons, with the background set to 0. The criterion says to compute RMS from "the Square and Edge stimulus image", and the dataset ships `EdgecompImage` holding "the actual grayscale values" (data description).
   - With a zero background, SD/mean of a window half on the background and half on the Edge is ≈ 1 at every level. The test therefore cannot reproduce the paper's curve by construction.
   - Synthetic check: take a background of 0.74, 0% = 3.05 and 100% = 25.2, with 50% = 14.07 cd/m² as the paper gives. SD/mean then runs 0.609 → 0.943, and the exponential fit gives a = −0.31, b = 0.046, c = 0.94, R² = 0.9945.
   - The refit variant of fig7c was skipped because of this.
2. [affects a conclusion] Baseline placement, cells 19 and 25–35: the paper does not say whether the squares sit inside the corners or centred on them. The centred variant was run only for fig4b and s4, not for the Table 1 claims. Since it shifts every Square and Edge difference by +0.38, it raises table1-edge (2/5 → 3/5) and table1-s90 (1/5 → 3/5) to partially_reproduced.
3. [does not affect a conclusion] Cells 7–8: 15 of 27 Star files are dropped. The only evidence that they cannot be registered is r = −0.11 between screen-frame and aligned midpoints in `star_screen_measures`. The fit residual of `star_aligned_angle` is never printed, and there is no direct registration test such as cross-correlating `Standard` against the screen map. All Star results rest on n = 12 of 30.
4. [does not affect a conclusion] Cell 15: the stored-`BaseActivity` variant is tested on smaller subsets, but the main placement is not tested on those same subsets. Power and placement cannot be separated, but the claim fails under the claims-file definition either way.
5. [does not affect a conclusion] Corners baseline (`corners_baseline_squares`): the bottom corners of the frame are an assumption the notebook states. Against the stored values, Spearman is 0.85 and the main baseline is higher (median 2.04 vs 1.32). S40 passes under either.
6. [does not affect a conclusion] `table1`: `sa` and `sem` are computed but unused. Cell 37 uses only block reading (i), whereas S52 reproduced under (ii). With p ≥ 0.43, this cannot change the result.
7. [does not affect a conclusion] In the data check, `measures` offfold for P180 at x + 32 = 155 lies outside the 151-wide frame, so its box is clipped to one column. The function is used only in the data check.
8. [does not affect a conclusion] Cell 0 / cell 13 text says "eye time in 1 of 75 files", but there are 77 map files (76 read).
9. [does not affect a conclusion] Claims file: its checks list "whether the Corners S40 midpoint averages the two S40 folds" as open. The paper (Methods, Corners, paragraph 2: "We did not analyze dark corner-folds") and the claims file's own criteria settle it as the bright fold only. The notebook follows the criteria.

**C. What I could not check**

- The gray levels of the stimulus image (background value, Edge 0%/100% levels) and the local RMS profile computed from `EdgecompImage`. These would decide fig7a and possibly fig7c. Output needed: those values plus `rms_profile` run on the image.
- That rasterising the polygons matches the stimulus image, and the 0%/100% direction of the Edge that fig7c's luminance mapping depends on. The module docstring asserts this but no output shows it. Output needed: a per-file agreement between polygon luminance and image gray levels.
- That the baseline squares, especially the Corners ones, lie in 0% luminance. Output needed: the stimulus luminance inside each square.
- Table 1, fig4b and fig7c under the centred baseline and under the stored baseline on the 38-file subset. Output needed: those tables. I derived the centred shift exactly from cell 19.
- The fit error of `star_aligned_angle`, and a cross-correlation registration of screen-frame Star maps against `Standard`.
- The paper's S1 and S2 Tables (exact p-values and correction family) are not in the text, so I could not compare corrections exactly.
