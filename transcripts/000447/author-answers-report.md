Reader questions: none. `questions/000447.yaml` does not exist. My first author run asked a reader nothing; the questions I had left concern method details, so they went to the paper's authors as `methods_unavailable` findings. The answer run confirmed it had nothing to answer and changed nothing. The claims file has not changed since the claims check (commit 5c671eee9).

So no claim was amended, no claim was re-run, and each outcome stays as it was. I made no changes to the notebook, the conclusions or `attempts/000447-tang-2023-01.yaml`.

| Claims | Earlier outcome | Now |
|---|---|---|
| cells-per-session, fig2d, figs3a-ca1-global-remapping, figs3c, figs4d, figs5d, fig2f, figs3d, manifold-cell-counts, fig3fg, fig3h, fig3i | reproduced (fig2f and figs3d rest on assumptions) | unchanged |
| figs3a-pfc-similar-ca1-lower, fig2e-ca1-error-familiar, fig2e-pfc-error-stable, figs5e, fig3j, figs6, fig4d-pfc-ccgp, figs7d | partially reproduced | unchanged |
| fig1c-familiar-above-novel, figs4-ramping-fraction, fig3d, fig3e, fig4d-ca1-ccgp-chance, figs7b-geometric-null | not reproduced | unchanged |
| fig1b, fig1-denovo-final, fig1c-session, figs1b, figs4-ramping-generalization, figs5f | blocked | unchanged |

I ran the entry's steps so this run has a fresh handover:
- **Lock:** `tools/entry.py lock` wrote the same lock file as before, so nothing tracked changed.
- **Run and checks:** `tools/entry.py all` passed with 0 errors, and the notebook ran in 1332 s.
- **Handover:** `tools/entry.py handover` wrote `executed/000447-tang-2023/handover`.

I did not verify my own work, commit or push. An untracked `scripts` entry at the repository root is a sandbox `/dev/null` mount, like the untracked dotfiles. I left it alone, and it should not be committed.
