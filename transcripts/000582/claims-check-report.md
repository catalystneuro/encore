I checked the 000582 claims file against the paper, corrected eight claims and added one. It is ready for an attempt. Nothing was committed.

**Checker:** `21 claims, 21 quotes, 12 statistical values, 0 problems` (it was 20 claims, 0 problems before my changes).

**Changes, by claim**
- **Every source from spacing-dorsoventral on:** the paragraph numbers were one too high. The file treated a page break in the middle of paragraph 3 as a new paragraph.
- **fieldsize-dorsoventral:** the expected r was computed wrongly. Widening 0.44 to 0.94 by 10% of each bound gives 0.715 ± 0.319; the file had 0.6935 ± 0.2935.
- **hd-layers:** the statement said "most ... were directionally tuned". It now uses the paper's words, "a large proportion ... had directional preferences".
- **hd-stable-trials:** the statement now keeps the paper's "always stable".
- **cue-rotation-coherent:** the statement now keeps "always". It had said all five cells rotated 90 degrees, but the text says that only of the head-direction cells; the grid cell's rotation is only shown in the figure.
- **speed:** the statement said "most" head-direction and conjunctive cells, but the paper says "nearly all" for all three cell types. The criterion also treated P < 0.001 as a test applied to each cell. The Fig. 4B legend counts cells by positive slope alone, so P < 0.001 may instead test the count across cells. Both readings are now named.
- **hd-colocalized-distributed:** Watson's U2 test of uniformity works on angles only, so the criterion now tests the directions of the mean vectors, not "direction and rate".
- **hd-rates (new):** the head-direction cells' background rate (typically below 0.5 Hz) and peak rate (5 to 40 Hz) had no claim.

**Checked and correct:** every table S1 count and percentage, the fig. S3 r values, the 8 of 12 non-clustered ensembles in fig. S5, the Tukey and ANOVA values, and the 150 grid cells in the speed analysis (203 minus 53 conjunctive). No claim draws on another source; the paper links no code.

**Still open** (recorded under `checks`)
- **deep-hd-conjunctive:** the paper does not give the table behind its chi-square. I recomputed it from table S1B two ways: conjunctive against pure grid cells gives 49.3 and 15.0, and conjunctive against all other cells gives 29.0 and 16.7. Neither gives the paper's 28.4 and 6.2.
- **speed-intercept:** the default 10% tolerance on 422 of 423 would accept about 42 cells with negative intercepts, which makes that part weak. I kept it because the paper gives no spread to use instead.
- **speed-slope-steeper:** the reported F(2,422) does not fit 423 cells in three groups, which allows 420 error degrees of freedom.
- **Several criteria** (grid stability, phase and orientation, continuity, cue rotation, direction coverage, field size, the new hd-rates) rely on measures and thresholds the paper does not give. Each is named as a reading or a standard choice; the paper has nothing that would settle them.
