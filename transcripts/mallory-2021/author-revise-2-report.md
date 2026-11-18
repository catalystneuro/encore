The revision is finished. No outcome changed, and the only proposed change is supp12 (blocked → reproduced), which goes to round 3. All four notebooks ran and passed, and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Proposed change (verified outcome kept as blocked)**
- **supp12-no-false-eye-detection:** I ran it in a new notebook, `simulated_eye_mallory_2021.ipynb` (41.3 min). Each eye cell's spikes are simulated from its fitted model with the eye terms removed, and the LN pipeline is rerun.
  - Eye variables and body position or speed share information: the data value is above all 100 shuffles in 11 of 11 sessions for each of the six pairs.
  - In the simulated data the eye variables are found in 0, 2, 2 and 0 cells, against 341, 243, 238 and 137 in the real data. That is at most 0.8%, well inside the criterion's 10%.
  - It rests on two choices the paper leaves open: which cells to simulate (the 718 eye cells plus a random 300 of the other encoding cells) and which fitted parameters to use. Both are recorded as assumptions.

**Marked `assumed: true`, with the reason written into each outcome**
- **fig7ab:** stays reproduced, but only with folds assigned in turn and fold 1 held out. With random folds, fold 1 gives 10 of 12 comparisons and 1 of 6 medians, and no fold meets both parts.
- **fig5bv:** stays partially reproduced on the same fold reading. With random folds it would be reproduced; the record says so, so it is treated the same way as fig7ab.
- **fig6-eye-velocity-linear-nasal and fig6v:** both hold only with folds assigned in turn.
- **The ten Cohort 1 claims:** two assumptions are now stated on each. The check that spikes and behaviour share a clock was inconclusive, and dropping out-of-range bins removes 31% of them.

**Corrected**
- **Stale notes:** supp4-eye, fig5a, fig5b and fig6-nonlinear-temporal now match the printed numbers.
- **fig1c-azimuthal-velocity-cells:** now reports the Cohort 1 count of 10, outside 12 ± 1.2, so it could be at most partially reproduced. It stays blocked because the Cohort 2 count was not run.
- **Timings:** the "about an hour per reading" estimates are gone, and the timings now match this run (31.4 min, 2021 s, and the notebook runtimes).
- **Notebook text:** I fixed the stale passages the verifier quoted in the main notebook (cells 4, 22, 64), the freely moving notebook (cell 8) and the readings notebook's Summary. The summaries and the README now state these fold dependencies.

**Recorded**
- Round 2 is under `verifications` for all 47 claims, using the verifier's reasons and my responses. supp12 is recorded as a disagreement.
- I added two questions for the paper's authors: the supp12 choices, and whether out-of-range bins were dropped or clipped in the freely moving model.
- No question for a reader was added, because the verifier reported no misreading of the claims file this round.

**Not done**
- **Clipping out-of-range bins (2b) and random folds (1b) on Cohort 1, and clipping on the head-fixed data:** none of these were run. Rerunning the four notebooks took about 3 hours, and I gave the remaining time to supp12. The Cohort 1 clipping run would keep about 1.44 times the bins, so about 45 min. The record says these were not run and why.
- **Cohort 2 claims, supp3-head and supp3-eye:** still blocked as too large, about 3 to 3.4 h each.
- **How it was run:** the four notebooks together take longer than the 2-hour limit on one command. So, as in round 1, I ran them in two parts with `entry.yaml` cut down, then restored it and joined `result.json`.
