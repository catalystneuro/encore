I wrote `claims/zandvakili-2015.yaml`. The quote checker passes it: 26 claims, 26 quotes, 20 statistical values, 0 problems. It contains no em dashes, no "rather", and no ": " inside plain scalars. Nothing was committed.

**Text read:** the version of record (PyMuPDF text of the journal PDF) with its full Supplemental Information appended: Figures S1 to S6 and the Supplemental Experimental Procedures. The full text, Methods and supplement were all there. The paper links no analysis code, so none was read. I could not render PDF pages here (`pdftoppm` and `fitz` are not installed), so every value comes from the text and no figure was read from its image.

**Claims:** 26, all with quotes and none `inferred`; all 26 have a criterion.
- 10 claims carry statistics: the narrow V1-V2 peak delay, the V1-V1 and V2-V2 zero offsets, the four Figure 6 and 7 divergence comparisons, and Figures S2A, S2B and S5.
- 8 claims carry expected values: the fraction of sites with a narrow peak, their depth, the RF-alignment probability, the fraction of pairs, delay and width, efficacy, the 3-fold ratio, and RF sizes.
- 4 claims are simulations (Figures 1, 3, 8 and S1). No code is published for them, so they would have to be re-simulated from the Methods; they are not tests on the recordings.

**Details the paper leaves open, with the readings named:**
- **CCG jitter window:** 10 ms, the only value given (for Fig. 4C), or another window.
- **Divergence epoch:** two 1-ms bins between 1.5 and 3.5 ms before the spike, or one bin centred 2.5 ms before it.
- **Jitter and control trials:** drawn from trials of the same orientation, or from all trials.
- **Jitter surrogate:** one jitter realization, or the mean of several.
- **Bootstrap p-value:** paired resampling, or two independent bootstrap distributions.
- **Shuffle for Fig. 7A:** within orientation, or across all trials.
- **Test of peak offset against zero (Fig. 5B, both claims):** Wilcoxon signed-rank or sign test.
- **Peak width:** full width at half height on the smoothed or the raw CCG.
- **Efficacy integral (Fig. S3):** on the jitter-corrected or the raw CCG.
- **Summary of the "roughly 3-fold" ratio:** geometric mean, median, or each window separately. Its tolerance is widened to ±1, with the reason given.
- **Time-course offset steps (Fig. 7D):** 2-ms epochs stepped by 1 ms, or 1-ms bins.
- **Broad-peak test (Fig. 4C):** none is given; one is fixed in the criterion, with two readings named.
- **Fig. S5 epoch:** printed "0.5±1 ms"; read as 0.5 to 1 ms before, a 2-ms epoch around the spike, or 1.5 to 3.5 ms before.
- **RF diameter of an elliptical fit:** two readings.
- **Printed 0.3% against counts of 296/83,441 (0.355%):** the claim holds if the result is within tolerance of either.

**Missing from the paper that some claims need:**
- **Pixels per degree:** the paper gives 1024 × 768 at 110 cm but no screen size. This affects the RF-offset bins, the 3° offset group and the RF sizes.
- **Depth and laminar order:** the depth claim, the non-middle-layer claims and the offset-RF claims need site depth relative to the layer 6/white matter border and the order of sites within a penetration.
- **Unit SNR:** the Fig. S2 single-unit claims need it.

The paper does not report any of these. Whether the dataset holds the depth and SNR data is for the author to find.

The paper's counts (896 V2 cells, 223 sites, 83,441 pairs, the epoch totals) come from 7 monkeys. The dataset holds 5 sessions in 3 animals, so the criteria compare proportions and medians and report the counts beside them.
