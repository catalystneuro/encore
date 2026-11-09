I re-ran the entry with `python tools/entry.py all`. All three notebooks pass: 15, 30 and 43 minutes. `entry.py check` reports 0 errors, and round 1 is recorded under `verifications` for all 30 claims.

**Outcome changes**
- **fig8b-lick-coding-direction**: blocked → **reproduced**. The archive's `BehavioralEvents` hold only valve opening times, so I fetched `Lick_times.mat` from the paper's Zenodo record (about 4 min). Its jaw trace and timestamps match the dataset's.
  - In wM2 the six trial groups differ (p 0.0036), and lick trials are above no-lick trials in all three contexts (p 0.044, 0.0064, 0.015).
  - In ALM only the Go-tone comparison is significant. A1, wS1 and wS2 show none.
- **figs18-later-lick-coding**: blocked → **not reproduced**. ALM, wM2, wS2 and wS1 all separate lick from no-lick trials. But both effect-size measures in the claims file put wM2 first, not ALM.
  - The plain difference of the means does give the paper's order (ALM, wM2, wS2, wS1). I asked a reader whether that is the paper's measure.
- All other outcomes are unchanged.

**What I added or corrected**
- **Quiet-trial rule**: the notebook now prints the paper's code lines and a per-session count of trials with missing video. This confirms the assumption the verifier could not check: those trials count as not quiet. Every session has at least one such trial, so a rule that kept the missing values would reject every trial. The outcome stays partial.
- **fig5b decoding**:
  - Added the code's quiet rule (still partial, 3 of 5 values within tolerance).
  - Added four more seed sets: area means move by at most 1.02 points, so the shortfall in wM2 and ALM is not noise.
  - Ran the Methods decoder on the cue bins: the time-course claim holds under both decoders.
- **fig5c cluster removal**: added two more seed sets and the code's quiet rule. The code decoder's own result is unstable: partial in two runs, not reproduced in three. It stays blocked.
- **fig7d**: the code decoder now averages 5 runs, as the paper's code does. wM2 starts at 1.020 s and ALM at 1.025 s, and A1 shows the single bin at 15 ms. It stays blocked because the Methods decoder still puts wM2 after ALM.
- **fig4 clustering**:
  - Checked against the paper's clustering code: the row centring and unscaled PCs match it. The model's covariance regularisation (`reg_covar`) is now 0, as in that code.
  - The BIC minimum lands at k = 36, 40, 42 and 42 over four seeds, and at 40 for the best of all 20 initialisations. It stays not reproduced. One seed alone (k = 36) would give partial, so the record says this outcome is not stable.
- **Questions file**: two questions added, the figs18 effect-size measure and whether fig8b and figs18 should be marked `with_inputs`. I did not change the claims file.
- **Record and texts**: the record's inputs (`Lick_times.mat`) and findings are updated. Conclusions, summaries, README and `entry.yaml` match the new numbers. The executed copies' markdown matches the sources.

**Not done, and why**
- **fig5d** stays blocked (`not_runnable`). I did not re-implement the subspace optimisation it needs; the verifier's view that it is testable is recorded as a disagreement.
- These were too slow to run:

  | Run | Estimated time |
  |---|---|
  | Methods decoder on all 29 clusters (fig5c) | about 77 min per run |
  | Methods decoder on all 10 baseline bins (fig7d) | about 57 min per run |
  | Methods decoder with the code's quiet rule | not run |
  | Seed spread for the Methods decoder | not run |
  | The paper's 1,000 GMM initialisations | not run |

  The notebooks print the time estimates and the record says what was skipped.

I did not commit anything; the workflow commits the changes.
