# Siegle, Jia et al. (2021) for dandiset 000253

Tests the findings of [Siegle, Jia et al. (2021)](https://doi.org/10.1038/s41586-020-03171-x) for
[DANDI:000253](https://dandiarchive.org/dandiset/000253/0.240923.1441), which names the paper but
holds a different experiment, the OpenScope Global/Local Oddball project. The paper's own passive
viewing recordings are in [DANDI:000021](https://dandiarchive.org/dandiset/000021/0.251116.2246) and
[DANDI:000022](https://dandiarchive.org/dandiset/000022/0.251116.2247), which its Data availability
names, so the claims are tested there. The behaviour claims of Figure 4 use the metrics tables of
the paper's GitHub repository.

| Claim | Outcome |
|---|---|
| 58 sessions by genotype; 284 of 332 probes in the CCF; units per experiment, probe and area | Reproduced |
| 60% of visual area units with a receptive field, 1.4% in the hippocampus | Partially reproduced (60.8%, 1.6%) |
| The paper's per-unit tables link to the dandisets' units (added link) | Partially reproduced (latencies differ) |
| Latency, RF size, modulation index and decay timescale follow the hierarchy (Fig. 3c, f, i, l) | Reproduced |
| Pairwise area differences: latency, RF size | Partially reproduced |
| Pairwise area differences: modulation index, decay timescale | Not reproduced |
| Figure 3 unit counts | Reproduced with the code's windows (assumption) |
| Intrinsic timescale, firing rate and spontaneous latency do not follow the hierarchy | Reproduced |
| Superficial and deep layers differ in the four metrics | Partially reproduced (3 of 4) |
| Anatomical hierarchy order | Reproduced |
| Behaviour metrics: latency, change modulation, decoders (Fig. 4e to h, Extended Data Fig. 9k to p) | Reproduced |
| Behavioural performance (Fig. 4b) | Blocked: data missing |
| Gaze stability | Reproduced |
| Sharp CCG peaks, V1 leads LM, DS correlates with hierarchy, THS, superficial leads deep | Reproduced |
| Neighbouring areas differ from within-area offsets; V1 leads, AM follows | Partially reproduced |
| Hierarchy absent in spontaneous activity | Not reproduced |
| Distance does not explain the DS correlation | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/000253-siegle-2021-01.yaml`](../../attempts/000253-siegle-2021-01.yaml).

- `reproduce_siegle_2021.ipynb`: everything but the CCGs. About 12 minutes, most of it streaming the
  spike times of about 70,000 units from 58 sessions.
- `ccg_siegle_2021.ipynb`: the jitter-corrected cross-correlograms of the 26 Functional
  Connectivity sessions. About 18 minutes.
- `siegle.py`: loading, the per-unit measures (receptive field test and area, times to first spike,
  modulation index, timescales) and the CCGs, with the source of every parameter in its docstring.
