I've checked and corrected the claims file, and it is ready for an attempt. Nothing is committed or pushed.

**Checker result after the changes:** `claims/000576/10.1016-j.neuroimage.2020.116705.yaml: 25 claims, 23 quotes, 21 statistical values, 0 problems`. Before the changes it reported 23 claims and 0 problems.

**Changes, by claim** (each is also listed under `checks`):
- **fig1b-delta-decrease**:
  - The Results report the delta decrease for amygdalae outside the seizure onset zone (nSOZ), and the statement now says so.
  - The rule giving a partial result when the significant clusters cover less than half the block had no source. It now rests on Discussion 3.1 ("lasted for most of the AVERSIVE sequence"), read as more than half, and the cluster extent is compared with the abstract's 18 s.
- **table2-bold-correlations-group**: I removed the `p < 0.05`, FDR entry from the statistics. It is the threshold used to count significant amygdalae, so it is a method, not a result.
- **fig2-participant4-bold-correlations**: Methods 4.10 say the BOLD and iEEG correlation is made "at the single trial level", which the criterion did not mention. It is now named as open, with two readings: one correlation over the whole sequence, or one per trial, averaged.
- **fig3d-firing-correlations-modalities, fig4d-hgp-bold-covariation**: `n: 41 neurons` was not from the paper. Only neurons in amygdalae with fMRI have BOLD (Tables 1 and 2), so not all 41 can enter. Both now say the number is not given.
- **fig4b-regression-firing-hgp**: The criterion required both coefficients to be positive, but the paper gives no signs. It now requires both with p < 0.05 and reports the signs.
- **fig3a-firing-increase-aversive**: noted that the paper prints no unit for FRV.
- **New claim nsoz-delta-hgp-mi-inverse**: Results 2.1, paragraph 2, says that among nSOZ amygdalae, stronger high gamma enhancement goes with stronger delta reduction. No claim covered it. The paper gives no test, so the criterion uses Spearman correlation, the paper's correlation measure.
- **New claim table2-bold-correlation-values**: Table 2 prints 18 per-amygdala BOLD correlations, which no claim held. The minus signs are garbled in the text, so I read them from the table and checked them against the counts in Results 2.2.

**Still open:**
- **Unnamed tests**: the paper does not name the tests behind p = 0.009 (table2-hgp-mi-positive-nsoz) and p = 0.019 (fig1e). The criteria list possible readings.
- **Fig. 1F**: the counts 5/5 against 1/5 match no subset of Table 2. A chi-square test of those counts gives p of about 0.01 (0.05 with Yates' correction), not the printed 0.2. I left the criterion as it was.
- **Fig. 1D**: the legend prints r = 0.67 with no sign, while the Results give -0.67. The Spearman r of the printed Table 2 values is -0.74. The claim keeps -0.67 and also reports the value from the printed table.
- **Microwire counts**: the paper is inconsistent. The abstract says 5 participants, the Results say 9 amygdalae, and Table 1 lists 8 amygdalae of 6 patients. This is recorded in neuron-count but not settled.
