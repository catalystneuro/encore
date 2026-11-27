**A. Outcomes**

The claims file holds 31 claims, and the notebook tests all 31; none is treated as blocked. My outcomes: 26 reproduced, 3 partially reproduced, 2 not reproduced.

| Claim | Outcome | Reason |
|---|---|---|
| units-responsive-count | reproduced | Cell 14, reading ace with `good` units only: total 2422, V1 580, LGN 142, LP 91, all within tolerance, and the 8 named regions are kept. Reading ade without the `good` filter also passes. |
| fig1d-v1-1back | reproduced | Cell 19: V1 ratio 0.821, inside [0.81, 0.84]; p = 6e-58 (FDR 2.4e-57); 580 units. |
| fig1d-extrastriate-1back | reproduced | Cell 21: ratios 0.795 to 0.876, all in [0.72, 0.968]; largest FDR p 2e-24. |
| fig1d-thalamus-1back | reproduced | Cell 23: LGN 0.935 (CI [0.91, 0.96]), p 6.7e-7; LP 0.833 (CI [0.79, 0.88]), p 1.7e-10. |
| fig1e-consistent-across-mice | partially_reproduced | Cell 26: cortex 32/32 mice meet (a). Thalamus 21/23 fails (a), but the sign test passes (p 6.6e-5), so only (b) holds there. The criterion makes that partial. |
| fig2-v1-tuning-main-effect | reproduced | Cell 29: main effect p 3.1e-9 (log ratios, 45° pooled) and p < 1e-9 in all four readings; the 0° ratio is lowest (0.799 < 0.875 < 0.927). |
| fig2-v1-tuning-interaction | reproduced | Cell 31: interaction p 0.011 (log) to 6e-7 (ratio). The spread across orientations is largest in the high-OSI tertile (0.248, against 0.057 and 0.125). |
| fig2-v1-adaptation-at-all-orientations | reproduced | Cell 33, 45° pooled with BH over the 9 V1 cells or over all 72 cells: 8/8 cells below 1, and the high-OSI 90° cell has p 0.92 (ratio 0.993). |
| fig2-thalamus-no-tuning-dependence | reproduced | Cell 35: no main effect or interaction is significant under any reading (LGN p_rel 0.073 to 0.28; LP ≥ 0.66). |
| fig3a-v1-long-term | reproduced | Cell 38, main reading: significant at 1 to 8, 8-back FDR p 0.022, 9-back p 0.09. |
| fig3a-v1-double-exponential | reproduced | Cell 41: a_fast 14.21, tau_fast 0.816, a_slow 3.755, tau_slow 6.714, all inside the Table 1 CIs (sign reading a). |
| fig3a-v1-half-life | reproduced | Cell 43: 6.714 trials × 3 s × ln 2 = 13.96 s, within 14 ± 1.4 s. |
| fig4-cumulative-adaptation | reproduced | Cell 45, main reading: 1-back reduction 17.88% (target 17 ± 1.7), 2- to 8-back 20.36% (target 19 ± 1.9), and the cumulative value is larger. |
| fig4b-linear-accumulation | reproduced | Cell 48, baseline (c): all 7 predicted values fall inside the bootstrap CIs, under seed +0 and 4 other seeds. Baseline (d) fails at pair 1-2. |
| fig3b-thalamus-short-term | reproduced (fragile) | Cell 50: the main reading fails because RL's largest significant n is 5. Only the pooled/hold/across reading passes (RL 6, LGN 1, LP 2). See problem 1. |
| v1-vs-thalamus-welch | reproduced | Cell 52: with region normalization over n 2 to 10, V1 > LGN at exactly 2, 4, 9 and V1 > LP at 3. The unnormalized test also passes all four. |
| fig3c-mice-long-term | reproduced | Cell 54: cortex 31/32 mice, sign test p 1.5e-8, so (b) holds. Thalamus 14/23, p 0.4, so neither (a) nor (b) holds. |
| decay-cortex-double-better | reproduced | Cell 56: F test p < 0.05 in V1, LM, AL, PM and AM under both F variants; RL p 0.22, as in the paper. |
| table1-extrastriate-tau-slow | reproduced | Cell 58: all 5 extrastriate tau_slow inside the Table 1 CIs; the six bootstrap CIs overlap under all 5 seeds; V1 has the largest tau_slow. The other Table 1 parameters are also inside their CIs. |
| decay-thalamus-single | reproduced | Cell 60: F test p 0.81 (LGN) and 0.57 (LP). LGN tau 0.031, a 6.48%; LP tau 0.712, a 16.85%; all inside their CIs. |
| fig5-repeat-suppression | not_reproduced | Cell 63: orthogonal/blank at 2-back is below 1 under both readings, every seed and the 100-draw average (0.972, CI [0.957, 0.986], FDR p 9e-4). The criterion forbids that. The repeat/blank 8-back value is also not significant under the claim's seed. |
| fig6c-static-v1-1back | reproduced | Cell 65: ratio 0.897, in [0.89, 0.91]; p 4e-85; 545 units (target 530 ± 53). |
| fig6c-static-other-areas-1back | reproduced | Cell 67: extrastriate 0.891 to 0.930; LGN 0.957 (p 0.0025, 61 units); LP 0.900 (p 0.0045, 17 units). All match under the widened rule. |
| fig6d-static-consistent-across-mice | partially_reproduced | Cell 69: cortex 32/32 mice; thalamus 15/17 (sign test p 0.0023), so only (b) holds there. |
| fig7a-static-v1-long-term | reproduced | Cell 71, FDR family 1 to 20: 20-back is significant and is the largest significant n. All four Table 2 estimates are inside their CIs (tau_slow 9.47). |
| fig7b-static-cortex-decay | reproduced | Cell 73: every F test p ≤ 1.4e-5; all 5 extrastriate tau_slow inside the Table 2 CIs; the CIs overlap. |
| fig7-static-lgn-single | reproduced | Cell 75: F test p 0.20; tau 2.77 in [1.36, 7.32]; a 4.00% in [1.80, 6.59]. |
| fig7b-static-areas-long-term | reproduced | Cell 77, family 1 to 20 with reading (c): V1, AL, PM and AM reach 20. The thalamus (5 and 9) is below every cortical area (smallest 15). See problem 4. |
| fig7c-static-long-term-across-mice | partially_reproduced | Cell 79: cortex 30/32 and V1 29/32 mice, sign test p ≤ 2.6e-6, so only (b) holds. Read as fig1e's rule requires, that is partial. A looser reading ("holds" as in fig3c) would make it reproduced. |
| fig8-no-spurious-long-term | not_reproduced | Cell 81: under the claim's seed, no reading meets the full rule or the partial rule. The Poisson static run excludes 1 at 5- and 6-back (0.986, 0.987); the no-noise drifting run excludes 1 at 2- and 6-back (0.996, 1.003). Only seed +1000 of five passes, under (a, c). See problem 2. |
| robust-threshold-preferred-window | reproduced | Cell 83: all 7 variants meet the reading (V1 significant beyond 1-back, double exponential better, LGN no later than 2). |

