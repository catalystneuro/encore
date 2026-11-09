No questions were asked or answered, so this run changed nothing in the entry, the attempt record or the claims file.

- **Questions:** `questions/001425.yaml` does not exist. The author run recorded "Questions to a reader: none" (`transcripts/001425/author-report.md`, line 49). Its open points went into the record as two `methods_unavailable` findings, which are questions for the paper's authors, not for a reader. The reader's `answer` run found nothing to answer and left the claims file as it was. That file was last changed in commit `ed2f3b9b91`, before the author run.
- **What the answers changed:** nothing. No claim was amended, so I re-ran no claims and changed no notebook, conclusion, record or claim notes.
- **Outcome per claim** (earlier outcome → now), all unchanged:
  - **Reproduced → reproduced (15):**
    - cohort-sex-age
    - task-sessions-collected
    - imaging-frame-counts
    - training-breaks
    - fig3c-response-rate-increase
    - fig3d-tpull-clusters
    - fig3e-cluster-a-high-tpull
    - fig3e-cluster-b-similar-rates
    - methods-no-signal-degradation
    - fig4d-visual-map
    - fig4d-tactile-map
    - fig4d-auditory-map
    - figs2b-no-aberrant-transients
    - fig5f-lever-tip-correlation
    - fig6b-motor-somatosensory-after-reward
    - fig6b-variability-decrease
  - **Partially reproduced → partially reproduced (1):** fig5f-forepaw-correlation.
  - **Blocked → blocked (6):**
    - fig3c-success-rate-constant (`methods_underspecified`)
    - fig4ab-landmark-validation (`data_missing`)
    - fig5abc-dlc-error (`data_missing`)
    - fig6b-movement-order (`methods_underspecified`)
    - fig6b-sensory-areas-track-pupil (`methods_underspecified`)
- **Entry checks:**
  - `lock` rewrote the lock file with identical content.
  - `all` gave 0 errors, and the notebook ran from a clean environment in 1353 s.
  - Spot-checks of the executed copy found the numbers in the record, including 0.556 and 0.856, 0.981, 0.482, the 7 and 18 clusters, the Spearman rho of 0.257 and the 0.436 prominence.
  - `handover` built `executed/001425-kondo-2025/handover/`.
- I did not verify my own work, and nothing is committed or pushed.

If questions were meant to come from a verifier, there aren't any yet. An `author-answers` run would only have something to do after a verifier adds questions to `questions/001425.yaml` and a reader answers them.
