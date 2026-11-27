**Verification report: lee-2023 (doi:10.1126/science.adf6484) on DANDI:000636 0.241120.0510, round 2**

The claims file has 46 claims, and the attempt record has 46 outcomes with matching ids: 20 reproduced, 10 partially_reproduced, 4 not_reproduced and 12 blocked. The new claim is mouse-label-link. It and the new `depends_on` entries on fig6c and fig6e were added after the claims file's only check (2026-10-23), and no check entry covers them. A second reader has therefore not checked this claim.

### 1. Outcomes

**I agree with these outcomes as stated:**
- cell-metadata-link, dataset-composition
- fig1b, figs1a, fig1d
- figs1: blocked; readings (a) and (b) disagree, as the criterion foresees
- figs2d, fig5a, figs7a-regions, figs7a-markers
- figs2b, fig1l, figs2c
- fig1i: feature space fails at 0.43 on every seed, and still fails (0.45) with the paper's 19 features added
- fig2f, fig2g, fig2h, fig3c, fig3e, figs6
- fig4a: partial is defensible, but the failing trait rests on one basket cell (1.55 against DBC 1.91)
- fig4d: the cluster part fails under the main reading, as the criterion requires
- fig5c
- fig5d-dbc-ephys-intermingled: feature space fails under both labels and all feature sets (2.54 to 3.42)
- figs5, fig1g, fig2c, fig2e, fig3g, fig1h
- mouse-label-link, fig6e
- fig6c: Sst 5 fails clearly in both spaces
- all remaining blocked claims

**I disagree with, or qualify, these outcomes:**
- **fig2b-ephys-umap-subclasses, partially_reproduced.** The separability miss (VIP 0.195) comes from the 19 features that cannot be computed. With the paper's 19 features added, all four subclasses pass in both spaces (cell 68: smallest excess 0.222 in feature space, 0.224 in UMAP). This is the figs2b situation, which is blocked. Separability is undecided on the dataset, not failed. The outcome should be blocked, or the notes should say plainly that the failing part is not established.
- **fig5d-dbc-morph-umap, partially_reproduced.** The criterion requires "both spaces" and has no partial case. The UMAP, the space the statement names, fails under all five seeds under the revised label (cell 121, ratios 1.62 to 1.85). fig1i, where the opposite space fails, is not_reproduced, so the two are treated differently. My round-1 point 1 also overreached: the header's `Revised_subclass_label` default is listed under "Method choices common to the electrophysiology claims". The default does not fix the subclass for this morphology claim. Under `subclass_label` the claim passes at the claim's seed (cell 121: features 3.48, UMAP 2.27). The outcome therefore depends on a choice the claims file leaves open. It should be blocked as methods_underspecified, or not_reproduced under the revised label, but not partially_reproduced.
- **figs8b-firing-differs-pvalb2-only, partially_reproduced.** The two rate readings disagree (cell 16). The convention recorded in the claims file's check is that a claim "names the readings and blocks when they disagree". By that convention the claim is blocked as methods_underspecified.

**Assumptions (`assumed: true`):**
- **fig1c.** The Patch-seq gene ranking stands in for the snRNA-seq ranking. This is stated and reasonable, since every reading gives r ≥ 0.75 with p ≤ 1.4e-5.
- **fig4c.** The isi_adapt_ratio definition agrees with the paper's table for only 27% of cells. This is stated and reasonable, because the paper's own values give the same ordering (cell 89).

No other outcome rests on an unflagged assumption.

**Places where the claims file may misread the paper (reported, not corrected):**
- figs9: the criterion reads "driven mainly by the culture condition" as "differs for culture but not for acute". "Mainly" also allows a weaker acute difference, which is what cell 19 shows: acute FDR 0.011 against culture 1.2e-10.
- figs8b: the second reading (rate at rheobase) is close to 1 spike/s by construction, with median 1 against 1 (cell 16), so it hardly reads "average firing rate".
- figs2d: the criterion has the code adjust "p-values of the condition term". The printed code (cell 33) adjusts each gene's three term p-values.

### 2. Sentences the outputs do not support

- **Cell 84 and fig3e notes:** "Dunn's p 2e-12 to 7.2e-09 for width" and "differs from PVALB in width (p 7.8e-05 to 0.0011)". The printed values are 7.4e-12 to 7.2e-09, and 7.8e-05 to 0.0006 (cell 83).
- **Cell 119 and fig1h notes:** "cross-group fractions 0.30 to 0.72" and "at least 88% of these cells have a PVALB majority". Cell 118 prints 0.33 to 0.74, and one fraction of 0.81 (all PVALB WFDC2, seed+1000, UMAP, acute). The conclusion is unaffected, since the criterion asks for most cells.
- **Cell 110 and fig2c notes:** "0.150 to 0.209 over the five seeds". The five seeds give 0.148 to 0.209 (cell 109).
- **cell-metadata-link notes, and fig1i notes ("seven of them"):** "Seven features agree for less than 80% of cells". Cell 10 lists nine; upstroke_ramp and threshold_i_ramp are also below 0.8.
- **Attempt record findings with no printed output in either notebook:**
  - condition2 calls 181 culture cells microglial where metaPatch calls 180;
  - "no threshold on the stored log2(CPM + 1) reproduces" Genes_Detected;
  - "public IPFX 2.1.2".
- **Cell 50, fig4d:** says the variant cannot reach a decision while the main reading gives 2 genes. The main reading's 2 genes against the paper's 253 suggests it is not the procedure the paper ran. The notes should say so.

Every other "**Result:**" sentence, both Summary sections, the README and the other notes match the printed outputs. That includes:
- the 4 values set missing and the 79 files at 200 kHz;
- the bounds 39 to 61;
- the 84-feature variants for fig1i and fig2b;
- every number in the species notebook.

The attempt record states my round-1 reasons faithfully and in my own words. The `agrees` flags match my round-1 table: false for fig2b, fig2c and fig5d-dbc-morph-umap.

### 3. Round-1 points

**Resolved:**
- **1 (ephys):** fig5d-dbc-ephys was rerun with the revised label and the outcome holds.
- **2:** figs1a was run on Genes_Detected, and it is now partially reproduced.
- **3:** the 84-feature variants are shown. This settles fig1i and fig3c but not fig2b; see below.
- **4:** figs1 was run, both readings disagree, and the claim is blocked.
- **5:** fig5b layers, the fig4a traits and the mouse claims are now run.
- **6:** fig4d now has a RESULT line and states that the variant count is an upper bound.
- **7:** chance level and z-scoring for fig3c.
- **8:** the orientation of `lm_pval` is printed and correct.
- **9, 10, 11, 13, 14:** reported in the notes.
- **Section C:** the sampling-rate crosstab and the 50 kHz-only test, the Virus values and MFEATS are all printed.

**Remaining that bears on a conclusion:**
- **fig2b:** separability depends on the 19 uncomputable features, so the outcome should be blocked or explicitly undecided.
- **fig5d-dbc-morph-umap:** the subclass reading for morphology is not fixed by the claims file. My round-1 point 1 was wrong to apply the electrophysiology default here. The outcome flips between readings, and "partial" is not available under the criterion.
- **figs8b:** the readings disagree, so by the claims file's convention the claim is blocked.
- **mouse-label-link:** the four mouse outcomes (fig6c, fig6e, figs8b, figs9) depend on it, and no second reader has checked it.

**Remaining that does not change an outcome:**
- Point 12: cell-level QC is still not recomputed.
- fig3: the Patch-seq part and fig6b were not run, "for lack of time". Both are blocked, and the reason is stated honestly.
