# Talbot, Sparks, Dvorak, Curran, Alarcon & Fenton (2018) from CRCNS hc-16

Tests the findings of [Talbot et al. (2018)](https://doi.org/10.1016/j.neuron.2017.12.043) that can
be tested on [CRCNS hc-16](https://doi.org/10.6080/K01V5C44), which holds CA1 spike trains with
tracked positions from 8 wild-type and 7 Fmr1-null mice in a large box and a stationary and rotating
circular arena. The slice recordings, LFP, sleep recordings and avoidance sessions of the paper are
not in it.

| Claim | Outcome |
|---|---|
| Mouse, cluster and cell counts | Blocked: data missing (15 of 21 mice) |
| Interneuron proportion | Partially reproduced |
| Place cell proportion | Not reproduced |
| Non-spatial discharge alike between genotypes (Figure S3) | Partially reproduced |
| Spatial firing quality alike between genotypes (Figure 2) | Not reproduced |
| Place cell properties alike (Table S1) | Partially reproduced |
| Non-spatial cells discharge in more of the environment (Table S1) | Not reproduced |
| Overdispersion lower in Fmr1-null, by pass and by cell | Not reproduced |
| Weaker pass-by-pass covariance of Fmr1-null pairs (30 and 40 passes) | Partially reproduced |
| Weaker Kendall correlations, place and non-spatial cells, and during quiet periods | Not reproduced |
| Network states recur less in Fmr1-null | Not reproduced |
| Locomotion alike | Reproduced, resting on an assumption |
| Room-frame Ipos greater in Fmr1-null (Figure 5B) | Partially reproduced |
| Weaker ensemble coordination of Ipos (Figure 5C) | Not reproduced |
| Room frame preferred during rotation (Figure S6) | Partially reproduced, resting on an assumption |
| Slice physiology, LFP, remapping and avoidance claims (13) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set has no isolation measures or waveforms, so every sorted cluster is used in place of the
paper's well-isolated cells; this bears on every tested claim. The overdispersion claims read the
paper's pass rule literally, as the claims file does; a reading of it as a count changes the
overdispersion result and is asked of a reader in
[`questions/crcns-hc-16.yaml`](../../questions/crcns-hc-16.yaml). The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/crcns-hc-16-talbot-2018-01.yaml`](../../attempts/crcns-hc-16-talbot-2018-01.yaml).
