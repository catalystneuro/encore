One outcome changed and no proposals remain.

- **traj-diverge** is now blocked (data_missing). It was partially reproduced. The verifier agreed with the proposed change: the x1 difference begins where the path turns back in x, so it says nothing about a sideways separation, and the dandiset has no y coordinate. I removed `proposed` and rewrote the notes. The notes now also say that whether the paths overlap in the central arm can't be judged from x1 either.
- No other outcomes changed.

I updated the attempt record, the notebook's header table, the traj-diverge conclusion, the summary table and text, and the entry README to show blocked. Round 3 is recorded under `verifications` with one result for traj-diverge: agreed, outcome blocked, the verifier's reason in its own words, and my response.

`python tools/entry.py all entries/000067-fujisawa-2008` reported 0 errors, and the notebook passed in 922 s. Nothing is committed.
