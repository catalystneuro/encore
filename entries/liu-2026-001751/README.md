# Liu, Huang, Shen, Shao, Jing et al. (2026) from dandiset 001751

Tests the local connectivity findings of Fig. 5d-i of
[Liu et al. (2026)](https://doi.org/10.1038/s41556-026-02009-4) on
[DANDI:001751](https://dandiarchive.org/dandiset/001751/0.260825.0222), which holds the
multi-patch recordings: 301 connection tests in 56 slices of six macaques, each a stimulated cell
and up to seven simultaneously recorded neighbours.

| Claim | Outcome |
|---|---|
| The paper's code table links to the dandiset's files and channels | Reproduced |
| 1,292 pairs among 377 neurons, 31 connections | Not reproduced |
| PC-to-PC, 24 of 503 | Not reproduced |
| VENs make no connection with VENs, PCs or interneurons | Partially reproduced |
| PC-to-VEN, 1 of 200 | Partially reproduced |
| PC-to-IN 2 of 65, IN-to-PC 4 of 65 | Partially reproduced |
| IN-to-VEN, 0 of 55 | Reproduced |
| VENs are sparsely connected compared with PCs (Fig. 5i) | Partially reproduced |
| The example slice of Fig. 5d-h | Reproduced |
| Soma distances of the pair classes | Blocked: data missing |
| The PC rate is comparable with the primate literature | Blocked: methods underspecified |
| eEPSPs larger in VENs than PCs (Fig. 4j, from the code's table) | Reproduced |
| AIS farther and shorter in VENs (Fig. 3c, from the code's table) | Blocked: metadata insufficient |
| eEPSP latencies similar (Fig. 4j) | Blocked: no latencies in the code's table |
| sPSC and mPSC frequencies lower in VENs (Fig. 5b, the code's per-cell values) | Reproduced |
| PSC amplitudes do not differ (Fig. 5c, the code's per-cell values) | Reproduced |
| Somatic Na+ currents lower in VENs (Fig. 4d, DANDI:001750) | Reproduced, resting on an assumption |
| VENs have the lowest phase-plane peak index (Fig. 3e, the code's table) | Reproduced |
| Metabolite counts AIC against V1 and PrC (Fig. 8a, MetaboLights MTBLS13927) | Partially reproduced |
| Citrate, 2-ketobutyrate and glutamate in AIC against V1 (Fig. 8d,e, MetaboLights MTBLS13927) | Partially reproduced |
| 29 VENs map to L5 ET (14) and L5/6 CT (15) | Reproduced |
| VEN-L to L5 ET and VEN-S to L5/6 CT (Fig. 6f,g) | Partially reproduced |
| Patch-seq neurons mapped to transcriptomic types | Blocked: metadata insufficient |
| 12 other claims on data in other archives | Blocked: not attempted (one also by its criterion) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files carry no cell types, connection labels or soma positions. Types and annotated
connections come from the paper's code, `metadata_multiPatch.xlsx` in
[RFLiu2021/AIC_proj](https://github.com/RFLiu2021/AIC_proj) at commit 44cd8a6, matched through
the file names it lists (ten of its presynaptic blocks name no file; eight are matched by the
cell that fires). That table counts 298 cells, 1,416 pairs (1,403 in files of the dandiset) and
26 connections, where the paper reports 377, 1,292 and 31. The attempt record, with the reasons and the differences from
the paper's method, is
[`attempts/liu-2026-03.yaml`](../../attempts/liu-2026-03.yaml).

The claims on data in other archives are tested on the paper's code tables where these hold
per-cell values, on DANDI:001750 for the Na+ currents and on MetaboLights MTBLS13927 for the
metabolites; they are counted apart from the
dandiset's.

- `reproduce_liu_2026.ipynb`: the analysis. Its last run took 4.9 minutes (printed at the end of
  the last code cell), 175 s of it streaming the 7 GB of files into memory.
- `multipatch.py`: loading the files, finding the stimulated cell, averaging and filtering the
  responses as the paper's code does, and reading the code's table. Other notebooks on this
  dandiset can import it.
