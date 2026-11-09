There were no questions to answer, so I changed nothing.

- **No questions file:** `questions/001960.yaml` does not exist on this branch, and git history on all branches has no version of it.
- **The author asked nothing:** the latest author run's report, `transcripts/001960/author-report.md:44`, says "Questions to a reader: none." It recorded its eight open method questions as `methods_unavailable` findings for the paper's authors, not as questions for a reader.

I left `claims/001960/` and `questions/` untouched. I also did not run the quote check: my call to `python tools/claims_check.py` used the wrong arguments and only printed its usage text. If a questions file is added later, this run should be repeated.
