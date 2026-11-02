Both claims touched by the answer are re-run, the entry passes its checks and runs cleanly, and the handover is built in `executed/000715-yemini-2021/handover/`. Nothing is committed or pushed, and I did not verify my own work.

## The question and what the answer changed

**Question (ms2-neuropal-color-violations):** should the code's measure (the mean shortfall below the margin, from `find_optimal_colors.m`) decide the claim, instead of the Methods measure (the share of neighboring pairs below the margin)? The paper's own inputs give 3.5% only under the code's measure.

**Answer:** the reader amended the claim. The code's mean shortfall now decides it, and the Methods share is kept as a variant. The statement now reads "theoretical color margin violation of 3.5%". fig7de-optimal-coloring-violations now uses the same measure. Expected values and tolerances are unchanged.

## Outcome per affected claim

| Claim | Earlier outcome | Now |
|---|---|---|
| ms2-neuropal-color-violations | not_reproduced (Methods share 21.50%) | **reproduced**: 3.64% on the dandiset's head atlas, inside 3.5 ± 0.35. Atlas variants give 3.62 to 3.66%, and the paper's own data.mat inputs give 3.47%. The share, now a variant, is still 21.50%. |
| fig7de-optimal-coloring-violations | blocked, `not_runnable` (reporter table unreadable without MATLAB) | **partially_reproduced**: 39-reporter case 1.72% (expected 1.7 ± 0.17, matches). 3-reporter case 6.95% (expected 10.5 ± 1.05, below the range, so a better coloring than the paper's). |

### fig7de in more detail
- **Why it could run this time:** the measure change alone would not have unblocked it. The `mat-io` package reads the MATLAB table that holds the reporters, so I ported `optimal_color_solver.m` to Python. It is in `neuropal.py`, and the claim has a new notebook, `optimal_coloring.ipynb`, which takes about 19 minutes.
- **Data check:** over the paper's 235 neurons the table gives 654 distinct reporters, which matches the 654 unique reporters the paper reports.
- **First value:** the best of 10,000 runs at sparsity 100 is 1.72%. The best run that keeps exactly 39 reporters gives 1.86%, also inside the range.
- **Second value:** the best of the 7,500 runs at sparsity 1500 that keep 3 reporters (7,106 runs) is 6.95%. Fewer runs would land in the range: the best of 10 runs falls within tolerance in 95% of random subsets, of 100 runs in 66%, and of 1,000 runs in 1%.
- **Reference:** on the paper's own adjacency from data.mat, 2,000 runs each give 1.74% and 8.71%.
- **New question for a reader** (in `questions/000715.yaml`): the paper's 7,500 simulations span 2 to 6 colors, 1 to 3 intensities and 2 to 71 reporters (Methods S2 Figure 6 legend). Its 3-reporter value may therefore be the best of far fewer runs than the 7,500 the criterion assumes. If so, the second value would probably be reproduced.
- **New finding for the paper's authors** (`methods_unavailable`): which sparsity, and how many runs of the 3-reporter setting, produced the 10.5% solution.

## Other changes
- **Main notebook:** the ms2 section quotes the amended statement, lists the code's measure first, and has a new conclusion. The header and summary point to the new notebook for fig7de.
- **Record:** each claim's notes say what the answer changed. `mat-io` was added to `requirements.in` and the lock file. `entry.yaml`, the README and the record's inputs list the new notebook and the reporter table.
- **Runs:** `lock`, `check` and `all` pass. The notebooks took 666 s, 118 s and 1132 s. Two full runs of the new notebook gave identical numbers.
