The reader answered the one question, and the claim it changed now tests as reproduced. `python tools/entry.py all entries/mcguire-2016` passes with 0 check errors, and both notebooks run (86 s and 651 s). The handover is built in `executed/mcguire-2016/handover/`. Nothing is committed or pushed, and I did not verify my own work.

**Question (fig2d-fixed-panel-impairs).** I had asked whether the claim should be tested on the paper's S2 Data, because CRCNS ssc-4 holds no fixed-panel trials. The reader changed the claim:
- Its data are now `elsewhere`: the per-rat values behind S2B Fig in S2 Data, with S1 Data supplying the Figure 2D d-prime as a variant.
- Because the paper's own per-rat values are used, the criterion no longer has to tell apart which normal sessions the fixed-panel trials are compared with.
- Both readings for the rat that completed no fixed-panel trials stay: (i) it is left out, (ii) it counts as 0.
- The criterion now asks for a lower fixed-panel value in at least five of the six rats.

| claim | earlier outcome | outcome now |
|---|---|---|
| fig2d-fixed-panel-impairs | blocked (data_missing) | reproduced |

- **Main test (S2B Fig values in S2 Data):** fixed-panel discrimination is lower than moving-panel discrimination in all six rats. The drop runs from 0.067 (18Ri) to 0.374 (107SI).
  - With the rat at 0 kept, the paired t test gives p = 0.0120 (the paper reports 0.012); the mean change is -0.169 (95% CI -0.282 to -0.056).
  - With that rat left out, p = 0.0308; the mean change is -0.174 (95% CI -0.322 to -0.026).
- **Variant (Figure 2D d-prime from S1 Data):** also lower in all six rats, p = 0.0051 and 0.0176 under the two readings.
- **Not testable:** the statement's "all but one rat" means one rat was not significantly impaired. That needs single trials, and the per-rat summaries cannot show it. The smallest drop is 18Ri's.
- **Moving-panel values:** for the six rats in the control, they match neither the Figure 2B means nor the data set's mean or last session. They therefore summarise sessions that are not in ssc-4.
- **New finding (`paper_inconsistency`):** in S1 Data, the Figure 2A sheet is labelled "Rat 107ST", but its values belong to 107Si. Its mean FFF fraction is 0.7485, which is 107Si's Figure 2B mean (107ST's is 0.5856). Its fixed-panel value (0.0991, d-prime 0.277) is 107Si's in S2B and Figure 2D.

**Files changed:**
- In `reproduce_mcguire_2016.ipynb`, the claim's section is rewritten with the new test, both readings, effect sizes, the d-prime variant and the two checks above. The header and summary tables are updated to match.
- In `attempts/mcguire-2016-01.yaml`, the outcome is updated. Its notes say what the answer changed. A deviation, the new finding and the updated input descriptions are added.
- The README and `entry.yaml` now say three claims use the paper's supporting data, not two.
- The lock file did not change.

No other claim was affected.
