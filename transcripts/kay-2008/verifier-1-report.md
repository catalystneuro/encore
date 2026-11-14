**A. Outcomes** (23 claims, counted from `kay-2008.yaml`; the notebook's status table also lists 23)

| Claim | Outcome | Reason |
|---|---|---|
| fig3-s1-repeated-120 | reproduced | Cell 11: 109/120 (90.8%) under O1a-O5a and O1b-O5a, within 92 ± 9.2. Both O5b readings give 75.8%, outside tolerance. Chance is 1/120, as in the paper. |
| fig4a-s2-repeated-120 | reproduced | Cell 11: 87/120 (72.5%, O1a-O5a) and 86/120 (71.7%, O1b-O5a), within 72 ± 7.2. O5b gives 46.7%. |
| fig4a-single-trial | blocked (too_large, weakly shown) | Not run. The cost estimate in cell 16 is inflated (problem 2). The 70 raw runs are on the archive, and reading O6(a) is testable. |
| fig4a-noise-ceiling | blocked (depends on single-trial) | Needs single-trial patterns. It becomes testable once those exist. |
| fig4b-set-size-1000 | blocked (data_missing) | The archive listing has no 999-image library. |
| fig4b-extrapolation | blocked (data_missing) | Needs the library. |
| fig4c-retinotopy-only-extrapolation | blocked (data_missing) | Needs the library. |
| suppm8-retinotopy-only-120 | reproduced (caveat, problem 4) | Cell 24: subject means 53.3% weighted (55 ± 5.5) and 43.8% standard (42 ± 4.2) on O1a voxels; 52.9% and 42.5% on O1b voxels. Both are below the GWP means (81.7% under O5a, 61.2% under O5b). |
| suppfig8-constrained-models | blocked (data_missing) | Needs the library. The orderings at set size 120, which the criterion allows as a non-deciding variant, were not shown. |
| time-two-months | blocked (data_missing) | The archive listing has only five sessions per subject. |
| time-fourteen-months | blocked (data_missing) | Same as above. |
| errors-similar-images | reproduced | Cell 22, reading (b), local contrast: median percentile 61 to 69, one-sided Wilcoxon p from 1.2e-5 to 3.1e-4 under all four model readings. Reading (a), luminance, fails (p ≥ 0.7). The random-choice null centres on 49.6. |
| suppfig4-500-voxels | partially_reproduced | The notebook calls this blocked, but cell 28 computes the two repeated-trial conditions and both meet the rule. S1 O1a-O5a: 90.8% at 500 voxels (the maximum), above 61.7% at 50. S2: 72.5% at 500 against a maximum of 73.3%, above 45.8% at 50. The criterion defines "partially" as the rule holding in two or three conditions; the two single-trial conditions are untested. |
| supptable1-voxel-counts | reproduced | Cell 18: all six counts match exactly. They come from the data set's own ROI labels. |
| supptable1-predictive-power-by-area | reproduced (caveat, problem 5) | Cell 19: 6/6 values within 10% and V1 > V2 > V3 in both subjects. This relies on counting voxels with missing values as non-significant. |
| supptable1-snr | blocked (too_large, weakly shown) | Not run. Partly testable: see problem 2 and section C. |
| methods-v4-poor | reproduced (fragile) | Cell 20: V4 is below V3 in both subjects, but in S1 only by 17.5% against 18.2% (about 11 voxels), from a single random seed. |
| fig2-representative-voxel | partially_reproduced | Cell 26: the receptive field is in the left hemifield and spatial-frequency tuning peaks at the top frequency under both readings. Under O5a, whose 5.45° field of view gives exactly the figure's 2.9 cycles/deg axis, the envelope peak is above the horizontal meridian (+0.24°) and the orientation max/min is 2.23 (16.2 with the DC offset), so "just below" and "broadband" fail. Both hold only under O5b with the DC offset removed (−0.47°, ratio 1.77). |
| suppfig7-roi-tuning | not_reproduced (incomplete) | Cell 27: in every reading run, spatial-frequency tuning peaks at the highest level (16 cycles/FOV) and the orientation range is 31% to 449% of the mean, against the < 10% rule. The model-I reading and the suppfig8 voxel-set reading were not run. |
| suppfig10-retinotopy-validation | blocked (data_missing) | The archive has no retinotopic mapping scans, only `Sub*_Anat_msk`. |
| suppfig11-rf-size-eccentricity | partially_reproduced | Cell 25: Spearman ρ is 0.54 to 0.68 with p < 1e-27 in every area, so receptive-field size rising with eccentricity holds. V1 < V2 < V3 holds in most bins only for the square bounds with 1° bins (5/8). With 0.5° bins it is 6/12, and with the circular bounds 3/6 and 3/9. |
| suppdisc1-classification-extension | not_reproduced | Cell 23: under every reading, S2's contrast metric is not above chance (1 or 2 of 120, p ≥ 0.26; the paper reports 7, p < 0.0001). S1's contrast count is 9 (SD) or 4 against the paper's 6. The luminance results meet the criterion. |
| suppm7-selected-voxels-v1 | not_reproduced | Cell 21: the V1 share of the selected voxels is 0.42 to 0.48 under all readings and both subjects. V1 is the largest share but never more than half. |

**B. Problems**

1. **[affects a conclusion]** suppfig4 is marked blocked although cell 28 computes and meets its two repeated-trial conditions. It should be partially_reproduced. Cell 28 also prints only two of the four O1/O5 combinations.
2. **[affects a conclusion]** The `too_large` estimate in cell 16 is not well founded. It times `lstsq` on a random dense matrix and scales it to all 10,228 V1–V3 voxels of both subjects and to the training runs as well. Reading O6(a) needs single-trial amplitudes only from the identification runs (1,392 × about 344 per session), and only for candidate voxels (1,574 + 1,086 under O1a). The per-area fractions for supptable1-snr could be estimated from a random voxel subsample. The 70 runs are on the archive (about 150 MB each). This bears on fig4a-single-trial, fig4a-noise-ceiling, supptable1-snr and the single-trial half of suppfig4.
3. **[affects a conclusion]** In `gratings()` and `tuning_of` (cells 26 and 27), the curves that include the DC offset depend on the arbitrary grating amplitude of 0.5. The docstring says the amplitude "does not change their shape", which is false once the DC offset is added. The fig2 "broadband" ratio (16.2 under O5a, 6.54 under O5b) and the suppfig7 "with DC" results are therefore not meaningful; only the curves without DC are scale-invariant.
4. **[affects a conclusion]** `ro_channels` is called with `full + MU` (cell 24), so the luminance channel is the absolute value relative to the grey background (0). SM8 defines it as "absolute deviation from mean luminance", paralleling the GWP model, which subtracts the mean (SM6), and `MU` = −0.074. The notebook does not state this deviation. The values sit within tolerance by 3.8 and 2.4 points.
5. **[affects a conclusion]** In cell 19, voxels dropped for missing values (345 in S1 V1–V3, 214 in S2) count as non-significant. Using only voxels without missing values, which the cell also prints, puts 3 of 6 within tolerance (S1 V3 20.1%, S2 V1 29.0%, S2 V2 23.7%), which would be partial. The notebook prints both but neither decides nor discusses which is right.
6. **[affects a conclusion]** In cell 25, the "circle" filter tests `ecc + 2 SD ≤ R`, a disc, not the ±2 SD square that SM5 and Fig 2 define as the receptive-field location. Fig 2's legend calls the white circle "the bounds of the stimulus", which makes the square-field-of-view reading, the only one that passes, the less supported one. The radius used is 9.5°, from the mask's area; the paper describes a 20° circle.
7. **[affects a conclusion]** suppfig7 readings (b) (grating-transformed weights of model I) and voxel set (b) were not run, although the criterion lists them. The outcome is not_reproduced only for the readings that were run.
8. **[does not affect a conclusion]** The O1a candidate p-values use all 120 identification images, including the one being identified. P5 requires leaving that image out. O1b, which has no such leak, gives 109 (same) and 86 against 87.
9. **[does not affect a conclusion]** The 100 bootstrap fits are replaced by one fit (a stated deviation). The 10-fit variant (cell 13) was run only for O5b, not for O5a, which carries the reproduced values. Under O5b it changed counts by at most 3.
10. **[does not affect a conclusion]** About 30% of initial fits stop at iteration 0 (cell 7), because the run stops at the first non-decrease with step 0.001. Those voxels get no model and p = 1. This is an unstated reading of the stopping rule; the Supplementary Table 1 fractions still match.
11. **[does not affect a conclusion as run]** Every result comes from one seed with one shared stopping set. That margin matters for methods-v4-poor in S1 (0.7 percentage points).
12. **[does not affect a conclusion]** `error_percentiles` (cell 22) includes the selected image among the "others", which caps the percentile at 99.2. The effect is negligible.
13. **Claims-file reading, reported not corrected:** fig4a-noise-ceiling gives 13 or 14 trials per image. Cell 4 shows 13, 14 or 15 presentations per image across all runs.
14. **Synthetic tests of `vim1.py`** passed:
    - `area_matrix` and `resize_stack`.
    - `gwp`: unit-length, zero-mean wavelets; masks sum to 1; gratings select the matching level and orientation.
    - `fit_gd` recovers a linear kernel (r = 0.9999).
    - `loo_power` matches a direct calculation.
    - `identify_repeated` gives 100% on informative synthetic data and 1/120 on null data.
    - `boot_p` under the null: 0.6% below 0.01 and 4.4% below 0.05.
    - `fit_gaussian` recovers the generating parameters exactly.

**C. Not checked, and what would have let me**

- Sensitivity to the seed: identification counts and the methods-v4-poor V4/V3 comparison across three or more seeds.
- O5a with bootstrap averaging: cell 13 run under O5a.
- The retinotopy-only model with mean-subtracted luminance: cell 24 with `full` in place of `full + MU`.
- Whether the voxels with missing values had usable data in the paper: per-area counts of missing values by session would show whether they are slab edges.
- suppfig11: overall median receptive-field size per area, and the strict filter (all four corners of the ±2 SD square inside a 10° circle).
- fig2: the orientation ratio without DC at other grating amplitudes, and the centre of a Gaussian fitted to the final-model envelope (the raw peak sits on a flat plateau, 0.94 to 1.0).
- Single-trial cost: timing of one real BRS single-trial fit on one voxel's identification runs.
- The 60-minute notebook limit cited in cell 17: docs/protocol.md is not available to me.
