# Verifier report, round 1: Bruno, Frost & Humphries 2017 (eLife 27342) on CRCNS apl-1

The claims file has 30 claims. My outcomes: 21 reproduced, 4 partially reproduced, 3 not reproduced, 2 blocked.

## A. Outcomes

| claim | outcome | reason |
|---|---|---|
| dataset-size | partially_reproduced | Cell 10 gives 10 preparations, 30 recordings and 1131 neurons, all exact. Only 12 of 30 recordings hold 108 to 198 neurons; the range is 75 to 160, which matches the data description, not the paper's 120 to 180. |
| fig1d-slow-oscillation | reproduced | Cell 12: the weighted peak of the grand mean spectrum is 0.0486 Hz, and 30 of 30 recordings lie in (0, 0.11] Hz. |
| fig1e-decaying-rate | reproduced | Cell 14: 30 of 30 responses decrease under both reading (a) (R < -0.2) and reading (b) (negative slope). |
| fig2b-dimensions | reproduced | Cell 16, code count (le80) with either the recording's own or the pooled median ISI: 28 of 30 counts in 3.6 to 8.8, and neurons/dimensions above 10 in 30 of 30. It fails under the Methods count (min80: ratio above 10 in only 29 of 30) and under both printed SDs (22 to 76 dimensions). |
| fig2ef-periodic-recurrence | reproduced | Cell 20: in all readings but one, more than 15 and fewer than 30 dominant periods lie in 9 to 16.5 s (adopted reading: 26 of 30, median 12.7 s). The exception is twelve/le80 with the mean period (13 of 30). |
| fig2e-single-dominant-orbit | reproduced | Cell 22: 29 of 30 responses have more than 50% of points in the dominant peak (27 of 30 counting all recurrent points); there are 1 to 4 peaks. |
| fig2s2-threshold-robust | reproduced | Cell 24: reading (a) holds at 5% and at 2% in every reading, Spearman 0.70 to 0.97 with p < 1e-4. |
| fig3a-coalescence | not_reproduced | Cell 26: coalescence comes within one period of onset in only 11 to 14 of 30 responses (27 required), and 16 to 20 of 30 measured from offset. The proportion recurrent after coalescence exceeds 50% in 30 of 30. |
| fig3c-same-manifold | reproduced | Cell 30: 29 of 30 pairs pass with recurrent points and 28 of 30 with the code's points. With the code's points the failing pairs are exactly (4; 1,2) and (4; 1,3), as in the paper. |
| fig3s1a-common-axes | reproduced | Cell 32: 27 to 30 of 30 pairs pass (26 required). |
| fig3d-initial-conditions | reproduced | Cell 34: the transient distance exceeds both other distances in 30 of 30 pairs. Medians: transient about 45, onset about 9.3, coalesced about 14. |
| fig3f-pairwise-similarity | reproduced | Cell 36: 27 to 30 of 30 pairs pass in every variant. Pearson with the larger control fails exactly (7; 1,3) and (7; 2,3), as in the paper. |
| fig3h-perturbations-return | reproduced | Cell 38, own/le80: 18 kept with 16 returned (mean period) and 19 kept with 17 returned (median period), both within tolerance. It fails under the adopted own/min80 reading (16 kept, 15 returned) and under the pooled readings. |
| fig3i-same-manifold-after | reproduced | Cell 40: 13 or 14 under own/le80 with reading (a), and under own/min80 or pooled/le80 with reading (b), all within 14 ± 1.4. The result depends strongly on the reading (range 9 to 17). |
| fig4bc-stable-spiral | partially_reproduced | Cell 42: the grand mean is a stable spiral in every reading, but only 6 to 9 of the 10 preparations have two of three spiral responses (adopted reading: 8; preparations 3 and 4 have 1 each). |
| fig4c-orbital-period | partially_reproduced | Cell 44: the mean linear-model period is 10.45 s (own/min80) and 10.12 s (pooled/min80), within 10 ± 1, but 13.55 s and 12.22 s under le80, the count under which fig2b holds. It is uncorrelated with the recurrence periods (r = -0.06, p = 0.74), so "consistent with" is not supported. |
| fig4s1a-contracting-dimensions | not_reproduced | Cell 46: only 8 to 11 of 30 responses have all dimension means negative (more than 15 required). |
| fig4s1b-rotation-dominant | reproduced | Cell 48: p_complex12 exceeds 0.5 in 30 of 30 responses in every reading (minimum 0.73). |
| fig5b-period-changes | reproduced | Cell 50, adopted reading: 12 slowing, 4 speeding and 14 unchanged; 31 to 73 windows per response, within 27.9 to 79.2. (own/le80 has a minimum of 27 windows, just below the range.) |
| fig5c-no-relation-contraction | reproduced | Cell 52: p ranges from 0.064 to 0.47 across readings, never below 0.05. The adopted reading is borderline (R = -0.34, p = 0.064). |
| fig6d-decode-p10 | not_reproduced | Cell 56: mean R − 2 s.e.m. is above 0 in 8 of 9 responses under all three windowings. Preparation 4, bout 1 has mean forecast R = -0.06. |
| fig6s1-no-p10-motorneurons | reproduced | Cell 54: the largest locking value is 0.522; no neuron reaches 0.9 in any program. |
| fig6s2-dimensions-p10 | reproduced | Cell 58: under le80, all 9 counts lie in 2.7 to 5.5 and the 90% count is at least twice the 80% count. The 90% models are not better: MAE is worse (p = 0.0195, 7 of 9 worse) and R² does not differ (p = 0.25). |
| fig7a-long-tailed-participation | reproduced | Cell 62: skewness is positive in 30 of 30 responses, and the fraction of neurons above 0.5 is at most 0.40. |
| fig7f-strongly-variable-neurons | reproduced | Cell 64: all 10 preparations have at least 4 strongly variable neurons, under both readings and both pools. |
| halving-participation | reproduced | Cell 66: 6 preparations under reading (a) (top neuron) and 9 under reading (b) (top 10%), against more than one required. |
| fig7s1-rate-synchrony | reproduced | Cell 68, main reading (rate from offset, matched pairs): mean R² 0.491 against 0.5 ± 0.05, and 0.239 against 0.23 ± 0.023. |
| fig7gh-robust-to-participation | partially_reproduced | Cell 70, adopted own/min80: one slope is significant with recurrent points (total change, p = 0.031) and one with the code's points (Hellinger, p = 0.028). Under pooled/le80 neither slope is significant. |
| fig7s2-no-invariant-core | blocked (other) | Cell 71 is a placeholder; nothing was computed. The data are not missing (see B.8). |
| fig8-caudolateral | blocked (metadata_insufficient) | I confirmed this in the archive (see B.9). Cell 73's quadrant counts decide nothing without the array's orientation. |

