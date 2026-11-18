The reader answered one question, and it changes the unit of one test without changing any outcome. The entry is locked, checked and run: the check found 0 errors and the notebook passed in 652 s. The handover is in `executed/zhai-2025/handover/`. Nothing is committed or pushed, and I did not verify my own work.

**The question (fig5f-ach-off-elevated):** should the test of the single-pulse normalised area use the paper's units, regions (ROIs), in place of "one region per mouse"?

- **Answer:** yes, amended. The paper's n for Figure 5F counts regions: 13 unlesioned regions from 3 mice and 11 off-state regions from 5 mice, per the legend and the Methods' "The stated n indicates ... the number of ROIs". The reader added the same "one value per region (ROI)" wording to the criterion of fig5f-ach-off-like-6ohda.
- **Changes I made:**
  - In the notebook, the fig5f-ach-off-elevated section now runs the per-region test as the main result. The earlier per-mouse test (the mean of each mouse's regions) is kept as a variant.
  - I rewrote that claim's criterion text and conclusion, updated the criterion text for fig5f-ach-off-like-6ohda, and removed the summary line that called the per-region test a variant.
  - In `attempts/zhai-2025-02.yaml`, I removed the deviation that read "one region per mouse" as "one value per mouse". Both claims' notes now say what the answer changed.

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| fig5f-ach-off-elevated | reproduced, tested per mouse: 0.388 (5 mice) against 0.131 (3 mice), P = 0.036 | reproduced, tested per region: off-state 0.406 (11) against unlesioned 0.111 (13), U = 1, P = 5.0e-05 (paper P < 0.0001) |
| fig5f-ach-off-like-6ohda | reproduced, P = 0.22 (paper P = 0.4679) | reproduced, unchanged: it was already tested per region, 10 against 11 |

For fig5f-ach-off-elevated, the other ways of computing the signal give the same outcome. Taking Fmin from the TTX trial only gives P = 8.2e-05, and using the whole frame gives P = 5.0e-05. The per-mouse variant still gives P = 0.036 under all three.

The numbers in the re-executed notebook match the updated conclusions and record notes.
