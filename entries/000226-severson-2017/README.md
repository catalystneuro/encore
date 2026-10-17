# Severson, Xu, Van de Loo, Bai, Ginty & O'Connor (2017) from dandiset 000226

Tests the findings of [Severson et al. (2017)](https://doi.org/10.1016/j.neuron.2017.03.045) that can
be tested on [DANDI:000226](https://dandiarchive.org/dandiset/000226/0.230607.1747), which holds 56
trigeminal afferent recordings with high-speed whisker video and 4 EMG sessions, one file each,
matching the paper's Table S1.

| Claim | Outcome |
|---|---|
| The recordings match Table S1 | Reproduced |
| Video frame counts (54.6 and 65.3 million) | Reproduced |
| Minutes of Merkel recordings (823 and 846) | Reproduced |
| Non-whisking rate 0.0 Hz | Reproduced |
| Contact rate 48.0 Hz, all afferents touch-responsive | Reproduced |
| 13 WT* afferents, whisking-in-air rate 19.1 Hz | Reproduced |
| Merkel and SA contact responses are direction selective | Partially reproduced |
| Full model of touch responses, r = 0.71 | Reproduced |
| Moment or its rate of change alone, r = 0.45 and 0.42 | Reproduced |
| Moment and its rate of change the best pair, r = 0.63 | Partially reproduced |
| Viscoelastic model comparable to the moment model | Reproduced |
| Phase modulation of WT* afferents, 2.1 against 51.2 Hz | Reproduced |
| Preferred phases span the whisk cycle | Partially reproduced |
| Preferred phase invariant to amplitude, frequency and setpoint | Reproduced |
| Kinematic models predict phase tuning, r = 0.97 | Reproduced (15 of 28 afferents) |
| Nasolabialis motor units follow negative velocity | Reproduced |
| Curvature noise 7.8% | Reproduced |
| Progressive cutting and 28-afferent phase claims (four) | Blocked: metadata insufficient |
| Intrinsic protractor EMG, cut lengths, optogenetic tagging, histology, contact curation (seven) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not say which experiment a recording belongs to, the afferent type or which afferents
are Merkel afferents; these come from Table S1 of the paper's Supplemental Information. The
progressive cutting recordings label every trial `intact`, so the cutting experiment cannot be
tested. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000226-severson-2017-01.yaml`](../../attempts/000226-severson-2017-01.yaml).

- `reproduce_severson_2017.ipynb`: the analysis. It takes about 13 minutes, half of it reading the
  13.7 GB of files into memory.
- `merkel.py`: loading, the Glossary's categories and classes, phase tuning, the spline models
  that stand in for the paper's GAMs, the viscoelastic model, and Table S1. Other notebooks on this
  dandiset can import it.
