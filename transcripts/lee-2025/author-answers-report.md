There were no questions to act on, so no claim was re-run and the notebook, conclusions and attempt record are unchanged.

- **No questions file:** `questions/001195.yaml` doesn't exist on this branch, on `origin/attempt/001195`, or anywhere in the git history.
- **No questions filed:** the first author run filed none for a reader (`transcripts/001195/author-report.md:44`, "Questions to a reader: none"). Its open points went to the paper's authors as `methods_unavailable` findings instead.
- **Nothing to answer:** the answer run reported the same (`transcripts/001195/answer-report.md`).
- **Claims file unamended:** `claims/001195/10.7554-elife.105955.yaml` was last changed in bfd71527c ("Claims for DANDI:001195, checked"), before the author run.

**Questions and what they changed:** none.

**Outcomes:** every claim keeps the outcome from the first author run, as listed in `transcripts/001195/author-report.md`. For example, fig6df is reproduced (with different cell counts), fig6k is not reproduced, fig6pq is partially reproduced, fig6-s1de is blocked (`metadata_insufficient`), and the in vivo and Figs. 1–5 and 8 claims are blocked (`data_missing`).

**Entry checks:**
- `lock`: the lock file came out unchanged.
- `all`: 0 errors, and `reproduce_lee_2025.ipynb` passes from a clean environment in 707 s.
- `handover`: the package is in `executed/001195-lee-2025/handover`.
- `git status` shows no changes under `entries/`, `attempts/`, `claims/` or `questions/`. I didn't commit or push.

If questions were meant to be filed for this dataset, that step didn't happen. A reader would need to file and answer them, and then the `author-answers` run would need to run again.
