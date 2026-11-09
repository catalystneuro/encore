# Timme et al. (2016) from CRCNS ssc-3

Tests the findings of [Timme et al. (2016)](https://doi.org/10.1371/journal.pcbi.1004858), "High-Degree
Neurons Feed Cortical Computations", on [CRCNS ssc-3](https://doi.org/10.6080/K07D2S2F): spike times
of 7735 neurons in 25 recordings of mouse somatosensory cortex slice cultures on a 512-electrode
array.

| Claim | Outcome |
|---|---|
| 25 recordings, 7735 neurons, 2.10 Hz | Reproduced |
| TE weights roughly log-normal, over several orders of magnitude | Partially reproduced (assumes the tie rule and past bins) |
| Degree distributions heavy-tailed | Reproduced |
| Out-degree tail longer than in-degree tail | Reproduced (assumes the tie rule) |
| Synergy and receiver in-degree uncorrelated, slight negative skew | Partially reproduced (assumes sub-networks, Pearson, the tie rule) |
| Synergy correlates positively with transmitter out-degree | Reproduced (assumes the tie rule) |
| Correlations beyond a permutation null | Partially reproduced (assumes sub-networks, Pearson, the tie rule) |
| Pooled trends of synergy with degree | Not reproduced |
| Information gain does not rise with inputs | Reproduced (assumes the normalized gain) |
| PID on the examples of Table 1 | Reproduced |
| Model connectivity patterns (Fig 7B) | Reproduced |
| Model correlations match the data, degree rule closest (Fig 7C) | Partially reproduced (assumes sub-networks, Pearson, the tie rule) |
| Degree rule highest conditioned MI (Fig 7D) | Not reproduced |
| Larger model (S1 Fig) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper analysed the TE networks of its reference [44] (Timme et al. 2014), which are not
deposited; the notebook rebuilds them from the spike times with that study's bins, past states and
jitter test. A surrogate whose TE equals the real TE counts as exceeding it (the "tie rule"); the
literal "larger than" of that study calls about 11% of independent pairs significant here, and is
shown as a variant. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/timme-2016-01.yaml`](../../attempts/timme-2016-01.yaml).

- `reproduce_timme_2016.ipynb`: the analysis. It takes about 52 minutes on four cores, most of it
  the jitter tests of the TE networks under both readings of the past state and the analyses of
  the variants.
- `hdn.py`: loading the data set, the TE networks with their jitter test, sub-networks, the partial
  information decomposition, the information gain and the feedforward model. Other notebooks on this
  data set can import it.
