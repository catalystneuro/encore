# Kim & Shin (2025) from dandiset 000248, with the Allen Visual Coding data

Tests the findings of [Kim & Shin (2025)](https://doi.org/10.1101/2025.06.30.662469) on
[DANDI:000248](https://dandiarchive.org/dandiset/000248/0.240502.2344), the Allen OpenScope
Illusion recordings the paper uses for its Isomap pictures (`reproduce_kim_2025.ipynb`). The
paper's main analyses use the Allen Visual Coding Neuropixels sessions; those claims are tested,
as data elsewhere, on the copies in [DANDI:000021](https://dandiarchive.org/dandiset/000021/0.251116.2246)
and [DANDI:000022](https://dandiarchive.org/dandiset/000022/0.251116.2247)
(`reproduce_kim_2025_allen.ipynb`, with decoding and the shuffled comparisons in
`reproduce_kim_2025_decoding.ipynb`).

| Claim | Data | Outcome |
|---|---|---|
| Dandiset 000248 holds the Illusion block, stimuli and units the paper's code uses | 000248 | Reproduced |
| Isomap manifolds: discontinuous at slope 0, overlapping at slope 2 | 000248 | Reproduced |
| Orthogonal variance of Lc1 larger toward faraway Ic1 than nearby Tre2 | 000248 | Reproduced |
| Geometry changes with slope as in the natural scenes data | 000248 | Reproduced |
| Unit and session counts; across-neuron slope near 1 | elsewhere | Reproduced (assumed AllenSDK "good" unit label, used in every Allen analysis) |
| Across-stimulus slope, behavioural state, higher visual areas | elsewhere | Reproduced |
| Noise correlations, dimensionality, occupancy, overlap, continuity | elsewhere | Reproduced |
| Geodesic and orthogonal variance, local and global alignment | elsewhere | Reproduced |
| Representational consistency within and across mice, LM and PM | elsewhere | Reproduced |
| Natural movie slope near 1 | elsewhere | Reproduced (23 sessions, median 1.116) |
| Change of decoding and RSM similarity with shuffling | elsewhere | Reproduced |
| Decoding falls with slope | elsewhere | Blocked: too large (run in part) |
| Gain variance, tangent space angle | elsewhere | Blocked: not ported in time |

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/kim-2025-01.yaml`](../../attempts/kim-2025-01.yaml).
