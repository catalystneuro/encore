# Vu, Brown, Wen et al. (2024) from dandiset 001084

Tests the findings of [Vu et al. (2024)](https://doi.org/10.1016/j.neuron.2023.12.011) that can be
tested on [DANDI:001084](https://dandiarchive.org/dandiset/001084/0.241023.2011), which holds
multi-fiber photometry from 16 mice: dopamine release to light and tone in 280 striatal fibers of 7
mice, chronic reward responses, D1 calcium signals with isosbestic controls, and single-fiber
optogenetic stimulation with its controls. The freely moving, histology and jaw movement data of
Figures 3, 7 and S1 are not in it.

| Claim | Outcome |
|---|---|
| D1 calcium transients at 470 nm, absent at 405 nm (Figure 1C) | Reproduced |
| Pairwise correlations low and falling with distance (Figure S2D) | Reproduced |
| No crosstalk between neighbouring fibers on the bundle (Figure S2E-F) | Reproduced |
| Reward responses stable over 12 weeks (Figure 1D) | Partially reproduced (weeks 5 to 8 testable) |
| The dandiset holds the data of the paper's per-fiber results (with Zenodo inputs) | Reproduced |
| Light evokes increases at many striatal sites (Figure 4E) | Reproduced |
| Light amplitude gradient, weaker and rarer increases in the tail (Figure 4E) | Partially reproduced |
| Tone: increases in the tail, decreases anterior to it (Figure 4F) | Reproduced |
| Tone decreases more lateral and ventral (Figure 4F) | Partially reproduced |
| Patterns consistent across mice (Figure S4A, C) | Partially reproduced |
| Patterns not driven by movement (Figure S4) | Partially reproduced |
| No pattern under isosbestic excitation (Figure S5E-H) | Partially reproduced |
| Latencies to half maximum (Figure 5A-B) | Partially reproduced |
| Light latencies faster anteriorly (Figure 5G) | Reproduced |
| Tone latencies faster posteriorly (Figure 5H) | Reproduced |
| Latency gradients in individual mice (Figure S6C-D) | Partially reproduced |
| Inclusion counts of the stimulation experiment (Figure 6) | Partially reproduced |
| Evoked release decays with distance (Figure 6G-H) | Reproduced |
| Slower decay dorsally than ventrally (Figure 6G) | Partially reproduced |
| No response in tdTomato controls (Figure 6) | Reproduced |
| Photoswitching confined to the stimulated fiber (Figure S7A) | Reproduced |
| Targeting errors (Figure S3): planned targets not public | Blocked: data missing |
| Figures 3, 7 and S1 (four claims, data only on Zenodo) | Blocked: not attempted |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The DF/F traces, fiber order and stimulus times in the files are exactly those behind the paper's
results. The files do not hold the stimulation times or the stimulated fiber of the optogenetic
sessions (found here from the laser artefact in the DF/F, as the paper's code does), the frequency of
DL18's tones, the planned fiber targets of Figure S3, or the task variables that separate unpredicted rewards in DL15's later sessions. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001084-vu-2024-01.yaml`](../../attempts/001084-vu-2024-01.yaml).

- `reproduce_vu_2024.ipynb`: the analysis. It takes about 14 minutes, most of it the 10000 null refits
  of the GLM for each mouse and streaming the files.
- `vu2024.py`: loading the files, overall velocity, the salient-stimulus GLM and its null, the
  half-maximum latency, and the stimulation response test. Other notebooks on this dandiset can import
  it.
