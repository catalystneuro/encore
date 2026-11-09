I wrote `claims/002035/10.3233-jad-220538.yaml`, and the quote checker passes it with no problems: all 33 quotes are word for word, and all 33 recorded statistical values were found in the text.

**Text read:** the PubMed Central author manuscript (NIHMS1886685, PMC10097438), from `paper/10.3233-jad-220538.txt`. That covers the main text, Methods, figure legends and Tables 1 to 6. I opened the PDF only to read the axis labels of Figs. 1 to 7. The paper has no supplement and links no code or data, so there was no code to read. I did not read the version of record. Nothing a claim needed was missing.

**Claims:** 33, all with quotes and none marked `inferred`.
- **Statistics:** 18 claims carry 33 entries in total, mostly Kruskal-Wallis across ages, layers or subregions and Mann-Whitney for pairs and sex, with the χ² and η² from the tables.
- **Expected values:** 12 claims have them. The tolerance is the paper's S.E. where it gives one, otherwise 10%. One claim departs from both, and its reason is given: the "roughly 2 months" lag from first cells to first plaques is judged as 45 to 70 days, the span of the paper's own lags.
- **Criteria:** all 33 claims have one. The opening comment sets out the shared method, all from the Methods: counting by eye, the eight 12.5% depth bins in A1, alignment to the Allen atlas (CCFv3), one value per mouse, and the PRNc circle 800 µm across.
- **Data:** one claim (`l5-pyramidal-fraction`) is `with_inputs`. It needs the share of layer 5 cells that are pyramidal neurons, from the paper's reference [30] (Erö et al. 2018, a mouse brain cell atlas). The paper does not state that number.

**Details the paper leaves open, with the readings named:**
- **DAPI counting in ImageJ:** (a) automatic threshold and particle count; (b) counting by hand.
- **One value per mouse from several images or hemispheres:** (a) counts and areas summed, then the ratio; (b) the mean of per-image values. Which hemisphere is not said.
- **What was imaged at 200X:** (a) the whole region; (b) sampled fields.
- **Which layers L5A and L5B are lower than, in DAPI density:** the Results say L2, L3, L4, L6A and L6B; the Fig. 1G legend omits L6A.
- **Which mice enter the DAPI-by-layer test:** the reported η² implies about 340 mouse-by-layer values, fewer than all 61 mice would give. Both all mice and only the mice counted in every layer are run.
- **Ages for the IC plaque-by-subregion test:** p90 to p150 (text) or all ages (Fig. 5C label).
- **Sample for the sex tests:** one value per mouse or per mouse and layer, and all ages or p90 to p150.
- **Thresholds that are words only:** "consistently" (every mouse, or more than half); "did not exceed 0.5%" (age means, or every mouse); "appeared first" (any mouse, or most mice).
- **Pyramidal fraction from reference [30]:** taken of all cells, or of neurons.
- **Effect sizes:** the paper cites a reference for η² but gives no formula. The reported values fit η² = (H − k + 1)/(n − k) for Kruskal-Wallis and z²/N for Mann-Whitney (n is the sample size, k the number of groups). That fit implies about 61 mice for most age tests, about 38 for PRNc and 24 for the p90 to p150 tests. This is my reading of the numbers, labelled as such in the file.

**Inconsistencies in the paper, noted in the file:**
- The Methods give 31 female and 30 male 5XFAD mice, but the per-age numbers add up to 30 and 31.
- The figure references in Tables 1 and 2 are off by one panel or one figure.
- The IC subregion test in Table 4 has the same χ² and η² as the MGB subregion test in Table 3.

**Other:** to read the figures I installed PyMuPDF into the temp directory. New untracked files appeared at the repository root during the run (`.bashrc`, `.vscode`, `scripts` and others). I did not create them on purpose. They fall outside `claims/002035/`, so the workflow will not keep them.
