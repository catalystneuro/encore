# Zheng, Huszár, Hainmueller, Bartos, Williams & Buzsáki (2024) from dandiset 000552

Tests the electrophysiology findings of [Zheng et al. (2024)](https://doi.org/10.1016/j.celrep.2024.114702)
on [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.261113.1035), the CA1 silicon-probe
recordings of mice running a spontaneous alternation task on a figure-8 maze, three of which also ran
in novel mazes. It detects place fields and their step-like switches in 45 familiar and 8 novel
sessions. The two-photon imaging of Figure 7 is not deposited.

| Claim | Outcome |
|---|---|
| Population vectors decorrelate with trial lag (Fig. 1D) | Reproduced |
| Faster drift in novel environments over lags 1 to 10 (Fig. 1E) | Reproduced |
| No difference over lags 11 to 30 (Fig. 1E) | Reproduced |
| Field peak rates decorrelate, field locations stay correlated (Fig. 1H) | Reproduced |
| Field-location distance still grows with lag (Fig. 1I) | Reproduced |
| The 40% step filter removes 212 of 3,184 putative switching fields | Not reproduced |
| 19% of familiar and 31% of novel fields switch (Fig. 2D) | Not reproduced |
| Switching is graded by experience (Fig. 2E) | Reproduced |
| Step models beat polynomials for over 96% of fields (Fig. 3D to F) | Partially reproduced |
| Polynomials beat step models for population decorrelation (Fig. 3D to F) | Reproduced |
| Population vectors themselves favour gradual models (Fig. S4G) | Not reproduced |
| Switches are abrupt (Fig. 3K) | Reproduced |
| Switchers drive population drift (Fig. S5) | Reproduced |
| A GLM explains 20% and 14% of switching deviance (Fig. 4) | Partially reproduced |
| More switching in the delay zone (Fig. 4) | Not reproduced |
| Choice and speed do not predict switching (Fig. 4) | Not reproduced |
| Switching decreases with trial (Fig. 4D, 4I) | Partially reproduced, on an assumption |
| Speed does not change with trial (Fig. S8) | Not reproduced |
| Head scans are not related to switching (Fig. 4L to O) | Not reproduced |
| Splitter fields switch too (Fig. S9) | Reproduced |
| Signatures of BTSP (Fig. S13) | Partially reproduced |
| Switchiness is not a neuron property (Fig. 5C) | Reproduced |
| Relations to NREM firing rate (Fig. 5D) | Reproduced |
| 41 of 781 same-cell field pairs switch together | Not reproduced |
| Fields are stable after switching ON (Fig. S12) | Partially reproduced |
| Co-switching above chance in 17%/20% and 57%/29% of sessions (Fig. 6) | Not reproduced |
| Up to 5% of fields switch per trial (Fig. 6F) | Reproduced |
| Pre-existing fields before ON and after OFF (Fig. S14) | Partially reproduced |
| ChR2 expression does not affect switching (Fig. S2) | Reproduced |
| Imaging across days (Fig. 7, Fig. S15), two claims | Blocked: data missing |
| Neighbouring waveforms do not change across a switch (Fig. S1) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper cites version 0.230630.2304, whose units have no cell-type or light-responsive labels; the
attempt pins 0.261113.1035, a re-conversion of the same sessions with the same spike times and those
labels. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/zheng-2024-01.yaml`](../../attempts/zheng-2024-01.yaml).

- `reproduce_zheng_2024.ipynb`: the analysis. It takes about 30 minutes, 25 of them running the
  field and switch pipeline under five seeds in four processes.
- `switching.py`: loading the files, rate maps, place-field detection, optimal partitioning and
  switch detection, and head-scan detection, with the source of every parameter. Other notebooks on
  this dandiset can import it.
