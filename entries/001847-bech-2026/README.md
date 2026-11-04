# Bech, Dard et al. (eLife) from dandiset 001847

Tests the findings of [Bech, Dard et al.](https://doi.org/10.7554/eLife.109717), "Retrosplenial cortex
enables context-dependent goal-directed sensorimotor transformation", on
[DANDI:001847](https://dandiarchive.org/dandiset/001847/0.260610.1400), which holds the behaviour,
orofacial tracking, optogenetic grid inactivation, muscimol and widefield imaging sessions of the paper.

| Claims | Outcome |
|---|---|
| The code's session lists match the dandiset (link) | Reproduced |
| 201 expert sessions in 41 mice by the Methods' rule | Not reproduced (the rule selects 318 in 49; the code's list matches) |
| Context modulation of licking, its independence of the noise, catch rates, Context Off, first-trial switch, further adaptation, temporal integration, block durations | Reproduced (9 claims) |
| Faster spout contact in W+ | Partially reproduced (tests match; means about 100 ms longer) |
| Pupil larger in W+; posture before lick | Reproduced (2 claims) |
| Jaw speed higher in W+ and before lick, whisking unchanged | Partially reproduced |
| Gradient-boosted model of the choice (Figure 1K-L) | Blocked, not run within the time limit (3 claims) |
| Optogenetic inactivation maps and latencies (Figure 2C-F, control mice) | Blocked, methods underspecified (7 claims; the nulls and thresholds disagree) |
| Muscimol in wS1 and RSC | Reproduced |
| Jaw onset 108 ms | Reproduced, resting on an assumption |
| Auditory activity similar across contexts, with an order of areas | Partially reproduced |
| Whisker activity diverges after 50 ms in RSC and wM1/2 | Reproduced |
| RSC first to discriminate contexts | Blocked, too large (pixel part) |
| GCaMP6f consistent, controls flat | Partially reproduced |
| RSC axon tracing | Blocked, data missing |
| Seed correlations (Figure 4A-B) | Blocked, too large (3 claims) |
| Inhibition effects on cortex, photoactivation control, angle predicts lick change | Reproduced (3 claims) |
| PC3 trajectories follow lick or no-lick | Not reproduced |
| Smaller angles for RSC and tjS1 | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files do not record the mouse lines or the session groups, so these come from the session lists
of the paper's processing code. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/001847-bech-2026-01.yaml`](../../attempts/001847-bech-2026-01.yaml).
`build_nb.py` regenerates the notebook from its cells.
