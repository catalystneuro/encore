No outcomes changed. All 31 claims stay `blocked`, `too_large`, which the round-2 verifier agreed with, so there is nothing under `proposed`. The final run of `python tools/entry.py all entries/000943-clark-2024` passed with 0 errors, and `check` passes. Nothing is committed.

**Outputs added to the notebook (the verifier asked for evidence behind these sentences):**
- **Cell 8:** now prints the position range of the 326 sessions on the 200 cm track (0 to 200.0 cm). Cell 9 cites it.
- **Cell 12:** now prints each column's smallest session minimum (column 6 starts at 33.4) and the largest gaps between where the position series and the raw signal end (451.9 s longer, 178.2 s shorter).
- **Cell 21:** now also scales the 638 GB by the paper's 215 of the 239 paired sessions, which gives 574 GB and 2.1 h to read. That is still over the 60-minute limit.

**Numbers updated to the final run:** 76.4 MB/s, 2.3 h for the 638 GB and 3.6 h for all 976 GB. The rate moves by a few percent between runs; the round-2 notebook had 72.4 MB/s. The outcome notes and responses use these printed figures in place of the rounded "73 MB/s". They also say "recording days of 239 sessions, a superset of the paper's 215" where they used to say "239 days".

**Wording corrected:**
- **"About 70 cm" for M1 and M2:** cell 13, the summary, the notes and the round-1 response now say that 18 of M1's 41 and 20 of M2's 21 open arena sessions span 67.5 to 89.8 cm. The other sessions span 88.0 to 103.7 cm.
- **Session counts:** the summary now says the counts differ from the paper's table for five of nine mice, four of them by more than 10%. The selection finding now names M13 (27 against 25).
- **The 26.5 GB pickle:** no output and no passage of the paper supports it, so I removed it from the findings, the README and the summary. They now say only that the paper's data are at Edinburgh DataShare, as the paper's data availability statement says.
- **README:** it now says the 638 GB covers more sessions than the paper used, and gives the scaled 2.1 h.
- **Findings:** the quoted position description keeps its colons. I quoted that YAML scalar so it stays valid.
- **Round-1 record:** the `reviewed` field now says the verifier found no misreading "that affects these blocks", and the responses give the 72.4 MB/s printed at the time.

**Round 2 recorded** under `verifications`: all 31 claims agreed and blocked, with the verifier's reasons in its own words. The supp1 claim also carries its five-mice point. The `response` fields and the `reviewed` text say what changed.

**Not done:**
- **The round-1 reasons** stay in the verifier's words. They cite the old cell numbers (6, 8 and 19); the `reviewed` field explains that these are now cells 8, 10 and 21.
- **No timed spike sort was run**, because reading the data alone already takes longer than the limit.
- **The protocol's 60-minute limit:** the verifier noted that `docs/protocol.md` is not among its materials, so it could only check the quoted text. I can't fix that from the entry.
- **The questions file:** I added nothing to `questions/000943.yaml`, because the verifier found no place where the claims file misreads the paper.
