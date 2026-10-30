# Athalye, Khanna, Gowda, Orsborn, Costa & Carmena (2023) from dandiset 000404

Tests the findings of [Athalye et al. (2023)](https://doi.org/10.1016/j.cub.2023.06.027) that can be
tested on [DANDI:000404](https://dandiarchive.org/dandiset/000404/0.230605.2024), which holds the
binned spike counts, decoder state, cursor and trials of 9 sessions of Monkey G and 4 of Monkey J
performing a center-out and an obstacle-avoidance task with a 2D cursor BMI.

| Claim | Outcome |
|---|---|
| Conditions per session (16 to 17 on average) | Reproduced |
| Conditions per command (about 7) | Reproduced |
| Command subtrajectories differ between conditions (Figure S1D) | Reproduced |
| Next commands differ between conditions (Figure S1E) | Partially reproduced |
| Population activity for a command differs between conditions (Figure 3D) | Reproduced |
| Single-neuron activity for a command differs between conditions (Figure 3B) | Reproduced |
| Fractions of tuples, commands and neurons that differ (Figure 3E) | Partially reproduced |
| Dynamics predict activity given the command, and generalize (Figure 4C) | Reproduced (assumption) |
| Dynamics predict condition-specific activity (Figure 4D, E) | Reproduced |
| Dynamics predict the condition-specific component (Figure 4F) | Partially reproduced |
| Most tuples, commands and neurons predicted (Figure 4G) | Reproduced |
| Low-dimensional decaying dynamics (Figure S3) | Not reproduced |
| Dynamics predict next activity (Figure 5C) | Partially reproduced (assumption) |
| About 4 dimensions predicted (Figure 5D) | Reproduced |
| Dynamics predict the next command (Figure 5E) | Partially reproduced (assumption) |
| Condition-specific next command predicted (Figure 5F) | Partially reproduced |
| Direction and angle of the turn predicted (Figure 5H) | Partially reproduced |
| Dynamics add to behavior-encoding models (Figure S5B) | Reproduced |
| rsLDS no better than linear dynamics (Figure S5F) | Blocked: too large |
| Residual larger early in the trial (Figure S3F) | Reproduced |
| Generalization to left-out command sets (Figure S4B) | Reproduced (assumption) |
| Generalization to left-out classes of conditions (Figure S4G) | Partially reproduced (assumption) |
| Pairwise distances predicted (Figure S6C, D) | Reproduced |
| Neural distance tracks behavior distance (Figure S6G) | Reproduced |
| Pairwise next-command distances predicted (Figure S6K) | Reproduced |
| Fitted dynamics reduce the input in an OFC model (Figure 6C) | Reproduced (assumption) |
| Decoder-null dynamics give no saving (Figure 6D) | Reproduced (assumption) |
| OFC with dynamics uses distinct patterns for a command (Figure 6G) | Partially reproduced (assumption) |
| Monkey J's command is linear in activity (Methods) | Not reproduced (assumption) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files hold no decoder matrices, although the paper says they were deposited. The decoder gain
is recovered from the decoder state and the spike counts by least squares: exactly for Monkey G's
Kalman filter, and as the paper's own linear approximation for Monkey J's point process filter.
Monkey J's target and obstacle series carry one value for a whole session, so the targets are read
from the cursor at reward. Monkey J's obstacle trial types are matched to the target list of the
paper's code (`resim_ppf/jeev_obs_positions_from_amy.mat` at commit 4161873), an outside input.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000404-athalye-2023-01.yaml`](../../attempts/000404-athalye-2023-01.yaml).

- `reproduce_athalye_2023.ipynb`: the analysis of the recorded data. It takes about 15 minutes on 4
  cores, most of it the 1000 behavior-preserving shuffles of the dynamics models.
- `ofc_simulations.ipynb`: the optimal feedback control simulations of Figure 6, about 6 minutes.
- `bmi.py`: loading the files, recovering the decoder, binning, conditions, command bins, the
  matching of the condition-pooled distribution, ridge regression and the shuffle.
- `analyses.py`: the per-session analyses (distances and their nulls, dynamics models and their
  left-out and shuffle versions, behavior-encoding models, pairs of conditions).
- `ofc.py`: the decoders' 100 ms cursor update, the finite-horizon LQR and the simulations.
