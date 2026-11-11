# Shi, Apker & Buneo (2013) from CRCNS ppc-1

Tests the findings of [Shi et al. (2013)](https://doi.org/10.1152/jn.00223.2012) on
[CRCNS ppc-1](https://doi.org/10.6080/K0CZ353K), which holds the sorted spikes and trial events of
area 5 recordings while monkeys held the arm at eight targets with or without vision of the arm
cursor. The notebook streams the data set's single `data.tar.gz` from the public CRCNS bucket.

| Claim | Outcome |
|---|---|
| Neurons with a position, vision or interaction effect in the hold (39%, 13%, 9%) | Reproduced (vision count rests on an assumption) |
| V and NV responses correlate alike whether endpoints differed or not | Reproduced (assumption) |
| CV2 larger in NV; decoding better in V; cross-condition decoding lower | Reproduced (two rest on an assumption) |
| Table 1 endpoint means; overall effect percentages; INDX1 mostly negative and its group means; rate variance higher in NV | Partially reproduced |
| Behavioural MANOVA and Levene percentages; Table 1 SDs; example neuron; movement epoch tuning; 400 ms subepochs; tuning shift; INDX2; Fano factor; decoding accuracies and subepochs; cells without effects | Not reproduced |
| Eye position; aborted trials; longer hold | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds monkey X's sessions only (every session has monkey X's target layout), and
which of the two condition codes is Vision is not documented: it is inferred from the aborted
trials. The data set has 359 usable monkey X sessions against the paper's 219; one unit is taken
from each, as the paper has one neuron per session, and which unit is an assumption (the first
sorted). The event codes and the per-trial text record are undocumented and were read from the
data. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/shi-2013-01.yaml`](../../attempts/shi-2013-01.yaml).
