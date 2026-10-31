**Verifier report, round 1: Chartrand et al. 2023 (doi:10.1126/science.adf0805) on DANDI:000630 0.230915.2257**

Materials checked: the claims file has 41 claims (15 `with_labels`, 8 `with_inputs`, 18 `elsewhere`). I read three executed notebooks: `reproduce_chartrand_2023.ipynb` (R), `mouse_comparison.ipynb` (M) and `morphology_tables.ipynb` (Mo). I ran the helper statistics on synthetic data in a temporary environment, and they behave correctly: `dprime_auc` returns 1.03 for a true d′ of 1; `run_kw_dunn` gives epsilon² = H/(n−1); `run_twosamp` gives exact p of 9.9e-5 for 2 against 200 cells; `run_correlations(filter_dropouts=True)` drops any feature with no values above 1.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| dandiset-cell-link | partially_reproduced | R c14: all 210 files match 210 distinct rows. Sex agrees for 209/210 (one file says "unknown"). Age agrees for 207/208, with one off by 1 year under the notebook's own floor(x+0.05) rounding. 39 of 44 computed features agree within 1% for at least half the cells. The criterion asks every record to agree, so this is partial (≥90%). |
| mouse-cell-link | partially_reproduced | M c5: 250 of the 272 strict mouse cells (91.9%) have a file in 000020, and all 250 names match. Most features agree within 1%. |
| patchseq-counts | reproduced | R c20: 194 cells, and 96/35/33/15/15 by subclass, all exact. No dandiset file is outside P. |
| fig2c-subclass-ephys-differences | partially_reproduced | R c22, reading (a), which is O1's primary reading: sag FDR p 6.6e-20, but first_isi_inv_hero FDR p 4.7e-7, which is not below 1e-7. Reading (b) passes both (1.7e-8). |
| fig2b-subclass-ephys-profiles | reproduced | R c25: (i), (ii) and (iii) all hold under both readings. |
| figs3a-sag-adaptation | not_reproduced | R c28: R² is 0.334 (a) and 0.359 (b), against 0.74 ± 0.074. The t-type-median variant gives 0.28–0.31. p < 1e-13 holds only in (b). |
| fig2c-lamp5-gradient | partially_reproduced | R c30: first_isi_inv_hero has FDR p 2.6e-5 with positive rho. Sag has positive rho but FDR p 0.022 (a) and 0.0020 (b), and 0.0039 in the three-site variant; it needs < 0.001. First-ISI medians are not monotone (DBP 18.6 < LCP2 22.5). |
| figs6-donor-condition-ephys | reproduced | R c32: no feature reaches FDR p < 0.05 for condition, sex or age under either reading. Smallest uncorrected p: sag 0.0027 (condition), rheobase 0.011 (sex), peak_deltav_hero 0.039 (age). |
| figs6c-region-ephys | reproduced | R c34: input_resistance_ss FDR p 0.029. The only region with a median below MTG is SFG (222 vs 234), with Dunn p 0.13. |
| fig4b-mc4r-sag-irregularity | reproduced | R c36, reading (a), MC4R subclass: sag FDR 1.6e-18 and ir_late_mean FDR 1.2e-5, both higher in MC4R. ADARB2 MC4R alone also passes. |
| fig4b-adarb2-irregular-firing | not_reproduced | R c38: (i) fails, because ADARB2 against CHRNA4 on ir_late_mean has Dunn FDR 0.18. (ii) fails, because CHRNA4 is above LAMP5 with FDR 0.046. (iii) and (iv) hold under both readings of "faster". |
| fig5b-tnfaip8l3-ephys | reproduced | R c40: first_isi_inv_rheo FDR 0.0081 / 0.0077 and postap_slope_rheo FDR 0.0051, both higher. This rests on n=2, and postap_slope comes only from the paper's table. |
| fig6a-ephys-dprime-subclass-structure | partially_reproduced | R c42: mean within-subclass d′ is below between-subclass d′ in all 6 runs. NMBR/LCP2 is the only high within-subclass pair under "≥2.2" in 4 of 6 runs (only seed 0 under (b)). Under "above median between" no within pair is high, so the criterion's "both readings" condition fails. |
| fig6d-gmm-subclass-f1 | reproduced | R c44: all four F1 values are within tolerance under both O3 readings (lowest margin: all others 0.490 against a floor of 0.45). Run on feature reading (a) only. |
| figs8a-classifier-cv | reproduced | R c46: accuracy 78.8–84.6% and balanced accuracy 74.5–78.8%, all within 82 ± 8.2. Chance is 52.4% for the majority class and 25% balanced; the paper states no chance level. |
| figs8b-classifier-holdout | blocked (data_missing) | All 210 files are AIBS (R c3, c17), and the archive confirms it. See C for possible other deposits. |
| fig3d-ephys-species | blocked (methods_underspecified) | M c8: directions and the within-subclass condition hold under both O2 readings. peak_deltav_ramp has species FDR 2.6e-38 under O2 (a), against 1e-38 required, and passes under (b). The readings disagree, so the criterion's rule applies. Substantively it is partial or full. |
| fig3e-tea-validation | blocked (data_missing) | No public mouse TEa electrophysiology; a DANDI search for "TEa" finds nothing relevant. The Allen TEa subset is unchecked (C). |
| fig3f-a-type-conductance | blocked (data_missing) | Patch diameters and mouse nucleated-patch recordings are missing. The human nucleated-patch sweeps are in the dandiset (problem 10). |
| fig3g-variability-dimensions | reproduced | M c10: (i) and (ii) hold under both readings. Selection deviates from the claims file (problem 4). |
| fig4d-mouse-no-rosehip-ephys | not_reproduced | M c12: MC4R sag is above LAMP5's. But only 15 of 30 irregular cells are LAMP5 (not "most"), and the largest group is Lamp5 Plch2 Dock5 (8), not Ntn1 Npy2r (6). Both fail under both readings. 11 L1 VIP cells are irregular. |
| fig5d-mouse-pax6-doublets | not_reproduced | M c14: PAX6's sag_depol median is the highest, but its first_isi_inv_hero median (97.7, n=2) is below L1 VIP's (171). |
| fig6b-dprime-correlation | blocked (other: not attempted) | The data are public (Zenodo), so this is not a data block. |
| fig2d-subclass-morphology | partially_reproduced | Mo c4: dendrite orientation FDR 2.0e-4 and axon extent 4.1e-4 pass; dendrite branches 3.4e-3 misses 1e-3. Tested on the paper's deposited features, not the dandiset. |
| fig4b-mc4r-axon | partially_reproduced | Mo c6: branch frequency FDR 1e-6 passes; max path distance FDR 0.0029 misses 1e-4. |
| fig5b-tnfaip8l3-dendrites | partially_reproduced | Mo c8: extent FDR 0.017 passes and both cells exceed 550 µm, but one other cell is at 571 µm. Branches FDR 0.085. |
| figs6a-tumor-dendrite-branching | blocked (metadata_insufficient) | Mo c10: 51 of 71 cells have no condition in the public table, and the MTG LAMP5 control cannot be run. |
| fig3b-l1-cytoarchitecture | blocked (metadata_insufficient) | This is the notebook's stated reason (unpublished scanner resolutions). I could not verify it. |
| fig1a, fig1b, fig1d, fig1e, figs2a, figs1d, fig3d-morphology-species, figs3c, figs3g, figs3e, fig4c, fig5c, fig6c (13) | blocked (other: not attempted) | `elsewhere` claims the attempt did not run. Not data_missing: fig1e is testable from the label tables already loaded (problem 10). |

