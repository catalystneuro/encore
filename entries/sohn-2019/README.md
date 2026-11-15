# Sohn et al. (2019) from dandiset 000130

Tests the findings of [Sohn, Narain, Meirhaeghe and Jazayeri (2019)](https://doi.org/10.1016/j.neuron.2019.06.012)
that can be tested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), version
0.241017.1448. The dandiset was prepared for the Neural Latents Benchmark and holds one session
(2016-12-11) of monkey H in the Ready-Set-Go task: 1160 trials with their task variables and the spikes
of 54 units from dorsomedial frontal cortex, and 283 further trials whose task variables are withheld.
The paper pools 17 sessions of monkey H and 12 of monkey G.

`reproduce_sohn_2019.ipynb` holds the behavioural, single-neuron and trial-averaged population
analyses (about 1 minute); `gpfa_sohn_2019.ipynb` holds the single-trial GPFA analyses (about 16
minutes). Loading and measures are in `rsg.py`.

| Claim | Outcome |
|---|---|
| Behavioural slopes between 0 and 1 | Not reproduced (Eye Short slopes at or above 1) |
| Opposite biases at the overlapping 800 ms | Not reproduced |
| Smaller tp increments at the extremes of the prior | Reproduced |
| Smaller slopes for the Long prior | Reproduced, resting on an assumption |
| Bayesian observer fits bias and variance | Partially reproduced |
| GLM: 65% prior-dependent, 27% ts-dependent units | Not reproduced (79% and 46%) |
| Largest prior effect at 800 ms during the support of the prior | Reproduced |
| 3 to 4 and 5 to 10 principal components | Not reproduced |
| Encoding-axis projections match the Bayesian estimate (R2) | Reproduced |
| Bayesian model better than linear for projections | Partially reproduced |
| No sigmoidal representation in "Short In Long" | Reproduced (by the paper's test) |
| More neural bias for the Long prior | Partially reproduced |
| Projection at Set predicts speed | Partially reproduced (stronger correlations) |
| Initial speed biased toward the middle | Not reproduced (p = 0.055) |
| Speed predicts mean tp | Partially reproduced (stronger correlations) |
| Speed unmodulated during the support | Reproduced (by the paper's test) |
| Post-Set trajectories parallel | Reproduced |
| Distances fall steadily to Go | Not reproduced |
| Inverted-U variance of GPFA projections | Not reproduced (p = 0.055) |
| Sigmoidal mean of GPFA projections | Reproduced |
| Recurrent network claims (2) | Blocked: data missing |
| Monkey G | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

With one session, the population tests run over 4 effector and direction datasets in place of the
paper's 8, so no signed-rank test over datasets can fall below p = 0.125, and the three claims of
absence are reproduced by tests that cannot find an effect. In this session the eye responses are
nearly unbiased (slopes 0.85 to 1.11), which drives several of the behavioural outcomes.

Found about the dataset: the test file withholds the task variables of 283 of the session's 1443
trials; the `iti` description reverses the two priors; `tp` exceeds `go_time - set_time` by a median
of 17.9 ms without a description of how it is measured; units have no electrode assignment and no
single or multi-unit label.
