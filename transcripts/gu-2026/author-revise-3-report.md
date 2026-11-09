Round 3 is applied and recorded. `python tools/entry.py all entries/001836-gu-2026` passed with 0 errors, and the re-run took 11 min 39 s. Nothing is committed.

**Outcome changed:**
- **fig3d-distant-vs-inbound** went from `partially_reproduced` to `not_reproduced`. The verifier agreed with the proposed change, so I removed the `proposed` block.
  - The notes now say the outcome verified in round 2 rested on the smaller bound.
  - The notes also give the verifier's caveat: the result is borderline. It rests on the first draw and on counting the tables that match neither trigger as COM tables.
  - The deviation that kept the smaller bound is marked as the round-2 assumption, now replaced. The decoder A assumption is no longer described as being only for the proposal.

**Proposals still standing:** none. This was the only proposal in the record, so no claim carries a `proposed` key now.

**Text updated to match:**
- In the notebook, the conclusion cell for this claim (cell 58) now reads "not reproduced", with the borderline caveat. The Summary table row (cell 69) is updated too.
- In `entries/001836-gu-2026/README.md`, the outcome table row and the Figure 3D paragraph now give the new outcome.
- In `attempts/001836-gu-2026-01.yaml`, round 3 is recorded under `verifications` with the one claim the verifier reviewed: it agreed, its outcome is `not_reproduced`, its reason in its own words, and my response.

The re-run's cell 56 and 57 outputs still match the numbers quoted in the record. For example, decoder A's fourth-smallest p has a median of 0.044 over the 20 draws.

`git status` also shows untracked files I didn't create and haven't touched: shell dotfiles, `.idea`, `.vscode`, `.mcp.json` and `scripts`. They were not there when the run started. Make sure the workflow's commit doesn't pick them up.
