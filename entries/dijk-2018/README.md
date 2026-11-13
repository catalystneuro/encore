# van Dijk and Fenton (2018) from CRCNS hc-17

Tests the findings of [van Dijk and Fenton (2018)](https://doi.org/10.1016/j.neuron.2018.04.018)
that can be tested on [CRCNS hc-17](https://doi.org/10.6080/K0Q23XDV), which holds the tetrode
spike trains and tracking of wild-type mice in the environment manipulation experiment (Figure 1)
and the active place avoidance task (Figures 3 to 6), with the paper's lists of place cells and
putative interneurons. The optogenetic experiments of Figure 2 are not in it.

| Claims | Outcome |
|---|---|
| Rate map stability, DG below CA and lower after wall removal; rate remapping (Figure 1B, C) | Reproduced |
| Place field counts in the environment experiment | Not reproduced |
| Table S1 properties (DG against CA) | Partially reproduced |
| Behaviour: learning curve partly, shock-on against shock-off not, running speed reproduced | Mixed |
| Stability and rate remapping in the place avoidance task (Figure 3C, D) | Mostly reproduced; interneurons and Table S2 not |
| Positional information (Figure 4) | Four of five reproduced or partially; the speed correlation not |
| Overdispersion and overall network consistency | Reproduced; zone network consistency not |
| Place cell-interneuron correlations and their changes (Figure 5D, S2) | Mostly reproduced; pair class counts and negative pairs not |
| Correlations near shock zones and before avoidances (Figures 5E, 6) | Not reproduced, except the absence before errors and the rate change insets |
| Optogenetic experiments (Figure 2, four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with every outcome, the reasons and the differences from the paper's method,
is [`attempts/dijk-2018-01.yaml`](../../attempts/dijk-2018-01.yaml).

- `reproduce_dijk_2018.ipynb`: the analysis. It takes about five minutes, a little over one of
  which is streaming the files from the archive.
- `hc17.py`: reading the TS and Tracker files from the zip in place, the cell lists, sessions,
  shock zone geometry, rate maps, stability, fields, information, coherence, positional
  information, standardized rates and the paper's statistics. Other notebooks on this data set
  can import it.
