There were no questions to act on, so I changed nothing in the entry, the notebook or the attempt record.

**Questions and answers**
- `questions/sohn-2019.yaml` does not exist. My earlier author run raised no questions to a reader (`transcripts/sohn-2019/author-report.md` says "Questions to a reader: none").
- The reader's answer run found the same thing (`transcripts/sohn-2019/answer-report.md`) and did not edit the claims file.
- `claims/sohn-2019.yaml` has no amendments and no `checks` entries recording a change.
- The one open method issue went to the paper's authors as a `methods_unavailable` finding, not to a reader. It asks about the regression intercept, rate normalisation before PCA, and the number of GPFA EM iterations. Those questions stay open.

**What each answer changed:** nothing, since there were no answers. I re-ran no claims and edited no claim notes.

**Outcomes, all the same as before** (from `attempts/sohn-2019-02.yaml`):

| Claim | Now | Before |
|---|---|---|
| beh-slopes | not_reproduced | not_reproduced |
| beh-overlap-prior | not_reproduced | not_reproduced |
| beh-sigmoid-increments | reproduced | reproduced |
| beh-long-more-bias | reproduced | reproduced |
| beh-bayes-model | partially_reproduced | partially_reproduced |
| glm-prior-ts | not_reproduced | not_reproduced |
| dfr-overlap-support | reproduced | reproduced |
| pca-dimensionality | not_reproduced | not_reproduced |
| encoding-r2 | reproduced | reproduced |
| encoding-bayes-beats-linear | not_reproduced | not_reproduced |
| short-in-long-control | reproduced | reproduced |
| neural-long-more-bias | reproduced | reproduced |
| speed-vs-projection | partially_reproduced | partially_reproduced |
| initial-speed-biased | reproduced | reproduced |
| speed-predicts-tp | partially_reproduced | partially_reproduced |
| alt-speed-unmodulated | reproduced | reproduced |
| alt-transient-parallel | reproduced | reproduced |
| alt-threshold-monotonic | not_reproduced | not_reproduced |
| gpfa-variance-inverted-u | not_reproduced | not_reproduced |
| gpfa-mean-sigmoid | reproduced | reproduced |
| rnn-curved-manifold | blocked (data_missing) | blocked (data_missing) |
| rnn-perturbation | blocked (data_missing) | blocked (data_missing) |
| monkey-g | blocked (data_missing) | blocked (data_missing) |

**Entry commands**
- `python tools/entry.py lock entries/sohn-2019` rewrote `requirements.lock.txt` with the same contents as before, and `entry.yaml` is also unchanged.
- `python tools/entry.py all entries/sohn-2019`: the check found 0 errors, and the notebook passed. Since nothing the run reads had changed, it reused the executed copy from 2026-11-14 14:07 UTC (727 s) and executed nothing.
- `python tools/entry.py handover entries/sohn-2019` wrote `executed/sohn-2019/handover/`.

I did not verify the work, and nothing is committed or pushed.
