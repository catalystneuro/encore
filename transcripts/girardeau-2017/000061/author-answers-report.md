All three answers are applied. One outcome went from blocked to reproduced, one to partially reproduced and one to not reproduced. The other three claims affected keep their outcomes.

The re-run notebook passed in a clean environment (454 s). The numbers in the conclusions match the executed outputs, and the handover is built in `executed/000061-girardeau-2017/handover/`. `entry.py check` still reports 29 errors. All of them are in the deprecated `-01` attempt record, which is checked against the rewritten claims file. The earlier author run hit the same errors, and I left that record as it was. Because `all` stops on those errors, I ran the notebook with `entry.py run`. The `-02` record, the notebook and the entry have no errors. Nothing is committed or pushed.

**Question 1: laps under O1 (`habituation-over-days`)**
The answer is that the claim is judged on reading c alone, laps between rewards at opposite ends, when the dataset has neither lap intervals nor position. That is what the attempt already did, so I only updated the notes and deviations.

| Claim | Before | Now |
|---|---|---|
| `habituation-over-days` | reproduced | reproduced (pooled rho 0.383, p = 0.015; air puff laps p = 0.046) |

**Question 2: which cells count under O4**
The answer is that the claims are judged on the identified cells alone (reading a). Reading b is not needed. The notes now say that the 152 excitatory and 36 inhibitory cells come from one rat, against the paper's four.

| Claim | Before | Now |
|---|---|---|
| `bla-pyr-sleep-firing-increase` | reproduced | reproduced (REM p = 7.0e-15, NREM p = 7.2e-12) |
| `bla-int-sleep-firing` | not reproduced | not reproduced (REM/wake p = 0.020, NREM p = 0.26) |

**Question 3: all-cell tests that depended on blocked claims**
The answer is that the dependencies were on method only, so they were removed. These claims are now judged on their all-cell tests. The pyramidal parts still cannot be run, because the dandiset has no putative cell types.

| Claim | Before | Now |
|---|---|---|
| `reactivation-peaks-at-ripples` | blocked (metadata insufficient) | partially reproduced: 11 of 15 sessions, one-tailed p = 0.0042; the pyramidal part is not tested |
| `direction-all-cell-pairs` | blocked (metadata insufficient) | reproduced: air puff p = 0.01, safe p = 0.0043, air puff against safe p = 0.48, over 14 sessions |
| `ripple-modulated-cells-larger-reactivation` | blocked (metadata insufficient) | not reproduced: rank sum p = 0.27 (O2 reading a) and 0.3 (reading b), over 12 sessions |

Two caveats on these:
- **`direction-all-cell-pairs`:** the air puff result rests mostly on Rat08 (7 of 8 sessions), with 2 of 3 in Rat10 and 1 of 3 in Rat11.
- **`ripple-modulated-cells-larger-reactivation`:** the modulated mean of 4.18% is below the expected 6.07 ± 1.3%. The non-modulated mean of 1.68% is within its expected range.

**What changed in the files**
- **Notebook:**
  - The header, the three claim sections and the summary are updated.
  - I added per-rat breakdowns, the expected values and a count of the sessions that enter the ripple-modulated test (12 of 23).
  - I removed stray bold markers at the end of three Result lines.
- **Attempt record:** each affected claim's notes say what the answer changed and give the earlier outcome. The finding's count of blocked claims is now 18 (it was 21).
- **README:** the tally is now 10 tested (6 reproduced, 1 partially reproduced, 3 not reproduced) and 22 blocked. The run time is updated.
