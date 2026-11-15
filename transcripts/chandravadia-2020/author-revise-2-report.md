I've revised the attempt for round 2. No outcome changed, and none needed a `proposed` change: the verifier agreed with all 25, so it stays at 10 reproduced, 10 partially reproduced, 4 not reproduced and 1 blocked. `python tools/entry.py all entries/chandravadia-2020` passed with 0 errors and the notebook ran in 225 s. Every number already in the notebook came out the same. The record now has the round-2 verification for all 25 claims, with the verifier's reasons in its own words and my response to each.

**Corrections and added outputs**
- **ttl-codes:** The notebook now prints the event sequence of every failing trial, file by file. This confirms the verifier's point and shows the details:
  - 19 of the 30 failing trials have an extra 3 before the 2: 6 of 7 in T88_2001, 9 of 10 in T88_2002 and 4 of 7 in T90_2003.
  - The other failing trials in those files have an unlisted 22 or 23 after the response.
  - I corrected the conclusion, the notes and the data finding to match.
- **ttl-codes, other way of cutting trials:** The notebook now also cuts trials at their start and stop times, which before was only described in the record. That cut gives 75 of 87 files in order, against 78. So "most files" holds either way, and the deviation now says so instead of claiming the notebook doesn't show it.
- **fig5f-site-proportions:** I removed the unsupported "equal to the figure's values to the second decimal". The notes now list the six values next to the figure's.
- **session-dates:** The H44_68 sentence now gives the span of all the Huntington files (2006 to 2016) and, separately, the dates of the nearest H sessions, H43_56 (2013) and H47_92 (2014). I checked those dates in the files.
- **README run time:** It said "about 6 minutes". It now says 4 to 9 minutes, since the last two runs took 3.6 and 8.3 minutes depending on streaming speed.
- **Assumptions:** The verifier said two choices could be flagged as assumptions, so I marked both `assumed: true`:
  - units-table: the deviation now says the column test fails without reading IsolationDist as IsolDist.
  - ttl-codes: how trials are cut from the event stream.

**Not done**
- The fig5f question about the claims file possibly misreading the paper was already in `questions/chandravadia-2020.yaml` from round 1. I left it and the claim as they are, for a reader to answer.
- The verifier couldn't see the published code, so its line-102 citation for the bootstrap mode is still unchecked by the verifier. The verifier said this doesn't affect the outcome.
- I changed nothing in the summary line "the per-site percentages of Figure 5f are matched". All six values are within tolerance, which supports it.

Nothing is committed, as instructed.
