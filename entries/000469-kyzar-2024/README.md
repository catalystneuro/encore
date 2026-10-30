# Kyzar et al. (2024) from dandiset 000469

Tests the technical validation of [Kyzar et al. (2024)](https://doi.org/10.1038/s41597-024-02943-8),
a data descriptor, on [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.240123.1806), which
holds the screening and Sternberg working memory sessions of 21 subjects (1809 units).

| Claim | Outcome |
|---|---|
| 41 sessions from 21 subjects, one without screening | Reproduced |
| 902 Sternberg units, by area | Reproduced |
| 907 screening units, 449 in the MTL | Reproduced (the MTL count is 421) |
| Mean accuracy 88.73% | Reproduced |
| Reaction time grows with load, F(2,40) = 7.92 | Reproduced |
| Accuracy falls with load | Reproduced |
| ISI violations 0.41 ± 0.50% | Reproduced (with the code's filter) |
| Firing rate 2.55 Hz, 0.11 to 33.82 Hz | Reproduced |
| Projection distance 13.77 ± 7.32 | Reproduced |
| Peak SNR 6.62 ± 3.63 | Reproduced |
| CV2 0.94 ± 0.14 | Reproduced |
| Median isolation distance 31.14 | Reproduced |
| Screening concept cells, MTL 138 (32.78%) | Reproduced |
| Screening concept cells, MFC 26 (5.35%) | Reproduced |
| Figure 4 example units are concept cells | Reproduced |
| Sternberg concept cells, MTL 94 (20.94%) | Reproduced |
| Persistent activity of concept cells, 4.76 against 2.67 Hz | Not reproduced |
| Figure 5 example units | Reproduced |
| MFC maintenance cells 144 (31.79%) | Reproduced |
| MFC probe cells 122 (26.93%) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The persistent activity values in the paper are recovered exactly from the firing rates in the
Encoding 1 window, not the maintenance window the text names. The selection counts use the
permutation tests of the Methods; the paper's own code uses parametric tests, which give the
paper's counts exactly and are shown as variants. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000469-kyzar-2024-01.yaml`](../../attempts/000469-kyzar-2024-01.yaml).

- `reproduce_kyzar_2024.ipynb`: the analysis. Its last cell prints its run time, 3.6 minutes in
  the recorded run.
- `sternberg.py`: loading the files without their waveforms, the spike sorting measures of the
  paper's code, window rates, and the concept, maintenance and probe cell tests. Other notebooks
  on this dandiset can import it.
