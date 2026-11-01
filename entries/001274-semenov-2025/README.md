# Semenov, Kim, Silkuniene & Pakhomov (2025) from dandiset 001274 and the paper's other dandisets

Tests the findings of [Semenov et al. (2025)](https://doi.org/10.1016/j.xcrp.2025.102660) that can be
tested on [DANDI:001274](https://dandiarchive.org/dandiset/001274/0.250805.1401), which holds the strobe
images of membrane polarization by 2-us pulses and 2-kHz sine waves (Figures 5, 6 and S3), and on the
other dandisets the paper deposited: the fast optical recordings of action potentials in 001032, 001033
and 001035 (Figures 1 and 2), 001030 (Figure 3C), 001271 (Figure S2) and 001272 (Figure S1). 001034 is a
second deposit of 001032.

| Claim | Outcome |
|---|---|
| Unmodulated 2- and 20-kHz sine waves excite every neuron | Not reproduced |
| Near-threshold APs come 100 to 200 ms after onset; stronger fields shorten the delay | Not reproduced |
| The maximum firing rate reaches a ceiling of 60 to 90 Hz | Not reproduced (resting on an assumption) |
| The highest fields give an excitation block | Not reproduced |
| 20-kHz thresholds are about twice the 2-kHz ones | Not reproduced |
| Modulated sine waves have higher thresholds | Partially reproduced |
| The 2-kHz threshold is 57.7 V/cm | Not reproduced |
| Firing locks to the 20-Hz beats, with no sustained depolarization | Not reproduced |
| Pure sine waves give more APs than modulated ones at the same field | Reproduced |
| Low conductivity halves thresholds (Figure 3B) | Blocked: metadata insufficient |
| 2-s ramped sine waves give sustained firing, then a block (Figure 3C) | Not reproduced |
| Di-8-ANEPPS gives the same responses (Figure S1) | Not reproduced |
| Tetrodotoxin abolishes APs and the sustained depolarization (Figure S2) | Not reproduced |
| Membrane charging kinetics (Figure 4, four claims) | Blocked: metadata insufficient |
| Polarization by sine waves and pulses (Figures 5, 6, S3, nine claims) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

The strobe dandisets (001274, 001273) hold raw image stacks only, with no ROIs, field values or cell
identifiers, so their claims are blocked; ROIs rebuilt from the paper's RATIO image are shown as a
variant. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001274-semenov-2025-01.yaml`](../../attempts/001274-semenov-2025-01.yaml).
