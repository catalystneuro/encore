I've revised the attempt for round 2 and re-run the entry with `python tools/entry.py all entries/alonso-2020`. All three notebooks pass (32.5, 57.9 and 23.5 min) and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes:** no recorded outcome changed. The spot-checked numbers came out the same in the new run.
- **fig6s1-crash-mechanisms:** the verified "not reproduced" stays, with a `proposed` change to blocked (`data_missing`) for round 3. The seven models present give 5 distinct patterns, and the missing Q8FBN1 could add a sixth, so "partially reproduced" is still possible. Cell 53 now prints this ("at most 6 distinct among 8; partial possible, reproduced not").
- **fig7-high-temperature-slow-timescales:** stays blocked. Its notes now say the outcome can be at best partially reproduced.

**Corrected or added:**
- **Stale timings:** removed from ramps cells 13 and 17 and main cell 28; those conclusions now point to the estimate printed in ramps cell 12. This run printed 39 simulated seconds per second, 117 min for the fig8 second reading and 59 min for the figs3 up legs. The record's notes quote these numbers, and the two round-1 responses now give the numbers that were printed at the time.
- **deposit-models:** cell 14 now prints the duty-cycle means, and `measured` is 0.193 and 0.234.
- **fig2:** the outcome is kept and still marked assumed. The verifier's concern (more spikes at 25 C could raise the edge with no change in threshold) is now in the notes, in voltage cell 6 and in the README table.
- **README:** the Java agreement is given at 18 and 25 C, the "four other spellings" wording is fixed (3 renamed, 1 unreadable character), and fig6s1's proposed change is noted. Finding 2 and main cell 6 (21 models, not 25) are fixed the same way.
- **Round-2 record:** all 23 claims are filed under `verifications` with the verifier's reasons and my responses. No finding is rated critical, so no `findings` list is needed for the round.
- **Questions file:** nothing added; the verifier found no misreading of the paper in the claims file.

**Not done:**
- **figs3 main reading (the ramp):** still not run. I wrote a separate notebook for the first 28 models and ran it once while preparing; all 378 pairs differed at p < 0.05. I then lost about 40 minutes when an entry run I had started in the background died as soon as the command returned. After that, a run including the new notebook (about 145 min) no longer fit in the time left or in one foreground command (120 min at most). I removed the notebook, and its result is not used anywhere.
- **fig8-up-down-ramps second reading:** not run (117 min estimated). It stays blocked (`too_large`), which the verifier accepted.
- **Run times in `README.md` and `entry.yaml`:** they read about 30, 50 and 20 min against 32.5, 57.9 and 23.5 printed. Changing them would have meant another full run, which there was no time for.
- **Ramps notebook near the limit:** it took 57.9 of its 60 allowed minutes, so a slower machine could push it over and fail the run.
