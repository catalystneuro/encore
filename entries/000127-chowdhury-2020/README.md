# Chowdhury, Glaser & Miller (2020) from dandiset 000127

Tests the findings of [Chowdhury et al. (2020)](https://doi.org/10.7554/eLife.48198) that can
be tested on [DANDI:000127](https://dandiarchive.org/dandiset/000127/0.220113.0359), which holds
one session of the paper's active/passive experiment.

| Claim | Outcome |
|---|---|
| Figures 4 to 7: the two-workspace experiment (four claims) | Blocked: data missing |
| Hand speed is similar in active and passive trials in the first 120 ms | Reproduced |
| Whole-arm kinematics tell active from passive trials | Reproduced |
| Many neurons tell active from passive trials above chance | Reproduced |
| The whole-arm model tends to beat the hand-only model, with many ties | Reproduced |
| Many neurons are fit poorly by one model across both conditions | Partially reproduced |
| The better a neuron separates the conditions, the worse one model fits it | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The whole-arm model here uses joint angles in place of the paper's arm markers, which are not
in the dandiset. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000127-chowdhury-2020-01.yaml`](../../attempts/000127-chowdhury-2020-01.yaml).

- `reproduce_chowdhury_2020.ipynb`: the analysis. It takes about four minutes.
- `area2.py`: loading the session, and the separability, model-fitting and cross-validation
  routines. Other notebooks on this dandiset can import it.
