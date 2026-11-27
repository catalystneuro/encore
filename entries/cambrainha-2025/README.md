# Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025) from dandiset 000713

Tests the findings of [Cambrainha et al. (2025)](https://doi.org/10.1103/w49n-2vz8), "Criticality
at Work: Scaling in the Mouse Cortex Enhances Performance", on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual
Behavior Neuropixels data. For each 30-s window of V1 spiking it computes the kurtosis after
momentum-space coarse graining and an ISI-shuffled surrogate, relates it to the hit rate of the
change-detection task, compares the active, passive and non-natural image phases, and fits the
real-space renormalization exponents.

| Claim | Outcome |
|---|---|
| 62 sessions (44 mice) have more than 128 V1 units | Not reproduced |
| Kurtosis spans a broad range above the surrogates, lowest surrogates around 6 | Partially reproduced (assumed) |
| Hit rate over scaling windows is higher than over no-scaling windows and the shuffle | Blocked: methods underspecified |
| Hit rate over scaling windows rises with the threshold | Blocked: methods underspecified |
| Relative performance gain reaches 24% | Not reproduced |
| Similar results with 10-s and 60-s windows | Not reproduced |
| Similar results with strictly sorted units (43 sessions) | Not reproduced (assumed) |
| More windows above threshold in active than passive than non-natural images | Blocked: methods underspecified |
| Exponents of the active phase | Not reproduced |
| Exponents of the passive phase, and their differences from active | Not reproduced |
| Exponents with non-natural images, and their differences | Not reproduced |
| Static exponents approach trivial values from active to passive to non-natural | Partially reproduced |
| Exponents stable with the kurtosis threshold | Blocked: methods underspecified |
| Kurtosis before coarse graining is a poor predictor of kurtosis after | Reproduced |
| Firing rate ordered active < non-natural < passive and falls with the threshold | Reproduced (assumed) |
| Hit rate below a firing-rate threshold is not monotonic | Reproduced |
| Relation between kurtosis and performance holds in both halves of the active phase | Not reproduced (assumed) |
| Second half has lower kurtosis, non-natural images the lowest | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper links no code. Computed as its equations describe, the surrogate kurtoses here are around
3.6, where the paper reports surrogate kurtoses of 6 or more and a surrogate maximum of about 7, so
the paper's kurtosis scale is not reached. The surrogate maximum here is set by a few windows
(34.29), which leaves the threshold ranges of five claims empty; they are blocked, with every
reading shown in the notebook. Over the whole range of thresholds the hit rate over high-kurtosis
windows is below that over low-kurtosis windows, and the non-natural image phase has the highest
kurtosis. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/cambrainha-2025-01.yaml`](../../attempts/cambrainha-2025-01.yaml).
