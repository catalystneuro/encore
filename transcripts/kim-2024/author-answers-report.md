There was one question, and its answer changed one claim and added another. I re-ran both on the amended claims file and updated the notebook, conclusions, README and attempt record. The entry is locked, `python tools/entry.py all` passed (0 check errors, notebook ran in 187 s), and the handover is built in `executed/001544-kim-2024/handover/`. I haven't verified my own work, and nothing is committed or pushed.

## Question: figs12-other-features-shared

**The question:** should "most other features are shared" be judged on the ten features the Figure S12 legend calls similar, instead of the fourteen the criterion used? Four of those fourteen are features the legend reports as differing.

**The answer:** yes. The reader limited the claim to the legend's ten features (threshold, upstroke, spike amplitude, spike latency, AHP latency, AHP width, CV of ISIs, rheobase, tau, adaptation index). It is still a claim of absence: a one-way ANOVA per feature at alpha 0.05, reproduced when more than half show no difference. The reader moved input resistance, spike width, downstroke and f-I slope into a new claim, `figs12-app-differs-from-all`.

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| figs12-other-features-shared | reproduced, resting on an assumption | reproduced, no longer resting on an assumption |
| figs12-app-differs-from-all (new) | not in the claims file | reproduced, resting on an assumption |

**figs12-other-features-shared**
- **Before:** 9 of 14 features showed no difference on all cells. Without the three `_FL` cells it was 7 of 14, which is not more than half. So the outcome depended on which home-cage cells were used.
- **Now:** 9 of 10 show no difference on all cells, 7 of 10 without `_FL`, and 10 of 10 without the cells whose resistance changed by more than 20%. The mixed model gives the same counts (9, 7, 10).
- The only feature that differs on all cells is AHP latency (p = 0.012). Every cell set gives more than half, so I dropped the assumption flag.

**figs12-app-differs-from-all**
- On all cells, APP differs from home-cage cells in all four features under both test readings:
  - input resistance is higher (p = 0.0089; mixed model 0.022);
  - spike width is shorter (p = 0.00037; 0.00082);
  - downstroke is steeper (p = 0.0015; 0.026);
  - f-I slope is larger (p = 2.8e-05; 0.0012).
- Without the `_FL` cells the result is the same.
- Without the cells whose resistance changed by more than 20%, input resistance no longer differs (p = 0.20 and 0.19). The downstroke then differs only under the cell-level test (mixed model p = 0.11), which would make the claim partially reproduced. So the outcome rests on using all 24 home-cage cells, and is marked as an assumption.

In the record, each claim's notes say what the answer changed. I also updated two findings: the count of untested claims is now 24 of 31, and the question for the paper's authors now gives input resistance as a second result that depends on the cell set.
