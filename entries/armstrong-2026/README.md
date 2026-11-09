# Armstrong & Vlasov (2026) from dandiset 001341

Tests the findings of [Armstrong and Vlasov (2026)](https://doi.org/10.1073/pnas.2514107123) on
[DANDI:001341](https://dandiarchive.org/dandiset/001341/0.260414.1316), version 0.260414.1316, the version the paper
cites. The dandiset holds two of the paper's 19 animals (489 and 503), with spike-sorted units, the trials table and
the ball tracking.

| Claim | Outcome |
|---|---|
| Recordings and counts of Table S1 | Not reproduced |
| Population rate of 489 about 2 Hz before the turn, then peak, suppression and ramp | Not reproduced (2 Hz part only) |
| Mice run at 21 ± 4 cm/s | Not reproduced |
| Animal 503 succeeds in 95% of turns | Not reproduced |
| Lateral positions confined at the turn start, widening after it | Not reproduced |
| DDM fit to reaction times (NDT 0.12 s; GDDM fits better) | Partially reproduced |
| 15 claims on spikes aligned to the turns | Blocked: metadata insufficient |
| 12 claims on whisker, touch, wall or gait data, or on animals not in the dandiset | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The spike times are not on the clock of the trials table, and the files hold no synchronisation signal: at the
stored turn onsets there is no trial-locked response. In 489 the onset lags suggest a drifting offset, but no
window's lag is separated from chance and no clock can be fitted. In 503 a clock fitted from running speed (spike
times about 12 s late, drifting by about 1.4 ms per s) recovers trial-locked responses, but only to about half a
second, too coarse for the timings the claims test; since 503 runs more in right turns than in left turns, these
responses may in part reflect running. The population rate of 489 before the turn is
6.65 to 7.80 Hz at any alignment, where the paper gives 2 Hz. The behaviour shares the trial clock, but the trials
table of 489 repeats one row for its last 611 rows, and some 60 turns per session have stop times before their
start times. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/armstrong-2026-01.yaml`](../../attempts/armstrong-2026-01.yaml).

- `reproduce_armstrong_2026.ipynb`: the analysis. It takes about six minutes, most of it streaming the files, the clock checks and
  fitting the drift diffusion models.
- `barrel_vr.py`: loading the files, the trial segments with the table's faults handled, lateral position and
  reaction times, the clock checks, and the PyDDM fits. Other notebooks on this dandiset can import it.
