No outcome changed: the record still has 12 blocked, 12 reproduced and 3 partially reproduced, and the verifier agreed with all 27 in round 2. I re-ran the entry with `python tools/entry.py all entries/wakhloo-2026`. The notebook passed in 32.4 min, it gives the same numbers as the run the verifier read, and the entry checks report 0 errors. Nothing has been committed.

**Possible misreading, sent to a reader.** The verifier noted that the claims file takes the CA1 task-relevant dimension on sets of 19 units, as the paper's code does. The Methods point to 24 CA1 units, the count they use for the other geometric measures. I added this as a question in `questions/wakhloo-2026.yaml`, with the numbers under both unit counts. It decides one outcome, late-trends-match-optimal: with 24-unit sets the CA1 slope is +0.0130 (P = 0.86), which passes the criterion's sign test, so the claim would be reproduced instead of partially reproduced. I wrote no `proposed` change, because the verifier agreed with the outcome under the claims file as it stands. That claim's notes now say plainly that the sign test passes with 24 units. Four other claims use the same unit count, and their outcomes are the same either way.

**Corrections:**
- **Result text in the notebook (cell 25):** the mean-difference comparison is now like for like. PFC is 11.55% here and 11.55% in the paper's file; CA1 with 19 units is 8.91% here and 9.04% there.
- **README run time:** it now says 17 to 33 minutes, depending on the machine. The verifier's run printed 17.0 min and this run 32.4 min.
- **GLM fit comparison (glm-cross-validated-d2):** the largest difference from the paper's own fits changes a little between runs. The notes now give both runs: 2.7e-10 and 1.8e-09 in this run, 9.3e-11 and 2.3e-09 in the verifier's. The round-1 response now says "below 3e-09".
- **Round-1 summary:** it said "two blocked pairs" had a different blocked reason; that is now "five claims".
- **Session-length finding:** "most 15 to 16 minutes" is now "median 15.85; 36 of the 64 between 15.0 and 16.0", counted from the table the notebook prints.

**Added:**
- **The missing round-1 point:** the empirical errors are likely optimistic, because training and test bins are drawn from 500 ms bins that are correlated in time, as in the paper's code. This is now in the notes of svc-hebbian-correlation, fig7e and fig7f, and in the fig7f result text.
- **Round-2 record:** each of the 27 claims has the verifier's agreement, its outcome, its reason as the report gives it, and my response. The `reviewed` text lists the corrections that are not tied to a claim.

**Not done:** the CA1 unit-count question stays unanswered until a reader takes it up in a separate run. The SVC still runs on 4 of the 500 subsets per session; the verifier did not ask for more.
