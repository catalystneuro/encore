There were no answered questions, so I changed nothing in the claims, notebook, conclusions or attempt record. No outcome changed.

**Why there was nothing to answer**
- `questions/001274.yaml` doesn't exist in the working tree or anywhere in git history.
- In the author run I asked a reader no questions (`transcripts/001274/author-report.md`: "Questions to a reader: none"). The three open items in `attempts/001274-semenov-2025-01.yaml` are questions for the paper's authors, not a reader: the soma ROI, how the generator voltages were set, and the rule for counting APs.
- The answer run found the same thing and changed no files (`transcripts/001274/answer-report.md`).
- `claims/001274/` hasn't changed since the claims check (last commit `3ced85ea0`). The claims tested are exactly the ones my author run tested.

**Question by question:** none, so no claim needed re-running and no claim's notes needed a line about an answer. All 26 outcomes stay as recorded: 2 reproduced (one resting on an assumption), 7 partially reproduced, 3 not reproduced and 14 blocked.

**Entry steps**
- **Lock:** `python tools/entry.py lock entries/001274-semenov-2025` wrote `requirements.lock.txt`, which came out unchanged.
- **Check and run:** `python tools/entry.py all entries/001274-semenov-2025` reported 0 errors. The notebook passed from a clean environment in 700 s, against 20.4 minutes last time.
- **Handover:** `python tools/entry.py handover entries/001274-semenov-2025` wrote `executed/001274-semenov-2025/handover`.

I didn't verify my own work, and nothing is committed or pushed. If questions were meant to go to a reader for 001274, the file was never created on this branch.
