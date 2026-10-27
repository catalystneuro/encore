# Tarduno, Cottrell & Zhou (2024) from Figshare 24639285

Tests the findings of [Tarduno, Cottrell & Zhou (2024)](https://doi.org/10.1038/s41597-024-03626-0)
on [Figshare 24639285, version 1](https://doi.org/10.6084/m9.figshare.24639285.v1). The item holds
magnetometer measurements of the 22 Apollo 64455 glass subsamples that failed the paleointensity
selection criteria (one workbook, one sheet per subsample) and the replicate measurements of twelve
single silicate crystals (one workbook each).

| Claim | Outcome |
|---|---|
| The deposit holds the 22 failed glass subsamples and the 12 crystals | Reproduced |
| Success rate of the glass experiments, 12% (3 of 25) | Reproduced |
| Table 2 fit statistics (n, MAD, R2, pTRM checks) | Partially reproduced (assumes averaged replicates) |
| Table 2 specimens with no fit acquire TRM irregularly | Reproduced |
| Figure 1: linear components in ss43 and ss19 | Reproduced (assumes averaged replicates) |
| Figure 2: changing directions in ss41 and ss22 | Reproduced (assumes averaged replicates) |
| Glass field-off directions are not random | Partially reproduced |
| AF cleaning did not change the NRM | Reproduced |
| Table 1 magnetization thresholds | Reproduced |
| Baseline of 0.2 to 0.5 uT | Reproduced |
| Technical Validation example for 14053g1 | Partially reproduced (the numbers are 12040g1's) |
| Crystal NRM replicates consistent, 590 C replicates and alteration checks not | Reproduced (three claims) |
| 14053g1 stable at 400 C | Reproduced |
| No alteration of the crystals | Reproduced |
| Impact magnetization and no long-lived dynamo | Blocked: interpretation, not tested |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The "replicates" in four glass sheets (g2, ss8, ss39, ss48) are one measurement multiplied by
factors near 1, not repeated measurements. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/figshare-24639285-tarduno-2024-01.yaml`](../../attempts/figshare-24639285-tarduno-2024-01.yaml).

- `reproduce_tarduno_2024.ipynb`: the analysis.
- `apollo.py`: loading the workbooks from Figshare, the Arai and directional measures (MAD, R2,
  pTRM checks, Fisher statistics, Watson's test), the check for scaled copies and the reading of
  the plotted points of the deposit's Supplementary Figure 1. Other notebooks on this dataset can
  import it.
