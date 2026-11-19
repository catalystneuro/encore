Both questions were answered by the reader amending the claims file. No outcome changed. The answers removed the dependence on which Corners fold is used, which had been one of the assumptions behind fig4b-spike-rate-difference and table1-s40. The entry passed `lock` and `all` (0 errors, notebook ran in 372 s), and `handover` wrote `executed/martinez-conde-2019/handover/`. Nothing is committed or pushed, and I did not verify my own work.

**Question 1, fig4b-spike-rate-difference.** I asked whether reading (a), which averages the two S40 folds, should be dropped, and whether reading (b), "the fold at the ROI centre", should say the bright fold. Neither fold is at the ROI centre. The reader dropped both readings. The criterion now takes the bright S40 fold alone, and the opening comment, fig4a-above-baseline and fig4b-pairwise-significance now say the same.

| Claim | Earlier outcome | Outcome now | What changed |
|---|---|---|---|
| fig4b-spike-rate-difference | partially reproduced (assumed) | partially reproduced (assumed) | The means are S40 26.27, S52 20.30, S90 10.83 and P180 6.47 spikes/s. The order holds, but P180 is outside its tolerance of 1.15 around 4.87. Under the dropped averaging reading, S40 was 19.09 and the order failed. The fold choice is no longer an assumption; the baseline placement still is. |
| fig4a-above-baseline | reproduced (assumed) | reproduced (assumed) | The criterion now names the bright fold, which the attempt already used. The variant with both folds averaged is no longer shown. |
| fig4b-pairwise-significance | reproduced | reproduced | Unchanged: BH p = 0.0015 for S40 against S90, 1.9e-05 for S40 against P180, and 0.00026 for S52 against P180. The both-folds variant is no longer shown. |

**Question 2, table1-s40.** I asked whether the claim should be tested on the bright S40 fold only. The reader dropped readings (i) and (ii), and the criterion now uses the ten blocks along the bright fold.

| Claim | Earlier outcome | Outcome now | What changed |
|---|---|---|---|
| table1-s40 | reproduced (assumed) | reproduced (assumed) | All five values are within the paper's SEM: 10.54, 34.25, 23.01, 23.02 and 26.27 spikes/s. Under the dropped averaging reading at most one of five was. The outcome now rests only on where the Corners baseline squares are placed. |

The amended opening comment also reaches the other claims that use S40: fig5-average-maps, fig6-midpoint-representative, fig7c-fold-edge-equivalence, fig7c-fold-edge-significance and fig7d-nonlinear. Their numbers and outcomes are unchanged. Their deviations no longer list the bright fold as an assumption, and the both-folds variants are gone from the fig5 and fig6 sections.

**Files changed:**
- **Notebook:** the header now describes the questions and answers. The both-folds variants are removed, except as reference lines in the fig4b and Table 1 cells that show what the answer changed. I updated the conclusions and the summary.
- **`vasarely.py`:** the docstrings now say the claims file fixes the bright fold.
- **README:** the assumptions paragraph is updated.
- **Attempt record:** each affected claim's notes now say what the answer changed. I removed the `methods_unavailable` finding that asked the authors about the bright fold, since the claims file now settles it.
