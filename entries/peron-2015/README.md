# Peron, Freeman, Iyer, Guo & Svoboda (2015) from CRCNS ssc-1

Tests the findings of [Peron et al. (2015)](https://doi.org/10.1016/j.neuron.2015.03.027) that can be
tested on [CRCNS ssc-1](https://doi.org/10.6080/K0TB14TN). The data set holds five imaging sessions
from three of the paper's eight volume-imaging mice. Each session has dF/F per ROI, whisker angle and
curvature, touches and trial data. It has no calcium events and no layer, cell-class or column
labels, and none of the learning, L4 axon, anesthetized or L5 soma and dendrite data.

| Claim | Outcome |
|---|---|
| Mice performed 245 ± 71 trials per session during imaging | Reproduced |
| Whisker movement amplitude 55.5 ± 13.3 degrees | Not reproduced |
| ROI counts per mouse (Table S1) | Blocked: data missing |
| Claims comparing layers, cell classes or columns (18) | Blocked: metadata insufficient |
| GABAergic, stack, training, trimming and dendrite claims (7) | Blocked: data missing |
| Neuropil, L4 axon, learning and anesthetized claims (14) | Blocked: data missing |
| Event detector validation on outside data | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper does not define its whisking amplitude. Under the three readings in the claims file the
three mice give 74.7, 29.0 and 26.9 degrees, and 72.4, 29.0 and 26.6 once tracking errors in the
whisker angle and the filter's edge effects are removed. Twice the peak Hilbert amplitude, which the criterion
does not list, gives 53.7. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/peron-2015-01.yaml`](../../attempts/peron-2015-01.yaml).
