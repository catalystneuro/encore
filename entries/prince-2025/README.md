# Prince, Cushing, Yassine, Katragadda, Roberts & Singer (2025) from dandiset 001371

Tests the findings of [Prince et al. (2025)](https://doi.org/10.1038/s41467-025-60122-8) that can be
tested on [DANDI:001371](https://dandiarchive.org/dandiset/001371/0.260831.0201), which holds the
units, behaviour and LFP of 66 sessions from 7 mice in a virtual y-maze with switch and stay cues.

The outcome of every claim, with the reasons and the differences from the paper's method, is in the
attempt record [`attempts/prince-2025-01.yaml`](../../attempts/prince-2025-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

- `reproduce_prince_2025.ipynb`: the analysis. It takes about 25 minutes, most of it streaming the
  units, trials, behaviour and one LFP channel of each file.
- `prince2025.py`: loading, track linearization, the Bayesian encoder and decoder, alignment to the
  update cue, theta phase, and the mixed models with Tukey contrasts. Other notebooks on this
  dandiset can import it.

The behaviour reproduces the paper's trial counts exactly, and most findings on position decoding in
CA1 reproduce. The units of five sessions carry no brain region or cell type. The LSTM choice
estimate (Figure 4 onward) needs about 18 models of 20 epochs per session on unresampled behaviour;
the notebook times one session, and it and the 18 claims built on it are blocked as too large.
