I worked through every point in the round-1 report and re-ran the entry. No outcome changed: the verifier agreed with all 23 outcomes, and the new analyses leave each one where it was. The clean run of `python tools/entry.py all entries/sohn-2019` passes with 0 check errors and takes 26 min (1581 s). Every conclusion matches its output. Round 1 is recorded under `verifications` in `attempts/sohn-2019-02.yaml`, with the verifier's reason for each claim and a `response`.

**Outputs added for the verifier's points**
- **GPFA convergence (problem 2):** the fits now run 1000 EM iterations. The log-likelihood still rises by 0.17 to 0.53 per 10 iterations at the end, against 7 to 14 at iteration 200.
  - gpfa-variance-inverted-u has p = 0.0547. The old 200-iteration fit gives 0.0742, and a fit with trials ending at the actual Set gives 0.125. All three fail, but the p value sits near 0.05 and moves with the fit.
  - gpfa-mean-sigmoid holds in all three fits; the main fit is now 7 of 8, p = 0.0156.
- **Smoothing width for pca-dimensionality (problem 3):** both epochs were run under the other readings. SD 20 ms puts 2 of 8 values in range and a 40 ms full width at half maximum puts 3 of 8, so it stays not reproduced. Unsmoothed rates give 5 of 8, but the Methods smooth, so that is not a reading of their method.
- **Noise in the speeds (problems 5 and 7):** I added a helper, `rsg.split_noise_sq`, that estimates how much of each speed is noise, by splitting the trials into random halves. This is my addition, not the paper's method.
  - For alt-speed-unmodulated, noise grows faster through the support than the measured speed does. With the noise removed, every slope is negative, so the rise the verifier flagged comes from noise.
  - The old bootstrap intervals were not valid confidence intervals. The record now says so and shows corrected intervals beside them, which include 0 in all 8.
  - For the speed claims, removing the noise leaves speed-vs-projection and speed-predicts-tp outside tolerance. For initial-speed-biased the effect weakens from p = 0.039 to p = 0.078 as a variant; the main result is unchanged.
- **Other variants:**
  - glm-prior-ts with the last window aligned to the actual Set: 75.0% and 43.8%, still out of range.
  - alt-threshold-monotonic smoothed past Go and then cropped: at the criterion's 60% the median minimum stays 230 ms before Go. At 75% it moves to 80 ms, which would be partial, but the criterion fixes 60%.
  - short-in-long-control: the paper's prior × model interaction run here gives F(1,3) = 0.56, p = 0.51, against the paper's F = 161.
- **Text corrections:** the encoding-r2 conclusion now says the test barely singles out the encoding axis. Both absence claims now say their test cannot fail with 4 datasets.
- **Header and data check (problem 10):** cell 0 no longer says the supplement was missing or that there is only one published version. 0.220113.0407 holds the same files as the pinned version.
- **Table S3:** beh-bayes-model now compares the fitted parameters with Table S3. The eye datasets' wm is low, at z = −1.56 and −1.13.
- **GPFA session:** the paper never dates its GPFA session, so the matching count of 48 units is the only link. The notebook and a finding now say so.
- **New finding:** a `paper_inconsistency`. The Methods give monkey G's GPFA session as 96 neurons, and the Figure S6 legend gives it as 107.

**Questions to a reader** (new file, `questions/sohn-2019.yaml`). The claims themselves are unchanged.
- beh-slopes: Table S1 tests the median slope with no intercept, while the claims file requires every condition to pass. Under the Table S1 reading, no p reaches 0.05 with 4 datasets.
- beh-bayes-model: should the criterion compare the fit with Table S3?
- short-in-long-control: should the criterion test the interaction?

**Not done**
- No claim was marked as resting on an assumption. Every reading I ran gave the same outcome.
- For problems 4, 6 and 7, I recorded the disagreement and kept the outcomes. The absence rule judges those claims on the paper's test alone.
- The GPFA cross-validation still runs 200 iterations, to save time. It picks 8 latent dimensions by a wide margin, 566 to 683 in summed held-out log-likelihood.
- Nothing is committed or pushed.
