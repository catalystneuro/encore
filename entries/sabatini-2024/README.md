# Sabatini and Kaufman (2024) on DANDI:000070

Tests the findings of [Sabatini and Kaufman (2024)](https://doi.org/10.1038/s41467-024-51308-7),
"Reach-dependent reorientation of rotational dynamics in motor cortex", on
[DANDI:000070](https://dandiarchive.org/dandiset/000070/0.261122.2046) version 0.261122.2046, using the
two maze sessions the paper names (monkey J 2009-09-18, monkey N 2010-09-23). Four datasets are analysed
separately: M1-J, PMd-J, M1-N, PMd-N.

- `reproduce_sabatini_2024.ipynb`: data check, temporal basis factorization, single-condition dynamics,
  jPCA and the geometry of the rotations.
- `reproduce_sabatini_2024_kinematics.ipynb`: prediction of rotations, LDR encoding and single-trial LDR
  decoding.
- `ldr.py`: loading (streamed from the archive) and the measures, with the source of each parameter.

| Claims | Outcome |
|---|---|
| Factorization variance, shuffle control, recoverability; jPCA variance; single-condition LDS; location distinct from rotations; rotation and location prediction; location tracks direction; LDR encoding, its controls and decoding | Reproduced |
| Data composition; basis frequencies; jPCA R2; plane alignment and its jPCA link; frequency segregation; excursion angles; location alignment; kinematics predict location; curvature decoding | Partially reproduced |
| Duration warping; single LDS; eigenvalue clusters and distances; eigenvalues from kinematics; model comparison; jPCA variance correlation; orientation and location dimensionality; no output-potent dependence | Not reproduced |
| Decoder comparison of Figure 7f | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/sabatini-2024-02.yaml`](../../attempts/sabatini-2024-02.yaml). Among other things it reports
that the dandiset's units are unsorted threshold crossings, one per electrode, where the paper analysed
sorted single units and stable multi-units.
