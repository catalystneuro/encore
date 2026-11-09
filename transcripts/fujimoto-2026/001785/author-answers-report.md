## Report: DANDI:001785, Fujimoto et al. 2026 (author-answers run)

**Result: there were no questions to act on, so no claim was re-run and no outcome changed.**

- **No questions file.** `questions/001785.yaml` does not exist. My earlier author run asked a reader nothing; its report says "Questions to a reader: none". The answer run (`transcripts/001785/answer-report.md`) found the same thing and changed nothing in the claims file.
- **No changes.** Because nothing was answered, I left the claims file, notebook, conclusions and attempt record (`attempts/001785-fujimoto-2026-01.yaml`) as they were. No claim's notes needed a line about what an answer changed.
- **Outcomes (unchanged from the earlier run):**
  - 26 claims reproduced, including the three link claims.
  - link-if-counts partially reproduced.
  - 2 claims not reproduced: ed1-sham-no-behavior-change and ed6a-dacc-cb-no-change.
  - 7 claims blocked: fig3f as not_runnable, and the six that need the connectomes or the voxel-wise control-group test as data_missing.
  - ed6b-uf-fm-no-change and fig6c-sham-cc1-no-change still rest on the assumed 10-pixel smallest object.
- **The one open question is for the paper's authors, not a reader.** It asks how cells were counted in FIJI (threshold method, size filter, watershed). It is recorded as a `methods_unavailable` finding in the attempt record.
- **Entry checks.**
  - `entry.py lock` rewrote `requirements.lock.txt` with no change.
  - `entry.py all` gave 0 errors, and the notebook passed in 222 s.
  - `entry.py handover` built `executed/001785-fujimoto-2026/handover`.
- **Unrelated changes.** `tools/build_site.py` and `tools/site_assets/app.css` were already modified when the run started, and I did not touch them.

Nothing was verified by me, committed or pushed.
