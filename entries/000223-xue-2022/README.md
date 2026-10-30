# Xue, Buccino, Saseendran Kumar, Hierlemann & Bartram (2022) from dandiset 000223

Tests the findings of [Xue et al. (2022)](https://doi.org/10.1088/1741-2552/ac8765) on
[DANDI:000223](https://dandiarchive.org/dandiset/000223/0.260528.0906), which holds 19 paired
recordings of dendritic spine Ca2+ imaging and HD-MEA spiking in rat cortical cultures, with the
sorted units and the spine and shaft ROIs. The notebook recomputes each spine's best-matching unit,
the surrogate acceptance test, the F-score grids of simulated ground-truth connections and the
network measures of Table 1.

| Claim | Outcome |
|---|---|
| 19 recordings in 10 cultures, 20 spines, 102 ± 43 units | Reproduced |
| Per-spine best-R of Table 1 | Partially reproduced |
| Best-R has the largest gap to the next R (Figure 1e) | Reproduced |
| Per-recording maximum F and optimal quantiles of Table 1 | Partially reproduced |
| Mean maximum F of 0.692 ± 0.136 | Partially reproduced |
| 9 of 20 connections accepted | Partially reproduced |
| Accepted connections have larger best-R | Partially reproduced |
| Best-R alone does not predict acceptance | Partially reproduced |
| Three rejection scenarios (Figure 5a) | Reproduced |
| Test threshold above GT threshold for some recordings, below for others | Reproduced |
| Spike contrast and OUT/IN ratio of Table 1 | Not reproduced |
| Spike contrast correlates with maximum F (Figure 5c) | Reproduced |
| OUT/IN ratio correlates with maximum F (Figure 5d) | Partially reproduced (assumption: noise region) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The background regions the paper used to estimate the imaging noise are not in the dataset, so
three regions near each spine are placed by a fixed rule and each is run. The files carry no link
to the rows of Table 1; they are matched by culture and unit count. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000223-xue-2022-01.yaml`](../../attempts/000223-xue-2022-01.yaml).
