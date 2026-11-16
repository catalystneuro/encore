**Verifier report, round 2: Sohn et al. 2019 on DANDI:000130 (0.241017.1448)**

The claims file lists 23 claims, and the attempt record has 23 outcomes: 8 reproduced, 5 partially reproduced, 7 not reproduced and 3 blocked (data_missing).

### 1. Outcomes and assumptions

I agree with all 23 stated outcomes. Each follows from the printed outputs under its criterion.

- beh-slopes, not reproduced (NB1 cell 8): 6 of 8 slopes lie in (0,1).
- beh-overlap-prior, not reproduced (cell 12).
- beh-sigmoid-increments, reproduced (cell 15).
- beh-long-more-bias, reproduced (cell 18).
- beh-bayes-model, partially reproduced (cell 21): bias R² is at least 0.8 in 2 of 4 datasets.
- glm-prior-ts, not reproduced (cell 26): 79.2% and 45.8%.
- dfr-overlap-support, reproduced (cell 30).
- pca-dimensionality, not reproduced (cell 35): 1 of 8 values in range.
- encoding-r2, reproduced (cell 38).
- encoding-bayes-beats-linear, partially reproduced (cell 42).
- short-in-long-control, reproduced (cell 45).
- neural-long-more-bias, partially reproduced (cell 48).
- speed-vs-projection, partially reproduced (cell 54).
- initial-speed-biased, not reproduced (cell 57): p = 0.0547.
- speed-predicts-tp, partially reproduced (cell 60): −0.722 and −0.744, both negative with p < 0.05 and both outside tolerance.
- alt-speed-unmodulated, reproduced (cell 63).
- alt-transient-parallel, reproduced (cell 68).
- alt-threshold-monotonic, not reproduced (cell 71): −250 ms.
- gpfa-variance-inverted-u, not reproduced (NB2 cell 8): every variant gives p ≥ 0.074.
- gpfa-mean-sigmoid, reproduced (NB2 cell 11).
- rnn-curved-manifold, rnn-perturbation and monkey-g, blocked.

Assumptions:
- Only beh-long-more-bias carries `assumed: true`, for a regression with an intercept. It is stated in the deviation, the notebook (cell 19) and the README. It is reasonable: a slope below 1 shows a bias toward the mean only if the line has an intercept. The other reading (3 of 4, partial) is shown.
- No other outcome needs the flag. Where the attempt made a choice (Long-prior GLM windows, the RMSE reading, the Short In Long axis, the GPFA iteration cap and z-scoring), the alternatives give the same outcome.
- pca-dimensionality, encoding-bayes-beats-linear and neural-long-more-bias rest on a choice the claims file fixed: unnormalised rates. With normalised rates some outcomes change (cells 35 and 51):
  - pca-dimensionality: z-scored rates put 8 of 8 values in range.
  - encoding-bayes-beats-linear: the soft-normalised space gives 4 and 4 of 4.
  - neural-long-more-bias: 4 of 4 in both normalised spaces.
  
  The record reports this and puts the question to the authors, which is appropriate.

### 2. Sentences the outputs do not support

- **NB1 cell 66, and the attempt record notes for alt-speed-unmodulated.** "The growth of the step distance over the support is what the falling number of trials gives without any time course" and "The positive slopes are what attrition gives without any time course." In cell 65, 3 of 8 observed slopes lie outside the permutation 95% range. Eye Left Short is above it (7.926 against 7.796; frac_null_ge 0.02), and Hand Left Short and Eye Left Long are below it. Attrition explains the sign and size of most slopes, but not "without any time course" in every dataset.
- **NB1 cell 75 (Summary).** "alt-speed-unmodulated | reproduced (…; slopes no larger than with time permuted)" is contradicted by Eye Left Short, above (cell 65).
- **NB1 cell 46.** "so the data show a smaller version of the Short-prior effect, not its absence."
  - In Hand Left the single-axis difference is −0.0007, which is zero.
  - In the variants (cell 51) the Bayesian RMSE is lower in only 2 of 4 datasets (soft) and 1 of 4 (z-scored).
  - The record's milder "a smaller version of the Short-prior effect in this period" holds only in the unnormalised 2-PC space. The record should say so next to the variant counts it already gives.
