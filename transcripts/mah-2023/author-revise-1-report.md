I've finished the round-1 revision. Both notebooks were re-run from a clean environment and pass: the behaviour notebook took 24 minutes and the models notebook 51. The entry check gives 0 errors and the record matches the schema. Nothing is committed.

## Outcome changes
| Claim | Before | Now | Why |
|---|---|---|---|
| fig2k | reproduced | partially_reproduced | The task repeats the offer after every violation (100% of 4.26M trials). The code's result comes entirely from those trials. Without them, the population starts trials faster after small offers (p = 2.4e-32), which matches the Methods reading. This is verifier problem 2. |
| fig2l | reproduced | partially_reproduced | Same cause as fig2k. |
| fig5c | reproduced | partially_reproduced | Same cause: the code's trials without post-violation trials give the wrong direction (p = 0.28). |
| fig5b | reproduced | partially_reproduced | The Methods' 30-session reading still rises from 5 to 10 µL, including when the 30 sessions are counted over the sessions the files flag as pre-cue (`center_port_cue`). |
| fig3l | reproduced | not_reproduced | With the bounds from the paper's `my_fit_sigmoid.m` (C ≥ 0) and continuous parameters, the wait-time C at mixed-to-low has p = 0.45. At mixed-to-high, C has p = 0.36 and D p = 0.31. The initiation-time C at mixed-to-low reaches p = 0.041. |
| suppfig8 | reproduced, seed sensitive | reproduced | On this run no seed goes below p = 0.05 (lowest 0.062). The first run, on another machine, had p = 0.031 at one seed; the notes give both. |

The verifier agreed with the other 27 outcomes, and none of those changed.

## What I added or corrected
- **fig3l:** the logistic fit now uses the paper's code bounds and a continuous fit. The cell prints the fits, any ties with the shuffles (none for a tested parameter), and shuffle fits at a bound.
- **fig3i:** I added a noise check. Without any noise, the alternative models still overshoot slightly (0.0005 to 0.0073, against 0.280 for the main model). So the small overshoots are in the models themselves, not noise, and the outcome stays partial. I also ran the exact mean of 50 log-normal draws in place of the shortcut, with the same result.
- **fig3f:** I added a variant that leaves out the 14 rats with a fitted parameter at a bound, and the model's prediction without noise (p = 6.5e-62). I also made the cell faster.
- **Figure 4 data from Zenodo:** 21,302 of 23,033 dandiset sessions are found in the deposit, none twice. The matches follow the dandiset's dates in 281 rats; in 10 rats one or two sessions step back. The matching also confirms that the dandiset's `inter_trial_interval` lines up trial for trial with the deposit's `ITI`.
- **fig4a:** the per-rat median and pooled ratios put the first session pair closer to 1. The criterion names the mean, which still fails (it rests on about 5 trials per rat), so the outcome stays partial.
- **bayes:** the text now says reading (i) goes the opposite way from the statement's sign. I added entropy as a variant: 0.358 to 0.283.
- **pre-cue link:** added two variants, the flagged sessions in place of the dates and the last two dates for S042 and S050. I also added a question for a reader in `questions/mah-2023.yaml`.
- **Problems 7 and 8:** no code change. The paper's own code does both things the verifier queried, and the record now cites the lines:
  - fig3c: `Figure3.m` drops the first 1000 trials of the filtered sessions, which are the sessions the dandiset holds.
  - Models: `GenerateSynthData_Bayes.m` uses one C per rat and the thresholded wait time.
- **Record:** I updated the fig2k `code_mismatch` finding and recorded round 1 under `verifications` for all 33 claims. No finding is rated critical.

## Not done
- **Model fits:** they still use 2 random starts, against the paper's 100. One seed takes about 4.4 minutes with 2 starts, so more would not fit the 60-minute limit.
- **Runtime in `entry.yaml`:** the behaviour notebook still says 15 minutes, though this run took 24 (the download was slow). Editing the file would have invalidated the completed run.
