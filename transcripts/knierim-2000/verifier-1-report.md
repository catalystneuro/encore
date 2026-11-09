## Verifier report, round 1: Knierim, McNaughton & Poe (2000), dandiset 001754 @ 0.260728.1352

The claims file has 10 claims. The notebook judges six against the data and blocks four.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| si-comparable-to-preflight | partially_reproduced | Cell 25: under M-a, neither preflight epoch shows a difference (p 0.88 and 0.66). Flight mean is 1.377 against 1.13 ± 0.09; preflight is 1.320 and 1.284 against 1.12 ± 0.08, so no reading puts both means within tolerance. M-b cannot be run on both sides (no preflight position), so as the criterion says it is not judged. |
| si-rat1-fd9-vs-preflight | blocked (methods_underspecified) | Cell 27: the readings disagree. Against preflight ES1 p = 0.50; against preflight MC1 p = 0.0055, with flight higher. Under S-a both preflight epochs are candidates, so the criterion blocks the claim. |
| si-rat3-fd4-vs-preflight | reproduced | Cell 29: no difference under either reading (p 0.28 and 0.77). With the ES1 preflight reading both means are within tolerance (1.231 against 1.12 ± 0.27; 1.518 against 1.48 ± 0.11). Cell counts are well off (11 flight against 7; 38 against 24), but the criterion's rule does not use counts. |
| flight-spatial-code | blocked (methods_underspecified) | Cell 32: the dependencies are partial, blocked and reproduced. If rat 1 were reproduced or partial the outcome would be partial; if not reproduced, not_reproduced. The others do not decide it, so the criterion blocks it. |
| fd4-abnormal-selectivity | partially_reproduced | Cell 34: Rat 2's FD4 information is significantly lower than preflight under both readings (p 0.0006 and 0.0015). Rat 1's is lower under neither (p 0.077 and 0.36). The rule gives "holds for one rat". This rests entirely on Rat 2's FD4 maps; see B2. |
| fig3-stability-across-sessions | blocked (methods_underspecified), possibly not_reproduced | Cell 36: under M-b, (a) 6 of 16 and (b) 1 of 16 cells keep their field. Cell 37: under M-a, (a) 6 of 11 (more than half) and (b) 5 of 11. The readings disagree only because M-a was admitted. The check that admits M-a does not test the criterion's condition (B1). If the condition fails, M-a is not run and the outcome is not_reproduced. |
| direction-selectivity | blocked (methods_underspecified) | Cell 39: position exists only at spike times (gaps up to 12.7 s), there is one occupancy map per epoch with no direction, and no file gives the track layout. The criterion blocks the claim when these are missing. In substance this is missing data, but the criterion fixes the label. |
| theta-normal | blocked (data_missing) | No ElectricalSeries or LFP in any file (cell 3). I confirmed this on the archive: every asset's `variableMeasured` is Units, ElectrodeGroup, SpatialSeries, ProcessingModule and Position, and the dandiset totals 32 MB in 8 files. No part can be tested. |
| ripples-normal | blocked (data_missing) | Same as theta-normal: there is no pouch or baseline EEG in the archive. No part can be tested. |
| three-orthogonal-surfaces | blocked (methods_underspecified) | Part (i) depends on two blocked claims, and the possible outcomes are not_reproduced or partially_reproduced, so the claim is undecided. Part (ii) cannot be tested at all: the position is one 2-D pixel frame with no track outline. If fig3 turns out not_reproduced (B1), this claim becomes not_reproduced. |

### B. Problems

1. **[affects a conclusion]** Cell 37, `owner` / `pairing_ok`: the check does not test the criterion's condition. The criterion admits M-a only when each map is tied to one unit and no unit to two maps.
   - The code pairs each unit with its best-matching map, and when two units pick the same map it silently keeps the higher match. That conflict is exactly what the condition is meant to catch.
   - The check is also never applied to the session 3 maps across all units.
   - I replicated the logic on a synthetic case where two units share a best map: `pairing_ok` comes out True.
   - The risk is real here: 47 units compete for 19 ES1 maps, and TT8 has at least 5 units for 3 to 4 maps.
   - Which way this goes decides whether fig3 is blocked or not_reproduced, and so the outcome of three-orthogonal-surfaces too.
2. **[affects a conclusion]** Cells 19–20 and 34: the notebook's own time-shift check finds no sign that the position trace in Rat 2's FD4 ES window is Rat 2's (0 of 17 units; 1 of 17 for Rat 1). The deposited maps came from the same shared tracker. So the low FD4 information for Rat 2, the only support for fd4-abnormal-selectivity, may come from tracking rather than firing. The notebook notes this caveat but still judges the claim.
3. **[affects a conclusion, unverified]** `ma_table`: M-a counts every deposited map as a cell, including maps with `cell_number` −1, which the table describes as "not a per-cell map" (14 to 33 per file outside Rat3 FD4). Their file names are printed only for Rat3 FD4 ES. If some are combined or multi-unit maps, they shift the counts and means in every spatial information comparison. Counts are off throughout (Rat3 preflight 38 against 24; Rat3 FD4 11 against 7), which is consistent with selection differing from the paper's.
4. **[does not affect a conclusion]** `mb_maps`: spikes that fall in bins with zero deposited occupancy (33 to 1,188 per epoch) are silently dropped. M-b is only a variant for the spatial information claims, and fig3 under M-b fails by a wide margin either way.
5. **[does not affect a conclusion]** Cell 36: M-b maps are unsmoothed at 4 px with very few spikes per bin, so reading (b), "peak in field", nearly always fails (1 of 16). This follows from the criterion's definition, not from a choice by the author.
6. **[does not affect a conclusion]** Rat 2's preflight units share no tetrode with its flight units (cell 7). The file may be assigned to the wrong rat; it cannot be checked from the data, and the notebook says so.
7. **[does not affect a conclusion]** Things I checked and found correct:
   - `skaggs_info` and `peak_in_field` pass their synthetic tests (cell 15).
   - `compare` is a two-sided Mann-Whitney test at 0.05, as the claims file reads it.
   - The 1/11 chance level of the shift test is correct for 10 shifts.
   - The paper states no chance level, so there is nothing to compare.
   - No training/test leakage applies.
8. **Claims file:** I found no misreading of the paper. The fig3 statement ("fourth cell lost its field", "a few other cells gained a field") matches the Fig. 3 legend. Fixing rat 2's preflight cells to the rectangular track is an inference from Fig. 2b, but the criterion runs both preflight epochs anyway.

### C. What I could not check, and the output that would settle it

- **Fig3 pairing (B1):** for every ES1 and ES2 map of Rat3 FD4, the best-matching unit and its correlation, plus every unit's best ES1 and ES2 map. Flag any map that is best for more than one unit and any unit that is best for more than one map.
- **M-a selection (B3):** `source_file` and `cell_number` of every map counted as active, per file. That would show whether maps with `cell_number` −1 are per-cell maps.
- **Rat 2 FD4 position (B2):** the time-shift contrast with Rat 2's units on the Rat 1 file's trace versus the Rat 2 file's trace in the same ES window, at the timestamps where they differ.
- **Cell counts:** for Rat3 FD4 ES1, which of the 11 active maps are place cells in the paper's sense. That would show whether some selection reproduces the paper's 7 cells.
- **Smoothing:** the kernel of the deposited maps is unknown and cannot be recovered from the files. I did not re-run any computation; every number above is taken from the notebook's outputs.
