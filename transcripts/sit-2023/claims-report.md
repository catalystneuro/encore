I wrote `claims/000483/10.1038-s41467-023-37704-5.yaml` with 24 claims. The quote checker passes every quote. It flags one value it couldn't match: p = 8.0 × 10⁻⁴ in `fig6b-landmark-cells`. I read the text and the value is correct; the paper prints "8.0 × 10−4", a form the checker doesn't recognise.

**Text read:** the version of record (a PDF supplied by a person, extracted to text): main text, figure legends, Methods and statistics. The Supplementary Information (Figures S1–S7, Table S1) is not in the paper store. All the main findings and their statistics are stated in the main text, so I went ahead and wrote the claims. I could not open the figures because there is no PDF renderer, so no number was read from a figure.

**Code read:**
- **The paper's code** (`ucsb-goard-lab/Neurotar-HD-Experiments`, commit c6344f5): the paper's URL is missing a hyphen. The repo holds MATLAB classes for tuning curves, heading selection, light/dark segmentation, flip score, Gaussian fits and one reviewer-response clustering script. It has no code for the V-tests, the remapping offsets, the F-tests, the LDA, the decoding or the statistics.
- **The lab's `HeadingDecoder`** (commit ca9842e): the paper doesn't link it, but its README says it belongs to this paper. I used it only as a named variant.
- **`leaveOneOutAligner`:** the alignment helper the code calls was not found.

**Counts:** 24 claims, all 24 with quotes and criteria, 11 with statistics, 10 with expected values. No claim needs outside data; I named the Dryad deposit (doi:10.25349/D91G8Q) for the author.

**Details left open, with the readings named:**
- **Free-chamber selection (Fig. 1):** all frames or only frames with speed above 2 (the code); 99th percentile (Methods) or 95th (code's default, as a variant).
- **Fig. 1H tiling and the excess near 0°:** the paper gives no measure. Readings: every 6° bin has a cell, or every 90° quadrant holds at least 10% of cells; the excess is more than 25% of cells within ±45° of 0°.
- **Fig. 2F and 3C:** which cells count (selective in both conditions, in either, or in the chamber-rotation condition); preferred heading as the tuning-curve peak or the code's Gaussian-fit method. For 3C, the expected offset is either the median of differences (Methods text) or the difference of medians (Methods equation). I read the subscripts in V32 and V66 as n, which matches the printed p-values closely.
- **Fig. 4 axons:** selected axons or all axons. Bimodality is judged by the sign of the flip score; light-off tuning by the selection test run on dark trials.
- **Fig. 5 clustering:** the Mahalanobis outlier rule (chi-square, 8 degrees of freedom, 95th percentile, or no outlier step as in the reviewer code); class shares averaged over recordings, over mice, or pooled. The cluster sizes 332/522/409 come from the F-test degrees of freedom.
- **Flip-score F-tests:** a mixed model with mouse as a random intercept; per-cell random effects as a variant.
- **Fig. 5K visual-cue-only rotation:** no number of recordings, measure or test is given. Readings: fraction of cells still selective, or tuning-curve range.
- **Decoding:**
  - Input: ΔF/F (Methods, "raw calcium data") or inferred spikes (`HeadingDecoder`).
  - Decoder: the naive Bayes decoder of Etter et al. or `HeadingDecoder`'s.
  - t-test: paired or unpaired.
  - Chance level: 0.18 (Methods) or 0.10 (Figure 6 legend). Under 0.10, the paper's own light-off interval for landmark cells (0.14 to 0.27) excludes chance, which contradicts "plummets to chance levels".
- **Fig. 5E coregistration, the 180° errors and the "tiling":** the paper gives no test. I used its own tools (the V-test; the 18° accuracy window moved to 180°).

**Missing from the paper that claims needed:**
- **Figures S5 and S6:** the text gives the bootstrapped KS p-values (0.0094 and 0.031) but not what is compared, so two readings are named for each.
- **Table S1:** it holds the mixed-model comparisons between decoding classes, so the model for `fig6-heading-below-population` is open.
- **Fig. 5K:** the number of visual-cue-only recordings is not given.
