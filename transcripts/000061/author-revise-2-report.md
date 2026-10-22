I've made the round-2 revision. **No outcome changed and none is proposed**: 6 reproduced, 1 partially reproduced, 3 not reproduced, 22 blocked. The verifier agreed with all 32 outcomes, and round 2 is recorded under `verifications` with its reason and my response for each claim.

**What I added**
- **`direction-all-cell-pairs`**: the verifier said the existing variant only drops Rat08-20130708, while other early Rat08 sessions also have very long laps. I added two variants that limit the platform time and stops in every session. The 30 s and 10 s values are my own choice; they decide nothing, and a small helper `trim_laps` in `hpcbla.py` applies them.
  - **Laps of at most 30 s (11 sessions):** same result. Air puff p = 0.034, safe p = 0.021, air puff greater than safe p = 0.71.
  - **Each lap cut to its last 10 s (14 sessions):** the air puff test holds (p = 0.034), but the safe test misses p < 0.05 (p = 0.052).
  - The criterion fixes the reward-to-reward laps, so the outcome stays reproduced and I proposed no change. The notebook, notes, summary and README now say the result depends partly on the time around the run that those laps include.
- **`bla-rate-same-across-directions`**: I ran the same two variants on the firing rates. With laps of at most 30 s the air puff versus safe difference remains (p = 0.016 and 0.0043). With laps cut to their last 10 s it disappears (p = 0.75 and 0.82). This supports the verifier's caveat that the difference may come from platform time, not the trajectory. The caveat is now in the notebook, notes and README, and the outcome stays blocked.

**What I corrected**
- **README and notes:** the timing figures now match the final run (8.3 s for 20 frames, about 222 hours to stream the run video, 10.2 min run time, 366 s loading). These numbers vary between runs.
- **`bla-int-sleep-firing` (cell 43):** I removed the unsupported sentence that these cells "differ from the paper's in REM". It now says no test compares the two samples and that the interval of the median includes zero.
- **`ripple-rate-unchanged` summary row:** "excludes changes above about 11%" is replaced by the bootstrap interval of the change, −1.4% to 8.4% of the rate.
- **Formatting:** removed stray `**` in cells 31 and 48.
- **Round-1 record:** the platform-time point was wrongly listed as the verifier's reason under `habituation-over-days`. I removed it there, and the response now says it was raised for the air puff and safe templates.

**What I did not do**
- I re-ran the notebook with `tools/entry.py run`, not `all`. `all` stops at the check step on 29 errors, all in the earlier `-01` record, which the protocol says must stay as it was; the earlier rounds hit the same errors. The check reports no errors for this attempt's files. The notebook passed in a clean environment, and every other number is the same as before.
- After the final run I added a missing cell id to the new notebook cell. That is metadata only; the cell's code is unchanged.
- The verifier also noted that the two absence claims (`cen-no-reactivation`, `ripple-rate-unchanged`) count as reproduced only on the paper's p threshold. I changed nothing for this, because the notebook, notes and README already say so.
- Nothing is committed or pushed.
