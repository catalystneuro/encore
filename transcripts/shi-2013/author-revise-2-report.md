Round 2 is done. No outcome changed, and none needs a `proposed` change. The verifier agreed with all 28 outcomes (7 reproduced, 5 partially reproduced, 13 not reproduced, 3 blocked). The entry re-ran cleanly with `python tools/entry.py all entries/shi-2013` (0 check errors, notebook passes in 330 s), and the numbers are the same as before.

**Wording the outputs did not support, now corrected in the notebook and the attempt record:**
- **Cell 10 and the movement-epoch-tuning deviation:** the event-timing ranges are now labelled as 5th to 95th percentiles, with the full minimum to maximum given beside them. "Code 10 follows by 320 ms on every trial" now says a median of 320 ms, range 0.22 to 0.42 s.
- **Cell 112 (longer hold):** I removed the per-session sentence. Cell 111 now lists the sessions whose shortest interval is below their first field 11 value. The re-run shows they are exactly the 3 sessions whose field 11 changes within the session, and their shortest interval falls on a trial with a lower field 11.
- **Cell 93 and notes (decoding V better than NV):** with all units and populations of 200 cells, the paired test over targets also finds the difference (P = 0.036).
- **Cell 68:** now gives reading (b)'s own values (78.4, 70.0, 75.0, 75.0%) in place of "gives the same".
- **Cell 59 and notes (400 ms subepochs):** now say the first-400 ms position percentage, 35.7%, is outside tolerance. The last-400 ms one is within.
- **Cell 76 and notes (INDX2):** now also give the all-units reading (c) result (−2.0, −14.1, −9.9%), where only Vision Only is within tolerance.

**Other changes:**
- **fig6-decoding-vv:** I removed `assumed: true`, as the verifier said. The outcome holds under both code mappings and with all units. The deviation and cell 91 now say so.
- **Eye position (cell 106 and notes):** they now say the block partly rests on a reading of the analog-file layout that is known to be partly wrong. They also say that if fields 22 and 23 were eye position, reading (a) would fail the claim (Levene's test P = 0.012 at 90°, vertical).
- **Point B8 (t-test over bootstrap accuracies):** I kept this test, because it is reading (b) of the claims file's criterion. Cell 93 and the notes now say it treats the resamples as independent, so its P value depends on how many are drawn. It decides no outcome.
- **Round-2 record:** added under `verifications` for all 28 claims, with the verifier's reasons from its report and my changes under `response`.

**Not done, and why:** the remaining points the verifier listed cannot be settled from the data set. These are the 359 sessions against the paper's 219, what fields 19 to 21 mean, the V = code 4 mapping, the clock check in sessions with no tuned unit, and the analog-file layout. They stay as stated findings and flagged assumptions. The possible misreading of the claims file (point B6) was already in `questions/shi-2013.yaml`, so I added no new question. I did not commit, as instructed.

The tool files that were already modified, and the untracked placeholder files at the repository root (such as `.bashrc` and `scripts`, created at 21:28 before this run started), are not mine and I left them alone.
