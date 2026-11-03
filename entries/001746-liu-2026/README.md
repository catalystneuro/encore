# Liu, Huang, Shen, Shao, Jing et al. (2026) from dandiset 001746

Tests the findings of [Liu et al. (2026)](https://doi.org/10.1038/s41556-026-02009-4) that can be
tested on [DANDI:001746](https://dandiarchive.org/dandiset/001746/0.260825.0222), which holds the
current-clamp step recordings of the 462 Patch-seq cells from the macaque anterior insular cortex.
The files carry no cell types; these come from the cell table in the paper's code repository
([RFLiu2021/AIC_proj](https://github.com/RFLiu2021/AIC_proj) at commit 44cd8a6), matched by file
name. For Fig. 7c the 10x data come from GEO GSE319557.

| Claim | Outcome |
|---|---|
| The recordings are the cells of the code's cell table, and their features match its feature table | Reproduced |
| The code's morphology table matches the dandiset's cells (link claim) | Reproduced |
| 462 cells with intrinsic properties from 12 male macaques | Partially reproduced (10 subjects) |
| 307 typed cells, 273 excitatory in 18 types, 34 inhibitory in 17 types | Partially reproduced |
| Excitatory cells by subclass | Partially reproduced |
| The 29 VENs map to L5 ET (14) and L5/6 CT (15) | Reproduced |
| VEN-L map to L5 ET, VEN-S to L5/6 CT | Partially reproduced |
| L2/3 IT HPCAL1 neurons have the smallest membrane time constant | Reproduced |
| L2/3 IT HPCAL1 neurons have narrow APs | Partially reproduced |
| IT RORB and L6 PC have a distinctive input resistance | Partially reproduced |
| L5 IT FEZF2 have a higher AP threshold and longer latency | Reproduced |
| VENs have the broadest APs | Partially reproduced |
| L5 ET have the deepest sag | Blocked: methods underspecified |
| VENs fire less and more irregularly than PCs | Not reproduced |
| L5 ET against L5 IT: deeper sag, lower input resistance, higher rate | Partially reproduced |
| VENs have the lowest phase peak index; their phase plots are saddle-shaped | Partially reproduced (change to blocked proposed) |
| VEN-L differ more from L5/6 CT than VEN-S do | Reproduced |
| Morphology differs on more features than physiology | Reproduced |
| Recordings without RNA (Fig. 4a-c, Extended Data Fig. 9c,d, Supplementary Table 8) | Blocked: data missing |
| Peak index against AIS distance (Fig. 4i) | Not reproduced (change to blocked proposed) |
| Tau distance against transcriptomic distance (Fig. 7) | Not reproduced |
| Nine claims on data in other archives | Blocked: other |

After the second verification, a change of the three phase peak index claims to blocked (methods
underspecified) is proposed and awaits a third round: the automatic index, which stands in for the
peaks the paper placed by hand, reads the AIS value next to the SD peak at the noise level of these
recordings, so it does not measure the saddle shape.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001746-liu-2026-01.yaml`](../../attempts/001746-liu-2026-01.yaml).

- `reproduce_liu_2026.ipynb`: the analysis. It reads all 462 files (about 15 GB) and streams the
  first 4.4 GB of the GEO h5ad archive. In the last run it took 6.5 minutes, of which reading the
  files took 4 and the GEO stream 1; the stream's time depends on the GEO server.
- `aic.py`: loading the files, and the electrophysiological features as the Methods define them,
  with the details taken from the paper's package PatchAnaLab 1.0; the docstring says where each
  parameter comes from. Other notebooks on this dandiset can import it.
