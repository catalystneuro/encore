**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| link-metadata-table | reproduced | All 1,328 dandiset cells match a table row (cell 13). Every compared field agrees for 1,328/1,328, with ET spelled PT in the files; age also 1,328/1,328. The table's 1,329th cell (20190211_sample_10) is not in the dandiset. |
| link-ephys-features | reproduced | 1,320/1,328 cells (99.4%) agree on all 28 non-rheobase features (cell 15). Rheobase agrees for 1,287 cells; reported, as the criterion asks. |
| cohort-cells-mice | reproduced | 1,328 distinct cells (reading b) and 266 subjects (cell 18). The archive summary gives the same counts. |
| cohort-ages | reproduced | Per mouse (n = 266): min 35, Q1 64, median 75, Q3 100, max 245 days under every quantile method (cell 20). |
| cohort-genotypes | partially_reproduced | 9 of 10 lines match and the total is 266. Wild type is 26 against 27, and one Scnn1a-Tg3-Cre mouse is not in the paper's list (cell 22). |
| stimulus-protocol | partially_reproduced | Steps conform for 89.0% of cells (cell 24: first step −200 pA 89.1%, max ≤1,380 pA 91.6%), which is in the 80–95% band. The interval part could not be tested: every `starting_time` is NaN. The repeat part could not be tested either: each file holds a single ascending series, so 0 repeats. Both parts are data_missing rather than failures. |
| soma-depth-count | reproduced | 1,283 cells have a depth (cell 26). The missing cell has a depth in the table, so the criterion's 1,283 alternative applies. `cortical_thickness_4x` equals the table's "Soma depth (4x)" for 1,328/1,328. |
| ed4-example-cell | reproduced | 23 of 23 values within tolerance (cell 28). AP threshold is −43.18 mV, within ±4.018 of −40.18. |
| ephys-feature-count | reproduced | 1,320 cells with all features and 1,219 with a t-type (all cells), or 1,317/1,216 with duplicates removed (cell 30). Both are within 10%. |
| fig2-family-features | reproduced | Under reading (b), Pvalb has the highest median max APs (71) and Sst the highest median sag ratio (1.154) and rebound (5.70) (cell 32). Under reading (a), ET has the highest sag ratio. |
| fig3d-families-ephys | reproduced | ET→IT is 49.0%. The largest other off-diagonal entry is 14.4% (Lamp5→Sst). Both handlings of excluded cells and both cell sets give the same result (cell 35). |
| ed6-it-et-room-features | reproduced | After the omissions, the four smallest p are sag ratio, input resistance, AP width and rebound (cell 38). The fifth, AHP, has p = 7.7e-5 against 2.9e-5 for rebound. |
| ed6-physiological-temperature | blocked (data_missing) | The 34 °C data are in DANDI:000035. The archive description of 000008 says so, and the paper gives no measure. |
| fig1a-ttype-coverage | partially_reproduced | Counts are 1,226 / 817 / 409 / 76 t-types (cell 40). The two one-short cell counts are accepted under reading (b). The t-type count, 76 against 77, is not covered by that allowance. The missing cell is the only L6 CT Gpr139 cell, so the shortfall is fully explained by it. |
| fig1b-depth-layers | partially_reproduced | 18 of 19 excitatory t-types agree (95%). L5 IT_4 has a median depth of 0.757, which falls in L6 (cell 42). |
| l45-it1-boundary | reproduced | Median 0.279 lies in 0.235–0.40, and the IQR (0.259–0.306) contains 0.29 (cell 44). |
| fig4c-distance-correlation | reproduced | Reading (a): 50 t-types, 200 within-family pairs, r = 0.597 (transcriptomics cell 10). |
| ed7-within-families | reproduced | All 6 families have r > 0, and 16 of 17 features have r > 0 in at least half the families (transcriptomics cell 12). |
| fig4d-it-depth | reproduced | 8 IT t-types; r = 0.690 from the files and 0.698 from the µm table, both within 0.70 ± 0.07 (transcriptomics cell 14). |
| fig4a-vip-tau | blocked (methods_underspecified) | Reading (a) gives ρ = −0.582, p = 1.6e-15. Reading (b) gives ρ = −0.383, p = 0.154. The readings disagree, which the criterion maps to blocked (transcriptomics cell 16). |
| fig4b-sst-rebound | reproduced | Over all 17 features, r = 0.347, p = 0.0094 (11 t-types, 55 pairs). Rebound alone gives r = 0.275, p = 0.042 (transcriptomics cell 18). |
| fig4e-pvalb-axon-shape | blocked (data_missing) | All 1,328 assets are NWB files, with no morphology. The paper gives no measure. |
| fig3d-morph-combined | reproduced | The inhibitory mean diagonal is 0.737 for morphology against 0.851 for ephys. The seven-family mean is highest for combined (0.872/0.874). This holds under 16 and 17 PCs and both handlings (cell 46). |
| fig5a-ttypes-between-families | reproduced | (i) 28 of 35 t-types are ≤25% wrong. (ii) Sst Pvalb Calb2→Pvalb is 0.385. (iii) Lamp5 Egln3_1→Vip+Sst is 0.90. (iv)(a) Vip Mybpc1_3→Sst is 0.375 (cell 48). |
| fig5b-ttype-variability | reproduced | Main reading (Methods membership, n_init = 10): 17 of 35 t-types (49%) above the band with all cells, 43% with duplicates removed. Pvalb Vipr2_2 (0.449) is not above the band; Vip Mybpc1_2 (0.692) is (cell 50). This is fragile; see B4. |
| ed8-leiden-entropy | not_reproduced | Main (Methods) membership gives Spearman ρ = 0.266, one-sided p = 0.061 (duplicates removed) and ρ = 0.166, p = 0.171 (all cells). Only one variant reaches p < 0.05: code membership with duplicates removed, p = 0.031 (cell 52). |
| fig5c-vip-mybpc1-rebound | blocked (methods_underspecified) | Reading (a) gives ρ = 0.356, p = 0.019. Reading (b) gives ρ = 0.067, p = 0.648. The Vip Sncg median rebound (2.26) is below Vip Mybpc1_2 (11.31). The readings disagree, so blocked per the criterion (transcriptomics cell 20). |
| fig5d-sst-pvalb-calb2-firing | reproduced (marginal) | Reading (a): ρ = 0.363 > 0. Reading (b) with seed 55: p = 0.0485, Clopper-Pearson upper bound 0.0499. The exact p over all 10.4M subsets is 0.0497 (transcriptomics cell 22). Five other seeds fail the upper-bound rule; see B3. |
| rnaseq-depth | reproduced | Median exonic reads 1,281,492, median intronic 687,965, mean detected genes 9,097: all within 10% (sequencing cell 4). |
| ttype-qc-counts | reproduced | 78 / 14 / 5 / 1,232. Pass/fail agrees with the table for 1,329 of 1,329 cells (sequencing cell 6). |
| ed2-smartseq-similarity | reproduced | Single-nucleus Smart-seq2 has the highest median max correlation (0.703). Single-cell Smart-seq2 and 10x v2 assign the same t-type for 78.6% of cells (sequencing cell 8). |
| morph-reconstructions | blocked (data_unreadable) | The Brain Image Library URL did not respond within 30 s when I tried it on 2026-10-21. The paper's morphometric table has 646 cells (cell 46), but it is not the SWC archive the criterion names. |
| fig2-rrr | reproduced | Main reading: at λ = 0.5, R² 0.370 and correlations 0.895, 0.725, 0.648 (24 genes); at λ = 0.45, 0.382, 0.898, 0.744, 0.669. All are within tolerance (transcriptomics cell 6). |
| ed5-rrr-ion-channels | reproduced | 307 genes. R² 0.341 and correlations 0.865, 0.706, 0.565: all within tolerance (transcriptomics cell 8). |
| hold-time-yield | reproduced | ρ = −0.0124 (n = 1,320), within ±0.05 of −0.01 (cell 54). Both variables come only from the paper's table; see B7. |

