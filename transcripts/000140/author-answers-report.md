There were no questions to act on, so I changed nothing in the notebook, the conclusions, the attempt record or any claim's notes.

**Why there are no questions**
- `questions/000140.yaml` does not exist, and git history shows it never has. The answer run's report (`transcripts/000140/answer-report.md`) says the same and that it made no changes.
- My earlier author run asked readers nothing. Its three open points are method details the paper leaves out: the >5 spikes/s inclusion rule, how the proto-trial was chosen along with how movement onset was detected, and the details of the task spaces. Those are questions for the paper's authors. They are recorded as `methods_unavailable` findings in the attempt, and the protocol sends that kind of question to the authors, not a reader.
- Nothing in `claims/`, `questions/`, `attempts/` or the entry has changed since the author run's commit (72bb5edc7), so no claim needed re-running.

**Outcomes** are unchanged from the earlier run:

| Claim | Earlier outcome | Now |
|---|---|---|
| fig4d-mean-correlation-j-array | not reproduced | unchanged |
| fig4abc-mean-correlation-other-datasets | blocked: data_missing | unchanged |
| fig4-broad-near-zero | partially reproduced (assumed) | unchanged |
| fig4e-correlation-time-course | reproduced (assumed) | unchanged |
| suppfig1-population-averages-lose-tuning | reproduced | unchanged |
| fig6d-perimovement-best-j-array | reproduced (assumed) | unchanged |
| fig6abc-perimovement-best-other-datasets | blocked: data_missing | unchanged |
| fig6-perimovement-best-each-dimensionality | not reproduced | unchanged |
| fig6-maze-endpoint-speed-space-poor | not reproduced (assumed) | unchanged |
| fig6-dimensionality-trend | not reproduced (assumed) | unchanged |
| fig6e-summary-rank | blocked: data_missing | unchanged |
| prep-dimensionality-7-to-10 | not reproduced | unchanged |
| fig7a-shuffled-space-poor | reproduced | unchanged |
| fig7b-window-start-slide | not reproduced | unchanged |
| ap-location-no-effect-j-array | reproduced (assumed) | unchanged |
| ap-location-no-effect-other-datasets | blocked: data_missing | unchanged |
| fig7c-anterior-posterior-performance | not reproduced (assumed) | unchanged |
| prep-activity-more-anterior | not reproduced (assumed) | unchanged |
| fig7d-pd-consistency | not reproduced | unchanged |
| fig8-linear-dynamics-simulation | reproduced | unchanged |

**Checks**
- `lock` rewrote `requirements.lock.txt` with identical contents.
- `all` reported 0 errors, and the notebook ran successfully in 72 s.
- `handover` wrote `executed/000140-churchland-2010/handover`.

I did not verify my own work, and I committed and pushed nothing.

If reader questions were meant to be part of this run, they were never committed. They would need to be added and answered before an answers run has anything to do.
