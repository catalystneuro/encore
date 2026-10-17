One outcome changed this round. **fig3g-spatial-information** went from reproduced to partially_reproduced. That was the only proposal, and the round-3 verifier agreed with it. No proposals remain.

- **Attempt record** (`attempts/000568-valero-2022-01.yaml`): I set the outcome, removed `proposed`, and rewrote the fig3g notes. The notes now give the time-matched correlations and label the matched increases by group (place -0.10, unmasked -0.17), which was the verifier's minor wording point. I added round 3 under `verifications` with one result for fig3g: agrees true, partially_reproduced, the verifier's reason and my response.
- **Notebook:** I rewrote cell 60's conclusion as "Result: partially reproduced" and updated the fig3g row in the summary table.
- **README:** I updated the spatial information row to "Partially reproduced".
- **Re-run:** `python tools/entry.py all entries/000568-valero-2022` passed with 0 errors in 289 s. The fig3g numbers in the new run are the same as before (0.501, 0.609, 7.6e-10, p = 0.3).

Nothing is committed. There are untracked dotfiles and folders in the repo root (`.bashrc`, `.idea`, `scripts` and others) that I did not create, and I left them alone.
