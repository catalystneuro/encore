# Watson, Levenstein, Greene, Gelinas & Buzsaki (2016) from CRCNS fcx-1

Tests the findings of [Watson et al. (2016)](https://doi.org/10.1016/j.neuron.2016.03.036) on
[CRCNS fcx-1](https://doi.org/10.6080/K02N506Q), which holds the spike trains, scored brain
states, detected UP/DOWN states and spindles, and LFP of 27 frontal cortex recordings in 11
rats. All 41 claims of the claims file are tested: 12 are reproduced, 15 partially reproduced and
14 not reproduced.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| Counts of cells, sessions, rats and WAKE-SLEEP episodes | Partially reproduced |
| Microarousal number, duration, incidence and time | Not reproduced |
| Median packet duration 111 s | Reproduced |
| pE and pI rate medians per state; skewed rates | Partially reproduced |
| nonREM against WAKE rate slope below 1 | Reproduced |
| Fraction of pE cells above 2 Hz per state | Reproduced |
| Burst index by state | Partially reproduced |
| Autocorrelogram peaks and decay | Partially reproduced |
| Skewed population synchrony | Reproduced |
| UP and DOWN durations | Reproduced |
| Rates, E/I ratio and spectra within UP states | Not reproduced |
| Stable UP-onset sequences, fast cells first | Reproduced |
| Pair correlations by rate group | Not reproduced |
| Population rate declines over sleep | Reproduced |
| First against last packet mean rate | Reproduced |
| Lower rates in WAKE after sleep | Partially reproduced |
| First against last packet slope below 1 | Reproduced |
| Top sextiles decrease, bottom increases over sleep | Reproduced |
| Rate CV decreases over sleep | Not reproduced |
| Spindles over sleep | Partially reproduced |
| UP/DOWN incidence and durations over sleep | Not reproduced |
| Within-UP rate changes over sleep | Partially reproduced |
| First against last REM, MA and WAKE slopes | Partially reproduced |
| WAKE before against after sleep, by sextile | Not reproduced |
| LFP band power within episodes and packets | Partially reproduced |
| UP/DOWN dynamics within packets | Reproduced |
| Spindles within episodes and packets | Partially reproduced |
| More sigma in late-packet UP states | Reproduced |
| Sextile, CV and burst trends within nonREM | Partially reproduced |
| Per-packet rate against LFP correlations | Partially reproduced |
| Within-UP sextile changes within packets | Not reproduced |
| Sextile trends within WAKE and REM | Not reproduced |
| MA-packet-MA triplets | Not reproduced |
| REM-packet-REM triplets | Not reproduced |
| Sigma and MA-to-MA change | Not reproduced |
| WAKE between packets | Partially reproduced (assumed) |
| MA between packets | Partially reproduced |
| REM between packets | Not reproduced |
| Delta change and slow-cell change | Not reproduced |
| Interneuron first against last packet slope of 1 | Not reproduced |
| Sleep homogenizes rates | Partially reproduced |

The data set matches the paper's counts of cells, sessions, rats, UP and DOWN states and spindles
exactly, but holds 51 WAKE-SLEEP episodes (54 in the paper) and 434 microarousals inside sleep
(790). The motion signal is not z-scored as described. Each session is one tar.gz whose member
order varies, so the notebook streams all 27 (about 90 GB) once, which takes about 12 minutes.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-fcx-1-watson-2016-01.yaml`](../../attempts/crcns-fcx-1-watson-2016-01.yaml).
