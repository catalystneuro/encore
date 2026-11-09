## Verification report, round 1: Sargolini et al. 2006 on dandiset 000582 (0.251111.2151)

The claims file has 21 claims; the notebook tests 18 and blocks 3. My outcomes: 5 reproduced, 2 partially reproduced, 4 not reproduced, 7 blocked as methods_underspecified and 3 blocked as data_missing. The paper states no chance level for any selection, so there was none to compare.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| layer2-grid | partially_reproduced | Cell 18: the order holds under all 56 readings (layer II 0.59–0.72, above 0.5 and above every deeper layer). Layers III (0.53–0.60), V (0.30–0.42) and VI (0.35–0.49) are outside tolerance under every reading. The non-grid cells are present, so the claim can be tested, but the denominators are not the paper's (problem 4). |
| grid-all-layers | reproduced | Cell 21: at least 35 grid cells in every layer under all 56 readings. |
| gridness-range-similar | blocked: methods_underspecified | Cell 23: Mann-Whitney finds a difference in 8 of 56 readings, Kruskal-Wallis in 53 of 56. The readings disagree. |
| grid-stable | blocked: methods_underspecified | Cell 25: no combination gives 100% stable. 84 of 448 give at least 90% (partial) and 364 do not. The grid-cell count (277–329 against 203 ± 20) is not judged, because the dataset is not the full set of sorted cells. |
| spacing-dorsoventral | blocked: data_missing | Confirmed (section C). |
| fieldsize-dorsoventral | blocked: data_missing | Confirmed (section C). |
| grid-phase-orientation | blocked: methods_underspecified | Cell 28: phase holds in all 224 readings. Orientation holds in every layer under only 88 of 224; layer VI fails under 22 to 33 of 56 and layer V under 14 to 15. The notebook's "partially_reproduced" is not an outcome the criterion names (problem 1). |
| hd-layers | not_reproduced | Cell 30: 2 to 9 layer II cells pass under all 4 readings, all from rat 11265. The criterion needs zero, and the partial outcome also needs zero. Layer III (0.53–0.60) is also outside tolerance. |
| hd-with-grid-colocalized | blocked: methods_underspecified | Cell 33: by file, more than half under 112/112 (grid or conjunctive) and 83/112 (pure grid). By tetrode, 0 of 224. |
| hd-tuning-breadth-layers | blocked: methods_underspecified | Cell 35: 196 of 696 tests find p < 0.05. U2 alone finds a difference in 10 of 232; angular SD in many more. |
| hd-full-range | reproduced | Cell 37: every 30°, 60° and 90° sector is filled in layers III, V and VI under all 4 readings. |
| hd-colocalized-distributed | reproduced | Cell 39: fewer than half the ensembles are clustered under every reading (pure HD: 0–3 of 9–16; with conjunctive: 2–4 of 26–28). The counts are off the expected 4 of 12; the criterion only says to compare them, and does not make them decide the outcome. |
| hd-stable-trials | reproduced | Cell 41: circular r 0.78–0.85 and mean curve r 0.77–0.81, all p < 0.001, within 0.84 ± 0.084 under both readings. This rests on only 88–96 cells from 3 rats; 7–14 cells have curve r < 0.5, which "always stable" does not reflect. |
| hd-rates | not_reproduced | Cell 43: the background part holds (median 0.32–0.50 Hz), but only 66–71% of cells have peaks from 4.5 to 44 Hz, against the 90% required. No reading reproduces. |
| deep-hd-conjunctive | not_reproduced | Cell 45: layer II has 1 to 8 conjunctive cells under all 112 readings, so both the reproduced and partial outcomes are excluded. Layer VI (0.53–0.74) is also far from 0.28. |
| gridness-hd-continuous | reproduced | Cell 48: 98 to 141 conjunctive cells; the largest gap is at most 0.21 of the axis range on both axes, under 112 of 112 readings. |
| conj-tuning-similar | blocked: methods_underspecified | Cell 50: the t-test finds a difference in 96 of 112 readings, Mann-Whitney in 42 of 112. |
| cue-rotation-coherent | blocked: data_missing | Confirmed (section C). |
| speed | blocked: methods_underspecified | Cell 53: taking the best counting/significance reading for each method combination gives 119 reproduced, 327 partial and 2 not reproduced across the 448 combinations. |
| speed-slope-steeper | partially_reproduced | Cell 56: all 448 readings give ANOVA p ≤ 0.012 and grid steeper than head-direction (p ≤ 0.0084). Conjunctive against head-direction is never significant (p 0.06–0.99). |
| speed-intercept | not_reproduced | Cell 58: the positive-intercept fraction is in tolerance (0.982–0.998), but the low-speed rates are 0.94–1.90 Hz against 2.26–2.50 Hz, beyond 10% in all 896 rows. |

### B. Problems

1. **[affects a conclusion]** Cell 28, `grid-phase-orientation`. The notebook invents a "partially_reproduced" outcome ("which the protocol calls partially reproduced"). The criterion names none, and the claims-file header says a claim that holds under some readings and not others is methods_underspecified.

