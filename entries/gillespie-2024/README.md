# Gillespie, Astudillo Maya, Denovellis, Desse & Frank (2024) from dandisets 000115 and 000629

Tests the findings of [Gillespie et al. (2024)](https://doi.org/10.7554/eLife.90944) on
[DANDI:000115](https://dandiarchive.org/dandiset/000115/0.210914.1732), the control cohort of four
rats, and on [DANDI:000629](https://dandiarchive.org/dandiset/000629/0.240627.0646), the
neurofeedback cohort the paper deposited. Both hold raw 30 kHz signals, head position, port events
and statescript logs, with no LFP, SWR detections, spikes or decodes.

| Claim | Outcome |
|---|---|
| Control trial counts per rat (2490, 2629, 2027, 3021) | Reproduced |
| Control epoch and trial counts of the replay analyses | Partially reproduced |
| Control post-reward dwell time increases with experience | Partially reproduced |
| Control head speed below 4 cm/s before reward | Reproduced |
| Control search efficiency increases over epochs | Reproduced (assumption) |
| Pre-reward time matched between NF and delay trials | Partially reproduced (three rats) |
| Post-reward dwell shorter on NF trials, about half of control | Partially reproduced (three rats) |
| Head speed below 4 cm/s, lower on NF trials | Partially reproduced (three rats) |
| Search efficiency higher than control on delay trials | Not reproduced |
| Redundant search trials balanced between NF and delay | Not reproduced |
| Repeat accuracy unchanged | Partially reproduced (three rats) |
| Repeat errors balanced between NF and delay | Partially reproduced (three rats) |
| 23 claims on SWRs and replay | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Trials are parsed from the port events by rules written here, as the lab's parser is not public;
the counts match the paper's within 3%. The neurofeedback plateau is not marked in the files and is
taken as the final days whose trial counts match the paper's, with the Methods' 7 and 10 days as
other readings. Rat 1 (remy) of the neurofeedback cohort could not be used: its port events are
corrupted. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/gillespie-2024-01.yaml`](../../attempts/gillespie-2024-01.yaml).
