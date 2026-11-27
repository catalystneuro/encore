**Verification report: lee-2023 (doi:10.1126/science.adf6484) on DANDI:000636 0.241120.0510, round 1**

The claims file has 45 claims. I checked the archive through the DANDI API. The pinned version holds 706 assets, all of them `.nwb` files of electrophysiology (current clamp, voltage clamp and stimulus series). It holds no morphology, transcriptome, MERFISH or image files. DANDI:000020, "Patch-seq recordings from mouse visual cortex" (published 0.210913.1639, 4435 assets), is on the same archive. I tested the helpers `neighbour_fraction`, `zscore_impute`, `bh`, `mannwhitney_table` and `kruskal_dunn` on synthetic inputs. They behave as documented: self is excluded, the among/query masks work, BH matches statsmodels, and the Dunn pairs are re-indexed correctly.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| cell-metadata-link | reproduced | 684 of 704 Has_ephys rows found (97.2%). Within 10% of the paper's table: rheobase 0.922, input resistance 0.945, sag 0.978, width_rheo 0.988. 16 files have no metadata row (cell 10). |
| dataset-composition | partially_reproduced | 778 neurons and 44 t-types are exact. Reading a gives PVALB 363, SST 158 and VIP 101, all within tolerance, but LAMP5/PAX6 64 (needs at least 67.5). Even the metadata's Has_ephys rows give only 67. Reading b misses PVALB (290) and SST (231) (cell 12). |
| fig1b-more-genes-in-culture | reproduced | Culture median is higher with p=4.3e-10 on counts from the matrix and p=1.6e-5 on the Genes_Detected column (cell 16). |
| figs1a-genes-across-days | reproduced (caveat, problem 2) | Pearson p=0.54, and every DIC median is above the acute median, but only on counts from the matrix (cell 18). |
| fig1d-nms-no-difference | reproduced | p=0.38, medians 0.962 and 0.962 (cell 20). |
| fig1c-marker-expression-correlated | reproduced | Every reading run gives r>0 and p<1e-4, the smallest margin being p=1.4e-5. The snRNA-seq gene-ranking reading was not run (cell 22). |
| figs2d-seven-channel-genes | blocked: data_missing | The `keepGenes` filter needs data the repository lacks. Unfiltered: 22 genes (Holm within each gene), 1 (Holm across genes), 12 (BH); 142 channel genes against 114 in the paper. Neither adjustment gives 7. |
| fig5a-dbc-two-ttypes | reproduced | 7 SST CALB1 and 4 SST ADGRG6. All 11 agree with the stored tree mapping (cell 26), which was not re-run. |
| figs7a-dbc-regions | reproduced | [6, 7, 3, 4] exactly, from `lobe` (cell 28). |
| figs7a-dbc-markers | reproduced | Of 11 DBCs: CALB1 >5 in 7, CALB2 >0 in 1, SST >0 in 10; TAC1, NOS1 and NPY each in 7, 9 and 10 of 11 (cell 30). |
| fig4d-calb1-genes-by-morphology | not_reproduced | The Methods reading gives 2 or 0 DE genes against 253±25, too few to build a UMAP. The notebook-code variant gives 431 (or 451 rows), not separated on any of 5 seeds; DBC majority 0.43–0.57 (cells 32–33). |
| figs2b-wfdc2-ephys-43-of-84 | blocked: methods_underspecified | 41 of the 65 computable features differ. 19 of the 84 need unreleased IPFX code, so the count over 84 is bounded at 39–61, which spans the tolerance 38.7–47.3 (cell 37). |
| fig1l-width-sag-differ | blocked: methods_underspecified | Sag holds (FDR 1.2e-14, higher in culture). Width holds for the rheo, hero and short-square readings, not for ramp (0.0077). ISI rheo differs (0.016) and ISI hero does not (0.75), so the readings disagree (cell 39). |
| figs2c-no-change-with-days | blocked: methods_underspecified | width_short_square correlates with DIC (r=0.37, FDR p=0.0015); the other widths and sag do not. Only one PVALB WFDC2 cell is at 2 DIC (cell 41). |
| fig1i-wfdc2-ephys-umap-overlap | not_reproduced | In feature space the culture cross-fraction is 0.191 against a shuffle median of 0.446 (ratio 0.43, below 0.5) on every seed and at k=10 and 30. UMAP passes. Only 65 of 84 features were used (cell 43). |
| fig2b-ephys-umap-subclasses | partially_reproduced | PVALB has the highest same-subclass fraction in every space. Separability misses narrowly: VIP excess 0.193 in feature space, SST 0.199 on 1 of 5 UMAP seeds (cell 45). |
| fig2f-ap-kinetics | partially_reproduced | PVALB has the narrowest width and lowest up/down ratio, against all others, under both readings. LAMP5/PAX6 has the highest peak median, but it is not significant against VIP (0.08, short square) or SST (0.061, rheobase). The readings agree (cell 47). |
| fig2g-sag-by-subclass | reproduced | Medians LAMP5 0.10 and VIP 0.15 against PVALB 0.24 and SST 0.30. All four pairs have Dunn p ≤ 1.9e-6 (cell 49). |
| fig2h-several-features-distinct | reproduced | 44 other features significant; 43 of them have a Dunn pair below 0.05 (cell 51). |
| fig3c-frzb-ephys-with-pvalb | reproduced | 71–73 of 73 SST FRZB cells have a PVALB majority, against about 0.89 expected by chance (problem 7) (cell 53). |
| fig3e-frzb-ap-like-pvalb | reproduced | In all 6 feature × sweep readings, FRZB differs from SST at Dunn p<1e-4 and its median is nearer PVALB (cell 55). |
| figs6-sst-features-acute-culture | reproduced | No FDR p below 0.05 in any of the 12 tests (the smallest is 0.22), with acute n of only 17–25 (cell 57). |
| fig4c-calb1-ephys-by-morphology | reproduced | All six median statements hold, and they also hold with the paper's own isi_adapt_ratio values (cell 59). |
| fig5c-dbc-higher-sag | partially_reproduced | The DBC median is higher under both readings. Under reading a, 6 of 8 DBCs are above the comparison median, which is the criterion's partial case (cell 61). |
| fig5d-dbc-ephys-intermingled | not_reproduced (problem 1) | DBC neighbour fraction is 2.28–3.71 times the DBC share, above the limit of 2, in every space and seed (cell 63). |
| figs5-vip-enhancer-enrichment | reproduced | 19 of 30 CN2039 cells are VIP (0.63). Fisher p=1.7e-9 against all other cells and 1e-14 against CN1390-only cells (cell 65). |
| fig1g-wfdc2-morphology-unchanged | reproduced | No feature has FDR p below 0.05 under any of the three readings (16/10, 9/9 and 10/10 cells). None matches the paper's 9/10 exactly (cell 69). |
| fig2c-morph-umap-subclasses | partially_reproduced | PVALB is the most distinct in every space. Separability fails: LAMP5 excess 0.10 in feature space, SST below 0.2 on 4 of 5 UMAP seeds (cell 71). |
| fig2e-lamp5-shortest-extent | reproduced | LAMP5 has the lowest median for both features; KW p 4.6e-6 and 2.4e-4 (cell 73). |
| fig3g-frzb-morphology-like-pvalb | reproduced | Both medians are nearer PVALB. SST against FRZB Dunn p is 0.0008 and 0.0006. 12 of 14 FRZB cells fall in PVALB-dominated clusters for both k and every seed (cell 75). |
| fig1h-wfdc2-morph-umap-overlap | reproduced | Holds for both cell sets, both spaces and all seeds (cell 77). |
| fig5d-dbc-morph-umap | partially_reproduced (problem 1) | Holds in feature space (ratio 3.48), and on 3 of 5 UMAP seeds (the other two give 1.54 and 1.62) (cell 79). |
| figs1-microglial-signature | blocked: other | Tooling, not data: the transcriptomes are loaded, and `condition2` already holds the paper's microglial calls (problem 4). |
| fig1e-wfdc2-transcriptome-overlap | blocked: other | The data are present. The block is the Seurat integration only. |
| figs1de-mapping-unaffected | blocked: other | Same as fig1e. |
| fig2a-patchseq-overlaps-snrnaseq | blocked: data_missing | The snRNA-seq reference is on the Allen portal and was not fetched. |
| fig3-frzb-transcriptome-intermediate | blocked: data_missing | The snRNA-seq part needs the reference. The Patch-seq SST/PVALB expression and the neighbour part could be run. |
| fig4a-calb1-morphology-types | blocked: data_missing | The L1 axon criteria need the BIL reconstructions. The DBC extent-ratio and sparse branch-density parts may be testable from `LeeDalley_morpho_features.csv`; not tried. |
| fig5b-merfish-layers | blocked: data_missing | The paper gives no location for the MERFISH data. The Patch-seq `Cortical_layer` report the criterion asks for was not made. |
| fig5e-bouton-density | blocked: data_missing | 63x image stacks at BIL only; counting method unstated. |
| fig6b-species-morphology | blocked: data_missing | Mouse reconstructions not located. |
| fig6c-species-ephys-umap | blocked: other | Mouse electrophysiology is on DANDI:000020; mouse t-type labels (Gouwens 2020) not checked. |
| fig6e-species-sag-rheobase-width | blocked: other | Same as fig6c. |
| figs8b-firing-differs-pvalb2-only | blocked: other | Same as fig6c. |
| figs9-species-differences-not-culture | blocked: other | Same as fig6c. |

