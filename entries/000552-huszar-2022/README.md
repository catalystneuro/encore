# Huszar, Zhang, Blockus & Buzsaki (2022) from dandiset 000552

Tests the findings of [Huszar et al. (2022)](https://doi.org/10.1038/s41593-022-01138-x) that can be
tested on [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.230630.2304), which holds sleep
states, sharp-wave ripples, spike-sorted units and position from 17 mice whose CA1 pyramidal neurons
were birthdated by in utero electroporation. The units carry no label of which neurons responded to
light (were birthdated), and no optogenetic pulse times, cell types or waveforms are stored, so the
paper's comparisons of same- and different-birthdate neurons cannot be made.

| Claim | Outcome |
|---|---|
| 17 mice at the stated birthdates, 12 males and 5 females | Not reproduced (one mouse's sex field) |
| 92 sessions of 113.7 to 475.6 min, median 309.1, each with sleep | Partially reproduced |
| Median SPW-R duration 36.4 ms, limits 20 to 200 ms | Reproduced |
| 9,471 well-isolated units | Not reproduced |
| Nine figure-eight mice by birthdate, three novel-environment mice | Reproduced |
| 205 cm trials, 30 Hz tracking, ten or more trials per arm | Not reproduced |
| 16 novel environment explorations | Partially reproduced |
| Population vectors decorrelate after the maze stem (Figure 5e) | Partially reproduced |
| Firing rates preserved between familiar and novel mazes (Figure 6c) | Reproduced |
| Ratemap correlations higher in novel mazes (Figure 6c) | Not reproduced |
| Spatial information lower in novel mazes (Figure 6d) | Partially reproduced |
| Firing rates lower in novel mazes (Figure 6d) | Partially reproduced |
| Same- against different-birthdate comparisons, birthdate profiles, model, histology (22 claims) | Blocked: data missing |
| Convergence onto interneurons over all pairs (Figure 7f, g) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

Putative pyramidal cells are units with a session mean rate of at most 5 Hz, as the files hold no
cell type, and the "theta-related" rate is the rate while running; both are substitutes for the
paper's methods. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/000552-huszar-2022-01.yaml`](../../attempts/000552-huszar-2022-01.yaml).

- `reproduce_huszar_2022.ipynb`: the analysis. It takes about six minutes, most of it streaming the
  104 processed files.
- `huszar.py`: loading the files, maze recordings, rate maps, spatial information and running
  rates. Other notebooks on this dandiset can import it.
