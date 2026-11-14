# Sohn, Narain, Meirhaeghe & Jazayeri (2019) from dandiset 000130

Tests the findings of [Sohn et al. (2019)](https://doi.org/10.1016/j.neuron.2019.06.012) that can be
tested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), which holds one
recording session (2016-12-11) of monkey H in the two-prior Ready-Set-Go task, prepared for the Neural
Latents Benchmark: 1160 trials with their task variables and 54 units in DMFC. The paper used 17
sessions of monkey H and 12 of monkey G; only this session is here.

| Claim | Outcome |
|---|---|
| Regression slopes of tp on ts between 0 and 1 in every condition | Not reproduced |
| Opposite biases of the two priors at ts = 800 ms | Not reproduced |
| tp increments smaller at the extremes of the prior | Reproduced |
| Smaller slopes for the Long prior | Reproduced |
| The Bayesian observer captures bias and variance | Partially reproduced |
| GLM: 65% of units prior-dependent, 27% ts-dependent | Not reproduced |
| Prior difference at ts = 800 ms largest during the support | Reproduced |
| 3 to 4 and 5 to 10 PCs explain 75% of the variance | Not reproduced |
| Projections on the encoding axis match the Bayesian estimate (R2) | Reproduced |
| Projections fit the Bayesian model better than a linear one | Not reproduced |
| No sigmoid in the "Short In Long" control | Reproduced |
| Smaller neural slope for the Long prior | Reproduced |
| Projection at Set predicts production speed | Partially reproduced |
| Initial speed biased toward the middle of the prior | Reproduced |
| Production speed predicts tp | Partially reproduced |
| Speed unmodulated during the support (H1) | Reproduced |
| Trajectories parallel after Set (H2) | Reproduced |
| Distances decrease up to Go (H3) | Not reproduced |
| GPFA variance has an inverted-U profile | Not reproduced |
| GPFA mean projection sigmoidal, steeper for Short | Reproduced |
| Recurrent network results (two claims) | Blocked: data missing |
| Monkey G | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every test over datasets has the 4 effector and direction conditions of this session, where the paper
has 8 over two animals and pools 17 sessions of monkey H for its behavioural statistics. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/sohn-2019-02.yaml`](../../attempts/sohn-2019-02.yaml).

- `reproduce_sohn_2019.ipynb`: the analysis. It takes about 13 minutes, most of it the GPFA fits.
- `rsg.py`: loading the files, unit selection, binned and trial-averaged rates, PCA, the encoding
  axis and the Bayesian observer model. Other notebooks on this dandiset can import it.