- **NB1 cell 75 (Summary): "The paper's PCA, GLM fractions and Bayesian fits pool sessions (Methods)."** The record's round-1 response says it "Corrected the deviation, which said the paper pools sessions; Table S3 fits each session separately." The paper says both:
  - The STAR Methods say "we fit the 4 free parameters … after pooling across sessions (Table S3)".
  - The Table S3 legend says "We fit the model to each session separately".
  
  The beh-bayes-model deviation cites only the legend, while the encoding-r2 deviation ("the paper's model is fitted to pooled sessions") and the Summary cite only the Methods. The record and notebook should state the conflict once and consistently. No outcome depends on it.
- **Attempt record, beh-bayes-model notes: "In the Eye datasets the behaviour is nearly unbiased."** This is not supported.
  - Both Eye Long slopes are below 1 with intervals that exclude 1 (0.743–0.948 and 0.769–1.038; cell 8).
  - Eye Left Short has a mean bias of +64 ms at ts = 800 (cell 12).
  
  Cell 24's wording, that the model "predicts little bias", is supported.
- **Attempt record findings.**
  - "the electrodes table has no positions or impedances (x, y, z and imp are NaN for all 72)" and "The units carry no single- or multi-unit label…" appear in no printed output of either notebook.
  - "`tp` is longer than go_time − set_time in every completed trial" (also cell 75): cell 4 computes this over the 982 valid trials, not the 1025 completed ones.
- **README.** "about twelve minutes" for the GPFA notebook: NB2 cell 13 prints 986 s, about 16 minutes.

Everything else I checked matches the outputs:
- every other "Result:" sentence in both notebooks;
- the NB2 Summary;
- the remaining README rows;
- the remaining notes, including the GPFA convergence figures (5e-5 to 1e-4, then 2e-6 to 2e-5), Table S3 z-scores up to 1.68, and the speed and trial-by-trial correlations;
- the beh-slopes notes' "W = 2346, 68 slopes per prior", which is in Table S1 (n = 68 = 17 sessions × 4).

**My round-1 reasons in the record.** The `reason` fields state my round-1 reasons faithfully and in my own wording, with the round-1 problems attached to the claims they bear on. Two small defects:
- The pca-dimensionality reason ends "(problem 2)", a reference to my report's numbering that means nothing inside the record.
- Problem 11 (`glm_bic` returning None, so a failed fit counts as "not dependent") appears in no reason. It is answered implicitly by the printed failed-fit counts, which are 0.

### 3. Round-1 points

Resolved:
- **1. GLM windows for the Long prior.** The ts model now uses windows ending at 800–1200 ms. The ts fraction is 45.8%, still outside tolerance.
- **2. Production trajectories split by prior.** Now 10 per dataset. All outcomes are unchanged; speed-predicts-tp is now outside tolerance for both priors, still partial.
- **4. alt-speed-unmodulated.** A permutation null and unsmoothed rates were added, the bootstrap intervals were dropped as the effect size, and the smoothing question is put to readers. Only the overstatement in section 2 remains.
- **5. beh-slopes and Table S3.** The criterion question is put to readers and Table S3 is compared. The claims file still says the supplement was unavailable (beh-slopes and beh-bayes-model). That cannot be fixed by the author and is reported. Figure S1A appears to show some of monkey H's Short slopes above 1, which supports the reading that the criterion is stricter than the paper.
- **6. Random-axis reference.** Reported, including in the normalised spaces.
- **7. initial-speed-biased.** Re-run: p = 0.0547 again.
- **8. short-in-long-control.** The test's floor of p = 0.125 is reported. The overstatement in cell 46 remains (section 2).
- **9 and 10. GPFA.** Fits with up to 1500 EM iterations and z-scoring over the dataset were both run; all variants give not reproduced. x_dim = 8 at the top of the criterion's {4, 8} remains, but the criterion fixes that range.
- **11 and 12.** Failed-fit counts are printed (0). The effect of using nominal ts was negligible.
- **Figures.** The plotted values for cells 9 and 39 are now printed.

What remains that bears on a conclusion:
- **Problem 3, normalisation.** pca-dimensionality, encoding-bayes-beats-linear and neural-long-more-bias change outcome under normalised rates. Those outcomes hold only under the claims file's unnormalised choice, which the paper neither states nor rules out. The record reports this and asks the authors; it is still open.
- **The overstatements in section 2:** cells 46, 66 and 75 and the alt-speed-unmodulated notes. They do not change any outcome, but they go beyond what the outputs show.
- **The paper's conflicting statements on the Bayesian fits** (pooled in the Methods, per session in Table S3), used inconsistently across the record and notebook. This bears on how the beh-bayes-model and encoding-r2 deviations are described, not on their outcomes.
