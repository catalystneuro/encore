# Geiller, Vancura et al. (2020) from dandiset 000625

Tests the findings of [Geiller, Vancura et al. (2020)](https://doi.org/10.1016/j.neuron.2020.09.013)
that can be tested on [DANDI:000625](https://dandiarchive.org/dandiset/000625/0.231114.0019),
which holds three random-foraging sessions of one mouse, with 231 interneurons of which 74 carry
one of the paper's six subtypes.

| Claim | Outcome |
|---|---|
| Interneurons imaged and identified per mouse | Partially reproduced |
| Most interneurons positively correlated with velocity, about 10% negatively | Reproduced |
| Negative correlations enriched in CCKC | Reproduced |
| Velocity correlation differs between subtypes | Reproduced |
| IvC/NGFC less modulated by locomotion | Not reproduced |
| Negatively correlated cells more tightly locked in time to velocity | Not reproduced |
| Immobility-triggered activation specific to CCKC | Partially reproduced |
| 17.5% of interneurons spatially selective; 12.7% with negative fields | Not reproduced |
| Spatially selective subset decodes position about as well as all cells | Not reproduced |
| Selectivity index does not differ between subtypes | Reproduced |
| Spatially selective PVBC more stable than SomC | Not reproduced |
| PVBC most and CCKC least stable within session | Partially reproduced |
| Stability across sessions lower but above chance | Partially reproduced |
| Depth, SWR, novel-context, goal-oriented learning, VIP and classifier findings (12 claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The stated imaging rate is wrong for two of the three sessions; the notebook fits it from the
data and shows why. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000625-geiller-2020-01.yaml`](../../attempts/000625-geiller-2020-01.yaml).

- `reproduce_geiller_2020.ipynb`: the analysis. It takes about eight minutes.
- `interneurons.py`: loading a session, the frame-rate fit, and the velocity, run-event,
  place-field, decoding and stability measures. Other notebooks on this dandiset can import it.
