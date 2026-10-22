# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000128

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000128](https://dandiarchive.org/dandiset/000128/0.220113.0400) (MC_Maze), which
holds the paper's J-array dataset: one session of monkey Jenkins on the maze task, 108 conditions,
recorded with two 96-electrode arrays. The speed task (monkeys A and B), the single-electrode maze
recordings (monkey J) and EMG are not in it.

| Claim | Outcome |
|---|---|
| The J-array dataset: 146 units, 108 conditions, about 2166 trials | Partially reproduced (182 units) |
| Mean correlation of preparatory and peri-movement tuning 0.13 (J-array) | Not reproduced |
| No separate concordant and opposing populations | Reproduced |
| The correlation declines from about 200 ms before movement onset to near zero | Reproduced |
| Population averages lose their relation to preparatory tuning by movement onset | Reproduced |
| 7 to 10 dimensions capture 90% of preparatory variance | Not reproduced |
| Most maze neurons do not keep their tuning | Reproduced |
| PD performance is highest in the peri-movement space | Reproduced |
| The peri-movement space wins at almost every dimensionality | Reproduced |
| PD performance peaks near 10 dimensions and then declines | Not reproduced (still rising at 14) |
| The shuffled peri-movement space performs poorly | Reproduced |
| Starting the peri-movement window at onset keeps about 97% of PD performance | Reproduced |
| The PD is most stable in the peri-movement space | Reproduced |
| The oscillator model: low tuning correlation, PD captures tuning perfectly | Reproduced (2 claims) |
| Anterior against posterior sites | Blocked: metadata insufficient (2 claims) |
| Speed task, single-electrode and EMG data | Blocked: data missing (5 claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000128-churchland-2010-01.yaml`](../../attempts/000128-churchland-2010-01.yaml).

The outcomes follow the answers of 2026-10-22 to the attempt's questions (`questions/000128.yaml`): the
proto-trial selection is reading T2 and the tuning measure reading S1.

- `reproduce_churchland_2010.ipynb`: the analysis. It takes about two minutes, most of it computing
  smoothed firing rates.
- `mcmaze.py`: streaming the files, the trial selection, condition-mean firing rates, the PD fits and
  the kinematic and task spaces. Other notebooks on this dandiset can import it.