### B. Problems

1. **figs3a, claims-file misreading** [does not affect a conclusion]. The paper says only "inverse relationship" (Fig. S3A legend). With the ratio as third over first, which matches the paper's table (R c15), the data show that more sag means a lower ratio, so a larger drop in upstroke. That is the opposite of the claims file's "less change". R c28 never states the direction. The outcome fails on R² regardless.
2. **R c16, how reading (a) is built** [affects a conclusion: fig2c]. The rule "use the computed feature if at least 50% of cells are within 1% of the paper's value" is the author's own and is not stated as an assumption tied to the claims file. In first_isi_inv_hero, 14% of cells disagree and are never inspected. That disagreement is what moves fig2c from reproduced to partial.
3. **Inconsistent "soma in L1" selection** [may affect fig6d, figs8a, fig3d]. R c44 and c46 use the depth-table `layer` only, giving 164 core cells. M c6 fills missing values from `layer_lims` "as the code does", giving 176. Only one of these can match the code, and the other was not run.
4. **M c8 and c10 use all visual areas (`M.vis`)** where the claims file says VISp for fig3d and fig3g [likely does not affect]. About 49 of the strict cells are non-VISp, and the effect was not shown.
5. **M c6 builds the mouse tables only from the 250 cells that have files**, even under reading (b), where the paper's values exist for all 272 [may affect fig4d]. fig4d's LAMP5 share sits at exactly 15/30. This may also explain why fig5d lists 3 Lamp5 Krt73 cells where the claims file says 4; the missing cell is unexplained, but it cannot change fig5d.
6. **R c30, fig2c-lamp5-gradient, uses `filter_dropouts=False` without saying why**, although the code's default is True [does not affect]. Under True, sag (all values below 1) would be dropped entirely. The sag p-value under (a), 0.0064 uncorrected, cannot reach 0.001 under any correction.
7. **R c32, figs6 donor condition** [does not affect the outcome, weakens it]. Medical condition is missing for 108 of 194 cells, so this absence-of-effect test has little power. The dropout filter the claims file requires leaves 36 of 92 features for age, so sag and all ratio features are never tested against age. Neither point is stated as a limitation.
8. **R c44 and c46, GMM and classifier, run only on feature reading (a)**, despite R c0 saying "Every analysis is run on both" [does not affect, given the margins].
9. **`pairwise_dprime` and `preproc_pipeline` fit scaling, imputation and LOF on all cells before cross-validation** [does not affect]. No labels are used, so there is no label leakage, and the code does the same. The classifier in R c46 fits these steps inside the folds, which is correct.
10. **The blocked statuses in the R c0 table are partly inaccurate** [affects blocked claims].
    - fig3f: the "not in the files" reason is wrong for the human half. Nucleated-patch voltage-clamp sweeps (`NucVCLS0`, 38 files; `NucVCLS1Leak`, 35) are in the dandiset (R c5), and the archive summary lists VoltageClampSeries. Human IKA and IKD conductances could be computed; per-area density and the mouse side are missing.
    - fig1e: testable from the label tables the notebook already loads (`labels`, `mlabels`).
    - fig6b and fig3d-morphology: their inputs are public.
