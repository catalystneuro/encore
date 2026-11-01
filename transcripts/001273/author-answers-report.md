I found no questions to answer, so I changed nothing in the claims, notebooks, conclusions or attempt record.

**Why:** `questions/001273.yaml` does not exist. The author run said it asked a reader nothing (`transcripts/001273/author-report.md`, line 1). The reader's answer run found nothing to answer and left the claims file alone (`transcripts/001273/answer-report.md`). The claims file `claims/001273/10.1016-j.xcrp.2025.102660.yaml` has had no commits since before the author run. The one open method question (ROI size and placement, how the fits were weighted, whether the discharge amplitude was free, and which 19 experiments were used) is for the paper's authors. It stays recorded as a `methods_unavailable` finding.

**Questions:** none, so no claim was re-run. Every outcome is the same as after the author run:

| Claim | Outcome (unchanged) |
|---|---|
| fig4-polarized-poles-face-electrodes | reproduced |
| fig4-no-pole-difference | reproduced |
| fig4-pooled-time-constants | not reproduced |
| fig4-orientation-time-constants, fig4-discharging-slower, fig4-full-charge-within-3us | blocked: metadata_insufficient |
| fig3c-sustained-firing-2s (DANDI:001030) | partially reproduced |
| figs1-di8-anepps-control (DANDI:001272) | not reproduced |
| fig1, fig2, fig2c, fig2d, fig3b, figs2 | blocked: other |
| fig5, fig6, threshold-depolarization-estimate | blocked: too_large |

**Entry:** The verifier's package from the author run was not in this checkout, so I locked, checked, ran and handed over the entry again:
- `lock` rewrote `requirements.lock.txt`, and the file is the same as before.
- `all` reported 0 errors, and all three notebooks passed: `reproduce_semenov_2025.ipynb` in 850 s, `elsewhere_001030.ipynb` in 24 s and `elsewhere_001272.ipynb` in 48 s.
- `handover` wrote `executed/001273-semenov-2025/handover`.

I did not compare the new run's outputs with the attempt record, since the verifier checks that. Nothing is committed or pushed.

If questions were meant to be asked for this attempt, they never reached the branch, and this run would need to be repeated once they are answered.
