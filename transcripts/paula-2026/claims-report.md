I've written `claims/paula-2026.yaml`. The quote checker reports no problems (38 claims, 37 quotes, 7 statistical values), and the file follows the style rules. Nothing is committed.

**Text read:** the version of record (PRX Life 4, 023018; published 22 May 2026, corrected 22 July 2026, the correction being to Eq. 9). It includes the full Methods, Table I, the figure legends and the Supplemental Material (Secs. I to III, supplementary Figs. 1 to 6). The PDF pages could not be opened as images (no renderer here), so every value comes from the text and legends. The paper links no analysis code, so none was read; its only URL is a link to the parameter-sweep figures.

**Counts:**
- **Claims:** 38. All have a criterion and 22 have expected values.
- **Quotes:** 37. The one without, `table1-sample`, is a count check marked `inferred` and built from Table I and the legend numbers.
- **Statistics:** 7 claims carry them. These are the Mann-Whitney tests against surrogates (p < 0.001) for CV and for each area's complexity, plus two tests the paper does not name (Fig. 4a pairwise comparisons, Fig. 4b LGd/LP modulation).
- **Data:** one claim, `fig3a-reference-systems`, uses no recordings and is marked `data: elsewhere` (synthetic series from the supplement's definitions). Every other claim uses the dataset.

**Details the paper leaves open, with the readings named:**
- **Session selection** (102 sessions, no rule given): (a) every session with a qualifying population, or (b) only sessions that also have the spontaneous epoch. The paper's own counts (sessions, 1437 populations, Table I neurons) pick between them.
- **Unit quality filter:** (a) all units, or (b) the Allen default filters. Table I counts decide.
- **Which flashes count:** whether change and omitted flashes are included, and which gray screens count as blanks; two readings.
- **Spontaneous windows:** the first two consecutive 100-s windows, or two centred in the gray-screen interval.
- **JS divergence histograms:** 50 or 100 bins. Log base 2 is used because the Fig. 4 colour scale tops out at 1.0; natural log is a variant.
- **"Summed along the main diagonal of each submatrix":** the diagonal of a region-by-region matrix is zero, so I named two readings of the sum (all within-area pairs, or the first off-diagonal). I also named two readings of the percentage difference.
- **Fig. 1d correlations across sessions:** one correlation over concatenated sessions, or one per session averaged.
- **Fig. 3 windows:** the section is about natural images, but the point counts sum to 51 704, the active-behaviour total. The readings are active-behaviour windows (favoured) or natural-image windows. Spans are read as 2.5–97.5 percentiles, with full range as a variant.
- **Unnamed tests:** for Fig. 4a, Mann-Whitney uncorrected or Bonferroni-corrected. For Fig. 4b modulation (and the absence claim for the other seven thalamic nuclei), Kruskal-Wallis or pairwise Mann-Whitney.
- **Fig. 5 trajectories:** CV bin width (0.1 or 0.05), minimum count per bin, and what "monotonic" means.
- **Supplementary Fig. 6 mean correlation:** count bin of 50 ms or 20 ms.
- **What "distinguishes" means** (CV and correlation fail to separate images from spontaneous activity in visual cortex, complexity does): JS divergence between the two conditions, or overlap of their interquartile ranges.
- **Fig. 3a synthetic systems:** parameter values and series lengths are only in the figure; standard choices are stated.

**Places where the paper disagrees with itself (both versions recorded, so a claim matches under either):**
- Fig. 4 text against legends: the thalamic LGd/LP values, the DG/CA3 ranges (the legend has natural images lowest), the NOT range, and APN printed as "0.9", read as 0.09.
- Fig. 2b: the legend says DG/CA3 JS divergences are 0.15–0.35, while the text gives medians of 0.84 and 0.63.
- Section III.B: "typically <4%" among visually driven conditions sits beside the ~30% separation of images from active behaviour and blanks.

**Missing:** nothing that stops the claims being written. Two things are absent: analysis code, and figure-only details such as the Fig. 3a parameters. Several thresholds in the criteria (the 0.2 surrogate-correlation bound, the 0.02 midbrain invariance bound, the "most" and "more than half" counts) are not from the paper; each is flagged where it is used.
