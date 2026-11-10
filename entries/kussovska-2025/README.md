# Kussovska, Kim & Rungratsameetaweemana (2025) from dandiset 000469

Tests the findings of [Kussovska et al. (2025)](https://doi.org/10.1101/2025.10.31.684900) on
[DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), the human single-neuron
recordings of Kyzar et al. (2024) during a Sternberg working memory task, which the paper reuses.

| Claims | Outcome |
|---|---|
| Units by region, behavior (accuracy, load effect, reaction times) | Reproduced (6) |
| Load-modulated neurons (Fig. 1e) | Reproduced |
| RT-modulated neurons not significant (Fig. 1f) | Not reproduced; the paper's values come from the code's use of subject 1's reaction times for every neuron |
| Concept cells, single-cell and population persistence, cross-temporal decoding | Reproduced (6) |
| Maintenance decoding within participant, load 1 / load 2 | Reproduced / partially reproduced |
| Bin-width decoding / pairwise comparisons / load 2 | Partially reproduced / not reproduced / reproduced |
| dPCA state-space analyses (Fig. 3) | Blocked: too large (3) |
| Population bursts against the Poisson null, encoding and maintenance; loads 2 and 3 | Reproduced (3) |
| Burst differences between ACG groups and across epochs (Fig. 4f-j) | Partially reproduced (3) |
| ACG fits, cell-type clusters and their features, rodent validation, concept cell types | Reproduced (6) |
| Cell-type bursting (Fig. 6a-d), IN load dependence | Partially reproduced (2), reproduced (1) |
| Load and RT modulation by cell type (Fig. 6e,f) | Partially reproduced / not reproduced |
| CV2 and decay constants of concept cells (Fig. 6g,h; Ext. Fig. 5g,h) | Not reproduced (2) |
| Bin-width decoding by cell type, cross-temporal by type, load 2 by type | Not reproduced (PY), partially reproduced (IN), reproduced (2) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's code (github.com/dariakussovska/heterogeneitywm, commit 5144fe8) supplies the
matched trial tables that several readings use and the features of the rodent validation set.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/kussovska-2025-01.yaml`](../../attempts/kussovska-2025-01.yaml).

- `reproduce_kussovska_2025.ipynb`: the analysis, about 20 minutes on four CPUs.
- `wm.py`: loading the Sternberg files, trial and spike helpers, the Poisson GLM, the concept-cell
  bootstrap, the linear SVM decoders, the CellExplorer ACG port, the burst detection and the
  neuron groups. Other notebooks on this dandiset can import it.
