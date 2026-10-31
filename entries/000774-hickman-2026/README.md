# Hickman, Hughes, Sahai, Miles & Denman (2026) from dandiset 000774

Tests the findings of [Hickman et al. (2026)](https://doi.org/10.1016/j.celrep.2026.117420) that can
be tested on [DANDI:000774](https://dandiarchive.org/dandiset/000774/0.260520.1753), which holds the
units (spike times, templates, CCF coordinates and regions) and the electrical pulses of the acute
recordings with three Neuropixels probes around a stimulating electrode in mouse V1. The raw AP band
behind the evoked-potential figures (1 to 3) and the behaviour of Figure 7 are not in it. The three
claims that compare units with the evoked-potential boundaries are tested with the boundaries the
paper's code computed (an outside input their criteria name).

| Claim | Outcome |
|---|---|
| Latency trough at a median 1.95 ms sets the 2 ms direct window | Reproduced |
| GMM direct windows of 0.68 to 1.47 ms, same responder proportion as 2 ms | Reproduced |
| Responders mostly lie within the evoked potential (code's boundaries) | Partially reproduced (assumption) |
| Spatial extent of direct responders constant across amplitude | Reproduced |
| Responders lie closer to the contact at higher amplitude | Partially reproduced |
| 5 and 100 uA recruit distinct spatial populations | Not reproduced |
| Under 5% of units within the evoked potential respond, rising with amplitude (code's boundaries) | Reproduced |
| Direct response probability of the 99 responders rises with amplitude | Reproduced |
| Broader windows give more responders | Partially reproduced |
| Six amplitude clusters, dose-dependent or amplitude-selective | Reproduced |
| Polarity clusters: 69% of responders are polarity-specific | Reproduced |
| FS and RS responders equally sparse | Not reproduced |
| FS responders lie closer than RS responders | Reproduced (assumption) |
| FS responders lie within the evoked potential even at 5 uA (code's boundaries) | Partially reproduced (assumption) |
| FS and RS early firing differ at every amplitude | Reproduced (assumption) |
| Cortical modulation grows with amplitude, subcortical does not | Partially reproduced |
| Higher visual areas more modulated than subcortical units | Not reproduced |
| Over half of cortical units join the circuit response at high amplitude | Partially reproduced |
| No propagating wave | Reproduced (assumption) |
| Direct response slightly higher in high cortical state | Partially reproduced |
| Population dimensionality collapses after a pulse | Reproduced |
| Evoked potentials (Figures 1 to 3, S1, S2; 11 claims) | Blocked: data missing |
| Behaviour (Figure 7, S10; 10 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The stimulation contact coordinates of two recordings (jlh31, jlh32) in the dandiset differ from those
in the paper's code by 206 and 373 um; with the code's coordinates the distance results match the
paper exactly, and the one claim not reproduced on distances (5 against 100 uA) is reproduced. The
FS/RS claims rest on the classes the paper's code computes (a 0.4 ms duration threshold), where the
Methods describe k-means, whose classes change with its initialisation here. The no-propagating-wave
claim rests on the code's peak rule, which skips the 4 ms minimum width its configuration sets. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000774-hickman-2026-01.yaml`](../../attempts/000774-hickman-2026-01.yaml).

- `reproduce_hickman_2026.ipynb`: the analysis. It takes about 13 minutes, most of it the ZETA tests.
- `estim.py`: loading the files, the stability filter, waveform classes, distances, the code's
  evoked-potential boundaries, direct response probability, modulation index and ZETA. Other notebooks on this dandiset can import it.
