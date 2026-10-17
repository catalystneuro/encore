# Round 3 verification: doi:10.1038/s41586-025-09235-0 on DANDI 000409 (0.260309.1324)

I took the counts from the files themselves. The claims file has 30 claims. The attempt record gives 17 reproduced, 4 partially reproduced, 2 not reproduced and 7 blocked. Only one claim has a `proposed` entry on its outcome: behav-zero-contrast. I did not download the paper, because this check needs only the notebook outputs, the helper module and the claims file.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| behav-zero-contrast | not reproduced | Yes | — | See below. |

**How the numbers are built (cells 2 and 48):** Cell 48 takes each mouse's mean of `correct` over its trials with `contrast == 0`, pooled over that mouse's sessions. It then runs `stats.ttest_1samp` against 50 with 138 degrees of freedom, as the criterion asks.
- `correct` is `is_mouse_rewarded` from the trials table and `contrast` is `gabor_stimulus_contrast / 100` (`bwm.task_table`, called in cell 2).
- Reading (b) uses the same `analysed` mask as the rest of the notebook.
- No choice in this analysis was tuned toward the result: both readings the criterion names are shown, plus the 454-session variant.

**Readings against the tolerances (cell 48):**

| Reading | Mean over mice | Within 58.7 ± 0.4 | t138 | Within 20.18 ± 2.02 |
|---|---|---|---|---|
| (a) all trials | 58.26% | No (0.44 below) | 19.68 | Yes |
| (b) analysed trials | 59.29% | No | 16.21 | No |
| (a) on the 454 canonical sessions | 58.27% | No | 19.68 | Yes |
| (b) on the 454 canonical sessions | 59.31% | No | 16.23 | No |

No reading puts both values within tolerance.

**How the criterion applies:** The criterion says only "Reproduced when both values are within tolerance under one reading" and gives no partial case. Other criteria in the claims file name their partial case explicitly, for example at lines 156, 240, 248, 274 and 283. Read as written, this criterion leaves not reproduced as the only outcome once the reproduced condition fails. Cell 49 now states this too.
