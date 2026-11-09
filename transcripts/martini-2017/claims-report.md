I wrote `claims/martini-2017.yaml`. The quote checker reports 18 claims, 18 quotes, 15 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (open access), extracted from the PDF, with the main text, Methods and figure legends. The supplement (`text_suppmat.docx`) only holds the legends of Supplementary Figs 1 to 3, which repeat Figs 2C, 2F and 4B split by colour channel. I did not need to open the PDF. The paper links no analysis code. It only names the tools it used: StackReg, Caltracer 2.5 and Groppe's `fdr_bh`.

**Claims:** 18, all with quotes and none marked `inferred`.
- 8 claims carry statistics: six Wilcoxon signed-rank tests, one Fisher exact test and three Kolmogorov–Smirnov tests, plus the 5–95% confidence intervals for the example neuron.
- 15 claims have expected values and all 18 have a criterion.
- 4 claims say an effect is absent: the correlation slope beyond 200 µm (P = 0.106), the similarity-index slope (Fig 3G, P = 0.114), barrel against septum (Fig 4C, P = 0.58) and distance to the barrel border (Fig 4D).
- Where the paper gives a SEM, I used it as the tolerance. The exception is the median similarity-index slope: its SEM of 0.000675 is about 0.1% of the value, so I used 10% and said why in the file.

**Details the paper leaves open, and the readings named:**
1. **Segmentation and field exclusion:** the halo width, the blood-vessel background, and how one set of ROIs covers the 4 movies of a field are not given. I used one ROI set on the mean of the registered movies. The motion threshold for discarding fields is not given either.
2. **Response window:** the frame boundaries around stimulus onset are not given. I took the first frame at or after onset as the first frame "after", a standard choice.
3. **Amplitude units in the regression:** normalized 1, 3, 5 (the Fig 2B legend) or command voltage, and ΔF/F0 as a fraction or a percent. This changes coefficient sizes but not significance.
4. **Slope test sign:** a significant slope of either sign counts as tuned, or positive only.
5. **False discovery rate:** `fdr_bh` with 'pdep' (Benjamini–Hochberg) or 'dep' (Benjamini–Yekutieli). The family is either all 3×N p-values of a field or N per feature.
6. **"Responded" (50.2%):** never defined. Readings: (a) a test over all presentations; (b) any one of the nine stimuli significant, with FDR correction.
7. **Correlations:**
   - Signal: neuropil-corrected fluorescence, or ΔF/F0.
   - Shuffle segments: permuted across the whole concatenated series, or within each recording.
   - Shuffle count: not given, so I used 100, with a single shuffle as a variant.
8. **Distance:** between ROI centroids, using all pairs or only pairs up to 300 µm.
9. **Similarity index:**
   - The paper does not say which 26 of the 49 fields entered. The main reading is fields with at least two tuned neurons.
   - Scale: the raw dot product the Methods give, or unit-length vectors.
10. **Fig 4D:** a neuron tuned to several features is counted in every group it is tuned to, or only single-feature neurons are used. The distance is either unsigned or signed.
11. **Beyond 200 µm:** the slope is fitted to pairs over 200 µm apart (main reading) or to all pairs of those 30 fields.
12. **Tuning consistency (95% and 81%):** the denominator is all neurons, tuned neurons, or neurons tuned in either half.
13. **Tuning by shuffle:** whether the FDR correction is applied after the 1000-repeat shuffle is not stated, so both are run.

**Missing from the paper:**
- **Unidentified examples:** the paper does not say which mouse, field or ROI the example neuron (Fig 2A–C) and the example field (Fig 3A/B/D/F) come from. The author has to match them from the figures, or those claims cannot be tested.
- **Inconsistent example size:** the example field has two sizes in the paper: 31 neurons (Fig 3B), and 29 neurons with 465 pairs (Fig 3F). 465 is the number of pairs among 31 neurons.
- **Raw data only:** the dataset description says it holds raw movies, stimulus signals and histology PDFs, but no ROIs or tuning labels. Neurons must be segmented again, so the counts carry a 10% tolerance.
