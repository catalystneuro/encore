# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000138

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015)
that can be tested on [DANDI:000138](https://dandiarchive.org/dandiset/000138/0.220113.0407)
(MC_Maze_Large, Neural Latents Benchmark), which holds 500 maze-task trials over 27 conditions and
162 units recorded with two Utah arrays in one session of monkey J. The paper's J-array dataset had
108 conditions; its single-electrode datasets (monkeys A, B and J) and the EMG are not in the
dandiset.

| Claim | Outcome |
|---|---|
| Single-electrode datasets: weak positive tuning correlation (Figure 4A-C) | Blocked: data missing |
| J-array: weak positive tuning correlation, mean r 0.13 (Figure 4D) | Partially reproduced (assumption) |
| The correlation is near zero by movement onset (Figure 4E) | Not reproduced |
| No effect of anterior-posterior location on the correlation | Reproduced for J-array (assumption) |
| 7 to 10 dimensions hold 90% of preparatory variance | Reproduced (assumption) |
| The peri-movement space captures preparatory tuning best (Figure 6) | Reproduced |
| The peri-movement space wins at almost every dimensionality | Reproduced (assumption) |
| Performance rises with dimensionality and falls beyond about 10 | Reproduced (assumption) |
| The PD performs above zero in most spaces | Reproduced (assumption) |
| Summary over monkeys A, B and J (Figure 6E) | Blocked: data missing |
| A shuffled peri-movement space performs poorly (Figure 7A) | Reproduced (assumption) |
| Starting the window at movement onset keeps 97% of performance (Figure 7B) | Reproduced for J-array (assumption) |
| Anterior and posterior sites perform like random halves (Figure 7C) | Not reproduced (assumption) |
| The PD is most stable in the peri-movement space (Figure 7D) | Reproduced for J-array |
| A linear oscillator shows both findings (Figure 8) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper leaves several method details open (the proto-trial used to select trials, movement
onset, what "tuning" in spikes/s means, whether the PCA space is recomputed for each left-out
condition, and others). The notebook runs every reading; "assumption" marks an outcome that
differs between readings and rests on the reading best supported by the paper. The units'
electrode references all point to the PMd array; the array of each unit is taken from the unit id
prefix, which the files do not document. The attempt record, with the reasons and the differences
from the paper's method, is
[`attempts/000138-churchland-2010-01.yaml`](../../attempts/000138-churchland-2010-01.yaml).

- `reproduce_churchland_2010.ipynb`: the analysis. It takes about ten minutes, most of it the
  grid of readings for Figure 6 and the refit variants of Figure 7.
- `prepspace.py`: loading, trial selection, firing rates, the task, kinematic and peri-movement
  spaces, and leave-one-condition-out PD performance. Other notebooks on this dandiset can import
  it.
