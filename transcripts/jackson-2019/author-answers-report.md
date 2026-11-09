There were no questions to answer, so no claim was re-run and no outcome changed.

**Questions:** none. `questions/openneuro-ds002778.yaml` doesn't exist and git history shows it never has. The author run asked a reader no questions. The answer run (`transcripts/openneuro-ds002778/answer-report.md`) found nothing to answer and changed nothing. The claims file, notebook, conclusions and attempt record are the same as at the author commit, so I left them alone. There were no claim notes to update.

The one open point from the author run is the alpha PAC phase filter length (192 taps adopted). It is still recorded as a `methods_unavailable` finding with `table1-alpha-pac-null` marked `assumed: true`. Under the protocol it is not a reader question.

**Outcomes:** all 25 claims stay as they were (earlier outcome = current outcome):
- **Reproduced:**
  - bipolar-off-on, temporalis-f7f8-null, temporalis-t7t8-null
  - offctrl-sharpness-null, offctrl-pac-null
  - updrs-improvement
  - table1-alpha-pac-null (resting on the assumption above)
  - fig4a-sensorimotor-q4, controls-q4, fig4b-temporalis-variable-shape
- **Partially reproduced:**
  - fig2-sharpness-off-on, fig2-steepness-off-on, fig2-pac-off-on
  - fig2c-topography-sensorimotor
  - offctrl-steepness
  - table1-alpha-shape-off-on, table2-alpha-offctrl
  - pac-beta-larger-than-alpha
  - fig3-sharpness-pac-correlation, fig3-steepness-pac-correlation
  - table3-q4-effect-size
- **Not reproduced:** offctrl-pac-csd, fig1c-beta-alpha-peaks, q4-patient-counts

**Entry checks:**
- `lock` rewrote `requirements.lock.txt`, and `git diff` shows it is unchanged.
- `all` reported 0 errors, and the notebook passed in 95 s.
- `handover` wrote the package to `executed/openneuro-ds002778-jackson-2019/handover/`.

Nothing was committed or pushed. `git status` lists untracked `scripts` and dotfiles at the repository root. `scripts` is a character device (`1, 3`, i.e. `/dev/null`), so these are sandbox mounts, not files from this run.
