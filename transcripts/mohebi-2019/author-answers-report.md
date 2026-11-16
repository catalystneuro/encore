No reader answered any questions, so no claim changed and I re-ran nothing as a result.

**Questions:** none. `questions/mohebi-2019.yaml` doesn't exist on this branch, and the earlier author run asked a reader nothing ("Questions to a reader: none" in `transcripts/mohebi-2019/author-report.md`). The answer run reported the same and left `claims/mohebi-2019.yaml` unchanged. Comparing with the author commit (cc9cccb7fb) shows no change to `claims/`, `attempts/` or `entries/`.

The open points from the first run went to the paper's authors as `methods_unavailable` findings, not to a reader. They are still recorded as assumptions:
- the per-cell tonic-firing test for Fig. 2f,h;
- the time window for cue responses;
- the pause measure for Extended Data Fig. 8.

**Outcomes per claim:** all the same as before, since no claim changed:
- **Reproduced (8):** fig1b, fig2d, ed5a, fig2i-burst, fig2i-no-inactive, fig4a-no-ramp, fig5a-positive-rpe, and fig5ab-weak-negative-rpe (which rests on an assumption).
- **Partially reproduced (6):** fig2-tagged, ed5 clicks, ed5 cues, fig4ac (rests on an assumption), fig4e, ed8.
- **Not reproduced (3):** fig2efgh (rests on an assumption), retro-tagged (rests on an assumption), fig5a-early-trial.
- **Blocked (20):** `data_missing`.

**Entry runs:**
- **Lock:** left `requirements.lock.txt` the same as before.
- **Check and run:** `entry.py all` reported 0 errors and the notebook passed in 226 s.
- **Handover:** written to `executed/mohebi-2019/handover`.

I didn't edit the notebook, conclusions, attempt record or claim notes, because there was no answer to record in them. Nothing is committed or pushed.
