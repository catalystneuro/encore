The file is ready for an attempt (`ready: true`). I made no commits and changed no claim ids.

**Checker result** (same before and after my edits): `claims/memar-2026.yaml: 20 claims, 20 quotes, 0 statistical values, 0 problems`

**What I confirmed:** every Table II and III value, source paragraph and quote matches the paper. I recomputed the Average rows: the ± is the population SD across subjects, as the opening comment says. All main findings have a claim, and none comes from outside this paper.

**Changes, by claim:**
- **Opening comment (mask intensity):** the file said the paper never states the mask intensity for the main columns. The Methods (Eqs. 1, 2 and 7) define the model with the whole neighborhood masked, and the EEG transfer uses m = 1.0. I added this as support for m = 1.0 alongside the code.
- **intra-eeg-above-ieeg:** the paper does not define "consistently". I named two readings (every subject, or the averages); the claim is judged on the averages and the every-subject reading is reported.
- **cross-ieeg-mean:** the paper does not say which of the target's trials go into the electrode correlation matrix. I named two readings: all trials (as the code does) or the validation trials only.
- **cross-below-intra-ieeg:** I removed a comparison with the surrogate floor and an 11-of-12-subjects rule; the paper makes neither. "Appreciable" is now judged by cross-ieeg-mean, the number the paper gives for it.
- **lagged-ieeg-no-gain:** the 10% bound on the difference is now marked as an assumption, not the paper's. A large drop now also fails the claim; before, it was left undecided. The Wilcoxon test no longer decides anything.
- **full-mask-above-zero-ieeg:** the paper compares with zero only, which can never fail because DistCorr is never negative. I named two readings: above zero as written, and above the phase-shuffled surrogate average, which the author judges by as an assumption. I dropped an every-subject requirement the paper does not make.
- **fig5a-coverage-ieeg, fig5b-coverage-eeg:** I removed the 11-of-12 and 14-of-15 thresholds for "consistently". The claims are judged on the averages, with subject counts reported.
- **transfer-penalty-larger-ieeg:** I named the ratio and the difference as readings of "transfer penalty". Both give iEEG the larger penalty on the paper's numbers.
- **surrogate-order-ieeg, surrogate-order-eeg:** the statements said IAAFT keeps the most of the three surrogates. The paper says only that it "retained somewhat more". I restated the claims and now judge them on phase shuffle being lowest.

**Still open (recorded in `checks`):**
- Several details are left as named readings because neither the paper nor the code settles them: the m = 1.0 setting, which movement events and recording days form the trials, where preprocessing is applied, and the subject order. The repository's code may also not be the version that produced the reported numbers.
- The per-subject cross-subject tolerances are the paper's own SDs across electrodes (0.004 to 0.016), so those claims are very strict.
- The paper does not say how Figure 4 averages over electrodes and subjects.
- For the EEG claims (data elsewhere), the paper gives no BNCI accession or version, and does not say which session or trial window was used.
