I've finished the blind repeat attempt on sohn-2019 (DANDI:000130, version 0.241017.1448) through handover. `entry.py check` reports 0 errors, both notebooks pass from a clean environment, and the verifier's package is built in `executed/sohn-2019/handover/`. I did not come across any earlier attempt's results.

## 1. Outcomes per claim

| claim | outcome | key numbers |
|---|---|---|
| beh-slopes | not reproduced | Eye Short slopes are 1.011 and 1.110; same outcome with or without an intercept |
| beh-overlap-prior | not reproduced | at ts = 800 ms the Short median bias is +28.3 ms, Long +47.6 ms; p = 0.073 |
| beh-sigmoid-increments | reproduced | 7 of 8, p = 0.0156 |
| beh-long-more-bias | reproduced, resting on an assumption | 4 of 4 with an intercept, 3 of 4 without |
| beh-bayes-model | partially reproduced | SD correlation positive in 4 of 4; bias R2 ≥ 0.8 in only 2 of 4 (the Eye datasets fail) |
| glm-prior-ts | not reproduced | 79.2% prior-dependent, 45.8% ts-dependent (expected 65% and 27%) |
| dfr-overlap-support | reproduced | peak in the 480–640 ms bin, 6.86 against a shuffle 95th percentile of 3.15 |
| pca-dimensionality | not reproduced | 1 of 8 counts in range; 2 estimation components in every dataset |
| encoding-r2 | reproduced | Hand Left 0.996 and 0.977 |
| encoding-bayes-beats-linear | partially reproduced | Short 4 of 4, Long 3 of 4 |
| short-in-long-control | reproduced (paper's test, p = 0.25) | but the Bayesian model fits better in 3 of 4 datasets |
| neural-long-more-bias | partially reproduced | 3 of 4 |
| speed-vs-projection | partially reproduced | r = −0.93 and −0.87, stronger than the paper's |
| initial-speed-biased | not reproduced | 7 of 8 shallower, p = 0.055 |
| speed-predicts-tp | partially reproduced | r = −0.72 and −0.74, stronger than the paper's |
| alt-speed-unmodulated | reproduced (paper's test) | but slopes are positive in 7 of 8 |
| alt-transient-parallel | reproduced | p = 0.195 and 1.0 |
| alt-threshold-monotonic | not reproduced | median minimum 230 ms before Go |
| gpfa-variance-inverted-u | not reproduced | 6 of 8 negative, p = 0.055; seed and dimension variants give 0.039 to 0.098 |
| gpfa-mean-sigmoid | reproduced | |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked, data_missing | |

## 2. Dataset, assumptions, questions

What I found about the dataset:
- **One session only.** It holds one of the paper's 29 sessions (monkey H, 2016-12-11).
- **Test-file trials unusable.** The test file's 283 trials have no task variables (prior, ts, effector, direction), so about 20% of the session cannot be analysed. Their spikes are not repeated in the train file.
- **`iti` description reversed.** It says 500 ms for Short and 1220 ms for Long; the values are the other way round, which matches the paper.
- **`tp` measurement undocumented.** `tp` is longer than `go_time − set_time` by a median of 17.9 ms, and the files don't say how it is measured.
- **Missing unit labels.** Units have no electrode assignment and no single-unit or multi-unit label.
- **Clock check passes.** Spikes share the trial clock: target direction decodes at 0.76 accuracy at the true times and about 0.5 when the times are shifted.

I made one assumption: the behavioural regression has an intercept. I recorded it as a question for the paper's authors (a `methods_unavailable` finding), because the Methods write `tp = β ts` without one. I asked readers no questions.

## 3. Where the protocol was unclear

1. **Absence claims that cannot fail.** The three absence claims are tested by a signed-rank test over 4 datasets, which cannot go below p = 0.125, so they are reproduced before any data are seen. I followed the criteria and reported effect sizes, which lean against absence.
2. **A seed that changes the outcome.** The protocol treats a random seed as unable to change an outcome, but elephant's GPFA draws random trial segments, and the result crossed p = 0.05 between runs. I seeded every fit, showed three other seeds plus the 4-dimension fit, and kept the main fit's outcome.
3. **How far to run standard choices.** Many small choices could matter for close calls: smoothing at epoch edges, where a time bin is placed, whether outlier trials enter the neural averages. Running every combination isn't practical, so I added one robustness table (outlier trials included; no smoothing).
4. **Where third-party method code goes.** The protocol doesn't say whether software implementing the paper's method (elephant's GPFA) belongs under `inputs`. I recorded it as a deviation instead.
5. **archives.md download step.** DANDI's signed download URL refuses HEAD requests (403), so the step in archives.md fails as written. I took the S3 URL from each asset's metadata.

## 4. Runtime and failures

- **Runtime.** The main notebook takes about 1 minute; the GPFA notebook takes 15 to 18 minutes. Peak memory was 0.6 GB. Work ran from 06:15 to about 08:25 UTC.
- **Fixed during development.** Early GPFA runs were not repeatable because elephant's random generator wasn't seeded; that is fixed, and the last three runs gave identical numbers. A smaller elephant time-bin rounding issue (spikes dropped at trial ends) is also fixed.
- **Nothing failed in the final run.**

Files are in `entries/sohn-2019/` and the record is `attempts/sohn-2019-02.yaml`.
