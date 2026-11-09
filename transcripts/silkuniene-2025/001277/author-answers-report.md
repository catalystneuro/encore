There were no questions to answer for DANDI:001277, so no outcome changed.

**Questions**
- `questions/001277.yaml` does not exist on this branch or in git history. The reader's answer run (`transcripts/001277/answer-report.md`) found nothing to answer and changed no files.
- My first author run asked a reader nothing. The open questions I had were for the paper's authors: which 600-ns wells were used, how far apart the ROIs were, and how the Fig. 6D trend was fitted. These are recorded as a `methods_unavailable` finding.
- The claims file is the same as when I tested it. The only commit since my author run adds the reader's transcript.

**Notebook, conclusions and attempt record:** I left them unchanged, because no claim was amended.

**Entry run**
- `lock`: the requirements lock file came out identical.
- `all`: check reports 0 errors, and the notebook runs from a clean environment (791 s).
- I spot-checked the executed copy against the conclusions: ANOVA p = 0.54 for Fig. 6B, trend p between 0.002 and 0.004 for the Fig. 6D slope with contiguous ROIs, and FWHM at 900 ns of 1.69 to 1.71 mm. They still match.
- `handover`: built in `executed/001277-silkuniene-2025/handover/`.

**Outcomes per claim** (the earlier outcome is unchanged in every case)

| Claim | Earlier outcome | Now |
|---|---|---|
| fig6b-peak-900ns-not-significant | reproduced (assumed) | unchanged |
| fig6c-normalized-decline-similar | not_reproduced | unchanged |
| fig6d-longer-pulses-sharper-peak | blocked, methods_underspecified | unchanged |
| fig6d-600-900-differ-from-300 | blocked, methods_underspecified | unchanged |
| fig6d-900ns-fwhm | blocked, methods_underspecified | unchanged |
| fig5-yp-lorentzian-pr-gaussian | not_reproduced (assumed) | unchanged |
| fig5-yp-spot-slightly-larger-than-pr | not_reproduced (assumed) | unchanged |
| 10 claims on Figs. 2, 3, 4B, 4C, 5 (raised electrodes) and 7 | blocked, data_missing | unchanged |

I did not verify my own work, and nothing is committed or pushed.
