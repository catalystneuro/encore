I finished steps 1 to 6 for `sohn-2019`. The entry is at `entries/sohn-2019/` and the record at `attempts/sohn-2019-02.yaml`. Both notebooks passed `entry.py all` in a clean environment, `check` reports 0 errors, and the handover is built. I did not come across any earlier attempt. Nothing is committed.

**(1) Outcomes** (20 tested, 3 blocked)

| Claim | Outcome |
|---|---|
| beh-slopes | not reproduced: the two Eye Short slopes are 1.011 and 1.107, above 1 |
| beh-overlap-prior | not reproduced: at ts = 800 both median biases are positive (+27.8 and +47.6 ms), p = 0.068 |
| beh-sigmoid-increments | reproduced: 7 of 8, p = 0.0156 |
| beh-long-more-bias | reproduced, resting on an assumption (4 of 4) |
| beh-bayes-model | partially reproduced: bias R2 ≥ 0.8 in only 2 of 4 datasets; SD correlation positive in 4 of 4 |
| glm-prior-ts | not reproduced: 79.2% prior-dependent and 50.0% ts-dependent units, against 65% and 27% |
| dfr-overlap-support | reproduced |
| pca-dimensionality | not reproduced: 0 of 8 in range (2 components for estimation, 2 to 4 for production) |
| encoding-r2 | reproduced: 0.9957 and 0.9774 (Hand Left); random axes also score high R2 |
| encoding-bayes-beats-linear | partially reproduced: Short 4 of 4, Long 3 of 4 |
| short-in-long-control | reproduced: p = 0.125; with 4 datasets the test cannot reach 0.05 |
| neural-long-more-bias | partially reproduced: 3 of 4 |
| speed-vs-projection | partially reproduced: r = −0.92 and −0.84, stronger than the paper's |
| initial-speed-biased | not reproduced: 7 of 8 in the right direction, but p = 0.0547 |
| speed-predicts-tp | partially reproduced: Short −0.61 within tolerance, Long −0.63 outside |
| alt-speed-unmodulated | reproduced: p = 0.25 and 0.125, though slopes lean positive |
| alt-transient-parallel | reproduced: p = 0.195 and 1.0 |
| alt-threshold-monotonic | not reproduced: median minimum 250 ms before Go |
| gpfa-variance-inverted-u | not reproduced: 5 of 8, p = 0.074 |
| gpfa-mean-sigmoid | reproduced: 7 of 8, p = 0.0156; Short slope higher in 4 of 4 |
| rnn-curved-manifold, rnn-perturbation, monkey-g | blocked, data_missing |

**(2) Dataset, assumptions, questions**
- **What is in it:** one session of monkey H (2016-12-11), 54 units (48 pass the paper's unit rule) and 982 usable trials. The paper uses 29 sessions from two monkeys, and its population analyses pool units across sessions. Monkey G and the paper's recurrent networks are absent.
- **Wrong description:** the `iti` column's description swaps the priors. The data match the paper's Methods (Short 1220 ms, Long 500 ms).
- **Undocumented `tp`:** it is longer than Go − Set by 0.1 to 153 ms (median 17.9 ms), and the files don't say how it was measured.
- **Test file:** its 283 trials hold no behaviour or condition labels and only 40 units, so they can't be used.
- **Missing unit metadata:** units have no single/multi-unit label and no electrode; electrode positions are NaN.
- **Clock check:** spikes and trial events share a clock. Target direction decodes at 0.62 to 0.75 around Go, and at chance with the windows shifted by 10 s.
- **Assumption (beh-long-more-bias):** I assumed the slope regression has an intercept. The Methods write "tp = β ts + ε", but the paper reads slopes below 1 as bias toward the mean, which only works with an intercept. Through the origin the result would be 3 of 4. This is recorded as a question for the authors (`methods_unavailable`).
- **Reader questions:** none asked.

**(3) Protocol points**
1. The claims file has no `checks` section, though the protocol says a file is ready when its last check says so. The prompt said it was checked, so I went ahead.
2. Three absence claims are tested by signed-rank tests over 4 datasets, which can never reach p < 0.05, so they are reproduced whatever the data show. I reported effect sizes; two of them point toward the effect being present.
3. There is no rule for expected values that depend on population size, such as PCA dimensions or GLM fractions computed from pooled sessions. I recorded the difference as a deviation and still judged the claims.
4. Any edit triggers a full re-run, so `runtime_minutes` has to be written before the final run. I left the GPFA notebook at 11 minutes; it took 11.4.

**(4) Runtime and failures**
- The whole run took about 50 minutes (12:41 to about 13:30 UTC).
- Main notebook: about 60 s. GPFA notebook (Elephant's implementation): 686 s. Peak memory 0.65 GB.
- Nothing failed: no fit failed, and the executed numbers match the development run exactly.
