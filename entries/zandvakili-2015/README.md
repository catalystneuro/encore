# Zandvakili & Kohn (2015) from CRCNS v1v2-1

Tests the findings of [Zandvakili and Kohn (2015)](https://doi.org/10.1016/j.neuron.2015.07.026)
that can be tested on [CRCNS v1v2-1](https://doi.org/10.6080/K0B27SHN), which holds V1 Utah array
and V2 tetrode spike times from 5 sessions in 3 anesthetized macaques viewing drifting gratings. It
has no V2 depths, unit SNR or pixel-to-degree scale, so the laminar, single-unit and receptive field
claims cannot be tested, and the paper's simulations were not run.

| Claim | Outcome |
|---|---|
| Broad V1-V2 CCG peaks at all sites | Reproduced |
| Narrow site-average peak at a minority of V2 sites (46 of 223) | Not reproduced (16 of 31) |
| Depth of narrow-peak sites (694 um) | Blocked: data missing |
| Narrow peaks in 0.3% of V1-V2 pairs | Not reproduced (1.05%) |
| V1-V2 peaks offset by a median of 2.8 ms, width 3.71 ms | Partially reproduced (2.0 ms, 3.89 ms) |
| V1-V1 and V2-V2 peaks at zero lag | Not reproduced, resting on an assumption |
| Efficacy, median 0.39% | Not reproduced (0.32%) |
| V1 divergence higher before middle-layer V2 spikes than in control epochs | Reproduced |
| About 3-fold higher | Partially reproduced (about 1.9-fold) |
| Divergence above shuffled data | Reproduced |
| No elevation after V2 spikes (5 to 80 ms) | Not reproduced (elevated at 80 ms) |
| Elevation before and after at 1280 ms | Reproduced |
| Time course peaks a few ms before V2 spikes | Partially reproduced |
| Elevation with and without a V1 partner | Reproduced |
| RF alignment and RF sizes | Blocked: metadata insufficient |
| Non-middle-layer, offset-RF, single-unit and V2 relay analyses (seven claims) | Blocked: data missing |
| Simulations (four claims) | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold spike times in 1 ms bins, where the paper used 0.1 ms. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/zandvakili-2015-01.yaml`](../../attempts/zandvakili-2015-01.yaml).

- `reproduce_zandvakili_2015.ipynb`: the analysis. It takes about 13 minutes, most of it the
  cross-correlograms and the jittered V1 populations.
- `v1v2.py`: loading the sessions from the zip in place, CCGs with shuffle and jitter correction,
  and the divergence of V1 population states around V2 spikes. Other notebooks on this data set
  can import it.
