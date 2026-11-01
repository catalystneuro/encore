# Mehrotra, Levenstein et al. (2024) from dandiset 000987

Tests the findings of [Mehrotra, Levenstein et al. (2024)](https://doi.org/10.1016/j.cub.2024.05.048),
"Hyperpolarization-activated currents drive neuronal activation sequences in sleep", on
[DANDI:000987](https://dandiarchive.org/dandiset/000987/0.261003.2342), which holds the paper's
retrosplenial cortex (RSC) recordings, and, counted apart, on the paper's postsubiculum (PoSub)
recordings in [DANDI:000939](https://dandiarchive.org/dandiset/000939/0.261016.2310).

| Claim | Data | Outcome |
|---|---|---|
| The RSC dataset holds 570 units from 14 sessions in 3 mice | 000987 | Not reproduced (638 units) |
| In RSC, UP onset delay and PMR are negatively correlated (tau = -0.28) | 000987 | Reproduced, resting on an assumption |
| The same in PoSub (tau = -0.19) | 000939 | Reproduced, resting on an assumption |
| The first Isomap dimension of DU-PETHs tracks PMR (R = 0.88) | 000939 | Reproduced |
| UP onset delays range from 5 to 100 ms | 000939 | Reproduced |
| Dorsal PoSub units enter the UP state first | 000939 | Reproduced, resting on an assumption |
| Ventral DOWN states last longer | 000939 | Reproduced |
| HD, speed and AHV tuning do not vary along the DV axis | 000939 | Reproduced, resting on an assumption |
| Dorsal and ventral PoSub decode the same HD in sleep | 000939 | Reproduced |
| UP onset delays are more stable across halves than UD timing | 000939 | Blocked: methods underspecified |
| Delays are explained by position better than by firing rate | 000939 | Blocked: methods underspecified |
| High gamma travels at UP onset, synchronous at UD | 000939 | Not reproduced |
| Unit and LFP delay-depth correlations agree | 000939 | Blocked: methods underspecified |
| Spike and LFP traveling speeds are similar | 000939 | Not reproduced, resting on an assumption |
| The DOWN state resets HD; HD is stable at UP onset | 000939 | Blocked: not attempted in the run's time |
| ADN activates more synchronously than PoSub | ADN data | Blocked: metadata insufficient |
| The same PMR relation in rat frontal cortex | CRCNS fcx-1 | Blocked: not runnable |
| Model results (Figure 3) | model code | Blocked: not runnable (MATLAB) |
| Ex vivo sag gradient and no other gradients (Figure 4, S4) | ex vivo | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

The RSC dandiset holds 638 units where the paper and the dandiset description say 570 were recorded;
570 is the number that enters the Figure 5F test. Its files hold no LFP, waveforms or unit positions,
though the description lists LFP. In the PoSub dandiset, the DOWN and UP event file the paper's code
holds for one session does not fit that session's spikes, and the sleep scoring runs outside the
sleep epochs. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000987-mehrotra-2024-01.yaml`](../../attempts/000987-mehrotra-2024-01.yaml).

- `reproduce_mehrotra_2024.ipynb`: the two claims on dandiset 000987, and the checks behind two blocked
  claims on outside data. About two minutes.
- `posub_000939.ipynb`: the PoSub spike claims on dandiset 000939. About six minutes.
- `posub_lfp_000939.ipynb`: the PoSub LFP claims, streaming the LFP of the NREM epochs. About 14 minutes.
- `mehrotra.py`: loading of both dandisets and of the paper's event files, UP and DOWN detection, the
  PETH, PMR and onset delay of the paper's code, HD tuning measures, decoding and LFP high gamma. Other
  notebooks on these dandisets can import it.
