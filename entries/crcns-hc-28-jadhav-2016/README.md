# Jadhav, Rothschild, Roumis & Frank (2016) from CRCNS hc-28

Tests the findings of [Jadhav et al. (2016)](https://doi.org/10.1016/j.neuron.2016.02.010) on
[CRCNS hc-28](https://doi.org/10.6080/K02N50G9), which holds simultaneous CA1 and prefrontal (PFC)
recordings from the three rats (HPa, HPb, HPc) that learned the W-track alternation task over 8 days.
The paper's three Y-track rats are not in the data set.

| Outcome | Claims |
|---|---|
| Reproduced | 7 |
| Partially reproduced | 12 |
| Not reproduced | 17 |
| Blocked | 3 (two need the Y-track rats; the replay analysis was not run in time) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Behavior, SWRs at the reward wells, the CA1-PFC pair findings in direction and the absence of task
structure in the pre-task rest hold. The central difference is SWR modulation of PFC cells: 19 of 167 PFC
cell-days are SWR modulated here (12 excited, 7 inhibited), against 56 of 165 in the paper's W-track data,
so most comparisons between excited, inhibited and unmodulated PFC cells fail. The paper links no code,
and its SWR detection is described only by reference; the choices made here are recorded as assumptions,
and questions for the authors are in the attempt record,
[`attempts/crcns-hc-28-jadhav-2016-01.yaml`](../../attempts/crcns-hc-28-jadhav-2016-01.yaml).

- `reproduce_jadhav_2016.ipynb`: the analysis. It takes about 20 minutes, of which about 8 stream the
  three archives (2.7 GB each).
- `hc28.py`: streaming and reducing each animal's archive in memory (SWR detection, theta phase, units,
  position), and the measures used (SWR modulation, theta locking, cross-covariance, rate maps, trials,
  GLM). Other notebooks on this data set can import it.
