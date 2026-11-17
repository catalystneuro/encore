I changed nothing in this run, because no question was ever asked on the claims file and so none was answered.

- **No questions file.** `questions/dana-2016.yaml` does not exist, either in the working tree or in any local branch's history. The first author run reported "Questions to a reader: none", and the reader's answer run (`transcripts/dana-2016/answer-report.md`) also found nothing to answer. `claims/dana-2016.yaml` was not amended.
- **Nothing re-run.** No claim was affected, so I left the notebook, the conclusions and the attempt record `attempts/dana-2016-01.yaml` alone. Every outcome is the same as before: 9 tested claims (8 reproduced, one of them resting on an assumption, and 1 partially reproduced), 1 not reproduced, and 25 blocked.
- **Entry commands.** I ran all three:
  - `lock` rewrote `requirements.lock.txt` with the same contents.
  - `all` passed with 0 errors. It reused the executed copy from 12:37 UTC, since nothing the run reads has changed (222 s originally).
  - `handover` wrote `executed/dana-2016/handover`.

  Nothing is committed or pushed, and I did not verify my own work.

One claim might be worth a question. `screen-single-mutations-improved` is not reproduced: by the criterion's rule the supplementary tables give 230 improved RCaMP1h variants and 58 improved R-GECO1 variants, against the paper's 353 and 187. The first run recorded that gap as a `paper_inconsistency` finding, not as a question about how the claims file reads the paper. If a verifier thinks the claims file misreads that passage, they can add a question for a later reader run.
