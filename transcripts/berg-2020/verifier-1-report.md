**A. Outcomes** (all 33 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| features-and-labels-link | reproduced (M2); M1 not reproduced | M1 links 0 files (cell 12). Under M2, 318 files link to 318 distinct cells, and all 283 of the code's cells that have features have a file. The median relative difference is 0 for all 18 features over 282 cells, and a match on features alone picks the M2 cell 282 of 282 times. |
| cohort-cells | not_reproduced | 318 cells, not 385. 283 is not reached under any reading: (a) 307, (b) 256, (c) 306 (cell 16). |
| cohort-donors | not_reproduced | 56 under both readings, not 90 (cell 18). The pathology table has 89 distinct donors in 90 rows. |
| cohort-type-counts | not_reproduced | At most 2 of 6 counts match under any reading (cell 20). The criterion needs at least 3 for partial. |
| fig1a-thickness | reproduced | 1.231 ± 0.155 mm over 5 sections, inside 1.23 ± 0.15 (cell 60). The mouse value is untested, as the criterion says. |
| fig1b-density | partially_reproduced | Human 27.70 ± 4.46, highest in L2 and falling to 0.43× at −0.575 (cell 62). The mouse figure (349.8) comes from a faulty port (problem 2), so the mouse part was not validly tested. |
| fig1c-soma-area | partially_reproduced | Human quartiles 107.5/252.6 and largest soma 886 µm² pass (cell 64). Mouse quartiles 24.4/61.0 fail, but they come from the faulty port; the claims file says Code7 prints 44.7/96.5 from the same files. |
| fig1c-soma-variation | blocked (other) | The ratio is NaN because all 1419 mouse somata sit at scaled depth −1.0 (cell 65). This is a port fault, not missing data, so the claim is testable. |
| fig1f-frem3-heterogeneity | blocked (data_missing) | Not in the archive: it holds only 318 `*_icephys.nwb` files (checked through the API). |
| fig1g-deep-types-de-genes | blocked (data_missing) | Same reason. |
| fig3a-platform-correlation | blocked (data_missing) | Same reason. |
| fig2d-pathology-scores | reproduced | Donor averages run from 0.056 to 1.833, and 86.7% of donors are below 1.0 (cell 45). |
| edfig1-marker-correlation | reproduced | Ki-67 with Nissl (cellularity) has the largest \|r\| of the 15 pairs, 0.391 (cell 46). |
| fig2ef-pathology-ephys | partially_reproduced | Reading (a), temporal cells: only RMP under IBA1 is significant. The difference is −4.10 mV (medians) and −4.08 mV (means), both outside −5 ± 0.5 (cell 43). Reading (b) has 3 significant IBA1 features. Neither reading gives the paper's group sizes (60/125 and 170/15). |
| fig3d-depth-by-type | partially_reproduced | The median order holds and CARM1P1 and COL22A1 are at least 90% deeper than 0.575. No FREM3 cell is deeper than 1 (maximum 0.992), in the linked cells or in the full table (cell 22). |
| fig4e-human-ephys-anova | partially_reproduced | Features with R2 > 0.1 are input resistance, rheobase and first_isi_hero_inv; f-I slope has 0.087. Maximum R2 is 0.141, outside 0.16 ± 0.016 (cell 24). On the code's 283 cells the claim reproduces. |
| fig4e-mouse-ephys-anova | reproduced | Exactly the three named features have R2 > 0.1 at BH p < 0.05. Maximum R2 0.123 is within tolerance and below the human 0.141 (cell 26). |
| fig4f-morph-anova | reproduced | 16 human features (all at FDR < 1e-3) and 12 mouse features (10 at FDR < 0.05) (cell 48). |
| fig4-glp2r-sag | reproduced | GLP2R sag is above LTK (0.061 against 0.026, BH p 0.023). Adaptation does not differ (BH p 0.31) (cell 28). |
| edtable1-species-ephys | reproduced | 17 of 18 features under Student's and under Welch's test; width is the one not significant (cell 30). |
| edfig6-classifier-human-ephys | reproduced | 0.632 over 1000 splits, inside 0.67 ± 0.067. The paper states no chance level. Here the largest class is 0.580 and shuffled labels give 0.451, so the margin over chance is small (cell 33). |
| edfig6-classifier-mouse-ephys | reproduced | 0.571, inside 0.54 ± 0.054, and below the human 0.632. Largest class 0.491, shuffled labels 0.421 (cell 34). |
| edfig6-classifier-morphoelectric | reproduced | Human 0.720 and mouse 0.582 over 250 splits (SE about 0.006), both inside tolerance (cell 54). |
| fig5c-frem3-ephys-depth | partially_reproduced | 10 features at FDR < 0.05, outside 9 ± 0.9; 7 at FDR < 0.01. The top three features and their signs are right, but the upstroke/downstroke ratio has BH p 1.003e-7, not below 1e-7 (cell 36). |
| fig5b-frem3-morph-depth | reproduced | 37 and 28 of the 58 kept features (cell 49). |
| fig5d-frem3-gene-depth | blocked (data_missing) | The repository's table gives 4417 genes at FDR < 0.05. It is the revision's table; the preprint's results are not available anywhere (cell 56). |
| fig6-deep-ephys-anova | partially_reproduced | 15 features at FDR < 0.05 passes. 5 features have R2 > 0.4, against 4 ± 0.4; tau, at 0.412, is the fifth (cell 38). On the code's 283 cells: 14 and 4. |
| fig6c-carm1p1-upstroke-rin | blocked (methods_underspecified) | By upstroke rate, CARM1P1 is above both other types. By upstroke/downstroke ratio it is below COL22A1 (4.58 against 4.83). The criterion makes this part methods_underspecified when the two readings differ. The input resistance part holds (BH p 0.0019) (cell 40). |
| fig6c-col22a1-rin-fi-sag | reproduced | All 3 parts hold (cells 40 and 41). |
| fig6a-deep-dendrites | blocked (methods_underspecified) | Under reading (b) with medians, deep FREM3 has the largest total length (12024 µm, CARM1P1 10447). The other readings hold (cell 52). |
| fig6e-deep-de-genes | blocked (data_missing) | Not in the archive. |
| fig6f-smi32 | blocked (data_missing) | Not in the archive. |

**B. Problems**

1. [affects a conclusion] **Labels for 35 of the 318 files are unverified (cells 12, 14, 16).** M2 links each file to the next SpecimenID above its session id, which by construction links every file. So "files not matched to the table: 0" (cell 16) is circular, and the claims file's "other cells, counted apart" can never be found. The feature check covers only the 282 linked cells that have features in the code's table. The other 35 cells (25 of them with features here) take their t-type and depth from an unchecked match; offsets reach 685 against a median of 34. These cells are in every main analysis. Dropping them changes fig4e-human-ephys-anova from partial to reproduced and fig6-deep-ephys-anova from partial to reproduced (cells 24 and 38).
2. [affects a conclusion] **The mouse NeuN port in `section_tables` / `_layer_matrix` is wrong.** Mouse L2/3 thickness comes out as 32, 133 and 90 µm, against Code7's 281, 223 and 257 µm, which cell 57 itself names as the check. All mouse somata are clipped to scaled depth −1.0, and the pooled mouse quartiles (24.4/61.0) do not match Code7's 44.7/96.5. The soma areas do not depend on the boundary lines, so the soma selection or pixel scale is probably also wrong. This invalidates the mouse parts of fig1b-density and fig1c-soma-area and all of fig1c-soma-variation. Cell 0 blames "mouse section files" for the blocking, which is the wrong reason.
3. [affects a conclusion, possibly] **Cell QC is computed but not applied** (`extract_cell`; cell 10 shows 35 of 318 failing). The paper's Methods require seal, access-resistance and other cell-level QC. The link criterion names only sweep QC, which is an omission in the claims file, not a misreading of the paper. Of the 25 extra cells with features, 5 fail cell QC, and those cells feed problem 1.
4. [does not affect a conclusion] **Bin edges are handled inconsistently in `density_profile`.** Counts use right-closed bins (`searchsorted`), but the area and SD means use a left-closed mask, so somata clipped to exactly 0 are left out of the area and SD statistics. The human density matches Code6, so the effect is small.
5. [does not affect a conclusion] **fig2ef group sizes are not recovered** (cell 43). Under both readings the low/high counts differ from the paper's. The verdict function ignores the counts, which is consistent with how the criterion is written, but the paper's cell set is not reproduced.
6. [does not affect a conclusion] **Possible duplicate donor in the pathology table** (cell 43). It has 90 rows but 89 distinct `donor_id[:10]`. A donor with two rows could be put in both the low and the high group; this is not checked.
7. [does not affect a conclusion] **Fewer classifier splits than the criterion** (cell 54). The morpho-electric classifiers use 250 splits instead of 1000. The standard errors (≤0.007) are far smaller than the distance to the tolerance bounds.
8. [does not affect a conclusion] **fig3d uses a different cell set as its main run** (cell 22). It uses the 318 linked cells, while the criterion names every cell of the code's table. The full-table variant gives the same verdict.
9. [does not affect a conclusion] **Donor metadata mismatches are noted but not followed up** (cell 12). H18.03.318 is female in the file and male in the tables; H18.06.005 differs in age.
10. [does not affect a conclusion] **Tolerances on small counts are effectively exact.** The claims file's 10% tolerances on small integers (4 ± 0.4, 9 ± 0.9) leave no room. This decides fig6-deep-ephys-anova and fig5c-frem3-ephys-depth, but it follows the claims file.

**C. What I could not check, and what would have let me**

- **Helper functions on synthetic inputs.** numpy, scipy and statsmodels are not installed here, so I checked `ols_hc3`, `bh`, `pairwise_mw` and `mw_scipy14` by reading only.
- **Whether the 35 unchecked links are right.** Needed: a per-file table of M2 offset and gap, split by whether the cell is in the code's feature table, plus every main analysis re-run without those 35 cells and with cell QC applied.
- **Why the mouse port fails.** Needed: the per-section boundary-line y positions and line order, and per-case soma counts and area quartiles, set against Code7's printed values.
- **Whether sweep QC worked as the Methods say.** Needed: the reasons sweeps failed QC, and confirmation that the bias-current criterion was used, given that long-square bias currents run from −284 to 195 pA and 1165 sweeps have no value. The IPFX version should also be printed.
- **The archive for the blocked claims.** The API confirms 318 human `icephys.nwb` assets across 56 subjects and no other file types. Asset metadata carry only subject id, session id, sex and age: no SpecimenID, t-type or depth. So none of the archive-blocked claims (fig1f-frem3-heterogeneity, fig1g-deep-types-de-genes, fig3a-platform-correlation, fig5d-frem3-gene-depth, fig6e-deep-de-genes, fig6f-smi32) can be tested from it. fig1c-soma-variation is testable from the code repository once the port is fixed.
