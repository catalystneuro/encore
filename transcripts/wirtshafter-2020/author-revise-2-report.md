No outcomes changed. `units-recorded` stays partially reproduced and the other 30 claims stay blocked (data missing). The verifier agreed with all 31 and nothing called for a proposed change. The final run of `python tools/entry.py all entries/wirtshafter-2020` passed in 243 s, and `check` reports 0 errors.

**What I corrected, with the new output behind each fix:**
- **Spike gaps (point 2.1):** the notebook now prints the silence before the first spike and after the last spike of each recording. The first spike comes within 0.09 h of every recording's start, but up to 27 h of silence can follow the last spike. Cell 14, finding 4, the summary and the README now say only that no recording has a silent minute between its first and last spike. In rats 7, 8 and 9 the spikes span 0.5 to 0.9 h, which may be the session. In rat 6 they span up to 4.9 h, and in rats 10 and 12 the whole recording. The notebook now names the rat 7 recording left out of the check (2017-08-02, which holds only copies), so 45 of 46 recordings are covered.
- **"31 findings" (2.2):** now reads "beyond the counts of units recorded (30 of 31 claims, and two of the four counts of the first)".
- **Rat 6 tetrode 26 (2.3):** a new table gives each of the 14 recordings with its cluster count. The largest cluster holds at least 99.6% of the spikes of every other cluster on the tetrode, 47 of 47. The wording now says exactly that.
- **Shifted-train control (2.4):** it is now printed for the 24 cross-tetrode pairs on their own (median 0.5%, at most 1.3%). Finding 3 uses these figures.
- **Gap range (2.5):** the shortest of the 25 long intervals is now printed. The range is corrected from 8.7–93 ms to 4.9–93 ms.
- **"After the end" (2.6):** the spikes outside a recording are now split by side: 0 before its start, 5403 after its end.
- **Longest silence (2.7):** the notebook now names the recording for each rat's longest stretch (rat 6, 2017-05-01, starting at 6626 s).
- **Code repository (2.8):** I read the variables of all 51 `.mat` files. They are all library examples. Only three of the 177 files that could hold data reach the 432,000 bytes one session of tracking would take, and those three are the chronux spike-sorting samples (one `spikes` struct each). The six files under `hannah-in-use/include/` are at most 4 kB.
- **410 distinct trains:** the notebook now prints 395 LS clusters once the 14 tetrode-26 clusters that hold the others' spikes and the MUA9 cluster are also dropped, which is outside the tolerance of 45. The result cell, the record notes and the summary now say that 410 is within tolerance only when exact copies alone are discounted. The outcome still rests on the 452 deposited clusters, which match the paper exactly.

**Other changes:**
- Round 2 is recorded under `verifications`, with the verifier's reasons in its own words and my replies under `response`.
- The `inputs` entry now covers reading the `.mat` variables from the code repository.
- The runtime is now given as 6 minutes in `entry.yaml` and the README.

**Not done:** I added nothing to `questions/wirtshafter-2020.yaml`, because the verifier found no place where the claims file misreads the paper. Nothing is committed, since the workflow commits the changes.
