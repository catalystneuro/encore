Nothing needed re-running: no reader has answered any question on this paper, because none was ever asked.

**The questions.** `questions/tingley-2018.yaml` does not exist. The first author run asked a reader nothing (`transcripts/tingley-2018/author-report.md`: "I asked a reader no questions"). Its two open method points, how bins with undefined phase enter the decoder and how peak information is converted to bits/cm, are questions for the paper's authors. They are recorded as `methods_unavailable` findings, not questions for a reader. The reader's answer run came to the same conclusion (`transcripts/tingley-2018/answer-report.md`) and changed nothing.

**What changed.** Nothing. `claims/tingley-2018.yaml` is byte-identical to the copy in the 09:58 UTC handover, so no claim was amended. I did not edit the notebook, the conclusions, the attempt record or any claim's notes, since there was no answer to record.

**Outcomes.** All 32 claims are unchanged from the first author run: 9 reproduced, 12 partially reproduced, 11 not reproduced, 6 blocked. The per-claim table is in `transcripts/tingley-2018/author-report.md`. No earlier outcome changed.

**Entry.**
- **Lock:** wrote `requirements.lock.txt`. The entry hash is still the one from the last clean run (6c76cd7b2638).
- **Check:** 0 errors.
- **Run:** the notebook passed, but nothing was executed. The tool reused the 09:58 UTC executed copy (a 1,139 s run) because nothing the run reads had changed. `--fresh` would force a full run of about 19 minutes; I didn't think it was needed.
- **Handover:** rebuilt in `executed/tingley-2018/handover/`.

I did not verify my own work, and nothing was committed or pushed. If the verifier's questions were meant to go into the questions file, they haven't been written there yet. Once a reader answers them, this step can be run again.
