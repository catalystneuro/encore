# Masset, Tano, Kim, Malik, Pouget & Uchida (2025) from dandiset 000251

Tests the findings of [Masset et al. (2025)](https://doi.org/10.1038/s41586-025-08929-9) on
[DANDI:000251](https://dandiarchive.org/dandiset/000251/draft), which holds the VR task single units
of Kim et al. (2020) that the paper reuses, and on the paper's own Mendeley deposit
([doi:10.17632/tc43t3s7c5.1](https://doi.org/10.17632/tc43t3s7c5.1)), which holds the cued delay
task units the dandiset lacks. The dandiset has no published version; the draft is used.

| Claim | Outcome |
|---|---|
| The units of both tasks link to the paper's per-neuron table (added check) | Reproduced |
| 78 neurons recorded in the cued delay task, 50 selected | Not reproduced (67 deposited, 43 selected) |
| Trials and sessions per task | Reproduced |
| Anticipatory licking starts later for longer delays | Reproduced |
| Mean cue response falls with delay | Reproduced |
| Exponential fits better than hyperbolic | Reproduced |
| Cued delay discount factors 0.56 +- 0.21 | Reproduced |
| Fit parameters agree between halves of the trials | Partially reproduced |
| Reward timing decoded better than shuffle | Reproduced |
| Better than a single-discount decoder | Partially reproduced |
| Exponential matrix decodes better than hyperbolic | Reproduced |
| Lick and neural discount factors uncorrelated | Reproduced |
| Decoding in single mice | Partially reproduced |
| Decoding as good as from simulated responses | Not reproduced |
| VR ramp slopes (Fig. 3b) | Partially reproduced |
| Common value function fit, discount factors 0.42 +- 0.23 | Reproduced |
| Slope and discount factor correlated (r = 0.81) | Partially reproduced |
| No relation of VR parameters to ML position | Reproduced |
| VR licking unrelated to discount factor | Reproduced |
| Single-mouse VR fits agree with the population fit | Partially reproduced |
| Discount factors correlated across tasks (r = 0.45) | Reproduced |
| Bootstrap correlations across tasks (0.34 +- 0.104) | Reproduced |
| Decoding with the VR discount factors | Partially reproduced |
| Common reward expectation model agrees | Blocked: too large |
| Simulations of Fig. 1 and Extended Data Figs 1 and 2 (four claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In the dandiset, 78 open-loop units are deposited twice under different session numbers, and one
open-loop file holds a teleport session. The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/masset-2025-01.yaml`](../../attempts/masset-2025-01.yaml).

- `vr_population.ipynb`: the VR claims on the population (about 25 minutes, most of it fitting).
- `vr_single_mouse.ipynb`: the single-mouse VR fits (about 32 minutes).
- `cued_delay_and_cross_task.ipynb`: the link, the cued delay claims and the cross-task claims
  (about 11 minutes).
- `multiscale.py`: loading both sources, the link to the paper's table, the PSTHs, the common
  value model fit, the cued delay fits and the decoder.
