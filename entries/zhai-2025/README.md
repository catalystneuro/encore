# Zhai, Cui, Wokosin, Sun, Tkatch, Crittenden, Graybiel & Surmeier (2025) from dandiset 001538

Tests the findings of [Zhai et al. (2025)](https://doi.org/10.1126/sciadv.adv8224) on
[DANDI:001538](https://dandiarchive.org/dandiset/001538/0.261124.1858), version 0.261124.1858. The
dandiset holds the somatic and dendritic patch-clamp recordings of the off-state, on-state and drug
groups (Figures 1, 3, 6, 7 and 9), the Sr2+-oEPSC recordings (Figures 2 and 4), the GRAB-ACh3.0
movies (Figure 5), the raw 2PLSM spine image stacks and the AIM score sheets (Figures 8 and 10).
The control and 6-OHDA patch-clamp recordings, the open-field data and the confocal images are not
in it; claims on them are tested on the paper's own tables (Zenodo 17307059).

| Claim | Outcome |
|---|---|
| Link: somatic recordings and the paper's spike counts | Partially reproduced |
| Link: dendritic line scans and the paper's index | Reproduced |
| Link: Sr2+-oEPSC cells and the paper's per-cell values | Partially reproduced |
| Link: GRAB-ACh3.0 regions and the paper's areas | Not reproduced |
| Link: AIM mice and the paper's scores | Not reproduced |
| dSPN somatic excitability higher in the on-state; not reversed by SCH 23390 (three claims) | Reproduced |
| dSPN dendritic index higher in the on-state | Reproduced |
| SCH 23390 lowers the on-state dSPN dendritic index | Not reproduced |
| iSPN somatic excitability lower in the on-state; sulpiride without effect (three claims) | Reproduced |
| iSPN dendritic index lower in the on-state; sulpiride without significant effect | Reproduced |
| Sr2+-oEPSC amplitude and frequency in dSPNs and iSPNs (four claims) | Reproduced, resting on a stand-in event detector |
| GRAB-ACh3.0: release raised after the lesion and in the off-state, D2R and dopamine effects (five claims) | Reproduced |
| M1R antagonist, CDGI KO and M1R CRISPR: somatic and dendritic claims (five claims) | Reproduced |
| AIMs in CDGI KO and M1R CRISPR mice (two claims) | Reproduced |
| Claims on the paper's tables: lesion effects, oxo-M, rotations, open field (eight claims) | Reproduced |
| Spine densities (2PLSM and confocal, six claims) | Blocked: not runnable |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/zhai-2025-03.yaml`](../../attempts/zhai-2025-03.yaml).

- `reproduce_zhai_2025.ipynb`: the analysis. It takes about eight minutes, most of it streaming
  the files.
- `zhai.py`: loading the files, spike counts and rheobase, the dendritic index, the Sr2+-oEPSC
  detector, the GRAB-ACh3.0 areas, the AIM scores and the paper's tables, with where each
  parameter comes from. Other notebooks on this dandiset can import it.
