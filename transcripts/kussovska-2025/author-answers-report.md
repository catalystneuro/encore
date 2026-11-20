Nobody asked or answered any questions for this attempt, so I changed nothing in the claims, notebook, conclusions or attempt record.

- **No questions file.** `questions/kussovska-2025.yaml` does not exist. My earlier author run asked a reader no questions: its four open points are for the paper's authors and are recorded as `methods_unavailable` findings. The `answer` run found the same and changed nothing (`transcripts/kussovska-2025/answer-report.md`).
- **No amendments.** `claims/kussovska-2025.yaml`, the entry and `attempts/kussovska-2025-01.yaml` have not changed since the author run (commit cf0b0e48f2). No claim was amended, so none needed re-running and no claim's notes needed updating.

**Outcomes per claim.** All stay as the author run left them: 27 reproduced, 9 partially reproduced, 6 not reproduced, 3 blocked (`too_large`, the dPCA claims fig3abc, fig3d and fig3h). The per-claim table in `transcripts/kussovska-2025/author-report.md` still applies.

**Entry checks:**
- `lock`: rewrote `requirements.lock.txt` with no changes.
- `all`: 0 errors, and the notebook passed in 2297 s (about 38 min, against 19.6 min last time).
- `handover`: wrote `executed/kussovska-2025/handover`.

I did not commit or push.
