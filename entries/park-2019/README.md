# Park, Keeley, Savin, Ranck & Fenton (2019) from CRCNS hc-20

Tests the findings of [Park et al. (2019)](https://doi.org/10.1016/j.neuron.2018.11.019) that can be
tested on [CRCNS hc-20](https://doi.org/10.6080/K0SF2TDN), which holds the spike trains of 115
medial entorhinal head-direction cells from 13 rats in stable, rotating and stable trials of a place
avoidance task, with the tracker files of those trials. The other MEC cells, the LFP and the
training sessions are not in it.

| Claim | Outcome |
|---|---|
| 115 head-direction cells from 13 rats (Table S1) | Partially reproduced |
| Head-direction cells fire at 1.41 AP/s | Reproduced |
| Rats learned the task (Figure 1A) | Blocked: data missing |
| Speed unchanged by rotation, lower in stable2 | Reproduced (assumption) |
| LFP power unchanged | Blocked: data missing |
| Firing rates maintained | Reproduced |
| Directional tuning degraded in both frames, more in the arena frame | Reproduced (assumption) |
| Change in preferred direction across trial pairs | Partially reproduced |
| Directional instability across trial pairs | Partially reproduced |
| Stable2 decoded better than rotation (seven ensembles) | Reproduced (assumption) |
| Four ensembles prefer the room frame, two the arena frame | Reproduced (assumption) |
| Frame preference anti-correlated with shock zone proximity | Partially reproduced |
| Frame preference not biased by head direction | Reproduced (assumption) |
| Head-direction pair correlations maintained | Reproduced |
| All MEC pair correlations maintained (Figure S4) | Blocked: data missing |
| Model-based head-direction information (Figure S5) | Blocked: data missing |
| Subclass pair correlations maintained (Figure S6) | Blocked: data missing |
| No angular velocity tuning | Not reproduced (assumption) |
| Internally referenced tuning preserved | Not reproduced |
| Arena-frame registration short-lived (Figure 4C) | Not reproduced |
| Decoding error inhomogeneous (Figure 5A, B) | Partially reproduced |
| Error minima at 110 and 350 degrees | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several files are wrong in ways the notebook shows: the rotating tracks of five sessions (one a
copy of another session's, four with frames that disagree in timing), one unit's rotating spikes
(a copy of its stable1 spikes), and the file list's stable2 column for one session. The
outcomes are decided on the files as deposited, as the paper's counts imply it used them; a clean
variant leaves these out, and four outcomes (Figures 1C directionality, 2, S2 and 4) change or lose
their margin without them. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/park-2019-01.yaml`](../../attempts/park-2019-01.yaml).

- `reproduce_park_2019.ipynb`: the analysis. It takes about two minutes, half of it streaming the
  zip.
- `hc20.py`: reading the TSD and tracker files from the zip in place, tuning measures, circular
  statistics, the repeated-measures ANOVA, the decoder of the paper's code, momentary directional
  information and internally referenced tuning. Other notebooks on this data set can import it.
