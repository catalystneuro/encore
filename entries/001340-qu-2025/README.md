# Qü et al. (2025) from dandiset 001340

Tests the findings of [Qü et al. (2025)](https://doi.org/10.1371/journal.pcbi.1013226) on
[DANDI:001340](https://dandiarchive.org/dandiset/001340/0.250221.0527), which holds the trial
tables of 5 mice over 69 sessions of a two-armed bandit task and raw dLight photometry (470 and
415 nm) from nucleus accumbens core in 48 of them.

| Claim | Outcome |
|---|---|
| Composition of the data (5 mice, 14 sessions each) | Partially reproduced |
| Behaviour: performance, its increase over sessions, trials to switch and to commit, their decrease, stay after omissions, decaying history weights (7 claims) | Reproduced |
| Model comparison by AIC: Bayesian and complex RL models beat RL4p, RLCF in between, no difference between the two families | Reproduced |
| Model identification | Reproduced |
| Parameter recovery (BRLfwr good, RL_meta poor) | Partially reproduced |
| BRLfw alpha is zero; RL4p learning rates; adaptation after a switch; switch rates after mixed contexts; AIC around switches | Reproduced |
| Errors against three-trial switch probabilities | Partially reproduced |
| No change of model fitness across sessions | Not reproduced |
| BRLwrp does not differ from BRLfwr | Not reproduced |
| Outcome dopamine: switch effect, no laterality effect, reward-switch-reward count | Reproduced (assumption) |
| Outcome dopamine: reward and omission estimates, port duration, cleaned trial counts | Partially reproduced (assumption) |
| Dopamine and model RPEs: Bayesian RPEs fit best (Fig 4F) | Partially reproduced (assumption) |
| Other metrics, reward history decrease, non-negative RPE on AAA, mixed models, model R_unchosen effects, per-animal results, feature sets | Reproduced (most with the assumption) |
| Consistency after a reward; RPE-only regressions | Partially reproduced and not reproduced (assumption) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not mark the paper's 34 sessions with valid dopamine. The dopamine claims use the 38
sessions in which outcome dopamine responds to reward (an assumption, recorded in the attempt); the
other 8, all from one mouse, show no response at any clock offset. The paper's cognitive models are
re-implemented from its code (cogmodels at commit 589555c) and checked against that code's own
likelihood. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001340-qu-2025-01.yaml`](../../attempts/001340-qu-2025-01.yaml).

- `reproduce_qu_2025.ipynb`: the analysis. It takes about ten minutes: two to stream the files and
  preprocess the photometry, four for the model identification simulations.
- `qu2025.py`: loading, behavioural measures, the cognitive models (fitting, simulation, RPEs) and
  the photometry preprocessing. Other notebooks on this dandiset can import it.
