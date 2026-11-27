There were no questions to answer, so nothing in the claims file, notebook, conclusions or attempt record changed. All 33 outcomes are the same as before.

- **No questions file.** `questions/mah-2023.yaml` does not exist. The first author run asked a reader nothing: its open points were method details for the paper's authors, and it recorded them as `methods_unavailable` findings in `attempts/mah-2023-01.yaml`. The answer run (`transcripts/mah-2023/answer-report.md`) found nothing to answer and changed no file.
- **Claims file unchanged.** `claims/mah-2023.yaml` has not changed since the author run (commit a3a7df4d2c), so no claim needed re-running.

**Outcomes, all unchanged from the first author run:**

| claims | outcome |
|---|---|
| cohort-size, fig1e, fig1f, fig1i, suppfig2, suppfig3, fig2a, suppfig5, suppfig6, fig2c-d, fig2e, fig2f, fig2g-h, fig2j, fig2k, fig2l, fig3c, bayes-observer, suppfig12, suppfig14, fig5b, fig5c, fig5d | reproduced |
| fig3i | partially reproduced, rests on an assumption |
| pre-cue-session-link (the link claim the author added) | partially reproduced, 14 of 16 rats |
| fig3j, suppfig8, fig3f, suppfig9, fig3l | blocked, `too_large` |
| fig4a, fig4c, fig4d | blocked, `data_missing` |

**Entry:**
- `lock`: rewrote `requirements.lock.txt` for Python 3.13, with no change to the tracked file.
- `all`: 0 check errors, and the notebook passed from a clean environment in 804 s.
- I spot-checked the executed copy for the numbers the conclusions rest on. It still prints 291 rats, a median of 33,493 trials, p = 1.82e-49 for Fig. 1i and 14 of 16 rats linked.
- `handover`: wrote `executed/mah-2023/handover/`.

I did not verify the attempt and did not commit or push. An untracked `scripts` directory sits at the top of the checkout; I didn't create it and left it alone.
