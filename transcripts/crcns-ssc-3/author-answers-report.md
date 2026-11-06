There were no answered questions, so nothing changed and no claim was re-run.

`questions/crcns-ssc-3.yaml` does not exist, and no other file under `questions/` covers this dataset. My first author run sent no questions to a reader. The answer run reported the same and changed nothing (`transcripts/crcns-ssc-3/answer-report.md`). The claims file was last changed by the claims check (84498fd33a), before my first author run, so every claim was already tested as the file has it now. The four open questions are for the paper's authors and stay recorded as `methods_unavailable` findings in the attempt record. They ask which bins form the transfer entropy's past state, whether Figs 4 and 5 used sub-networks or full networks and Pearson or Spearman, which 40 of the 50 correlations Fig 5 uses, and how the model's synergy was computed.

I did not edit the notebook, conclusions, attempt record or any claim's notes. With no answers, there was nothing for the notes to report.

Each outcome stays as it was:

| Claim | Earlier outcome | Now |
|---|---|---|
| data-recordings | reproduced | unchanged |
| fig4ac-te-lognormal | partially reproduced | unchanged |
| fig4bd-heavy-tailed-degree | reproduced | unchanged |
| fig4bd-out-tail-longer | reproduced (assumption) | unchanged |
| fig5a-in-degree-uncorrelated | partially reproduced (assumption) | unchanged |
| fig5b-out-degree-positive | reproduced (assumption) | unchanged |
| fig5ab-correlations-beyond-null | reproduced (assumption) | unchanged |
| fig5cd-pooled-trends | not reproduced | unchanged |
| fig6-information-gain-not-rising | reproduced | unchanged |
| table1-pid-examples | reproduced | unchanged |
| fig7b-connectivity-patterns | reproduced | unchanged |
| fig7c-degree-modified-rule-matches | partially reproduced (assumption) | unchanged |
| fig7d-degree-rule-highest-conditioned-mi | not reproduced | unchanged |
| figs1-larger-model | not reproduced | unchanged |

**Entry runs:**
- **`lock`:** rewrote `requirements.lock.txt` with no change to its contents.
- **`all`:** the check found 0 errors, and the notebook passed in 1814 s (30.2 min, limit 60).
- **Spot check:** the fresh run prints the same key numbers the conclusions quote: 7735 neurons, 2.10 Hz, R² 0.08 to 0.61, 41 of 50 and 44 of 50.
- **`handover`:** the package is in `executed/crcns-ssc-3-timme-2016/handover/`.

Nothing is committed or pushed, and there are no tracked changes.
