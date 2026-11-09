I've written `claims/000023/10.1101-2020.03.31.018820.yaml`. The quote checker passes except for two values it can't parse: the GO p-values printed as "p=3.5 10 −6" and "p=5.3 10 −5". I read them in the text and they are correct. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1 (the version the dandiset names), from the JATS XML: main text, Methods, figure legends, and the legends of the Extended Data figures and tables. There is no PDF, so none of the figures could be read.

**Code read:** `AllenInstitute/patchseq_human_L23` at commit `3daf9f0803ea0c220a040ea523f23af5f93c56ac`. That commit was updated for the later Nature version, so some of its outputs differ from the preprint. In those places the criteria follow the preprint's Methods and run the code's choice as a variant:
- its feature table has 316 human cells, against the preprint's 283;
- its comparison of the three homologous types uses only the superficial FREM3 cells;
- the updated pathology notebook finds 2 significant comparisons out of 18, against 1 in the original.

**Counts:** 33 claims (1 link check, 32 findings). 32 have quotes; the link has none and needs none. 17 statistical values, and every claim has a criterion or expected values.
- 13 can be tested on the dandiset once each cell's t-type and depth are attached: 12 `with_labels` (cell counts, depth by type, the type ANOVAs, FREM3 depth correlations, the human classifier, pairwise deep-type tests) plus the link.
- 4 are `with_inputs`: pathology against electrophysiology, the mouse ANOVA, the mouse classifier, and the human against mouse comparison.
- 16 are `elsewhere`: histology, transcriptomics, morphology and SMI-32.

**Details the paper leaves open, and the readings named:**
- **Which cells have features:** at least one feature, all 18, or no more than 3 of 18 missing.
- **Donor count of 90:** all subjects in the dandiset, or the donors of the paper's 385 cells.
- **Cells in the pathology comparison:** temporal cortex only, as the code does, or all regions, as the text says. The paper doesn't name the test; the code settles it as a Mann-Whitney test whose p is half the two-sided value (the scipy 1.4 default), at Bonferroni 0.05/18. The two-sided test is run as a variant.
- **"About 5 mV more hyperpolarized":** difference of medians or of means.
- **"Almost entirely in deep L3":** at least 90% or at least 80% of cells deeper than 0.575.
- **The cross-species t-test:** Student's or Welch's. The code's Mann-Whitney test is a variant.
- **"Faster AP upstroke" in CARM1P1:** the upstroke rate or the upstroke/downstroke ratio.
- **Version of the feature software (IPFX):** not given. A current release is used as a standard choice, checked against the code's feature table by the link claim.
- **"Most cases below 1.0":** read as more than half of donors.
- **"Strongest" depth correlations:** read as the largest explained variance.

**Missing from the text:**
- The contents of Extended Data Table 1 (cross-species values per feature) and Table 2 (donors).
- Supplementary Data 1 (results per feature).
- The figure images.

No claim depends on numbers that appear only in those. Two gaps did leave parts untested:
- **Deep-type ANOVA:** the text doesn't say whether its "maximum R² = 0.26" for the homologous types is electrophysiology or morphology, so that number isn't tested.
- **Mouse recordings:** the paper doesn't say where they are deposited. The mouse claims rely on the code's tables.
