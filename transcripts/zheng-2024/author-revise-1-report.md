I've revised the attempt in response to every point in the round 1 report and re-run the entry. The final run of `python tools/entry.py all entries/zheng-2024` passes with 0 errors in about 31 minutes, and its numbers match the conclusions, README, summary and record. Nothing is committed.

**Outcome changes (round 1, so changes are allowed)**
- **figs8-speed-no-trend: not reproduced → reproduced, resting on an assumption.** The paper's familiar r = 0.01 with p = 3e-11 needs about 400,000 samples, so I took the correlation to be per frame of forward running, not per trial. On that reading r = 0.042 (familiar) and −0.052 (novel), both within tolerance. Per trial they are still 0.154 and −0.148, which would fail. The paper's novel p fits about 200 samples, so its two values contradict each other; I added a question for the paper's authors on this.
- **fig4no-head-scans-not-related: not reproduced → partially reproduced, resting on an assumption.** This matches the verifier's outcome. The assumption is that maze segments are compared per position bin. The positive link between switching ON and head scans still holds (r = 0.262, p = 0.0085).
- **figs1-not-electrode-drift: blocked → not reproduced, on one session only.** I ran it on e16_3m1_210201 (smallest raw file, 52 GB), using the paper's code for the switch time and waveform window. Across switches ON, neighbouring units' amplitude drops by 1.2% (p = 0.0034); across switches OFF it does not change (p = 0.31). This is fragile: it rests on measuring amplitude peak to trough, which the paper doesn't define. Measuring the trough alone, or timing switches from the trial start, gives no significant ON change. I added a question for the authors.

**Other fixes**
- **Switch detection (problem 5):** I fetched the paper's code. Ties between models go to the smaller number of change points, as the notebook already did. One change: the significance bound is now "at most", as in the code, instead of "below". That moved every number slightly but no outcome.
  - The alternatives are now variants. Breaking ties toward the larger number would put all four fig2d ON/OFF fractions in tolerance.
  - Detecting fields on per-trial-averaged maps (the Methods' wording) would change only fig2e: one test gives p = 0.058, which would make it partially reproduced. The record says so.
  - Per-session counts are printed. The code's stored outputs give only totals, so a session-by-session comparison isn't possible.
- **fig6 (problem 2):** the shuffle now stays within each field's own turn, as the code does, and the lag-1 window variant is run. Familiar sessions with significant co-switching drop to 10 ON and 10 OFF; ON is still two sessions above the expected count, so it stays not reproduced. The lag-1 variant matches all four values.
- **figs12 (problem 3):** three field selections are shown, including the code's. None brings the medians within tolerance. I found that the legend's "start" and "middle" windows are swapped relative to the code's stored outputs, and recorded it as a code mismatch.
- **fig4di (problem 6):** if the last two trials are also left out, no correlation is significant. The decrease rests on the trials at session ends where no switch can be detected; the notes now say so and the outcome stays partially reproduced.
- **fig4-glm-deviance (problem 4):** kept partially reproduced, the same as the verifier's judgement, and the notes say the criterion doesn't name this case.
- **Smaller items:** fig1h and fig1i slopes now use per-lag averages as the criterion says (outcomes unchanged). The fig4-delay-zone cell prints segment boundaries and field peaks per segment. The data-check label is fixed.
- **Record:** round 1 is recorded under `verifications`, and new findings are added at the end. There were no critical findings to review.

**Not done**
- The full figs1 test on all 11 raw files (about 78 GB) was not run; the result covers one session.
- The segment check for fig4-delay-zone is a printed table, not the plot the verifier asked for.
- No reader questions were added to `questions/zheng-2024.yaml`, because the verifier reported no place where the claims file misreads the paper.
