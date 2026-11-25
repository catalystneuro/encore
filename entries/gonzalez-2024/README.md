# Gonzalez & Giocomo (2024) from dandiset 000405

Tests the findings of [Gonzalez and Giocomo (2024)](https://doi.org/10.7554/elife.85646) on
[DANDI:000405](https://dandiarchive.org/dandiset/000405/draft), which holds, for five rats, binned firing
rates, tracking and trial tables of 143 Tree-Maze sessions and binned rates and tracking of 133
open-field sessions. The dandiset has no published version, so the draft is read.

| Claim | Outcome |
|---|---|
| Median session accuracy 72.6% and 110 trials per session (Figure 1d) | Partially reproduced |
| Switch-trial accuracy 76.9%, 54 Switch trials, similar to non-Switch | Partially reproduced |
| 25 training sessions to criterion | Blocked: data missing |
| Cue U_Z follows left > stem > right (Figure 2c) | Reproduced |
| Cue remapping score below zero, mean -0.67 (Figure 2d) | Reproduced |
| Unit cue remapping relates to performance (Figure 2e) | Reproduced |
| Session mean cue remapping relates more strongly (Figure 2f) | Partially reproduced |
| Population cue remapping relates to performance (Figure 2g) | Reproduced |
| The relation holds within subjects (Figure 2h) | Reproduced |
| Cue remapping and behaviour, control analyses | Reproduced |
| Cue rate-remapping encoder best, R2 12% (Figure 3d) | Reproduced |
| Population decoders (Figure 3e to 3g, three claims) | Blocked: other (not run in this attempt) |
| Unrewarded trials have higher rates (Figure 4c) | Reproduced |
| Reward remapping score below zero, mean -1.03 (Figure 4d) | Reproduced |
| Reward remapping relates to performance (Figure 4e, 4f) | Partially reproduced |
| Population and subject reward remapping (Figure 4g, 4h) | Reproduced |
| Reward remapping and behaviour, control analyses | Reproduced |
| Reward rate-remapping encoder best (Figure 5) | Reproduced |
| Cue and reward remapping correlated | Reproduced |
| Incorrect coding overlaps between cue and reward | Reproduced (depends on the seed) |
| The error signal persists into the inbound run | Reproduced |
| Open-field aggregate model best (Figure 6c, 6d) | Reproduced |
| Unit matching (Figure 7b) | Blocked: data missing |
| Clustering and tuning scores of matched units (Figure 7d to 7f, two claims) | Blocked: other (not run in this attempt) |
| Matched head-direction units remap more (Figure 7g) | Blocked: other; partially reproduced proposed for a third verification round |
| Matched head-direction units have higher encoder scores (Figure 7h) | Blocked: other; partially reproduced proposed for a third verification round |
| The look-ahead encoder performs best | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold smoothed firing rates in 20 ms bins, with no spike times or waveforms, so units cannot
be matched across sessions; the paper's own match table names the dandiset's units, and Figure 7g and 7h are
tested on it. Twelve Tree-Maze sessions that the paper's repository lists are not in the
dandiset. The analyses are ports of the paper's code (github.com/alexgonzl/TMA at commit 6f93593) in
`tma.py`. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/gonzalez-2024-01.yaml`](../../attempts/gonzalez-2024-01.yaml).
