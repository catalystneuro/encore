I wrote `claims/001065/10.1016-j.celrep.2024.114718.yaml`. The quote checker passes it: 40 claims, 40 quotes, 25 statistical values, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript (PMC11488157, from Europe PMC): main text, STAR Methods, figure legends, key resources table, and the supplemental PDF with the legends of Figures S1 to S7.

**Missing from the paper.** Tables S1 to S5 are not in `paper/`. They hold the gene lists and statistics, the means and SE of the 40 physiology features, and the two physiology ANOVAs (Figure 4A and Figure 6A). The results are stated in the text and legends, so I went ahead. Where a claim needed a number only those tables hold, I took it from the paper's code output and marked it as reference, not target. The projection-type ANOVA of Figure 4A (Table S4) has no deposited output, so those claims have no reported numbers.

**Code read.** Zenodo doi:10.5281/zenodo.13749343 (record 13749343, one version, 2024-09-11): notebooks for Figures 1 to 6 and S1 to S6, plus per-cell tables. It does not include the helper modules (the classifier, imputation and gain functions), the extraction of features from raw traces, or the R code for Figure 7. The code settles:
- the MCx brain regions and how a cell gets its L5 ET label;
- type II ANOVAs with all interactions, Benjamini-Hochberg correction across features;
- Welch t-tests and pooled-SD Cohen's d;
- the UMAP and sparse-PCA parameters.

The code's "partial eta" formula is not the standard partial eta squared the Methods name. The Methods version is the main reading; the code's is a variant.

**Claims.**
- 40 claims, all with quotes; 17 carry statistics and all 40 have criteria.
- `data` field: 29 claims need per-cell area, preparation and subclass labels from the Zenodo tables (`with_labels`); 9 use data held elsewhere (SRA PRJNA1088539, NeMO, Brain Image Library doi:10.35077/g.1160); 2 use the dataset alone (cohort counts).

**Details left open, with the readings named:**
- **Classifier (Figs 3E to 3G, 5E):** regularization and solver (standard choice: scikit-learn defaults), stratified or not (both run), and the score (weighted f1 or class-weighted recall).
- **Feature extraction:** windows for peak and steady-state input resistance, which steps form the "linear portion", chirp averaging, and the fAHP window. Standard choices are named.
- **Fig 3A, "exclusively distributed with":** two neighbour-based readings, both mine.
- **Fig 4A, "input resistance":** maximum or steady-state.
- **Fig S3D, "small" interactions:** two readings, both mine.
- **Species 4-way ANOVA:** "subclass" read as projection class or predicted subclass.
- **TCx L5 ET types:** test unnamed; Welch t-test or two-way ANOVA.
- **Fig S6B input resistance:** steady-state matches the printed p of 0.003; maximum is run as a variant.
- **Fig 6 "faster" spikes:** half-width or min dV/dt.
- **Depolarization block:** any step-to-step decrease, or the last step below the peak.
- **Figs 6J and 6K step choice:** the step with most spikes, or the code's indexing, which can pick a later step.
- **Figure 7 (no code):** the second ANOVA factor and its bin edges (10 or 25 spikes), the curve fitted to the AHP, the band-pass filter, the spline, the autocorrelogram frequency, and the mode bin width (1 or 2 Hz).
- **Morphology (Fig 5C):** "longer basal dendrites" read as max path distance or total length.
- **Thresholds that are mine:** where the paper uses words like "similar", "substantial" or "exclusively", the criterion's threshold is my reading and is labelled as such.

**Paper inconsistencies recorded:**
- The Figure 6D/E legend contradicts the Results on which area has the deeper fAHP and more symmetrical spikes. The code's means agree with the Results, so the Results are tested.
- The Fig S6B gain p is printed as 0.869; the code gives 0.850.
- The TCx Fig 7J pair (r² < 0.001 with p = 0.146 on 82 observations) is not self-consistent, so only p is used for TCx.
- The deposited morphology and classifier notebooks printed values that differ from the paper's (e.g. d 2.79 against 2.65, f1 0.900 and 0.741 against 91.9% and 76.1%), so the paper's numbers come from another run.
