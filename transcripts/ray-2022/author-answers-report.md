There were no questions to answer, so no claim was re-run and no outcome changed.

- **No questions file.** `questions/crcns-nac-1.yaml` does not exist. The author run asked a reader nothing ("Questions to a reader: none" in `transcripts/crcns-nac-1/author-report.md`). The reader's answer run found nothing to answer and changed nothing (`transcripts/crcns-nac-1/answer-report.md`).
- **Nothing was amended.** `git diff 5787303155 HEAD` shows no change to `claims/`, `questions/`, `attempts/` or `entries/` since the author run. The claims file, notebook, conclusions and attempt record are as the author run left them. I did not edit them, since there is no answer to record in any claim's notes.
- **Questions for the paper's authors.** The three open questions from the author run remain recorded as `methods_unavailable` findings in `attempts/crcns-nac-1-ray-2022-01.yaml`. They cover the k-means normalization and labels, how ITI events were chosen, and how 0/0 suppression ratios were handled. They are not reader questions, so the answer run did not settle them.

Outcomes, all unchanged from the author run (earlier outcome = current outcome): 17 reproduced, 8 partially reproduced, 8 not reproduced, 1 blocked (fig1c-acquisition, `data_missing`).

**Entry checks:**
- `lock` rewrote `requirements.lock.txt` with identical content (no diff).
- `all` passed: 0 errors, and the notebook ran in 103 s from a clean environment.
- `handover` wrote `executed/crcns-nac-1-ray-2022/handover/`.

Nothing was committed or pushed, and I did not verify the attempt myself.
