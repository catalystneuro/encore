Every question is taken up, the entry passes its check, all six notebooks run from a clean environment (01 is the longest at 12 minutes), and the handover is built in `executed/ebrains-q0fg-1x8-nagelhus-2023/handover/`. Nothing is committed or pushed, and I did not verify my own work.

An earlier run on these answers had been cancelled partway. It had already switched the code to the paper's rate-map method and started the object-vector analysis; I checked that code, finished it and re-ran everything. A second full run gave the same numbers.

### 1. How unvisited bins are smoothed (fig1c and the claims that use rate maps)
**Answer:** the paper's `calculateRateMap.m` computes the rate per bin, puts 0 in unvisited bins, then smooths. Time per position sample is capped at 0.1 s, and a spike counts at the last position sample at or before it. This one method now replaces the two I ran before, in every notebook.

| Claim | Before | Now |
|---|---|---|
| fig1c-object-tuned-fraction | blocked (methods underspecified) | **partially reproduced**: 18.7% of CA1 cells tuned (within tolerance, p = 6e-79 against controls), but the control level is 4.11% against 5.03% ± 0.5%. That is 9 of 219 against the paper's 11 of 219, which a binomial test does not tell apart (p = 0.64). |
| figs2e-within-trial-stability | blocked | **reproduced** (r = 0.41 and 0.42) |
| fig2-fraction-changed-no-o | blocked | **reproduced** (66.4% and 66.7%) |
| figs5l-without-positively-tuned | blocked | **reproduced** (bin 1 highest under both speed readings) |
| figs5m-without-object-tuned | blocked (depended on fig1c) | **reproduced** |
| fig1f-orientation-coverage | blocked (depended on fig1c) | **reproduced** |
| fig1d-field-distances | blocked (depended on fig1c) | **partially reproduced**: the largest distance (104 to 125 cm) is beyond the bound under every reading |
| fig1e-object-cells-and-object-vector-cells | blocked (depended on fig1c) | **partially reproduced**: no reading has all three values within tolerance |
| figs3f, fig2d-rate-overlap, figs2d-traces, figs5e, fig4e, fig6c, fig6d | blocked | still **blocked**: other readings, which these answers don't cover, still disagree |
| The other 23 rate-map claims (CA3 tuning, whole-trial changes, traces, decoders, distance tuning) | as before | **unchanged** (numbers updated) |

### 2. Where the 1 Hz field rule applies
**Answer:** the paper does not say, so both readings are allowed.
- fig1d, fig1e and figs4-object-traces now have the outcomes in the table above. figs4 is still **partially reproduced**, with trace cells at 6.1 to 9.8%.
- figs5ghi-fields-and-rates is still **not reproduced**.
- The two field readings give the same outcome for each of these claims.

### 3. ovs-method-extra-cells: the vector map's bins
**Answer:** 2 cm and 10° bins with smoothing of SD 1.5 bins, plus two readings of the distance range. The claim now runs, but it stays **blocked (methods underspecified)** for a different reason. The count depends on which fields decide the exclusion of cells before the criteria, and the claims file doesn't say:
- If a cell is excluded when any of its fields would leave the arena, the count is 9 to 15, never within 40 ± 4.
- If only when all of them would, the count is 34 to 53, within tolerance under 27 of 48 readings.
- Neither rule excludes the paper's 28.8% of cells.

I added this as a new question in `questions/ebrains-q0fg-1x8.yaml`, and added a finding that the paper's code lacks several of these analyses.

### 4. figs6l-sampling-thresholds
**Answer:** the paper does not say; the four combinations I already ran are now the criterion's readings. Still **reproduced**.

### 5. figs5f-random-partition
**Answer:** the shuffled timepoints are the 1 s spike-count windows, which was the reading I had run. The second reading no longer applies. Still **reproduced**.

### 6. figs7cd-number-of-words
**Answer:** the paper does not say; both readings are allowed and are now labelled w-a and w-b. Still **reproduced** (p = 0.94 and 0.85).

### 7. fig4h-population-vector-correlation
**Answer:** the paper does not say. I added the blanked-map readings, so four are now run. Still **reproduced** under all four.

### 8. fig7: the mean rate in spatial information
**Answer:** the paper does not say; both definitions are allowed and both are run.
- fig7-single-cell-properties was blocked (depended on fig1c) and is now **partially reproduced**. Spatial information does not correlate with distance tuning under either definition (r between -0.04 and 0, against -0.13). The other three correlations are within 0.05 of the printed values over the 1,189 cells.
- fig7-slope-variant was blocked and is now **partially reproduced**: two of its four correlations match.

### Totals
Of the 57 claims, 30 are reproduced, 7 partially reproduced, 7 not reproduced and 13 blocked. Eight of the blocked claims are blocked because the claims file's own readings still disagree.

Files changed:
- **Entry:** the six notebooks, `objcode.py`, `README.md` and `entry.yaml`.
- **Attempt record:** `attempts/ebrains-q0fg-1x8-nagelhus-2023-01.yaml`.
- **Questions:** `questions/ebrains-q0fg-1x8.yaml`, with the new question.
