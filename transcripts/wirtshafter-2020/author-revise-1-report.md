I've worked through the round-1 report and re-run the entry with `python tools/entry.py all entries/wirtshafter-2020`. It passes the checks (0 errors) and the notebook runs in about 4 to 5 minutes. Nothing is committed.

**What changed in the outcomes**
- **`units-recorded`**: changed from blocked to partially_reproduced, which is the outcome the verifier gave. Two of the four counts are tested and match the paper exactly: 452 LS and 178 CA1 units. The LS count stays within tolerance (410) when duplicate trains are dropped. The other two counts, 165 CA1 and 378 LS cells meeting the rate and coverage criteria, need the animal's position and speed, so they stay untested (data_missing). I updated the notebook's header, result and summary, the README and `entry.yaml` to match, and added the required sentence that a failure here may be a failure of this attempt.
- **The other 30 claims**: unchanged, all blocked (data_missing). The verifier agreed with each of them. The three that depend on `units-recorded` now say that what is untested is its counts of cells meeting the criteria.

**What I added or corrected**
- **Paper's code repository**: the notebook now lists every file at commit 5c6320a9 with its size: 4890 files, 35.4 MB. The largest data-like files are library sample data under 1 MB each, and no tracking file is there. This listing is now recorded under `inputs`.
- **Times.mat read in full**: every sample interval of all 57 recordings is now checked. No recording changes its sampling rate or has a gap of 0.1 s. The only odd intervals are in the six rat 6 recordings sampled at 3.2 ms: 25 short gaps of 8.7 to 93 ms, and repeated timestamps on 2017-04-21 (1121 of them) and 2017-04-26 (3280). I updated the Times.mat finding to say this.
- **Looking for the 30 min maze session**: no recording has a stretch of 60 s or more without a spike; the longest is 38 s. So neither the time files nor the spikes mark where the maze session is.
- **Duplicate-search helpers**: I ran them on made-up spike trains with known answers, and they give the expected results.
- **Check that was circular**: the table of what each claim needs no longer fills in a default. It prints any claims without an entry and any entries for no claim; both lists are empty.
- **CA1 from only two rats**: the notebook now says that rats 10 and 12 give 184 of the 452 LS clusters. Any CA1 versus LS comparison over all units would therefore compare two rats with six.
- **Corrected count**: the summary said the copied rat 7 trains were spread over 18 recordings; it now says 16 of 19.
- **`verifications`**: round 1 is recorded for all 31 claims, with the verifier's reasons in its own words and my changes under `response`.

**What I did not do**
- I added nothing to `questions/wirtshafter-2020.yaml`, because the verifier reported no place where the claims file misreads the paper.
- No claim statement, expected value or criterion was changed.
- Problems 2 and 3 in the report do not affect any conclusion, and the notebook already stated them, so they needed no change.
