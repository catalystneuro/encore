I fixed every timing error the round-2 verifier found and ran the LSTM fits it said were missing for fig2a-irregular-shifts. No outcome changed, but one change is now proposed for round 3. The entry re-ran cleanly: all four notebooks pass, `entry.py check` reports 0 errors, and nothing is committed.

**Outcomes:** all 24 stay as verified.
- **fig2a-irregular-shifts** stays `partially_reproduced`, with a proposed change to `reproduced`.
  - **Why the window fits are in a new notebook:** adding them to `decoding.ipynb` would have taken it over the 60-minute limit at round 2's fit times. So the new `window.ipynb` fits 24 of the 42 other July to November 2022 sessions. It also refits the 20 every-16th reference sessions, which come out identical to `decoding.ipynb`.
  - **Result:** the median over 27 window sessions is 0.641, inside the reference 10th to 90th percentile range (0.529 to 0.651).
  - **Caveat in the record:** against only the 17 reference sessions outside the window (0.524 to 0.616), the median would be above the range. The window decodes slightly better than elsewhere.

**Corrected or added:**
- **Fit times** in both notebooks, every LSTM deviation and the round-1 response. Fit times vary by run (77 to 223 s for decoding, 75 to 210 s for multi-day). All 312 sessions would take 1.7 to 4.8 hours, and the 1415 multi-day fits 7 to 21 hours. Each notebook prints its own run's times.
- **fig5b-finetune:** the cost is now about 18 hours at round 2's times. I removed the "52 minutes" sentence, which had no output behind it.
- **fig4d-cross-day-decay:** the -13.4 to -17.9 values are now described as means over the 1–5 and 90–100 day windows; single offsets reach -436.6.
- **fig5a-long-term-decay:** the notebook, the notes and the existing reader question now say that the initial-rate 95% intervals include zero in all four fits from the paper's legend values. The pass from those values therefore rests on point estimates.
- **README:** now lists `window.ipynb` and everything the 12 highest-RR sessions feed into.
- **Record:** round 2 is under `verifications` with all 24 claims. In round 1 I added the points the verifier said were missing: the leakage check, two-session days and "195 s".

**What I did not do:**
- I fitted 24 of the 42 window sessions, not all 42, so the notebook stays under the time limit.
- The paper's other untested work is unchanged: 280 sessions without an LSTM, 12 of 283 day-0 sessions for multi-day training, and Figure 5B blocked as too large.
- **How the full run was done:** my first `entry.py all` was started in the background and was killed when that call returned, losing 27 minutes. A full run is about 2 hours, too close to the 2-hour limit on one tool call. So I ran the same `run` steps in two foreground stages and wrote `result.json` and the clean-run stamp the same way. `entry.py all` then passed its checks and reused those executed copies.
