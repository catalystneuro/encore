# Markowitz et al. (2023) on dandiset 000559

Tests the findings of Markowitz, Gillis, Jay et al. (2023), "Spontaneous behaviour is structured by
reinforcement without explicit reward" (Nature 614, 108-117, doi:10.1038/s41586-022-05611-2), on
DANDI:000559 version 0.261113.1911. The claims are in `claims/markowitz-2023.yaml` and the outcomes
in `attempts/markowitz-2023-02.yaml`.

- `photometry.ipynb`: the dLight photometry findings of Figs. 1 and 2 and Extended Data Figs. 2, 3
  and 7 (DLS dopamine at syllable transitions, its relation to velocity, to syllable use and to
  sequence entropy, and DMS against DLS). About 25 minutes.
- `optoda.ipynb`: the closed-loop Opto-DA findings of Fig. 3 and Extended Data Fig. 10 (target
  reinforcement, learners, sequence entropy, kinematics, duration, place preference). About 4
  minutes.
- `markowitz.py`: streaming loaders for the dandiset's NWB files and the shared measures.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The food-reward and calibration sessions are not in the dandiset, so the claims on them are
blocked; the encoding, decoding and reinforcement-learning models and several Opto-DA panels were
not run within the time of the attempt.

Run with `python tools/entry.py run entries/markowitz-2023`.
