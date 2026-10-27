# Mintal et al. (2024), the Volebny Kompas datasets, from Figshare item 24949470

Tests the findings of [Mintal et al. (2024)](https://doi.org/10.1038/s41597-024-03777-0) on
[Figshare item 24949470, version 1](https://doi.org/10.6084/m9.figshare.24949470.v1), which holds 134,699
responses to the Volebny Kompas voting advice application before the 2023 Slovak election, the positions of
11 parties on its 39 statements, Supplementary Table 1 and the paper's R code.

| Claim | Outcome |
|---|---|
| 134,699 responses with the columns of Table 1 | Reproduced |
| Responses gathered from 5 to 30 September 2023 | Partially reproduced (432 responses dated after election day) |
| 39 statements in three languages, 429 party positions | Reproduced |
| 11 parties | Reproduced |
| 4 parties placed themselves | Reproduced |
| Coders agree with weighted kappa 0.84 | Reproduced (assumed quadratic weights) |
| Placements on the uni-dimensions and the landscape match Figs. 2 and 3 | Partially reproduced |
| Party clustering matches Fig. 7 | Reproduced |
| Table 2: gender, age and education | Reproduced (three claims) |
| 40 under-18 and 400 aged 18-20 with university education | Partially reproduced (400 only) |
| S2 to S5 summary statistics | Reproduced (two claims) |
| Parallel analysis gives 11 factors | Reproduced |
| ML and principal axis solutions consistent, S1 and S3 load strongly | Partially reproduced (Pearson only; assumed thresholds) |
| The 11 parties were the top 11 vote recipients | Blocked: no pinned source of the results |
| 270,836 website views | Blocked: usage records not public |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The party workbook numbers statements 16 to 24 wrongly, and the R code removes 330 straight-line responses
that the paper does not mention; with that step Table 2 is reproduced exactly. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/figshare-24949470-mintal-2024-01.yaml`](../../attempts/figshare-24949470-mintal-2024-01.yaml).

- `reproduce_mintal_2024.ipynb`: the analysis. It takes about eighteen minutes, most of it the simulated
  and resampled reference data of the parallel analysis.
- `vk.py`: loading the files from Figshare, the row selections, the dimension scores, weighted kappa,
  polychoric correlations, parallel analysis and factor extraction with promax rotation.
