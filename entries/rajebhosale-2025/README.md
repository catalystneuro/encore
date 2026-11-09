# Rajebhosale et al. (2025) from dandiset 001545

Tests the findings of [Rajebhosale et al. (2025)](https://doi.org/10.26508/lsa.202403169) that can
be tested on [DANDI:001545](https://dandiarchive.org/dandiset/001545/0.250809.1653), which holds
whole-cell current clamp recordings of 48 dentate granule cells, typical GCs and semilunar granule
cells (SGCs), from 5 wild-type and 5 Nrg1 V321L mice. Soma positions, dendritic morphology, the
Golgi and RNAScope data and the snMultiome data are not in it.

| Claim | Outcome |
|---|---|
| WT SGCs have a more hyperpolarized RMP than WT GCs (Fig 1J) | Not reproduced |
| WT SGCs have narrower spikes (Fig 1K) | Not reproduced |
| WT SGCs have a faster downstroke (Fig 1L) | Not reproduced |
| Phase plots differ between WT GCs and SGCs (Fig 1M) | Not reproduced |
| The remaining properties do not differ between WT GCs and SGCs or with soma position | Partially reproduced |
| V321L GCs and SGCs do not differ in RMP, spike width or downstroke (Fig 2I to K) | Reproduced (3 claims) |
| LDA separates WT GCs from the other groups (Fig 2M) | Blocked: methods underspecified |
| k-means places V321L cells like WT SGCs (Fig S2D) | Reproduced (rests on the 4 GCs of mouse VV253) |
| PCA separates WT GCs from SGCs, not V321L (Fig S2E) | Not reproduced |
| A WT-trained LDA classifier: 78% on WT, 52% on V321L (Fig S2G) | Not reproduced |
| V321L centroids close together on the WT SGC side (Fig S2F) | Not reproduced |
| Soma position, morphology, Golgi and RNAScope (23 claims) | Blocked: data missing |
| snMultiome data in GEO (19 claims) | Blocked: not runnable |
| SGC-enriched genes at the dorsal border of the E18.5 dentate gyrus, Allen ISH images (Fig S9C) | Reproduced (read by eye, assumed) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/rajebhosale-2025-01.yaml`](../../attempts/rajebhosale-2025-01.yaml).
