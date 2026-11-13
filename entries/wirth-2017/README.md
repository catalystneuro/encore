# Wirth, Baraduc, Plante, Pinede & Duhamel (2017) from CRCNS hc-12

Tests the findings of [Wirth et al. (2017)](https://doi.org/10.1371/journal.pbio.2001045) that can be
tested on [CRCNS hc-12](https://doi.org/10.6080/K0R49NQV), which holds the 189 analysed hippocampal
cells of two macaques navigating a virtual star maze, with eye tracking. [CRCNS
hc-21](https://doi.org/10.6080/K0GX48R9) is read to check which of its recordings are also in hc-12.

| Claim | Outcome |
|---|---|
| Gaze anticipates the turn, and the side where landmarks will appear | Reproduced (sign of the eye signal assumed, supported by the slow phases) |
| Learning in about a dozen trials; fewer than 10 more trials to 90% | Reproduced |
| Performance after new entries in probe sessions | Not reproduced (monkey K only) |
| Faster learning after new entries | Blocked: methods underspecified |
| 189 cells analysed of 270 recorded | Partially reproduced |
| State space has the most responsive cells (84) | Not reproduced |
| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced (both with the three-space responsive cells standing in for the paper's set) |
| Higher information in state space than in position and direction space | Partially reproduced (the gaze comparison cannot be made) |
| Sparser in state space than in direction space | Reproduced (full-trial window) |
| Sparsity, state against position space | Not reproduced |
| State-space selectivity in the centre | Not reproduced (assuming permuted chunks; open under shifted chunks) |
| Landmark identity and distance (two-way ANOVA) | Not reproduced |
| Claims that need the point-of-gaze space or the paper's responsive set (11 claims) | Blocked: metadata insufficient |
| Number of fields, control for dimensionality | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The eye signal has no calibration, units or sign in the files, so the paper's point-of-gaze maps
cannot be built. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/wirth-2017-01.yaml`](../../attempts/wirth-2017-01.yaml).
