# Asari & Zador (2009) from CRCNS ac-1

Tests the findings of [Asari and Zador (2009)](https://doi.org/10.1152/jn.00577.2009) that can be
tested on [CRCNS ac-1](https://doi.org/10.6080/K0KW5CXR). The data set holds the whole-cell
recordings of 39 A1 cells probed with natural sound sequences and 96 probed with synthetic
ensembles, and the cell-attached recordings of 14 MGB cells, with the authors' MATLAB analysis code,
and Michael Wehr's whole-cell recordings of Machens et al. (2004), used here for the STRF models.
The voltage-clamp recordings of Figures 5 and 6 are not in it.

| Claim | Outcome |
|---|---|
| Counts of cells and probes analysed | Partially reproduced |
| Firing rates in A1 and MGB | Partially reproduced |
| Trial-to-trial reliability, population and example cell (Figure 2) | Reproduced |
| Example cell with intermittent, long context dependence (Figure 2) | Reproduced |
| 204 of 305 probes context dependent, a quarter of events after 1 s (Figure 3A) | Reproduced |
| Two-exponential decay of the significance measure (Figure 3A) | Partially reproduced |
| Normalized context-dependent power decays with a 1.04 s constant (Figure 3B) | Not reproduced |
| Noise and spontaneous autocorrelations decay within about 100 ms | Reproduced |
| Upper bound on model performance, 0.51 at onset, 1.04 s constant (Figure 4) | Not reproduced |
| STRF models predict under 20% and do not improve with longer windows (Figure 4) | Not reproduced |
| Synaptic conductances (Figures 5 and 6) | Blocked: data missing |
| Example cell with three DMR frequency bands as contexts (Figure 7) | Blocked: data missing |
| Proportion of significant probes by sound property (Figure 8A) | Partially reproduced |
| Decay of the normalized power by sound property (Figure 8B) | Partially reproduced |
| Exponential fits of the significance measure by property (Figure 8A) | Not reproduced |
| Effects of each property relative to natural sounds (Figure 8C) | Not reproduced |
| Natural and synthetic probes alike | Reproduced |
| Fast decay of context dependence in MGB (Figure 9) | Reproduced |
| Example MGB unit, effect only in the first bin (Figure 9) | Reproduced |
| Context dependence after the intersequence silences (Supplemental Figure S1) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/asari-2009-02.yaml`](../../attempts/asari-2009-02.yaml).

- `reproduce_asari_2009.ipynb`: the analysis. It takes about 40 minutes, most of it the
  Kruskal-Wallis tests with 1,000 shuffles per probe and the STRF fits, run in four worker
  processes.
- `asari.py`: streaming the files from the crcnsarchive bucket, the probe sets of the authors'
  `CxtDep.m`, the significance and fractional power measures, spike extraction and the
  exponential fits, and the map from the synthetic stimuli to the sound property varied. Other
  notebooks on this data set can import it.
- `wehr.py`: Wehr's recordings and stimuli, the spectrograms, and the STRF and LN models with
  cross-validated ridge regression over the nine window lengths of the paper.
