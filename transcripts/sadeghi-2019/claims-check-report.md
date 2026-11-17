I checked the claims file against the paper. It is ready for an attempt, though some method details remain open (listed below). Nothing is committed or pushed.

**Checker result (after my changes):** `claims/sadeghi-2019.yaml: 28 claims, 28 quotes, 14 statistical values, 0 problems`. It gave the same result before the changes.

**Changes, by claim**
- **Source paragraph numbers, first Results section** (fig1k-example-temporal-widths, fig1-snr-noise-stronger, fig1-s5-model-predicts-neural, fig2-noise-restricted, fig3a-example-tonotopy-removal, fig3a-example-classifier-order, fig3b-population-above-chance): each was one too high. They are corrected to paragraphs 4 to 9.
- **fig1k-example-temporal-widths:**
  - Removed a 300 ms lag range the paper never gives. The 161.2 ms full width only needs lags of ±81 ms.
  - The "upper eight channels" for the snake's period was the writer's own choice. The paper says only "high-frequency sites", so the criterion now names two readings.
  - Said that the pass counts are the reader's.
- **fig1-snr-noise-stronger:** the quote stopped before the numbers; it now includes the ranges, means and SDs. I added a reading where the SNR comes from the example site alone, because that paragraph is about that site.
- **fig1-s5-model-predicts-neural:** "well above" the control is not the paper's wording. It now says "significantly above" by the one-tailed t test in the S5 Fig legend.
- **fig3b-population-above-chance:** the paired t test for the drop when tonotopy is removed is now marked as the reader's choice; the paper reports no test for it.
- **figs9-mixing-coefficient:** added readings for the median, pooled over sites or taken per paradigm.
- **figs10-amua-tmua:** the legend says the tMUA against aMUA r is measured between halves of the data. The criterion left this out; it now names two readings.
- **fig4f-example-equalized-classification:** added a second reading of the within-site t test.
- **fig4h-population-equalized-classification:** the statement now says "does not substantially improve" with duration, as the paper does. It also adds that the spectrum classifier beats all three correlation classifiers on the original sounds.
- **fig8b-example-pca-variance:** the PCA training set is either five exemplars per category (from the Results) or six (from the legend). Both are named.
- **fig8e-example-categorization:** the 90% threshold for "approached 100%" is now marked as the reader's.
- **fig9-spectrum-classifier-lower:** the reproduction rule was garbled (a 10 s accuracy compared "at every duration"). It now compares accuracy at each duration.
- **fig10-vocalization-background:** the paper does not say at which duration the temporal classifier is about 20% lower; two readings are named.
- **fig9c-time-averaged-worse:** `expected` was a mapping, not a list like every other claim; it is now a list.
- **Opening comment:** added the PC counts the paper reports (26, 8 and 87).

**Still open**
- **The paper's MATLAB code was not read**, by the writer or by me. It sits in the CRCNS deposit with the data. It may settle readings (1) to (7) and the formulas the extracted text lost (SNR, SI, CDI and the correlogram normalization). The author should read it, as protocol step 2 asks.
- **The Fig 9C time-averaged classifier** is not described in the paper. The SNR, SI and CDI formulas are missing from the extracted text. All of these rest on the readings named in the criteria until the code is read.
- **Qualitative words** such as "restricted", "substantially" and "does not depend" are judged by thresholds I or the writer chose. Each is labelled as the reader's.

All the paper's main findings have a claim, and none comes from outside the paper. The check entry is at the end of the file under `checks`, with `ready: true`.
