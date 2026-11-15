# Asari and Zador (2009) from CRCNS ac-1

Tests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) that can be
tested on [CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR), which holds the whole-cell current-clamp
recordings of rat A1 neurons to sequences of natural and synthetic sounds, the cell-attached
recordings of MGB units, and the recordings of Wehr reanalysed for the encoding models. The
voltage-clamp recordings of Figures 5 and 6 are not in it.

| Claim | Outcome |
|---|---|
| Cell and probe counts (305 natural sound probes in 39 cells, 93 MGB probes in 14 cells) | Partially reproduced |
| Low firing rates in A1, high evoked rates in MGB | Partially reproduced |
| Trial-to-trial reliability, 0.31 over the population | Reproduced |
| Example neuron with context effects for about 4 s, absent from 2 to 4 s | Reproduced, resting on an assumption (pairwise reliability) |
| 204 of 305 probes (66.9%) significant, a quarter of events after 1 s | Reproduced |
| Proportion significant decays as two exponentials (0.20 and 0.90 s) | Partially reproduced |
| Normalized context-dependent power decays with a constant of 1.04 s | Partially reproduced |
| Noise and spontaneous autocorrelations decay within about 100 ms | Reproduced |
| No model without context captures more than half the predictable power at 100 ms | Partially reproduced |
| STRF and LN models stay below about 20% and do not improve with longer windows | Partially reproduced |
| Context dependence of excitatory and inhibitory conductances (Figures 5 and 6) | Blocked: data missing |
| Effects of amplitude, frequency, AM, FM and higher-order properties (Figure 8, five claims) | Blocked: metadata insufficient |
| Example of frequency context (Figure 7) | Blocked: data missing |
| Fast decay of context dependence in MGB (about 80 ms) | Reproduced |
| Example MGB unit with an effect in the first 100-ms bin only | Reproduced |
| Significant effects soon after the onset of the silences | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set includes the authors' MATLAB analysis code (`asari/Tools/CxtDep.m`), which settles how
probes, contexts and the silence periods are formed; the helper ports it. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/asari-2009-02.yaml`](../../attempts/asari-2009-02.yaml).

- `reproduce_asari_2009.ipynb`: all claims except the encoding models. It takes about four
  minutes, most of it streaming the files.
- `strf_asari_2009.ipynb`: the STRF and LN models on the Wehr cells. It takes about 22 minutes.
- `ctxdep.py`: loading the files, probe construction, the significance and fractional power
  measures, spike extraction and curve fits. Other notebooks on this data set can import it.
- `strf.py`: spectrograms, lagged designs, ridge regression with cross-validation, the static
  nonlinearity and the performance measure of the paper.
