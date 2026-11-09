# Espinosa et al. (2017) from CRCNS bf-2

Tests the findings of [Espinosa et al. (2017)](https://doi.org/10.1093/cercor/bhx302) that can be
tested on [CRCNS bf-2](https://doi.org/10.6080/K0MG7MQW), which holds the ventral pallidum (basal
forebrain) optrode recordings of 330 units in 4 anesthetized mice, with 5-s light pulses and, in two
of the animals, tail pinch. The data set also holds medial septum recordings for a later paper and
open-field videos. It holds none of the paper's prefrontal recordings, in vitro or histology data.

| Claim | Outcome |
|---|---|
| Light changes a minority of basal forebrain units: 29 inhibited, 56 excited, 245 unaffected | Not reproduced |
| Excited units have higher spontaneous rates | Reproduced |
| Discharge during light differs between the three classes | Reproduced |
| Excited units respond with slower kinetics | Not reproduced |
| Responses to light and tail pinch cross-tabulated (Supplementary Figure 4) | Not reproduced |
| Histology and in vitro recordings (Supplementary Figures 1 to 3) | Blocked: data missing |
| Prefrontal units and LFP (Figures 2 to 4, Supplementary Figures 6 to 11, Table 2; 16 claims) | Blocked: data missing |
| Locomotion with the light path blocked (Figure 5C) | Blocked: data missing |
| Locomotion in NpHR+ against NpHR- mice (Figure 5D, Supplementary Figure 14) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set's own per-unit flags give 56 excited, 30 inhibited and 244 unaffected units, close to
the paper's counts, while the classification method as the claims file reads it from the paper
gives other counts under every reading. The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/espinosa-2017-01.yaml`](../../attempts/espinosa-2017-01.yaml).

The archives are tar.gz files, streamed once each from start to end; a run takes about 11 minutes.
