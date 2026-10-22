# Bouchard, Mesgarani, Johnson & Chang (2013) from dandiset 000019

Tests the findings of [Bouchard et al. (2013)](https://doi.org/10.1038/nature11911) that can be
tested on [DANDI:000019](https://dandiarchive.org/dandiset/000019/0.220126.2148), which holds raw
ECoG and hand-marked syllable annotations of subjects reading consonant-vowel syllables. High gamma
is computed here from the raw voltage. The audio and the electrode positions relative to the
central sulcus and Sylvian fissure are not in the dandiset.

| Claim | Outcome |
|---|---|
| Data composition (subjects, syllables, renditions, rate) | Partially reproduced |
| About 30 active vSMC electrodes per subject | Blocked: methods underspecified |
| Named electrodes of Fig. 1c-e | Blocked: metadata insufficient |
| Lips electrode active for /ju/ only (Fig. 1h) | Not reproduced |
| Spatial maps and their statistics (Fig. 2, Supplementary Figures 3, 5 and 7; seven claims) | Blocked: metadata insufficient |
| Mixed tuning at single electrodes | Reproduced |
| Timing sequence of articulator correlations | Not reproduced |
| Nine PCs explain about 60% of variance | Blocked: methods underspecified |
| Three k-means clusters most parsimonious | Blocked: methods underspecified |
| Co-clustering with articulators and vowels | Blocked: methods underspecified |
| Hierarchical clustering | Blocked: methods underspecified |
| Feature correlations, early and late | Blocked: methods underspecified |
| Separability timing | Not reproduced |
| Separability coupled to feature correlations | Blocked: methods underspecified |
| Consonant-vowel distances | Blocked: methods underspecified |
| PC articulator weights | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The claims blocked as methods underspecified depend on details the paper does not fix: which
syllables are averaged (all, or only those with 15 or more renditions), the baseline of the
z-scores, how the state-space input is z-scored, and which input is projected onto the PCs. They
were asked as questions (`questions/000019.yaml`), and the reader's answers, from the paper, left
them open, so every reading is run and the outcomes differ between readings. The separability
coupling is the exception: its outcomes differ between the claims file's own readings of the
clusters and of the feature set used, not between those of the details above. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/000019-bouchard-2013-01.yaml`](../../attempts/000019-bouchard-2013-01.yaml).

- `reproduce_bouchard_2013.ipynb`: the analysis. It takes about 21 minutes, about 16 of them streaming
  39 GB of raw ECoG and computing high gamma.
- `bouchard.py`: streaming the files, high gamma, the paper's articulator and phonetic feature
  matrices, and the measures (partial correlation, GLM, state space, co-clustering, separability).
  Other notebooks on this dandiset can import it.
