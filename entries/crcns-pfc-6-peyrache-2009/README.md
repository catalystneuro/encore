# Peyrache, Khamassi, Benchenane, Wiener & Battaglia (2009) from CRCNS pfc-6

Tests the findings of [Peyrache et al. (2009)](https://doi.org/10.1038/nn.2337) that can be tested on
[CRCNS pfc-6](https://doi.org/10.6080/K0KH0KH5), which holds the prefrontal spike trains, cell types,
behaviour, position, and awake and SWS intervals of 86 sessions from four rats. It holds no LFP, no
sharp-wave ripple, delta-wave or spindle times, and no tetrode of each cell, so the analyses of
Figures 5 to 7 and the same-tetrode control cannot be repeated.

| Claim | Outcome |
|---|---|
| 1,692 cells in 63 sessions | Not reproduced (56 sessions, 1499 cells under the inclusion rule) |
| Rules learned by each rat | Not reproduced |
| Ten learning sessions by the paper's definition | Not reproduced |
| 323 signal and 811 nonsignal components | Partially reproduced |
| Reactivation higher in post than pre SWS, all signal groups | Reproduced |
| Replay concentrated in SWS (Supplementary Fig. 5) | Partially reproduced |
| Pre and post SWS alike in duration and firing rate | Reproduced (LFP measures not testable) |
| Reactivation correlates with encoding strength, r squared 0.61 | Not reproduced |
| Weaker relation in pre SWS | Partially reproduced |
| Post distributions more skewed | Not reproduced |
| 40 to 50% of net reactivation above the 99th percentile | Partially reproduced |
| Patterns do not coactivate in sleep, do awake | Reproduced |
| Shuffle control | Partially reproduced |
| Reactivation before DOWN to UP transitions | Reproduced, resting on an assumption |
| Behaviour unchanged by learning | Reproduced |
| SPWR, delta, spindle and same-tetrode analyses (14 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-pfc-6-peyrache-2009-01.yaml`](../../attempts/crcns-pfc-6-peyrache-2009-01.yaml).

- `reproduce_peyrache_2009.ipynb`: the analysis. It takes about two minutes, most of it streaming
  the 295 MB archive.
- `pfc6.py`: streaming and parsing the archive, the awake templates and reactivation strengths of
  the Online Methods, the closed-form shuffle mean, and the behavioural criteria. Other notebooks on
  this data set can import it.
