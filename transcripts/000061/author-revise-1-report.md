Round 1 revision is done. Five of the six outcomes are unchanged. The one change is the reason the behaviour claim is blocked. The entry re-ran cleanly with `python tools/entry.py all` (670 s, check passes with 0 errors), and every conclusion matches the new outputs.

**Outcome changes**
- `rats-learn-puff-location`: still blocked, but `blocked_by` is now `too_large` instead of `data_missing`, as the verifier argued. The files hold the raw video frames, so position could in principle be tracked. The run videos alone are about 1.9 million frames (1328 GB uncompressed). Streaming 20 frames took 8.1 s, so the run frames would take about 217 hours. The video timestamps are also not on the session clock.
- The other five outcomes stand: four `reproduced`, and `aversive-direction-stronger` is `not_reproduced` (p = 0.11). The verifier agreed with all of them.

**Added or corrected, by verifier point**
- **Run epochs:** a data check now prints every run epoch, the one used, and the sleep epochs on each side. Only Rat08-20130708 has a second run, and the first is used.
- **Ripple peak (claim 2):** added session-level tests. Peak over flanks holds in 13 of 15 sessions (p = 0.00031), and its post minus pre increase in 10 of 15 (p = 0.03). Reading (b) holds in 10 of 15 (p = 0.03). The conclusion now says that much of the peak is already there in pre-sleep, so only the post minus pre contrasts speak to reactivation.
- **Ripple-up cells (claim 3):** each rat is now also tested against its own chance level (Rat10 p = 0.018). About 1% of the shifted windows fall outside Non-REM.
- **Involvement (claim 4):** added a firing-rate control.
  - Up units fire faster in the run (1.66 against 0.41 Hz).
  - Against other units of matched rate they still carry more weight (24 of 31 patterns, p = 0.012).
  - At session level the plain difference holds (p = 0.027), but the rate-matched difference does not (p = 0.22).
  - The outcome stays `reproduced`, because the criterion is the pooled per-pattern test; the notes now say rate explains part of the effect.
- **Puff direction (claim 5):** added a table of lap durations and template bins per session, plus two variants. Leaving out the sessions with fewer than 5 puffs gives p = 0.15. Using only the travel part of each lap gives p = 0.19. The equal-bins variant now uses a random subset instead of the first bins, which moved it from p = 0.28 to 0.33. Two new deviations record the missing puff minimum and that laps include waiting time.
- **Behaviour:** added a section with lap counts and durations by direction in the pre-run, run and post-run. Laps toward the puff end are slower only during the run (ratio 1.18, p = 0.0063). This is shown as a description only and decides no outcome.
- **Corrections:**
  - The data-check text said twelve files lack sleep states; the output shows sixteen.
  - The README, the summary and the findings now describe the video correctly.
  - New notebook cells got cell ids, to clear an nbformat warning.
- **Record:** round 1 is recorded under `verifications`, with each claim's agreement, the verifier's outcome and reason, and my response.

**Not done**
- I left the behaviour claim blocked instead of testing the lap-duration proxy the verifier suggested. No criterion was written for that claim before the data were seen, and lap times give no position on the track.
- I did not download any paper text; the full text is not open access.
- Nothing was committed or pushed.
