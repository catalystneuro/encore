# Watson, Levenstein, Greene, Gelinas & Buzsáki (2016) from dandiset 000041

Tests the findings of [Watson et al. (2016)](https://doi.org/10.1016/j.neuron.2016.03.036) that can be
tested on [DANDI:000041](https://dandiarchive.org/dandiset/000041/0.250624.0419), which holds units,
LFP and sleep states recorded with silicon probes in the frontal cortex of rats in their home cage.
The dandiset holds 22 of the paper's 27 sessions and 10 of its 11 rats; one session's spike times
are unusable.

| Claim | Outcome |
|---|---|
| 11 rats, 27 sessions, 995 pE and 126 pI cells | Not reproduced |
| Median rates by state (pE 0.76, 0.69, 0.88 Hz; pI 5.59, 4.69, 4.25 Hz) | Partially reproduced |
| pE rates skewed, spanning 0.05 to 5 Hz | Partially reproduced |
| Fraction of pE cells above 2 Hz lower in nonREM | Not reproduced |
| nonREM against WAKE rates, slope below 1 | Reproduced |
| Burst index highest in nonREM, lowest in WAKE | Partially reproduced |
| Autocorrelogram peaks at 8 ms (nonREM) and 125 ms (REM, WAKE) | Partially reproduced |
| Pairwise correlations by rate group in nonREM | Partially reproduced |
| Microarousal duration, frequency and share of SLEEP | Not reproduced |
| MA fraction decreases over nonREM episodes | Partially reproduced |
| Median nonREM packet 111 s | Reproduced |
| About 2 WAKE-SLEEP cycles per session | Not reproduced |
| Population rate declines over SLEEP | Partially reproduced |
| Lower rate in the last than the first packet of SLEEP | Reproduced |
| First against last packet slope below 1 | Reproduced |
| Lower rates in WAKE after SLEEP, by sextile | Partially reproduced |
| Fastest sextile slows and slowest speeds up over SLEEP | Reproduced |
| CV of rates decreases over SLEEP | Not reproduced |
| Fastest sextile slows and slowest speeds up within nonREM | Reproduced |
| CV and burst index change within nonREM | Not reproduced (two claims) |
| Band power changes within nonREM | Not reproduced |
| Packet delta power grows with packet length | Reproduced |
| Packet rates against delta, gamma and sigma power | Partially reproduced |
| Rate changes across MA, WAKE and REM triplets (four claims) | Not reproduced |
| REM duration and packet-end sigma against rate changes | Not reproduced (two claims) |
| Slow sextile change against delta power change | Reproduced |
| Rate changes within WAKE and REM | Not reproduced |
| WAKE movement against rate change | Blocked: data missing |
| UP/DOWN states, spindles, autocorrelogram decay (six claims) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The state table in the files has no microarousal label, so microarousals are derived from short Awake
epochs between Non-REM epochs; the claims on state triplets depend on this. The notebook also shows
tests with one value per cycle, triplet or session, and every claim's main numbers without the
sessions whose state labels or LFP could not be checked against the spikes. The supplement, which
describes UP/DOWN state and spindle detection, could not be retrieved. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000041-watson-2016-01.yaml`](../../attempts/000041-watson-2016-01.yaml).

- `reproduce_watson_2016.ipynb`: the analysis. It takes about four minutes, two of them streaming the
  files with six processes.
- `sleepstates.py`: loading the files, the derived states (microarousals, packets, episodes, SLEEP
  periods and WAKE-SLEEP cycles), rates, burst index, autocorrelograms and LFP band power. Other
  notebooks on this dandiset can import it.
