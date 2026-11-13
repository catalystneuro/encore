# Hazon et al. (2022) from CRCNS hc-30

Tests the findings of [Hazon et al. (2022)](https://doi.org/10.1038/s41467-022-31254-y) on
[CRCNS hc-30](https://doi.org/10.6080/K0GH9G5X), which holds the event onsets and track positions
of the paper's 110 working sessions (12 mice, 27,898 CA1 neurons). The helper `hc30.py` streams
the one data file and rebuilds the paper's event trace, trials, activity tensor, trial shuffle,
decoders and signal and noise measures, citing the paper or its code for each choice. A third
notebook repeats the IMSE fits with the paper's 80 neuron subsets for 16 sessions, and with 40
for one more, and fits N with other decoder settings on 9 sessions.

| Claim | Outcome |
|---|---|
| Sessions, mice and neuron counts | Reproduced |
| Single-cell response variability and SNR | Reproduced |
| Place-field properties (Supplementary Table 1) | Not reproduced |
| Noise correlations fall with place-field distance and vanish with shuffling | Reproduced |
| Correlations do not depend on the cells' physical distance | Blocked: no cell positions |
| Position measurement noise 0.28 cm | Reproduced |
| Signal and noise growth with ensemble size | Reproduced |
| Asymptotic SNR lower with correlations | Reproduced |
| Signal slope changes over the run (Fig. 3f) | Reproduced (larger at the end, as the code tests; the legend's decrease does not hold) |
| Noise slope falls over the run | Reproduced |
| SNR higher at the end of runs | Reproduced |
| SNR along noise components peaks at the sixth | Partially reproduced (peak at the seventh) |
| Correlations increase noise and signal overlap | Reproduced |
| Overlap predicts asymptotic SNR across animals | Reproduced |
| PF width variance against NSV across animals | Reproduced |
| NSV predicts the effect of correlations | Reproduced |
| NSV is the best predictor (Supplementary Table 2) | Reproduced |
| PF width variance does not predict the effect | Reproduced (with the filter of Supplementary Table 2) |
| Synthetic narrow width distributions have higher NSV | Reproduced (legend's widths) |
| RMS error 9.38 against 5.15 cm | Reproduced |
| Shuffled decoding better in every bin | Reproduced |
| IMSE saturates with correlations, not without | Reproduced |
| Initial slope I0 differs | Reproduced |
| Saturation at 346 to 1402 neurons | Not reproduced |
| I0 against single-cell SNR | Partially reproduced (failed fits left out) |
| Asymptotic IMSE against asymptotic SNR | Reproduced (log scale) |
| Task performance and decoding accuracy | Not reproduced |
| Twenty bins near the smallest error | Reproduced |
| Fit recovers saturation on simulated data | Reproduced (simulation) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In six sessions the event trace does not track the position at lag 0; two are offset by about 4
s and two show no alignment. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/hazon-2022-01.yaml`](../../attempts/hazon-2022-01.yaml).
