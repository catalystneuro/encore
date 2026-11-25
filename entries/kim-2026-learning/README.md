# Kim, Lycke, Zolotavin, Montes, Xie & Luan (2026) from dandiset 001868

Tests the findings of [Kim et al. (2026)](https://doi.org/10.64898/2026.06.05.730421) that can be
tested on [DANDI:001868](https://dandiarchive.org/dandiset/001868/0.260715.2016): the behaviour, the
sorted units and the ICMS trains of six trained mice, the activation tables of
six passive controls, and the recordings of four of them.

| Claim | Outcome |
|---|---|
| Detection thresholds fall from 5.5 to 4.2 uA | Reproduced |
| Response times fall with training | Reproduced |
| Wheel-movement onset falls; 122, 135 and 129 ms medians | Reproduced (assumed) |
| 973 units, 484 modulated, bimodal spike width | Not reproduced |
| Modulation of all cells rises; stable at threshold | Partially reproduced |
| More modulated units in Mouse 1 at 4 uA, none at group level | Not reproduced (assumed) |
| Changes driven by pyramidal cells | Reproduced (assumed); partially reproduced under the criterion's cell-type rule, proposed |
| Over 80% of units keep their PL or NPL identity | Reproduced |
| Pyramidal cells more common among PL units (76.2 against 49.8%) | Partially reproduced |
| Conduction velocities of 0.2 to 0.27 m/s | Not reproduced |
| PL modulation rises, latency falls at 5 and 6 uA | Partially reproduced |
| NPL responses do not change | Reproduced |
| PL peak spike probability rises at 5 and 6 uA | Partially reproduced |
| The same in a 120 ms pre-movement window | Partially reproduced (assumed) |
| No change in control mice (ephys) | Not reproduced (assumed) |
| No change in control mice (imaging) | Not reproduced |
| KL divergence of hit and miss | Partially reproduced |
| NPL hit-miss divergence from 65 and 35 ms, none in PL | Not reproduced (assumed) |
| PL coupling rises, NPL stable | Reproduced |
| NPL coupling above PL | Reproduced |
| Coupling controls (fig. S9) | Partially reproduced (assumed) |
| Volumetric activation (Figure 2, six claims) | Blocked: metadata insufficient |
| Tracked imaged neurons (Figure 3 and fig. S6, ten claims) | Blocked: metadata insufficient |
| Waveform separation and UnitMatch tracking (two claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The volumetric dF/F cannot be placed in the trial windows, the planar ROIs are not linked across
sessions, and the files hold one mean waveform per unit, so 18 claims are blocked. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/kim-2026-learning-01.yaml`](../../attempts/kim-2026-learning-01.yaml).

- `reproduce_kim_2026_learning.ipynb`: the analysis. It takes about 15 minutes, most of it the
  psychometric fits and the pulse-locking of each claim under five seeds.
- `icms.py`: loading the files, the responses (modulation, time to maximum, pulse-locking, latency),
  the thresholds, the wheel onsets, the KL divergence, the cluster test and the population coupling.
  Other notebooks on this dandiset can import it.
