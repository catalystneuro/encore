# Bennett, Ouellette, Ramirez et al. (2024) from dandiset 001051

Tests the findings of [Bennett et al. (2024)](https://doi.org/10.1016/j.neuron.2024.06.015), the
SHIELD implant paper, on [DANDI:001051](https://dandiarchive.org/dandiset/001051/0.260922.1827),
which holds 99 change-detection sessions of 27 mice recorded with up to six Neuropixels probes. The
surgery, imaging, histology, MRI and optogenetics material of Figures 3, 5 and 6 is not in it.

| Claims | Outcome |
|---|---|
| The paper's session list and unit table match the files (added link) | Partially reproduced (6 of 87 sessions hold other units) |
| Scale, units and areas per session, penetration, unit drift, QC fraction, yield and firing rate across days, VBN yield drop, RF fraction, visual responses across days (10 claims) | Reproduced |
| Insertions per mouse (holes not testable), behaviour across days | Partially reproduced |
| QC metrics comparable to the 5-mm window, recovery time constant after insertion | Not reproduced |
| Alpha events: MOp higher frequency, VISp offset locking | Reproduced |
| Alpha events: low arousal (direction holds, size differs) | Partially reproduced |
| Alpha events: replay correlation, lags straddling zero, no hippocampal engagement | Not reproduced |
| Alpha events: VISp coupling, VISp and MOp networks, CP-RF coherence | Blocked: methods underspecified (the readings of the random-time coherence and area labels disagree) |
| Alpha events: MOp coupling | Blocked: methods underspecified (MOp-PO coupling holds under one event rule and cannot be tested under the other) |
| Striatum: CP-RF location (dorsal yes, medial no); larger response (holds, but the unit counts match only with the code's filter) | Partially reproduced |
| Striatum: modulation at troughs | Reproduced |
| Striatum: response latencies | Blocked: methods underspecified (half-peak and peak latencies give different outcomes; the paper picks neither) |
| Figure 3, 4B trajectories, 4C, 4F, S3D, S4D to S4H, Figures 5 and 6 (16 claims) | Blocked: data missing, metadata insufficient or methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The session list, the paper's unit tables and the VBN comparison tables come from the paper's
repository at a pinned commit. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/001051-bennett-2024-01.yaml`](../../attempts/001051-bennett-2024-01.yaml).

- `reproduce_bennett_2024.ipynb`: the analysis. It takes about 20 minutes, most of it streaming the
  spike times of the 99 sessions.
- `shield.py`: loading the files, the receptive-field test, the alpha-event detector and the per-session
  spike pass. Other notebooks on this dandiset can import it.
