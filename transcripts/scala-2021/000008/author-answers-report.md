One question was answered. Under its new criterion, fig5d-sst-pvalb-calb2-firing goes from blocked to reproduced, but only just: another seed would have kept it blocked. The entry is locked and passes `entry.py all` with 0 check errors. All three notebooks ran, the executed numbers match the new conclusion, and the handover is built in `executed/000008-scala-2021/handover/`. I did not verify my own work, and nothing is committed or pushed.

## The question: fig5d-sst-pvalb-calb2-firing, reading (b)

**What I asked:** whether reading (b) should be judged with a fixed, larger number of permutations (or exactly), since with 1,000 permutations the random seed decided the result.

**What the answer changed:** the paper has no test for this; the 1,000 permutations were the claims file's own choice. The criterion now says:
- Compute p exactly when there are at most 1,000,000 subsets of that size.
- Otherwise use 100,000 random subsets, with p = (k + 1) / (N + 1).
- Reading (b) holds only when p < 0.05 and the upper bound of the 95% Clopper-Pearson interval is also below 0.05.

**Re-run:**
- There are 10,400,600 subsets of 13 cells out of 26, so the 100,000-subset rule applies.
- With the section's existing seed (55), p = 0.0485 and the interval is 0.0472 to 0.0499, so (b) holds.
- Reading (a) still holds (rho = 0.363, one-sided p = 0.034).
- Both readings hold, which the criterion counts as reproduced.

**How thin the margin is:** I added two variants to the notebook.
- The exact p-value over all 10,400,600 subsets is 0.0497, which agrees with the main result.
- The 100,000-subset estimate with five other seeds (56 to 60) gives 0.0496 to 0.0514. Each of those intervals reaches 0.05 or above, so (b) would fail under the criterion with any of them. The seed can still decide the outcome.

The notebook conclusion, the attempt record notes and the README all say this. Seed 55 was the section's seed before the answer came in; I did not pick it afterwards. I added a follow-up question to `questions/000008.yaml`: should (b) be judged on the exact p-value when it can be computed? Here that is 0.0497.

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| fig5d-sst-pvalb-calb2-firing | blocked (methods_underspecified) | reproduced (p = 0.0485, bound 0.0499; exact p = 0.0497) |

**Files changed:**
- `entries/000008-scala-2021/scala_2021_transcriptomics.ipynb`: the test cell, its conclusion and the summary.
- `entries/000008-scala-2021/README.md`: the outcome table.
- `attempts/000008-scala-2021-01.yaml`: the outcome, notes and deviation.
- `questions/000008.yaml`: the new follow-up question.
