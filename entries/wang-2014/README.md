# Wang, Romani, Lustig, Leonardo & Pastalkova (2015) on CRCNS hc-5

Tests the findings of [Wang et al. (2015)](https://doi.org/10.1038/nn.3904), "Theta sequences are
essential for internally generated hippocampal firing fields", on
[CRCNS hc-5](https://doi.org/10.6080/K0KS6PHF). The data set names the paper, but it holds 13 sessions
of one rat (i01) recorded in June 2008 without any injection: alternation sessions with 15-20 s wheel
runs, home-cage wheel running and open-platform exploration. None of the paper's medial septum
muscimol or saline recordings, its linear track or its platform experiments are in it, so every
claim on recorded data is blocked. The three claims about the paper's network model need no data and
are tested by simulation.

| Claim | Outcome |
|---|---|
| 26 claims on recorded data (cell counts, Figures 1, 2, 4, 5, 6 and their supplementary figures) | Blocked: data missing |
| The model with theta builds theta sequences and fields; removing theta disrupts both (Fig. 3c) | Partially reproduced (assumed) |
| With a moving cue, removing theta disrupts sequences but fields are kept (Fig. 3d) | Reproduced (assumed) |
| Raising the nonspecific input without theta gives fast sequences, not fields (Supp. Fig. 10b,c) | Reproduced (assumed) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The notebook streams all 130 GB of the data set's archives to list their contents and read each
session's processed file; nothing is written to disk. The attempt record, with the reasons and the
differences from the paper's method, is [`attempts/wang-2014-01.yaml`](../../attempts/wang-2014-01.yaml).
