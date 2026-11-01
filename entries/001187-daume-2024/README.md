# Daume et al. (2024) from dandiset 001187

Tests the findings of [Daume et al. (2024)](https://doi.org/10.1016/j.neuron.2024.09.013) on
[DANDI:001187](https://dandiarchive.org/dandiset/001187/0.240904.2347), the version the paper
cites. It holds the spike times of 950 units from the hippocampus and amygdala of 39 patients
in 46 sessions of a Sternberg working memory task and a later recognition test.

| Claim | Outcome |
|---|---|
| Sessions and units (46 sessions, 950 units, 351 and 532 after the rate filter) | Reproduced |
| Per-session unit counts of Table S1 | Partially reproduced |
| Behaviour (accuracy, d', load, confidence, probe effects; five claims) | Reproduced |
| WM responses faster in load 1 | Partially reproduced |
| Category neuron counts | Reproduced |
| Persistent and preferred-category maintenance activity (Fig. 2b, 2e) | Partially reproduced |
| Accuracy and load effects for preferred trials (Fig. 2c) | Not reproduced |
| Load but not accuracy effect in amygdala (Fig. 2f) | Partially reproduced |
| Area interactions and hippocampal prediction of later memory (Fig. 3a, 3b) | Partially reproduced |
| No prediction in amygdala (Fig. 3b, 3d, 3f) | Reproduced |
| Remembered above forgotten with high confidence in hippocampus (Fig. 3c) | Not reproduced |
| Early-maintenance cluster in hippocampus (Fig. 3e) | Partially reproduced |
| No effect for non-preferred pictures (Fig. 3g) | Reproduced |
| No effect during encoding (Fig. 3h) | Not reproduced |
| Memory-selective neurons, their AUC and overlap with category neurons (Fig. 4b, 4c) | Reproduced |
| Category neurons carry no memory signal (Fig. 4d) | Blocked: metadata insufficient |
| FS neurons fire more after strong maintenance (Fig. 4e) | Not reproduced |
| NS neurons show no such effect (Fig. 4f) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several of the mixed-model outcomes depend on the outlier rule. The claims file makes the rule of
the Methods the main reading; the rule in the paper's code gives the paper's betas for Figures 2c,
3a and 3b, and this is asked of a reader in `questions/001187.yaml`. The new pictures of the
recognition test carry no category in the dataset, which blocks Figure 4d. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/001187-daume-2024-01.yaml`](../../attempts/001187-daume-2024-01.yaml).
