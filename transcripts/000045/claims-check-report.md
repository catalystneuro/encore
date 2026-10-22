## Report on claims/000045/10.7554-elife.63711.yaml

**Checker:** `claims/000045/10.7554-elife.63711.yaml: 38 claims, 38 quotes, 26 statistical values, 0 problems`. I ran it once before my edits and once after.

I checked every claim against the paper text and against the paper-behavior code at the commit the paper cites (edc4531). The quotes, sources, statistics and most code citations are right. That includes the session windows, the FDR and test choices, the classifier rule, the GLM settings and the Kaplan-Meier coding.

**Changes, by claim**
- **fig2s1-trials-to-proficiency:** the file said no code computes the "~7.4 thousand trials". That is wrong: `supp_figure2_performance_trials.py` prints it. The criterion now follows that script's method, and the old per-mouse reading is kept as a variant.
- **fig2s2-variability-decreases:** added the per-day mean and s.d. over mice that the same script computes (it does not print them) as reading (1). Both day-counting conventions are named: from 0 as in the code, or from 1.
- **fig2h-proportion-learned-40-days:** the legend says the estimate covers all 206 mice. The main reading now keeps mice still in training as censored; the code's dropping of them is a variant.
- **fig2bc-threshold-bias-iqr:** stated that the code counts training days from 0, so the first 10 days are code days 0 to 9.
- **fig3de-threshold-bias-basic:** added the reported s.d. values (3.8 and 8.4) to `expected`.
- **fig3s5-first-full-sessions:** the legend's measure, performance on 100% contrast trials, is now the main reading. The code's measure (contrasts of 50% or more) is a variant.
- **fig3s5a-prior-used-from-first-sessions:** the bias-shift > 5 threshold is a criterion for counting mice as proficient, not a result, so it no longer decides the claim. The claim is now judged by the Figure 4i Wilcoxon test plus the direction of the shift; the threshold is reported as a variant.
- **early-sessions-predict-slow-learners:** added three more readings the text allows: quartiles from trials, bottom quartile against the rest, and precision of the bottom-quartile class.
- **full-task-training-time:** added the fastest and slowest mice in trials (4,691 and 61,316) to `expected`, since the statement reports them.

**Still open (recorded under `checks`)**
- **fig2-abs-bias-threshold-during-training:** the statement says absolute bias was "similar across laboratories" and mice were "not systematically biased". The paper gives no test or code for either, and the criterion does not judge them.
- **fig5s1c-updating-by-contrast:** comparing updating after 0% and 6.25% with updating after 100% is a reading of the legend's wording, not a test the paper names.
- **Tolerances:** where the paper gives mean ± s.d. over mice, the file sets the tolerance to 10% of the mean, not the s.d. The protocol's phrase "stated spread" could be read the other way. I kept the 10% rule, because an s.d. across mice is not an uncertainty of the mean.

Every main finding has a claim, and nothing comes from outside this paper.

**Ready:** yes (`ready: true`). Nothing was committed.
