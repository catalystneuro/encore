One question was answered, and with the amended claim `imaging-cell-counts` goes from `not_reproduced` to `partially_reproduced`: the cells per day now match, and the 78 tracked cells still can't be measured. The lock, check and run passed (0 errors, notebook runs in 40 s). The handover is built in `executed/kennedy-2020/handover/`. I have not verified the work, committed or pushed.

**The question (`imaging-cell-counts`).** I had asked whether the paper's "187.3±8.1 cells imaged per day" means per mouse and day, or summed over the five mice. The reader found that the claims file had misread the unit and amended the claim:
- **New unit:** "cells per day, summed over the 5 mice". The reader's reason is the paper's own counts: 202 rat-responsive cells (Fig 2j), 133 USS-responsive cells (Fig 3e), and 74.4% of neurons responding to at least one stimulus. Those fit about 562 cell-days, not about 2810.
- **Tracked count:** the 78 cells are now a total over the five mice. The clause giving two readings of it is gone.
- **Criterion:** reproduced only when both counts are within tolerance.

**Re-run on the amended claim:**

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| `imaging-cell-counts` | `not_reproduced`, measured 37.47 cells per mouse and day (SEM 3.26) | `partially_reproduced`, measured 187.33 |

- **Cells per day:** summed over the five mice, the three days hold 203, 183 and 176 cells. That is a mean of 187.33 with an SEM over the days of 8.09, inside 187.3 +/- 8.1.
- **Tracked cells:** the files hold no cross-day registration, cell identifiers or footprints, so the count can't be measured. The data only bound it: the smallest day of each mouse sums to 158 cells, and 78 is 42% of the cells per day, the Methods' "roughly half".
- **Why partially reproduced:** the criterion needs both counts and only one could be tested. bennett-2024-01 recorded a claim with an untestable part the same way.

**Updated:**
- **Notebook:** the claim section quotes the amended claim and says how the reader changed it. The test now uses the summed count, with the per-mouse mean printed only for reference. The Result, the summary and the header table are updated.
- **Helper:** the docstring of `vmhdm.cells_per_day` gives the new unit and where it comes from.
- **README:** the outcome row and its prose.
- **Attempt record:** `attempts/kennedy-2020-01.yaml` has the new outcome and measured value. The claim's notes say what the answer changed.

No other claim was affected; the other 38 stay blocked as before.
