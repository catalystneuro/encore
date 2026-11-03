# Ghaderi, Crochet & Petersen (2026) from dandiset 001530

Tests the findings of [Ghaderi et al. (2026)](https://doi.org/10.1038/s41467-026-73622-y) on
[DANDI:001530](https://dandiarchive.org/dandiset/001530/0.260605.0601), which holds the 35 Neuropixels
sessions (14 mice) of a delayed, context-dependent whisker detection task and the 91 optogenetic
inactivation sessions of the paper.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| Lick probabilities per trial type (Fig. 1c) | Reproduced |
| Movement latencies after the whisker stimulus (Fig. 1f) | Partially reproduced |
| Quiet-trial selection rejects about half of the trials | Partially reproduced |
| Optogenetic inactivation in the Auditory, Delay and Whisker windows (Fig. 2) | Reproduced (3 claims) |
| wM2 against ALM inactivation in the Auditory window | Reproduced |
| Little effect of inactivation on the other trial types | Not reproduced |
| 10,294 units in five areas | Reproduced |
| Activity maps (Fig. 3a) | Reproduced |
| Delay and response PSTHs (Fig. 3b) | Partially reproduced |
| wM2 against ALM delay modulation (Fig. 3c) | Partially reproduced |
| wM2 infragranular delay activity (Fig. 3d) | Partially reproduced |
| The paper's cluster labels link to the dataset's units (registry check) | Reproduced |
| 29 clusters at the BIC minimum (Fig. 4a) | Not reproduced |
| Named clusters (Fig. 4b) | Blocked: methods underspecified |
| Single-neuron context modulation (Fig. 5a) | Partially reproduced |
| Context decoding in the delay (Fig. 5b) | Partially reproduced |
| Decoding time course and neuron counts (Fig. 5b) | Reproduced |
| Cluster removal (Fig. 5c) | Blocked: methods underspecified |
| Null-space decoding (Fig. 5d) | Blocked: not runnable |
| PCA delay states (Fig. 6a) | Partially reproduced |
| Context coding direction (Fig. 6b) | Reproduced |
| Temporal correlation (Fig. 6c) | Reproduced |
| Early whisker response by context (Fig. 7b) | Reproduced |
| No context effect on the whisker coding direction (Fig. 7c) | Reproduced |
| Context decoding after the whisker stimulus (Fig. 7d) | Blocked: methods underspecified |
| wM2 lick divergence at 30 ms (Fig. 8a) | Partially reproduced |
| Lick coding direction at 30 ms (Fig. 8b) | Reproduced |
| Later lick coding ranked by area (Supplementary Fig. 18) | Not reproduced |

Several single-neuron and population values come out at the paper's numbers only with the quiet-trial
rule of the paper's code (mean absolute deviation), not with the rule the Methods state (median
absolute deviation), which the claims file follows. The areas of the units need the CCF label lists of
the paper's Zenodo record (`Area_list.mat`); with them the unit counts match the paper exactly. The lick coding direction needs the lick times of
the same record (`Lick_times.mat`). The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001530-ghaderi-2026-01.yaml`](../../attempts/001530-ghaderi-2026-01.yaml).

- `reproduce_ghaderi_2026.ipynb`: data check, behaviour, optogenetics, unit counts, single-neuron and
  population analyses, cluster labels, lick coding direction. About 15 minutes.
- `decoding_delay.ipynb`: context decoding during the delay (Fig. 5b). About 30 minutes.
- `decoding_clusters_whisker.ipynb`: cluster removal, decoding after the whisker stimulus and the
  clustering of Fig. 4a. About 22 minutes.
- `ghaderi.py`: streaming, trial and quiet-trial selection, area assignment, spike counts, the
  statistics and the decoders. Other notebooks on this dandiset can import it.
