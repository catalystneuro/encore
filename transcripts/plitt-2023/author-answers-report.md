No reader question was answered, because none was asked. No claim was re-run and no outcome changed.

**Questions:** none. `questions/001710.yaml` does not exist. My author run asked a reader nothing, and the answer run's report (`transcripts/001710/answer-report.md`) says it changed nothing for that reason. The four open questions in the attempt record are for the paper's authors, not a reader, so the answer run did not take them up. Since the author run, the only changed files are the answer run's two transcripts; the claims file is as it was.

**What changed per claim:** nothing. The claims file has no amendments, so there was nothing to re-run. I left the notebook, conclusions, attempt record and claim notes untouched, since there is no answer to describe in them. All 57 outcomes are the same as after the author run:

| Outcome | Count |
|---|---|
| reproduced | 31 |
| partially_reproduced | 4 |
| not_reproduced | 10 |
| blocked | 12 |

**Entry tooling:**
- **Lock:** `entry.py lock` rewrote `requirements.lock.txt` with the same pins, so git shows no change.
- **Check and run:** `entry.py all` passed with 0 errors. The notebook ran from a clean environment in 2141 s (about 36 min, up from 26.7 min last time). That is over the 10-minute aim and under the 60-minute limit.
- **Handover:** `entry.py handover` wrote the package to `executed/001710-plitt-2023/handover`.

I did not verify my own work, and nothing was committed or pushed.
