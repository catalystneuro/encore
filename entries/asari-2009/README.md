# Asari & Zador (2009) from CRCNS ac-1

Tests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) that can be
tested on [CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR): Hiroki Asari's whole-cell recordings
from rat primary auditory cortex with natural and synthetic sound ensembles, and his cell-attached
recordings from the auditory thalamus. The data set holds no voltage-clamp recordings (Figures 5
and 6). The STRF models on Michael Wehr's recordings (Figure 4) were not run in this attempt.

| Claim | Outcome |
|---|---|
| Counts of cells and probes (Table 1) | Partially reproduced |
| Low firing rates in A1, high in MGB | Partially reproduced |
| Trial-to-trial reliability, example and population | Reproduced |
| Example neuron, context effect for about 4 s with a gap | Reproduced |
| 204 of 305 probes significant, a quarter of events after 1 s | Reproduced |
| Proportion significant decays as two exponentials | Partially reproduced |
| Normalized context-dependent power decays with tau about 1 s | Partially reproduced |
| Noise and spontaneous autocorrelations decay within about 100 ms | Reproduced |
| Upper bound on prediction without context (0.51, tau 1.04 s) | Partially reproduced |
| STRF models predict under 20% at any window | Blocked: not run in the time of this attempt |
| Example conductances (Figure 5) | Blocked: data missing |
| Conductance decay constants (Figure 6) | Blocked: data missing |
| Proportion significant by sound property | Partially reproduced |
| Power decay constants by property | Partially reproduced |
| Significance fits by property | Not reproduced |
| Relative effects by property | Partially reproduced |
| Natural and synthetic probes alike | Reproduced (on an assumed test) |
| Fast decay in MGB | Partially reproduced |
| Example MGB unit, effect in the first bin only | Reproduced |
| Example DMR frequency context (Figure 7) | Blocked: no recording matches |
| Context dependence in the intersequence silences | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/asari-2009-03.yaml`](../../attempts/asari-2009-03.yaml).

- `reproduce_asari_2009.ipynb`: the analysis. It reads about 3 GB from the CRCNS bucket in four
  processes and runs 1000 shuffles per probe under five seeds; it takes about 35 minutes.
- `asari.py`: reading the zips in place, cutting recordings into context-probe pairs as the
  authors' `CxtDep.m` does, the significance and fractional power measures, the exponential fits,
  the spike detectors, and the property sets of the synthetic ensembles. Other notebooks on this
  data set can import it.
