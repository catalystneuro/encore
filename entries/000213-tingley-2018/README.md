# Tingley & Buzsáki (2018) from dandiset 000213

Tests the findings of [Tingley and Buzsáki (2018)](https://doi.org/10.1016/j.neuron.2018.04.028)
that can be tested on [DANDI:000213](https://dandiarchive.org/dandiset/000213/0.250624.0438), which
holds 67 sessions of simultaneous hippocampal and lateral septum (LS) recordings from five rats.

| Claim | Outcome |
|---|---|
| 1,647 LS neurons in 62 sessions | Reproduced |
| 2,297 CA1 and 654 CA3 units | Partially reproduced |
| 840 LS neurons fire at least 1.5 spikes per trial | Reproduced |
| 89% of LS neurons code position in spike phase | Not reproduced |
| Phase beats rate in most neurons, conditions and all sessions | Not reproduced |
| Phase MSE below rate MSE across LS conditions and sessions | Reproduced |
| Mean phase minus rate MSE, LS and hippocampus | Partially reproduced |
| Rate and phase decoding equivalent for hippocampal place fields | Reproduced |
| 5.3% of LS and 31.7% of hippocampal rate maps have place fields | Not reproduced |
| Hippocampal place field counts, peak rates and widths | Partially reproduced |
| LS place fields less stable | Partially reproduced |
| Peak information at a smaller smoothing for phase than rate | Partially reproduced |
| Phase more informative at fine scales, rate at coarse ones | Partially reproduced |
| Phase coding grows with LS depth | Partially reproduced |
| Onset phase of LS phase fields varies with depth | Not reproduced |
| LS-CA3 theta coherence rises along the run | Not reproduced |
| Theta-gamma coupling rises along the run, stronger for CA3 | Reproduced |
| LS ensemble phases decode position better than hippocampal ensembles | Not reproduced |
| Hippocampal-LS gamma assemblies (three claims) | Blocked: not runnable |
| Speed and phase precession; information in bits/cm | Blocked: methods underspecified |
| Maze rotation (Figure S6) | Blocked: metadata insufficient |
| Spiking model (Figure 7) | Blocked: other |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's linearized behaviour, trial conditions and choice of CA1 channel are not in the
dandiset, so they are rebuilt here; several outcomes depend on those choices. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/000213-tingley-2018-01.yaml`](../../attempts/000213-tingley-2018-01.yaml).

- `reproduce_tingley_2018.ipynb`: the analysis. It takes about eight to ten minutes on four
  processes, streaming only the trials of each file.
- `lshpc.py`: loading, linearization, conditions, the per-cell decoder, place fields, information,
  and the LFP measures. Other notebooks on this dandiset can import it.
