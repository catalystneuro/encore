# Sabatini & Kaufman (2024) from dandiset 000070

Tests the findings of [Sabatini & Kaufman (2024)](https://doi.org/10.1038/s41467-024-51308-7) on
[DANDI:000070](https://dandiarchive.org/dandiset/000070/0.260528.0919), version 0.260528.0919, which holds
the two maze-task sessions the paper names (monkey J, 2009-09-18; monkey N, 2010-09-23), each with a PMd
and an M1 Utah array and hand position. The notebook rebuilds the paper's four datasets (M1-J, PMd-J,
M1-N, PMd-N) and tests its claims on jPCA, single-condition dynamics, the temporal basis factorization,
the orientation of rotational planes, the state space location, and LDR encoding and decoding.

| Group | Outcomes |
|---|---|
| Reproduced | 11 claims, among them the factorization's variance explained, the misalignment of rotational planes across conditions, the segregation of frequencies, prediction of rotations from each other and from the location, and LDR encoding against standard encoding models |
| Partially reproduced | 12 claims, among them LDR decoding, the time-shuffle control, and the comparison with instantaneous decoders, run without the GPFA decoders |
| Not reproduced | 11 claims, among them the eigenvalue frequencies and distances, the basis frequencies, the single-LDS fit, the dimensionality of rotation orientations and location, and the warping control |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The dandiset's units are one per electrode, with no single- or multi-unit label, where the paper used
sorted units; the Nitschke file joins five recording segments whose clocks overlap, and in the Jenkins
file one unit's spike train continues in the next unit's row. The main notebook
uses all successful trials; `reproduce_sabatini_2024_trials_b.ipynb` runs the same analyses on trials
with a delay above 400 ms, the claims file's other reading, and every outcome is the same.
`reproduce_sabatini_2024_stable_units.ipynb` leaves out three units whose spike trains are not one stable
unit's (in the Jenkins file, unit 0's train continues in unit 1's row; in the Nitschke file, unit 170 fires
above 100 spikes/s on 229 trials of one segment), and every outcome is the same except
fig6e-kinematics-predict-location, for which the record proposes a change. The attempt record,
with the reasons, the differences from the paper's method and the findings about the dataset, is
[`attempts/sabatini-2024-01.yaml`](../../attempts/sabatini-2024-01.yaml).

Run with `python tools/entry.py run entries/sabatini-2024`; it streams about 1 GB of spike times and hand
position and the three notebooks take about 25, 15 and 25 minutes.
