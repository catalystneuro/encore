No outcome changed. All 29 outcomes stay as the round-2 verifier agreed them, and nothing needed a `proposed` change. I re-ran the entry three times with `python tools/entry.py all`. The last run passed, and the entry check reports 0 errors.

**The verifier's numbers did not match my runs.** It found three places where the text disagreed with the printed output: 1,879 trials (fig3e), 0.570 (figs4) and p = 0.051 (figs7). My runs on this machine all print what the text already said: 1,821, 0.5673 and p = 0.053. Two consecutive runs gave identical text output, so the difference most likely comes from running on another machine. I added a printout to test this: 9,869 trials have a running speed below 1e-9 m/s that is not exactly 0. So the count of "speed exactly 0" depends on rounding in the smoothing filter, which would explain why a run elsewhere differs. I kept my run's numbers and added the verifier's alongside them in the notebook and the record's notes. None of these differences changes an outcome.

**Text corrections:**
- **fig2c (cell 27):** it now says only the optimal and sub-optimal dwells are longer than the paper's. The disengaged dwell is within tolerance under readings (a) and (c).
- **figs8a:** cell 80 now prints each p-value with two significant digits. The notes give the printed values (0.00024 and 0.0012 for the optimal fits, and so on) in place of "below 0.001, 0.001".
- **Run time:** the notebook now prints its total run time. Cell 0 and the README give this run's 15.7 minutes (2.0 to stream the files, 9.1 for the cross-validated fits, 4.1 for the decoders), plus the slower stage times from the verifier's run.

**Recorded:** round 2 is under `verifications`, one entry per claim, all marked as agreeing. Each gives the verifier's outcome, its reason paraphrased from the report, and my response. The marginal fig3f result (0.5737 against the 0.57 lower bound) is recorded as the verifier accepted it. The same value printed in all three of my runs.

**Not done:**
- The verifier's open points that do not affect any conclusion are left as they were: which 381 sessions the paper used (already a question to the authors), the untested stage 6 part of distractor-response-rate, and the 5 unexplained visual sessions.
- The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/000678.yaml`.
- The reason for the cross-machine difference is my inference. It is not confirmed, because I do not have the verifier's executed copy.

Nothing is committed, as instructed.
