# Chandravadia et al. (2020) from dandiset 000004

Tests the claims of [Chandravadia et al. (2020)](https://doi.org/10.1038/s41597-020-0415-9), a data
descriptor of 1863 single neurons recorded in the human amygdala and hippocampus during a new/old
recognition memory task, on [DANDI:000004](https://dandiarchive.org/dandiset/000004/0.220126.1852)
version 0.220126.1852. The claims cover the file contents the paper describes (sessions, subjects,
trials, event codes, units and electrode tables), the behavioural ROC analyses of Figure 5, and the
proportions of visually and memory selective cells.

| Claim | Outcome |
|---|---|
| 1863 neurons from 59 subjects | Reproduced (1864 unit rows) |
| 87 sessions of Online-only Table 1 | Reproduced |
| Age and sex of every subject | Partially reproduced (3 subjects differ) |
| 100 encoding and 100 recognition trials per session, 5 categories | Partially reproduced (8 sessions lack encoding trials) |
| new_old_labels_recog is 0 for old, 1 for new | Not reproduced (the coding is reversed) |
| TTL codes of Table 1 | Partially reproduced |
| Experiment ids of Table 2 | Partially reproduced |
| Session dates on the first of the month | Partially reproduced |
| Units table columns and metrics | Partially reproduced (metrics missing or not finite) |
| Electrodes table, including impedance | Not reproduced (impedance empty) |
| Refractory criterion (< 3% of ISIs below 3 ms) | Partially reproduced (6 units fail) |
| All units in amygdala or hippocampus | Reproduced |
| Behavioural AUC 0.74 ± 0.10 | Reproduced |
| AUC by site | Reproduced |
| Asymmetric ROC | Reproduced |
| Accuracy higher with high confidence | Reproduced |
| 343 VS cells (18.4%) | Reproduced (332) |
| 146 MS cells (7.8%) | Not reproduced (110; the code's trial selection gives 147) |
| 26 dual cells (1.4%) | Not reproduced (12; the code's choices give 26) |
| VS, MS and dual percentages by site | Partially reproduced |
| 9 TWH sessions | Reproduced |
| Link to the earlier release (Faraut et al. 2018) | Partially reproduced (64 of 65 sessions) |
| 23 sessions, 17 subjects and 288 neurons added | Partially reproduced (325 neurons) |
| Figure 4 example neuron | Reproduced |
| Figure 3 example neuron | Blocked: session 144 is not in the dandiset |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/chandravadia-2020-02.yaml`](../../attempts/chandravadia-2020-02.yaml).

- `reproduce_chandravadia_2020.ipynb`: the analysis. It streams the trials, events, electrodes and
  units of all 87 files (not the stimulus images) and takes about 3 minutes.
- `chandravadia.py`: reading the files, the paper's session tables from Europe PMC, the ROC, z-ROC
  and accuracy measures of the paper's code, window firing rates, the ANOVA and the bootstrap test.
  Other notebooks on this dataset can import it.
