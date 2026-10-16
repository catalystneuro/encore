# Carcea et al. (2021) from dandiset 000114

Tests the findings of [Carcea et al. (2021)](https://doi.org/10.1038/s41586-021-03814-7) that can
be tested on [DANDI:000114](https://dandiarchive.org/dandiset/000114/0.230602.1643). The dandiset
holds PVN single units and video annotations from four virgin mice co-housed with a dam and
litter, raw voltage from a fifth, and fibre photometry from six virgins watching dam retrievals.
It does not hold the optical tagging that identifies oxytocin neurons, the behavioural cohorts of
Figures 1 to 4, or the auditory cortex data.

| Claim | Outcome |
|---|---|
| The behaviour labels can be named through the paper's code | Reproduced |
| Units activated during nest entry (26.5%) | Partially reproduced |
| Units activated during shepherding (11.9%) | Not reproduced |
| Units activated during dam retrieval (17.4%) | Partially reproduced |
| Higher firing after shepherded than voluntary nest entries | Not reproduced |
| Shepherding more often than 0.2 per hour (3.5 per hour) | Partially reproduced |
| Dams retrieve pups about once every two hours | Not reproduced |
| OT-PVN units; behavioural cohorts; observation units; auditory cortex (10 claims) | Blocked: data missing |
| Virgin-to-dam chases; photometry of learners against non-learners | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The behaviour labels in the files have no description; their names come from the paper's code
(GitHub `ic283/Carcea-et-al.-2021`, commit 2db2a75). The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/000114-carcea-2021-01.yaml`](../../attempts/000114-carcea-2021-01.yaml).

- `reproduce_carcea_2021.ipynb`: the analysis. It takes about two minutes, most of it streaming
  the spike times and photometry.
- `pvn.py`: loading the files without the raw voltage, the modulation index and shuffle test of the
  paper's code, and quality measures of the units. Other notebooks on this dandiset can import it.
