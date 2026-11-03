# Chantranupong et al. (2023) from dandiset 001767

Tests the findings of [Chantranupong et al. (2023)](https://doi.org/10.1038/s41586-023-06492-9) that can be tested on
[DANDI:001767](https://dandiarchive.org/dandiset/001767/0.260318.1448), which holds fibre photometry of dopamine,
acetylcholine, glutamate and terminal calcium in the ventrolateral striatum of 112 mice in a two-armed bandit task, with the
behaviour of each session (379 sessions). The slice recordings, histology, head-fixed and dopamine-neuron inhibition
experiments are not in it.

| Claim | Outcome |
|---|---|
| The export table's figure and genotype labels match the files | Reproduced |
| Block transitions, outcome and history coding, cue omission, LDA, mutant sensors (Fig. 1, Extended Data Figs. 1 to 4) | 8 reproduced, 4 not reproduced |
| DA and Ach anticorrelation (Fig. 2, Extended Data Fig. 6) | 3 reproduced, 2 partially, 1 not reproduced |
| TelC in cholinergic interneurons (Fig. 3, Extended Data Figs. 7 to 9) | 2 reproduced, 3 not reproduced |
| Drd2 deletion in cholinergic interneurons (Fig. 4, Extended Data Fig. 11) | 1 reproduced, 5 not reproduced |
| Glutamate and its inputs (Fig. 5, Extended Data Fig. 13) | 1 reproduced, 2 partially, 2 not reproduced |
| GLMs (Extended Data Figs. 5, 6h, 11b,c; five claims) | Blocked: methods underspecified |
| Slice, histology, head-fixed and DAN-inhibition experiments, Fig. 3d, Fig. 5e,f dF/F0, Extended Data Fig. 8f (eight claims) | Blocked: data missing (seven) or methods underspecified (one) |

The counts by claim are in the attempt record. A failure to reproduce here may be a failure of this attempt, not of the paper:
see the reasoning and the differences from the paper's method.

The files carry no figure, cohort or genotype labels; they come from `manuscript_sessions.csv` of the dandiset's export code,
which the dandiset's metadata links. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001767-chantranupong-2023-01.yaml`](../../attempts/001767-chantranupong-2023-01.yaml).

- `reproduce_chantranupong_2023.ipynb`: the analysis. It takes about 20 minutes: about 8 streaming the files and about 9
  fitting the GLMs.
- `achda.py`: loading the files, trial windows and measures, cross-correlation, dF/F0, the behaviour metrics and the RFLR, and
  the GLM. Other notebooks on this dandiset can import it.
