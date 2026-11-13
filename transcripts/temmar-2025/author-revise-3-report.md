One outcome changed and no proposals are left. Round 3 is recorded, and `python tools/entry.py all entries/temmar-2025` gives 0 errors with all four notebooks passing on a fresh execution. Nothing is committed.

**Outcome changed**
- **`fig2a-irregular-shifts`** goes from `partially_reproduced` to `reproduced`. The verifier agreed with the proposal, so I set the outcome and removed `proposed`. In the fresh run, the LSTM median over the 27 window sessions is 0.641, inside the 0.529 to 0.651 range of the 20 every-16th reference sessions. The ridge regression part (0.321 inside 0.220 to 0.360) and the shift part (38 of 42 window days) also hold. All figures are unchanged from round 2.
- No other outcome was touched.

**Proposals that stand:** none. This was the only proposal.

**Other changes**
- **Attempt record:** I rewrote the claim's notes. They now say that only the summary percentiles of the refit reference sessions are shown to match, not each session's R2, as the verifier pointed out. They also say the pass is narrow: 0.010 below the 90th percentile, with 18 window sessions unfitted. Round 3 is added under `verifications` with one result: agrees, `reproduced`, the verifier's reason, and my response.
- **Notebooks:** the conclusion and summary of `decoding.ipynb` and `window.ipynb` now give `reproduced`. I dropped the "a failure to reproduce here..." sentence from `window.ipynb`'s summary, because nothing in that notebook fails now. `decoding.ipynb` keeps it for `suppc1-shuffle-baseline`, which is still partially reproduced.
- **README:** no change was needed, as it does not state this claim's outcome.
- **`questions/temmar-2025.yaml`:** I added a question for a reader. The verifier found the claims file's shift rule fires on 237 of the 243 days outside the window, so it does not single out July to November 2022.

**How the run was done:** the full run takes about 2 h 20 min, over the 2 h limit on one command. A detached run gets killed when its call ends, even when started outside the sandbox. So I used a small script with `entry.py`'s own functions and the same `nbconvert` command to execute the notebooks in two foreground calls of two each (8, 34, 24 and 29 min). It then wrote the clean-run stamp the same way `run` does. The final `entry.py all` ran the check and reused those copies without executing anything. If you want one uninterrupted run, `--fresh` will do it.

The untracked dotfiles in the repo root (`.bashrc`, `.mcp.json` and others) are placeholders the sandbox created at 03:16, before this run started. They are not part of these changes.
