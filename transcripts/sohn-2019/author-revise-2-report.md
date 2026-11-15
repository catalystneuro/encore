Round 2 is handled. No outcome changed and nothing is proposed for round 3. The entry re-ran cleanly with `python tools/entry.py all entries/sohn-2019`: checks report 0 errors, the main notebook took 174 s and the GPFA notebook 1412 s, and every number I cite matches the new outputs.

**Outcomes**
- **beh-long-more-bias:** stays partially reproduced, now marked `assumed: true`, as the verifier asked.
  - The regression through the origin, as the Methods write it, gives 3 of 4; with an intercept it gives 4 of 4.
  - The notebook now prints the intercepts of the regression with one (-60 to +435 ms). The slopes through the origin are within 0.010 of mean tp / mean ts in every condition, which supports the verifier's point that they mostly measure that ratio.
  - I added a question for a reader in `questions/sohn-2019.yaml` and put back the finding asking the paper's authors whether the regression had an intercept.
- **encoding-bayes-beats-linear:** stays partially reproduced. It would become not reproduced under the narrower kernels, but the claims file fixes SD 40 ms and the kernel width is already an open question to a reader. The record notes the disagreement.

**Corrections**
- **Summary:** "about 80% of trials analysed" now reads 983 of 1443 (68%).
- **Signed-rank limit:** the README, summary and record no longer apply the "cannot fall below p = 0.125" sentence to every test.
  - It now applies only to the tests over the 4 datasets, so only short-in-long-control and alt-speed-unmodulated are said to be unable to fail.
  - alt-transient-parallel, initial-speed-biased and the GPFA claims test 8 dataset-priors and could reach p = 0.0078.
  - I removed the sentence from the correlation claims and from alt-threshold-monotonic.
- **GPFA sessions:** the GPFA summary and the record now quote the paper's "high-yield sessions (N=48 for monkey H)" without saying it was one session.
- **Attrition (alt-speed-unmodulated):** "follows from attrition" is now "consistent with attrition". The text notes that the control also uses fewer trials and only the longest-ts ones, and that neither bootstrap interval removes the bias in the point estimate.
- **Variants reported in both directions:** the robustness table now prints p for each correlation, and the conclusions, notes, summary and README report the variants that hurt as well as those that help.
  - Without smoothing: encoding-r2 would be partially reproduced (Hand Left 0.909 and 0.581), speed-vs-projection not reproduced (+0.255, -0.036), and speed-predicts-tp not reproduced (-0.103, -0.310).
  - With outlier trials included: speed-predicts-tp Long is r = -0.439, p = 0.053, so it would be not reproduced.
- **Record:** round 2 is added under `verifications` with the verifier's reasons and my responses. The README and summary now count five open questions to a reader.

**Not done**
- The verifier counted 24 claims; the claims file and the record have 23. I recorded 23 results.
- I did not go back and edit the round-1 entry to attach the pooled-population problem to the speed claims, which the verifier called minor. The round-2 entry for speed-vs-projection notes it, and the existing question on the pooled population already covers those tolerances.

Nothing is committed, as instructed.
