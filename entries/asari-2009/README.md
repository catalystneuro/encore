# Asari & Zador (2009) from CRCNS ac-1

Tests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) on
[CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR), which holds their whole-cell recordings in rat A1
and cell-attached recordings in MGB with natural and synthetic sound sequences, the paper's
analysis code, and Wehr's recordings of Machens et al. (2004). The voltage-clamp recordings of
Figures 5 and 6 are not in the data set.

| Claim | Outcome |
|---|---|
| Recording counts (305 probes in 39 A1 cells, 93 in 14 MGB cells, 123 A1 cells in all) | Partially reproduced |
| Low firing rates in A1, high in MGB | Partially reproduced |
| Trial-to-trial reliability (0.31 over the population, 0.61 in the example cell) | Reproduced |
| Example context effect lasting about 4 s, with a gap from 2 to 4 s | Reproduced (a selected candidate) |
| 204 of 305 probes context dependent, a quarter of the events after 1 s | Reproduced |
| Two-exponential decay of the proportion of significant probes | Partially reproduced |
| Normalized context-dependent power decays with a 1.04 s constant | Not reproduced |
| Noise and spontaneous autocorrelations decay within about 100 ms | Reproduced |
| Upper bound on prediction without context is about half near onset | Not reproduced |
| STRF models capture under 20% at any window length | Not reproduced (assumed cell selection and test) |
| Figures 5 and 6: synaptic conductances | Blocked: data missing |
| Figure 7 example (DMR frequency contexts) | Blocked: data missing |
| Context effects by sound property, counts (Figure 8A) | Partially reproduced (assumed property sets) |
| Exponential fits of the significance by property (Figure 8A) | Not reproduced (assumed property sets) |
| Decay of the normalized power by property (Figure 8B) | Partially reproduced (assumed property sets) |
| Relative effects by property (Figure 8C) | Not reproduced (assumed property sets) |
| Natural and synthetic probes alike | Reproduced (assumed test and property sets) |
| Fast decay of context dependence in MGB (about 80 ms) | Reproduced |
| MGB example, effect in the first 100-ms bin only | Reproduced |
| Context dependence soon after silence onset, power fading within 1 s | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set includes the paper's own analysis script, `CxtDep.m`; where the Methods leave a step
open the analysis follows it. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/asari-2009-01.yaml`](../../attempts/asari-2009-01.yaml).

- `reproduce_asari_2009.ipynb`: the analysis. It streams all 346 of Asari's recordings once
  (2.8 GB) and takes about 25 minutes.
- `strf_wehr.ipynb`: the STRF and LN models of Figure 4, fitted to Wehr's recordings of Machens et
  al. (2004) in the same data set; it takes about 22 minutes.
- `wehr_strf.py`: reading Wehr's trial files and stimuli, spectrograms, the lagged designs and
  the ridge, lowess and performance computations.
- `asari.py`: reading the zip files in place, forming the probe responses as `CxtDep.m` does, the
  significance and fractional power measures, spike detection, PSTHs, the property sets of the
  synthetic sounds and the exponential fits. Other notebooks on this data set can import it.
