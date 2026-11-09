I made no changes, because there are no questions to answer for DANDI:001845.

- `questions/001845.yaml` does not exist, and git history has no version of it on any branch.
- The author's report says so directly (`transcripts/001845/author-report.md:35`): "Questions to a reader: none."
- The author's open points went to the paper's authors instead, as four `methods_unavailable` findings: the ANOVA type, the rate units, the event and trial definitions, and the reinforcement-learning parameters. Those are not reader questions under protocol step 6.
- No verifier run has happened yet, so no verifier questions exist either.

I left `claims/001845/` alone and did not create a questions file. Since nothing changed, I didn't run `tools/claims_check.py`.

The working tree already had uncommitted edits to `tools/build_site.py` and `tools/site_assets/app.css` before I started. I didn't touch them.
