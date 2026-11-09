**A. Outcomes** (50 claims in the claims file; the notebook tests 43 and treats 7 as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig1h-lick-ratio-improves | reproduced | Under reading (b), 11 of 11 mice improve, and 11 of 11 keep a positive next-day ratio (cell 10). Under reading (a), 8 of 11 do. |
| place-cell-fraction | not_reproduced | 577.1 place cells (expected 459 ± 45.9) and 60.0% (expected 48.5 ± 4.85). Cells imaged, 969.5, is within tolerance (cell 12). |
| remap-category-fractions | not_reproduced | Reading (a): disappearing 8.6, appearing 4.9 and far 17.9 are outside tolerance; TR and near match. Reading (b) is worse, with near at 1.2 (cell 14). |
| ed2cd-switch-remapping-intermediate | reproduced | All six orderings hold at Holm p < 0.05 with both diagonal bands (cell 63). |
| ed2f-teleport-distance | reproduced | 6.1% before (6.7 ± 0.67) and 6.8% after (7.5 ± 0.75; only 0.05 inside the bound). 6762 RR cells tested, against 5979 (cell 39). |
| fig2e-rr-remapping-above-chance | reproduced | On day 3, 8 of 11 bins exceed the shuffle and the above-chance fraction is 0.158. The remapping-cell counts, 1465 and 1500, are outside 1082 and 1153 ± 10% (cell 25). |
| fig2h-rr-remapping-grows | reproduced | Pooled regression slope 0.018, p = 0.008. Logit mixed model slope 0.153, p = 0.003 (cell 27). |
| fig2eg-mean-rr-position-after-reward | reproduced | 0.385 rad [0.261, 0.508] on day 3 and 0.321 [0.238, 0.404] on day 14, both within tolerance. n is 676 and 850, against 453 and 645 (cell 29). |
| fig2i-rr-remapping-spans-track | reproduced | On day 14 the fraction is positive at every distance from 10 to 190 cm (cell 31). See B12. |
| ed2jl-rr-remapping-beyond-50cm | not_reproduced | The criterion requires the expected counts: 1197 and 1060 are outside 888 ± 89 and 795 ± 80. The means (1.315, 1.360), the intervals and the positive fractions do hold (cell 33). |
| ed2m-more-fields-after-reward | partially_reproduced | Day 3 is significant from 10 to 50 cm. Day 14 fails at 70 cm (p = 0.007) and 80 cm (cell 35). |
| ed2n-far-remapping-no-increase | reproduced | Slope 0.0047, p = 0.175 (cell 37). |
| rr-cell-fractions | not_reproduced | Methods reading: RR all days 14.6 (lower bound 14.67), day 14 17.1, and non-RR 14.3 or 13.9 are outside tolerance. Day 3 and unclassified match (cell 16). |
| ed2pq-rr-reward-aligned-correlation | reproduced | All four rank-sum tests go in the stated direction with p ≈ 0. The counts (6762, 9442, 6417) are 13–49% above the paper's (cell 22). |
| fig3b-decode-rr-position | blocked (other) | Not run because of run time; the data are in the archive (see C). |
| fig3c-decode-range | blocked (other) | Depends on fig3b. |
| fig4c-rr-sequences-preserved | reproduced | 75 of 77 sessions (cell 42). |
| fig4f-tr-sequences-preserved | reproduced | 76 of 77 sessions (cell 44). |
| fig4i-nonrr-sequences-not-preserved | reproduced | 62 of 77 sessions, against 61 ± 6.1 (cell 46). |
| ed5a-tr-fewer-across-environments | not_reproduced | Friedman p = 1.6e-4, but day 8 against day 10 has Holm p = 0.073, and day 8 is 10.5% against 8.4 ± 0.84. The direction holds (cell 18). |
| ed5f-rr-no-decrease-across-environments | reproduced | No post hoc test shows day 8 lower; day 8 median is 15.2 (cell 20). |
| fig4j-rr-overrepresent-reward | not_reproduced | Region runs from −50 to +90 cm (+85 using bin centres), against +70 ± 10. The densest bin, 10–20 cm, does fit. No single day fits either (cell 49). |
| fig4m-rr-density-near-reward-grows | reproduced | Raw: near p = 3.6e-5, far p = 0.083. Logit: near p = 1.9e-4, far p = 0.062. The logit fits gave convergence warnings (cell 51). |
| fig4no-licking-speed-increase | reproduced | Lick rate p = 1e-4. Speed p = 0.012 near and p = 3e-6 far (cell 53). |
| fig4p-lick-precision-sequence-precision | reproduced | Holds under reading (a): p = 0.003 before, 0.042 after. Reading (b) fails after the switch (p = 0.067) (cell 55). |
| ed4hij-sequence-variance-decreases | not_reproduced | RR variance slope −0.012, p = 0.069. The lick-variance and mean-position parts do hold (cell 57). |
| fig4qr-tr-track-ends | reproduced | Density at the track ends is 0.0103, against a uniform level of 0.0047. Far-from-ends slope: p = 0.005 raw, 0.010 logit (cell 59). |
| ed4l-disappearing-decrease | not_reproduced | Disappearing far from reward has p = 0.21. Disappearing near (p = 0.040) and the four null results hold (cell 61). |
| ed5-teleport-fractions | blocked (other) | Not attempted; the data are present (cell 6 lists the 47 sessions imaged through the teleport). |
| fig5b-rr-remain-rr-increases | reproduced | Slope +0.021, p = 0.002 (cell 67). |
| fig5d-nontr-to-rr-increases | not_reproduced | Slope +0.007, p = 0.137 (cell 69). |
| fig5f-nonpc-to-rr-increases | not_reproduced | Slope +0.006, p = 0.20 (cell 71). |
| fig5h-tr-to-rr-constant | reproduced | p = 0.57 (cell 73). |
| fig5i-rr-to-tr-decreases | reproduced (provisional) | Slope −0.016, p = 0.027, but the fit's Hessian is not positive definite (cell 75; see B2). |
| fig5jkl-tr-no-recruitment | reproduced | No positive slope: p = 0.35, 0.52, 0.79 (cell 77). |
| ed6a-rr-near-reward-stable | reproduced | Both readings agree for RR and for TR. The followed counts, 3407 and 5217, are outside 2294 and 3408 (cell 79). |
| ed6c-rr-shift-toward-reward | not_reproduced | n = 577 is within tolerance, but the slope is −0.095 with p = 0.080 (cell 81). |
| ed6-across-day-drift | reproduced | Across-day medians are below within-day medians under both readings (cell 83). |
| ed7-no-anatomical-bias | reproduced (ML/AP only) | 2 and 0 significant mice or planes, within the limits under either axis mapping. The depth part is blocked (data_missing) and was not run (cell 85). |
| fig6e-rr-prefer-reward | not_reproduced | 5 of 11 under reading (a) and 7 of 11 under (b), against 9 ± 1. Medians are above 0 in 10 of 11 mice. Trial-set days match the paper for every mouse (cell 88). |
| ed8k-rr-prefer-reward-after-switch | reproduced | 8 of 11 under both readings; days per mouse match the legend (cell 90). |
| ed8df-time-warp-speed-mse | reproduced | Warped below raw, p = 9e-13. After above before, p = 5e-4. The n is 41 and 18 sets, against the paper's 61 (cell 92). |
| glm-well-fit-cells | blocked (too_large) | Not run; the data are present. |
| fig7de-glm-top-predictors | blocked (too_large) | Depends on the GLM. |
| fig8e-rr-remap-precedes-behavior | blocked (other) | Not attempted; the data are present. |
| ed10-appearing-remap-later | blocked (other) | Not attempted. |
| ed3d-single-field-increases | not_reproduced | All slopes are ≤ 0 with p ≥ 0.24 (cell 95). |
| ed3fg-fields-remap-independently | not_reproduced | Significant on day 5 (p = 0.007) and day 14 (p = 0.036). n is 103 on day 3 against 31, and 153 on day 8 against 20 (cell 97). |
| ed3mo-appearing-late-backward | reproduced | All six tests pass at the legend's levels. The RR primary fields number 6328, against 2368 (cell 99). |
| ed3p-shift-follows-reward-direction | reproduced | All four subpopulations reach p = 0.0099, the smallest value 100 permutations allow (cell 101). |

**Totals:** 28 reproduced, 1 partially reproduced, 14 not reproduced, 7 blocked.

**B. Problems**

1. **[affects a conclusion]** `sosa.spatial_info_shuffle` / cell 12: about 25% too many place cells (60% against 48.5%), and the cause is never found.
   - The excess carries into every pooled count: RR, TR and non-RR cells, remapping cells, and the ed6a followed cells.
   - It also deflates the category fractions. That probably drives remap-category-fractions, rr-cell-fractions, ed2jl and fig4j.
   - Nothing tests the cause. One untested difference: each shuffle applies the same per-trial offsets to all cells, whereas the Methods say position is permuted "relative to the timeseries of each cell". OASIS tau = 0.7 is another candidate.
   - Synthetic checks of `_si`, `pop_shuffle_p` and `xcorr_same` (against `scipy.signal.correlate`) found no bug. A synthetic place cell came out significant and noise cells did not.
2. **[affects a conclusion]** `mixed` (cell 8) never checks convergence.
   - The fig5i fit reports a non-positive-definite Hessian and a failed gradient, so its p = 0.027 is not reliable.
   - Fits in cells 51 and 57 report failed gradients too. Since stderr is interleaved, the failing fit cannot be identified, though cell 51's warnings come where the logit fits run.
3. **[affects a conclusion]** Cell 93: fields are found on 10 cm binned data instead of raw activity. The notebook states this deviation, but it is not a reasonable one here.
   - It gives about 3× the paper's two-field cells (103 vs 31; 153 vs 20) and 2.7× the RR primary fields (6328 vs 2368).
   - ed3d and ed3fg fail on these cell sets; ed3mo and ed3p pass on sets that are not the paper's.
   - No run uses the Methods' unbinned reading.
4. **[affects a conclusion]** Cell 64: cross-day matching is the notebook's own. It uses a per-pair IoU threshold and a rigid phase-correlation shift, both stated assumptions; the paper's threshold is "for each dataset", which may mean per mouse. No alternative was run, and fig5d/fig5f and ed6c depend on it.
5. **[does not affect a conclusion]** `omission_trials` (cell 86): an omission is taken to be an unrewarded trial with a lick in the zone. This is an assumption, but the qualifying trial sets per mouse match both legends exactly.
6. **[does not affect a conclusion]** Cell 92: the MSE tests use 41 before-switch sets and 18 paired sessions, against the legend's 61 sessions. The 77-session variant agrees.
7. **[does not affect a conclusion]** Cell 49: fig4j limits are taken from outer bin edges. With bin centres the upper limit is still out (85 against ≤ 80).
8. **[does not affect a conclusion]** `circ_bin_index(code_bins=True)`: the code variant has 45 centres with a 2π/44 step, but bin 44 is empty (positions fill only 44 bins). The 0–44 roll in `above_chance` therefore mixes in a centre beyond π. This touches variants only.
9. **[does not affect a conclusion]** `rr_xcorr`: it takes the largest cross-correlation among the lags that beat the shuffle, not the global peak, so it may admit slightly more RR cells.
10. **[does not affect a conclusion]** Cell 12: the "mean over mice of per-mouse means" variant equals the session mean by construction, since every mouse has 7 switch sessions.
11. **[does not affect a conclusion]** Cell 102: fig3b/c are labelled too_large, but the estimate is about 78 minutes of fitting on data that are in the archive. The real reason is run time ("other"). The fig8e/ed10 and ed5-teleport data are present too, so all of these are testable.
12. **Claims file, reported not corrected.**
    - ed8df: the criterion restricts the MSE tests to the fig6e trial sets. The Extended Data Fig. 8d,f legend has 61 sessions and marks the Fig. 6 subset with black edges, so the MSE tests use more sessions than that.
    - fig2i: the statistic sums positive excess over 11 bins, so it is biased above 0. "Positive at every distance" is therefore a weak test.
    - Header: it lists per-ROI z-stack depth estimates among the variables used. The DANDI asset metadata shows only TwoPhotonSeries and PlaneSegmentation.

**C. What I could not check**

- **Version choice.** I could not confirm from content that the cited version is broken. The API shows all 152 asset IDs changed between 0.250406.0045 and 0.251124.0550, and 143 sizes differ, which fits a re-upload.
- **Depth and matching data.** Without opening the files I could not tell whether they hold depth or cross-day matching data. A printed HDF5 group listing for one day-14 file would settle it.
- **Cause of the place-cell excess.** These outputs would help:
  - the per-set SI threshold against the distribution of cell SI;
  - the place-cell fraction with independent per-cell shuffle offsets;
  - the fraction with OASIS tau = 1.0.
- **Mixed-model reliability.** For each fit: `fit.converged`, the random-effect variance, and an OLS or cluster-robust comparison.
- **Field detection.** Per-day counts of cells with 1 and 2 fields, compared with Extended Data Fig. 3 under a raw-activity variant.
- **Cross-day matching.** Matched counts under one threshold per mouse.
- **Blocked analyses.** These were not run: the decoder, GLM, k-means remap trials and teleport re-binning. None is blocked by missing data.
