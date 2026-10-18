# Schwab, Kase, Zimnik, Rosenbaum, Codianni, Rubin & Turner (2020) from dandiset 000947

Tests the findings of [Schwab et al. (2020)](https://doi.org/10.1371/journal.pbio.3000829) on the
pre-MPTP recordings of [DANDI:000947](https://dandiarchive.org/dandiset/000947/0.240510.2211):
single units from the internal globus pallidus (GPi) and the ventrolateral anterior thalamus (VLa)
of two monkeys performing a reaching task.

| Claim | Outcome |
|---|---|
| The paper's units can be found in the dandiset and their activity reproduced | Reproduced |
| 209 GPi and 185 VLa units | Not reproduced |
| Rest rate GPi 70.1, VLa 13.5 spikes/s | Reproduced |
| Spike width GPi 0.24, VLa 0.50 ms | Reproduced |
| Hold-period ramps in 97% and 98% of units, no difference between areas | Partially reproduced |
| Nearly all units respond around movement | Reproduced |
| Monophasic increases are the most common response | Partially reproduced |
| Monophasic responses more common in VLa | Not reproduced |
| Integrated change positive in both areas | Partially reproduced |
| GPi changes begin later than VLa changes (Fig 3A) | Not reproduced |
| GPi decreases lag VLa increases (Fig 3B) | Reproduced |
| VLa decreases precede GPi increases (Fig 3C) | Not reproduced |
| 96% of response comparisons conflict with gating | Reproduced |
| GPi units more often directional than VLa units | Partially reproduced |
| GPi-VLa spike correlations no larger than controls (Fig 4A-F) | Not reproduced |
| GPi-VLa noise correlations no larger than controls (Fig 4G-H) | Not reproduced |
| VLa rate decreases after GPi bursts and pauses (Fig 5) | Not reproduced |
| Reaction times and movement durations (S2 Fig) | Partially reproduced |
| EMG onsets (S3 Fig) | Blocked: methods underspecified |
| Localization of VLa by stimulation (Fig 1) | Blocked: data missing |
| Simulations (Fig 6) | Blocked: other |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The units are selected from the dandiset's own labels, which gives more units than the paper
analysed; the paper's own unit list, from its Dryad deposit, is shown as a variant, and two
outcomes (monophasic responses, Fig 3A) would differ with it. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/000947-schwab-2020-01.yaml`](../../attempts/000947-schwab-2020-01.yaml).

- `reproduce_schwab_2020.ipynb`: the analysis. It takes about 12 minutes, about 3 of them streaming
  the files and another 3 reading the filtered traces for the spike widths.
- `gpivla.py`: loading the files, valid trials, spike density and ISI functions, the detection of
  peri-movement changes, CCFs with jittered controls, burst and pause detection, and spike widths.
  Other notebooks on this dandiset can import it.
