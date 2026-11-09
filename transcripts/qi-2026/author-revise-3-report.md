I made the one change the verifier agreed with, and no proposals stand.

**Outcome changed**
- **voltage-to-spike-sigmoid**: changed from reproduced (resting on an assumption) to blocked, `methods_underspecified`. I removed `proposed` and also dropped `assumed: true`, since the outcome no longer rests on a chosen reading. The readings the criterion names give different results. With V at the spike frame, 262 of 505 cells (52%) pass. With the mean of the 10 ms before, 214 (42%) pass, and with the single sample 10 ms before, 121 (24%); both of those fail.

**Other outcomes**: unchanged. The totals are now 46 tested (35 reproduced, 5 partially reproduced, 6 not reproduced) and 10 blocked. Five outcomes rest on an assumption.

**Text updated to match**
- **Attempt record:** the claim's notes and deviation are rewritten. The `methods_unavailable` finding now attributes the 10 ms to the Results and the Figure 4E legend, not the Methods, and gives all three percentages. Round 3 is recorded under `verifications` with the verifier's agreement, reason and my response. I had first put `blocked_by` in that result too, but the schema does not allow it there, so I took it out; the outcome itself carries it.
- **Notebook (`qi2026_spontaneous.ipynb`):** the Result cell, the Summary row and the header table now say the claim is blocked.
- **Entry README:** the counts, the outcome table and the list of assumed outcomes are updated.

**The CV point from the verifier**: this run printed 4.54 for the spread of the fitted maxima, and the verifier saw 4.56 in its run. The value changes between runs in the second decimal because those fits are poorly constrained, so the text now says "about 4.5 (4.54 and 4.56 in different runs)".

**Run**: `python tools/entry.py all entries/001960-qi-2026` finished with 0 check errors, and all three notebooks passed (29.4, 21.2 and 9.8 minutes). Nothing is committed.
