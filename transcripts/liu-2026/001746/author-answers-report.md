There were no questions to answer, so nothing in the attempt changed.

**Questions.** `questions/001746.yaml` doesn't exist on this branch or in the history of any branch. My earlier author run asked a reader nothing (`transcripts/001746/author-report.md`: "Questions asked of a reader: none"). The answer run (`bc87717bae`) found nothing to answer and didn't change the claims file. Since no claim was amended, I didn't re-run any claims or edit the notebook, the conclusions, the claim notes or `attempts/001746-liu-2026-01.yaml`.

**Outcomes per claim.** Every outcome is the same as before.

**Entry.** I ran the commands as asked:
- `python tools/entry.py lock` rewrote the lock file with the same contents, so there is no diff.
- `python tools/entry.py all` reported 0 errors, and the notebook passed in 246 s (last time it took about 166 s).
- `python tools/entry.py handover` built `executed/001746-liu-2026/handover/`.

The working tree has no tracked changes. Nothing was committed or pushed.

**Still open.** Three questions for the paper's authors were already recorded as `methods_unavailable` findings in the attempt record. They are method details, not questions for a reader, so they remain open:
- Which measure "deeper sag" uses.
- How the 19 undefined features of the per-cell feature table are computed.
- How the phase peaks were placed by hand.
