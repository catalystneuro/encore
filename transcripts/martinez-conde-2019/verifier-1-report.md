**A. Outcomes** (19 claims, from the claims file. The attempt record was not among my materials.)

| Claim | My outcome | Reason |
|---|---|---|
| neuron-counts | not_reproduced | The deposited files give 53 neurons; 22/29/26 per condition; 7/10/36 tested in three/two/one conditions. The paper has 58; 25/30/28; 7/11/40 (cell 26). The spreadsheet lists 58 cells, but 5 have no experiment marked. The gap fits exactly 5 undeposited neurons (one tested in two conditions, four in one: 83 − 77 = 6 condition slots), so this is a deposit gap, not evidence against the paper. |
| spikes-per-condition | blocked (data_missing) | The zip holds only rate maps, stimuli and the spreadsheet (I checked its central directory). One file stores eye time and gives 15,644 spikes, which is ≥ 10,000. The `norm` field was never inspected (see B6). |
| s4-baseline-no-difference | not_reproduced (low confidence) | With the Methods' baseline squares, all three tests are significant: Kruskal-Wallis p = 0.0035, ANOVA p = 0.0010, and BH-corrected rank sums p = 0.013 and 0.008 for Square and Edge against the other two (cell 29). Square and Edge has median 7.68 against 1.84 and 2.45. With the undocumented `BaseActivity` (38 files) no test is significant. The outcome depends on the baseline definition. |
| fig4a-above-baseline | reproduced | More than half above the line for every fold (91 to 100%). Mass centres are above the line and ordered P180 < S90 < S52 < S40 under both mass-centre readings and both baselines (cell 31). |
| fig4b-spike-rate-difference | partially_reproduced | The order S40 > S52 > S90 > P180 holds in every variant. In the main reading S90 is 8.21 against 10.69 ± 1.94, just outside tolerance. No variant puts all four means within tolerance (cell 33). |
| fig4b-pairwise-significance | reproduced | All three named pairs have BH p ≤ 0.0001, in both families and both baselines (cell 35). |
| fig5-average-maps | reproduced | Midpoints of the average maps are ordered 26.41 > 19.07 > 8.15 > 3.79 (cell 37). As the claims file says, this is not independent of fig4b. |
| table1-edge | not_reproduced | At most 2 of 5 values within tolerance under any reading (cell 41). |
| table1-p180 | partially_reproduced | 3 of 5 within tolerance under main readings (a) and (b) (cell 43). |
| table1-s90 | not_reproduced | At most 2 of 5 within tolerance; every value is low (cell 45). |
| table1-s52 | partially_reproduced | 4 of 5 under squares baseline, reading (a). The minimum is 9.19 against 6.26 ± 1.33 (cell 47). |
| table1-s40 | reproduced | 5 of 5 under reading (a) with either baseline (cell 49). |
| fig6-midpoint-representative | reproduced | 0 of 10 rank-sum tests are significant under every reading (cell 51). The paired signed-rank variant finds S40 and S90 significant; the notebook reports it. |
| fig7a-rms-contrast-fit | not_reproduced (uninformative) | Reading (a) gives 0.94 to 2.09. Reading (b) gives at most 0.475 and degenerate fit parameters (cell 53). Neither reading in the claims file can produce the paper's curve (B4). |
| fig7c-fold-edge-equivalence | not_reproduced | Under reading (a), P180 (3.88) is nearest the 0% Edge level, not 50%. Under reading (b), S40 is nearest 0.943, which is 0.043 from 0.90, more than one step (cell 55). The result is sensitive to how "one step" is read (B5). |
| fig7c-fold-edge-significance | reproduced | Squares baseline: P180 < Edge at 0.943 and S40 > Edge at 0.610 and 0.647 under every correction (cell 57). Bonferroni over all 40 tests also matches the paper's boundary: S40 is significant only at 0.610 and 0.647. |
| fig7d-nonlinear | reproduced | Monotonic, and three of four means lie off the fitted line by more than their SEM (cell 59). The slope variant also differs between 52–90 and 90–180. |
| fig7d-dog-similar | blocked (data_missing) | Needs the DOG model output of reference [3]. The archive does not hold it. |
| s3-latency-peak | blocked (data_missing) | The zip holds only maps made at 60 ms: no spike times or eye traces (confirmed from the zip listing). No part can be tested. |

