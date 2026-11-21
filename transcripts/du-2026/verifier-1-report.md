**A. Outcomes** (33 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| synthetic-template-null | reproduced | 01 cell 4: median −0.0000023, median \|gain\| 0.0000092, which is below 0.03. The range −0.0000588 to 0.0000248 matches the paper exactly. |
| synthetic-signal-ordering | reproduced | 01 cell 6: weak 0.22451 and strong 0.37360, strictly increasing from template-only. |
| synthetic-pair-breaking | reproduced | 01 cell 8: 10/10 seeds above both controls. Replacement mean −0.3486, permutation mean −0.3663. |
| link-development-sample | reproduced | 02 cell 10: 9 dates, 6,750 usable trials, all 18 sessions have 375. |
| link-neural-only-r2 | reproduced | 02 cell 12: CO 0.3077, RD 0.3129. |
| link-context-ladder-gain | reproduced | 02 cell 14: gain falls at every step for both tasks, and 10/10 values are within tolerance (all equal the paper to 4 decimals). |
| link-context-only-r2 | reproduced | 02 cell 16: plus history 0.6617/0.6839; phase only 0.0084/0.0055, both below 0.02. |
| link-phase-only-replacement | reproduced | 02 cell 18: RD mean 0.10498, positive. |
| link-task-contrast-by-context | reproduced | 02 cell 20: signs +, −, −, + as stated. Geometry by phase (0.0015) is near zero under both readings: its CI contains 0, and it is smaller in absolute value than the direction (0.0155) and additive (0.0110) contrasts. |
| nested-geometry-gain | reproduced | 02 cell 22: SBP 0.02009 (18/18 positive), TCR 0.01155 (17/18). Date CIs 0.01586–0.02401 and 0.00711–0.01591, close to Table 1. |
| nested-history-gain | reproduced | 02 cell 24: 0.00873 (17/18), 0.00420 (16/18), each below its geometry mean. |
| nested-replacement-negative | reproduced | 02 cell 26: all four negative, 4/4 within tolerance. |
| replacement-source-diagnostics | reproduced | 02 cell 28: minimum eligible sources 5, median maximum reuse 3, maximum 4, self-replacement error 0. |
| permutation-negative | reproduced | 02 cell 30, reading (a): 18/18 negative, mean −0.01418. Reading (b) also passes (36/36, −0.01387). |
| replacement-penalty-distance | reproduced | 02 cell 32: 8 positive and 10 negative correlations, and the date CI −0.0204 to 0.0301 contains 0. Both readings hold. |
| replacement-ranks-lower | reproduced | 02 cell 34: ranks 1–5 and all five random draws are below the correct-pair mean, for SBP and TCR. |
| practical-mse-reduction | reproduced | 02 cell 36: 6/6 within tolerance (4.92%, 0.01407, 0.01372, 2.72%, 2.83%, 1.31%). |
| representative-trial | reproduced | 02 cell 38: the ninth session in gain order is 2022-09-21 RD. Its median trial is 123 under readings (a) and (b). The other session reading (earlier date of the two middle sessions) gives 2021-10-15 RD. |
| confirm-geometry-gain | reproduced | 05 cell 6: 20/20 positive; 0.02158 (CO 0.02104, RD 0.02213). The re-run selection rule gives the same 20 assets as the frozen manifest, and the paper's gate passes. |
| confirm-history-contraction | reproduced | 05 cell 8: 0.00755 (CO 0.00670, RD 0.00840), 19/20 positive, below the geometry mean. |
| confirm-replacement | reproduced | 05 cell 10: −0.00771; correct-pair gain above replacement in 20/20 sessions and in both task means. |
| confirm-table1-values | reproduced | 05 cell 12: −0.00498, 4.761%, 2.047%. |
| rtt-data | reproduced | 06 cell 4: 1080 blocks, 130 units, 810/270 split, 21 bins per block. |
| rtt-gain | reproduced | 06 cell 6: gain 0.06846 (positive) and replacement −0.02297 (negative); all 7 other values within tolerance. |
| rff-rtt | reproduced | 06 cell 8: 0.01685, 0.01501, 0.01491; all positive and inside the widened range. |
| rff-link | reproduced | 02 cell 42: CO and RD positive under every map. Reading (a) 0.00310–0.00404 is inside the range; history 0.00111–0.00142 is inside. Reading (b) fails (0.00269 is outside), but one reading suffices. |
| estimator-family-link | reproduced | 03 cell 4: under the code's setting (nonlinear-context reading (a)), every CO, RD and 18-session mean is positive for both families. Reading (b), all 27 nonlinear-context settings, was not run; the criterion needs only one reading. |
| estimator-family-nlb | reproduced (MC_RTT part only) | 06 cell 10: block 0.06901 and nonlinear context 0.04619, both positive. The criterion makes the outcome depend only on MC_RTT; the MC_Maze half of the statement is untested. |
| temporal-offset | reproduced | 04 cell 5: under both estimators, gain at 120 ms is below gain at 0 ms for CO and RD. Under the fully nested reading only RD-change reading (b) holds (RD−CO goes from +0.00241 to −0.00024 and −0.00061); under the evaluate_decoders_nested reading, (a) and (b) both hold. |
| split-seed-stability | reproduced | 02 cell 40: 6/6 positive and within tolerance. |
| context-capacity-contrast | reproduced | 04 cell 7: quadratic-plus-history contrast positive for SBP and TCR under both estimators. Only TCR shows a "changed" contrast: its interval excludes 0 under quadratic geometry but not under linear. SBP does not change. |
| maze-gain | blocked (data_missing) | DANDI:000139 is not one of this attempt's datasets. The API shows 000129 holds only sub-Indy files (2 assets) and 001201 only sub-Monkey-N (312); the MC_Maze file exists only in 000139 0.220113.0408. No part can be tested. |
| rff-maze | blocked (data_missing) | Same as maze-gain. |

Totals: 31 reproduced, 2 blocked.

**B. Problems**

1. [does not affect a conclusion] 02 cell 38. The "position among 113 held-out trials" (39 and 75) is an index into `test_indices` in `train_test_split`'s shuffled order, so it is not a meaningful position for reading (c). Readings (a) and (b) already give 123.
2. [does not affect a conclusion] 04 cell 3. The context feature counts 141/351/151/361 are a hard-coded string, not computed. I checked `build_link_dataset` on a synthetic session and it gives 9/81/87/141/151/351/361, matching Methods 4.4.
3. [does not affect a conclusion] `_BlockRidge` solves with cholesky where the release uses lsqr. This is stated in the code, and one session differs by 5e-7. A different solver could in principle tip a penalty-grid tie, but cannot plausibly flip the positive means in 03 cell 4.
4. [does not affect a conclusion] The confirmation results depend strongly on the split seed (05 cells 6–12). Under seeds +1000 to +4000, the combined geometry mean is 0.0148–0.0207, the history mean 0.0034–0.0082, and the plus-history replacement −0.0047 to −0.0146. At several of these seeds the values fall outside the 10% tolerances. The criterion fixes seed 20260726, so the outcomes stand, but the exact match does not hold across splits. The development-set gains are much more stable (02 cells 22 and 24).
5. [does not affect a conclusion] 02 cell 4 shows `velocity[t]` equals `position[t+1] − position[t]` (correlation 1.000, SD ratio 1.00). The outcome at bin b therefore uses position at b+1, after both histories end. No future values enter the predictors: I checked that the neural and position histories end at b−1 (and at b−7 for the 120 ms offset). This is consistent with the paper's caveat on post hoc velocity.
6. [does not affect a conclusion] 02 cell 38 sorts sessions by (gain, date, task) and takes index (n−1)//2 as "ninth in gain order". That matches the claims file's first reading.

No leakage found. In `fully_nested`, every scaler, penalty and coefficient is fit on outer-training trials (or OOF folds). Replacement scales come from training trials. Test Y enters only scoring and Var(Y). All numbers derive from the streamed NWB arrays or from the generator. The only external input is the frozen confirmation manifest, which the claims file names, and the notebook re-derives it exactly from asset metadata. The helpers behaved as documented on synthetic inputs:
- interior ranks
- octants
- window and drop rule (count 33 kept, 32 dropped)
- neural, position and behaviour alignment
- tie rule to the lower index
- permutations with no fixed points within condition
- gain at 0 and 1
- Spearman
- date bootstrap

The paper states no chance levels, so there are none to compare.

**C. What I could not check**

- Whether the ports match the release code line for line (release not available to me). Values that match the paper to 4–7 digits everywhere strongly suggest they do. A notebook cell running one release function next to its port on one session would settle it.
- confirm-replacement under seeds +1000 to +4000. The notebook prints only how many replacement gains are positive, not how many sessions have correct-pair gain above replacement.
- estimator-family-link nonlinear-context reading (b), the 27 settings of Methods 4.6 (not run).
- The MC_Maze part of estimator-family-nlb, maze-gain and rff-maze (need DANDI:000139).
- The notebook's statement that later 001201 versions list identical assets has no supporting output.
