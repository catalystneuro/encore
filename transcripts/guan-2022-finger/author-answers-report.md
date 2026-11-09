No reader answered any question for DANDI:000252, so no claim changed and every outcome stays as it was.

**Questions.** `questions/000252.yaml` doesn't exist, and git history shows it never did. My earlier author run raised no reader questions because I found no misreading in the claims file. The reader's answer run (`transcripts/000252/answer-report.md`) also found no questions and made no changes. The claims file hasn't changed since the author run, so I didn't touch the notebook, the conclusions, the attempt record (`attempts/000252-guan-2022-01.yaml`) or any claim's notes.

**Outcomes per claim (unchanged):**

| Claim | Earlier outcome | Now |
|---|---|---|
| tenfinger-recording-counts | reproduced | reproduced |
| tenfinger-pooled-npcc-neurons | reproduced | reproduced |
| tenfinger-discriminative-fraction | not reproduced | not reproduced |
| tenfinger-decoding-accuracy | reproduced | reproduced |
| tenfinger-error-structure | reproduced | reproduced |
| fig8b-matching-closer | reproduced, resting on an assumption | same |
| fig8a-npcc-index-distinct | reproduced | reproduced |
| fig8e-hand-ccgp | reproduced | reproduced |
| fig8e-finger-ccgp | reproduced | reproduced |
| jppc-finger-ccgp-low | partially reproduced, resting on an assumption | same |
| figs11-jppc-lower-matched-size | reproduced | reproduced |
| fig4c, fig4e, fig5a, fig5bcd, fig5e | blocked, data_missing | same |
| fig6-online-bmi, figs6, figs7 | blocked, data_missing | same |

**Entry checks:**
- **Lock:** `python tools/entry.py lock` rewrote `requirements.lock.txt` with no change to its contents.
- **Checks and run:** `python tools/entry.py all` passed with 0 errors. The notebook ran in 416 seconds, from 12:39 to 12:46 UTC.
- **Handover:** `python tools/entry.py handover` wrote the package to `executed/000252-guan-2022/handover`.
- **Repository:** no tracked file changed. The untracked dotfiles and the `scripts` folder in the repository root were there before this run, and I left them alone.

I didn't verify the work, commit or push.
