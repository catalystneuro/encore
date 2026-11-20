One outcome changed and no proposals are left open.

**Outcome changed:** fascicles-larger-cervical went from `reproduced` to `partially_reproduced`, which the verifier agreed with in round 3. With the mixed model test that matches the paper's F and p, cervical fascicles are larger in all three species. But the pig difference has p = 0.055, so only two of three species pass p < 0.05. I removed `proposed` from the claim. It keeps `assumed: true`, and the deviation now also says this test does not give the paper's p values for the within-species level comparisons.

**Proposals still standing:** none. This was the only proposal, and no proposal was refused.

**Updated to match:**
- **Notebook:** the result cell for the claim and its row in the summary table.
- **Entry README:** the table now reads 28 reproduced (five resting on an assumption) and 4 partially reproduced.
- **Attempt record:** the claim's notes and deviation.
- **Round 3 under `verifications`:** one result for this claim, with agreement, the outcome partially reproduced, the verifier's reasons and caveats in its own words, and my response.

`python tools/entry.py all entries/pelot-2020` passes: 0 check errors, and the notebook ran in 245 s. Nothing is committed.

Some untracked files are in the repository root that I did not create: `.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.vscode`, `scripts` and others. I left them alone. You may want to keep them out of the workflow's commit.
