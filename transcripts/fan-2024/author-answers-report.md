There were no questions, so nothing changed. `questions/000959.yaml` does not exist on this branch, and no commit on any branch has ever contained it.

- **Why no questions:** in my earlier author run I asked a reader nothing. My report says "Questions to a reader: none." The reader's answer run found nothing to answer and changed nothing (`transcripts/000959/answer-report.md`).
- **The claims file is the same:** `claims/000959/` has had no commits since my author run, so no claim's statement, expected values or criterion was amended.
- **The open questions are for the paper's authors:** the three in the attempt record (whether a face event on the trial sample counts as a look back with latency 0, which reference M2's reciprocation latency is measured from, and which side the bootstrap p-value takes) stay recorded as `methods_unavailable` findings. None of them says the claims file misreads the paper.

So I re-ran no claims and edited nothing: not the notebook, the conclusions, any claim's notes, nor `attempts/000959-fan-2024-01.yaml`. Each claim keeps its earlier outcome:

| Claims | Outcome (unchanged) |
|---|---|
| 19 claims | reproduced |
| design-sessions-per-day, methods-ofc-longer-face-looking, partner-monkey-unchanged, and one more | partially reproduced |
| figs1e-eyes-vs-rdm-comparable, methods-eyes-vs-mouth-bootstrap, fig5a-trigger-duration-unchanged, and two more | not reproduced |
| figs4a, figs4b, ofc-slope, fig4c, fig4d, dmpfc-slope-positive | blocked, `too_large` |
| fig5cd, fig5e-h (saccades) | blocked, `not_runnable` |

That is 28 of 33 claims tested; my earlier author report lists the full per-claim table.

**Entry checks:**
- `lock`: the lock file was rewritten with no change.
- `all`: 0 errors, and the notebook passes in 652 s.
- `handover`: written to `executed/000959-fan-2024/handover/`.

`git status` shows no changes under `entries/`, `attempts/`, `claims/` or `questions/`. Nothing is committed or pushed.

If questions were meant to exist for this attempt, someone needs to supply them before an `author-answers` run has anything to act on.
