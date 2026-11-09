No outcome changed in this round. I re-ran the entry with `python tools/entry.py all entries/000409-ibl-2025`: the check gave 0 errors and the notebook ran in 24.6 minutes. Apart from the new oscillation variants, every number came out the same as the previous run. Nothing was committed or pushed.

**Outcomes**
- **behav-zero-contrast:** I agree with the verifier. The criterion only defines when the claim is reproduced, and neither reading meets it. The verified outcome stays partially reproduced, and I wrote `proposed: not_reproduced` on it with the reason, so a third round will review it. Cell 49, the summary table and the README now say this.
- **fback-oscillation-licking:** stays partially reproduced. The verifier asked for a power test that picks its frequency band without using the correct trials, and for one with the evoked response removed. I added both to cell 102:
  - With the band set within 1 Hz of each session's lick peak, power is still higher after correct feedback: 15 of 26 sessions, p = 0.038.
  - After subtracting each condition's slow evoked response, it is 15 of 26, p = 0.031.
  - Measuring each condition at its own peak gives 16 of 27, p = 0.077.
  - In the paper's 9 to 11 Hz band there is no difference (p = 0.7).

  So condition (ii) holds when the band follows the licks. The PSTHs are averages over trials, so the faster part of the evoked response cannot be removed. Cell 103 and the notes now say so.

**Text corrected**
- **README run time:** now matches the timings printed by this run (3.6, 1.8, 11.8, 4 and 1.8 minutes). `runtime_minutes` in `entry.yaml` is now 25.
- **wheel-speed-decoding notes:** the decoding estimate is now this run's 30 minutes, noting that the previous run gave 41.
- **Cell 97 and the traj-latency-late notes:** the latencies barely move when the window end goes from 150 to 200 ms. They do change in the paper's 0 to 100 ms window, so the outcome depends on the criterion's 0 to 150 ms window.
- **dec-feedback-nearly-all notes:** removed the sentence blaming the smaller null, which no output supported.
- **Summary (cell 106):** it no longer says the dandiset holds the released dataset completely. It now says the receptive-field mapping and the saturation intervals are missing.
- **Stimulus against choice margin:** cell 76 and the dec-choice-widespread notes now say the one-region margin depends on CL. CL is at the lowest p a 2-session region can reach (0.0010), and the full nested null was only run for VISp stimulus.
- **Round 2 record:** added under `verifications`, with the verifier's agreement, outcome, reason and my response for all 30 claims.

**Not done**
- **Nested null for the choice regions:** not added. The notebook already takes 24 to 29 minutes of the 30-minute limit. With fewer nulls, CL's 2-session floor would rise above its current p, so the run could not test CL anyway. I recorded this as the response under dec-stim-restricted and dec-choice-widespread.
