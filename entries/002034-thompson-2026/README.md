# Thompson & Gold (2026) from dandiset 002034

Tests the findings of [Thompson and Gold (2026)](https://doi.org/10.7554/elife.112525) on
[DANDI:002034](https://dandiarchive.org/dandiset/002034/0.261019.2146), which holds the 83 sessions
(32 for monkey Oz, 51 for monkey Ci) and 105 LC single units with pupil diameter that the paper
reanalyses.

| Claim | Outcome |
|---|---|
| The dandiset is the data of the paper's code, and the code's printed statistics can be recomputed (link) | Reproduced |
| 42 units in 32 sessions (Oz), 63 in 51 (Ci) | Reproduced |
| Baseline LC and baseline pupil correlate positively (Figure 2, row 1) | Reproduced |
| Evoked LC and evoked pupil correlate positively (row 2) | Reproduced |
| Evoked pupil falls with baseline pupil (row 3) | Reproduced |
| Evoked LC falls with baseline LC (row 4) | Reproduced |
| No relation of evoked pupil with baseline LC (row 5) | Reproduced |
| Baseline pupil and evoked LC: none in Oz, weak in Ci (row 6) | Reproduced |
| No reliable cross-epoch relation | Reproduced |
| Row 6 does not depend on the range of evoked LC | Reproduced |
| Row 5 depends on the range of evoked pupil in Oz only (rho = -0.33) | Not reproduced |
| Raw baselines give similar results (Supplemental Figure 1) | Partially reproduced |
| Few sessions favour a quadratic fit for pupil (7/32, 6/51) | Reproduced |
| Few units favour a quadratic fit for LC (2/42, 3/63) | Reproduced |
| Few units favour a quadratic fit across epochs (4/42, 4/63, 2/42, 5/63) | Not reproduced |
| Pooled within-epoch relations hold (Figure 3) | Reproduced |
| No pooled cross-epoch relation, also by unit group (Figure 3) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The deciding readings follow the Methods; the paper's code, run here as a variant, gives its own
printed numbers and the paper's for all three claims that do not reproduce in full. They differ
in how the evoked pupil is measured (to 20 ms before the end of fixation in the Methods, 0 to 800 ms
after the beep in the code) and which beep trials are kept. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/002034-thompson-2026-01.yaml`](../../attempts/002034-thompson-2026-01.yaml).
