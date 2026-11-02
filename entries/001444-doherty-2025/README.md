# Doherty, Chen, Smith, Wichmann, Chu & Lytton (2025) from dandiset 001444

Tests the findings of [Doherty et al. (2025)](https://doi.org/10.1038/s41531-025-01070-4) on
[DANDI:001444](https://dandiarchive.org/dandiset/001444/0.250805.2002), which holds four sets of
four NetPyNE simulations of a 10,073-cell model of mouse M1 (control and parkinsonian, rest and
activated). The paper reports set sM1_12-12-2023, and the claims are tested on it.

| Claims | Outcome |
|---|---|
| Dominant frequencies at control rest (19 Hz), control activated (44 Hz) and parkinsonian rest (15 Hz) | Reproduced |
| PT5B rates and their changes, except the control against parkinsonian activated comparison | Reproduced |
| PT5B ISI CV in both conditions | Reproduced |
| More negative PT5B potential in the parkinsonian activated state; more 20 to 35 Hz power | Reproduced |
| PT5B activated rate, parkinsonian against control (one test of four above p = 0.001) | Partially reproduced |
| Order-of-magnitude increase of 15 Hz power at rest (the ratio is 65 to 129) | Partially reproduced |
| IT4, IT5A, IT5B and IT6 rates (seven claims), under rate reading R3 (cells that fired at least once) | Reproduced, resting on R3 as an assumption (and, for parkinsonian IT6, on which cells the paired tests pair) |
| IT2 rate increase with activation, control and parkinsonian (values match under R3, paired or rank tests above p = 0.001 under every pairing) | Not reproduced |
| IT4 rest rate, parkinsonian against control (values match under R3, no test below p = 0.05) | Not reproduced |
| Parkinsonian activated dominant frequency (27 Hz against 43) | Not reproduced |
| Duty cycles, LFP burst rates, coincident spikes, unitary-event durations (ten claims) | Not reproduced |
| Network size (the files store only cells that fired) | Not reproduced |
| More synchrony at rest in the parkinsonian condition | Reproduced, resting on counting pairs of coincident cells as an assumption |
| Highest PT5B rate (PV5A fires faster) | Blocked: methods underspecified |
| Robustness over four sets; subthreshold oscillations (three claims) | Blocked: methods underspecified |
| PT5B current-injection excitability | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The units tables hold only cells that fired; the paper's IT rates match exactly when the mean is
taken over those cells (reading R3, which a reader added to the claims file in answer to a
question; the paper does not say which cells it averaged over). The paper's set holds 20 PT5B
potentials per file (not 400), and in the analysis window they do not match the stored spikes of
the same cells. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/001444-doherty-2025-01.yaml`](../../attempts/001444-doherty-2025-01.yaml).

- `reproduce_doherty_2025.ipynb`: the analysis. It takes about six minutes, most of it streaming
  the files.
- `m1sim.py`: loading the files, population sizes from the gid blocks, rates, spectra (with
  NetPyNE 1.0.5's Morlet spectrogram), duty cycles, coincidences and unitary events. Other
  notebooks on this dandiset can import it.
