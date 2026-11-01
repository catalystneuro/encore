Nothing changed in this run: no reader answered any question on DANDI:000946, because none was asked.

- **No questions file.** `questions/000946.yaml` does not exist. The reader's answer run (`transcripts/000946/answer-report.md`) found the same thing and changed nothing. The first author run's report says it asked no questions. Its one open point, how the normalized spiking rate is computed, was put to the paper's own authors as a `methods_unavailable` finding.
- **The claims file is unchanged.** The last commit to `claims/000946/` (ae36cfe63, "Claims for DANDI:000946, checked") came before the author run. So no claim was amended, and there was nothing to re-run.
- **No edits.** I did not change any claim's notes, the notebook, the conclusions or the attempt record (`attempts/000946-gao-2025-01.yaml`).

| Question | What its answer changed | Affected claims | Outcome now (earlier) |
|---|---|---|---|
| none | – | – | – |

All 33 outcomes stay as recorded: fig11b-ac-responses is partially reproduced and rests on the normalization assumption. The other 32 claims are blocked: 30 because the dataset has no cell types, sham or CG1 sessions, and 2 because they depend on blocked claims.

**Checks and run**
- `python tools/entry.py lock entries/000946-gao-2025` rewrote the lock file with no difference.
- `python tools/entry.py all entries/000946-gao-2025` reported 0 errors, and the notebook passed in 267 s from a clean environment.
- I read the Fig. 11B cell in the executed copy and its numbers are the ones in the record:
  - 633 AC units against the paper's 453.
  - During sonication the set above baseline is 1500, 3000 and 4500 Hz; after sonication it is 30, 1500, 3000 and 4500 Hz.
  - 300 Hz is the lowest in both windows, and both Kruskal-Wallis tests are significant.
- `python tools/entry.py handover entries/000946-gao-2025` built `executed/000946-gao-2025/handover/`.

I did not verify my own work, and nothing is committed or pushed.
