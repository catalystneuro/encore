One outcome changed and no proposals remain open.

**Changed:** `behav-zero-contrast` went from `partially_reproduced` to `not_reproduced`. The round-3 verifier agreed with this proposal. The criterion defines only the reproduced case, and no reading puts both values within tolerance: the best is 58.26% with t138 = 19.68, against 58.7 ± 0.4 and 20.18 ± 2.02. I removed `proposed` and also dropped the deviation entry, which only explained the old partial outcome. The notes now say that no reading meets the criterion and that mice are still well above chance.

**Proposals still standing:** none. This was the only one.

**Other updates:**
- **Notebook:** the conclusion in cell 49 and the summary table now say "not reproduced".
- **README:** the claims table row is updated. The run time now reads 25.0 minutes, from this run.
- **Attempt record:** I added round 3 under `verifications`, with one result for `behav-zero-contrast`: agrees true, outcome `not_reproduced`, the verifier's reason, and my response. The `wheel-speed-decoding` notes now give this run's decoding estimate of about 41 minutes (30 in the previous run).

**Re-run:** `python tools/entry.py all entries/000409-ibl-2025` reported 0 errors and the notebook passed in 1513 s. The values in cell 48 are unchanged. I left the work uncommitted, as instructed.
