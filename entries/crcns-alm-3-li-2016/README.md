# Li, Daie, Svoboda & Druckmann (2016) from CRCNS alm-3

Tests the findings of [Li et al. (2016)](https://doi.org/10.1038/nature17643) that can be tested
on CRCNS data set [alm-3](https://doi.org/10.6080/K0RB72JW), which holds the sorted single units,
trial tables, photostimulus types and lick and laser traces of 91 recording sessions from 19 mice:
unilateral photoinhibition (Experiment 1), bilateral experiments (Experiments 2 and 3) and
callosotomy. CRCNS data sets are not versioned; the files are streamed from the public bucket and
their MD5 sums printed in the notebook.

| Claim | Outcome |
|---|---|
| Unit and session counts | Not reproduced (FS count 89 against 72; the other counts exact) |
| Selective fraction of pyramidal neurons (ED Fig. 1) | Reproduced |
| Earlier photoinhibition has minimal behavioural effect (Fig. 1d) | Reproduced |
| Photoinhibition silences more than 90% of activity (ED Fig. 2b) | Reproduced |
| No rebound after photoinhibition (ED Fig. 2e) | Partially reproduced |
| Rate recovery in 90% of neurons (Fig. 1f) | Partially reproduced |
| Selectivity recovery times after unilateral photoinhibition (Fig. 1g) | Reproduced |
| Decreasing neurons return to their trajectory (ED Fig. 4) | Not reproduced |
| Behaviour under unilateral and bilateral photoinhibition (Fig. 2b) | Partially reproduced |
| Bilateral bias follows the cd trajectory (ED Fig. 6) | Reproduced |
| Recovery after ipsilateral, contralateral and bilateral photoinhibition (Fig. 2) | Partially reproduced |
| Experiment 3 recovery (ED Fig. 7d) | Partially reproduced |
| Experiment 3 cd ROC (ED Fig. 7e) | Partially reproduced |
| cd ROC at the end of the delay (Fig. 3) | Reproduced |
| cd ROC during photoinhibition (ED Fig. 8) | Reproduced |
| Stability of the coding direction (ED Fig. 9b) | Reproduced |
| Variance and selectivity captured by the modes (ED Fig. 8a) | Partially reproduced |
| cd predicts the movement trial by trial (Fig. 3, 4) | Reproduced |
| Persistent and ramping modes (Fig. 3d, e) | Not reproduced |
| Callosotomy behaviour (Fig. 5b) | Partially reproduced (after the cut only) |
| Callosotomy recovery (Fig. 5) | Reproduced |
| Callosotomy preparatory activity (ED Fig. 10) | Partially reproduced |
| Monolithic models fail to recover (ED Fig. 1) | Partially reproduced (three of five models simulated) |
| Modular models are robust (Fig. 6) | Partially reproduced |
| Late-delay bias, recovery interval, spatial extent, photoactivation (Fig. 1d, ED Fig. 2d, 3, 5) | Blocked: data missing |
| Reaction time and distance from the boundary (ED Fig. 9f) | Blocked: data missing (no licks in the Experiment 2 lick traces) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Method details the claims file leaves open are taken from the Methods and, where those leave them
open, from the authors' MATLAB analysis scripts deposited in the data set. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/crcns-alm-3-li-2016-01.yaml`](../../attempts/crcns-alm-3-li-2016-01.yaml).

- `reproduce_li_2016.ipynb`: the analysis. It takes about four minutes, most of it streaming the
  12 GB of session files.
- `alm3.py`: streaming and reducing the session files, trial selection, spike counts, the rate
  test, selectivity recovery and the population analyses. Other notebooks on this data set can
  import it.
- `models.py`: the network models of the Methods.
