# Ostadsharif Memar & Dehghani (2026) on AJILE12, dandiset 000055

Tests the iEEG findings of [Ostadsharif Memar & Dehghani (2026)](https://doi.org/10.48550/arxiv.2606.11415),
"Spatially Masked Regression Reveals Local and Distributed Predictability in Electrophysiological
Recordings", on [DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which
holds the intracranial recordings and wrist movement events of the paper's 12 subjects. The paper's
scalp EEG dataset is not in the dandiset. The trials are built from the `ReachEvents` times: in three
files the `reaches` table is offset from the recording's clock by the session's start time.

| Claim | Outcome |
|---|---|
| Intra-subject iEEG DistCorr 0.553 ± 0.068 | Reproduced |
| Intra-subject values per subject (Table II) | Partially reproduced |
| Cross-subject iEEG DistCorr 0.389 ± 0.064 | Reproduced (on preprocessing before segmentation) |
| Cross-subject values per subject (Table II) | Not reproduced |
| Cross-subject below intra-subject | Reproduced (on preprocessing before segmentation) |
| DistCorr falls as more of the neighbourhood is masked | Reproduced |
| Reconstruction stays above zero with the neighbourhood masked | Reproduced (on an assumed reading) |
| All > Local > Non-local electrodes as predictors | Not reproduced |
| Surrogates reduce DistCorr to 0.181, 0.232 and 0.201 | Reproduced |
| Phase shuffling degrades most, IAAFT retains more | Not reproduced |
| Lagged predictors barely change DistCorr | Reproduced |
| Nine EEG claims | Blocked: not runnable in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Three notebooks, each loading the data again: `reproduce_memar_2026.ipynb` (data check,
intra-subject and cross-subject), `masking_coverage.ipynb` and `surrogates_lagged.ipynb`. The
helper `smr.py` holds the loading, preprocessing, model and measures, with the source of every
parameter. The attempt record is [`attempts/memar-2026-01.yaml`](../../attempts/memar-2026-01.yaml).
