# Fujisawa, Amarasingham, Harrison & Buzsáki (2008) from dandiset 000067

Tests the findings of [Fujisawa et al. (2008)](https://doi.org/10.1038/nn.2134) that can be tested
on [DANDI:000067](https://dandiarchive.org/dandiset/000067/0.250624.0419), which holds recordings
of three rats from a 64-site prefrontal probe and a 32-site CA1 probe during an odor-place
matching task. The paper's fourth rat and its example session (EE.188) are not in it.

| Claim | Outcome |
|---|---|
| The channels can be mapped to the probes and sensors with the CRCNS description | Partially reproduced |
| 633 mPFC units from four rats | Not reproduced |
| Task performance of 92% correct | Blocked: data missing |
| About 10% (layer 2/3) and 20% (layer 5) of neurons active per 100 ms, constant along the maze | Not reproduced |
| Field sizes of 0.27 plus or minus 0.17 of the track | Partially reproduced |
| Trajectory-selective neurons in the central and side arms | Partially reproduced |
| Trajectories diverge at position 0.3 | Blocked: data missing |
| About a quarter of neurons respond differently to the two odors | Partially reproduced |
| 0.79% of pairs connected (0.55% excitatory, 0.24% inhibitory) | Partially reproduced |
| 32.5% pyramidal cells and 12.5% interneurons by their connections | Not reproduced |
| Connection probability falls with distance | Not reproduced |
| 67 of 343 excitatory pairs depend on position | Not reproduced |
| 12.7% depressing and 10.7% facilitating pairs | Not reproduced |
| Supralinear effect of coincident presynaptic spikes | Not reproduced |
| Most pyramidal cells and interneurons are trajectory specific | Not reproduced |
| Values of the example session (Figures 2a, 3b to 3d, 4 to 7) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The units table holds spike times only, so each unit is placed on a probe from its mean waveform
in the wideband signal, and the probes are named with the channel map of the CRCNS pfc-2
description of the same recordings, which the data confirm for two rats and correct for the
third. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000067-fujisawa-2008-01.yaml`](../../attempts/000067-fujisawa-2008-01.yaml).

- `reproduce_fujisawa_2008.ipynb`: the analysis. It takes about ten minutes, most of it streaming
  the files.
- `pfc.py`: loading, the placement of units on the probes, and the measures: rate maps, the
  permutation test of left against right, the jitter test for monosynaptic connections, the
  position dependence of coincidences, first against later spikes, and coincident inputs. Other
  notebooks on this dandiset can import it.
