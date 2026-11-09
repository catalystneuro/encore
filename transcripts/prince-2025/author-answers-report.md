The one question is answered and its change is applied. The entry passes `check`, the notebook ran clean from a fresh environment in about 19 minutes, and the handover package is built in `executed/001371-prince-2025/handover/`. Nothing is committed or pushed, and I did not verify my own work.

## The question: fig2g-pfc-no-goal-increase (and every claim that uses S1)

**What the answer changed.** S1 used to count the encoder training trials for the rule that drops sessions with fewer than 50 trials, as the code does. The reader amended it to count the final-task trials of the session, as the Methods say ("less than 50 trials for the behavioral session"). The code's count stays as a named variant. No claim's statement, expected values or criterion changed.

**What I did:**
- **Helper:** in `prince2025.py`, `included()` and `trial_table()` now default to `rule="final"`, and the docstring cites the amended S1 and the Methods passage.
- **Notebook:** the Methods' count now decides everywhere, and the code's count is shown beside every test. That variant is new for tuning, validation, goal bias, the GLM claims, commitment and the theta claims.
- **Inclusion:** 55 CA1 and 46 PFC sessions are now included, against the paper's 56 and 47 (before: 47 and 37). CA1 now has 1241 switch and 871 delay only correct trials, against the paper's 1295 and 926.
- **Record:** I rewrote every affected claim's notes, `measured` values and S1 deviation, and each note says what the answer changed. I also updated the conclusions and the summary.

## Outcome per affected claim (now, with the earlier outcome after the arrow)

**One outcome changed:**
- **fig5d-stay-hpc-like-delay:** reproduced ← not reproduced. Stay against delay only gives p = 0.85 for the initial arm and p = 0.063 for the new arm; before, the new arm gave p = 0.032. The new arm is close to the 0.05 threshold.

**fig2g-pfc-no-goal-increase stays not reproduced.** On reading (a) the ANOVA gives p = 0.038 and the new-arm contrast p = 0.035. I judged it on reading (a) because the paper's degrees of freedom, F(3773.42), fit a model of switch and delay only trials (about 2 × 1907 rows); adding the stay trials would give about 4780. Reading (b) alone would pass, with no p below 0.05 (smallest 0.066). The switch Wilcoxon moved from p = 0.029 to p = 0.080. Your question's "why" pointed at reading (b), so this judgement is the one point a verifier should look at.

**No other outcome changed:**

| Claim | Outcome |
|---|---|
| tuning-tiles-track | reproduced |
| decoding-validation | reproduced |
| fig2e-hpc-goal-increase | reproduced |
| fig2e-hpc-arms-equal | reproduced |
| sfig2e-goal-bias | reproduced |
| sfig3c-goals-over-retrospective | not reproduced |
| sfig3c-retrospective-unchanged | reproduced |
| sfig3ab-original-vs-update-cue | partially reproduced |
| sfig2f-all-trials-encoder | partially reproduced |
| sfig5f-pfc-wider-spread | partially reproduced |
| sfig5g-ca1-more-goal-coding | reproduced |
| sfig5e-pfc-windows | not reproduced |
| fig3c-theta-phase-segregation | not reproduced |
| fig3b-theta-pre-post | reproduced |
| sfig6-theta-switch-over-delay | reproduced |
| fig3d-new-arm-theta-modulated | reproduced |
| fig5d-stay-hpc-below-switch | partially reproduced |
| sfig10-stay-transient-new-arm | reproduced |
| fig6b-hpc-new-lower-incorrect | reproduced |
| fig6b-hpc-initial-no-difference | reproduced |
| fig6-hpc-pre-cue-initial-higher-incorrect | reproduced |
| sfig12-delay-hpc-no-outcome-difference | not reproduced |
| fig7c-hpc-commitment-new-arm | partially reproduced |
| fig7c-hpc-commitment-initial-arm | not reproduced |

Small changes within those claims:
- **sfig10-stay-transient-new-arm:** the delay only new-arm value (0.100) is now within tolerance.
- **sfig5f-pfc-wider-spread:** 42 sessions enter, up from 36.

**Unaffected:** the behaviour claims don't use S1. The 19 LSTM and choice-decoding claims stay blocked as `too_large`; I updated the fig4a timing note to this run's estimate of 12.4 h.

The `code_mismatch` finding now notes that the code's count would change one outcome, fig5d-stay-hpc-like-delay.
