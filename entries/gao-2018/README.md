# Gao et al. (2018) from dandiset 000007

Tests the findings of [Gao et al. (2018)](https://doi.org/10.1038/s41586-018-0633-x), "A
cortico-cerebellar loop for motor planning", that can be tested on
[DANDI:000007](https://dandiarchive.org/dandiset/000007/0.220126.1903), which holds the ALM
recordings of 13 mice during cerebellar nucleus photo-activation or photo-inhibition. The lesion,
CN recording, licking, VGAT-ChR2 and anatomy data are not in it.

| Claim | Outcome |
|---|---|
| Fastigial photo-activation in the early sample epoch leaves choice unaffected | Reproduced |
| Fastigial photo-activation in the early delay epoch causes errors | Reproduced |
| Delay photo-activation biases choice either way, depending on the mouse | Reproduced |
| Dentate photo-activation has little effect on choice | Reproduced |
| Delay photo-inhibition biases choice either way, depending on the mouse | Partially reproduced |
| Most ALM pyramidal neurons are selective for trial type | Reproduced |
| ALM selectivity emerges gradually and peaks in the response epoch | Blocked: methods underspecified |
| CN photo-inhibition rapidly alters many ALM neurons | Partially reproduced |
| The mean ALM rate is nearly unchanged by CN photo-inhibition | Partially reproduced |
| Modulated ALM neurons increase or decrease | Reproduced |
| CN photo-inhibition abolishes ALM selectivity | Reproduced (on an assumption) |
| Fastigial photo-activation changes ALM activity within a few ms | Partially reproduced |
| Fastigial photo-activation abolishes most ALM selectivity | Reproduced |
| The fastigial effect persists more than 1 s after the photostimulus | Reproduced |
| ALM recovers quickly after dentate photo-activation | Not reproduced |
| Trajectories separate along the coding direction in control trials | Reproduced |
| Fastigial, not dentate, photo-activation collapses the separation | Reproduced |
| The coding direction captures 64% of selectivity and 27% of variance | Reproduced (on an assumption) |
| After fastigial photo-activation ALM no longer predicts the movement | Not reproduced |
| Lesions, CN recordings, licking, other photostimulation epochs, VGAT-ChR2 mice, anatomy (26 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not describe their photostimulation codes; the notebook reads them from the timing of
the ALM response. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/gao-2018-01.yaml`](../../attempts/gao-2018-01.yaml).
