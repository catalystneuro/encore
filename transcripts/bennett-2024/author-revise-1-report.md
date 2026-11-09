I've revised the attempt for every point in the verifier's report and re-run it. `python tools/entry.py all entries/001051-bennett-2024` ends with 0 errors, the notebook runs cleanly in about 17 minutes, and the conclusions match the new numbers. Nothing is committed.

**Outcome changes**
- **fig8d-cp-rf-larger-response**: changed from reproduced to partially reproduced, as the verifier said. With the Methods' quality filter, which the claim uses, the unit counts are 70, 162 and 218; the first two miss the expected 80 and 205. The effect itself holds (53 significant bins, CP-RF higher in all).
- **fig7cd-mop-coupling**: kept as reproduced; the disagreement is recorded. The notebook now reports parts that have too few events as untested, not as "not significant". All four parts can be tested only under one combination of readings (the code's area labels with the code's event rule), and they all hold there. No tested part goes against the claim under any reading.
- **fig8d-response-latencies**: kept as reproduced, resting on the half-peak latency assumption; the disagreement is recorded. Both unit filters now give the same lags: 16 and 20 ms at half-peak, 34 and 9 ms at the peak.
- All other outcomes are unchanged. The verifier agreed with 43 of 46.

**Corrections and added outputs**
- **Link claim**: RF agreement is now given per session. The share of units whose significance differs has a median of 0.8% and a maximum of 3.8%, and is above 1% in 33 of 79 sessions. All of those units sit at the threshold (p between 0.003 and 0.020 in both computations).
- **The 6 mismatched sessions**: a new spike-count check shows the files' spike counts fit the files' firing rates but not the code table's. So the code's table describes other units under those ids.
- **Penetration count**: the code's probes table marks all 467 probes (87 sessions) and all 533 (99 sessions) as inserted, so it records no failed attempts.
- **Clock check for running and pupil**: added to the data check. Running slows after hits from a median 0.225 s after the change, and the pupil constricts after white flashes from a median 0.35 s. The check is too weak to show alignment in 5 sessions for running and 3 for the pupil.
- **figs4i**: the fit window is now stated as an assumption. Every window from 30 to 77 min gives a time constant above 33 min, so the outcome does not depend on it.
- **figs6-replay**: the requested run keeping only events 0 to 0.5 s after the stimulus gives r = 0.19 to 0.53, none within tolerance.
- **fig7a**: a zero-padded spectrum removes the 0.5 Hz quantisation. The MOp median moves to 4.64 to 4.74 Hz, inside the range, and MOp is still higher in all 8 combinations. A synthetic test shows the event detector only finds 3 to 5 Hz rhythms, so a 5 to 7 Hz MOp band could not appear.
- **Statistics fixes**:
  - The multiple-comparison correction now covers brain areas only; this changes significance for 4 of 734 pair results and no outcome.
  - Noise CP units now get RF p values, so the code's filter splits them correctly. It now gives 79, 206 and 239 units, within one of the paper's counts.
  - Area labels under both labelling schemes are listed: SSp has no subdivisions in these files.
- **Statements**: the helper's docstring now names the bootstrap RF p value it actually uses, not the analytic one. The choice of unsmoothed rate for the coherence steps is now stated, with its source: only that choice reproduces the code's printed event counts.
- **Reader questions**: `questions/001051.yaml` is new, with two questions:
  - **fig7e**: whether "straddled zero" means a signed-rank test of the median lag or a spread of lags across zero.
  - **fig8d**: whether the claim should use the code's unit filter, which matches the paper's counts.
- **Record**: the round is recorded under `verifications`. The behaviour claim's notes now carry the verifier's point about the paper's half-integer medians. README, summary and runtime (now about 20 minutes) are updated.

**Not done**
- I did not run the full coherence analysis on the smoothed rate. Its event counts are far from the code's (3035 to 3426 against 1653 for VISp), so the code settles that choice.
- I did not change any claim's statement, expected values or criterion. The two possible misreadings are left to a reader.
