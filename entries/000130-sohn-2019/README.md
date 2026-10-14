# Sohn, Narain, Meirhaeghe & Jazayeri (2019) from dandiset 000130

Tests the findings of [Sohn et al. (2019)](https://doi.org/10.1016/j.neuron.2019.06.012) that can
be tested on [DANDI:000130](https://dandiarchive.org/dandiset/000130/0.241017.1448), the Neural
Latents Benchmark's DMFC_RSG set. It holds one recording session of monkey H in the Ready-Set-Go
task, with 54 units from dorsomedial frontal cortex. The paper uses 17 sessions of monkey H and 12
of monkey G; monkey G and the recurrent network models are not in the dandiset.

| Claim | Outcome |
|---|---|
| Slopes of tp on ts between 0 and 1 in every condition | Not reproduced |
| Opposite biases of the two priors at ts = 800 ms | Not reproduced |
| Smaller tp increments at the extremes of the prior | Reproduced |
| Smaller slopes for the Long prior | Reproduced |
| The Bayesian observer captures bias and variance | Partially reproduced |
| 65% of units prior-dependent and 27% ts-dependent | Not reproduced |
| Prior difference at 800 ms largest during the support | Reproduced |
| 3 to 4 and 5 to 10 PCs explain 75% of the variance | Not reproduced |
| Projections on the encoding axis match the Bayesian estimate | Reproduced |
| Bayesian model better than linear for the projections | Partially reproduced |
| No sigmoid in the Long prior's matched period | Reproduced (the test cannot detect an effect with 4 datasets) |
| Smaller neural slope for the Long prior | Reproduced |
| Larger projection at Set, slower trajectory | Partially reproduced |
| Initial speed biased toward the mean | Reproduced |
| Speed predicts tp | Partially reproduced |
| Speed unmodulated during the support | Reproduced (the test cannot detect an effect; the speed rises in all 8) |
| Parallel trajectories after Set | Not reproduced |
| Distances fall steadily up to Go | Not reproduced |
| Inverted-U variance of single-trial projections | Not reproduced |
| Sigmoidal mean of single-trial projections | Reproduced |
| Recurrent network models (two claims) | Blocked |
| The results hold in monkey G | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000130-sohn-2019-01.yaml`](../../attempts/000130-sohn-2019-01.yaml).

- `reproduce_sohn_2019.ipynb`: the analysis. It takes about seven minutes, most of it fitting GPFA.
- `rsg.py`: loading the files, unit selection, population rates with attrition, PCA, the encoding
  axis, the Bayesian observer and the GPFA fits. Other notebooks on this dandiset can import it.
