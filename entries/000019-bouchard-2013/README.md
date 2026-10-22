# Bouchard, Mesgarani, Johnson & Chang (2013) from dandiset 000019

Tests the findings of [Bouchard et al. (2013)](https://doi.org/10.1038/nature11911) that can be
tested on [DANDI:000019](https://dandiarchive.org/dandiset/000019/0.220126.2148), which holds raw
ECoG and hand-marked syllable annotations of subjects reading consonant-vowel syllables. High gamma
is computed here from the raw voltage. The audio and the electrode positions relative to the
central sulcus and Sylvian fissure are not in the dandiset.

| Claim | Outcome |
|---|---|
| Data composition (subjects, syllables, renditions, rate) | Partially reproduced |
| About 30 active vSMC electrodes per subject | Not reproduced |
| Named electrodes of Fig. 1c-e | Blocked: metadata insufficient |
| Lips electrode active for /ju/ only (Fig. 1h) | Not reproduced |
| Spatial maps and their statistics (Fig. 2, Supplementary Figures 3, 5 and 7; seven claims) | Blocked: metadata insufficient |
| Mixed tuning at single electrodes | Reproduced |
| Timing sequence of articulator correlations | Not reproduced |
| Nine PCs explain about 60% of variance | Blocked: methods underspecified |
| Three k-means clusters most parsimonious | Not reproduced |
| Co-clustering with articulators and vowels | Blocked: methods underspecified |
| Hierarchical clustering | Blocked: methods underspecified |
| Feature correlations, early and late | Blocked: methods underspecified |
| Separability timing | Not reproduced |
| Separability coupled to feature correlations | Blocked: methods underspecified |
| Consonant-vowel distances | Blocked: methods underspecified |
| PC articulator weights | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most claims blocked as methods underspecified depend on two details the claims file does not fix
and that were asked as questions (`questions/000019.yaml`): how the state-space input is z-scored,
and whether syllables with fewer than 15 renditions are kept. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/000019-bouchard-2013-01.yaml`](../../attempts/000019-bouchard-2013-01.yaml).

- `reproduce_bouchard_2013.ipynb`: the analysis. It takes about 15 minutes, 11 of them streaming
  about 42 GB of raw ECoG and computing high gamma.
- `bouchard.py`: streaming the files, high gamma, the paper's articulator and phonetic feature
  matrices, and the measures (partial correlation, GLM, state space, co-clustering, separability).
  Other notebooks on this dandiset can import it.
