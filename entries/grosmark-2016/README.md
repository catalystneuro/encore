# Grosmark & Buzsáki (2016) from DANDI:000044 and CRCNS hc-11

Tests the findings of [Grosmark and Buzsáki (2016)](https://doi.org/10.1126/science.aad1935) on
its two datasets, [DANDI:000044](https://dandiarchive.org/dandiset/000044/0.261106.0236) and
[CRCNS hc-11](https://doi.org/10.6080/K0862DC5). Both hold the same eight sessions of bilateral CA1
recordings in four rats, each a PRE rest and sleep epoch, a novel maze and a POST epoch; their units,
spike times and state epochs are identical. Spikes, position and states are streamed from the
CRCNS sessInfo files and the LFP, for sharp wave-ripple detection, from the NWB files.

| Claim | Outcome |
|---|---|
| Four rats, eight sessions, PRE, MAZE and POST on linear and circular tracks | Reproduced |
| 491 place cells of 562 pyramidal cells | Partially reproduced |
| Sequence scores above chance; POST and MAZE above PRE; observed above null | Reproduced (4 claims) |
| Ripple-event duration unchanged from PRE to POST | Not reproduced |
| More place cells participate in POST events | Reproduced |
| Per cell contribution higher in POST | Partially reproduced |
| Strongly contributing cells (216), 73% overlap, 105 rigid and 105 plastic | Partially reproduced, reproduced, not reproduced |
| Per-cell PRE against POST PCC tests (2.2% and 21.4%) | Not reproduced |
| Shuffling or excluding high-dPCC cells, removing plastic cells | Partially reproduced, reproduced, reproduced |
| Rigid and plastic fields along the track | Reproduced |
| Plastic cells more specific; specificity rising over laps; out-of-field rate falling | Partially reproduced, not reproduced, not reproduced |
| Rigid cells fire faster; plastic cells' ripple gain, bursting and synchrony | Partially reproduced (3), not reproduced (bursting) |
| Cluster quality of rigid and plastic cells | Blocked: too large |
| Rate split medians; low-rate cells' coding | Reproduced, partially reproduced |
| Coactivity by firing rate (Figure 4C, three claims) | Reproduced, not reproduced, partially reproduced |
| Replay carried by slow cells and high-gain cells | Reproduced, partially reproduced |
| More ripples in POST; coactivity and temporal-bias preservation (four claims) | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The notebook uses fewer shuffles than the paper (200 null templates per event and 100
cell-specific shuffles, against 1,000) to fit the time limit. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/grosmark-2016-02.yaml`](../../attempts/grosmark-2016-02.yaml).
