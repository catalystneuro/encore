# Hernández-Pérez, Cooper & Newman (2020) from CRCNS hc-27

Tests the findings of [Hernández-Pérez et al. (2020)](https://doi.org/10.7554/elife.52289) that
can be tested on [CRCNS hc-27](https://doi.org/10.6080/K0C53J2R), which holds the LFP of the six
rats' key recordings, 5 or 6 channels each along the dorsal-ventral axis of the medial entorhinal
cortex, at 500 Hz. The laminar array of Figure 3 and the multi-unit recordings of Figure 4 are not
in it.

| Claim | Outcome |
|---|---|
| Theta phase shifts at 26.36 deg/mm, ventral sites lagging | Reproduced |
| The shift is linear with distance (r2 = 0.76) | Reproduced |
| The shift is seen in all six rats | Reproduced |
| Median phase locking between sites is 0.90 | Reproduced (assumed) |
| Phase locking falls with distance, -0.067 per mm | Reproduced (assumed) |
| Theta coherence is 0.73 | Reproduced |
| Coherence falls with distance, 0.067 per mm | Not reproduced |
| Theta power does not change along the axis | Reproduced |
| Phase shifts run along, not across, the layers (Figure 3) | Blocked: data missing |
| Multi-unit activity forms a traveling wave (Figure 4, two claims) | Blocked: data missing |
| Rise/decay asymmetry, -0.43 dorsal against -0.11 ventral | Partially reproduced |
| Peak/trough asymmetry, 0.21 dorsal against -0.10 ventral | Reproduced |
| Dorsal theta is sawtooth-shaped | Reproduced |
| About 2.8 mm down, rise still shorter, peak and trough no longer differ | Reproduced |
| Conduction delay shortest for the falling phase, longest for the peak | Partially reproduced |
| Delay rises with reference phase, 0.02 (ms/mm)/deg, R2 = 0.82 | Partially reproduced (assumed) |
| Phase-specific shifts bracket the Hilbert shift | Reproduced (assumed) |
| Delay due to asymmetry, 3.56 ms/mm | Not reproduced (assumed) |
| Residual delay of 9.61 ms/mm after removing asymmetry | Not reproduced |
| Relative delay does not change with theta frequency | Not reproduced (assumed) |
| Absolute delay falls with theta frequency, -3.12 ms/Hz | Not reproduced (assumed) |
| Absolute delay varies more with frequency than relative delay | Not reproduced (assumed) |
| The residual shifts behave as coupled oscillators | Partially reproduced (assumed) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files state no unit, and two of the six are on a scale about five times smaller than the
others, so the paper's 400 µV theta threshold selects nothing in them as stored. "Assumed" marks
outcomes that rest on applying the threshold on one scale for all rats (400 µV only if the
integer files are in µV), and, for Figure 8, on the claims file's definition of a cycle's period,
which shares timing with the per-cycle delay. The notebook shows a threshold sweep and Figure 8
variants that do not share that timing. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/hernandez-perez-2020-01.yaml`](../../attempts/hernandez-perez-2020-01.yaml).
