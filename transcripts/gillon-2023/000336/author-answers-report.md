There were no questions to process, so I changed no claims and no outcomes.

**Why there was nothing to re-run**
- `questions/000336.yaml` does not exist. The earlier author run asked a reader nothing, and the answer run's report (`transcripts/000336/answer-report.md`) says it had no questions and changed nothing.
- `claims/000336/` has not changed since the claims file was checked (last commit 1e5f70a07). No claim was amended, so the notebook, the conclusions and the record `attempts/000336-gillon-2023-01.yaml` didn't need updating, and I left them as they were.
- The two open method questions both go to the paper's authors, not a reader. One asks which similarity measure Fig. 7c rests on, the other which overlap measure and threshold the ROI matching used. They are still recorded as `methods_unavailable` findings.

**Outcome per claim (unchanged from the earlier run)**

| Claim | Earlier outcome | Now |
|---|---|---|
| dataset-holds-paper-sessions | not reproduced | same |
| table1-subjects, table2-sessions, session-schedule, roi-counts-per-session, tracked-rois-per-plane, fig8-example-matches, stimulus-durations, inconsistent-event-fraction, fig5-stimulus-responses, fig6-behaviour, fig7a-snr-high-stable, fig7b-signal-stable, fig9-onset-offset-transients | reproduced | same |
| fig8-ordering-variation | reproduced, rests on an assumption | same |
| imaging-planes | partially reproduced | same |
| fig7c-correlations-similar | blocked, `methods_underspecified` | same |
| high-correlation-pairs | not reproduced | same |

**Entry commands**
- `lock`: rewrote `requirements.lock.txt` with no change from the committed file.
- `all`: 0 errors. `reproduce_gillon_2023.ipynb` passed in 651 s and `roi_matching_orderings.ipynb` in 1222 s.
- `handover`: wrote `executed/000336-gillon-2023/handover`.

Nothing is committed and the tracked tree is clean. Some files I didn't create (`.bashrc`, `.mcp.json`, `.idea` and similar) are still untracked in the repository root and should not be committed.
