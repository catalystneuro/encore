# Knierim, McNaughton & Poe (2000) from dandiset 001754

Tests the findings of [Knierim et al. (2000)](https://doi.org/10.1038/72910) that can be tested on
[DANDI:001754](https://dandiarchive.org/dandiset/001754/0.260728.1352), which holds sorted units,
task epochs, the original rate maps and the position at spike times of three rats recorded before
and during the Neurolab shuttle mission (STS-90). The paper is not open access: the claims come from
its abstract, the titles of its figures, and the dandiset's description of its findings.

| Claim | Outcome |
|---|---|
| A robust spatial code on the Escher staircase in flight | Partially reproduced (a change to not reproduced is proposed) |
| The code covers each of the three orthogonal surfaces | Blocked: metadata insufficient |
| Spatial information in flight comparable to preflight | Reproduced |
| Abnormal spatial selectivity on flight day 4 | Not reproduced |
| Place fields stable across sessions | Reproduced |
| Normal theta in flight | Blocked: data missing |
| Normal sharp waves and ripples in flight | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The Rat1 and Rat2 files of each flight day share one position trace, and Rat2's units are not
spatially selective with it. The description places the preflight recordings on a flat
rectangular track, but the files label them as Escher staircase and Magic Carpet epochs. The rate
maps cannot be linked to units, and there is no EEG. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001754-knierim-2000-01.yaml`](../../attempts/001754-knierim-2000-01.yaml).

- `reproduce_knierim_2000.ipynb`: the analysis. It takes about five minutes; its last code cell prints the run
  time (5.1 minutes in the latest run).
- `neurolab.py`: loading the files, the original rate maps and their spatial information, and the
  spike-based spatial information with its shuffle test. Other notebooks on this dandiset can import
  it.
