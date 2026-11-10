# Kondo, Sehara, Harukuni, Aoki et al. (2025) from dandiset 001425

Tests the findings of [Kondo et al. (2025)](https://doi.org/10.1101/2025.02.03.631599) on
[DANDI:001425](https://dandiarchive.org/dandiset/001425/0.250705.0947), the BraiDyn-BC lever-pull
dataset: wide-field calcium imaging (44 Allen CCF ROIs), behavioural sensors and video keypoints from
25 mice over 15 task sessions, with resting-state and sensory-mapping sessions.

| Claim | Outcome |
|---|---|
| 25 mice, 11 male and 14 female, 17 to 31 weeks old | Reproduced |
| 364 of 375 task sessions, all 15 for 16 mice | Reproduced |
| 54000, 18000 and 27000 frames per channel by session type | Reproduced |
| Training breaks and the length of the recording period | Reproduced |
| Response rate rises from about 0.55 to about 0.85 | Reproduced |
| Success rate roughly constant | Blocked: methods underspecified |
| Ward clustering of T_pull_final gives clusters of 7 and 18 | Reproduced |
| Cluster A: high early success, high late T_pull_final | Reproduced |
| Cluster B: rarely high T_pull_final, similar late rates | Blocked: methods underspecified |
| No fluorescence degradation across sessions | Reproduced |
| MesoNet landmarks agree with manual annotations | Blocked: data missing |
| Visual, tactile and auditory sensory maps | Reproduced (three claims; the auditory one with little evidence) |
| No aberrant short, large transients | Reproduced |
| DeepLabCut error against manual annotations | Blocked: data missing |
| Lever-tip keypoint correlates with the lever, R 0.98 | Reproduced |
| Right forepaw correlates with the lever, the left does not | Partially reproduced |
| Figure 6b example session: movement order, pupil tracking | Blocked: methods underspecified (two claims) |
| Figure 6b: MOs against MOp and SSp after reward; lower variability after onset | Reproduced (two claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/kondo-2025-01.yaml`](../../attempts/kondo-2025-01.yaml).

- `reproduce_kondo_2025.ipynb`: the analysis. It streams about 400 NWB files, reading only the
  arrays it needs, and every frame of four task sessions, and takes about 25 minutes with 8 worker
  processes.
- `bdbc.py`: listing and streaming the files, and the per-session measures (trial outcomes and
  rates, lever and keypoint correlations, pull-aligned averages, sensory responses). Other notebooks
  on this dandiset can import it.
