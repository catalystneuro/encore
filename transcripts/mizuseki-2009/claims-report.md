I wrote `claims/mizuseki-2009.yaml` and did not commit it.

**Text read.** I read the version of record with its supplement: the Supplemental Experimental Procedures, Table S1 and the legends of Figures S1 to S19. The extracted text garbles degree and minus signs, so I read those values from the PDF. Table S1 is an image, so I read it from the rendered page, as I did the Fig. 3D/3H significance marks, the Fig. 4 arrows and the Fig. 7 percentages and n. Nothing the claims needed was missing. The paper links no code (its analysis used unpublished custom MATLAB), so every method comes from the paper and supplement.

**Counts.** There are 33 claims. 31 have quotes and 2 are `inferred`: the Table S1 cell counts, and the hippocampal comparisons in Fig. 3D, which only the figure shows. There are 14 recorded statistics: one-sided KS tests for bursting, Wilcoxon rank-sum and chi-square tests for Fig. 3D/H, and the jitter test for group cross-correlograms. Every claim has a criterion, and 13 have expected values. One claim, the Fig. 8 sink timing, is `with_inputs`, because its CSD sink phases come from Montgomery et al. 2009 and the paper names no archive for them.

**Quote check.** `tools/claims_check.py` reports 3 remaining problems. All are the p < 10⁻⁴ bound, which the text prints as "10�4". I confirmed it from the rendered Fig. 3 legend.

**Details the paper leaves open, with the readings named:**
- **Spatial coherence:** "neighbouring bins" means either the two adjacent bins, or each bin against the mean of its neighbours.
- **Counting units:** session by session, as the Table S1 legend says the paper did, with once per unit as a variant.
- **EC cell classification:** the visual pruning of spurious pairs can't be repeated, so the readings are all jitter-detected pairs, or different-shank pairs only. The "hyperplane" classifier is read as a linear discriminant.
- **EC3–CA1 coherence:** the estimator and band are not given. Readings: at the theta peak, or the mean over 5–11 Hz.
- **Group phase:** the circular mean of significantly modulated cells' preferred phases, or the peak of the pooled spike histogram.
- **"Ascending phase" minimum:** 180–360°, or the shaded column, about 280–340° as read from the figure.
- **"Approximately opposite":** more than 90° apart (by symmetry with the paper's own "<90° = in phase"), or within 45° of 180°.
- **Thresholds the paper doesn't give:**
  - **Fig. 3C EC3 subgroup:** within 90° or 45° of the EC2 mean.
  - **Fig. 4 offsets:** what counts as "small" or "large".
  - **Similarity across tasks and phase methods:** within 45° or 90°.
  - **"Close correlation" in Fig. S11:** a correlation above 0.5.
  - **"Robust" precession:** more than half of fields.
  - **"Two small peaks" in burst firing:** two local maxima, or a two-component mixture.
- **Which peak sets the 50–85 ms offset:** the first significant peak of the group cross-correlogram, or the mode of the pair-offset distribution.
- **"Negatively correlated" fields in Fig. 7A:** r < 0, or r < 0 with p < 0.05.
- **Multitaper settings for Fig. 7B and Fig. S18:** time-bandwidth 3 with 5 tapers, or 5 with 9.
- **Open-field shift magnitude:** median or mean shift.
- **Ripple fold-increase baseline:** −500 to −250 ms, or the rate outside ripples.
- **Fig. 8:** how the CSD phases of Montgomery et al. were referred to EC3 theta. "Half a cycle" is read as more than 90°, or 180 ± 45°.

**Missing for claims.** The Fig. 8 CSD sink phases have no archive the paper names. Hippocampal Fig. 3D values exist only as bar heights, read approximately. The CRCNS data description suggests hc-2 holds only CA1 recordings in the open field, which I didn't check further. If so, the many claims that need EC, CA3/DG or other tasks will be untestable, and each criterion says so.
