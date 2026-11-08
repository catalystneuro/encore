# Bruno, Frost & Humphries (2017) from CRCNS apl-1

Tests the findings of [Bruno, Frost & Humphries (2017)](https://doi.org/10.7554/elife.27342),
"A spiral attractor network drives rhythmic locomotion", on CRCNS data set
[apl-1](https://doi.org/10.6080/K0SN074B): spike times of 30 voltage-sensitive dye recordings of the
Aplysia pedal ganglion (three evoked bouts in each of 10 preparations), P10 nerve spikes for nine of
them, and neuron positions on the photodiode array.

| Claim | Outcome |
|---|---|
| Counts of preparations, recordings and neurons; 120 to 180 neurons per recording | Partially reproduced |
| Slow (at most 0.1 Hz) oscillation in the spectra | Reproduced |
| Decaying population rate | Reproduced |
| 4 to 8 dimensions for 80% of the variance | Reproduced (under the code's count rule) |
| Periodic recurrence at 10 to 15 s in many responses | Reproduced |
| A single dominant orbit | Reproduced |
| Periods robust to the recurrence threshold | Reproduced |
| Coalescence within one period of stimulation | Not reproduced |
| Same manifold across bouts (two axis choices) | Reproduced (2 claims) |
| Different initial conditions | Reproduced |
| Pairwise similarity preserved | Reproduced |
| 17 of 19 perturbations return | Partially reproduced (assumed) |
| Return to the same manifold | Reproduced |
| Stable spiral in every preparation | Partially reproduced |
| Linear-model period of about 10 s | Reproduced (assumed) |
| Contraction in all dimensions in most responses | Not reproduced |
| Rotation dominates | Reproduced |
| Period slows, speeds up or is unchanged | Reproduced |
| No relation between period change and contraction | Reproduced |
| No P10 motorneurons recorded | Reproduced |
| P10 decoded in all nine responses | Partially reproduced |
| 3 to 5 dimensions for the P10 recordings; 90% no better | Reproduced (under the code's count rule) |
| Long-tailed, variable participation (three claims) | Reproduced |
| Rate explains 50% of participation, 23% of its change | Reproduced |
| Distance between bouts unrelated to participation change | Partially reproduced (assumed) |
| No invariant core of oscillator neurons | Reproduced (port of the code's ensemble toolbox) |
| Strong participation in the caudo-lateral quadrant | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several outcomes depend on two details the paper leaves open: the width of the Gaussian kernel
(the Methods' printed formula gives 21 to 76 dimensions; the code uses the median ISI) and whether
the number of PCs is the smallest reaching 80% (Methods) or the largest at most 80% (code). The
notebook runs every reading, and its summary tabulates the outcome under each for the claims that
change; no single reading makes all of them hold. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/crcns-apl-1-bruno-2017-01.yaml`](../../attempts/crcns-apl-1-bruno-2017-01.yaml).

- `reproduce_bruno_2017.ipynb`: the analysis, about 36 minutes on 4 CPUs (the recurrence analysis
  under eight readings, the manifold comparisons with 100 shuffles, the P10 decoding under four
  readings, and the ensemble typing).
- `apl.py`: streaming the files from the CRCNS bucket, spike-density functions, PCA, the
  recurrence analysis, local linear models, Hausdorff comparisons, a port of Chronux
  `mtspectrumpt`, P10 decoding, participation, and a port of the code's consensus clustering and
  ensemble typing. Other notebooks on this data set can import it.
