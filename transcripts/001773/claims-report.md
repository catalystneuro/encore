I wrote the claims file: `claims/001773/10.1038-s41593-026-02301-4.yaml`. The checker passes every quote and the schema. It exits non-zero only because it can't find 8 p-values, and I confirmed each of those by reading it in the text: they are printed with thin spaces, as the garbled "9.10 × 10 −1 3", or as Supplementary Table 9's E-notation and 9-digit values.

**Text read.** The version of record (open access, PMC13337501, from Europe PMC): main text, figure legends, Methods and Extended Data legends 1 to 10. The supplement was extracted into the same `.txt`: Supplementary Methods 1 to 7 and Supplementary Tables 1 to 11. The supplement the earlier run reported missing is now there. There is no PDF of the main article, and no figure needed one.

**Code not read.** The paper's MATLAB fMRI scripts are deposited inside dandiset 001773 itself, which a reader may not open. Every criterion therefore rests on the Methods, legends and supplement. The opening comment asks the author to check that code for the details listed below as open, and to ask a reader.

**Counts.** 32 claims: 31 have quotes and 1 is `inferred` (the per-ROI significance counts, taken from Supplementary Tables 1 and 2). 21 claims have statistics, 32 have criteria and 12 have expected values. All are `data: dataset`. The archive describes the dataset as "Data and code (fMRI, DWI IF, EM, behavior)", about 3.2 MB.

**Details fixed from the paper.**
- **ANOVA models:** the error df printed in the paper match full-factorial three-way ANOVAs plus a monkey main effect, and none for monkey D. Tukey–Kramer runs over all cells (MATLAB multcompare).
- **"One-way ANOVA with monkey as fixed effect":** its df match a model with condition, monkey and their interaction.
- **Hub networks:** the voxel counts of each network equal the sum of its hub ROIs' counts in Supplementary Table 8.

**Details the paper leaves open, with the readings named:**
- **One-way ANOVA model:** (a) with the condition × monkey interaction, which matches the df; (b) the additive model.
- **Sum of squares type:** type III (MATLAB's default); type II run as a variant.
- **Seed maps:** correlations computed per run and averaged, or on concatenated runs.
- **LIM network:** with area 25 (matches the reported n = 821) or without it (the Methods list).
- **Fig. 4b rank-sum test:** pre against post values, or the changes against zero. For the threshold: whether the listed P values are Bonferroni-adjusted, or raw at P < 0.01. Whether the ROI's own diagonal entry is included (121 or 122 values).
- **Fig. 4a pattern:** block means of the difference connectome, or the median of per-ROI mean changes.
- **Pre-stimulation SCC connectivity signs:** ROIs of the stimulated hemisphere only, or both hemispheres.
- **Voxelwise cluster maps (nonsurgical controls, monkey D):** the test is not named (run-level two-sample or subject-level one-sample), nor the cluster neighbourhood.
- **Monkey D paired t-test:** how fields are paired across hemispheres.
- **Monkey D network reductions "not observed":** sham side only, or both sides.
- **Monkey D behavior:** the paper reports no test; the claim uses the Methods' ANOVA applied to monkey D.
- **CB subregions:** what "adjacent" to each area means; the legend's voxel counts serve as the check.

**Missing from the paper:**
- **Fig. 4c:** the network membership of the 122 ROIs is not given. That claim is blocked unless the deposited code supplies it.
- **Fig. 6d:** the lead location is given only as images, so that claim may be blocked for lack of metadata.

**Paper inconsistencies** (recorded in the opening comment):
- Supplementary Tables 3, 4 and 11 (effect sizes for three different groups) are identical, and their values don't fit the P values of Table 1.
- Some P values listed as Bonferroni-significant exceed 0.01/122.
- The Fig. 6a P (0.0025) matches F(2,1238), not the printed F(1,1238).
- Area 25 is described as a target on one side only but is listed on both sides.
- Table 9 shows a significant change in control-side MT, while the Results say "no change ... in areas within the VIS".
- Extended Data Fig. 10d says the post scan was 10 weeks after implantation; the Methods say 6.

I did not commit anything.
