# Najafi et al. (2020) on dandiset 000016

Tests the findings of [Najafi et al. (2020)](https://doi.org/10.1016/j.neuron.2019.09.045) that can
be tested on [DANDI:000016](https://dandiarchive.org/dandiset/000016/0.260915.2309). The dandiset
holds 135 two-photon imaging sessions from 4 mice: the inferred spiking activity of each good ROI,
segmented by trial and aligned to trial events, the ROI classes (excitatory, inhibitory, unknown),
and the trial tables. Fluorescence traces, raw movies and histology are not in it.

| Claims | Outcome |
|---|---|
| Data description, psychometric curve, selectivity with matched activity, decoders of equal accuracy, mixed populations, stability, same-preference correlations (7) | Reproduced |
| Selectivity magnitude, decoder weights through the trial, correlations in learning (3) | Partially reproduced |
| Activity difference between types, example session counts, fraction selective, wider window, correct-error correlation, decoder time course, incorrect-trial decoding, learning accuracy and onset, learning in parallel, equal trials, running, pseudo populations in learning, threefold increase of selective neurons (14) | Not reproduced |
| Selectivity time course, inhibitory correlations, pseudo populations (3) | Blocked: the readings the criterion names disagree |
| Trial history (no ITI), fluorescence decoding, neuropil, histology (4) | Blocked: data missing |
| Previous choice and stimulus, outcome decoding, temporal dynamics, the three circuit models (6), decoder angles (1) | Blocked: not run in the time, or too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The traces named `dFoF_*` hold the inferred spiking activity, not Delta F/F, and the trial times are
relative to each trial. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/najafi-2020-01.yaml`](../../attempts/najafi-2020-01.yaml).

- `01_single_neurons_correlations.ipynb`: data checks, behaviour, single-neuron ROC and noise
  correlations, about 30 minutes, most of it streaming.
- `02_decoders.ipynb`: choice decoders in every session at the bin before the choice, about 40 minutes.
- `03_learning_decoders.ipynb`: decoder time courses, per-bin weights and the learning analysis, about 50 minutes.
- `04_time_course_per_bin_C.ipynb`: the decoder time course for mice 2 and 3 with C chosen at every bin, about 20 minutes.
- `najafi.py`: streaming and loading, the ROC, decoder, correlation and learning measures. Other
  notebooks on this dandiset can import it.
