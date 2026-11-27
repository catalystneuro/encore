# Dvali, Seguin, Betzel & Leifer (2025) from dandiset 001075

Tests the findings of [Dvali et al. (2025)](https://doi.org/10.1103/6wgv-b9m6) that can be tested
on [DANDI:001075](https://dandiarchive.org/dandiset/001075/0.240920.1434), the signal propagation
atlas of Randi et al. (2023), at the version the paper cites. The dandiset holds the calcium
recordings, labels and stimulations, not the network. The q-values that define the network need
control recordings that are not in it, so the signaling network is taken from the atlas released
with Randi et al. (2023) and a link claim tests it against the recordings. The anatomical network
comes from the EM connectomes stored with Randi et al.'s code.

| Claim | Outcome |
|---|---|
| The released atlas matches the dandiset's recordings (link) | Partially reproduced |
| The signaling network has 1151 edges, density 0.033 | Reproduced |
| Signaling clustering 0.13, small-world coefficient 4.76 | Reproduced |
| Anatomical network: 3250 edges, density 0.092, clustering 0.3, sigma 2.52 | Reproduced (assumed) |
| The two networks differ in their triad motifs | Reproduced |
| Signaling is not feed-forward along the sensory, inter, motor path | Reproduced |
| Anatomy is feed-forward along that path | Partially reproduced |
| Pharyngeal neurons broadcast, amphid neurons integrate | Partially reproduced |
| Pharynx not stimulated more, amphid not observed more | Reproduced |
| Dual rich club of 16 and 5 neurons | Partially reproduced |
| The rich clubs share only AVEL and AVER | Reproduced |
| Signaling and anatomical degree correlate with r = 0.22 | Reproduced (assumed) |
| The signaling rich club spans all classes, the anatomical one is interneurons | Reproduced |
| Degree correlates with observations (r = 0.71), rich club well above | Partially reproduced |
| AVE is the most connected in both networks | Reproduced (assumed) |
| Threshold controls at q < 0.01 and q <= 0.18 (three claims) | Blocked: data missing (one rich club pair holds) |
| Stochastic block model communities and what rests on them (21 claims) | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/dvali-2025-01.yaml`](../../attempts/dvali-2025-01.yaml).

- `reproduce_dvali_2025.ipynb`: the analysis. It takes about eight minutes, most of it streaming
  the 110 segmentation files of the cited version and the stimulated-ROI ids of the next one.
- `networks.py`: loading the files, the atlas and the connectomes, and the network measures of
  the paper's code. Other notebooks on this dandiset can import it.
