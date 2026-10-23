I've written `claims/000931/10.1016-j.celrep.2024.114013.yaml`. The quote checker reports 37 claims, 37 quotes, 8 statistical values and 0 problems. The style rules (no em dashes outside quotes, no "rather", no ": " in plain scalars) also check out. Nothing was committed.

**Text read**
- The version of record, as text extracted from a publisher PDF that a person supplied. It includes the main text, figure legends, STAR Methods and the supplement (legends of Figures S1 to S6). The paper has no supplementary tables, and I didn't need to open the PDF.
- The code: `iurillilab/mechano-olfactory_code` v1.1, commit 3bec502, from the Zenodo deposit doi:10.5281/zenodo.10381293. It holds MATLAB scripts and Python notebooks for each figure panel. Its panel letters follow the bioRxiv preprint, not the published figures.
- The code leaves some steps uncovered. It loads preprocessed files and helper functions that aren't in the repository. It has nothing for:
  - the inhalation clustering;
  - the phase decoding;
  - Figure 5G to 5I;
  - Figure S2C;
  - Figure S6H.

**Claims**
- 37 claims, all with quotes and criteria. 16 have expected values and 6 have statistics.
- They cover inhalation sorting, phase and speed decoding, odor responsiveness, sniff effects on responses (Figure 1H to 1L, S1), the GLM (Figure 2, S2), and airflow tuning under anesthesia, awake and after nerve section (Figure 3, S3).
- They also cover bulbectomy and motor cortex (Figure 4, S4), population decoding and encoding angles (Figure 5, S5), the simulation (Figure 6) and the waveform check (S6H).

**Where the code settles or disagrees with the Methods**
- **Odor-inhalation window:** the Methods say 0 to 5 s after odor onset; the code uses 0.4 to 5 s. The Methods window is the main reading and the code's is a variant.
- **GLM:** the code fixes the concentration coding (0, 0.33, 0.66, 1) and the penalty (lambda_1se).
- **Tests the code ran differently from the legends:** the legends name signed-rank tests for Fig 1J and 1L, but the code runs rank-sum and Kolmogorov-Smirnov tests. The legends' tests are used, with the code's as variants.
- **Fig 5C angle transform:** the Methods give 90 − |90 − Q|; the notebook computes |90 − angle|. The Methods form is used.
- **Fig 5E/F selection bound:** the code's lower bound differs slightly from the Methods' tan(π/12). The code's is a variant.
- **Fig 6 simulation:** the code models the inhalation-driven concentration change differently from the Methods. The code's model is a variant.

**Details left open, with the readings named**
- **Odor-responsiveness test (Fig 1H):** what the signed-rank test compares isn't stated. Readings: whole 5 s odor period against the preceding period, one-sided or two-sided; or the per-trial inhalation response against odorless inhalations.
- **CDI (Fig 1L):** the sample size per draw and how the mixed sample is made up. Three readings.
- **GLM "91.9% of variance":** pooled R² of condition means, per-pair R², or deviance explained.
- **Speed decoding:** whether "400 inhalations" is the total or per class.
- **Bulbectomy fraction:** the text says 15.7%, but 23 of 153 is 15.0%. Readings: pooled over neurons, or the mean of per-mouse fractions.
- **Motor cortex:** which mice hold the neurons (the code takes them from both groups), and the chi-square threshold (0.05 or 0.01).
- **Number of neurons in the angle analysis:** all 464, or 143.
- **SD for the sniff-invariant and mechanosensitive selection (Fig 5G to 5I):** per odor, or over pooled pairs.
- **Fig 5I two-way ANOVA:** its factors aren't given. Two readings.
- **Fig S2C:** which weights are used (GLM or linear model) and what makes an R² "significant".
- **Inhalation clustering:** how the dendrogram is cut when it gives three clusters.
- **Words like "similar", "monotonic", "several tens of ms" and "could not decode":** the paper reports no test for them, mostly for Fig 3B, S1D, S3E, S6H and the Fig 5 panels shown as mean ± SD. Each criterion names readings. Where a figure shows mean ± SD, decoders are judged against chance by one SD.

**Missing from the paper**
- Nothing a claim needed is missing.
- The Methods list the odor panel inconsistently: three odors at "0.01 and 1%" against the four-odor, two-concentration experiment. The author has to take odors and concentrations from the files.
- Fig 3 and the Methods disagree on the artificial airflow pulse rate (1 Hz against 750 ms intervals). It doesn't affect any criterion.
