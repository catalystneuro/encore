Nothing changed in this run, because there were no answered questions to act on.

**Questions.** `questions/peron-2020.yaml` doesn't exist, and git history on every branch shows it never has. The first author run asked a reader nothing; its report says "Questions to a reader: none". The reader's `answer` run (`transcripts/peron-2020/answer-report.md`) also found no questions and left `claims/peron-2020.yaml` untouched. The two open points from the first run are questions for the paper's authors, not for a reader: which proximity rule is meant, and how touches are merged into bursts at 50 ms. They stay recorded as `methods_unavailable` findings.

**What changed per claim.** Nothing. No claim was amended, so none was re-run, and the notebook, conclusions and attempt record are as the first run left them. Every outcome is the same as before:
- **Reproduced (19):**
  - one marked as resting on an assumption: per-mouse-table
  - the other 18: neurons-per-mouse, representation-sizes, touch-ablation-size, touch-ablation-reduces-touch, touch-ablation-touch-count, touch-ablation-whisking-unchanged, ablation-size-correlation, distance-dependence-touch, distance-dependence-whisking-absent, whisking-ablation-size, whisking-ablation-no-effect-touch, whisking-ablation-no-effect-whisking, silent-ablation-size, silent-ablation-no-effect-touch, silent-ablation-no-effect-whisking, ablation-type-specificity, response-similarity-whisking-ablation, ablation-no-off-target-event-rate, ablation-success-rate
- **Not reproduced (3):** behaviour-unchanged, response-similarity-touch-ablation, response-similarity-example
- **Blocked (8):**
  - the seven model claims (`other`: the network model was never built in the first run)
  - glial-reaction-local (`data_missing`: the histology is not in the data set)

**Entry steps.**
- `lock`: the lock file came out unchanged.
- `all`: the check found 0 errors and the notebook passed. Because nothing it reads had changed, it reused the executed copy from 20:55 UTC and executed nothing.
- `handover`: wrote the verifier's files to `executed/peron-2020/handover/`.

I committed nothing.

I didn't start on the seven blocked model claims in the time left. This run is for re-running claims a reader's answers changed, and none were changed. A later attempt can take them up; the first run estimated about 2.2 hours of compute for them on one core.
