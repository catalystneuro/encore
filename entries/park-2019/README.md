# Park, Keeley, Savin, Ranck & Fenton (2019) from CRCNS hc-20

Tests the findings of [Park et al. (2019)](https://doi.org/10.1016/j.neuron.2018.11.019) that can be
tested on [CRCNS hc-20](https://doi.org/10.6080/K0SF2TDN), which holds the spike trains and 30 Hz
tracking of the 115 MEC head-direction cells (13 rats, 44 sessions) in the stable1, rotating and
stable2 trials, and the tracker files of each trial. The other MEC cells, the LFP, the waveforms and
the training sessions are not in it.

| Claim | Outcome |
|---|---|
| 115 head-direction cells from 13 rats, among 353 MEC cells and 556 pairs | Partially reproduced |
| Mean rate 1.41 AP/s | Reproduced |
| Avoidance learning curves (Figure 1A) | Blocked: data missing |
| Speed lower in stable2 only | Reproduced |
| LFP power unchanged | Blocked: data missing |
| Firing rates maintained | Reproduced |
| Directionality degraded in rotation, more in the arena frame | Reproduced (assumed) |
| Change in preferred direction across trial pairs | Partially reproduced |
| Directional instability across trial pairs | Partially reproduced (assumed) |
| Decoding accurate in stable2, poor in rotation | Reproduced (assumed) |
| 4 of 7 ensembles prefer the room frame, 2 the arena | Reproduced (assumed) |
| Idir anticorrelated with shock zone proximity | Partially reproduced |
| ΔIdir not biased by head direction | Reproduced (assumed) |
| Head-direction pair correlations maintained | Reproduced |
| All MEC pair correlations maintained (Figure S4) | Blocked: data missing |
| Model-based head-direction information (Figure S5) | Blocked: data missing |
| Subclass pair correlations (Figure S6) | Blocked: data missing |
| No angular velocity tuning | Not reproduced (assumed) |
| Internally referenced tuning preserved (Figure 4D) | Not reproduced |
| Arena-frame internal tuning falls beyond 10 s (Figure 4C) | Not reproduced (assumed) |
| Decoding error distributions inhomogeneous (Figure 5) | Partially reproduced |
| Error minima at 110 and 350 degrees | Reproduced (assumed) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data check found the stable2 column of FileNameList.xlsx shifted for five units of one
session, two pairs of trials from different days sharing their tracking, one stable1 file holding
its rotating trial's spikes, and undocumented codes for untracked samples. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/park-2019-02.yaml`](../../attempts/park-2019-02.yaml).

- `reproduce_park_2019.ipynb`: the analysis. It takes six to eight minutes, about five of them for
  the internally referenced tuning of Figure 4; it prints both times.
- `hd20.py`: reading the TSD and tracker files from the zip in place, the tuning measures, the
  decoder and internally referenced tuning ported from the paper's code, Idir, and the statistics.
  Other notebooks on this data set can import it.
