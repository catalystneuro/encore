# Petersen & Buzsaki (2020) from dandiset 000059

Tests the findings of [Petersen and Buzsaki (2020)](https://doi.org/10.1016/j.neuron.2020.05.023)
that can be tested on [DANDI:000059](https://dandiarchive.org/dandiset/000059/0.250624.0444), which
holds 50 sessions of five rats running a spatial alternation task on a figure-8 maze while the
medial septum (MS) was cooled: MS temperature, trials with cooling state and choice errors,
position, LFP, wide-band data, and sorted units in 24 sessions.

| Claim | Outcome |
|---|---|
| Session structure (trials per state) | Reproduced |
| Cooling time course (minimum after 60 s, lasting 10 to 12 min) | Partially reproduced |
| Theta frequency follows MS temperature (R = 0.81) | Reproduced |
| Theta power follows MS temperature (R = 0.54) | Not reproduced |
| Frequency effect more consistent across rats than power | Reproduced |
| Theta frequency and power lower during cooling | Partially reproduced |
| Theta frequency falls by 12% | Partially reproduced |
| Errors increase about 3-fold, in every rat | Partially reproduced |
| Errors recover after cooling | Reproduced |
| Worst performance 4 to 8 trials after onset | Reproduced |
| Errors correlate with temperature and theta frequency (R = -0.35) | Partially reproduced (two claims) |
| Errors correlate with theta power in 2 of 5 rats | Partially reproduced |
| Errors do not correlate with running speed | Not reproduced |
| Running speed falls within a session | Reproduced |
| Running speed in control and cooling trials | Partially reproduced |
| Place cell and interneuron rates fall by 11 to 14% | Partially reproduced (two claims) |
| Interneuron oscillation frequency slows | Reproduced |
| Spike waveforms unchanged | Not reproduced |
| fp and fLFP fall and recover (Figure 4B values) | Reproduced |
| fp and fLFP correlated; fp and fLFP against temperature | Partially reproduced (two claims) |
| fp - fLFP preserved | Not reproduced |
| Field size before and during cooling correlated (R = 0.91) | Reproduced |
| Field size against fp; against the model of Geisler et al. | Partially reproduced (two claims) |
| Information content unchanged | Not reproduced |
| Population vector scale unchanged | Reproduced |
| Phase precession slope decreases | Partially reproduced |
| fp depends on speed more than fLFP, lower during cooling | Reproduced |
| Pair correlogram period lengthens (85 ms before) | Partially reproduced |
| Distance-time compression falls (0.54 cm/ms) | Not reproduced |
| Pair time lags increase | Reproduced |
| Pair phase lags, fraction active and spikes per cycle unchanged | Not reproduced (three claims) |
| Hippocampal temperature barely changes | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files carry no cell types, place fields or electrode locations, so putative cell types (from
waveforms streamed from the wide-band data) and place fields (the automatic criteria of the
Methods) are made here. The temperature of the MS10 sessions and of two control sessions is not a
recording. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000059-petersen-2020-01.yaml`](../../attempts/000059-petersen-2020-01.yaml).

- `reproduce_petersen_2020.ipynb`: the analysis. It takes about 6 minutes, most of it streaming
  LFP and wide-band data, with sessions processed in parallel.
- `cooling.py`: loading, the theta measures of the paper's code, trial measures and the
  onset-aligned series, linearization of the maze, place fields, oscillation frequency, pair
  cross-correlograms and waveforms. Other notebooks on this dandiset can import it.
