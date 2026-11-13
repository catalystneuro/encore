Round 3 is recorded. One outcome changed, and no proposals are left open.

**Changed:** `fig10c-strf-mi-higher` went from reproduced to not_reproduced. This was the only claim with a proposal, and the round-3 verifier agreed. In the printed draw none of the four readings reaches p < 0.001: p = 0.0015, 0.0076, 0.049 and 0.19. The linear (a) reading passes in only 2 of 5 subsampling draws, so the result is the same under either projection.

**Updated to match:**
- **Attempt record** (`attempts/see-2018-01.yaml`):
  - I set the outcome and removed the `proposed` block.
  - I rewrote the claim's notes.
  - I rewrote the deviation that said the linear projection had been chosen. It now says both projections were run and neither passes.
  - I left `assumed: true` as it was, because the STRF resolution and MI bins are still this attempt's own choices.
  - I added round 3 under `verifications` with one result: agrees, not_reproduced, the verifier's reason in its own words, and my response.
- **Notebook:** I rewrote the conclusion in cell 80 and the summary row in cell 99.
- **README:** I changed the outcome row and the paragraph that described the proposal.

`python tools/entry.py all entries/see-2018` passed: 0 check errors, and the notebook ran in 2821 s. The new execution prints exactly the fig10c numbers the text cites, including the held-out check and the five-draw table.

Nothing is committed. `tools/entry.py` and `tools/notify.py` already had changes when the run started, and several untracked dotfiles and folders are in the checkout. I did not create or touch any of them.
