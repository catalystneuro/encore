# Asari and Zador (2009) from CRCNS ac-1

Tests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) that can be
tested on [CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR), which holds the whole-cell current-clamp
recordings of rat A1 neurons to sequences of natural and synthetic sounds, the cell-attached
recordings of MGB units, and the recordings of Wehr reanalysed for the encoding models. The
voltage-clamp recordings of Figures 5 and 6 are not in it.

| Claim | Outcome |
|---|---|
| Cell and probe counts (305 natural sound probes in 39 cells, 93 MGB probes in 14 cells) | Partially reproduced |
| Low firing rates in A1, high evoked rates in MGB | Partially reproduced, resting on an assumption (A1 spike detector) |
| Trial-to-trial reliability, 0.31 over the population | Reproduced, resting on an assumption (pairwise reliability) |
| Example neuron with context effects before 2 s, none from 2 to 3.6 s, and again after 3.6 s | Reproduced, resting on an assumption (pairwise reliability) |
| 204 of 305 probes (66.9%) significant, a quarter of events after 1 s | Reproduced |
| Proportion significant decays as two exponentials (0.20 and 0.90 s) | Partially reproduced |
| Normalized context-dependent power decays with a constant of 1.04 s | Not reproduced |
| Noise and spontaneous autocorrelations decay within about 100 ms | Reproduced |
| No model without context captures more than half the predictable power at 100 ms | Not reproduced |
| STRF and LN models stay below about 20% and do not improve with longer windows | Partially reproduced, resting on an assumption (the claims file's test, 16 of 20 cells) |
| Context dependence of excitatory and inhibitory conductances (Figures 5 and 6) | Blocked: data missing |
| Proportions of significant probes by stimulus property (Figure 8A) | Partially reproduced, resting on an assumption (property sets); the order holds by 0.002 and fails with every set as a test |
| Fits of the proportions by property (Figure 8A legend) | Not reproduced, resting on an assumption (property sets) |
| Decay of the normalized power by property (Figure 8B) | Not reproduced, resting on an assumption (property sets); partial with the naturalistic probes added |
| Effects of each property relative to natural sounds (Figure 8C) | Not reproduced, resting on an assumption (property sets); partial with every set or the naturalistic probes |
| No difference between natural and synthetic probes | Reproduced, resting on assumptions (property sets, the claims file's test) |
| Example of frequency context (Figure 7) | Blocked: data missing |
| Fast decay of context dependence in MGB (about 80 ms) | Reproduced, resting on an assumption (plateau against the fitted constant) |
| Example MGB unit with an effect in the first 100-ms bin only | Reproduced |
| Significant effects soon after the onset of the silences | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set includes the authors' MATLAB analysis code (`asari/Tools/CxtDep.m`), which settles how
probes, contexts and the silence periods are formed; the helper ports it. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/asari-2009-02.yaml`](../../attempts/asari-2009-02.yaml).

- `reproduce_asari_2009.ipynb`: all claims except the encoding models. It takes about five
  minutes, most of it streaming the files.
- `strf_asari_2009.ipynb`: the STRF and LN models on the Wehr cells. It took 24 minutes in the latest run and 31 in the one before.
- `ctxdep.py`: loading the files, probe construction, the significance and fractional power
  measures, the property sets of the synthetic stimuli, spike extraction and curve fits. Other notebooks on this data set can import it.
- `strf.py`: spectrograms, lagged designs, ridge regression with cross-validation, the static
  nonlinearity and the performance measure of the paper.