**B. Problems**

1. [affects a conclusion] **fig3b, cells 37 and 50.** The claim passes only under the pooled/hold/across reading. Every other claim uses hold/within. That passing reading has RL at exactly the threshold of 6. `nback_tests` counts an n as significant only when the ratio is below 1. Under that same reading, LGN 9-back is significant with a ratio above 1 (`LGN_any [1, 9]`). If two-tailed significance in either direction counts, as the paper's black borders likely do, the outcome drops to partially reproduced.
2. [affects a conclusion] **fig8, cell 81, and the claims file.** The paper says the simulated points are "centered on an adaptation ratio of one". The claims file turns that into "every CI over 9 or 49 n contains 1", which noise alone breaks: about 0.45 exclusions are expected per stimulus set over 9 n, and about 2.5 over 49 n. That fits the 1 seed in 5 that passes. Every excluded ratio is within 0.015 of 1 (empirical V1 2-back: 0.918). The not_reproduced outcome therefore comes from the claims file's misreading of the paper, not from the data. The notebook checked the partial rule on seed +0 only.
3. [does not affect a conclusion] **fig5, cell 62.** The unit bootstrap and t tests treat units as independent, but within a session they share one trial subsample, so the CIs are too narrow. The orthogonal/blank 2-back failure persists in the 100-draw average, so the outcome holds either way.
4. [does not affect a conclusion] **fig7a and fig7b-static-areas, cells 71 and 77.** With the 1-to-20 family, the largest significant n cannot exceed 20, so the 18-to-22 test is partly met by construction. With 1 to 50, isolated late n are significant (V1: 26, 41, 46, 49). That points to scattered significance, or anticonservative tests, rather than a clean bound at 20. This is the claims file's reading, reported here, not corrected.
5. [does not affect a conclusion] **Fig. 2, `tuning_cells` in cell 28.** OSI tertiles are assigned before units with a non-finite log ratio in any cell are dropped. V1 loses 78 units, mostly from the high-OSI tertile (116 left, against 194 and 192). That shifts the composition of the critical high-OSI 90° cell.
6. [does not affect a conclusion] **Unit selection, cells 12 and 15.** The main O4 reading was picked by matching the paper's counts, which "under one reading" allows, and is then used consistently. The `noise`-label filter is an assumption beyond the Methods' three metrics. It is reasonable (AllenSDK's `filter_by_validity` does this), and cell 17 shows the results are unchanged without it.
7. [does not affect a conclusion] **`invalid_times`, cells 6 and 10.** These intervals are not applied, though they overlap the grating epochs in several sessions (e.g. 715093703: 4 drifting, 4 static). The paper is silent on them, and whether the AllenSDK would drop those presentations was not checked.
8. [does not affect a conclusion] **`adaptation._boot_task`.** It does not pass `sign`, so every bootstrap uses sign −1. That is harmless here, because reading (a) is the one used.

I tested the helpers on synthetic inputs:
- `fdr` matches statsmodels' BH to 1e-17.
- `mixed_anova` matches pingouin's `mixed_anova` exactly on unbalanced groups.
- `pair_masks` handles blanks and block boundaries correctly.
- `nback_rates` / `ratios` recover a planted 1-back ratio of 0.8 exactly.
- `fit_models` recovers planted double-exponential parameters exactly.
- The hard-coded Table 1 CIs match the paper's text.

**C. What I could not check, and which output would settle it**

- **Effect of `invalid_times`.** The 1-back ratios and unit counts recomputed with presentations inside invalid intervals excluded.
- **Fig. 2 drop pattern.** Units dropped per tertile × relative-orientation cell, and the high-OSI 90° t test with zero-count units kept on the ratio scale.
- **fig3b direction.** The LGN 9-back ratio and p value under pooled/hold/across, and a two-sided significance column per area for every reading.
- **fig8 seed dependence.** The fraction of, say, 200 Poisson seeds meeting each reading, and the number of exclusions expected by chance.
- **fig1e, fig6d, fig7c.** Thalamic unit counts for each mouse that fails reading (a).
- **fig5 clustering.** A session-level (cluster) bootstrap for the orthogonal/blank 2-back value.
- **The authors' choices.** I could not check their actual readings of O1 to O5: the paper's code (doi:10.34973/kpt9-y956) is restricted, and figure values were not available.
