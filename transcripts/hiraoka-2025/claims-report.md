I wrote `claims/hiraoka-2025.yaml` and did not commit it. The quote checker reports 14 claims, 14 quotes, 2 statistical values and 0 problems.

**Text read.** The file's header says "version of record", but only the abstract and the 54-item reference list at the top are from that version. The body is the arXiv preprint (arXiv:2508.18281v1, dated September 22, 2025, 50 references, with a different abstract), so every claim comes from the preprint. The paper has no supplement. There was no PDF, so I read the figures only from the labels the text keeps (the δ values, n, τmin, τmax). The paper links no code. It cites Clauset et al. and the Python `powerlaw` package for the fits, without giving a version.

**Claims.** There are 14 claims, all with quotes and none marked `inferred`.
- **Statistics:** 2 entries. Both are the Figure 2 likelihood ratio test of power law against exponential (p < 0.05), for burst sizes and for merging numbers.
- **Expected values:** 7 claims carry them.
  - Unit 9 of session Achilles-10252013: n = 228 356 spikes, τmin = 1.05 ms, τmax = 1.82×10⁴ ms.
  - Neuron burst-size exponent β ≃ 2.35.
  - Wikipedia β ≃ 2.50; earthquake β ≃ 2.60 with 330 215 events.
  - The model's maximum IETs from Figure 4.
- **Criteria:** all 14 have one.
- **Testable on the dandiset:** 9 claims. These are the representative neuron (IET range, heavy tails, β stable, β falling above 3000 ms with γ, merging tails, collapse, exponents above 2 and Eq. 8) and "other sequences show similar patterns".
- **`data: elsewhere`:** 5 claims. These are Wikipedia and earthquakes (catalogs named) and three on the model, whose simulations were not deposited.

**Details the paper leaves open, and the readings named:**
- **O1, which unit is "unit 9":** the units table id 9, row 9 counted from 0, the ninth unit counted from 1, or a cluster number 9 in the metadata. The one whose spike count and IET range match Figure 2 is used.
- **O2, which part of the recording:** the whole session (both rest periods and the maze). Each epoch taken separately is a variant.
- **O3, the fit:** a lower cutoff (xmin) chosen by the KS-distance default, or xmin = 1, each fitted as discrete and as continuous. The test is `powerlaw`'s `distribution_compare`, with R > 0 and p < 0.05 counting as support.
- **O4, the grid of δ:** the paper does not give it. I used a geometric grid with a ratio of 1.8, which matches the figure legends and cannot change an outcome. The pair ratios 3.3, 5.9 and 11 come from the Figure 2 legend.
- **Vague words:** "stable", "relatively constant", "most", "agrees well", "collapse", "similar patterns" and "statistically equivalent" have no test in the paper. Each criterion names the reading it uses and says it is the registry's: "most" is more than half, interquartile range under 0.5, within 10%, CCDFs within a factor of 2, KS with Bonferroni.
- **Which neurons count as "other sequences":** the pyramidal units of Achilles-10252013, or those of every session.

**Missing from the paper.** It names no analysis code and no fit settings (xmin, discrete or continuous). It gives no thresholds for its statements of stability or collapse. It does not say which neurons "show similar patterns", and the Wikipedia data were never deposited.
