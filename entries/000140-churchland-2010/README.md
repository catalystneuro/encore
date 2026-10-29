# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000140

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000140](https://dandiarchive.org/dandiset/000140/0.220113.0408) (MC_Maze_Small of
the Neural Latents Benchmark), which holds 100 trials of 27 maze conditions recorded with the two Utah
arrays of monkey J. The paper's J-array dataset has 108 conditions and about 2166 trials per neuron; its
single-electrode datasets of monkeys A, B and J and its EMG are not in the dandiset.

| Claim | Outcome |
|---|---|
| Mean preparatory to peri-movement tuning correlation, J-array (r = 0.13) | Not reproduced |
| The same for monkeys A, B and J | Blocked: data missing |
| Correlations broad and centred near zero | Not reproduced (assumption) |
| Correlation falls to near zero by movement onset | Reproduced (assumption; trial noise also passes) |
| Population averages lose preparatory tuning by movement onset | Reproduced (trial noise passes about half the time) |
| PD performance best in the peri-movement space, J-array | Partially reproduced (assumption) |
| The same for monkeys A, B and J | Blocked: data missing |
| Peri-movement space best at each dimensionality | Not reproduced |
| Endpoints + max. speed space performs poorly in the maze task | Not reproduced (assumption) |
| Performance rises with dimensionality, then declines above 10 | Not reproduced (assumption) |
| Summary ranking across monkeys A, B and J (Figure 6E) | Blocked: data missing |
| 7 to 10 dimensions capture 90% of preparatory variance | Not reproduced |
| Shuffled peri-movement space performs poorly | Reproduced (weak) |
| Window start can slide to movement onset (97% of performance) | Not reproduced (assumption) |
| Tuning correlation does not depend on AP location, J-array | Reproduced (assumption) |
| The same for monkeys A, B and J | Blocked: data missing |
| Peri-movement space works at anterior and posterior sites | Blocked: other (normalisation undefined) |
| Preparatory activity more prevalent at anterior sites | Blocked: metadata insufficient (which array is anterior) |
| PD more stable in the peri-movement space | Not reproduced |
| Rotational linear system: low correlation, perfect PD | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

With 1 to 4 trials per condition the condition means are noisy (median split-half reliability of
preparatory tuning 0.20). With condition labels shuffled about as many units pass the 5 spikes/s range
rule as with the true labels, and the two time-course criteria (Figure 4E, Supplemental Figure 1) are
met by trial noise. When tuning is read as the range across conditions every preferred direction space
performs below zero. Several outcomes change when tuning is read as the SD across
conditions, which keeps 7 or 8 units. Every unit's electrode entry points to the PMd group and the
electrodes have no positions, so the anterior-posterior claims use the array read from the unit ids;
the file does not say which array is PMd.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000140-churchland-2010-01.yaml`](../../attempts/000140-churchland-2010-01.yaml).

- `reproduce_churchland_2010.ipynb`: the analysis, about four minutes.
- `maze_prep.py`: loading, condition means, tuning measures, the leave-one-condition-out PD
  performance, the peri-movement, kinematic and task spaces, and the Figure 8 simulation. Other
  notebooks on this dandiset can import it.
