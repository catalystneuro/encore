The round-3 verifier agreed with both proposed changes, so both outcomes are now changed and no proposals are left.

**Outcomes changed**
- **fig4c-wt-contrast-zx1-effects**: from blocked (methods_underspecified) to **partially_reproduced**, marked `assumed: true`. I removed `blocked_by` and `proposed`. All four model and coding readings meet the partial condition: the contrast × ZX1 term has p = 3.0e-05, and 5, 5, 4 and 3 terms pass. The result depends on the pupil cleaning.
- **fig4-wt-posthoc**: from partially_reproduced to **not_reproduced**, still `assumed: true`, with `proposed` removed. The criterion's part that ZX1 does not change LOW fails at p = 0.0496, and the criterion has no partial level. The notes still say that the narrower step rule meets all four parts, as the verifier asked.

**Other updates**
- **Notebook:** I rewrote the conclusion cells for both claims and updated the header (the tested table and the revision history), the summary table and the Discussion cell that mentioned the post hoc outcome.
- **README:** both rows of the outcome table are updated.
- **Attempt notes:** both claims now describe their new outcome.
- **Round 3:** recorded under `verifications` with two results. Each says the verifier agreed, gives its outcome, its reason in its own words and my response.

`python tools/entry.py all entries/001256-cody-2024` ran in about 3 minutes with 0 errors, and the notebook passed. I added the round-3 record after that run. It changes only the attempt file, and `tools/entry.py check` still reports 0 errors. Nothing is committed.

`git status` lists some untracked files I did not create: dotfiles such as `.bashrc` and `.gitconfig`, plus `.idea`, `.vscode`, `.mcp.json` and `scripts/`. I left them alone. Leave them out of the workflow's commit unless they belong in it.
