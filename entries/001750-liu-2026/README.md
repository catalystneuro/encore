# Liu, Huang, Shen, Shao, Jing et al. (2026) from dandiset 001750

Tests the findings of [Liu et al. (2026)](https://doi.org/10.1038/s41556-026-02009-4) that rest on
[DANDI:001750](https://dandiarchive.org/dandiset/001750/0.260825.0222), which holds 35 somatic
outside-out patch recordings of Na+ currents from one macaque (Figure 4d). Cell types come from the
paper's code table, as the files carry none. Two metabolomics claims are tested on MetaboLights
MTBLS13927, and the eEPSP amplitude, VEN subtype and phase peak index claims on tables in the paper's
code repository.

| Claim | Outcome |
|---|---|
| The files are the 35 patches of the paper's code table, with matching maximal currents | Partially reproduced |
| Na+ currents are lower in VENs (n = 14) than in L5 PCs (n = 21) | Blocked: methods underspecified |
| VEN to PC ratio of peak Na+ current near 0.69 | Blocked: methods underspecified |
| Patch capacitance about 50 fF, area about 5 um2 | Blocked: data missing |
| 228 metabolites differ between AIC and V1, 108 between AIC and PrC (MetaboLights) | Not reproduced |
| Higher citrate and glutamate, lower 2-ketobutyrate in AIC than V1 (MetaboLights) | Partially reproduced |
| eEPSP amplitudes higher in VENs than PCs (code repository table) | Reproduced |
| VEN-L and VEN-S have similar AP width, AP amplitude and eEPSP amplitude (code repository tables) | Reproduced |
| VENs have lower AP phase-plane peak indices than every PC type (code repository table) | Reproduced |
| AIS distance and length, two-way ANOVA (code repository table) | Blocked: metadata insufficient |
| 24 other claims on data elsewhere (other dandisets, GEO, Zenodo, NeuroMorpho, and for fig4j-eepsp-latency a repository table that holds no latency); ven-firing-rate-variability is blocked on method, the others on data or time | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/001750-liu-2026-01.yaml`](../../attempts/001750-liu-2026-01.yaml).

- `reproduce_liu_2026.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  files.
- `nacurrent.py`: loading the files and the paper's cell table, the step levels, and the maximal
  inward current under each reading of the method. Other notebooks on this dandiset can import it.