### B. Problems

1. **[affects a conclusion]** Cells 63 and 79: fig5d-dbc-ephys-intermingled and fig5d-dbc-morph-umap define "SST" by `subclass_label`, which includes the SST FRZB cells (73 in the electrophysiology set, 14 in the morphology set). The header's default is `Revised_subclass_label`. The paper's reading is open, and only one reading was run.
   - Morphology: the DBC share would rise from 0.224 to 11/35 = 0.31, so the threshold rises to 0.63. Every UMAP fraction shown (0.35–0.58) is below that.
   - Electrophysiology: the share would rise from 0.039 to 0.057. Some UMAP seeds (0.089–0.111) would then fall under the new limit of 0.114.
2. **[affects a conclusion, unverified]** Cell 18: figs1a uses gene counts from the matrix (>0). The claim's `where` names the `Genes_Detected` column, and cell 14 shows that the two measures disagree for all 778 cells (median difference 4394). On the matrix counts, the day-3 median exceeds the acute median by only 229 genes. The per-day test was not run on `Genes_Detected`.
3. **[affects a conclusion]** Cells 43, 45, 53 and 63: the neighbour and UMAP claims silently use 65 of the 84 features, while figs2b treats the same gap as blocking. fig1i (ratio 0.43 against 0.5) and fig2b (0.193 against 0.2) are near their thresholds. The paper's 84-column table is already loaded (`fx_paper`) and was not used as a check.
4. **[affects a conclusion]** Cells 0 and 13: figs1, fig1e and figs1de are blocked as "Seurat in R", but the data are present. Reading (a) of figs1 can be computed directly from the `condition2` counts by condition, and reading (b) from X with the Data S2 genes.
5. **[affects a conclusion]** The parts of blocked claims that the criteria say are testable were not run:
   - fig5b: Patch-seq `Cortical_layer` of the two t-types.
   - fig4a: extent-ratio and branch-density parts from the morphology table.
   - fig6c, fig6e, figs8b and figs9: the mouse electrophysiology exists on DANDI:000020, so "data missing" is not established for them.
