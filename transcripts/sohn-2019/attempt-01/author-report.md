I've finished steps 1 to 6 for dandiset 000130. `entry.py check` reports 0 errors, the notebook passes `entry.py all` from a clean environment in 397 s, and the verifier's package is built in `executed/000130-sohn-2019/handover/`. Nothing is committed.

**Paper text:** I used the full text of the accepted author manuscript (PMC6805134). It is saved under `paper/`. The supplementary tables and figures were not available.

**Version pinned:** 0.241017.1448. The paper cites no DANDI version. The two published versions hold the same two files and differ only in publication metadata, so I pinned the most recent; the notebook header says why.

### 1. Outcome per claim

| Claim | Outcome |
|---|---|
| beh-slopes | Not reproduced: 6 of 8 slopes between 0 and 1; the two Eye Short slopes are 1.11 and 1.01 |
| beh-overlap-prior | Not reproduced: both biases positive (+28 and +48 ms), p = 0.073 |
| beh-sigmoid-increments | Reproduced: 7 of 8, p = 0.016 |
| beh-long-more-bias | Reproduced: 4 of 4 |
| beh-bayes-model | Partially reproduced: SD fits in 4 of 4, bias R2 ≥ 0.8 in only 2 of 4 |
| glm-prior-ts | Not reproduced: 75.0% and 45.8%, against the paper's 65% and 27% |
| dfr-overlap-support | Reproduced: largest at 480 to 640 ms after Ready |
| pca-dimensionality | Not reproduced: 2 PCs reach 75% in the estimation epoch |
| encoding-r2 | Reproduced: 0.998 and 0.996, but random axes beat it in 5 of 8 dataset-priors |
| encoding-bayes-beats-linear | Partially reproduced: Long 4 of 4, Short 3 of 4 |
| short-in-long-control | Reproduced by the paper's test, which cannot detect an effect with 4 datasets |
| neural-long-more-bias | Reproduced: 4 of 4 |
| speed-vs-projection | Partially reproduced: rho −0.94 and −0.88, stronger than reported |
| initial-speed-biased | Reproduced: 7 of 8, p = 0.039 |
| speed-predicts-tp | Partially reproduced: rho −0.73 and −0.74, stronger than reported |
| alt-speed-unmodulated | Reproduced by the paper's test, but the speed rises in all 8 dataset-priors (bootstrap intervals exclude 0) |
| alt-transient-parallel | Not reproduced: longest ts, p = 0.039 |
| alt-threshold-monotonic | Not reproduced: median minimum 210 ms before Go; depends on how many PCs are kept |
| gpfa-variance-inverted-u | Not reproduced: 5 of 8, p = 0.125 |
| gpfa-mean-sigmoid | Reproduced: p = 0.0078 and 0.0625, the paper's exact values |
| rnn-curved-manifold, rnn-perturbation | Blocked (`other`): these concern trained network models, not recorded data |
| monkey-g | Blocked (`data_missing`) |

### 2. What was found about the dandiset
- **One session only.** It is the Neural Latents Benchmark version of a single session of monkey H (2016-12-11), out of the paper's 29 sessions over two monkeys. No other dandiset on the archive holds these recordings.
- **Likely the paper's GPFA session.** 48 of its 54 units pass the paper's 1 spike/s rule, which matches the paper's GPFA count for monkey H. The dandiset does not say this.
- **Test trials unusable.** 283 trials are in the test file with no task variables and without 14 of the 54 units, so no analysis can use them.
- **`iti` description reversed.** It says 500 ms after Short trials and 1220 after Long; the values (and the paper) are the other way round.
- **`tp` does not match the event times.** It is a median 18 ms longer than `go_time − set_time` (up to 200 ms), and this is not documented.
- **`is_outlier` not reproduced.** A refit of the paper's mixture model flags only 10 of the file's 46 outliers.
- **Units under-described.** There is no single-unit or multi-unit label and no electrode assignment, and the electrode table has no positions.
- **Code not public.** The paper's code is available only on request, and the linked benchmark code holds none of its analyses.
- **Paper inconsistency.** The Results give the GPFA counts as 48 and 107 neurons; the Methods give 48 and 96.

### 3. Where the protocol was unclear, wrong or missing something
1. **Claims of absence tested on a subset.** "Judged on the paper's test alone" breaks down when the dandiset holds 4 of the paper's 8 datasets. A signed-rank test over 4 can never give p < 0.05, so two absence claims come out "reproduced" automatically, one of them against clear evidence. I followed the rule and said so in each claim's notes and Result text.
2. **No guidance on adapting the paper's statistics to a subset.** Where the paper's p = 0.008 means "all 8 datasets", I wrote criteria that count datasets (for example, 4 of 4).
3. **The default 10% tolerance fits some measures badly.** For R2 near 1 it accepts anything above 0.894. For a proportion from 48 units, sampling error is larger than 10%. I kept the default and reported binomial intervals.
4. **No blocking reason for model-only claims.** For the recurrent network claims I used `other`.
5. **No place in the record for the code read.** When the linked code is unrelated to the paper's analyses, there is no field for it (`inputs` is for data). I recorded the repository and commit in the notebook header and added a `methods_unavailable` finding.
6. **The suggested clock check confounds latency with offset.** Decoding peaks at +100 ms for every event, which reflects response latency. I reported the check as consistent with a shared clock, not as shown.
7. **Fixed seeds do not make the GPFA fits deterministic.** Values move in the third significant digit between runs (probably multithreaded numerics); counts and p values were unchanged over four runs. I noted this.
8. **Bug fixed after seeing outputs.** The Bayesian observer's optimiser left the offsets at 0 because its first step from a zero start is tiny. I fixed the optimiser after the first run without changing any criterion. The protocol does not say how to record such a fix; it is not in the attempt record.
9. **Ambiguous test in the paper.** The paper's test for the threshold claim (one-tailed, p = 1.5e-4) cannot be read unambiguously. I fixed my own criterion before the analysis and recorded it as a deviation.

### 4. Runtime and failures
- **Runtime.** The notebook takes about 400 s, of which GPFA is about 360 s.
- **Failures.** Europe PMC's full-text XML endpoint returned an HTTP 500, so I used the NCBI BioC API for the same manuscript. The first notebook run had the optimiser bug in point 8. Nothing else failed.
- **Untracked files not created by me.** `git status` shows `.bashrc`, `.gitconfig`, `scripts` and similar at the repo root. They are character devices from the sandbox, not files, and should not be committed.

Files are in the repository root:
- `claims/000130/10.1016-j.neuron.2019.06.012.yaml`
- `attempts/000130-sohn-2019-01.yaml`
- `entries/000130-sohn-2019/`
