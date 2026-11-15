I went through all 12 points in the verifier's report. No outcome changed. The verifier agreed with all 23 outcomes in round 1, and every fix and new variant left them where they were. The final run of `python tools/entry.py all entries/sohn-2019` passed both notebooks with 0 check errors, and the conclusions match the new numbers.

**Fixed**
- **Production epoch (point 2):** `rsg.production_rates` was pooling the Short and Long trials at ts = 800. It now keeps them apart, giving 10 trajectories per dataset. New values, same outcomes:
  - speed-vs-projection: r = −0.931 (Short) and −0.874 (Long), still partially reproduced.
  - speed-predicts-tp: r = −0.722 and −0.744. Both are now outside tolerance but negative with p < 0.05, which the criterion still calls partially reproduced.
  - pca-dimensionality: 1 of 8 counts in range, still not reproduced.
  - initial-speed-biased: unchanged, p = 0.0547.
- **glm-prior-ts (point 1):** the Long prior's ts model now uses windows ending at 800–1200 ms, citing the Methods' "two distinct GLMs". The ts fraction is 45.8%, still outside 27 ± 2.7%, so still not reproduced. The old windows are shown as a variant (50.0%).
- **beh-bayes-model (point 5):** a new cell compares the fits with Table S3. Every parameter is within 1.7 SD of the paper's session mean. I corrected a wrong deviation: the paper fits each session separately, not pooled.
- **Findings:** I corrected the finding that said the supplement was unavailable. It now asks the paper's authors about normalising rates before PCA and about the GPFA settings.

**Outputs the verifier asked for**
- **Normalised PC spaces (point 3):** the encoding claims are now also run on soft-normalised and z-scored rates, with the random-axis reference. These are variants only. The claims file fixes unnormalised rates, so the outcomes stay on that, and the verifier's objection is recorded.
- **alt-speed-unmodulated (point 4):** added a null that shuffles each trial's spike counts in time, on smoothed and unsmoothed rates. The observed slopes beat the null mean in 1 of 4 and 0 of 4 datasets (Short, Long), which supports the verifier's view that the positive slopes come from fewer trials being averaged late in the window. The notes now use this null as the effect size in place of the bootstrap intervals.
- **GPFA (points 9 and 10):** the notebook now prints the EM log-likelihood and refits with up to 1500 iterations. It also z-scores across both priors. Every variant still gives not reproduced (p = 0.074 or 0.098).
- **Figures:** the plotted values for the two figures are now printed.

**Questions for a reader:** I created `questions/sohn-2019.yaml` with three questions. It did not exist before.
- beh-slopes: Table S1 tests median slopes across sessions, which is looser than the criterion.
- alt-speed-unmodulated: smoothed versus unsmoothed rates.
- gpfa-variance-inverted-u: how to read "We z-scored Xu of all trials".

No claim was changed.

**Not done, and why**
- **short-in-long-control (point 8):** no question added. A test that cannot fail with 4 datasets is the protocol's rule for judging absence, not a misreading of the paper. The notes already say so.
- **Points 6, 11 and 12:** no code change. They don't affect any conclusion, and the record says why for each.

The record has the round 1 entry under `verifications`, with the verifier's reasons and my responses. I set the GPFA notebook's runtime in `entry.yaml` to 12 minutes; the clean run took about 12. I deleted a `.venv` I had created at the repo root while reading the supplement. Nothing is committed.
