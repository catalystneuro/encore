# The International Brain Laboratory (2021) from dandiset 000045

Tests the findings of [The International Brain Laboratory (2021)](https://doi.org/10.7554/eLife.63711),
"Standardized and reproducible measurement of decision-making in mice", on
[DANDI:000045](https://dandiarchive.org/dandiset/000045/0.211209.1413), which holds the trial tables
of 178 mice trained in seven laboratories between 2019-06-11 and 2020-03-23. The paper's mice began
training in January 2019, so 136 mice of the paper's project have their whole training in the
dandiset, against 206 in the paper.

| Outcome | Claims |
|---|---|
| Reproduced | 17, and the link claim that matches the labs |
| Partially reproduced | 10 |
| Not reproduced | 8 |
| Blocked: the readings disagree (methods underspecified) | 2 |
| Blocked: the Random Forest cannot run in the time limit (not runnable) | 1 |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files carry no training status, so basic and full task proficiency are recomputed from the
trials with the paper's criteria, as the claims file gives them after the questions this attempt
asked were answered (`questions/000045.yaml`). The per-claim outcomes, the reasons and the differences from the
paper's method are in the attempt record,
[`attempts/000045-ibl-2021-01.yaml`](../../attempts/000045-ibl-2021-01.yaml).

- `reproduce_ibl_2021.ipynb`: the analysis. It streams every file (about six minutes) and runs in
  about twenty-five minutes.
- `ibl_behavior.py`: loading the files, the proficiency criteria, the psychometric fit (with the
  paper's `psychofit`), the lab tests and classifiers, the choice model and the history analysis.
  Other notebooks on this dandiset can import it.
