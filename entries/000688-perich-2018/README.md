# Perich, Gallego & Miller (2018) from dandiset 000688

Tests the findings of [Perich et al. (2018)](https://doi.org/10.1016/j.neuron.2018.09.030) that can
be tested on [DANDI:000688](https://dandiarchive.org/dandiset/000688/0.250122.1735). The dandiset
holds the Baseline epoch of the dual-array center-out sessions of Monkeys C and M, about 200 reward
trials each. The curl field, visuomotor rotation and Washout trials are not in it, and nothing marks
which sessions are the paper's.

| Claim | Outcome |
|---|---|
| Units per session and units above 5 Hz | Partially reproduced (assumed) |
| PMd has more dimensions than M1 (medians 14 and 8.5) | Reproduced (assumed); partially reproduced proposed under one kernel reading for all claims |
| PMd stays higher-dimensional in subsamples of equal size | Reproduced (assumed) |
| The null/potent index is centered on zero | Reproduced (assumed) |
| Output-null activity leads output-potent by 35 ms in Baseline | Partially reproduced (assumed) |
| 23 claims on the Force, Rotation and Washout trials | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The record, with the assumptions, the differences from the paper's method and the findings about the
dataset, is [`attempts/000688-perich-2018-01.yaml`](../../attempts/000688-perich-2018-01.yaml).

- `reproduce_perich_2018.ipynb`: the analysis. It takes about 20 minutes, two of them reading the
  metadata of all 111 files.
- `perich.py`: loading the sessions, binning and smoothing, PCA, the output-potent and output-null
  subspaces, the dimensionality estimate, the null/potent index and the lag. Other notebooks on this
  dandiset can import it.
