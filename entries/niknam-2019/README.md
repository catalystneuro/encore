# Niknam et al. (2019) from CRCNS mt-3

Tests the findings of [Niknam et al. (2019)](https://doi.org/10.1371/journal.pcbi.1007275) on
[CRCNS mt-3](https://doi.org/10.6080/K0FB514J), the spike trains, probe sequences and saccade
times of the paper's 41 MT neurons. The RF, FF and ST probes come from the paper's code
repository (https://github.com/nnategh/SFA-Models at commit 1438dde).

| Claim | Outcome |
|---|---|
| The code's RF, FF and ST probes link to the neurons | Reproduced |
| 41 neurons, 11 sessions, 27 leftward and 14 rightward | Reproduced |
| Saccadic suppression in 8 neurons (Figure 1B) | Reproduced |
| FF-remapping in 23 neurons (Figure 1C) | Not reproduced |
| ST-remapping in 37 neurons (Figure 1D) | Not reproduced |
| Both remapping effects in 22 neurons (Figure 1E) | Not reproduced |
| Remapped responses come later than RF responses | Reproduced |
| Example neurons of Figure 1 | Partially reproduced |
| N-model comparison (Figure 5A) | Blocked: methods underspecified |
| S-, F- and A-model claims (Figures 3, 5 to 8, S4, S5; 24 claims) | Blocked: too large |
| RF centres in degrees (Figure S1) | Blocked: metadata insufficient |

The remapping counts depend on what the paper's signed-rank test pairs, which the Methods do not
say; whether the claims file should include a pairing over time bins is asked of a reader in
[`questions/niknam-2019.yaml`](../../questions/niknam-2019.yaml).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/niknam-2019-01.yaml`](../../attempts/niknam-2019-01.yaml).
