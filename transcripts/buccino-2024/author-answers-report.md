There were no answered questions, so nothing in the attempt changed.

**Questions.** `questions/000294.yaml` does not exist. The author run asked no reader anything, and the answer run's report (`transcripts/000294/answer-report.md`) says it found no questions and left `claims/000294/` unchanged. Git history agrees: the claims file was last changed in `3515158b1`, before the author run. So no claim was amended, and I did not touch the notebook, conclusions, claim notes or attempt record.

**Outcomes.** All 23 claims keep their earlier outcomes:
- **Reproduced (10):**
  - recordings-two-cells-runs
  - ecode-protocol-structure
  - holding-potential
  - extracellular-spikes-above-50uv
  - fig6-ais-from-dendrite
  - gt-rheobase
  - fig3b-ap-initiates-distal-ais
  - fig3a-largest-channel-at-ais
  - table1-feature-counts
- **Partially reproduced (1):** mea-electrodes-and-rates.
- **Blocked, `metadata_insufficient` (1):** culture-age.
- **Blocked, `too_large` (12):**
  - fig4a, gt-intracellular-scores, fig4c, both fig4b claims, fig4d, fig5
  - fig78a, experimental-intracellular-scores, fig78b, fig78c, fig10

**Entry runs.**
- `lock`: wrote `requirements.lock.txt` with no change from the committed file.
- `all`: 0 check errors, and the notebook ran from a clean environment in 510 s.
- `handover`: wrote `executed/000294-buccino-2024/handover`.

I didn't verify the work, and nothing is committed or pushed. The untracked files at the repository root (`.bashrc`, `scripts` and others) were there before this run, and I left them alone.
