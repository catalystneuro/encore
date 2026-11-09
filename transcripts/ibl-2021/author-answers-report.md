All seven answers are now applied: the claims were re-run under their updated criteria, and the notebook, README, `entry.yaml` and attempt record are updated. `entry.py lock` left the lock file unchanged, `entry.py all` passes (0 errors, 21.6 min), and the handover is built in `executed/000045-ibl-2021/handover/`. Nothing is committed or verified.

Where the claims file now names a main reading and variants, the main reading decides each outcome and the variants are shown. Each claim's notes say what the answer changed and give the earlier outcome.

## The questions and what each answer changed

1. **"All contrasts introduced" (fig2h and others).** The answer made "each of the three sessions" the main reading and the pipeline's check of the last session a variant; pooling over the three sessions is no longer a reading. With the header's account of how the pipeline computes the status, P1 is now computed per session over that session and the two before it, any protocol, with percent correct on trials of 50% contrast and up. Under the main reading 83 mice reach P1 (75 to 84 before).
2. **1b date and 1a vs 1b (cohort-counts, fig3cde medians).** P1 is now the first session meeting either set, at any date. "1b replaces 1a from 2019-09-12" is a variant.
3. **Trials completed.** All trials count, as already run. I removed the sensitivity that counted only trials with a response.
4. **P1b (fig3s5 and the fig5 claims).** The main reading is the first full-task session at or after P1, as already run. I added the code's P1b (at or after the first session meeting 1b) as a variant: 66 mice have one, against 72 under the main reading.
5. **50:50 sessions (fig2bc, fig2s2).** Basic-task sessions with all their trials, as already run. Only the text changed.
6. **Classifier subsample (fig3f and others).** The subsample is now the lowest lab count over the datasets classified, which is 5 mice per lab. All the classifiers now run. Naive Bayes and Logistic Regression are computed directly and match scikit-learn on every subsample checked.
7. **The 50% weight in the GLM (fig5).** The paper does not say what to do for mice shown no 50% trials, so readings (a) and (b) are open readings that must agree.

## Outcome per affected claim (earlier outcome in brackets)

| Claim | Now | Earlier |
|---|---|---|
| cohort-counts | not reproduced (83 of 140 reach P1) | not reproduced |
| fig2g-days-to-proficiency | partially reproduced | partially reproduced |
| fig2g-days-differ-across-labs | not reproduced | not reproduced |
| fig2s1-trials-to-proficiency | partially reproduced | partially reproduced |
| fig2h-proportion-learned-40-days | **reproduced** (0.749 at day 40) | blocked: methods underspecified |
| fig2bc-threshold-bias-iqr | partially reproduced | partially reproduced |
| fig2-abs-bias-threshold-during-training | reproduced | reproduced |
| fig2s2-variability-decreases | partially reproduced | partially reproduced |
| early-sessions-predict-slow-learners | blocked: methods underspecified | same |
| fig3c-easy-errors-basic | **partially reproduced** (mean 8.41, tolerance starts at 8.55) | reproduced |
| fig3de-threshold-bias-basic | reproduced | reproduced |
| fig3cde-no-lab-difference-medians | **reproduced** (smallest corrected p 0.287) | blocked: methods underspecified |
| fig3cde-no-lab-difference-variances | reproduced | reproduced |
| fig3s2a-trial-duration | not reproduced | not reproduced |
| fig3s2b-trials-per-session | partially reproduced | partially reproduced |
| fig3f-classifier-chance-basic | **reproduced** (not above chance) | blocked: other |
| fig3f-positive-control | **reproduced** | blocked: other |
| fig3s3-other-classifiers | **blocked: not runnable** | blocked: other |
| fig3s1a-choice-consistency-basic | reproduced | reproduced |
| fig3s4-looser-criterion | not reproduced (lab tests fail; classifier now not above chance) | not reproduced |
| fig3s5-first-full-sessions | not reproduced (three p below 0.05; classifier not above chance) | not reproduced |
| fig3s5a-prior-used-from-first-sessions | reproduced | reproduced |
| fig4j-classifier-chance-full | **reproduced** | blocked: other |
| fig5cf-glm-weights | partially reproduced under both 50% readings | partially reproduced |
| fig5dg-history-weights-higher-full | reproduced | reproduced |
| fig5s2-glm-accuracy | **blocked: methods underspecified** | reproduced |
| fig5s2-weights-similar-across-labs | not reproduced | not reproduced |
| fig5s1b-win-stay-lose-switch | reproduced | reproduced |
| fig5s1c-updating-by-contrast | reproduced | reproduced |

New totals: 17 reproduced (plus lab-link), 10 partially reproduced, 8 not reproduced, 3 blocked. The claims that do not use P1, P1b or the classifiers did not change (fig4 claims, full-task-training-time, fig3s1bc, session-end, lab-link).

Three of these need a word of explanation:
- **fig3s3:** Logistic Regression is not above chance. The Random Forest would need about 4.4 h for the 2000 subsamples the criterion asks, so it was run on 6 subsamples only, which decide nothing.
- **fig5s2-glm-accuracy:** the basic-task condition number is 2.89 under reading (a), outside 2.4 ± 0.24, and 2.38 under reading (b), inside. The two readings give different outcomes, so the protocol rule for open details blocks the claim.
- **fig3cde medians:** the "1b replaces 1a" variant would find a lab difference in performance (corrected p = 0.038). The main reading does not.

## Other changes
- **Runtime:** to keep the notebook under the time limit, the shuffle test, the window fits and the process pool are faster, and give the same results. Some costly variants now run only under the main reading of P1: early-sessions, fig5s1b and fig5s1c.
- **Finding:** I updated the paper_inconsistency finding: the claims file now follows the pipeline for the performance criterion (easy trials). With performance on 100% contrast only, as the Appendix table words it, 84 mice reach P1 against 83.
- **Untracked file:** `git status` shows a `scripts` entry at the repository root that I did not create. It is a character device dated before this session, and I left it alone.
