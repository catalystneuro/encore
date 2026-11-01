**Verifier report, round 3: Semenov et al. 2025 (attempt 001048-semenov-2025-01)**

The claims file has 20 claims, and the attempt record gives an outcome for each of the 20. Only one outcome carries a `proposed` change: fig6-sine-less-than-pulse. That claim is the only one reviewed here.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig6-sine-less-than-pulse | blocked, metadata_insufficient | **Yes** | — | See below. |

**The numbers come from the data (cells 71–73).** Every value in the proposed reason matches a printed output:
- **Pulse mean 13.3 to 17.4 % per kV/cm:** cell 73 gives 16.9 (6 × 6 boxes), 17.4 (12 × 12) and 13.3 (20 × 20).
- **Cells with p < 0.0001 in both ROIs, 1 to 4:** cell 73 gives 1, 4 and 4 under the signed regression.
- **Direction in 15 to 18 of 18 ROIs:** cell 72 gives 18 of 18 under the signed regression (reading a) and 15 of 18 per cycle (reading b). Cell 73 gives 17 and 18 for the other box sizes.

The cell selection in cell 71 takes 9 cells, each with a pulse session and sessions modulated at 100 Hz, without TTX. The rule is fixed in advance (cell 64), not picked for its result. The box-size variant reuses the same ROI centres. None of the variants brings the values nearer the paper's, so the variant was not chosen to produce a result.

**The criterion is applied as written, with one exception.** Cell 72 tests all seven parts of the criterion under O5 a/b, O6 2/4 ms and slope readings a/b. `holds` is False in all 8 rows.
- The exception is reading (b). The criterion says "per-cycle peak-to-peak amplitude on the cycle's peak field", but the notebook regresses half the peak-to-peak amplitude (cell 70, cell 71 line `cp.p2p / 2`). The record's deviations do not list this.
- With the full peak-to-peak amplitude, the reading-(b) sine means would roughly double, to about 13.7 to 16.2. The ratio would rise to about 79 to 93 %. The criterion would still fail, so the outcome does not change. The halving should be added to the deviations or removed.
- The proposed reason's count of "1 to 4" cells covers only the signed regression. Under reading (b) the count is 0 in every row of cell 72. This makes the reason incomplete, but it does not change its conclusion.

**Why I agree with blocking:**
1. **The values rest on information the dandiset lacks.** Six of the seven parts are numbers measured in the paper's hand-drawn ROIs, and 001274 holds no ROIs. The paper confirms the ROIs were drawn over the most polarized regions, with no size given (its Figure 5 legend and Methods). Cell 73 shows that the means and the significant-cell count change with box size.
2. **The fields are assumed as well.** Both sensitivities are divided by the paper's nominal fields (257 V/cm for the pulse, 136 V/cm for the sine). These are scaled by generator voltage because 001274 gives no measured amplitudes (record deviations; cell 71). A wrong field scales every value in proportion. This is a second missing-metadata reason. The record's deviations name it, but the proposed reason does not.
3. **The nine cells are inferred.** The files do not label them as the paper's cells.
4. **A partial outcome cannot rest on the direction.** "Sine below pulse in every ROI" fails under reading (b), at 15 of 18 in cell 72, so no part of the criterion holds under every reading. A partially reproduced outcome would rest on one reading of one part.
5. **It matches fig4-pooled-time-constants.** That claim was blocked as metadata_insufficient in cell 69, even though all its variants also miss (0 of 4 values within the SEM in cell 67). The same treatment fixes the inconsistency I raised in round 2.

**Not reproduced was considered.** The pulse mean stays far below 28 ± 2.5 under every box size, and smaller boxes do not raise it towards 28. The paper's ROIs could still be smaller than 6 × 6 or placed differently. The fields are also uncalibrated. So a failure of the paper is not shown, and blocked fits better than not reproduced.

**The claims file reads the paper correctly here.** The paper text confirms the 15 to 47 % range with a mean of 28 %, the 1.5 to 28.4 % range with a mean of 11.8 %, the 42 % ratio, "smaller in every ROI", and p < 0.01 % for both ROIs in eight cells.
