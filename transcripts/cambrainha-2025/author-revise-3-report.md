Round 3 is recorded and the entry re-ran cleanly: the notebook passed in 1599 s and `tools/entry.py` found 0 errors. Nothing is committed.

**Outcome changed**
- `figs3-exponents-stable-with-threshold` goes from not reproduced to **partially reproduced**, still marked `assumed: true`, and `proposed` is removed. The verifier agreed on condition that it stays marked as assumed, because the outcome rests on CV (a) and on starting the grid at 7.
  - From 7 to 12, only NNI z fails (0.083 against an SD of 0.058). Passive and NNI μ pass only because no grid point has 10 sessions, so the condition holds vacuously.
  - The notes now state the verifier's two caveats. Passive and NNI μ are not actually tested, since only 1.7% of windows pass the r² rule. The NNI z failure is narrow and depends only on the SD at the start of the grid.
  - The deviations now apply the criterion as written.
  - The re-run printed the same verdicts as before. Starting at 7 or the 99th percentile gives partially reproduced; starting at the 99.9th percentile or using CV (b) gives reproduced.
  - In those reproduced cases, active μ also has no point with 10 sessions, so μ is vacuous in every phase there.

**Proposals still standing:** none. This was the only proposal.

**Other updates**
- In the notebook, the "How readings decide" section, the result cell for this claim and the summary table now match the new outcome.
- The verdict printed in the cell tagged for this claim (cell 81) still uses the old rule, under which an exponent with no evaluable point fails. The literal verdict is in the next cell. I left the code alone because the verifier reviewed those cells as they are; the result text explains which column is which.
- The README table and paragraph are updated.
- Round 3 is added under `verifications` in the attempt record: agreed, partially reproduced, the verifier's reason and my response.
