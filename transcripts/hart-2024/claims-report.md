I wrote `claims/000773/10.1016-j.cub.2024.05.031.yaml`. It passes the schema and every quote is found word for word. The checker still reports 28 problems, all of them p-values it could not find in the text: they are printed only inside the panels of supplement Figures S2B, S3B, S4A, S4B and S4D, and I confirmed each one by reading the supplement PDF. Nothing is committed.

**Text read:** the accepted author manuscript (NIHMS1997610, PMC11265976, from Europe PMC), with its main text, figure legends and STAR Methods, plus supplement MMC1 (Figures S1–S4 and Table S1). I opened supplement PDF pages 2–7 only to read the p-values and sample sizes inside the figures and to check Table S1. Data S1 and S2 are spreadsheets and I did not read them.

**Code read:** two Zenodo records.
- doi:10.5281/zenodo.11151724 (Hart_Kronauer2023 v1.0.0, commit 72d041a): converts the NWB files to TIFF, and an ImageJ macro makes the fold-change maps and Z-projections.
- doi:10.5281/zenodo.11151756 (Hart_Kronauer2024 v1.0.0, commit 1aef6bc): computes the behavior proportions and plots the curves.
- No code is published for the glomerulus ROIs, the area under the curve, the counts of responding ROIs, or the statistics (run in R and Prism).

**Claims:** 21, all with quotes; 20 record statistics (50 values) and 20 have criteria.
- **Data:** 5 behavior claims and 1 confocal claim are `elsewhere` (Data S1; Brain Image Library doi:10.35077/g.1153). The 60- versus 90-day comparison is `with_inputs` (DANDI 000467). The other 14 use this dataset.
- **Expected values:** two claims have them, given with tolerances: the six Table S1 curve parameters (tolerance from their 95% CIs), the medians of 4 and 2 responding ROIs, and the >9-fold and >57-fold declines.

**Details the paper leaves open, with the readings named:**
- **How an ant's three trials are combined:** the mean, taken from the Figure S4C legend.
- **Glomerulus fold change:** (a) the ROI mean of the projected signal, then fold change; (b) fold change per pixel, then the ROI mean.
- **Trials with motion artifacts:** (a) all trials kept; (b) the trials Data S2 leaves out, if it marks them.
- **Hand-drawn ROIs** (whole-AL outline, responding-ROI sets, the six focal glomeruli): no coordinates are given. The criteria use a standard, sensitivity-bracketed choice and check the counts against Data S2.
- **Confocal sample unit:** (a) each AL; (b) the mean of a brain's two ALs.
- **"Faster" behavior:** (a) the old ants' rate K is higher; (b) the old ants' curve is above the young ants' from 0 to 60 s.
- **"Sparse":** (a) at most 5% of about 500 glomeruli; (b) at most 10%.
- **Which pairs in Figure 3D are significant:** (a) PGb for both pheromones and PGa for 4-methyl-3-heptanol; (b) PGb for at least one pheromone and PGa for 4-methyl-3-heptanol.
- **The 90-day data:** (a) the 000467 ants given 48% pheromone, with the area under the curve recomputed here; (b) the published per-ant values.
- **The Methods and code disagree in two places:**
  - Proportion of ants outside the nest: the code settles it as divided by the number of ants of that age.
  - Z-projection: the macro skips the 0 µm plane; the Methods are followed and the macro's version is a variant.
- **Volume period:** the Methods say 0.83 s and the code says 1.2 s. All windows are in frames, so this changes nothing.

**Missing from the paper:**
- **p-values in the main figures:** the images of Figures 1–4 are not in the text, so p-values printed only in Figures 2D, 2E, 3B, 3D and 4 are recorded as bounds (p < 0.05 or > 0.05). The confocal n (Figure 2B) and the 90-day n are also unknown.
- **Inconsistencies:**
  - G3's young/old n is 7/6 in Figure S2 but 7/5 in Figure S4.
  - Two Table S1 entries are inconsistent: the blend's young Y0 confidence interval, and one K value for the stimulus comparison that falls outside its own interval.
