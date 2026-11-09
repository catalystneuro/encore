**A. Outcomes**

The claims file holds 39 claims, all tested in the notebook. Totals: 17 reproduced, 15 partially reproduced, 6 not reproduced, 1 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| cohort-counts | not_reproduced | Cells 9 and 12 give 136 started, 83 at P1 (main reading) and 60 at P2, against 206/140/98. The dataset only covers 2019-06-11 to 2020-03-23 (178 subjects). The criterion judges on the counts. |
| fig2g-days-to-proficiency | partially_reproduced | Cell 14, main/incl: mean 19.87 and max 58 are in tolerance. s.d. 11.39 (needs ≥11.7) and min 5 (needs 3) are not. The excl count gives the same split. |
| fig2g-days-differ-across-labs | partially_reproduced | Cell 16: Kruskal-Wallis p=0.029, so the labs differ at 0.05 but not at the required <0.001. Lab 2 IQR 7.75 is in tolerance; Lab 6 IQR 5.75 is far from 22. |
| fig2s1-trials-to-proficiency | partially_reproduced | Cell 18: the mean of 11,839 and the 7,329 trials to reach 80% are in tolerance. s.d. 7,515, min 2,357 and max 34,998 are not. |
| fig2h-proportion-learned-40-days | reproduced | Cell 20, main reading: Kaplan-Meier 0.749 (incl) / 0.741 (excl) at day 40, within 0.8±0.08, and 1.0 at the last day. This is over 136 mice, not 206. |
| fig2bc-threshold-bias-iqr | partially_reproduced | Cell 22: at most 4 of 8 bounds are in tolerance under any reading. The early bias IQR (−8.4 to 6.1) and the early threshold upper bound (24.3 vs 29) miss. The threshold IQR does narrow. |
| fig2-abs-bias-threshold-during-training | reproduced | Cell 24, main/filtered/pooled: means 8.82 and 18.39 are in tolerance, which is what the criterion requires. The s.d.s (6.4 vs 12.1; 8.8 vs 11.7) are well below the paper's. |
| fig2s2-variability-decreases | partially_reproduced | Cell 26: the mean rises and the s.d. falls under every reading. At most 3 of 4 values are in tolerance (day-15 s.d. is 15–17 vs 19.1). |
| early-sessions-predict-slow-learners | blocked (methods_underspecified) | Cell 28: accuracy readings range 0.14–0.67. Some are near 0.53 and some are at chance (base rate 0.253), so the readings disagree. The criterion says that case is blocked. |
| fig3c-easy-errors-basic | partially_reproduced | Cell 32, main reading: s.d. 3.79 is in tolerance; mean 8.41 is just outside 9.5±0.95. |
| fig3de-threshold-bias-basic | reproduced | Cell 34, main reading over mice: all four values (14.09, 3.80, −0.46, 8.09) are in tolerance. |
| fig3cde-no-lab-difference-medians | reproduced | Cell 37, main reading: smallest FDR-corrected Kruskal-Wallis p is 0.287. (Both 1b-replace variants fail.) |
| fig3cde-no-lab-difference-variances | reproduced | Cell 37: smallest FDR-corrected Levene p is 0.268. |
| fig3s2a-trial-duration | partially_reproduced | Cell 39: s.d. 219 ms is in tolerance. Median 420.4 ms is just outside (needs ≥421.2). Lab p=0.061 uncorrected, so the lab difference is not shown. |
| fig3s2b-trials-per-session | partially_reproduced | Cell 41: ANOVA p=1.2e-4 (not <1e-6), s.d. 197 is out of tolerance, the mean is in. All significant Tukey pairs involve Lab 7. |
| fig3f-classifier-chance-basic | reproduced | Cell 73: accuracy 0.140±0.063; 2.5th percentile 0.029 ≤ null 0.106. The notebook's chance level of 0.106 matches the paper's 0.11. |
| fig3f-positive-control | reproduced | Cells 73–74: 2.5th percentile 0.257 > null 0.118. All off-diagonal mass falls on same-time-zone labs. |
| fig3s3-other-classifiers | partially_reproduced | Cell 73: Logistic Regression is not above chance (2.5th percentile 0.000 vs 0.070). Cell 75: Random Forest ran only 6 of the 2000 subsamples. Those 6 are not above chance, but that decides nothing. |
| lab-link | reproduced | Cell 43: the 7 institutions map one-to-one to the 7 labs. The start times labelled "+00:00" are not UTC: Berkeley's median of 11.0 would be 04:00 local. They look like local times. |
| fig3s1a-choice-consistency-basic | reproduced | Cell 45: p=0.458 on S1, and ≥0.44 under all variants. |
| fig3s1bc-choice-consistency-full | not_reproduced | Cell 49: choice consistency by block gives p=0.0168 (<0.05). The bias-shift test gives p=0.154. |
| fig3s4-looser-criterion | partially_reproduced | Cell 51: 91 mice vs 150±15. Trials per session differs (FDR p=0.002) as claimed, but trials per minute also differs (FDR p=0.002). Cell 73: the classifier is not above chance. |
| fig3s5-first-full-sessions | not_reproduced | Cell 56, main reading: threshold 20:80 p=0.022, threshold 50:50 p=0.038 and 100%-contrast performance p=0.022 (Kruskal-Wallis, uncorrected as the legend names it). Only the code's Holm-Sidak variant passes (min 0.14). |
| fig3s5a-prior-used-from-first-sessions | reproduced | Cell 59: median bias difference 4.45, 69 of 72 mice positive, p=2e-13. |
| full-task-training-time | partially_reproduced | Cell 61: mean days 29.4 and mean trials 19,637 are in tolerance. Both s.d.s, the min and the max (days and trials) are out, over 60 mice. |
| fig4cd-biasshift-largest-at-zero | reproduced | Cell 63: mean 28.0 vs 28.5±2.85, and the lab mean peaks at 0% in all 7 labs. |
| fig4de-biasshift-no-lab-difference | reproduced | Cell 65: ANOVA p=0.072. |
| fig4f-threshold-unchanged-by-block | reproduced | Cell 67: Wilcoxon p=0.80. |
| fig4gh-lapses-change-with-block | partially_reproduced | Cell 68: both directions hold, but p=2.3e-6 and 2.2e-5 miss the 1e-6 and 1e-7 bounds, which n=60 could reach. |
| fig4i-bias-shifts-with-block | partially_reproduced | Cell 69: all 60 mice go the right way, p=1.6e-11. That is the floor for n=60, so p<1e-16 cannot be reached with this sample. |
| fig4fi-no-lab-difference | reproduced | Cell 71: smallest FDR-corrected p is 0.189. |
| fig4j-classifier-chance-full | reproduced | Cell 73: 2.5th percentile 0.086 ≤ null 0.107. |
| fig5cf-glm-weights | partially_reproduced | Cell 80, main reading: 100% weight is 3.6 in both tasks. Without the 50% weight, the unrewarded basic weight of 0.2966 misses tolerance (≥0.297) by 0.0004. With it, all 4 history weights are in tolerance but the `increasing` check fails (see B3). Only the variant P1b passes everything. |
| fig5dg-history-weights-higher-full | partially_reproduced | Cell 82: the rewarded test passes under every reading (t≈9.9). The unrewarded test passes with the code's sessions (t=3.54, p=7e-4) but fails with reading (b) (p=0.30). |
| fig5s2-glm-accuracy | reproduced | Cell 84: accuracy (81.9 / 83.5) and full-model condition number 3.14 are in tolerance under every reading. Basic condition number is 2.38 under the code's model (no 50% trials), which reproduces as fig5cf's "under one reading" rule allows. The notebook's "blocked" depends on its own agree-or-block rule, not on the criterion. |
| fig5s2-weights-similar-across-labs | not_reproduced | Cell 86, main reading: 6–7 of 19 lab tests give p<0.05, all on visual weights. The criterion allows at most 2 for partial. |
| fig5s1b-win-stay-lose-switch | reproduced | Cell 88: share of mice with both signs is 0.587 (basic) and 0.859 (full). |
| fig5s1c-updating-by-contrast | reproduced | Cell 90: updating after 0% and after 6.25% exceeds that after 100% in both tasks. The basic-task 0% mean rests on only 4 mice; the pooled 0+6.25% value (69 mice) agrees. |
| session-end-criteria | not_reproduced | Cell 92: 6,539 sessions, 5,698 met a criterion (87% vs the paper's 51%), extra trials median 16 / m.a.d. 14 vs 19±1.9 / 16±1.6. |

**B. Problems**

1. [affects a conclusion] `training_status` and `full_proficiency` require the median 0% reaction time to be <2 s. With stimOn missing, rt0 is NaN, so the test fails and the window is rejected. Cell 6 shows 257,021 trials without stimOn, 185 sessions with none and 2,858 with some missing. The notebook never counts how many 1b or P2 windows fail only for this reason, so P1 status (1a vs 1b), the P1b variant and P2 (60 mice) could be undercounted. That would affect cohort-counts, full-task-training-time and every S2 claim.
2. [affects a conclusion] Cell 9 selects "complete" mice as those whose first session in the dataset shows only 50% and 100% contrasts. A mouse that started stage 1 before 2019-06-11, the first date in the dataset, would also pass, and its training days would be undercounted. The notebook never shows how many complete mice start on 2019-06-11. This bears on fig2g (min 5 vs 3), fig2s1, fig2h and full-task-training-time.
3. [affects a conclusion] Cell 80: with the 50% weight kept (drop50=False), `increasing` compares the mean 50% weight over the 7 mice that have it with means over all ~70 mice. That reading's failure, and so fig5cf's outcome, may be an artifact of this. The per-contrast means are not printed.
4. [affects a conclusion] Cells 75 and 84 mark two claims blocked for reasons that are not data limits. fig3s3: the Random Forest needs ~4.9 h single-threaded on data already loaded; the archive holds everything needed. fig5s2-glm-accuracy: blocked under the notebook's own rule that readings must agree, which the criterion does not state.
5. [does not affect a conclusion] Cell 41: the column `p_anova_fdr` holds `labtests[r].loc["n_trials","kruskal_fdr"]`, a Kruskal-Wallis FDR value, not an ANOVA one.
6. [does not affect a conclusion] Cell 20: the "excl" count gives events p1_tday0 but leaves censored mice at max(tday0)+1, mixing the two counts. The "drop_in_training" variant's rule ("a session in the last 7 days") is the author's own; it is only a variant.
7. [does not affect a conclusion] Cell 92: values of `disengaged` == False (727 sessions) count as "not met" with no recomputation, while None is recomputed. This is not justified, but the totals miss tolerance either way.
8. [does not affect a conclusion] `full_proficiency` slides over consecutive full-task days, not sessions. The two can differ on the 73 days with more than one session (cell 9).
9. Checked and found sound:
   * The NB and LR leave-one-out classifiers match scikit-learn (cell 73, 100% agreement). I re-ran the NB check on synthetic data: identical, and its random-feature null at 5 mice per lab is 0.111, consistent with the paper's 0.11.
   * The vectorised consistency null equals the direct computation on synthetic data.
   * `end_criterion_trial` returns the expected trial on synthetic inputs for all three criteria.
   * The GLM history coding is correct on a toy session.
   * The P1 and P2 thresholds match Appendix 1, table 1d.
   * The choice sign is confirmed against feedback (cell 6).
   * No train/test leakage in the leave-one-out or k-fold code.

**C. Not checked, and the output that would settle it**

- Effect of missing stimOn on proficiency (B1). Needed: per reading, the number of candidate windows that pass every criterion except rt0 only because rt0 is NaN, for both 1b and P2.
- Start dates of the complete-history mice (B2). Needed: the distribution of first-session dates of the 136 mice, and how many start on 2019-06-11.
- fig5cf monotonicity (B3). Needed: mean per-contrast weights per task, restricted to mice that have every weight.
- fig3s3 Random Forest. Needed: the full 2000-subsample run (parallel).
- Whether the archive holds the paper's other mice: it does not. All published versions (draft, 0.211209.1412, 0.211209.1413) hold the same 6,615 assets and 178 subjects, so the cohort shortfall is the dataset's.
- None of the blocked claims is blocked by the archive: the data for all three is loaded in the notebook.
- I did not find any place where the claims file misreads the paper. The table 1d criteria, the Figure 4 p bounds, the classifier chance level (0.11) and the session-end counts all match the paper text.
