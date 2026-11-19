# Huszár, Zhang, Blockus & Buzsáki (2022) from dandiset 000552

Tests the findings of [Huszár et al. (2022)](https://doi.org/10.1038/s41593-022-01138-x) that can be tested
on [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.261113.1035), which holds the CA1 silicon-probe
recordings of 17 mice whose pyramidal neurons were birthdated by in utero electroporation (104 sessions),
with units, light-responsive labels, sleep states, SPW-Rs, LFP and maze position.

| Claim | Outcome |
|---|---|
| Cohort, sessions, units and light-responsive counts (4 claims) | Reproduced |
| Session count and durations | Not reproduced (two sessions hold wake only, no sleep) |
| SPW-R duration | Reproduced |
| Labelled fraction, firing rate, SPW-R firing and cofiring by birthdate (Figs 1e, 1g, 2b, 2f, 2g) | Reproduced |
| Burst index by birthdate (Fig. 1h) | Partially reproduced |
| Theta depth, theta-related rates (Figs 2d, 6c, 6d) | Reproduced, on an assumed theta channel |
| Theta cofiring (Fig. 2c) | Partially reproduced, on an assumed theta channel |
| REM shifting (Fig. 1f) | Not reproduced, on an assumed theta channel |
| Maze cohort and novel explorations | Reproduced |
| Maze trial counts | Not reproduced |
| Place maps on the familiar maze (Figs 5b to 5e) | Partially reproduced |
| Remapping of SBD pairs (Figs 5f, 6f) | Reproduced |
| Novel environments (Figs 6c bottom, 6d right, 6e) | One not reproduced (on an assumed open-field scale), two partially reproduced |
| Pyramidal-to-interneuron convergence (Fig. 7) | Two partially reproduced, two not reproduced, on an assumed detector |
| Depth control (Extended Data Fig. 3) | Not reproduced (fractions above the paper's), on an assumed depth reference |
| Histology, light-evoked waveforms, L-ratio controls (5 claims) | Blocked: data missing |
| Assemblies and network model (5 claims) | Blocked: too large (not run; see the attempt record) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/huszar-2022-02.yaml`](../../attempts/huszar-2022-02.yaml).

- `reproduce_huszar_2022.ipynb`: the analysis. It takes about 47 minutes, most of it reading two LFP channels
  per session for the theta analyses.
- `huszar.py`: streaming the files, the homecage, theta, maze and connectivity measures, and the bootstrap
  tests. Other notebooks on this dandiset can import it.
