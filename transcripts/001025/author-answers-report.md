There were no questions to act on, so I changed nothing in this run.

**Why:** `questions/001025.yaml` does not exist. It is not in the working tree, at HEAD, or anywhere in the git history. The answer run before this one (`transcripts/001025/answer-report.md`) found the same thing and changed nothing. The claims file `claims/001025/10.1016-j.bioelechem.2023.108437.yaml` has not changed since my first author run. The two open methods questions in the attempt record (whether a background was subtracted, and how the ROIs were laid out and the pixel size) are for the paper's authors. They were never put to a reader, so nobody answered them.

**Per claim:** no claim was amended, so none was re-run for an answer. Every outcome is the same as before:

| Claim | Earlier outcome | Now |
|---|---|---|
| fig4-unipolar-strongest, fig4-bipolar-cancellation | blocked (data_missing) | unchanged |
| fig5a, fig5bc, fig6a, fig6b, fig8a, fig8b, fig9, fig9c | blocked (other: the data are in dandisets 000686, 000875, 001027 and 001028) | unchanged |
| fig7a-amplitude-scales-uptake | not_reproduced (ratios 5.99, 5.65 and 7.25) | unchanged |
| fig7b-targeting-independent-of-amplitude | not_reproduced, assumed (1 of 20 pairs differs, p = 0.0037) | unchanged |
| fig7cd-holds-for-large-array | not_reproduced, assumed (centre p = 0.0494) | unchanged |
| discussion-independent-of-array-size | not_reproduced, assumed | unchanged |

I didn't edit the notebook, the conclusions or the attempt record, and I added no claim notes, since no answer changed anything.

**Entry:**
- **Lock:** the lock file was regenerated with no change.
- **Check:** 0 errors.
- **Run:** the notebook passed in a clean environment in 545 s. The executed outputs give the same values as the record, for example ratios of 5.99, 5.65 and 7.25 for fig7a and p = 0.0494 / 0.1594 for fig7cd.
- **Handover:** written to `executed/001025-pakhomov-2023/handover`.

I did not verify my own work, and nothing is committed or pushed. If questions for 001025 were meant to be asked, someone needs to add the questions file and run the answer step before this step can do anything.
