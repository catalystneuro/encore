# Strickland and McDannald (2022) from CRCNS bst-3

Tests the findings of [Strickland and McDannald (2022)](https://doi.org/10.1038/s41467-022-34021-1)
on CRCNS data set [bst-3](https://doi.org/10.6080/K0Q23XGR), which holds 1812 brainstem single
units recorded with Neuropixels in ten rats during probabilistic fear discrimination, the cube file
of binned and normalized firing that the paper's scripts build from them, and those scripts.

| Claim | Outcome |
|---|---|
| The units match the paper's Source Data cluster rows (link) | Reproduced |
| Suppression ordered danger > uncertainty > safety, F(2,142) = 149.2 | Reproduced |
| Every rat discriminates | Reproduced |
| 1812 units, 73 sessions, 965 from females, per-subject totals | Reproduced |
| 21 regions and their unit counts | Reproduced |
| 21 cue clusters of 24 to 219 units | Reproduced |
| Cue PC1 (29.7%) is ordered danger > uncertainty > safety | Reproduced |
| PC1 comes from k1 to k9 (505 units), k1 and k2 most | Reproduced |
| Danger latency correlates with PC1 contribution (R2 = 0.41) | Not reproduced |
| k1 to k9 form a correlated subnetwork, k3 the exception | Reproduced |
| k1 and k2 are hubs of the cue subnetwork | Partially reproduced (assumption) |
| Cue clusters span six or more regions; subnetwork in SC and PAG | Reproduced |
| Cluster regression shapes (k5, k15, k10, k6) | Partially reproduced |
| Beta PCA, PC1 62.7% and PC2 26.1% | Reproduced |
| Subnetwork lesion | Partially reproduced |
| Supranetwork lesion | Reproduced |
| DPG and LPAG bias toward the subnetwork | Reproduced |
| 11 outcome clusters of 46 to 322 units | Partially reproduced |
| Outcome PC1 (17.7%) is positive prediction error | Reproduced |
| Phasic outcome network k1 to k3 | Reproduced (assumption) |
| Tonic outcome network k6 to k9 | Reproduced (assumption) |
| Network PCAs, 37.0% and 29.2% | Reproduced |
| Outcome hubs | Reproduced |
| Outcome network anatomy | Reproduced |
| Outcome regression, k1 and k6 | Reproduced |
| Outcome beta PCA, 53.7% and 33.4% | Reproduced |
| Phasic and tonic lesions | Reproduced |
| No anatomical bias of outcome networks | Reproduced |
| Cue and outcome network membership independent | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds no cluster membership; the paper's clusters are taken from its Source Data
workbook, which every unit matches exactly. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/strickland-2022-01.yaml`](../../attempts/strickland-2022-01.yaml).

- `reproduce_strickland_2022.ipynb`: the analysis. It takes about two minutes, most of it reading
  the 1812 unit files and the cube from the archive.
- `bst3.py`: reading the zip in place, the cube and the unit files, and the measures of the paper's
  scripts (normalization, suppression ratios, PCA, shuffles, regression, latency). Other notebooks
  on this data set can import it.