## B. Problems

1. **[affects a conclusion] The adopted reading fails fig2b (cells 17 and 18, `ADOPT = "own/min80"`).** Under the Methods count, fig2b fails (ratio above 10 in only 29 of 30). Every single-reading downstream analysis uses this reading: decoding, participation, fig7gh and fig8. Several outcomes reverse between min80 and le80: fig3h (fails / passes), fig4c (passes / fails) and fig7gh (fails / passes). No single reading makes the whole chain hold, and the notebook does not say so.
2. **[affects a conclusion] fig7gh was run under only 2 of the 4 readings (cell 70).** own/le80 and pooled/min80 are missing, and the outcome flips between the two readings that were run.
3. **[affects a conclusion] fig6d was decoded only under own/min80 (cell 56, `decode_program` hard-codes `"min80"`).** The le80 and pooled readings that the criterion carries over from fig2b were not run. So it is unknown whether preparation 4, bout 1 fails under every reading.
4. **[affects a conclusion] fig3h and fig3i are reading-shopped.** Eight readings (plus code-rule variants) were run. The target counts are met in only a few of them, and not under the adopted reading. The criterion allows "under a reading", but this success is weak evidence.
5. **[does not affect a conclusion] Asymmetric history search in fig6s2 (cell 56).** The 90% models search only 50, 100, 150 and 200 ms; the 80% models search 50 to 200 ms in 10 ms steps. This favours the 80% models, the direction of the claim. A like-for-like comparison was available from `by_history` but was not shown. The 90% MAE was worse by a median of 1.56, so this is unlikely to reverse the result.
6. **[does not affect a conclusion] fig6s2 mixes readings.** The counts pass only under le80, but the forecasts compare min80 against min90 dimensions.
7. **[does not affect a conclusion] Strict inequality where the paper says "at least" (`summarise`, `divergences`).** Coalescence and divergence use `dens > 0.9` where the paper says "at least 90%". With a 500-point denominator the effect is negligible.
8. **[affects a conclusion] fig7s2 is labelled blocked although it is testable.** The archive holds all 30 spike-time sets, which is everything the ensemble typing needs. The paper links the code toolbox (consensus clustering and spike-train typing), and the claims file names those scripts. A partial test is also possible with no typing: the top 10% by maximum participation and their median maximum change, from `PART`.
9. **[does not affect a conclusion] fig8 is correctly blocked.** I listed the archive (S3 prefix `apl-1/`): the `live/` files above plus `plot_maps.m`, `plot_rasters.m`, `load_raw_data.m`, the docs, `rawdata.tar.gz` and `orig/`. `plot_maps.m` plots `floor(x*10)`, `floor(y*10)` on the diode template with `YDir` normal and no anatomical labels. The description only names left and right preparations. Nothing gives which way is caudal or lateral. One part is testable without orientation: whether the top-fifth neurons concentrate in a single quadrant (left: 15 of 21 in x−y−). Separately, the range test is nearly empty as run: pooling the equal-width fifths over 8 preparations leaves 1 to 2 neurons in the top fifth.
10. **[does not affect a conclusion] fig1d may be measuring the rate decay, not an oscillation (cell 12).** The grand mean spectrum's maximum is at the lowest non-zero bin (0.0076 Hz). The criterion passes, but there is no pre-stimulus or detrended comparison to tell the two apart.
11. **[does not affect a conclusion] Helper checks on synthetic inputs.**
    - These behaved correctly: kernel unit area and centring, SDF area, `n_pcs`, recurrence on a smooth 12 s orbit (peak at 11.3 s; the code's first-entry rule biases it low), `weighted_spearman` (matches scipy with unit weights), `hellinger`, `p10_locking`, and `iterate_outliers`. `iterate_outliers` also trims some core points, but that is the code's rule.
    - On a toy orbit, the mean-imaginary-part period came out about 2× the true period, because real maximum eigenvalues contribute b = 0. This is inherent to the criterion's method. In the real data p_complex1 is high, so the effect is smaller.

## C. What I could not check

- **The ≥100-neighbour filter.** It never removed a point (`n_used == n_all` in all 30, cell 42). A histogram of `npts` per response would show whether the filter is meaningful.
- **Why coalescence is late (fig3a).** The recurrence-density time course of a few responses, and the density in the first windows, would show whether late coalescence is real. Windows can only start at 35 s, so the earliest possible value is 7.5 s after onset.
- **Whether the fig6d failure is robust.** Decoding under own/le80 and pooled/le80, plus a plot of P10 against the forecast for preparation 4, bout 1, would settle it.
- **fig7gh's remaining readings.** The regressions under own/le80 and pooled/min80 were not run.
- **The fig6s2 comparison on equal history grids.** The 80% models restricted to 50, 100, 150 and 200 ms.
- **fig7s2.** There are no outputs at all.
