# Garud & Morris (2026) on dandiset 001552 and the Krausz et al. (2023) table

Tests the findings of [Garud and Morris (2026)](https://doi.org/10.64898/2026.04.07.716149), a
preprint that reuses two published datasets. Figure 4 uses
[DANDI:001552](https://dandiarchive.org/dandiset/001552/0.250828.1728) (Floeder et al. 2025),
dLight photometry in head-fixed mice in short-ITI and long-ITI Pavlovian sessions. Figures 2, 3
and 5 use the Krausz et al. (2023) hex-level table on
[Mendeley Data](https://doi.org/10.17632/m59zdjpm9h.1); those claims are counted apart from the
dandiset.

| Claim | Outcome |
|---|---|
| 18 mice with 16 to 24 sessions in both ITI conditions | Reproduced |
| Higher anticipatory lick rate in short-ITI sessions | Reproduced |
| Late-ITI dopamine below baseline in long-ITI sessions; short-ITI response unresolved | Partially reproduced |
| Tonic dip deepens over training (r = -0.29, p < 0.001) | Partially reproduced |
| Lick rate rises over training (r = 0.65) | Reproduced |
| Krausz selection keeps 264,042 observations | Reproduced (outside data) |
| Ramp toward the goal, steeper for high reward, similar early and late, larger when fast | Reproduced (outside data) |
| Velocity covaries with distance; coupling grows near the goal (r = -0.494) | Reproduced (outside data) |
| Stationary dopamine dips below zero (t = -4.27) | Reproduced, resting on an assumption (outside data) |
| Recovered value increases toward the goal in 8 of 10 rats | Partially reproduced, resting on an assumption (outside data) |
| Gaussian value shape wins in 8 rats, all shapes R² above 0.8 | Partially reproduced (outside data) |
| Gaussian CT TD model best, 8 of 10 rats; tonic and Gaussian ΔBIC 1156 and 706 | Reproduced (outside data) |
| No velocity coupling without a spatial goal (Supplementary Figure S2) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset's photometry series state a wrong sampling rate in part of the sessions and start
on a clock of their own; the notebook aligns them to the event log through the TTL2 channel,
which steps at each cue. Two sessions are deposited twice and are counted once. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/garud-2026-01.yaml`](../../attempts/garud-2026-01.yaml).

- `reproduce_garud_2026.ipynb`: the analysis. It takes about five minutes, most of it streaming
  the 358 session files.
- `ctd.py`: loading the files and aligning their clocks, ΔF/F, the tonic and lick measures, and
  the Krausz selection, value recovery and model fits. Other notebooks on this dandiset can
  import it.
