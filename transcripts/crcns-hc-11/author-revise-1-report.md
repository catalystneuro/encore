I've finished the round-1 revision, but the notebook now takes 71 minutes to run, over the 60-minute CI limit. `entry.py all` ran every cell without an error and flagged it as FAIL on run time. There wasn't time for a second run, so the next run needs to get it back under the limit. The quickest fix is to give the new rate-split variant fewer shuffles, or move it to its own notebook. It took 7 of the roughly 12 minutes my additions cost. `entry.py check` gives 0 errors. Nothing is committed.

**Outcome changes** (the tally is now 12 reproduced, 10 partially reproduced, 8 not reproduced, 1 blocked):
- **rigid-plastic-counts:** not reproduced → partially reproduced, as the verifier gave it. The counts match the paper under one direction reading (D-b: 109, 113 and 108 per group) and miss under the other (D-a: 121).
- **figs16de-more-ripples-post:** partially reproduced → not reproduced. The criterion requires the interval medians within tolerance, and ours (1.35 and 1.24 s) are less than half the paper's (3 and 2.47 s). The LFP half was not tested.
- **fig4c-coactivation-by-rate:** kept as reproduced, against the verifier's partially reproduced. It rests on within-session rate ranks, which the paper's "within each session" passage supports. The disagreement is recorded.

**What I added:**
- **D-b groups:** every rigid/plastic claim is rerun with the D-b groups under all three yoking readings. Offline measures are also rerun with each cell counted once. No outcome changes. figs13 and figs18 fail further under some of these readings, and figs13 stays marked as resting on the D-a groups.
- **Rate splits:** fig4d and fig4e are run under the five rate splits that weren't run before, at 100 shuffles. No split gives fig4d's reproduced pattern. fig4e meets its reproduced criterion under split (b, ii) only, so both outcomes are kept and marked as resting on split (a, i).
- **fig2d and figs12:** both are pooled under all six Y × D readings from the same templates. Both still hold, with cells ranked under Y-a, D-a throughout.
- **Diagnostics:**
  - Event counts after each selection step, and 1,855 events per hour of NREM over all sessions (mean interval 1.94 s).
  - A within-session test for fig1c (13 of 13 templates, p = 2.5e-25) and figs5f (9 of 13, p = 1.0e-16).
  - Laps against running time per session.
  - An MD5 check of the streamed file, which matches `checksums.md5`.

**Corrections:**
- Spikes after the session end in Gatsby_08022013 are now left out instead of being clipped into the last bin.
- Two-sided p-values now decide figs14 and figs16ab. figs16ab still holds on coactivity reading (d).
- The `verifications` block records the verifier's outcome and reasons for all 31 claims (28 agree) and what I changed in reply.

**Not done:**
- **LFP readings (problem 1):** not run. The LFP is about 70 GB of tar.gz and would not fit within the notebook limit. This is stated in the fig1c and figs16de conclusions.
- **FWHM kernel downstream (problem 3):** not rerun. The claims file names the SD reading as the standard one, and a rerun would repeat the whole pipeline.
- **figs11:** still blocked. The verifier showed the quality and stability parts are testable from the per-session archives, and the notes now say so, but I didn't write the test in time.
- **Also not done:** fig2e with D-b groups, fig2d and figs12 re-ranked under each reading, and more templates for fig2d.

No question was added for a reader, because the report didn't flag any place where the claims file misreads the paper.

About an hour of the session was lost to a dev script of mine that ran the shuffles with too many threads at once. That is why I dropped the one-session LFP check and the figs11 test.
