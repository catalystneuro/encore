# Senzai, Fernandez-Ruiz & Buzsaki (2019) from dandiset 000166

Tests the findings of [Senzai et al. (2019)](https://doi.org/10.1016/j.neuron.2018.12.009) on
[DANDI:000166](https://dandiarchive.org/dandiset/000166/0.250624.0434), which holds one session from each of 19
mice recorded with a 64-site linear probe in V1: spike-sorted units, the raw signal, the LFP, brain state and
UP/DOWN intervals, and laser pulse times. It holds no unit waveforms, site depths, or layer labels.

| Claim | Outcome |
|---|---|
| 1,472 units, 251 narrow-waveform I cells and 1,075 wide-waveform E cells | Reproduced |
| 347 CCG-based E and 100 I cells, agreeing with the waveform classes | Not reproduced |
| 525 excitatory and 323 inhibitory connections among 102,332 pairs | Not reproduced |
| Most E cells have one I target; an I cell has up to 16 presynaptic E cells | Partially reproduced |
| I-E dips stronger in waking than in non-REM (24.1% against 22.8%) | Not reproduced |
| 14 of 15 PV and 40 of 52 VGAT tagged cells are narrow-waveform I cells | Not reproduced |
| Spike-LFP coupling strongest at 3-6 Hz, then 30-60 Hz | Partially reproduced (assumed LFP site) |
| Distances between the five depth landmarks vary by less than 100 um | Blocked: methods underspecified |
| Lognormal connection strengths; analogy with monkey alpha | Blocked: methods underspecified |
| Light-evoked CSD landmarks and the visual offset rebound (three claims) | Blocked: data missing |
| Laminar LFP coupling and phase claims placed by the landmarks (four claims) | Blocked: methods underspecified |
| Claims that rest on the landmarks, gamma ICs or the eight unit clusters (30 claims) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper places its depth landmarks by eye, and a rule that takes the extreme CSD sinks and sources places them
inconsistently across mice, so the layer groups that most of the paper's findings rest on could not be rebuilt. The
dataset holds the visual stimulus times for 2 of the 13 stimulated mice, and its genotypes disagree with the paper's
counts of PV-Cre and VGAT-Cre mice. The attempt record, with the reasons and the differences from the paper's method,
is [`attempts/000166-senzai-2019-01.yaml`](../../attempts/000166-senzai-2019-01.yaml).