**B. Problems**

1. [affects a conclusion] The s4 outcome depends on the baseline (`baseline_squares`, cells 21 and 29), and it was not tested for sensitivity.
   - For Square and Edge, the squares are moved inside the corners of the 138 DU square, not centred on them. For Corners, their placement is assumed.
   - `BaseActivity` is probably the authors' own number. It reverses the outcome, but exists for only 38 of 60 files.
   - No alternative placement was run, for example centred squares clipped to the ROI.
2. [affects a conclusion] Star rests on 12 of 30 neurons, the files that have `Standard` (cell 23). This touches s4, fig4a, fig4b, the pairwise tests and table1-s52. Nothing checks whether these 12 differ from the 17 that cannot be registered, for example in gaze-frame peak rate or baseline.
3. [affects a conclusion] Every Square and Edge quantity is below the paper: Edge midpoint 18.7 vs 22.0, S90 8.2 vs 10.7, P180 3.9 vs 4.9. Star and Corners match. The Square and Edge baseline is also the high one in s4. This points to an offset specific to that condition, from the baseline or the geometry. It was not investigated, and it drives the table1-edge, table1-s90 and fig4b S90 failures.
4. [affects a conclusion] `rms_contrast` reading (a): a 16 DU box centred on the Edge with a 0 background gives SD/mean = 1 exactly at any luminance (I confirmed this on a synthetic image). It cannot rise with luminance. Reading (b) cannot exceed 0.5. The paper's 0.61 to 0.943 requires physical luminance with a non-zero black level (it gives 14.07 cd/m² at 50%). This is a gap in the claims file's readings, not in the code, but it makes the fig7a test uninformative. The robust fit uses `soft_l1`, not LAR; this does not matter here.
5. [affects a conclusion] In `equivalence` (cell 55), reading (b) uses |level − 0.90| ≤ 0.037. Reading "one step" as one grid step from the level nearest 90% (0.906) lets 0.943 pass, and the claim would be reproduced. Also, P180 lies below every Edge level and S40 above every level, so "nearest" just picks the ends of the range.
6. [does not affect a conclusion; could affect the blocked status of spikes-per-condition] The fields `norm` (74 of 77 files) and `smoothed_image_norm` (38 files) are listed but never examined (cells 3 and 9). The descriptor says `smoothed_image_norm` is normalised by eye time. If `norm` holds eye time or a count, spike totals could be computed.
7. [does not affect a conclusion] Cell 17 says every fold runs from 0% to 100%. Yet Edge@50% and Edge@95% go as low as 24% and 47% (cell 14). That is the 2 DU check box straddling the rectangle boundary, not a geometry error, but the statement is unsupported for the Edge.
8. [does not affect a conclusion] The refit variant for fig7c named in the claims file was not run (cell 55). The refit parameters are degenerate anyway.
9. [does not affect a conclusion] `avg_map` (cell 37) assumes the two Corners map sizes are concentric and never checks it. The midpoint of the average map equals the per-neuron mean (26.41), so it holds.
10. [does not affect a conclusion] The smoothing kernel does not match Fig 3B (SD 7 vs about 5, cell 11). The deposited maps are used, and the notebook says so.
11. [does not affect a conclusion] Registration rests on the authors' `Standard`. The band along the Edge beats every shifted band in only 16 of 22 neurons (cell 18).

I tested `box_mask`, `midpoint`, `blocks`, `box_mean` and `rms_contrast` on synthetic arrays. They return the expected values: 64-pixel boxes, correct block centres, and a half-covered box giving 0.5.

**C. What I could not check**

- What `norm` and `smoothed_image_norm` hold. Printing their shape, range, and ratio to `image` and `smoothed_image` would settle the units and possibly unblock spikes-per-condition.
- Whether the s4 and Square-and-Edge results survive other baseline placements. A run with squares centred on the 138 DU corners (clipped to the ROI), and a per-file listing of the squares and `BaseActivity` side by side, would show this.
- Whether the 12 registered Star neurons are representative. Gaze-frame peak rate and spike-map statistics for registered vs unregistered Star files would show this.
- Why Square and Edge falls short. Per-neuron midpoint response and baseline for Square and Edge, set against implied paper values, would help.
- The stimulus luminance in physical units or the monitor black level. Neither is in the data, so fig7a cannot be tested meaningfully.
