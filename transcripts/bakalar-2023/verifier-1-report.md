**A. Outcomes**

The claims file has 27 claims. The notebook tests 3 and treats 24 as blocked.

| Claim | My outcome | Reason |
|---|---|---|
| fig5-dg-fos | blocked: methods_underspecified | The readings of (1) to (3) disagree. Under the main rule (cell 12) they give 12 reproduced, 3 partial and 5 not; under the every-component rule (cell 13) they give 15, 2 and 3. The criterion says that case is blocked. The reading closest to the paper (density, IQR within genotype) is reproduced at all 5 thresholds, with DG-sg and DG-po p_adj between 0.001 and 0.035. The pooled-IQR readings fail at 10000 to 12000. |
| table4-lenient-regions | partially_reproduced | All 20 main readings and all 20 every-component readings give partial (cell 19). IGL is always at p ≤ 0.01 with PACAPko higher. SNr meets the cutoff in most readings. STN meets it only at 4000 density under the main rule (more often under the every-component rule). The number of other regions at p ≤ 0.01 is within 13 ± 1.3 in only one reading (8000 raw pooled, 13). |
| table4-region-values | partially_reproduced | All 13 directions match in every reading (cell 22), including DTN below 100%. At most 1 of 13 regions has both U and % within tolerance at 22 hemispheres, and at most 8 in the paper-sized subsets (cell 24). This is short of the 10 needed. |
| fig2a-pca-components, table3-pca-loadings, fig2a-two-trajectories, fig2b-pc-index-behaviours, fig3a-travel-development, fig3b-jumping-development, fig4-wheel-repetitive-jumping | blocked: data_missing | I listed the archive's assets: 765 files, all CATNIP light-sheet derivatives plus the raw stacks and BIDS sidecars. There is no Homecage Scan data. |
| fig6-ihc-fos-confirmation | blocked: data_missing | The archive has no IHC section images or counts. |
| fig7a-adult-induction-adcyap1, fig7b-postnatal-induction-adcyap1, fig7-cprg-expression | blocked: data_missing | The archive has no qRT-PCR data. |
| fig8-induced-ko-no-hyperlocomotion, fig10a-baf53b-no-hyperlocomotion, fig11-placental-pacap-no-effect | blocked: data_missing | The archive has no behaviour data. |
| fig9-postnatal-ko-pvn-fos, fig10c-baf53b-ish-knockdown | blocked: data_missing | The archive has no RNAscope or HCR images. |
| fig10b-baf53b-restraint-weight-loss | blocked: data_missing | The archive has no body weights. |
| fig12b-pacapko-fasting-hypothermia, fig12b-pacapko-higher-tb, fig12d-pacapko-more-active, fig13a-sim1-tb-unchanged, fig13b-sim1-activity-unchanged, fig13c-pac1ko-tb-unchanged, fig13d-pac1ko-activity | blocked: data_missing | The archive has no telemetry. No part of any of these 24 claims can be tested from this dandiset. |

**B. Problems**

1. **[affects a conclusion] Thresholds (`fos.THRESHOLDS`, cells 6 and 10).**
   - Reading (1) of the claims file says to run "every threshold the derivatives hold". The notebook runs only the 5 that all 22 hemispheres share.
   - Not run: 14000 to 40000, which exist for 18 hemispheres, and 2000, 3000, 5000, 7000, 9000 and 11000, which exist for 4.
   - p for SNr, STN and IGL rises with threshold. At 12000 raw, IGL is already at 0.009. Higher thresholds could therefore produce "not" readings for table4-lenient-regions, so its uniform "partial" is untested beyond 12000.
   - 4 hemispheres (45925flox L, 45926flox R, 45478ko L, 45670ko L) were re-segmented on a finer 2000 to 12000 series. That points to thresholds chosen per hemisphere ("which threshold(s)", Supplemental Methods). This reading is neither run nor stated as an assumption.
2. **[affects a conclusion, plausibly] Artifact mask not handled.**
   - The Supplemental Methods and the criterion say counts of regions overlapping an artifact mask are ignored. The notebook neither implements nor mentions this.
   - The archive holds no mask files. It does hold `HeatmapsAtlasSpaceCorrected` for two hemispheres (45670ko L, 45925flox L), which the notebook never examines.
   - Whether any regions should have been dropped is unknown.
3. **[does not affect a conclusion] Region set (`fos.regions`, cell 4).**
   - The colour-based grouping leaves 497 labels after removing tracts, nerves and ventricles; the paper has 462. It ends with 438 regions; the paper has 431.
   - The 35-label gap at the first step shrinking to 7 at the end suggests misclassifications that partly cancel.
   - Parent labels such as HPF and HY are included and come out significant at 4000 (cell 14).
   - The effect on the BKY count is small (438 vs 431).
4. **[does not affect a conclusion] Masked vs unmasked labels (`fos.label_path`).**
   - 6 hemispheres fall back to unmasked `AtlasLabel`, 5 of them PACAPko (45467ko R, 45469ko L/R, 45476ko R, 45670ko R) and one control (45930flox L). So the region-volume definition is unbalanced between genotypes.
   - The count tables for 45467ko R and 45469ko R match the unmasked volumes, so CATNIP did the same.
   - The notebook never shows how much this shifts the densities.
5. **[does not affect a conclusion] U is not comparable at 22 hemispheres (cells 12 and 22).** The maximum U is 12 × 10 = 120, against 88 in the paper. Only the subset analyses (cells 17 and 24) make the U tolerances meaningful, and they give partial anyway.
6. **[does not affect a conclusion] Slab edge handling (`fos._components`).**
   - I tested it on a synthetic 300-plane volume against `scipy.ndimage.label` with 26-connectivity and majority-label assignment.
   - Region volumes and the 9 to 900 voxel counts matched exactly. With every component counted, one component of 731 was lost and one too many was counted as dropped, apparently because a component split by the slab boundary is counted twice.
   - The notebook reports a dropped fraction of 1.5e-4.
   - `iqr_keep` and `region_tests` behave correctly: complete separation at 11 vs 8 gives U = 88 and p = 2/C(19,8) = 2.65e-05.
7. **[does not affect a conclusion] Count-table variant has little power (cell 16).** This variant uses 13 hemispheres, 7 vs 6. Its uniform "not" reflects that: the smallest possible raw p is 2/C(13,6) ≈ 1.2e-3, tested across 438 regions. It is not evidence against the claim.
8. **Claims file.** I found no misreading of the paper. The units (voxel 6.845e-08 mm³), the exact two-sided test, the PACAPko U, and `fdr_tsbky` at α = 0.05 and 0.1 all follow the claims file and the Supplemental Methods.

**C. What I could not check**

- **The recount itself.** I can't re-run it. It agrees with the dataset's count tables to a median of 1.25% per region (cell 7), but that check covers only the every-component rule; nothing in the data validates the 9 to 900 voxel rule.
- **Higher thresholds.** Needed output: results at 14000 to 40000 on the 18 hemispheres that have them, and a run that uses each hemisphere's own threshold series.
- **Masked vs unmasked labels.** Needed output: DG-sg and DG-po densities under masked and unmasked labels for the 10 hemispheres that have both.
- **Region list.** Needed output: the 438 included acronyms, and the 59 labels excluded beyond tracts and ventricles, to compare against the paper's 431.
- **Corrected heatmaps.** Needed output: a comparison of `HeatmapsAtlasSpaceCorrected` with `HeatmapsAtlasSpace` for the two hemispheres that have both, to see whether it marks an artifact exclusion.
