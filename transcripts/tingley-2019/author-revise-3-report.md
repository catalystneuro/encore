One outcome changed and no proposals are left open.

**Changed:**
- **fig5d-lag** went from partially reproduced to not reproduced. The verifier agreed with the proposal. The coupling part of the criterion holds: the correlogram peaks at 0 ms, 166.3 SD above its flanks. The lag part fails: it is 0.00 ms under both readings, and 0.00 or 0.80 ms on the re-referenced channel, all outside 2.2 to 10.6 ms. The criterion defines no partial outcome, so the claim is not reproduced. I removed `proposed` from this claim.

**Still standing:** nothing. fig5d-lag was the only proposal, and no other outcome changed.

**Files updated:**
- In the attempt record, I rewrote the end of the fig5d-lag notes and added round 3 under `verifications`. It has one result for fig5d-lag: the verifier agreed and gave not reproduced. The record has its reason in its own words and my response.
- In the notebook, the cell 61 conclusion and the summary table now say not reproduced.
- The entry README table row now says not reproduced.

`python tools/entry.py all entries/000218-tingley-2019` finished with 0 errors, and the notebook passed in 1580 s. The re-run prints the same fig5d numbers as before. Nothing is committed or pushed.
