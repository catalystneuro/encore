# Pakhomov et al. (2023) from dandisets 000686, 000875, 001025, 001027 and 001028

Tests the findings of [Pakhomov et al. (2023)](https://doi.org/10.1016/j.bioelechem.2023.108437)
on the five dandisets that hold its monolayer images:
[000686](https://dandiarchive.org/dandiset/000686/0.240515.1909) (Fig. 5),
[000875](https://dandiarchive.org/dandiset/000875/0.240515.1925) (Fig. 6),
[001025](https://dandiarchive.org/dandiset/001025/0.240605.1826) (Fig. 7),
[001027](https://dandiarchive.org/dandiset/001027/0.240605.1859) (Fig. 8) and
[001028](https://dandiarchive.org/dandiset/001028/0.240605.1954) (Fig. 9). Each file holds one
dish, a stitched image of YO-PRO-1 uptake, and 17 files of 001025 and 001028 hold a second
channel. The files hold no ROI, pixel size or electrode
position, so the electrode square is found in each image and the ROIs of Methods 2.4 are rebuilt
from it (`cancan.py`). The single-cell time lapse of Fig. 4 and the field simulations of Fig. 3
are in none of the datasets.

| Claim | Outcome |
|---|---|
| Fig. 3 field simulation; Fig. 4 single-cell cancellation (four claims); cancellation predicts targeting | Blocked: data missing |
| 5A: trains stronger than packets throughout the array | Not reproduced |
| 5A: packets enhance the centre, near e1 still stronger | Partially reproduced |
| 5B: rotated packets give a central peak, rotated trains a central void | Blocked: methods underspecified (readings disagree) |
| 5C: normalized centre higher for packets than trains | Blocked: depends on 5B (its own test holds) |
| 6A: more packets, more uptake, central peak for all | Partially reproduced |
| 6B: centre about 200% for 1Px4, about 100% for 5Px4 and 10Px4 | Partially reproduced |
| 6: trough about half the centre | Partially reproduced |
| 6: peak narrower with more packets | Blocked: methods underspecified (readings disagree) |
| 7A: 15.5 to 16.8-fold rise from 2.4 to 5.6 kV | Partially reproduced |
| 7B: normalized profiles independent of amplitude, small array | Blocked: methods underspecified (readings disagree) |
| 7C, D: the same in the large array | Blocked: methods underspecified (readings disagree) |
| Discussion: targeting independent of amplitude and array size | Blocked: depends on 7B |
| 8A: equal centre uptake for Packets 1 to 3 | Not reproduced |
| 8A: more uptake near electrodes for Packets 1 and 3 | Not reproduced |
| 8B: normalized centre 183% for Packet 2, 83% and 74% for 3 and 1 | Not reproduced |
| 9A: lifting the array lowers uptake near electrodes more than in the centre | Partially reproduced |
| 9B: targeting up to 600% at 2 mm | Reproduced |
| 9C: uptake restricted to the centre with lifted electrodes | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/pakhomov-2023-05.yaml`](../../attempts/pakhomov-2023-05.yaml).
