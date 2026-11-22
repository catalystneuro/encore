I applied all three outcome changes. The verifier agreed with every proposal from round 2, so none are left standing.

**Outcomes changed:**
- **speed-threshold-robust**: partially reproduced → not reproduced. LFP fails at 5 cm/s and CSD fails from 0.5 cm/s, and the criterion has no clause for a partial result.
- **figs10a-fs-trn-no-modulation**: partially reproduced → reproduced, under the per-trial reading (c) used for fig3a. As the proposal said, I also removed its "Assumed" deviation and the `assumed: true` flag, which go beyond the outcome field itself. The notes and the notebook conclusion now give the two weak points the verifier asked the record to state:
  - FS rates are lower during running per unit, per mouse and within sessions (van Elteren p = 1.3e-08).
  - The result depends on TRN being only the SM-TH units under 0.35 ms. Adding the one responsive RT unit gives p = 8e-06, which would make the claim not reproduced.
- **fig2fg-opto-thalamic-inhibition-delays-rebound**: partially reproduced → not reproduced. One of the six signed-rank tests fails (SM-TH Opto75 against Opto125, p = 0.20).

**Other edits:**
- I removed the three `proposed` blocks.
- In both notebooks I updated the conclusion cells (main cells 28 and 56, opto cell 9) and the summary tables.
- In the README I updated the table rows and removed the paragraph about pending proposals.
- I recorded round 3 under `verifications` with one result per reviewed claim: agrees true, the verifier's outcome, its reasons and my response.

`python tools/entry.py all entries/russo-2025` ran in 17 min with 0 errors, and both notebooks pass. The re-run outputs still show the numbers the conclusions cite (cells 27, 54 and 55, and opto cell 8).

Nothing is committed. There are untracked files I did not create (dotfiles such as `.bashrc` and `.gitconfig`, plus `.idea`, `.vscode`, `.mcp.json` and `scripts`). I left them alone, but they should stay out of the workflow's commit.
