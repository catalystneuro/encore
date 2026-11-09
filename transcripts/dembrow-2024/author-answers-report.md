No reader answered any question, so I changed no claim, notebook, conclusion or attempt record.

**Questions:** none. `questions/001065.yaml` does not exist on this branch. The author run asked nothing, because it found no misreading in the claims file. The answer run (`transcripts/001065/answer-report.md`) found no questions and changed nothing. The claims file has not changed since the author run (commit 8120f61d5). The three method details that run could not settle are still recorded as `methods_unavailable` findings for the paper's authors: whether the classifier splits were stratified, how the Figure 7 oscillations were computed, and which sweeps the features use. They were not questions for a reader.

**Effect on claims:** no claim changed, so every outcome is the same as in the earlier run:
- 21 reproduced
- 7 partially reproduced
- 7 not reproduced
- 7 blocked (their data is held elsewhere: SRA, NeMO and the Brain Image Library)

**Entry commands:**
- `lock`: wrote `requirements.lock.txt` again with no change.
- `all`: the check found 0 errors, and `reproduce_dembrow_2024.ipynb` passed in 668 s.
- `handover`: wrote `executed/001065-dembrow-2024/handover`.

I did not verify my own work, and I did not commit or push. The edit to `tools/build_site.py` was already there when I started, and I left it alone.
