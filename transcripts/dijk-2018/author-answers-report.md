There were no questions to answer, so no claim was re-run and no outcome changed.

**What I found**
- `questions/dijk-2018.yaml` does not exist, and git history has no file under `questions/dijk*`.
- The earlier author run's report says "Questions to a reader: none". The gaps it found (field definition and map smoothing, which session pairs form the manipulations, the Ipos location size, the 5-s episodes, the test that classes correlated pairs) are recorded as three `methods_unavailable` findings, which are questions for the paper's authors. Under Author step 1.6 those are not put to a reader.
- The reader's answer run (`transcripts/dijk-2018/answer-report.md`) found the same: no questions, so the claims file was not amended.

**What I did**
- I made no edits. The claims file, notebook, conclusions and `attempts/dijk-2018-01.yaml` are as the author run left them, and every outcome is unchanged.
- I did not run `lock` or `all`. With no changes, they would only have re-executed the notebook for the same result.
- `python tools/entry.py check entries/dijk-2018` passed with 0 errors.
- `python tools/entry.py handover entries/dijk-2018` ran and wrote `executed/dijk-2018/handover` from the executed notebook already there.
- I did not verify my own work, and nothing was committed or pushed.

`tools/entry.py` and `tools/notify.py` were already modified when this run started. I left them as they were.

**Questions and outcomes per claim:** none answered, so there is nothing to compare.

If questions were meant to be filed for this attempt, someone has to add them to `questions/dijk-2018.yaml` and get a reader to answer them before an author-answers run can act on them.
