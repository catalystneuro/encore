I've updated the attempt for all five answers. One outcome changed: `grid-phase-orientation` went from blocked to partially reproduced. Every other affected claim keeps its earlier outcome under the updated criteria.

**Runs.** I re-locked the entry and the notebook passes `entry.py run` from a clean environment in 230 s. `entry.py all` stops at its check step with 18 errors. All 18 are on the deprecated `-01` record, which has no outcomes for the claims added since. HEAD gives the same 18 errors without my changes, and the protocol says an earlier record stays as it was, so I left it alone and ran the run step separately. No error concerns `-02` or the entry. `entry.py handover` built `executed/000582-sargolini-2006/handover/`. Nothing is committed.

**Q1: a peak's centre and radius (O3).** The helper now runs both centres (pixel of highest correlation, centroid) and both radii (disc of the same area, largest distance to one of its pixels). They apply to the central peak too, and the same centre sets spacing and orientation. In one pair of readings the radius is never used, so I run that pair once. That gives 56 grid readings (32 before) and 112 for conjunctive cells (64 before). Every claim that uses the grid class was re-run.

| Claim | Before | Now |
|---|---|---|
| `layer2-grid` | partially reproduced | partially reproduced (order holds under all 56; layer II within tolerance under 32 of 56, deeper layers under none) |
| `grid-all-layers` | reproduced | reproduced |
| `gridness-range-similar` | blocked, methods_underspecified | same (Mann-Whitney finds a difference under 8 of 56, Kruskal-Wallis under 53 of 56) |
| `grid-stable` | blocked, methods_underspecified | same (84 combinations partially reproduced, 364 not) |
| `deep-hd-conjunctive` | not reproduced | not reproduced (layer II has conjunctive cells under every reading) |
| `gridness-hd-continuous` | reproduced | reproduced (largest gridness gap now 0.209 of the range, still below a quarter) |
| `conj-tuning-similar` | blocked, methods_underspecified | same (t-test 98 of 112, Mann-Whitney 42 of 112) |
| `hd-colocalized-distributed` | reproduced | reproduced |
| `hd-rates` | not reproduced | not reproduced |

**Q2: angular standard deviation (`hd-tuning-breadth-layers`).** The answer names both of Batschelet's formulas as readings, which the attempt already ran. Before and after: blocked, methods_underspecified. The U2 tests find almost no layer difference (ANOVA 0, Kruskal-Wallis 10 of 116), while the angular-deviation tests often do (35 to 61 of 116).

**Q3: how to read the `speed` criterion.** The counting and significance readings now count at their best, while the method details must agree. Taking the best reading for each of the 448 method combinations gives 119 reproduced, 327 partially reproduced and 2 not reproduced.
- `speed`: before blocked, methods_underspecified; now the same, because the method details disagree.
- `speed-slope-steeper`: before blocked, still blocked because it depends on `speed`. On its own it would be partially reproduced under all 448 combinations.
- `speed-intercept`: before blocked, still blocked because it depends on `speed`. On its own it would be not reproduced under every combination.

**Q4: which cells count in `hd-with-grid-colocalized`.** The answer confirmed pure head-direction cells found with another cell, as I had assumed. It added "a pure grid cell" as a second reading of that other cell. Before and after: blocked, methods_underspecified.
- **By file:** 75% to 91% of files hold a grid or conjunctive cell, and 47% to 60% a pure grid cell.
- **By tetrode:** 36% to 48% hold a grid or conjunctive cell, and 14.5% to 19.4% a pure grid cell, below half under every reading.

**Q5: the comparison pool and "every reading" in `grid-phase-orientation`.** Both pools (other rats in the same layer, or in any layer) are now readings, and "every reading" covers O1 to O3.
- **Before:** blocked, methods_underspecified.
- **Now:** partially reproduced.
- **Phase:** holds in every layer under all 224 readings.
- **Orientation:** holds in layers II and III under every reading, but in layer V only under 41 or 42 of 56 readings and in layer VI under 23 or 35 of 56, depending on the pool.

The criterion names no outcome below reproduced. I applied the protocol's definition of partially reproduced, the effect holding only in part, and said so in the notebook and in the record. The verifier may weigh in on that choice.

I updated the notebook's header, criterion and conclusion cells, the summary, the README and the attempt record. Each affected claim's notes say what the answer changed. During checking I also fixed a grouping step in the `speed` cell that could mix rows; the counts did not change.
