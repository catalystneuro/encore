# Churchland et al. (2012) from dandiset 000070

Tests the findings of [Churchland et al. (2012)](https://doi.org/10.1038/nature11129) that can be
tested on [DANDI:000070](https://dandiarchive.org/dandiset/000070/0.261122.2046), which holds the
paper's two Utah-array datasets, J-array (sub-Jenkins ses-20090918) and N-array (sub-Nitschke
ses-20100923), with 108 maze conditions each. Their Units tables hold unsorted threshold crossings,
one per electrode (192 per session), where the paper analysed 146 and 218 sorted isolations. The
single-electrode datasets, the EMG and the leech and walking-monkey recordings are not in it.

| Claim | Outcome |
|---|---|
| The array datasets have 108 conditions and 146 and 218 isolations | Partially reproduced |
| The state rotates the same way for all conditions | Reproduced |
| Rotations do not depend on reach curvature | Partially reproduced (assumed onset column) |
| The rotation phase follows from the preparatory state | Partially reproduced |
| The jPCA plane captures 28% of the variance | Not reproduced (assumed onset column) |
| PC2 and PC3 capture 29%, as much as the jPCA plane | Not reproduced (assumed onset column) |
| J-array: three planes capture 22, 19 and 12% (Supplementary Figure 4) | Not reproduced |
| Three planes capture 50 to 70% in every dataset | Partially reproduced |
| The state-derivative angle peaks near pi/2 | Reproduced |
| M_skew fits nearly as well as the unconstrained M | Reproduced |
| Rotations up to about 2.5 Hz | Reproduced (assumed onset column) |
| Shuffle controls remove the rotations | Partially reproduced (assumed onset column) |
| PMd and M1 each capture 28 to 32% in the jPCA plane | Not reproduced |
| Rotations are faster in M1 than in PMd | Reproduced |
| A velocity-tuned simulated population does not rotate | Partially reproduced (assumed model) |
| A complex kinematic simulated population does not rotate | Not reproduced (assumed model) |
| Leech, walking monkey, single electrodes, EMG, generator model, speed task (six claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/churchland-2012-02.yaml`](../../attempts/churchland-2012-02.yaml).

- `reproduce_churchland_2012.ipynb`: the analysis. It takes about twenty minutes, most of it
  streaming the spikes and simulating the kinematic populations.
- `reach.py`: loading the files, condition-averaged rates aligned on movement onset, jPCA as in the
  paper's Methods, the shuffle controls of Supplementary Figure 2 and the simulated kinematic
  populations. Other notebooks on this dandiset can import it.
