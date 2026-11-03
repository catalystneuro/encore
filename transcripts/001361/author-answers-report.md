There were no questions to act on, so no claim, outcome, notebook cell, conclusion or record entry changed.

**The questions.** `questions/001361.yaml` does not exist, and git has no history of it on any branch. The earlier author run asked a reader no questions. The answer run's report (`transcripts/001361/answer-report.md`) agrees: it found nothing to answer and did not amend the claims file. The attempt record holds three `methods_unavailable` findings, but those are questions for the paper's authors, not a reader:
- the OASIS time constant and shuffle details;
- how cells were registered across days;
- how the active-trial threshold is defined.

**Per claim.** With no answered questions, no claim was affected, so every outcome stands as before: 27 reproduced, 11 partially reproduced, 5 not reproduced and 7 blocked, out of 50.

**Entry steps:**
- **Lock:** `requirements.lock.txt` came out unchanged.
- **Check and run:** 0 errors, and the notebook ran clean from a fresh environment in 41 minutes. This checkout had no executed copy, so the handover needed this run.
- **Numbers:** all 20 claims that record a measured value show that value in the new outputs. That includes fig6e and ed8k, whose counts varied before seeding was fixed, so the conclusions still match the numbers.
- **Handover:** built in `executed/001361-sosa-2025/handover/` (notebook, `sosa.py`, claims file).

No tracked file changed, and nothing is committed or pushed. If a questions file was meant to be supplied for this run, it is missing, and this step would need to be repeated once it is added.