11. **R c14 matches age with an ad hoc floor(x+0.05) rounding** [does not affect]. One mismatch remains.

### C. What I could not check, and the output that would have let me

- Whether IPFX extraction and sweep QC are right in detail (I did not download any files). Would help: for each computed feature, the cells outside 1% with both values and the rheobase and hero sweep amplitudes from each side, especially for first_isi_inv_hero.
- Which "layer" rule the code uses, and how fig6d, figs8a and fig3d change under the other rule. Would help: both counts and both results.
- fig3d and fig3g restricted to VISp. Would help: re-running both on VISp cells only.
- fig4d and fig5d on all 272 strict mouse cells using the paper's values. Would help: that re-run, plus the specimen ids of the 22 cells without files and the missing fourth Lamp5 Krt73 cell.
- figs3a direction. Would help: the slope with the ratio order and its sign spelled out against the paper's Fig. S3A.
- The one donor whose age disagrees. Would help: its raw days and its table value.
- figs8b: DANDI 000228 (Tamás and Molnár contributors, "U01 Lein PatchSeq") and 000337 (Mansvelder lab human patch-seq) may hold the Szeged and Amsterdam held-out cells. I could not match their cells to `tamas_features_E.csv` or `mansvelder_features_E.csv` without the tables. Would help: cross-referencing those dandisets' session ids with the label table.
- fig3e and fig3f: whether 000020 holds Allen mouse TEa cells or mouse nucleated-patch (`NucVC`) sweeps. Would help: the stimulus-code counts M c3 already computed (`m_feats.codes`), and the structure counts for 000020.