2. **[affects a conclusion]** Every HD-dependent claim, `classify`. With tens of thousands of samples, the Watson two-sample U2 is significant for almost every cell: 39 to 41 of 43 layer II cells (cell 30), median layer II U2 1.4. In practice the HD class is decided by the block correlation alone.
   - This follows the SOM as the claims file quotes it, so the outcomes stand. But the 9 layer II "HD cells" that sink `hd-layers` and `deep-hd-conjunctive` all come from two same-day files of rat 11265, at depths 3.20 and 3.25 mm.
   - No check of their tracking or LED separation was shown. Per-file LED separation ranges from 2.6 to 36 cm (cell 5), and the notebook never asks which files are the outliers or whether rat 11265's files are among them.

3. **[affects a conclusion]** `layer2-grid`, `grid-stable`, `speed`. Gridness above 0 is a lax criterion. In my synthetic test, 27.5% of 200 smoothed random-noise maps scored gridness > 0 under the first reading. That is consistent with the notebook finding 277–329 grid cells where the paper has 203. The fractions and grid classes are inflated relative to the paper whatever the implementation, and this is not discussed.

4. **[affects a conclusion]** Cells 11 and 19: the unit of counting is the cell-session. 584 cell-sessions with a depth reduce to 425 distinct (rat, depth, hemisphere, name) combinations, 99 of which appear in 2 to 7 files.
   - Fractions, ensembles (`hd-colocalized-distributed`: 18 of 28 ensembles from rat 11207 on consecutive days) and between-rat orientation pairs count the same neurons repeatedly.
   - Only `layer2-grid` gets a de-duplicated variant (cell 19, still out of tolerance).
   - Layer II is under-represented (71 against 108) while the deeper layers exceed table S1A. The sample's selection is undocumented.

5. **[does not affect a conclusion]** Cell 53, speed reading (b). The binomial sign test the criterion attaches to reading (b) is computed but never used in the outcome. The largest pure-HD p is 0.0015, above 0.001. The claim is methods_underspecified either way.

6. **[does not affect a conclusion]** Cell 28. Pairs are restricted to cells of the same layer, which is the author's choice. The criterion says only "pairs of grid cells recorded simultaneously".

7. **[does not affect a conclusion]** Positions are rescaled to exact spans of 100, 150 or 200 cm (cell 5), and the 19 circular files are about 11% too large. This affects the cm-based quantities: speed slopes, which bins fall below 3 cm/s, and spacing. It does not explain rates about 40% too low in `speed-intercept`.

8. **[does not affect a conclusion]** `smooth_positions` and `rate_map` filter and pool across the 600 s join between trials, where trial 2 is not re-centred (offsets 0.6–10 cm, cell 7). This adds a small blur to the pooled maps of 23 files.

9. **[does not affect a conclusion]** Cells 37, 39, 41, 43, 48 and 50 print no outcome line. The outcomes above are mine, derived from the printed tables.

Helper checks on synthetic inputs:
- `correlogram` matches a brute-force Pearson calculation to 2e-16.
- `grid_measures` on a hexagonal map gives gridness about 1.2–1.4, spacing about 40 cm for a true 40, and orientation shifting correctly with rotation (30° → 42° for an 11.5° rotation).
- The Watson two-sample U2 p-value is calibrated under the null (5.2% rejected at 0.05, 1.0% at 0.01).
- The one-sample U2 critical value rejects 4.5% at n = 8 and reproduces the paper's 0.18 at n = 7.
- `speed_bins` returns 5.00 cm/s for a constant 5 cm/s path and does not cross the trial join.

I found no misreading of the paper in the claims file. I spot-checked the table S1B arithmetic, the SOM gridness, HD, block-correlation and speed methods, and the angular-SD definition.

### C. What I could not check, and the blocked claims

- **spacing-dorsoventral and fieldsize-dorsoventral.** In the archive's dandiset and asset metadata (DANDI API), `variableMeasured` lists only ElectricalSeries, Position, Units, ElectrodeGroup, ProcessingModule, LFP and SpatialSeries, with no histology distance. The notebook reports that the units table holds only `histology`, `depth`, `hemisphere` and `unit_name`.
  - Electrode depth is not the SOM's distance, which is measured along the layer from the postrhinal border.
  - A within-rat test of spacing against depth could serve as a proxy for the sign of the correlation, but it is not the claim's measure. The near-border 35–40 cm, the ratio and the r values cannot be tested, especially since positions are rescaled. data_missing stands.
  - The notebook did not inspect the electrodes table: an `electrodes` table with x/y/z or location columns would have settled this.
- **cue-rotation-coherent.** All 118 assets carry the same session description, with no condition or cue field. Beyond the notebook's statement, cell 5 shows that no 100-cm-span file is circular: every circular file spans 200 cm. So the small-circle rotation sessions appear absent altogether. data_missing stands.
- **Outputs that would have let me check more:**
  - LED separation and the fraction of implausible LED geometry for rat 11265's files.
  - `hd-layers` and `deep-hd-conjunctive` recomputed without those two files.
  - A grid-class table for each rat and reading after de-duplicating cell-sessions.
  - The speed outcome with the sign test applied.
  - The gridness distribution under a shuffled-spike control, to judge the false-positive rate of gridness above 0 on these data.
  - Whether LED1 is the red LED (the files don't say).
  - Explicit outcome lines for cells 37 to 50.
