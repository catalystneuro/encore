There was nothing to answer, so I changed no files.

- **No questions file:** `questions/001274.yaml` does not exist, either in the working tree or anywhere in the git history (`git log --all -- questions/001274.yaml` returns nothing).
- **The author asked none:** their report (`transcripts/001274/author-report.md:46`) says "Questions to a reader: none."
- **The open items are for the paper's authors:** the attempt file (`attempts/001274-semenov-2025-01.yaml`, lines 352 to 362) has three questions. They ask which pixels form the soma ROI, how the generator voltages were set, and what rule counted APs. These are method details, which the author takes from the paper (Author, step 1.6), so they don't come to me.

`claims/001274/` is unchanged and I didn't run `tools/claims_check.py`. If questions for 001274 were expected, the file was probably never created or wasn't put on this branch.
