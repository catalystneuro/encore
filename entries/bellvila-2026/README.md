# Bell Vila et al. (2026) from dandiset 001678

Tests the findings of [Bell Vila et al. (2026)](https://doi.org/10.1162/imag.a.1066), on
alternating current stimulation of rat sensorimotor cortex, against
[DANDI:001678](https://dandiarchive.org/dandiset/001678/0.260227.1824) (version 0.260227.1824).

The 1-minute files hold only the stimulation command, one series per trial, and no recording, so
the paper's parameter exploration cannot be tested. The 20-minute files hold a 16-channel stream
at 12207 Hz that carries the LFP and spikes, but no sorted units; loading and sorting the 13 rats
takes longer than the 60-minute notebook limit at the speed measured on one full rat (68 to 85 minutes in
the runs so far, depending on the machine). The sham recording is not in the
dandiset.

| Claim | Outcome |
|---|---|
| Median electric field of the 20-minute experiments, 1.65 mV/mm | Reproduced (resting on an assumed channel layout) |
| Electric fields of the 1-minute experiments, and the three finite element model claims (the model is not public) | Blocked: data missing |
| Neurons, firing rates and entrainment in the 1-minute experiments, and their LFP (26 claims) | Blocked: data missing |
| Neurons, firing rates and entrainment in the 20-minute experiments (4 claims) | Blocked: too large |
| LFP power and phase-amplitude coupling near affected neurons after 20-minute stimulation (8 claims) | Blocked: too large |
| Sham stimulation (2 claims) | Blocked: data missing |

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/bellvila-2026-01.yaml`](../../attempts/bellvila-2026-01.yaml).
