The round-3 verifier agreed with the only proposed change, so it now stands as the outcome and no proposals remain.

**What changed:** fig3b-pmd-higher-dimensional moves from reproduced to partially_reproduced (still marked assumed), and its `proposed` field is gone. This follows from using one kernel reading for every claim: a 100 ms standard deviation. Under it, the M1 and PMd medians are 7 and 10, outside the paper's tolerance of 8.5 and 14. They stay outside tolerance in all 2002 possible sets of 16 sessions. PMd is still higher than M1 in every session. No other outcome changed.

**Updates to match:**
- **Attempt record:** for fig3b, `measured` is now 7 and 10, and the notes and kernel deviation are rewritten for the standard-deviation reading. I also updated the fig6c kernel deviation and the noise-scale finding, which still referred to the old fig3b result. The verifier's points that remain open are recorded: the claims file header would block the claim, and the outcome still rests on the assumed noise scale.
- **Notebook:**
  - The fig3b conclusion (cell 19) and the Summary are rewritten.
  - Cell 34 now says the Gallego 2020 paper used multiunit threshold crossings in 30 ms bins. The verifier said this cell overstated how closely that paper matches.
- **Entry README:** the fig3b row now reads "Partially reproduced (assumed)".
- **Round 3:** recorded under `verifications`, with the verifier's result, its reasons and my response.

`python tools/entry.py all entries/000688-perich-2018` passed: 0 check errors, and the notebook ran in 1075 s. I checked the numbers now cited in the text against the executed copy and they match. Nothing is committed.

The working tree has some untracked files I didn't create: shell dotfiles, `.idea`, `.vscode`, `.mcp.json` and `scripts`. I left them alone; check they don't get picked up by the workflow's commit.
