There were no answered questions, so no claim was re-run and no outcome changed.

**Why there was nothing to answer**
- `questions/sohn-2019.yaml` does not exist, and nothing under `questions/` mentions sohn-2019 or DANDI:000130.
- In the earlier author run I asked readers no questions (`transcripts/sohn-2019/author-report.md`). My one open point was whether the behavioural regression `tp = beta ts + epsilon` has an intercept. I recorded it as a question for the paper's authors (a `methods_unavailable` finding), not a question for a reader, as step 1.6 of the Author section says.
- The reader's answer run found the same and changed nothing (`transcripts/sohn-2019/answer-report.md`). `claims/sohn-2019.yaml` is identical to the copy in the handover package.

**What I did**
- I did not change the notebooks, the conclusions or `attempts/sohn-2019-02.yaml`. With no amended claim there was nothing to re-run and no notes to update.
- `python tools/entry.py lock entries/sohn-2019` rewrote `requirements.lock.txt`, and the inputs hash stayed the same.
- `python tools/entry.py all entries/sohn-2019` found 0 errors, and both notebooks pass. It reused the executed copies from 08:22 UTC because nothing they read has changed (hash 1636c181a22a), so nothing was re-executed.
- `python tools/entry.py handover entries/sohn-2019` rebuilt `executed/sohn-2019/handover`.

**Outcomes, all the same as before**
- reproduced: beh-sigmoid-increments, beh-long-more-bias (rests on the intercept assumption), dfr-overlap-support, encoding-r2, short-in-long-control, alt-speed-unmodulated, alt-transient-parallel, gpfa-mean-sigmoid
- partially reproduced: beh-bayes-model, encoding-bayes-beats-linear, neural-long-more-bias, speed-vs-projection, speed-predicts-tp
- not reproduced: beh-slopes, beh-overlap-prior, glm-prior-ts, pca-dimensionality, initial-speed-biased, alt-threshold-monotonic, gpfa-variance-inverted-u
- blocked (data missing): rnn-curved-manifold, rnn-perturbation, monkey-g

I did not verify my own work, and nothing is committed or pushed.
