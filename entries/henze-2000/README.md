# Henze, Borhegyi, Csicsvari, Mamiya, Harris & Buzsaki (2000) on CRCNS hc-1

Tests the findings of [Henze et al. (2000)](https://doi.org/10.1152/jn.2000.84.1.390) that can be
tested on [CRCNS hc-1](https://doi.org/10.6080/K02Z13FP), simultaneous intracellular and
extracellular recordings from CA1 cells of anesthetized rats: 21 cells recorded with a wire
tetrode and 18 with a two-shank silicon probe. The behaving-animal recordings and the
histological distances the paper also uses are not in the data set.

| Claim | Outcome |
|---|---|
| 33 cells recorded, 22 kept, 21 pyramidal and 1 interneuron | Not reproduced |
| Extracellular and intracellular start and end coincide | Not reproduced |
| Duration 1.28 ms intracellular, 1.27 ms extracellular | Reproduced |
| The two durations correlate (R = 0.66) | Reproduced, resting on an assumption |
| Extracellular negative peak precedes the AP peak by 0.20 ms | Reproduced |
| The extracellular spike departs from the derivative after the rising phase | Reproduced |
| Notch and slope change match the AP peak and the AHP peak | Not reproduced |
| The basket cell has a narrow spike | Blocked: metadata insufficient |
| Latency grows as AP amplitude falls, longer in dendrites | Reproduced |
| The example somatic and dendritic pair (0.28 and 0.55 ms) | Not reproduced, resting on an assumption |
| Back-propagation velocity 1.61 m/s | Not reproduced |
| APs and extracellular spikes attenuate during evoked trains | Partially reproduced, resting on an assumption (not reproduced proposed for review) |
| Extracellular and intracellular amplitudes correlate in bursts (R = 0.40) | Reproduced |
| Spike amplitude and firing rate in theta sleep (two claims) | Blocked: data missing |
| Amplitude against distance and the cell-count estimates (three claims) | Blocked: data missing |
| The spike spreads 100 um or more along a silicon probe | Not reproduced |
| Propagation velocities of 0.4 to 2 m/s | Blocked: data missing |
| Spikes on neighbouring shanks | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set gives no cell type, impalement site or distance for 19 of its 21 tetrode cells, and
names the recording channels in only 5 of 39 folders; the notebook finds the intracellular
channel in each file from the data and classifies somatic and dendritic impalements by the
paper's rule, allowing 10 mV for the electrode offset the data set does not give, and shows the
timing claims under three other versions of the rule. The attempt record, with the reasons and
the differences from the paper's method, is [`attempts/henze-2000-01.yaml`](../../attempts/henze-2000-01.yaml).
