# Peron et al. (2020) from CRCNS ssc-11

Tests the findings of [Peron et al. (2020)](https://doi.org/10.1038/s41586-020-2062-x),
"Recurrent interactions in local cortical circuits", that can be tested on
[CRCNS ssc-11](https://doi.org/10.6080/K0Z31WWG): volumetric calcium imaging of L2/3 of mouse
barrel cortex in 16 mice before and after 24 targeted ablations of touch, whisking or silent
neurons. The notebook streams the 16 archives (128 GB) from the public CRCNS bucket once, in
about 17 minutes, and reduces them in memory.

| Claim | Outcome |
|---|---|
| Network model claims (seven) | Blocked: not run in this attempt |
| Neurons per mouse, representation sizes | Reproduced |
| Sizes of the touch, whisking and silent ablations | Reproduced |
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
| Extended Data Table 1 | Reproduced (resting on an assumption) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.
