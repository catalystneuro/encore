# Martinez-Conde et al. (2019) from CRCNS pvc-12

Tests the findings of [Martinez-Conde et al. (2019)](https://doi.org/10.1371/journal.pone.0210941)
that can be tested on [CRCNS pvc-12](https://doi.org/10.6080/K05D8Q1T). The data set holds the spike
rate maps and stimuli of 53 V1 neurons from two monkeys, for the Square and Edge, Star and Corners
stimuli. It holds no spike times or eye positions, and only 12 of the 27 Star neurons carry the
aligned frame that registers the map to the stimulus.

| Claim | Outcome |
|---|---|
| Neuron counts (58 analysed; 25, 30 and 28 per condition) | Not reproduced |
| At least 10,000 spikes per condition, mean 35,998 | Blocked: data missing |
| Baseline does not differ across stimuli | Reproduced (assumed baseline placement; the readings disagree) |
| Midpoint responses above baseline, more so for sharper folds (Fig 4A) | Reproduced |
| Spike rate difference at the midpoint by fold angle (Fig 4B) | Partially reproduced |
| S40 > S90, S40 > P180, S52 > P180 (Fig 4B tests) | Reproduced |
| Average maps increase with sharper corners (Fig 5) | Reproduced |
| Table 1, Edge | Partially reproduced (assumed baseline placement) |
| Table 1, P180 | Partially reproduced |
| Table 1, S90 | Partially reproduced (assumed baseline placement) |
| Table 1, S52 | Reproduced |
| Table 1, S40 | Reproduced |
| Midpoint represents the whole fold (Fig 6) | Reproduced |
| Edge RMS contrast and its exponential fit (Fig 7A) | Blocked: methods underspecified |
| P180 matches a 50% Edge, S40 a 90% Edge (Fig 7C) | Not reproduced |
| P180 and S40 differ from the Edge at the extreme contrasts (Fig 7C tests) | Reproduced |
| Response against angle is not linear (Fig 7D) | Reproduced |
| Similar to the DOG model output (Fig 7D) | Blocked: data missing |
| Responses peak at a 60 ms latency (S3 Fig) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/martinez-conde-2019-02.yaml`](../../attempts/martinez-conde-2019-02.yaml).

- `reproduce_martinez_conde_2019.ipynb`: the analysis. It takes about three minutes, most of it reading
  the zip file in place and rasterising the stimuli.
- `vasarely.py`: reading the zip over range requests, the aligned maps and polygons, the fold
  geometry, and the midpoint, block, baseline and Edge measures. Other notebooks on this data set can
  import it.
