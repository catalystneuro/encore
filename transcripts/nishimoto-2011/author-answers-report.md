I made no changes because there were no answered questions to act on.

**Why there was nothing to do**
- `questions/nishimoto-2011.yaml` doesn't exist. The answer run that came just before this one found the same thing (`transcripts/nishimoto-2011/answer-report.md`): it had nothing to answer and changed no files.
- The first author run asked a reader no questions (`transcripts/nishimoto-2011/author-report.md`, line 47). Its three "Question for the authors" items, at `attempts/nishimoto-2011-01.yaml:345-356`, are `methods_unavailable` findings for the paper's authors. They cover the temporal envelope and filter-bank frequencies, the boosting step, stopping rule, sigma and held-out folds, and the grating and plaid settings. None of them says the claims file misreads the paper.
- The claims file `claims/nishimoto-2011.yaml` has no amendments.

**Questions, changes and outcomes per claim:** none. Every outcome stays as the first author run recorded it:
- **reproduced (11):** fig3a-example-neuron, fig2b-contrast-normalization-no-effect, fig2b-compressive-divisive-best, fig2b-no-interaction, complex-cells-dominate, fig6a-null-on-plane, fig6a-excitatory-on-plane, fig6b-suppressive-off-plane, fig7a-partial-ring, fig7c-no-corr-prediction-pattern, fig8-recovery-simulated.
- **partially_reproduced (4):** fig2b-compressive-improves, fig2b-expansive-decreases, fig7a-no-corr-prediction-hv, natural-movie-control.
- **not_reproduced (4):** fig3b-mean-prediction (0.448 against 0.468 to 0.572), fig2b-divisive-improves, fig7b-pattern-index, fig7c-hv-pattern-correlation.
- **blocked (1):** fig3b-explainable-variance, as `data_missing` (the files hold only the response averaged over repeats).

**Entry steps**
- `python tools/entry.py check entries/nishimoto-2011` passed with 0 errors.
- I did not run `lock` or `run`/`all`. With nothing changed, `lock` could only pull newer package versions into the lock file. The entry's hash (`5c70a7a1…`) matches the hash of the clean run that finished this morning, so a rerun would take about 53 minutes to execute the same inputs again.
- `python tools/entry.py handover entries/nishimoto-2011` rebuilt `executed/nishimoto-2011/handover/`.

No tracked files changed, and nothing was committed or pushed.
