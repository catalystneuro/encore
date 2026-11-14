There were no questions to answer, so I changed nothing in the attempt.

`questions/andrews-2024.yaml` does not exist in the working tree, on `main`, or anywhere in git history. The first author run asked readers nothing (`transcripts/andrews-2024/author-report.md:24`), and the answer run found no questions (`transcripts/andrews-2024/answer-report.md`). `claims/andrews-2024.yaml` has not changed since that author run, so no claim's statement, expected values or criterion differs from what I tested before.

**Per question:** none, so no claim was re-run. The outcomes are the same as before:
- `table1-cohort`: partially_reproduced.
- The other 28 claims: blocked, mostly `data_missing`. `simulation-dampening` is blocked as `not_runnable`.

I left the notebook, the conclusions and `attempts/andrews-2024-01.yaml` unchanged, because there was nothing to say in a claim's notes about an answer.

**Entry commands:**
- `lock`: the lock file is unchanged.
- `all`: 0 check errors, and `reproduce_andrews_2024.ipynb` passed in 839 s.
- `handover`: written to `executed/andrews-2024/handover/`.

Nothing is committed or pushed. `tools/entry.py` already had changes when I started, and I did not touch it. The untracked dotfiles and `scripts/` in `git status` are not mine either.
