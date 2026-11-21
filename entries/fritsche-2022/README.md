# Fritsche, Solomon & de Lange (2022) from dandiset 000021

Tests the findings of [Fritsche et al. (2022)](https://doi.org/10.1523/JNEUROSCI.1350-21.2021) on
[DANDI:000021](https://dandiarchive.org/dandiset/000021/0.251116.2246), the Allen Brain
Observatory Visual Coding Neuropixels sessions of the Brain Observatory 1.1 stimulus set (32
mice), which the paper reuses.

| Claims | Outcome |
|---|---|
| Unit counts, 1-back adaptation to drifting gratings in cortex and thalamus (4) | Reproduced |
| Dependence of 1-back adaptation on orientation preference (Figure 2, four claims) | Reproduced |
| Long-term adaptation in V1, its double-exponential decay, half-life, cumulative and linear accumulation (5) | Reproduced |
| Short-term adaptation in thalamus, V1 against thalamus, decay fits per area (5) | Reproduced (two rest on an assumption) |
| Consistency across mice of long-term drifting adaptation | Reproduced |
| Consistency across mice of 1-back adaptation (drifting and static) and of long-term static adaptation (3) | Partially reproduced |
| Repeat and orthogonal suppression against a blank baseline (Figure 5) | Not reproduced |
| Static gratings, 1-back and long-term adaptation and decay fits (6) | Reproduced |
| Simulated neuron with only 1-back adaptation (Figure 8) | Not reproduced (depends on the seed) |
| Robustness to threshold, preferred-orientation trials and window | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/fritsche-2022-01.yaml`](../../attempts/fritsche-2022-01.yaml).

- `reproduce_fritsche_2022.ipynb`: the analysis. It takes about ten minutes; streaming the 32
  session files takes two to three of them.
- `adaptation.py`: streaming the files and reducing them to spike counts per unit and
  presentation, the responsiveness rule, the n-back adaptation ratios, the exponential decay fits
  and their bootstrap, and the mixed ANOVA. Other notebooks on this dandiset can import it.
