There were no questions to answer, so nothing changed. Every claim keeps the outcome from the earlier author run.

**The questions file is missing.** `questions/crcns-hc-11.yaml` does not exist. The answer run's report (`transcripts/crcns-hc-11/answer-report.md`) says there were no questions and it changed nothing. The earlier author run asked a reader nothing; its eight open points are for the paper's authors and sit in one `methods_unavailable` finding. The claims file, `claims/crcns-hc-11/10.1126-science.aad1935.yaml`, was last changed by the claims-check run, before the author run.

**Effect on claims.** No claim was amended, so I re-ran nothing as a changed claim. I did not edit the notebook, the conclusions, the attempt record (`attempts/crcns-hc-11-grosmark-2016-01.yaml`) or any claim's notes.

Outcomes, unchanged from the earlier run:

| Outcome | Count | Claims |
|---|---|---|
| Reproduced | 12 | fig1c, figs5b, figs5e, figs5f, fig2-pre-contributors-persist, fig2d, figs12, figs2, figs13, figs16ab, low-high-rate-split, fig4c, fig2e |
| Partially reproduced | 9 | place-cell-count, figs9b, fig2b, fig3a, figs16c, fig4d, fig4e, figs16de, figs17 |
| Not reproduced | 9 | rigid-plastic-counts, fig3b, fig4a, figs14 gain, figs14 bursting, figs17d, figs18, figs19c |
| Blocked (`other`) | 1 | figs11-cluster-quality-similar |

The reproduced row lists 13 names for a count of 12; fig2e is the extra one.

**Entry commands:**
- `lock`: the lock file came out the same.
- `all`: `check` gave 0 errors and the notebook passed in 1,974 s (about 33 minutes), against the 60-minute limit. The analysis is seeded, so this run should give the same values as the recorded one. I did not compare the outputs, since checking my own work is the verifier's job.
- `handover`: it wrote `executed/crcns-hc-11-grosmark-2016/handover`.

Nothing is committed or pushed. The working tree has no changes apart from the sandbox dotfiles that were there before the run.
