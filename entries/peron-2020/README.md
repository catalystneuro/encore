# Peron et al. (2020) from CRCNS ssc-11

Tests the findings of [Peron et al. (2020)](https://doi.org/10.1038/s41586-020-2062-x),
"Recurrent interactions in local cortical circuits", that can be tested on
[CRCNS ssc-11](https://doi.org/10.6080/K0Z31WWG): volumetric calcium imaging of L2/3 of mouse
barrel cortex in 16 mice before and after 24 targeted ablations of touch, whisking or silent
neurons. The notebook streams the 16 archives (120.9 GB compressed) from the public CRCNS bucket once,
in 11 to 18 minutes depending on the connection, and reduces them in memory. It then rebuilds the network model of the Methods
(2,000 leaky integrate-and-fire neurons, helper `peron2020_model.py`) and simulates 30 networks
per condition, in about 21 minutes.

| Claim | Outcome |
|---|---|
| Model: amplification grows with subnetwork connectivity | Reproduced (resting on assumptions) |
| Model: ablation raises scores at equal connectivity | Not reproduced (resting on assumptions); partially reproduced proposed for a third verification round |
| Model: ablation lowers scores at increased connectivity | Partially reproduced (resting on assumptions) |
| Model: all-or-none networks robust to ablation | Blocked: the Methods' input rule gives no positive strength here |
| Model: larger ablations, larger declines | Partially reproduced (resting on assumptions); reproduced proposed for a third verification round |
| Model: slow input also sensitive at increased connectivity | Partially reproduced (resting on assumptions) |
| Model: decline follows response similarity | Not reproduced (resting on assumptions) |
| Neurons per mouse, representation sizes | Reproduced |
| Sizes of the touch and whisking ablations | Partially reproduced |
| Size of the silent ablations | Reproduced |
| Touch ablation lowers Rtouch (0.123 to 0.100) and the touch neuron count | Reproduced |
| Touch ablation leaves Rwhisking unchanged | Reproduced |
| Whisking and silent ablations change neither representation | Reproduced |
| Ablation types differ in their effect on Rtouch only | Reproduced |
| Decline grows with the touch score ablated | Reproduced |
| Distance dependence for touch neurons, none for whisking neurons | Reproduced |
| Behaviour unchanged after ablation | Not reproduced |
| Response similarity: touch ablation | Not reproduced |
| Response similarity: example mouse slope | Not reproduced |
| Response similarity: whisking ablation | Reproduced |
| No change in event rate next to ablated silent neurons | Reproduced |
| About two thirds of ablations succeed | Reproduced |
| Glial reaction confined to the lesion | Blocked: data missing |
| Extended Data Table 1 | Partially reproduced (23 of 24 rows; 24 with the code's cylinder) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.
