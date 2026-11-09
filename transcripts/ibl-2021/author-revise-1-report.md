I made the round-1 revisions to `000045-ibl-2021`. The final run of `python tools/entry.py all entries/000045-ibl-2021` passes with 0 errors in 26.3 minutes, and its numbers match the earlier run. Nothing is committed.

**Outcome changes.** The new totals are 19 reproduced (plus lab-link), 13 partially reproduced, 5 not reproduced and 1 blocked.

| Claim | Was | Now | Why |
|---|---|---|---|
| fig2g-days-differ-across-labs | not reproduced | partially reproduced | I accepted the verifier's view: the labs differ at p = 0.029, not at the required p < 0.001, and one of the two interquartile ranges matches. |
| fig3s2a-trial-duration | not reproduced | partially reproduced | Accepted: the s.d. is within tolerance and the median, 420.45 ms, is just outside it. |
| fig3s4-looser-criterion | not reproduced | partially reproduced | Accepted: one of the six lab tests (trials per minute) and the mouse count miss. |
| fig5s2-glm-accuracy | blocked | reproduced | Accepted: my rule that readings of an open detail must agree is not in the criterion, so I removed it from the notebook header. All four values are within tolerance under reading (b). No other outcome rested on that rule. |
| fig3s3-other-classifiers | blocked | reproduced | The verifier said partially reproduced because the Random Forest was undecided. It now runs in parallel on 50 of the 2000 subsamples: its 2.5th percentile is 0.035 (bootstrap interval 0.029 to 0.057), below the shuffled mean of 0.100, so it is not above chance. |

**Disagreement kept.** fig5dg-history-weights-higher-full stays reproduced, against the verifier's partially reproduced. Its criterion uses the weights of fig5cf, which counts as matched when any one reading matches. The verifier applies that same rule to fig5s2-glm-accuracy, and on the code's sessions both t-tests pass. This is recorded under `verifications`.

**Outputs added for the report's problems:**
- **Missing stimulus onsets (B1):** no 1b or P2 window fails only because its reaction time is undefined (0 windows under every reading), so the counts are not lowered.
- **Mice that may have started before the dataset (B2):** 6 of the 136 mice start in its first week. Leaving them out leaves fig2g at two of four values within tolerance, and the five fastest mice started between August and November 2019.
- **50% weight in fig5cf (B3):** the failure is not caused by averaging over different mice. In the 7 mice that have a 50% weight, it is 8.05, above their 100% weight of 3.25.
- **Mislabelled column (B5):** it now says it holds a Kruskal-Wallis corrected p.
- **Survival curve (B6):** mice that never reach proficiency are now censored with the same day count as the others. The proportion counted without the proficiency day moves from 0.741 to 0.749.
- **Session-end status False (B7):** a variant recomputes these sessions too, giving 5,734 of 6,539 (88%). The outcome is the same.
- **Days against sessions in P2 (B8):** 10 days with more than one full-task session fall in 7 mice, which bounds the effect.

The notes, deviations, findings, notebook conclusions, summary and README are updated to match. The `verifications` entry covers all 39 claims.

**Not done:**
- **Random Forest at full size:** the full 2000 subsamples would take about 2 hours even on 4 cores, and the notebook limit is 30 minutes. The record lists the 50-subsample run as a deviation.
- **Untracked files:** `git status` shows untracked dotfiles and a `scripts` entry at the repository root. They are `/dev/null` character devices from the sandbox, not files I made, so I left them alone.
