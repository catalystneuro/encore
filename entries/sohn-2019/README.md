# Sohn, Narain, Meirhaeghe & Jazayeri (2019) from dandiset 000130

Tests the findings of [Sohn et al. (2019)](https://doi.org/10.1016/j.neuron.2019.06.012) that can be
tested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), which holds one
session of monkey H (2016-12-11) in the Ready-Set-Go task with two priors of the sample interval:
54 units of dorsomedial frontal cortex and 1160 trials, prepared for the Neural Latents Benchmark.
The paper analyses 29 sessions of two monkeys; monkey G and the paper's recurrent networks are not
in the dandiset.

| Claim | Outcome |
|---|---|
| Regression slopes of tp on ts lie between 0 and 1 | Not reproduced |
| Biases in opposite directions at the overlapping ts | Not reproduced |
| tp increments smaller at the extremes of the prior | Reproduced |
| Larger biases (smaller slopes) for the Long prior | Reproduced, on an assumption |
| Bayesian observer captures bias and variance | Partially reproduced |
| GLM: 65% prior-dependent and 27% ts-dependent units | Not reproduced |
| Prior difference at ts = 800 largest in the support | Reproduced |
| 3 to 4 and 5 to 10 PCs explain 75% of the variance | Not reproduced |
| Projections on the encoding axis match the Bayesian estimate (R2) | Reproduced |
| Bayesian model better than linear for the projections | Partially reproduced |
| No sigmoidal representation in "Short In Long" | Reproduced |
| Smaller neural slope for the Long prior | Partially reproduced |
| Projection at Set predicts production speed | Partially reproduced |
| Initial speed biased toward the middle of the prior | Not reproduced |
| Production speed predicts mean tp | Partially reproduced |
| Speed unmodulated during the support (H1) | Reproduced |
| Parallel trajectories after Set (H2) | Reproduced |
| Distances fall steadily to Go (H3) | Not reproduced |
| Inverted-U variance of single-trial GPFA projections | Not reproduced |
| Sigmoidal mean of single-trial GPFA projections | Reproduced |
| Recurrent network claims (two) and monkey G | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every analysis here uses one session with 48 selected units, where the paper pools 17 sessions
of monkey H and 12 of monkey G. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/sohn-2019-02.yaml`](../../attempts/sohn-2019-02.yaml).

- `reproduce_sohn_2019.ipynb`: behaviour, the Bayesian model, the GLM, PCA, encoding axis, speed
  and the alternative mechanisms. It takes about a minute.
- `gpfa_sohn_2019.ipynb`: the single-trial GPFA analysis (Elephant's GPFA). It takes about sixteen
  minutes.
- `rsg.py`: loading the files, unit and trial selection, rates, PCA, the encoding axis and the
  Bayesian observer model. Other notebooks on this dandiset can import it.
