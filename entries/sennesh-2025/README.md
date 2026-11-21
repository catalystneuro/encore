# Sennesh, Westerberg, Spencer-Smith & Bastos (2025) from dandiset 000253

Tests the findings of [Sennesh et al. (2025)](https://doi.org/10.1101/2025.07.31.667946) on
[DANDI:000253](https://dandiarchive.org/dandiset/000253/0.240923.1441), the Allen Institute
OpenScope Global/Local Oddball recordings: 14 mice, six Neuropixels probes each in V1, LM, RL, AL,
PM and AM, with LFP, stimulus tables and eye tracking.

| Claims | Outcome |
|---|---|
| Trial counts | Partially reproduced |
| Gamma increase in all three oddball contrasts (V1) | Reproduced |
| V1 condition spectrograms (Figures 2, 3, 4 a and b) | 2 partially reproduced, 1 not reproduced |
| V1 cluster-tested contrasts (Figures 2c, 3c, 4c) | 2 reproduced, 1 partially reproduced |
| V1 laminar panels (Figures 2d-f, 3d-f, 4d-f) | 1 reproduced, 5 partially reproduced, 1 not reproduced |
| Trough-locked CSD patterns (Figures 2g-i, 3g-i, 4g-i) | 5 reproduced, 4 not reproduced, all resting on an assumption |
| Gamma and theta peaks, V1 and LM | 4 reproduced (one sensitive to the seed), 1 partially reproduced |
| Aperiodic components (Supplementary Figures 1 and 3) | 2 reproduced, 1 not reproduced |
| Alpha/beta and gamma peak heights (Supplementary Figure 2) | 1 reproduced, 1 not reproduced |
| L2/3 gamma by area (Figure 5) | 2 not reproduced |
| Pupil (Supplementary Figure 4) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper cites version 0.240503.0152, in which the LFP of 7 of the 14 mice cannot be put on the
stimulus clock (its timestamps are not in seconds), two pairs of mice hold nearly the same LFP, and
one mouse has one LFP channel in four. Version 0.240923.1441 replaced those files, and this entry
uses it. The stimulus tables have no block or condition labels; the conditions are rebuilt from
the grating sequences. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/sennesh-2025-01.yaml`](../../attempts/sennesh-2025-01.yaml).

- `v1_laminar.ipynb`: the data checks and the V1 claims (spectrograms, cluster tests, laminar
  panels, trough-locked CSD, gamma and theta peaks, pupil). About 17 minutes, most of it streaming
  the V1 LFP of 14 mice.
- `areas.ipynb`: the claims across the six areas (aperiodic components, spectral peaks, L2/3 gamma
  of Figure 5). About 35 minutes.
- `glo.py`: streaming the LFP by its HDF5 chunks, rebuilding the conditions, the channel alignment,
  spectrograms, FOOOF, the cluster permutation test and the trough-locked CSD.
