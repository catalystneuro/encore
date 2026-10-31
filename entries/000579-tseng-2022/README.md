# Tseng, Chettih, Arlt, Barroso-Luque & Harvey (2022) from dandiset 000579

Tests the findings of [Tseng et al. (2022)](https://doi.org/10.1016/j.neuron.2022.05.012) that can be
tested on [DANDI:000579](https://dandiarchive.org/dandiset/000579/0.230728.1727), which holds 300
two-photon imaging sessions of 8 mice running a virtual Y-maze with rule switches, with the paper's
behavioural model outputs in each file.

| Claim | Outcome |
|---|---|
| Neuron counts (93,881 layer 2/3 neurons, 141 sessions, six areas) | Reproduced, on an assumption |
| Performance falls below chance after a switch and recovers | Reproduced |
| LSTM predicts held-out choices with 80.2% accuracy | Reproduced, on an assumption |
| LSTM beats the best RL model | Reproduced |
| Strategy variables around switches | Reproduced |
| Visually guided trials do not update rule belief more | Not reproduced, on an assumption |
| Photoinhibition (three claims) | Blocked: data missing |
| Running trajectories vary more after a switch | Reproduced |
| Dynamic choice crosses threshold sooner with higher rule- or bias-following | Reproduced, on an assumption |
| Choice commitment and strategy | Reproduced |
| Cue-biased running is unrelated to performance | Partially reproduced |
| RSC activity by trial epoch | Partially reproduced |
| GLM encoding analyses (24 claims) | Blocked: too large |
| Population decoders (5 claims) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The stored rule belief has the opposite sign to the paper's definition, and the paper's session
counts cannot be recovered from the files. The attempt record, with the reasons and the differences
from the paper's method, is
[`attempts/000579-tseng-2022-01.yaml`](../../attempts/000579-tseng-2022-01.yaml).

- `reproduce_tseng_2022.ipynb`: the analysis. It takes about ten minutes, most of it streaming the
  files and refitting the RL model.
- `tseng.py`: streaming and reducing each session, the hierarchical bootstrap, the block sigmoid fit
  and RL model 4. Other notebooks on this dandiset can import it.
