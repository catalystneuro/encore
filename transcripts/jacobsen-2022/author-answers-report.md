There were no answered questions on this paper, so nothing changed: no claim was re-run and the notebook, conclusions and attempt record are as the first run left them.

**Why there were no questions.** `questions/jacobsen-2022.yaml` doesn't exist in the working tree or anywhere in git history, and no file under `questions/` mentions jacobsen-2022 or DANDI:000230. The first run's report says "Questions to a reader: none." (`transcripts/jacobsen-2022/author-report.md:44`). The reader's answer run found the same and changed nothing (`transcripts/jacobsen-2022/answer-report.md`). The claims file has no edits since the author run.

The three questions in `attempts/jacobsen-2022-01.yaml` (lines 300 to 310) are for the paper's authors, not a reader, and none has been answered:
- the head direction score of 0.81 that Figure S4 gives T4 C16;
- the two laser epochs in the day-17 session of mouse 58313;
- how the Rowland et al. (2018) classification should be read.

**Outcome per claim.** Every claim keeps its earlier outcome. For example, `fig5c-functional-cell-types` stays reproduced, resting on the assumption about how the shuffle should be read.

**Entry commands:**
- `lock` rebuilt `requirements.lock.txt` and added `python: "3.13"` to `entry.yaml`. The schema rejects that field, so `check` failed with one error. As in the first run, I deleted the line.
- `all` then passed with 0 errors. The tool did not run the notebook again: it reused the copy executed at 03:24 UTC, because nothing the notebook reads had changed.
- `handover` rewrote `executed/jacobsen-2022/handover`.
- After these steps, `git status` shows no tracked changes under `entries/`, `claims/` or `attempts/`.

The bug that keeps coming back is in the repository's tools: `tools/entry.py lock` writes a `python` field that the entry schema doesn't allow. It will fail every entry's check until someone fixes the tool or the schema. I didn't verify my own work, and nothing is committed or pushed.
