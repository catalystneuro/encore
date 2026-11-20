# Lesica, Jin, Weng, Yeh, Butts, Stanley & Alonso (2007) from dandiset 002028

Tests the findings of [Lesica et al. (2007)](https://doi.org/10.1016/j.neuron.2007.07.013) on
[DANDI:002028](https://dandiarchive.org/dandiset/002028/0.261102.1631), which holds cat LGN units
recorded during natural movies and binary white noise at two contrasts, with the stimulus frames. The
paper's data are the Expt1 and Expt2 recordings.

Of 38 claims, 16 are reproduced, 7 partially reproduced and 15 not reproduced; none is blocked. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/lesica-2007-01.yaml`](../../attempts/lesica-2007-01.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

- `reproduce_lesica_2007.ipynb`: the analysis. It takes about 47 minutes, most of it estimating
  receptive fields for 143 units in four parallel processes (at the frame rate under three ridge
  penalties, and at 128 Hz for the temporal properties).
- `lesica.py`: loading the files and the stimulus library, receptive field and nonlinearity
  estimation, and the measures of the paper, each parameter with its source. Other notebooks on this
  dandiset can import it.
