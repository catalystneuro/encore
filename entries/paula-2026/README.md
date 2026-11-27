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
| CV modules and DG/CA3 hubs of Fig. 1e; CV by condition in visual cortex, thalamus and hippocampus; complexity time course by area; C-H spans of thalamus, hippocampus and midbrain; hippocampal and midbrain complexity by condition; complexity separates images from spontaneous activity (12 claims) | Reproduced |
| CV medians by region; CV against surrogates; summed JS of CV in visual cortex; JS of CV among visually driven conditions; reference systems; parameter robustness (6 claims) | Partially reproduced |
| Table I counts; surrogate CV correlations; midbrain CV correlations; midbrain CV; JS of CV in hippocampus, midbrain, DG/CA3 and the Fig. 2b legend; visual C-H plane; complexity range fractions; complexity by condition in visual cortex and thalamus; JS of complexity in every condition; complexity-CV coupling in every area; mean pairwise correlation (20 claims) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's 102 sessions and its unit selection are not stated. All 153 sessions are used. Every
claim is run under three unit selections: the claims file's two (all units, and ISI violations,
amplitude cutoff and presence ratio filters) and the unit filter of the Allen Institute's Visual
Behavior Neuropixels tutorial (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s). The last is
adopted, as its neurons per population match Table I within 5% in each area; ten outcomes would
differ under one of the other two. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/paula-2026-01.yaml`](../../attempts/paula-2026-01.yaml).

The notebook took 34 to 43 minutes in the runs of this attempt, most of it (33 to 42 minutes) reading the spike times from the archive.
