# Brezovec, Berger, Druckmann & Clandinin (2022) from dandiset 000727

Tests the findings of [Brezovec et al. (2022)](https://doi.org/10.1101/2022.03.20.485047) that can be
tested on [DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), which holds the
whole-brain two-photon imaging and ball tracking of the paper's nine walking flies. The analysis uses
the authors' processed volumes, registered into the Functional Drosophila Atlas, and streams 12 of
their 91 planes.

| Claim | Outcome |
|---|---|
| Nine flies, 30,456 volumes at 1.8 Hz, 1.6M voxels, 50 Hz ball tracking | Reproduced |
| 39% of the brain correlates with velocity | Partially reproduced |
| 15% forward only, 20% forward and turning, 4% turning only | Partially reproduced |
| Forward correlations symmetric, turning anti-symmetric | Reproduced |
| PC1 tracks stop and go, PC2 forward velocity, PC3 turn direction | Reproduced |
| Velocity predicted from 100 PCs with R2 about 0.3 | Partially reproduced |
| Flies that move more are better predicted, R2 up to 0.6 | Partially reproduced |
| PC weights stereotyped across flies | Reproduced |
| Forward velocity uniquely encoded, walking state not | Partially reproduced |
| Velocity regions all active at movement onset | Reproduced |
| Turning raises ipsilateral and lowers contralateral activity | Not reproduced |
| Peak correlations from 300 ms before to over 1 s after behaviour | Reproduced |
| Lagging signals have broader kernels | Reproduced |
| Ipsilateral activity leads contralateral for turning | Reproduced |
| Region-level maps and sequences (Figures 2E to I, 3, 6E to G, 7) | Blocked: metadata insufficient |
| tdTomato motion control (Figure S2) | Blocked: data missing |
| Supervoxel number sweep (Figure S4A) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset has no neuropil labels, supervoxels or per-plane acquisition times, so the analysis
replaces supervoxels with 6 x 6 voxel blocks and samples behaviour at the middle of each volume. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000727-brezovec-2022-01.yaml`](../../attempts/000727-brezovec-2022-01.yaml).

- `reproduce_brezovec_2022.ipynb`: the analysis. It takes about eight minutes, most of it streaming
  22 GB of compressed planes.
- `brainwide.py`: loading the files (direct reads of the compressed chunks of the processed series),
  the behaviour variables of the paper's code, and the measures. Other notebooks on this dandiset can
  import it.
