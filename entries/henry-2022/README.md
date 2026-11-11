# Henry & Kohn (2022) from CRCNS v4-2

Tests the findings of [Henry and Kohn (2022)](https://doi.org/10.1016/j.cub.2022.10.049) on
[CRCNS v4-2](https://doi.org/10.6080/K0736P4H), which holds the spike counts of the V1 and V4
populations recorded in two macaques viewing target gratings alone and amid distractors. The
receptive-field maps, the per-session coarse mapping and the waveforms are not in it.

| Claim | Outcome |
|---|---|
| 11 sessions, 22 populations, 396 V1 and 691 V4 units | Partially reproduced |
| V4 receptive fields many-fold larger (Figure 1B) | Blocked: data missing |
| Single-neuron discriminability slopes, V1 and V4, near and far (Figure 2A to 2C, four claims) | Reproduced |
| Population decoding example (Figure 2D, 2E) | Reproduced |
| V1 threshold elevation (Figure 2F) | Not reproduced |
| V4 threshold elevation (Figure 2F) | Partially reproduced |
| Pseudo-populations (Figure S3) | Reproduced |
| Noise correlations reduced (Figure 3A, 3B) | Reproduced |
| Shuffled decoding (Figure 3C) | Reproduced |
| Fano factors (Figure 3D, 3E, two claims) | Reproduced |
| V1 modulation indices (Figure 4A) | Partially reproduced |
| V4 modulation indices (Figure 4B) | Reproduced |
| Modulation strength (Figure 4C, three claims) | Reproduced |
| Receptive-field alignment (Figure S4) | Blocked: data missing |
| Additive against multiplicative (Figure S5) | Reproduced |
| Tuning model terms (Figure 5B, 5C) | Partially reproduced |
| Fit quality | Not reproduced |
| Terms covary (Figure 5) | Reproduced |
| Negative multiplicative terms (Figure 5) | Partially reproduced |
| Simulated discriminability (Figure 5D, 5E) | Reproduced |
| Tuning correlations, near and spacing (Figure 6C, 6D) | Partially reproduced |
| Tuning correlations, configuration (Figure 6E) | Reproduced |
| Well-isolated units (Figure 6) | Blocked: data missing |
| Fixed decoders (Figure 7C, 7D) | Partially reproduced |
| Common neuron pool (Figure S6) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In six of the eleven sessions the epochs labelled blank respond as the target epochs do, and the
V4 epochs are not stored in the V1 (recording) order. The attempt record, with the reasons and
the differences from the paper's method, is
[`attempts/henry-2022-01.yaml`](../../attempts/henry-2022-01.yaml).
