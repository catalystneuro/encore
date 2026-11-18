**figs12-3v-propagation is now blocked (data_missing).** It was the only claim with a proposed change, and the round-3 verifier agreed with it. It was partially reproduced before. No other outcome changed and no proposals remain open. `python tools/entry.py all entries/xia-2021` passes with 0 errors, and the notebook ran in 122 s.

**What changed in the record (`attempts/xia-2021-01.yaml`):**
- The claim now has `outcome: blocked` and `blocked_by: data_missing`, and the `proposed` block is gone.
- I also had to remove the claim's `assumed: true`. The schema does not allow it on a blocked outcome, and the check failed until I took it out. The deviations stay, since they still describe the analysis of the one deposited mouse.
- The claim's notes now say the block was agreed in round 3. They also pass on the verifier's point about the claims file: if the two missing mice are ever deposited, rostral should be read from the electrode side as the criterion says, not from the frame orientation assumed here.
- The data_missing finding now counts sixteen claims blocked for missing data, up from fifteen.
- Round 3 is recorded under `verifications` with one result for this claim: it agreed, its outcome is blocked, its reason is in its own words, and my response is there.

**Notebook and README:**
- The notebook's header now says 12 claims are analysed and 18 blocked in all, and its claims table, the conclusion in cell 55 and the summary row match the blocked outcome.
- The README moves the claim into the "Blocked" row, which now covers 17 claims.

Nothing is committed. The working tree also has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.
