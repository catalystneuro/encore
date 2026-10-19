# Zhai, Cui, Wokosin, Sun, Tkatch, Crittenden, Graybiel & Surmeier (2025) from dandiset 001538

Tests the findings of [Zhai et al. (2025)](https://doi.org/10.1126/sciadv.adv8224) that can be tested
on [DANDI:001538](https://dandiarchive.org/dandiset/001538/0.260527.1302). The dandiset holds the
somatic and dendritic patch-clamp recordings of dSPNs and iSPNs in the LID off- and on-states and
under the drug and genetic manipulations, GRAB-ACh3.0 imaging, Sr2+-oEPSC recordings, AIM scores,
rotation videos and spine image stacks. It holds no patch-clamp recordings from unlesioned or
6-OHDA-lesioned mice, no spine or rotation counts and no open-field data.

| Claim | Outcome |
|---|---|
| Somatic recordings are the paper's cells (spike counts against its tables) | Partially reproduced |
| Dendritic line scans are the paper's cells (index against its tables) | Reproduced |
| Sr2+-oEPSC cells are the paper's cells | Partially reproduced |
| GRAB-ACh regions are the paper's regions | Not reproduced |
| AIM mice are the paper's mice, with its scores | Not reproduced |
| dSPN rheobase lower and F-I higher in the on-state (Fig. 1E, F) | Reproduced (2 claims) |
| SCH 23390 does not reverse the dSPN rheobase (Fig. 1F) | Reproduced |
| dSPN dendritic index higher in the on-state (Fig. 1I) | Reproduced |
| SCH 23390 reverses the dSPN dendritic index (Fig. 1I) | Not reproduced |
| iSPN rheobase higher and F-I lower in the on-state (Fig. 3C, D) | Reproduced (2 claims) |
| Sulpiride does not change iSPN rheobase (Fig. 3D) | Reproduced |
| iSPN dendritic index lower in the on-state (Fig. 3F) | Reproduced |
| Sulpiride does not change the iSPN dendritic index (Fig. 3F) | Not reproduced |
| ACh release higher in the off-state than unlesioned, similar to 6-OHDA (Fig. 5F) | Reproduced (2 claims) |
| M1R antagonist: somatic unchanged, dendritic index lower (Fig. 6C, D) | Reproduced (2 claims) |
| CDGI KO: somatic oscillation kept, dendritic index unchanged (Fig. 7C, F) | Reproduced (2 claims) |
| M1R deletion does not change somatic excitability (Fig. 9D) | Reproduced |
| Sr2+-oEPSC amplitude and frequency (Fig. 2, 4; four claims) | Blocked: one cell per mouse, too few for the paper's test |
| ACh release in 6-OHDA and its D2 modulation (Fig. 5F; three claims) | Blocked: too few mice for the paper's test |
| AIM scores in CDGI KO and M1R deletion (Fig. 8, 10; two claims) | Blocked: too few mice |
| Spine density (Fig. 2, 4, 6, 7, 9; six claims) | Blocked: methods underspecified, raw stacks only and counting needs manual correction |
| Lesion effects, oxo-M, rotations, open field (eight claims on the paper's Zenodo tables) | Reproduced (counted apart) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Groups have to be read from each sweep's `condition_subfolder`, since files named for a drug also
hold baseline cells. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/001538-zhai-2025-01.yaml`](../../attempts/001538-zhai-2025-01.yaml).

- `reproduce_zhai_2025.ipynb`: the analysis. It takes about ten minutes, most of it streaming the
  files.
- `lid.py`: loading the patch-clamp, Sr2+-oEPSC, GRAB-ACh and AIM files, the somatic and dendritic
  measures of the paper's scripts, an event detector, and the paper's per-cell tables. Other
  notebooks on this dandiset can import it.
