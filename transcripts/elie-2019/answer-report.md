There are no questions to answer, so I changed nothing.

- **No questions file:** `questions/elie-2019.yaml` does not exist in the working tree or anywhere in git history (`git log --all` finds nothing).
- **The author asked none:** the author run's report says "Questions to a reader: none." (`transcripts/elie-2019/author-report.md:36`). The questions it did have are for the paper's authors, and it recorded them as a `methods_unavailable` finding, which is not a reader's job.
- **No verifier questions either:** no verifier run has been made on this attempt yet.

I left `claims/elie-2019.yaml` as it is and did not create an empty questions file. I didn't run `tools/claims_check.py` because no claim was edited. If a verifier raises questions later, this answer step can be run again on them.
