No reader answered any question for this attempt, so nothing changed. `questions/000138.yaml` doesn't exist. My first author run asked a reader nothing. The reader's answer run (`transcripts/000138/answer-report.md`) says the same and left the claims file unchanged. With no amended claims, there was nothing to re-run. I left the notebook, conclusions, attempt record and claim notes as they were.

The four questions from the first run are for the paper's authors, not a reader. They're recorded as `methods_unavailable` findings in `attempts/000138-churchland-2010-01.yaml`:
- whether the space was computed once or refit;
- how the proto-trial and its window were defined;
- the tuning measure and the movement-onset method;
- the Fig 7C upper limit.

**Questions answered and what changed:** none.

**Outcomes per claim (unchanged from the first author run):**

| Claim | Earlier outcome | Now |
|---|---|---|
| fig4abc-tuning-correlation-single-electrode | blocked, data_missing | same |
| fig4d-tuning-correlation-j-array | partially reproduced, assumed | same |
| fig4e-correlation-time-course | not reproduced | same |
| results-ap-location-no-effect | reproduced (J-array only), assumed | same |
| supp-preparatory-dimensionality | reproduced, assumed | same |
| fig6-peri-movement-space-best | reproduced | same |
| fig6-each-dimensionality | reproduced, assumed | same |
| fig6-dimensionality-trend | reproduced, assumed | same |
| fig6-pd-adequate-all-spaces | reproduced, assumed | same |
| fig6e-summary-rank | blocked, data_missing | same |
| fig7a-shuffled-space-poor | reproduced, assumed | same |
| fig7b-window-start-onset | reproduced (J-array only), assumed | same |
| fig7c-anterior-posterior | not reproduced, assumed | same |
| fig7d-pd-consistency | reproduced (J-array) | same |
| fig8-oscillator-model | reproduced (simulation) | same |

**Entry commands:**
- `lock` rewrote `requirements.lock.txt` with identical content.
- `all` found 0 check errors, and the notebook passed in 137 s.
- `handover` wrote `executed/000138-churchland-2010/handover`.

Nothing is committed or pushed. The working tree has untracked files I didn't create: the root dotfiles (`.bashrc`, `.gitconfig`, `.mcp.json` and others), `.idea`, `.vscode` and a `scripts/` directory. Someone should remove them before the next commit so they aren't committed by accident.
