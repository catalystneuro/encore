# Zhuang, Lemak, Sridhar & Nelson (2025) from DANDI:001177 and its Zenodo deposit

Tests the findings of [Zhuang et al. (2025)](https://doi.org/10.1093/brain/awaf312) on
[DANDI:001177](https://dandiarchive.org/dandiset/001177/0.250902.2127), which holds the striatal
recordings of Figures 4, 6 and S5 and S8, and on the paper's
[Zenodo deposit](https://doi.org/10.5281/zenodo.15258978), which holds its behaviour, histology,
rotarod and slice data.

The dandiset holds raw voltage, LFP and per-electrode threshold crossings for the paper's 18 mice,
but no sorted units, unit classes, optical labels, laser times or injection times, so the 14
electrophysiology claims are blocked. Of the 30 claims on the Zenodo data, 28 are tested, each
operant session recounted from its raw log.

| Claims | Outcome |
|---|---|
| Delayed/large choices at baseline, under PPX and A77636, and over repeated dosing (9 claims) | 9 reproduced |
| Washout, omissions and choice latencies (4 claims) | 1 reproduced, 3 partially reproduced (PPX washout rests on how the Bonferroni comparisons are made) |
| Hyperbolic fit parameters A, K and AUC (PPX, A77636, DREADD) | 1 reproduced, 1 partially reproduced, 1 not reproduced |
| DREADD delay discounting (mCherry, hM4Di, hM3Dq) | 1 reproduced, 1 partially reproduced |
| Rotarod, SNc cell counts, slice validation | 3 reproduced |
| Striatal TH loss | Partially reproduced |
| Correlations of A and K with TH (3 claims) | 2 reproduced, 1 not reproduced |
| Instrumental learning | Partially reproduced |
| Open field after A77636 and after CNO | 1 reproduced, 1 partially reproduced (both assume the injection time) |
| Sex differences; PPX open field | Blocked: sex not recorded; no PPX open field file |
| Electrophysiology (14 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001177-zhuang-2025-01.yaml`](../../attempts/001177-zhuang-2025-01.yaml).

- `reproduce_zhuang_2025.ipynb`: the analysis. It takes about 18 minutes, most of it opening the 56
  NWB files to list their contents and reading the open field workbooks.
- `icd.py`: listing the dandiset, reading the Zenodo files, parsing the operant logs with the event
  names of the paper's code, the hyperbolic fit, and the statistics. Other notebooks on these data
  can import it.
