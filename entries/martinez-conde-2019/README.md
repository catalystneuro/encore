# Martinez-Conde et al. (2019) from CRCNS pvc-12

Tests the findings of [Martinez-Conde et al. (2019)](https://doi.org/10.1371/journal.pone.0210941)
that can be tested on [CRCNS pvc-12](https://doi.org/10.6080/K05D8Q1T), which holds the spike rate
maps and stimuli of V1 neurons recorded while two monkeys viewed the Square and Edge, Star and
Corners stimuli.

| Claim | Outcome |
|---|---|
| Neuron counts (58 analysed; 25, 30 and 28 per condition) | Not reproduced |
| Spikes per condition (mean 35,998) | Blocked: data missing |
| Baseline does not differ across stimuli (S4 Fig) | Not reproduced |
| Midpoint responses above baseline, more so for sharper folds (Fig 4A) | Reproduced |
| Midpoint spike rate difference by fold (Fig 4B, Table 1) | Partially reproduced |
| S40 > S90, S40 > P180, S52 > P180 (Fig 4B) | Reproduced |
| Average maps increase with sharper corners (Fig 5) | Reproduced |
| Table 1, Edge, P180 and S90 rows | Not reproduced |
| Table 1, S52 and S40 rows | Reproduced |
| Midpoint represents the whole fold (Fig 6) | Reproduced |
| RMS contrast along the Edge and its exponential fit (Fig 7A) | Not reproduced |
| P180 matches a 50% Edge, S40 a 90% Edge (Fig 7C) | Not reproduced |
| P180 below the 94% Edge, S40 above Edges under 68% (Fig 7C) | Reproduced |
| Angle and response related monotonically but not linearly (Fig 7D) | Reproduced |
| Similar to the DOG model output (Fig 7D) | Blocked: data missing |
| Responses peak at a latency near 60 ms (S3 Fig) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds 53 neurons in 77 recordings, against the paper's 58, and only 12 of its 29 Star
recordings can be placed on the stimulus. The files hold rate maps, not spike times. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/martinez-conde-2019-02.yaml`](../../attempts/martinez-conde-2019-02.yaml).
