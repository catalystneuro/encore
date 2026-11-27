I wrote `claims/yang-2026-electrophysiological.yaml` with 21 claims, and all 21 quotes match the text. The quote checker still reports one problem: p = 0.002 for Figure 5A is not in the text because it is printed only inside the figure. I confirmed it by reading the figure in the PDF.

**Text read:** the bioRxiv preprint, version 2 (2026-08-20), with Results, Methods sections 1 to 7, the legends of Figures 1 to 5 and the Data and Code Availability statement. The supplement is only Supplementary Table 1, the list of derived features for each protocol. Its body and Table 1 are images, so I read them from the PDFs.

The text gives no numbers at all. Cell counts, variance explained, correlations and n all come from the figures. Figures 4E, 5A and 5B print their statistics inside the panel; everything else was read off bars or box plots, and the claims mark those values as approximate. The paper links no code: it says the code "will be made publicly available upon publication". So none of the open details below could be settled by code.

**Claims:**
- **Quotes:** 21 of 21.
- **Statistics:** 2 claims.
  - Fig 5A: Spearman r = 0.883, p = 0.002, n = 9 driver lines.
  - Fig 5B: Spearman r = 0.707, p < 0.001, 36 driver-line pairs.
- **Expected values:** 9 claims.
- **Criteria:** all 21. All claims use the dataset itself.

**Details the paper leaves open, with the readings named:**
- **Quality control thresholds:** none are given.
- **Which stimulus descriptions count as long pulse and ramp:** only the brief-pulse protocol, X5SP_Search_DA_0, is named. Readings: all long square steps, or only the suprathreshold family.
- **Spike detection,** which sets recruitment current and latency: a 0 mV crossing, or dV/dt of 20 V/s.
- **Response window for gain:** pulse plus 10 ms, or pulse plus 50 ms.
- **Imputation and missingness:** mean or median imputation. Dropping features over 50% missing is my assumption.
- **Feature-set membership:**
  - Ramp, recruitment-focused: the 8 features shown in Fig 3D, or all ramp features.
  - Brief response: two variants of the listed amplitude features.
  - Brief base set: all brief-pulse features.
  - Brief gain set: gain plus the command-slope features.
- **How many PCs form the space for centroids and distances:** all, the first five, or PC1 and PC2.
- **Per-group summary for orderings:** median or mean.
- **Balanced resampling:** cells per line per draw (the smallest line's count, or 20). The exclusion rule follows from that number. I used 1000 iterations and sampling without replacement as standard choices.
- **Empirical p-value:** a plain fraction, or a fraction with one added to each count. The shuffle can be applied in one geometry or both.
- **Stars in Fig 5C:** their meaning is not given.
- **Shared driver lines:** the paper is inconsistent. Fig 1D prints 7 lines shared by all three protocols, but the line names in Figs 2 to 4 give 8, so the claim accepts 7 or 8. The Fig 1D diagram also labels the ramp set "Short pulse".

**Missing that a claim needed:** no exact numbers in the text, no code, and no definitions of the feature sets or resampling parameters. Nothing missing stops a claim from being written, so I did not stop the run.
