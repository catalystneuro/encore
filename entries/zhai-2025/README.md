# Zhai et al. (2025) from dandiset 001538

Tests the findings of [Zhai et al. (2025)](https://doi.org/10.1126/sciadv.adv8224) that can be tested
on the draft of [DANDI:001538](https://dandiarchive.org/dandiset/001538/draft), as modified on
2026-11-09. The draft holds the whole-cell somatic and dendritic excitability recordings of dSPNs and
iSPNs in the on- and off-states of levodopa-induced dyskinesia (with SCH 23390, sulpiride, M1R
antagonists, CDGI knockout and M1R deletion), the Sr2+-oEPSC recordings, the GRAB-ACh3.0 imaging,
the AIM score sheets and videos, two-photon spine images and the confocal spine images of Figure 4I
to 4K, but no spine counts. Control and 6-OHDA patch-clamp recordings, rotation counts and
open-field data are not in it; the claims on those are tested on the paper's tables at Zenodo.

| Claim | Outcome |
|---|---|
| Link: somatic recordings match the paper's per-cell spike counts | Partially reproduced |
| Link: dendritic index matches the paper's per-cell values | Reproduced |
| Link: Sr2+-oEPSC cells and events match the paper's | Partially reproduced |
| Link: GRAB-ACh3.0 regions match the paper's areas | Not reproduced |
| Link: AIM mice and scores match the paper's tables | Not reproduced |
| dSPN rheobase lower and F-I higher on-state; SCH 23390 does not reverse it | Reproduced (3 claims) |
| dSPN dendritic index higher on-state | Reproduced |
| SCH 23390 reverses the higher dSPN dendritic index | Reproduced, resting on an assumption (a cell the dandiset holds only in part is left out) |
| dSPN Sr2+-oEPSC amplitude larger on-state, frequency unchanged | Reproduced, resting on an assumption (2 claims) |
| iSPN rheobase higher and F-I lower on-state; sulpiride has no effect | Reproduced (3 claims) |
| iSPN dendritic index lower on-state; sulpiride has no effect | Reproduced (2 claims) |
| iSPN Sr2+-oEPSC amplitude smaller on-state, frequency unchanged | Reproduced, resting on an assumption (2 claims) |
| Evoked ACh release: off-state and 6-OHDA elevated, D2R and dopamine effects | Reproduced (5 claims) |
| M1R antagonism, CDGI knockout and M1R deletion: somatic and dendritic effects | Reproduced (5 claims) |
| AIMs attenuated by M1R deletion (Figure 10B) | Reproduced |
| Claims on the paper's tables (lesion effects, oxo-M, rotations, open field) | Reproduced (8 claims) |
| Spine density from 2PLSM and confocal images | Blocked: methods underspecified (6 claims) |
| AIMs less severe in CDGI knockout (Figure 8B, C) | Blocked: data missing (the published Figure 8 scores are not in the dandiset) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/zhai-2025-02.yaml`](../../attempts/zhai-2025-02.yaml).

- `reproduce_zhai_2025.ipynb`: the analysis. It takes about eight minutes, most of it streaming the files.
- `lid.py`: loading the files, spike counts and rheobase, the dendritic excitability index, a
  Sr2+-oEPSC event detector, the GRAB-ACh3.0 normalised area and the AIM sheets, each parameter
  with its source. Other notebooks on this dandiset can import it.
