# de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli & de Vasconcelos (2026) from dandiset 000713

Tests the findings of [de Paula et al. (2026)](https://doi.org/10.1103/wndc-k654), "Revealing
Stimulus-Dependent Dynamics Through Statistical Complexity", on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual
Behavior Neuropixels dataset. The notebook streams all 153 ecephys sessions and computes, for every
local population and 100-s window, the CV, permutation entropy and statistical complexity of the
population rate, with ISI-shuffled surrogates, JS divergences between regions, complexity-CV
trajectories and mean pairwise correlations.

| Claims | Outcome |
|---|---|
| CV by condition in visual cortex and thalamus; complexity time course by area; thalamic, hippocampal and midbrain complexity by condition; C-H spans of thalamus, hippocampus and midbrain; complexity separates images from spontaneous activity (13 claims) | Reproduced |
| CV against surrogates; CV correlation modules and hubs; hippocampal and midbrain CV; JS of CV in visual cortex and DG/CA3; reference systems; visual C-H plane; complexity by condition in visual cortex; JS of complexity in natural images; parameter robustness; complexity-CV coupling in visual cortex, thalamus and midbrain (15 claims) | Partially reproduced |
| Table I counts; CV medians by region; surrogate CV correlations; JS of CV in hippocampus and midbrain and in the Fig. 2b legend; complexity range fractions; JS of complexity in active behavior, blanks and spontaneous activity; hippocampal spontaneous complexity; mean pairwise correlation (10 claims) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's 102 sessions and its unit selection are not stated, and neither reading of them in the
claims file reproduces its counts (Table I). The notebook uses all 153 sessions and all units, the
reading that keeps Table I's 26 subregions, so almost every outcome rests on that assumption. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/paula-2026-01.yaml`](../../attempts/paula-2026-01.yaml).

The notebook takes about 40 minutes, most of it reading the spike times from the archive.
