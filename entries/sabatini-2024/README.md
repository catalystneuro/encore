# Sabatini & Kaufman (2024) from dandiset 000070

Tests the findings of [Sabatini & Kaufman (2024)](https://doi.org/10.1038/s41467-024-51308-7) on
[DANDI:000070](https://dandiarchive.org/dandiset/000070/0.260528.0919), version 0.260528.0919, which holds
the two maze-task sessions the paper names (monkey J, 2009-09-18; monkey N, 2010-09-23), each with a PMd
and an M1 Utah array and hand position. The notebook rebuilds the paper's four datasets (M1-J, PMd-J,
M1-N, PMd-N) and tests its claims on jPCA, single-condition dynamics, the temporal basis factorization,
the orientation of rotational planes, the state space location, and LDR encoding and decoding.

| Group | Outcomes |
|---|---|
| Reproduced | 9 claims, among them the factorization's variance explained, the misalignment of rotational planes across conditions, prediction of rotations from each other and from the location, and LDR encoding |
| Partially reproduced | 16 claims, among them the comparison with instantaneous decoders, run without the GPFA decoders |
| Not reproduced | 9 claims, among them the eigenvalue distances, the single-LDS fit, the dimensionality of rotation orientations and location, and the warping control |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The dandiset's units are one per electrode, with no single- or multi-unit label, where the paper used
sorted units; the Nitschke file joins five recording segments whose clocks overlap. The attempt record,
with the reasons, the differences from the paper's method and the findings about the dataset, is
[`attempts/sabatini-2024-01.yaml`](../../attempts/sabatini-2024-01.yaml).

Run with `python tools/entry.py run entries/sabatini-2024`; it streams about 1 GB of spike times and hand
position and takes about 30 minutes.
