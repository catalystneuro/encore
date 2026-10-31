# Hulsey, Zumwalt, Mazzucato, McCormick & Jaramillo (2024) from dandiset 000678

Tests the findings of [Hulsey et al. (2024)](https://doi.org/10.1016/j.celrep.2024.113709) on
[DANDI:000678](https://dandiarchive.org/dandiset/000678/0.231004.2146), which holds the stage 5 and 6
sessions of the 13 mice the paper analysed, with pupil diameter, face motion energy and locomotion
speed. The notebook fits the paper's GLM-HMM to each mouse's choices, labels the performance states,
and relates them to the arousal and movement measures.

| Claim | Outcome |
|---|---|
| 13 mice included, 8 auditory and 5 visual, 381 sessions | Partially reproduced (376 sessions) |
| 21 +/- 8 training sessions to reach stage 5 | Blocked: data missing |
| Distractor responses below 10% | Reproduced |
| 3 to 5 GLM-HMM states per mouse | Reproduced |
| Example mouse: 4 states, 78% against 70% of choices predicted | Reproduced |
| Every mouse has optimal, disengaged and sub-optimal states | Reproduced (one assumption) |
| Optimal state most occupied; 13.1% indeterminate | Reproduced |
| Optimal epochs longer; 3.4-trial transitions | Partially reproduced |
| GLM-HMM predicts 75.7% of choices, 10.8% better than one state | Reproduced |
| Inverted U of optimal state on pupil diameter | Reproduced |
| Smaller optimal pupil in the auditory task | Reproduced |
| Inverted U (optimal) and U (disengaged) aligned to the optimal pupil | Reproduced |
| Face and locomotion r2 below pupil's | Partially reproduced |
| Inverted U on the movement index, r2 like pupil's | Reproduced |
| U of the disengaged state on the movement index | Reproduced |
| Movement index equally correlated with face and locomotion | Reproduced |
| Pupil closest to optimal in the optimal state | Partially reproduced |
| Face motion energy larger in the optimal state | Reproduced |
| No difference in locomotion speed between states | Reproduced |
| Lower variability of the measures in the optimal state | Partially reproduced |
| Variability falls on entering and rises on leaving the optimal state | Partially reproduced |
| Pupil and movement decoupled in the optimal state | Reproduced |
| Pupil decoupled from face and locomotion in the optimal state | Reproduced |
| SVM decoding of states: 88.2% and 77.7% | Reproduced |
| Pupil the best single raw measure for decoding | Reproduced |
| Movement index the best predictor of state | Not reproduced |
| Regression weights of pupil and locomotion terms | Reproduced |
| Pupil-by-movement interaction for sub-optimal states | Reproduced |
| ITI does not carry over; evoked pupil equal across states | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The GLM-HMM of the paper's ssm fork is reimplemented in `hulsey.py`, and the decoders use fewer
shuffle runs than the paper, to keep the notebook near 26 minutes on 4 cores. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000678-hulsey-2024-01.yaml`](../../attempts/000678-hulsey-2024-01.yaml).

- `reproduce_hulsey_2024.ipynb`: the analysis.
- `hulsey.py`: streaming and preprocessing the files as the paper's code does, the GLM-HMM, state
  labels, dwell times, choice prediction and the decoders. Other notebooks on this dandiset can
  import it.
