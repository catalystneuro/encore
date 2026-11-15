I had no questions to process, so nothing in the attempt changed.

`questions/sohn-2019.yaml` doesn't exist, and there is no `questions/000130.yaml` either. No other file in `questions/` mentions sohn-2019. The reader's answer run says the same in `transcripts/sohn-2019/answer-report.md`: it found no questions and made no change to `claims/sohn-2019.yaml`. That fits my earlier run, which asked readers nothing. Its one open point, whether the tp-on-ts regression has an intercept, I recorded as a `methods_unavailable` finding for the paper's authors, not as a reader question.

So no claim was re-run. The notebooks, the conclusions and `attempts/sohn-2019-02.yaml` are as they were, and every claim keeps its earlier outcome. Of the 20 tested, 7 are reproduced (beh-long-more-bias rests on the intercept assumption), 5 are partially reproduced and 8 are not reproduced. The 3 blocked claims (rnn-curved-manifold, rnn-perturbation, monkey-g) are still `data_missing`.

What I ran:
- **Lock:** `python tools/entry.py lock entries/sohn-2019` rewrote `requirements.lock.txt` with the same contents, still Python 3.13.
- **Check and run:** `python tools/entry.py all entries/sohn-2019` reported 0 errors and both notebooks passed. Nothing the run reads had changed since the last run, so it reused the executed copies from 13:28 UTC instead of executing again (60 s and 686 s then).
- **Handover:** `python tools/entry.py handover entries/sohn-2019` wrote `executed/sohn-2019/handover/`.

Nothing is committed or pushed. If questions were meant to go to a reader, someone has to write `questions/sohn-2019.yaml` and run the reader's answer step again before another `author-answers` run.
