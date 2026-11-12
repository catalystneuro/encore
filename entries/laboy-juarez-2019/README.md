# Laboy-Juarez, Langberg, Ahn & Feldman (2019) from CRCNS ssc-9

Tests the findings of [Laboy-Juarez et al. (2019)](https://doi.org/10.1038/s41593-019-0448-6) on
[CRCNS ssc-9](https://doi.org/10.6080/K0FJ2F13), which holds the spike times of single units in
mouse barrel cortex during single- and two-whisker stimulation in the paper's three experiments:
a survey of all two-whisker combinations in anesthetized mice (Figure 1), dense dt mapping of
CW-SW sequences in anesthetized mice (Figures 2 to 7) and a replication in awake mice (Figure 8).

| Experiment | Claims | Reproduced | Partially | Not reproduced | Blocked |
|---|---|---|---|---|---|
| 1, anesthetized survey | 10 | 9 | 1 | 0 | 0 |
| 2, dense dt mapping | 31 | 14 | 11 | 6 | 0 |
| 3, awake mice | 9 | 6 | 1 | 1 | 1 |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The unit counts of all three experiments match the paper. Single-whisker tuning, the preference
for CW-SW sequences, sublinear integration with near-linear best combinations, the inbound order
preference and the awake results mostly reproduce. The shuffle test of combination selectivity
finds more selective response sets than the paper (318 of 463, against 187 of 451) and, on a
null built from the real data, gives p < 0.05 for a quarter of the sets; every claim on the
selective group is also run on the 187 sets with the smallest p, which changes the outcome
of four claims, and of a fifth under one reading.
The dt smoothing classifies curves differently, and the population decoders of combination identity
and order fall short of the paper's accuracies. The paper's analysis code is available only on
request, so these methods rest on the Methods text. The behavioral claim is blocked: the files
hold no lick times.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/laboy-juarez-2019-01.yaml`](../../attempts/laboy-juarez-2019-01.yaml).

- `reproduce_laboy_juarez_2019.ipynb`: the analysis. It takes about 45 minutes, most of it the
  dt smoothing, the 5,000 shuffles per response set of experiment 2 and their calibration on a
  null built from the data.
- `lj2019.py`: streaming the zip from the CRCNS bucket and reducing each unit to spike counts per
  trial, with the Poisson responsiveness test, lifetime sparseness, the cross-validated dt
  smoothing, the shuffle test and the population decoders of the Methods.
