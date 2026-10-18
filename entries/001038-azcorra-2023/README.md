# Azcorra, Gaertner et al. (2023) from dandiset 001038

Tests the findings of [Azcorra, Gaertner et al. (2023)](https://doi.org/10.1038/s41593-023-01401-9)
that can be tested on [DANDI:001038](https://dandiarchive.org/dandiset/001038/0.241111.1719), the fiber
photometry from striatal axons and SNc somas of Vglut2, Calb1, Anxa1, Aldh1a1 and DAT mice. Two
snRNA-seq claims of Figure 1 are tested on the paper's GEO deposit (GSE222558) and counted apart.

| Claim | Outcome |
|---|---|
| Locomotion recording counts (Figure 2) | Not reproduced |
| Reward and air puff recording counts (Figure 4) | Reproduced |
| Vglut2 and Calb1 signal after decelerations, Anxa1 after accelerations (Figure 2f) | Reproduced |
| Calb1 trough lag shorter than Vglut2 (Figure 2i) | Partially reproduced |
| PCA variance of the cross-correlations (Figure 2j,k) | Reproduced |
| PC1/PC2 angles separate the subtypes (Figure 2l) | Reproduced |
| Accelerations and decelerations per recording (Figure 2g) | Reproduced |
| Probability of a transient after an event (Extended Data Figure 7f) | Reproduced |
| Peak timing after decelerations (Extended Data Figure 6f) | Partially reproduced |
| Transients scale with event size (Figure 5a,b) | Partially reproduced |
| Vglut2, Calb1 and DAT reward responses (Figure 4g) | Partially reproduced |
| No Anxa1 reward response (Figure 4g) | Reproduced |
| Air puff responses (Figure 4g) | Partially reproduced |
| Vglut2 prefer air puffs, Calb1 rewards (Figure 4h) | Reproduced |
| Reward size sensitivity (Figure 4i) | Partially reproduced |
| Same reward response at rest (Extended Data Figure 8f) | Reproduced |
| k-means matches subtypes, 91% (Figure 6c) | Reproduced |
| Soma and axon correlation within subtypes (Figure 7f) | Reproduced |
| SNc somas respond like their axons (Extended Data Figure 9c) | Reproduced |
| Striatal PCs explain SNc variance (Extended Data Figure 9k) | Reproduced |
| Aldh1a1 signaling varies with depth (Extended Data Figure 1h) | Partially reproduced |
| Aldh1a1 reward response against locomotion signaling (Extended Data Figure 1i) | Reproduced |
| Calb1 and Anxa1 differ where their axons overlap (Figures 3a and 4l, two claims) | Reproduced |
| snRNA-seq nuclei after quality control (GEO) | Reproduced |
| Anxa1 within a subset of Aldh1a1 nuclei (GEO) | Reproduced |
| snRNA-seq clustering, scRNA-seq integration, histology (three claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001038-azcorra-2023-01.yaml`](../../attempts/001038-azcorra-2023-01.yaml).

- `reproduce_azcorra_2023.ipynb`: the analysis. It takes about three minutes, most of it streaming
  the files.
- `azcorra.py`: loading the files and a port of the paper's MATLAB selection and measures. Other
  notebooks on this dandiset can import it.
