# Chantranupong et al. (2023) from dandiset 001767

Tests the findings of [Chantranupong et al. (2023)](https://doi.org/10.1038/s41586-023-06492-9) that can be tested on
[DANDI:001767](https://dandiarchive.org/dandiset/001767/0.260318.1448), which holds fibre photometry of dopamine,
acetylcholine, glutamate and terminal calcium in the ventrolateral striatum of 112 mice in a two-armed bandit task, with the
behaviour of each session (379 sessions). The slice recordings, histology, head-fixed and dopamine-neuron inhibition
experiments are not in it.

| Claim | Outcome |
|---|---|
| The export table's figure and genotype labels match the files | Reproduced |
| Block transitions, outcome and history coding, cue omission, LDA, mutant sensors (Fig. 1, Extended Data Figs. 1 to 4) | 7 reproduced, 5 not reproduced |
| DA and Ach anticorrelation (Fig. 2, Extended Data Fig. 6) | 3 reproduced, 2 partially, 1 not reproduced |
| TelC in cholinergic interneurons (Fig. 3, Extended Data Figs. 8 and 9) | 1 reproduced, 4 not reproduced |
| Drd2 deletion in cholinergic interneurons (Fig. 4, Extended Data Fig. 11) | 1 reproduced, 5 not reproduced |
| Glutamate and its inputs (Fig. 5, Extended Data Fig. 13) | 1 reproduced, 3 partially, 2 not reproduced |
| GLMs (Extended Data Figs. 5, 6h, 11b,c; five claims) | 1 partially, 2 not reproduced, 2 blocked: methods underspecified |
| Slice, histology, head-fixed, DAN-inhibition and CIN-stimulation experiments, Fig. 3d (seven claims) | Blocked: data missing |

The counts by claim are in the attempt record. After the second verification round a change to not reproduced was proposed
for three claims (fig1e-reward-outcome-not-pre, ed8g-vls-telc-ach-suppressed, ed11-cko-glm-r2); the third round agreed, and
the table gives the changed outcomes. A failure to reproduce here may be a failure of this attempt, not of the paper:
see the reasoning and the differences from the paper's method.

The files carry no figure, cohort or genotype labels; they come from `manuscript_sessions.csv` of the dandiset's export code,
which the dandiset's metadata links. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001767-chantranupong-2023-01.yaml`](../../attempts/001767-chantranupong-2023-01.yaml).

- `reproduce_chantranupong_2023.ipynb`: the analysis. It takes about 45 minutes: up to 25 streaming the files and about 20
  fitting the GLMs.
- `achda.py`: loading the files, trial windows and measures, cross-correlation, dF/F0, the behaviour metrics and the RFLR, and
  the GLM. Other notebooks on this dandiset can import it.
