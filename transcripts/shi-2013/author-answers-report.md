I made no changes in this run because there were no answers to work from. `questions/shi-2013.yaml` doesn't exist, either in the working tree, on `main`, or anywhere in git history.

- **No questions were asked.** My first author run (`transcripts/shi-2013/author-report.md:40`) says "I asked no reader questions." The open method details were questions for the paper's authors. They are recorded in `attempts/shi-2013-01.yaml` as a `methods_unavailable` finding.
- **The reader changed nothing.** The answer run (`transcripts/shi-2013/answer-report.md`) found no file, amended no claim and created no questions file.
- **No claim was amended.** `claims/shi-2013.yaml`, `entries/shi-2013/` and `attempts/shi-2013-01.yaml` are identical to my first author commit (49499d33c2), and none of them has uncommitted changes.

**Answers, changes and outcomes:** with no questions, no claim was affected, so every outcome stays as the first run left it. Of the 28 claims, 7 are reproduced, 6 partially reproduced, 12 not reproduced and 3 blocked.

**Not done:** I didn't re-run the notebook, the conclusions or the record, and I didn't run `lock`, `all` or `handover`. Those steps re-run claims that an answer changed, and nothing changed. The first run already ran `lock`, `check`, `all` and `handover` on this same entry, with 0 errors. If you still want a fresh run as a formality, `python tools/entry.py all entries/shi-2013` took about 7 minutes last time.

If questions were meant to be asked, step 1.6 points at three readings the claims file may need to settle:
- which trial code means Vision (I inferred code 7 is No Vision from the abort counts);
- that monkey B is missing from the deposit;
- how to compare counts out of 343 when the data hold 359 monkey X sessions.

The first run treated these as assumptions and deviations, not as reader questions. Nothing is committed.
