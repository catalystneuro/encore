# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000139

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000139](https://dandiarchive.org/dandiset/000139/0.220113.0408) (MC_Maze_Medium).
The dandiset holds one session of monkey J on the maze task, with two Utah arrays (152 units) and 250
labelled trials over 27 conditions, cut for the Neural Latents Benchmark. The paper's J-array dataset
had 108 conditions and about 2166 trials per neuron, so every measure here rests on far fewer trials.
The speed-task and single-electrode datasets and the EMG are not in the dandiset.

| Claim | Outcome |
|---|---|
| 146 units, 108 conditions in the J-array dataset | Partially reproduced (27 conditions, assumed among the 108) |
| Mean preparatory vs peri-movement correlation 0.13 (J-array) | Partially reproduced |
| Correlations broad and unimodal | Reproduced |
| Correlation declines from 200 ms before onset to near zero | Reproduced; in the main selection only through the splice, elsewhere with the decline near -300 ms |
| Population PSTHs show weak movement tuning by onset | Reproduced under reading (a) only; not under cross-validated ranking |
| Peri-movement space gives the best PD performance | Reproduced |
| Peri-movement space best at almost every dimensionality | Reproduced |
| Performance peaks at middle dimensionality | Reproduced, resting on S fixed across folds |
| Segment directions and initial velocity perform reasonably well | Reproduced (segments equal in time) |
| 7 to 10 dimensions for 90% of preparatory variance | Not reproduced |
| Shuffled space performs poorly | Reproduced |
| Window start can slide to onset (97%) | Reproduced |
| No effect of AP location on the tuning correlation | Reproduced |
| Anterior and posterior halves perform like random halves | Not reproduced |
| Preparatory activity more prevalent anteriorly | Blocked: metadata insufficient (which array is PMd) |
| PD most stable in peri-movement space | Reproduced |
| Some neurons better in other spaces | Reproduced |
| High-dimensional task spaces underperform | Reproduced |
| Linear dynamical system simulation (Figure 8) | Reproduced (full-cycle reading of the gray interval) |
| Monkeys A, B and J single-electrode results (four claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Several outcomes rest on readings of methods the paper leaves open (the proto-trial, the tuning
measure, whether the PCA space is recomputed in each cross-validation fold, where the Figure 4E
trace is spliced, the length of the Figure 8 gray interval); the notebook runs each
reading, and the attempt record,
[`attempts/000139-churchland-2010-01.yaml`](../../attempts/000139-churchland-2010-01.yaml), says which
was adopted and why. The units' electrode references all point at the PMd array; the array is read
from the unit ids, and the files do not say which id prefix is PMd.

- `reproduce_churchland_2010.ipynb`: the analysis, about ten minutes.
- `maze.py`: loading the files, trial selection, condition means, the PD model with
  leave-one-condition-out performance, and the peri-movement, kinematic and task spaces.
