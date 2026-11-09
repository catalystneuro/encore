There were no reader questions to act on, so I didn't change any claim, the notebook, the conclusions or the attempt record.

**Why there's nothing to re-run**
- `questions/001260.yaml` doesn't exist. The reader's answer run (`transcripts/001260/answer-report.md`) found the same: no reader questions were ever filed for this dataset, on this branch, on `main` or in git history.
- The three open questions in `attempts/001260-le-merre-2026-01.yaml` are `methods_unavailable` findings meant for the paper's authors, not a reader. None says the claims file misreads the paper. They cover:
  - how to number the spontaneous categories on a retrained SOM (this blocks 8 claims);
  - which test supports "not significantly different across behavioral settings";
  - which recordings have a block structure.
  
  Since the reader can't settle these, they stay as filed.
- The claims file hasn't changed since the author run. The only commit since then adds the reader's transcripts.
- So no claim is affected. Every outcome stays as the earlier author run recorded it, including the 8 claims blocked on the category numbering.

**Entry commands**
- `lock`: the lock file came out the same as before.
- `all`: 0 check errors, and the notebook ran in 585 s from a clean environment (`pass reproduce_le_merre_2026.ipynb`). I didn't compare its outputs with the recorded outcomes, since checking my own work is the verifier's job.
- `handover`: written to `executed/001260-le-merre-2026/handover/`.

There are untracked files in the repository root (`.bashrc`, `.profile`, `.gitconfig`, `.mcp.json`, `.idea`, `.vscode`, `scripts` and others), plus uncommitted edits to `tools/build_site.py` and `tools/site_assets/progress.js`. None of them are mine. The earlier author run flagged the untracked files too, and I left them all alone. They should be checked before anything is committed. I didn't commit or push.
