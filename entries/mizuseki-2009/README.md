# Mizuseki, Sirota, Pastalkova & Buzsaki (2009) on CRCNS hc-2

Tests the findings of [Mizuseki et al. (2009)](https://doi.org/10.1016/j.neuron.2009.08.037) that
can be tested on [CRCNS hc-2](https://doi.org/10.6080/K0Z60KZ9), which holds 21 open-field
sessions of CA1 recordings from three rats (ec13, ec14, ec16). The entorhinal, CA3 and dentate
recordings, the other tasks and two of the five rats of the paper are not in it, so the claims
are tested on CA1 alone, with theta referred to the CA1 pyramidal layer in place of EC3.

| Claim | Outcome |
|---|---|
| CA1 pyramidal cells: mean R 0.19, 84% theta modulated (Figure 3D) | Partially reproduced (assumed) |
| CA1 cells least active on the ascending theta phase | Reproduced (assumed) |
| Preferred phases agree across three phase methods | Reproduced (assumed) |
| CA1 pyramidal cells advance with firing rate | Partially reproduced (assumed) |
| Burst spikes share the phase of fast spikes, with a double peak | Partially reproduced (assumed) |
| Interneuron phase changes little with rate (< 30 degrees) | Not reproduced (assumed) |
| Burst and single spikes differ in phase in many CA1 cells | Reproduced (assumed) |
| Most CA1 spikes are at low rates | Reproduced (assumed) |
| Phase preferences consistent across rats | Reproduced (assumed) |
| Pair time offsets agree with phase differences | Partially reproduced (assumed) |
| Ripple-triggered increases, CA1 about 6-fold and 3-fold | Not reproduced (assumed) |
| Table S1 cell counts | Blocked: data missing |
| 25 claims on EC, CA3, DG, other tasks and outside CSD data | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most outcomes rest on assumptions the paper leaves open: the theta-epoch thresholds, the rule
separating CA1 pyramidal cells from interneurons (hc-2 has no cell-type labels) and the choice
of the pyramidal layer channel. The notebook shows the results under variants of each. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/mizuseki-2009-01.yaml`](../../attempts/mizuseki-2009-01.yaml).

- `reproduce_mizuseki_2009.ipynb`: the analysis. It takes about ten minutes, most of it streaming
  the 21 session tarballs (about 22 GB) from the CRCNS bucket.
- `hc2.py`: streaming and reducing an hc-2 session, theta epochs and phase, circular statistics,
  instantaneous rate and burst groups, waveform features, cell types and ripple detection. Other
  notebooks on hc-2 can import it.
