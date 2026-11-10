# Huang, Hess, Bajpai, Li, Hobson, Xu, Barton & Lu (2025) from dandiset 001349

Tests the findings of [Huang et al. (2025)](https://doi.org/10.1016/j.isci.2025.112104) on
[DANDI:001349](https://dandiarchive.org/dandiset/001349/0.250604.1510), which holds two-photon
imaging of L2/3 and L4 of mouse primary somatosensory cortex from P11 to P21, and of DREADD mice at
P15 before and after CNO: Suite2p ROIs with their fluorescence, dF/F, Z-score and detected events.

| Claim | Outcome |
|---|---|
| The repository's per-field tables (quiescent windows) can be linked to the files | Partially reproduced (88% and 58% of rows) |
| Event and synchrony frequency fall from P11 to P21 | Reproduced |
| Pearson correlation falls in females, not males; L2/3 above L4 at P11 | Reproduced |
| Five claims on mutual information | Blocked: methods underspecified |
| Subnetworks present at P11, similar number at P21; silhouette value rises | Reproduced |
| tCC higher within than between subnetworks | Reproduced |
| Within-subnetwork tCC rises in L2/3 | Not reproduced |
| Subnetwork number unrelated to neuron number and window length | Reproduced |
| Single-cluster neurons fall, non-cluster rise, multiple-cluster unchanged (P11 to P21) | Reproduced |
| Subnetwork size unchanged, centroids closer at P21 | Reproduced |
| Trajectories over P11 to P21 (Figure 4, S4): nine claims | 4 reproduced, 1 partially, 4 not reproduced |
| CNO lowers event and synchrony frequency, raises silhouette and female tCC | Reproduced |
| CNO leaves correlation, subnetwork number, configuration and topography unchanged | Not reproduced |
| About 25% of events clustered (Figure S7A) | Not reproduced |
| Comparisons of clustering methods (Figures S7, S8) | Blocked (not run) |
| Figure S5 cell-type counts | Blocked (not public) |
| Figure S9 histology, from the code repository | 1 reproduced, 1 partially |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset holds no behavioural data, so the quiescent windows in which the paper measures
everything come from the paper's code repository
([EdnaHuang/SubnetworkAssembley2024](https://github.com/EdnaHuang/SubnetworkAssembley2024), commit
28e1b6d). The Methods and the code differ on the synchrony threshold, the number of k-means runs and
the participation test; the paper's own tables match the code's choices, and 13 outcomes rest on
that assumption (every reading is shown). The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/huang-2025-01.yaml`](../../attempts/huang-2025-01.yaml).

- `reproduce_huang_2025.ipynb`: the imaging analysis. It takes about 40 minutes on four processes,
  most of it the k-means runs (100 and 10 per cluster number for 422 fields).
- `histology_figs9.ipynb`: the Figure S9 histology, from the repository's spreadsheet (seconds).
- `subnet.py`: loading, the link to the repository's tables, the paper's measures (events,
  synchrony, correlation, MI, k-means event clusters, subnetworks, tCC, distances) and its mixed-model
  bootstrap tests. Other notebooks on this dandiset can import it.
