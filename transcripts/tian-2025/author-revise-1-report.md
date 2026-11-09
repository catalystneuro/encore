The round-1 revision is done and the entry re-runs cleanly: `python tools/entry.py all entries/001559-tian-2025` gives 0 check errors and the notebook passes in 522 s. The numbers that were already there came out unchanged on the second run.

**Outcomes: none changed.**
- **Verifier agreed on 19 of 21 claims**, including fig4b reproduced, fig4c blocked, fig4d-steady-baseline partially reproduced, fig4d-evoked-increase blocked, and the 15 claims blocked for missing data.
- **Disagreements kept and recorded:** the verifier would give fig4d-4ma-single-trials as reproduced (conditional) and fig4d-electrode-timing as partially reproduced. Both stay blocked as `methods_underspecified`. The claims file lists fig4d-evoked-increase under `depends_on` for both, and the protocol blocks a claim that depends on a blocked claim for the same reason. The notes give the test results as run.

**Added in reply to the report:**
- **Speckle (problem 4):** the notebook now reads every frame of the three movies, not just the first 400, and describes the whole-field flow index (1/K²). In the three less noisy exposure phases it varies by 0.8% to 4.5% (s.d.). It shows at most three small episodes per movie (0.9% to 2.6%) and no repeated change at a regular period. This is labelled as a partial look, not a test. It uses the whole field because the speckle field is not registered to the eBRIC region.
- **File contents:** a new data-check cell lists every file's top-level groups. No file has an `intervals` group, and in all 35 the `stimulus` group is empty and `processing` holds nothing.
- **Session 150418 around onset (problem 1):** the averaged trace from −2 to +3 s is now printed, smoothed and unsmoothed, with baselines.
  - The unsmoothed trace is 0.77 above baseline in the second before onset. It passes half its peak (1.27) in the first bin after onset, so the 0.005 s "rise" is a step at onset that the centred 1 s average shifts earlier.
  - I added two variants of the rise time. Both give the same result: 145053 is later on both peak and rise at the assumed 2 mA, and neither session is at 4 mA.
- **One condition per session (problem 3):** per-trial responses are now printed in trial order. There is no sign of alternation or blocks within a session (p 0.31 to 0.89). Every trial of the two strong sessions is 7.64 or more, and only one weak-session trial (7.77) is above that. This is consistent with one condition per session but does not show it.
- **Steady baseline (problem 2):** added a straight-line-trend variant. Session 145053 still fails on channel 4. The conclusion now says the roughly 50-unit rise over the six recordings is larger than the 4 mA response, so the level is not steady across recordings, though the criterion judges each recording.
- **Baseline s.d. (problem 5):** added a variant that leaves out the last 0.5 s of the baseline. Every 4 mA fraction stays at 1.0.

To support these, `ebric.py` gained `layout`, `speckle_timecourse`, a `rise="crossing"` option in `peak_and_rise`, `smoothed=False` in `event_average`, and a new `baseline_sd_smoothed_pre` column. The conclusions, summary, README, attempt notes and `verifications` block are updated to match the new numbers.

**Not done, and why:**
- **Processes in fig4b (problem 7):** no measure added. The files give neither a usable pixel size nor the z step, so nothing here can tell processes from neuropil.
- **Channel 3 count and pixel size (problems 6 and 8):** already correct in the record, so no change.
- **Questions file:** no question added, because the verifier did not report any place where the claims file misreads the paper.
- **Commit:** nothing committed, as instructed.
