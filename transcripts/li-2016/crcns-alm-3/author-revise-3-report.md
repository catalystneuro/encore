One outcome changed and no proposals remain open.

- **Changed:** `fig6-modular-models-robust` went from `partially_reproduced` to `not_reproduced`. The verifier agreed with the proposal in round 3. The modular integrator, using the matrix printed in the paper, recovers on lick-right trials but not on lick-left trials (-7.2 against -14.4). That is 50% of runs, and the criterion needs 90%. The criterion also has no rule for a partial result. I set the outcome, removed `proposed`, and updated the claim's notes.
- **Still standing:** none. This was the only proposal, and no other outcome changed.

I updated the notebook's result for this claim and its summary row, and the README table. In the attempt record I added round 3 under `verifications`, with one result for this claim: the verifier agreed, gave `not_reproduced`, its reason is in its own words, and my response is included. `python tools/entry.py all entries/crcns-alm-3-li-2016` reported 0 errors and the notebook passed (502 s). Nothing is committed or pushed.

The working tree also has untracked files I didn't create, such as `.bashrc`, `.mcp.json` and `scripts`. I left them alone; they shouldn't go into the commit.
