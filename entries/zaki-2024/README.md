# Zaki et al. (2024) from dandiset 000718

Tests the findings of [Zaki et al. (2024)](https://doi.org/10.1038/s41586-024-08168-4) that can be
tested on [DANDI:000718](https://dandiarchive.org/dandiset/000718/0.261122.2159), version
0.261122.2159. The dandiset holds two of the nine mice of the paper's calcium imaging and EEG/EMG
experiment (Figure 5, Extended Data Figures 9 and 10), Ca_EEG2-1 (1.5 mA) and Ca_EEG3-4 (0.25 mA),
with one offline recording per offline period. The mice of the one-hour offline experiments and of
the behaviour-only experiments are not in it.

| Claim | Outcome |
|---|---|
| The deposited mice are the source data's mice, with the same freezing | Reproduced |
| High-shock mouse froze more in aversive recall than low-shock mouse | Reproduced |
| Offline bursts more frequent than in circularly shifted data | Reproduced, under an assumption |
| Offline population activity more skewed than in circularly shifted data | Reproduced |
| Movement pauses about 1 s before bursts | Not reproduced |
| In wake, overlap co-bursts more with neutral than with aversive (high shock) | Partially reproduced |
| NREM and REM co-bursting, low-shock wake co-bursting, EEG cohort linking, sleep structure | Blocked: data missing |
| Findings of the other experiments (16 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The burst-frequency outcome turns on whether the shuffled population trace is z-scored again
before bursts are counted, which the paper does not say. After a reader's answer the criterion names
both readings: held to the true trace's threshold, the shuffles hold almost no bursts and the claim
is reproduced; z-scored again, they hold more bursts than the data. The outcome rests on the first,
which a synthetic check shows is also passed by cells that only share a slow drift, so it shows that
the cells co-vary, not that they burst. The wake co-bursting outcome rests on reading wake without
the dataset's quiet wake, which the files define as a waking state; with it, the order reverses. In Ca_EEG2-1 the behaviour sessions are timestamped about 1 h later
than the offline recordings and the telemetry, so that the first offline recording after fear
conditioning appears to start before it. The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/zaki-2024-02.yaml`](../../attempts/zaki-2024-02.yaml).

- `reproduce_zaki_2024.ipynb`: the analysis. It takes about six minutes, most of it the
  surrogates and reading the week of telemetry.
- `zaki.py`: streaming the files, freezing, burst detection, circular-shift surrogates, ensembles
  from the cell registration, movement from the telemetry, and sleep scoring of the continuous telemetry. Other notebooks on this dandiset can
  import it.