6. **[affects a conclusion]** Cell 32, fig4d: the variant leaves out the immune-gene and `keepGenes` filters. Its 431 genes is therefore only an upper bound, and a count within 253±25 is not excluded under the variant reading. The criterion accepts "one reading". The cell also has no RESULT line.
7. **[does not affect a conclusion]** Cell 53: the fig3c threshold (more than half of cells with a PVALB majority) is below chance. With a PVALB share of 0.65 and 15 neighbours, P(majority) is 0.887. The observed 0.97–0.99 and the mean PVALB fraction of 0.86 (against 0.65) are above it, but the notebook reports no chance level. The z-scoring also includes the FRZB cells, against the criterion's "over SST and PVALB cells".
8. **[does not affect a conclusion]** Cell 24, figs2d: the notebook asserts that `apply(lm_pval, 2, p.adjust)` adjusts within each gene, while the claims file reads it as adjusting the condition term. Both were run and neither gives 7.
9. **[does not affect a conclusion]** Cell 49, fig2g: the sag result is confounded by condition. Sag is higher in culture, and the subclass mix differs by condition: SST is 139 of 158 culture cells, while LAMP5 is mostly acute. Within acute cells, VIP (0.167) is above PVALB (0.106). The criterion pools, as the paper does.
10. **[does not affect a conclusion]** Cell 8 and `long_square_features`: feature failures are not excluded. Input resistance goes down to -789 MΩ, width_rheo and width_short_square include 0, and fi_fit_slope 4e-19. The rank tests limit the impact.
11. **[does not affect a conclusion]** `long_square_features`: the isi_adapt_ratio assumption (second ISI over first) agrees with the paper's table in only 27% of cells (cell 10). fig4c gives the same ordering with the paper's values.
12. **[does not affect a conclusion]** Cell 12: cell-level QC (seal, access) is not recomputed, although the files hold test pulses. Applying it could only lower the counts, and LAMP5 is already low.
13. **[does not affect a conclusion]** fig1l and figs2b: BH is computed over 65 features, not 84. The worst-case factor of 84/65 moves width_short_square to 9.9e-5, at the edge of the 1e-4 cut, but the claim is blocked by the ISI disagreement in any case.
14. **[does not affect a conclusion]** Cell 57: figs6 is an absence result with acute n of 17–25 against culture n of 117–199, and width rbc is about -0.2. Power is low.

### C. Not checked, and the output that would settle it

- Sampling rate by condition: 78 files are at 200 kHz (2020–21), against the paper's 50 kHz. A crosstab of `rates` × `condition` for PVALB WFDC2 would show whether the width difference in fig1l could come from sampling.
- figs5: the distinct `Virus` values. An exact `== "CN2039"` match would miss mixed labels; print `m1.Virus.value_counts()`.
- figs1a: per-day medians on `Genes_Detected`.
- fig5d (both claims): rerun with `Revised_subclass_label`.
- Neighbour and UMAP claims (fig1i, fig2b, fig3c, fig5d-dbc-ephys-intermingled): rerun on the paper's 84-column table for the same cells.
- figs1 reading (a): `condition2` fractions over all cells.
- fig4a: the list of morphology columns (`MFEATS`) was never printed, so I cannot tell which parts are testable from the table.
- fig5b: `Cortical_layer` for SST CALB1 and SST ADGRG6.
- figs2d: the orientation of `lm_pval` in the authors' R code (rows are terms or genes).
- I did not fetch the code-repository tables, so I cannot verify any value that comes only from them.
