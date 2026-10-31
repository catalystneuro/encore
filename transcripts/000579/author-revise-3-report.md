Round 3 is recorded and the entry passes its checks. `python tools/entry.py all entries/000579-tseng-2022` gave 0 errors, and both notebooks passed: the main one in 1161 s and the second in 1080 s, both under the 30-minute limit. Nothing is committed.

**Outcome changed:**
- **fig3q-cue-decoding** moved from partially reproduced to reproduced, and `proposed` is removed. The verifier agreed with the proposal. In the re-run, the numbers behind this claim are the same as the ones it reviewed:
  - V1 is above PM under all 12 readings, by 0.027 to 0.062.
  - AM, the highest of the other four areas, is 0.118 to 0.157 below V1.
  - A is the lowest area, below V1 at p < 0.001.

**Proposals still standing:** none. This was the only proposal. The fig8cd result in the second notebook is a check of an assumption, so its outcome stays reproduced.

**Other changes:**
- **Notebooks:** the main notebook's fig3q conclusion and summary row, the second notebook's result and summary, and the README row now give fig3q as reproduced. They also state the verifier's caveats:
  - The ranking takes V1 and PM from every V1 and PM field session, and the other four areas from the 18-session subsample.
  - Decoders labelled PM in sessions of other fields were not fitted, so PM has 71 to 80 decoders against the paper's 106.
  - The per-mouse and per-field checks are printed for one reading only.
- **Timing figures:** these did not match the printed output, as the verifier noted. The record and README now quote this run's numbers:
  - decoders: 488 s for the subsample, 4.5 CPU hours and 67 minutes for the whole pool;
  - second notebook: 922 s of fitting, 18.0 minutes in total;
  - main notebook: 19.2 minutes;
  - GLM: 652 CPU hours;
  - shattering: 5.1 CPU hours.

  No conclusion changes, because every figure is still over the limits.
- **`verifications`:** round 3 is added with one result for fig3q. It records that the verifier agreed and gave reproduced, its reason and caveats in its own words, and my response.
