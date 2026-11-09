# Fujimoto, Fujimoto, Elorette et al. (2026) from dandiset 001773

Tests the findings of [Fujimoto et al. (2026)](https://doi.org/10.1038/s41593-026-02301-4) that can
be tested on [DANDI:001773](https://dandiarchive.org/dandiset/001773/0.260416.1939). The dandiset
holds the paper's derived values (voxel FA, voxel seed connectivity in 17 target ROIs, group
connectomes, CC1 and DAPI counts, EM g-ratios, home-cage behavior bins) and its MATLAB scripts.
No images are in it.

| Claims | Outcome |
|---|---|
| DWI, histology, EM and behavior of the stimulated monkeys N and T (9 claims) | Reproduced |
| Connectome patterns and per-ROI counts, DBS group and nonsurgical controls (3 claims) | Reproduced |
| Fig. 4c network sorting | Blocked: the connectome ROIs have no names |
| Seed connectivity of the SCC, ROIs and networks, N and T (10 claims) | Reproduced |
| Voxelwise maps of the nonsurgical controls and of monkey D (2 claims) | Blocked: data missing |
| Monkey D, FA, CC1, connectome and seed ROIs (5 claims) | Reproduced |
| Monkey D, behavior unchanged | Not reproduced (foraging falls, P = 0.023) |
| Monkey D, no network reduction | Blocked: the readings disagree |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/fujimoto-2026-01.yaml`](../../attempts/fujimoto-2026-01.yaml).

- `reproduce_fujimoto_2026.ipynb`: the analysis. It takes under a minute.
- `dbs.py`: reading the sheets from the archive, and the paper's statistics as its MATLAB scripts
  compute them (`anovan` type III with the scripts' model terms, `multcompare` Tukey-Kramer on
  population marginal means). Other notebooks on this dandiset can import it.
