# Buccino et al. (2024) from dandiset 000294

Tests the findings of [Buccino et al. (2024)](https://doi.org/10.1162/neco_a_01672) that can be tested
on [DANDI:000294](https://dandiarchive.org/dandiset/000294/0.260528.0854), which holds simultaneous
patch-clamp and HD-MEA recordings of two cultured rat cortical neurons stimulated with the eCode
protocols, and, from the paper's code repository, the claims on its ground-truth model and
morphologies.

| Claim | Outcome |
|---|---|
| Two neurons, four to six runs of about 200 s | Reproduced |
| eCode protocols with the Methods' sweeps, durations and amplitudes | Reproduced |
| Holding at about -70 mV (uncorrected) | Reproduced |
| Extracellular spikes of at least 50 uV | Reproduced |
| More than 500 MEA electrodes at 20 kHz; patch at 20 kHz | Partially reproduced |
| Recorded between DIV 18 and 24 | Blocked: metadata insufficient |
| AIS starts from a dendrite in both cells (repository morphologies) | Reproduced |
| Ground-truth rheobase of 150 pA | Reproduced |
| AP starts in the distal AIS of the ground-truth model | Reproduced (assumed: read between the code's 0.05 ms samples) |
| Largest ground-truth signal on the electrode nearest the AIS | Reproduced |
| Table 1 feature counts | Reproduced |
| The model fits of Figures 4, 5, 7, 8 and 10 (twelve claims) | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The patch sampling is 20.41 kHz for most protocols and 125 kHz for APWaveform, where the paper says
20 kHz and about 200 kHz. The model fits need more than 1000 CPU hours for the ground-truth fits and as
many again for the experimental fits (2457 and 2182 CPU hours in the run recorded; the estimate varies
with the runner's load). The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000294-buccino-2024-01.yaml`](../../attempts/000294-buccino-2024-01.yaml).

- `reproduce_buccino_2024.ipynb`: the analysis. It takes about ten to fifteen minutes (12.2 minutes in the run
  recorded; it prints its time): streaming the MEA data around the spikes, and the ground-truth
  simulations.
- `multimodal.py`: loading the files, the stimulus segments, spike detection and the paper's
  patch-triggered template. Other notebooks on this dandiset can import it.
- `gtmodel.py`: fetches the paper's repository at a pinned commit and simulates its ground-truth
  model with BluePyOpt's NEURON and LFPy simulators, using the repository's own protocols,
  cut-outs, template function and evaluators.
