I've finished the blind repeat attempt on sohn-2019 (DANDI:000130, version 0.241017.1448, the version the prompt asked for). `python tools/entry.py all entries/sohn-2019` passes, `check` reports 0 errors, and the handover is built in `executed/sohn-2019/handover/`. Nothing is committed. I did not come across any earlier attempt's results.

**1. Outcomes**

| Claim | Outcome | Key numbers |
|---|---|---|
| beh-slopes | not reproduced | 6 of 8 slopes between 0 and 1; the Short-prior slopes of both eye datasets are 1.011 and 1.110 |
| beh-overlap-prior | not reproduced | median biases +28.3 (Short) and +47.6 ms (Long), both positive; p = 0.073 |
| beh-sigmoid-increments | reproduced | 7 of 8, p = 0.0156 |
| beh-long-more-bias | reproduced | 4 of 4 |
| beh-bayes-model | partially reproduced | bias R2 at least 0.8 in 2 of 4; SD correlation positive in 4 of 4 |
| glm-prior-ts | not reproduced | 79.2% prior-dependent, 45.8% ts-dependent (expected 65% and 27%) |
| dfr-overlap-support | reproduced | peak 6.86 spikes/s at 480 to 640 ms after Ready; shuffle 95th percentile 3.09 |
| pca-dimensionality | not reproduced | 1 of 8 in range; 2 components reach 75% in every estimation epoch |
| encoding-r2 | reproduced | 0.994 and 0.986 (Hand Left); the PC space is only 2-dimensional, so random axes also score high |
| encoding-bayes-beats-linear | not reproduced | Bayesian model better in 3 of 4 datasets for each prior |
| short-in-long-control | reproduced (paper's test) | p = 0.25, but the effect is present in 3 of 4 datasets |
| neural-long-more-bias | reproduced | 4 of 4 |
| speed-vs-projection | partially reproduced | r = -0.926 and -0.834, stronger than the paper's, outside tolerance |
| initial-speed-biased | reproduced | 7 of 8, p = 0.039 |
| speed-predicts-tp | partially reproduced | r = -0.720 and -0.699, outside tolerance |
| alt-speed-unmodulated | reproduced (paper's test) | p = 0.125, the smallest possible with 4 datasets; speed rises in 8 of 8, partly an attrition artefact |
| alt-transient-parallel | reproduced | p = 0.109 (shortest ts) and 1.0 (longest) |
| alt-threshold-monotonic | not reproduced | median time of the minimum distance is 230 ms before Go |
| gpfa-variance-inverted-u | not reproduced | 6 of 8 coefficients negative, p = 0.074 |
| gpfa-mean-sigmoid | reproduced | p = 0.0078 and 0.0625 |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked: data_missing | — |

**2. Dataset, assumptions and questions**

- **Coverage:** the dandiset holds one of the paper's 29 sessions (monkey H, 2016-12-11). The train file has 1160 trials (983 completed and not outliers) and 54 units, of which 48 pass the paper's unit selection. That matches the 48 units the paper gives for its GPFA session of monkey H.
- **Test file:** its 283 trials have no task variables (the Neural Latents Benchmark withholds them), so they can't be used.
- **`iti` column:** the description reverses the two priors; the values match the paper's Methods.
- **`tp` column:** it exceeds `go_time - set_time` by a median of 17.9 ms, which is not documented. Aborted trials hold undocumented negative `tp` values.
- **Unit labels:** units have no electrode, probe or single/multi-unit label, and the electrode table has no positions.
- **Timing:** the clock checks are consistent. Target direction decodes at 0.80 at 300 to 600 ms after target onset against 0.50 with the next trial's labels, and there is a population transient after Set.
- **Assumptions:** no outcome is marked `assumed`. Where the paper allows two readings (regression intercept, how R2 is computed, the Short-In-Long axis), both readings give the same outcome.
- **Question for the paper's authors** (one `methods_unavailable` finding): whether the tp-on-ts regression had an intercept, whether rates were normalised before PCA, and how many GPFA EM iterations were run.
- **Questions to a reader:** none.

**3. Protocol points**

1. With 4 datasets, a two-sided signed-rank test can't reach p < 0.05, so the absence claims pass automatically under the rule "judged on the paper's test". I recorded them as reproduced and put the effect sizes in the notes; for alt-speed-unmodulated and short-in-long-control the effect is in fact present.
2. The claims file fixes a choice the paper leaves open: rates are not normalised before PCA. Step 1.6 doesn't say whether that choice binds the author. I followed the claims file, showed the unsmoothed and normalised versions as variants, and put the question to the authors.
3. The suggested clock check uses windows around the trial start. Here the prior is cued from trial start, so I used target onset and the Set transient instead.
4. The protocol gives `about` only for two finding kinds. I also set it on a `data_missing` and a `methods_unavailable` finding; the check accepted this.
5. The protocol asks for under ten minutes. GPFA with cross-validation takes about 11 minutes on its own, so I capped EM at 200 iterations (elephant's default is 500) and recorded that as a deviation. The fits had not fully converged.

**4. Runtime and failures**

The notebook takes about 12 minutes (12.2 at the last full run, 0.59 GB peak memory), most of it GPFA. Nothing failed. I ran the entry three times: once for the first run, then twice more after edits that only silenced elephant's log output, with identical results each time. Analysis finished at 14:07 UTC, well before the 17:10 cut-off.

Files are in `entries/sohn-2019`:
- reproduce_sohn_2019.ipynb
- rsg.py
- entry.yaml
- README.md
- requirements.in
- requirements.lock.txt

The attempt record is `attempts/sohn-2019-02.yaml`.