That is 35 claims: 25 reproduced, 4 partially reproduced, 1 not reproduced, 5 blocked.

**B. Problems**

1. [does not affect a conclusion] **ed6-it-et-room-features and fig4b-sst-rebound (`cell_table`, `t.layer`):** the layer comes from the files' `inferred_layer`, not from depth with the Nissl boundaries as the claims file's opening comment specifies. The two disagree for 19 of 1,283 cells (cell 8). The ed6 ranking margin (rebound 2.9e-5 against AHP 7.7e-5) and the fig4b p (0.009) are probably robust, but this was not checked.
2. [does not affect a conclusion] **`layer_from_depth`:** depths exactly at 0.07, 0.29 or 0.73 fall back to the targeted layer (I checked this on synthetic input). It is used only in the data check.
3. [affects a conclusion] **fig5d-sst-pvalb-calb2-firing, transcriptomics cell 22:** reading (b) holds only with seed 55. Seeds 56–60 all fail the upper-bound rule, and the exact p is 0.0497. So the seed decides the criterion's outcome, which the criterion's rule was written to prevent. The true p is just below 0.05, so I keep "reproduced", but the outcome is marginal.
4. [affects a conclusion] **fig5b-ttype-variability, cell 50:** the share of t-types above the band ranges from 22% to 56% depending on k-means `n_init` (10 or 'auto') and membership handling. Two of the eight variants fall below the 25% reading. The claims file's "scikit-learn defaults" is version-dependent; the author's choice of n_init = 10 (the default under the code's Python 3.7) is reasoned but is a choice.
5. [affects a conclusion] **ed8-leiden-entropy:** the outcome flips between membership handlings (p = 0.061 under the Methods' handling, 0.031 under the code's, both with duplicates removed). The criterion does not say which handling governs. I took the Methods' handling, which fig5b treats as the main reading.
6. [could affect a conclusion, not verified] **fig5c-vip-mybpc1-rebound reading (b), transcriptomics cell 20:** the Patch-seq expression is exon/kb + intron/kb with no library-size normalization before log2(x + 1). This is the author's own choice, not the code's `normalizeNew` path. With ρ = 0.067 a flip is unlikely.
7. [does not affect a conclusion] **hold-time-yield, cell 54:** the dandiset contributes nothing. Hold time and yield both come from the paper's table, so this re-computes the paper's own table. Cell 6 also lists only a fixed whitelist of file fields, so it is not shown whether the files hold a hold time.
8. [does not affect a conclusion] **link-metadata-table, `norm` in cell 13:** numbers are compared after `.6g` formatting. That can hide differences of up to about 50 reads in counts above 10⁶.
9. [does not affect a conclusion] **Duplicate recordings (cells 10–11):** three pairs of different cells carry identical voltage matrices. The author reports this and runs each analysis both with duplicates removed and with all cells; outcomes agree between the two except in the B4/B5 variants.
10. [affects a conclusion; a gap in the claims file, not the notebook] **fig1a-ttype-coverage:** the reading-(b) allowance covers one fewer cell but not one fewer t-type. The missing cell is the sole L6 CT Gpr139 cell, which forces 76 t-types.
11. [does not affect a conclusion] **fig3d-morph-combined, cell 46:** the morphological representation is rebuilt inline (20 PCs, z-profile PCs 2–5, the +0.25 offset, √2 scaling of the ephys block), but `phenotype-tsne.ipynb` is not cited cell by cell, so I could not verify it against the code. The combined cell count is 627 with duplicates removed; the criterion says 628, and the all-cells count is not printed.
12. [does not affect a conclusion] **`leiden_entropies`:** the function reads the global loop variable `label`. It works as executed but is fragile.
13. [does not affect a conclusion] **fig2-rrr:** gene selection and X standardization use all cells before cross-validation. This follows the paper, uses no Y, and so leaks no labels.

Helper checks on synthetic inputs all passed: `knn_predictions` (excludes the cell itself; breaks ties in code-point order with "low quality" last), `family_confusion`, `normalized_variance` and `paper_name`.

**C. What I could not check, and the output that would have allowed it**

- **ed6 / fig4b layer effect:** the ed6 ranking and the fig4b r recomputed with the depth-derived layer.
- **hold-time-yield:** a list of every DandiIcephysMetadata and subject field in the files, not the whitelist in cell 6, to show whether hold time is in the files.
- **fig3d-morph-combined:** the all-cells cell counts and a cell-by-cell citation of the code being reproduced.
- **fig5c reading (b):** the result with CPM normalization, or via the code's own normalization in `rnaseqTools`.
- **fig5d:** the exact p is given, but which cells sit above the median is not shown; ties at the median could not be checked.
- **fig2-rrr fold construction:** the `sparseRRR` cross-validation folds (seed 42, contiguous). I could not inspect `sparseRRR.py`; printing the fold indices would settle it.
- **stimulus-protocol:** the 90 cells starting at −100 pA and the 87 ending at 1,480 pA are probably the same cells. A cross-tabulation would show that.
- **morph-reconstructions:** a listing of the Brain Image Library folder, which was unreachable for me as well.
