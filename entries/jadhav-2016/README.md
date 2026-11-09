# Jadhav, Rothschild, Roumis & Frank (2016) from CRCNS hc-28

Tests the findings of [Jadhav et al. (2016)](https://doi.org/10.1016/j.neuron.2016.02.010) on
[CRCNS hc-28](https://doi.org/10.6080/K02N50G9), which holds simultaneous CA1 and prefrontal (PFC)
recordings from the three rats (HPa, HPb, HPc) that learned the W-track alternation task over 8 days.
The paper's three Y-track rats are not in the data set.

| Outcome | Claims |
|---|---|
| Reproduced | 9 |
| Partially reproduced | 7 |
| Not reproduced | 21 |
| Blocked | 2 (both need the Y-track rats) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Behavior, SWRs at the reward wells, the CA1-PFC pair findings in direction and the absence of task
structure in the pre-task rest hold. The central difference is SWR modulation of PFC cells: 19 of 167 PFC
cell-days are SWR modulated here (12 excited, 7 inhibited), against 56 of 165 in the paper's W-track data,
so most comparisons between excited, inhibited and unmodulated PFC cells fail. The classification stays far
from the paper's with SWRs detected on the mean of the tetrodes' envelopes and without the second-environment
(`wtr2`) runs of days 6 to 8. The notebook repeats the tests of every claim downstream of the classification under
both, and no claim that fails under the main reading meets its criterion under either; two that meet it under the main
reading fail under a variant (figs5-matched-selectivity under both, fig6e-glm-swr-prediction under the mean envelope).
The paper links no code,
and its SWR detection is described only by reference; the choices made here are recorded as assumptions,
and questions for the authors are in the attempt record,
[`attempts/jadhav-2016-01.yaml`](../../attempts/jadhav-2016-01.yaml).

- `reproduce_jadhav_2016.ipynb`: the analysis. It takes about 32 minutes, of which about 10 stream the
  three archives (2.7 GB each).
- `hc28.py`: streaming and reducing each animal's archive in memory (SWR detection, theta phase, units,
  position), and the measures used (SWR modulation, theta locking, cross-covariance, rate maps, trials,
  GLM, replay decoding). Other notebooks on this data set can import it.
