I changed nothing in the attempt, because no reader answered any question on DANDI:001474.

**Why there was nothing to answer**
- `questions/001474.yaml` does not exist, and no branch's git history has a version of it.
- My author run asked a reader nothing.
- The reader's answer run (`transcripts/001474/answer-report.md`) found no questions and made no change.
- The claims file has not changed since it was checked (last commit `012d95173`).

The attempt does raise three questions, but they are for the paper's authors, not a reader, and are recorded as `methods_unavailable` findings in the attempt record:
1. How was the Z-score computed?
2. How was the Supp. Fig. 1d lick AUC normalized?
3. Which recordings enter Supp. Fig. 3l–q?

A reader's answer cannot settle these, so they stay open.

**Answers and their effect:** none. No question was answered, so no claim was re-run, and the notebook, conclusions, attempt record and claim notes are as the author run left them. Every claim keeps its earlier outcome:

| Outcome | Count |
|---|---|
| Reproduced | 24 |
| Partially reproduced | 6 |
| Not reproduced | 5 |
| Blocked | 2 (supp1cd: `methods_underspecified`; supp2q: `data_missing`) |
| **Total** | **37** |

**Entry commands**
- `lock`: rewrote `requirements.lock.txt` with no change.
- `all`: 0 errors, and the notebook ran clean in 109 s.
- `handover`: wrote `executed/001474-porniece-2025/handover`.

I did not verify my own work, and nothing is committed or pushed.
