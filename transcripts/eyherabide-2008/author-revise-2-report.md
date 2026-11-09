No outcome changed in this round, as round 2 requires. I re-ran the entry twice with `python tools/entry.py all entries/crcns-ia-1-eyherabide-2008`; each run passed with 0 check errors in about 9 minutes, and the numbers are the same as before apart from the new outputs below.

**Outcomes**
- **table1-bursting-sessions:** stays `partially_reproduced`, with a change to `not_reproduced` recorded under `proposed` for round 3. I accept the verifier's argument. Selection (c) was chosen partly because it makes these counts close to Table 1, and its off-line exclusion has no basis in the paper. Under selections (a) and (b), which the criterion supports, at most 2 of the 7 counts are within tolerance. The notebook's conclusion cell, cell 7, the Summary and the README now treat (c) as only a variant for the three claims built on Table 1's counts.
- **All other outcomes:** unchanged. The verifier agreed with all 25.

**New outputs the verifier asked for**
- **fig8-latency-decreases:** the latency cell now prints the values that sit on the 0 ms edge of the search: 17 values in 13 of 53 sessions. Without them the mean latencies (τ_1 to τ_4) are 5.80, 4.32, 3.67 and 3.37 ms. Over the 40 sessions with no value on the edge they are 5.77, 4.33, 3.77 and 3.40 ms. Of the 48 sessions with τ_1 to τ_3 off the edge, 32 have τ_1 > τ_2 > τ_3. The latency still falls with n, and the outcome stands. The text now says that "no negative τ_n" holds by construction.
- **fig9c-population-nbta:** the cell now prints which cell each session comes from. The 7 sessions of selection (c) come from 7 distinct cells; 03-04-23-aa and 03-04-23-ah are different cells recorded on the same date.
- **Dataset check (cell 6):** it now names the one session whose spike-triggered average peaks at 0 ms (03-03-06-aa sig2).

**Text corrected**
- **data-sessions-and-trials:** selection (c) comes from 29 cells on 18 dates, outside the paper's 37 cells and 23 animals. Those two counts match only over all seven-protocol sessions, and the text now says so.
- **fig7ab:** in the cell, the notes, the Summary and finding (7), "the rise is estimator bias" now reads "the bias is of the order of the rise".
- **Summary:** the population bullet now says selection (c) is the main population from firing-rate-uniform on. The bullet on the spike-triggered average no longer says "in every session".
- **firing-rate-uniform, table1-isolated-spikes, table1-burst-length:** each selection deviation now says the outcome is the same under every population shown, so it does not rest on the assumption.
- **Round-1 record:** the fig8-nbta-differ reason now includes the verifier's label that problem 7 does not affect a conclusion.

**Recorded:** the round-2 `verifications` entry covers all 26 claims, with the verifier's agreement, outcome and reason in its own words, and my response to each.

**Not done:** I added no question to `questions/crcns-ia-1.yaml`, because the verifier found no place where the claims file misreads the paper. Nothing was committed.
