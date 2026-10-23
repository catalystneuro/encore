I've revised the attempt for all the round-1 points, and four outcomes changed. I re-ran the entry twice with `tools/entry.py all`; both runs pass in 14.3 minutes and give the same numbers, and the check reports 0 errors. Every conclusion, the summary, the README and the attempt record now match the new output. The round is recorded under `verifications`: the verifier's outcome matches the record on 26 of its 32 claims, and its report gives no outcome for fig6-deep-morph-anova, so that claim is left out.

**Outcome changes**
- **fig1b-density, fig1c-soma-area:** partially reproduced → reproduced. **fig1c-soma-variation:** blocked → reproduced (ratio 3.94, expected 4 ± 0.4). The verifier was right that the mouse part of the section port was faulty. My port followed Code7 as committed, but that version doesn't give the values its comments print. Two changes make it give every one of them: reading the four mouse boundary lines the way Code6 reads the human ones, and putting case_set_1 at 165 pixels per 100 µm, the scale Code7's own comment gives. The printed values are mouse L2/3 thickness 281/223/257 µm, density 164.7 ± 24.9, and soma-area quartiles 44.7/96.5. The finding now says the script, not the data files, is at fault.
- **fig6-deep-ephys-anova:** partially reproduced → reproduced (14 features at FDR < 0.05, 4 with R² > 0.4). The verifier asked whether the bias-current limit was applied. It wasn't: IPFX 2.1.2 checks only noise and a Vm-delta limit per sweep, and skips the Methods' bias-current and bridge-balance limits, even though the old helper docstring said it applied them. The link criterion asks for the Methods' sweep QC, so I added those two limits. IPFX's own QC is kept as a variant, under which this claim stays partial (15 and 5).

**What I added or corrected**
- **The 35 links the features can't check:** a table of each file's link offset and its gap to the next candidate cell. Two checks that don't use features support these links without proving them:
  - The date in each cell's sample ID equals the file's local recording date for all 35.
  - Within each rig and day (71 groups, 253 files), tube numbers rise with recording time without exception.

  The cohort text now says the link method gives every file a cell, so it can't find cells outside the table.
- **Sensitivity section:** every electrophysiology verdict rerun on seven cell sets (sweep QC choice, the code's 283 cells only, with or without cell QC), plus a classifier check on three of them. Some outcomes do move:
  - Dropping the 35 cells makes fig2ef not reproduced.
  - Applying cell QC makes fig4-glp2r-sag not reproduced (sag BH p 0.060).
- **Smaller fixes:** the notebook now prints the IPFX version, why sweeps failed QC, and the bias-current figures. fig3d's judged cell set is now the code's full table, as the criterion says. The donor with two pathology rows has no file here. The area-bin inconsistency is Code6's and Code7's own, so I kept it and printed a variant with consistent bins.
- **Findings:** one new code_mismatch. The paper's feature table looks like it used noise-only sweep QC: with the Methods' limits, 22 of its 283 cells give no features here (1 with IPFX's QC alone). Also, 29 of the 283 fail cell QC as IPFX computes it. I updated the other findings with the new numbers.

**What I did not do, and why**
- **Blocking reason for six claims:** I kept `other` instead of the verifier's `data_missing` for fig1f, fig1g, fig3a, fig5d, fig6e and fig6f. The claims file marks them `elsewhere`, and the protocol and `entry.py check` reject `data_missing` for those. The disagreement is recorded.
- **Dropping the 35 cells:** I didn't remove them from the main analysis, as the verifier suggested for fig4e-human and fig6-deep. The claims file's analysis cells include them and their links are now supported. Under the Methods' QC, fig4e-human stays partial even on the code's 283 cells alone.
- **Cell QC:** not applied in the main analysis, because the claims file asks for sweep QC only. I added two questions to `questions/000023.yaml`: whether cell QC applies, and which input resistance the 15% bridge-balance limit means. The second also covers whether the bias-current and bridge-balance limits belong at all.
- **Classifier splits:** the morpho-electric classifier stays at 250 splits instead of 1000, a recorded deviation; the standard errors are 0.007 or less.

Nothing was committed or pushed.
