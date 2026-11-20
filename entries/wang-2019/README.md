# Wang, Morotti, Tapa et al. (2019) from SPARC dataset 212

Tests the findings of [Wang et al. (2019)](https://doi.org/10.1113/jp278016) that can be tested on
[SPARC:212](https://sparc.science/datasets/212), version 1
([doi:10.26275/lok5-wje6](https://doi.org/10.26275/lok5-wje6)). The dataset holds the authors'
per-heart summary tables for Figures 1 (heart rate), 2, 3, 5F and 7F, and the MATLAB myocyte models
of Figure 8. It holds no optical maps or traces.

| Claim | Outcome |
|---|---|
| SNS raises heart rate in rabbit and mouse (Fig. 1A, 1D) | Reproduced |
| Rabbit APD and CaTD shorten, CaT amplitude rises; mouse APD prolongs (Fig. 1) | Reproduced, on the first 20 s of the Fig. 2 series; rabbit APD80 only on the majority reading (falls in 4 of 4 hearts, paired p = 0.13) |
| Rabbit HR, APD and CaTD change monotonically over 60 s (Fig. 2A) | Not reproduced: heart rate peaks at 20 s and is not monotonic, and CaTD80 is monotonic under one reading only; under that reading the result rests on one unadjusted step test of heart rate (p = 0.047) |
| Mouse APD is biphasic, 50.9, 60.6 and 46.5 ms at 0, 15 and 60 s (Fig. 2D) | Reproduced |
| CaT amplitude rises similarly in both species (Fig. 2C, 2F) | Reproduced |
| Tyramine and noradrenaline mimic SNS (Fig. 3B, 3C) | Reproduced; for noradrenaline under one reading of "monotonic" |
| Propranolol abolishes the SNS response (Fig. 3D) | Not reproduced |
| Rate steps give a biphasic APD, exaggerated by SNS (Fig. 3E) | Reproduced |
| At constant pacing SNS prolongs APD without a biphasic response (Fig. 3F) | Reproduced, resting on an assumption |
| Base-apex APD change differs in rabbit (Fig. 5F) and mouse (Fig. 7F) | Reproduced |
| Maps and paced 20 s series (Figs. 4 to 7, eight claims) | Blocked: data missing |
| Model simulations (Figs. 8 and 9, four claims) | Blocked: not runnable (MATLAB code, which the entry's Python environment cannot run) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/wang-2019-01.yaml`](../../attempts/wang-2019-01.yaml).

- `reproduce_wang_2019.ipynb`: the analysis. It takes under a minute.
- `sns.py`: reading the pinned files from the SPARC bucket, parsing the workbook into per-heart
  tables, and the paired t-tests, repeated measures ANOVA and monotonicity readings used by the claims.
