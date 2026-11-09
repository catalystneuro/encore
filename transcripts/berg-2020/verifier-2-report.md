**Round 2 verification: Berg et al. 2020 on DANDI:000023 (attempt 000023-berg-2020-01)**

**1. Outcomes**

The claims file and the attempt record each hold 33 claims. The record gives 18 reproduced, 4 partially reproduced, 3 not reproduced and 8 blocked.

- **I agree, with no caveat (22 claims):** features-and-labels-link (M2), cohort-cells, cohort-donors, cohort-type-counts, fig3d-depth-by-type, fig4e-human-ephys-anova, fig4e-mouse-ephys-anova, edfig6-classifier-human-ephys, edfig6-classifier-mouse-ephys, edfig6-classifier-morphoelectric, fig5c-frem3-ephys-depth, fig6c-carm1p1-upstroke-rin, fig6c-col22a1-rin-fi-sag, fig2d-pathology-scores, edfig1-marker-correlation, fig4f-morph-anova, fig5b-frem3-morph-depth, fig6-deep-morph-anova, fig6a-deep-dendrites, fig1a-thickness, fig1b-density, fig1c-soma-area.
- **I agree under the claims file as written, but the result is fragile (4 claims):**
  - fig4-glp2r-sag: sag BH p is 0.046. With the Methods' cell QC it is 0.060, and the claim is not reproduced (cell 61).
  - edtable1-species-ephys: with cell QC, Student's test gives 16 and Welch's 17, so the outcome becomes methods_underspecified (cell 61).
  - fig6-deep-ephys-anova: tau has R2 0.395, just under 0.4, and the count of 4 has a tolerance of 0.4. With IPFX's sweep QC the counts are 15 and 5; with cell QC they are 12 and 4. Both give partially reproduced (cells 50 and 61).
  - fig2ef-pathology-ephys: this is partially reproduced only under reading (a) on all linked cells. On the code's 283 cells it is not reproduced (cell 61).
- **I agree (1 claim):** fig1c-soma-variation. The ratio is 3.94, within 4 ± 0.4. The claims file says Code7 prints 4.0; the notebook never compares the two.
- **I agree they are blocked (6 claims):** fig5d-frem3-gene-depth, fig1f-frem3-heterogeneity, fig1g-deep-types-de-genes, fig3a-platform-correlation, fig6e-deep-de-genes, fig6f-smi32. The claims file marks them `elsewhere`. I can't see the protocol rule the author cites, but "other" is consistent with that marking, so I no longer press data_missing.

**2. Sentences the printed outputs do not support**

- **Run times.**
  - Cell 0 and the README say "took 14 minutes in its last run … about 5 to read and analyse the 318 files … about 6 for the two electrophysiology classifiers … about 2 for the morpho-electric". The outputs show 21.0 min in total (cell 98), 7.2 min to extract (cell 8), 4.9 + 4.3 min for the classifiers (cells 42 and 44) and 3.5 min for the morpho-electric classifiers (cell 79).
  - Cell 7 says "This takes about 9 minutes"; the extraction took 7.2 min (cell 8).
- **How far the features confirm the link.**
  - Cell 97 says the link is one "which the features confirm for the 283 cells with features in the code".
  - The record's deviation says "the code's per-cell features confirm the match for the 283 cells that have them", and its identifier_missing finding says "confirm the link for every cell that has them".
  - Under the main QC (the Methods' sweep QC), only 261 of the 283 have features on both sides. The feature-only match is 261 of 261 (cell 12), and 22 of the 283 give no features here (cell 17). The IPFX variant prints only median agreement; it runs no per-cell match.
- **The one cell missing under IPFX's QC.** The record's cohort-cells note says "(IPFX fails on its f-I fit)". Cell 10 shows that cell's error as "ValueError: `ydata` must not be empty!", which does not name the f-I fit.
- **Port fidelity.**
  - Cell 84 lists Code6's printed human L2 fractions as −0.179 to −0.199. Cell 85 gives −0.1639 for case_316, and the mismatch is not mentioned anywhere.
  - Cell 94 says "equal to the quantiles Code7 prints". The record says "all eight pooled quantiles equal those Code7 prints", and its code_mismatch finding says the port "reproduces every printed value". Code7's printed values beyond 44.7/96.5/107.5/252.6/886 are never printed for comparison. Code7's soma-variation ratio (4.0 per the claims file) is not matched: the port gives 3.94 (cell 95).
- **Verification block.** "Of the 32, its outcome matches the record's on 26" is true only of the round-1 record. Against the current record it is 22: fig1b-density, fig1c-soma-area, fig1c-soma-variation and fig6-deep-ephys-anova have since changed. The `agrees: true` entries for those four need the same qualifier.

The record states my round-1 reasons faithfully, mostly in my own wording, and folds problems 1–4 and 10 into the right claims. All other conclusion, Summary, README and record sentences I checked match the outputs.

**3. Round-1 points**

Resolved:
- **Problem 2, the mouse port.** It now gives Code7's printed thicknesses, L2 fractions, density and quartiles. The case_set_1 scale (165 px per 100 µm) is a reconstruction based on Code7's own comment, and it is disclosed.
- **Problem 4, bin edges.** The right-closed variant is printed and gives 3.94 too.
- **Problem 6, the duplicate pathology donor.** It has no file here.
- **Problem 8, the fig3d cell set.** The judged run now uses every cell of the code's table.
- **Problem 9, donor metadata.** It is recorded as a finding.
- **Section C, the sweep QC request.** The IPFX version (2.1.2), the failure reasons and the bias currents are printed, and the Methods' limits are added.

Still open, and bearing on a conclusion:
- **Cell QC is not applied (problem 3).** The paper requires it as a condition for including a cell (paper line 179). The claims file's link criterion names only sweep QC. That is an omission in the claims file, not a misreading of the paper. Applying it moves fig4-glp2r-sag, edtable1-species-ephys and fig6-deep-ephys-anova.
- **The 35 links without features (problem 1).** The date check (35 of 35) and tube order (27 of the 35) support them but do not prove them. Dropping them makes fig2ef-pathology-ephys not reproduced.
- **Which sweep QC to use.** The code's table matches IPFX's QC alone better: 145 cells against 128 identical on every shared feature, and 1 against 22 of its cells without features here. So the Methods' limits as applied here are not what made the paper's numbers. The largest single reason sweeps fail is the 15%-of-Rin limit (469 sweeps), which uses an input resistance the Methods do not fix. In addition, 1118 sweeps have no bias-current value and are kept. This choice alone turns fig6-deep-ephys-anova from partial to reproduced.
- **Exact small-count tolerances (problem 10).** They still decide fig6-deep-ephys-anova (4 ± 0.4, tau at R2 0.395) and fig5c-frem3-ephys-depth (8 against 9 ± 0.9).

Open, but not bearing on a conclusion: problem 5 (the fig2ef group sizes are still not recovered), problem 7 (250 splits, with standard errors printed), and the run-time and port-fidelity wording in section 2.
