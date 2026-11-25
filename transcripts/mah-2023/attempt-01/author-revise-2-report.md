No outcome changed, and I'm not proposing any changes. The verifier agreed with all 33 outcomes in round 2, and the new outputs back them. The entry was re-run with `python tools/entry.py all entries/mah-2023`: it passed in 24.0 min, and `check` reports 0 errors.

**Outputs added (two new notebook cells)**
- **fig3i:** the report said nothing backed the claim that the direction holds for "any small positive alpha_0". A new cell runs the Equation 10 model without noise for every rat at alpha_0 = 0.01, 0.05, 0.1042, 0.2, 0.4 and 0.8. At every value the model is higher after offers below 20 uL, by +0.077 to +1.076 z on average. That holds in 273 of 291 rats at 0.01 and in 290 or 291 at the others. The deviation now cites these numbers.
- **fig5c:** the report asked how often trials after a violation repeat the previous offer.
  - Within a session and block they always do: the share is 1.000 in all 16 rats, against 0.195 to 0.226 after other trials. So the confound argument holds within sessions.
  - The only trials that don't repeat are each session's first trial, whose "previous trial" is the last trial of the session before.
  - Dropping post-violation trials removes only those: 455 of the 18,075 trials in the 20 uL test, all slow to initiate (mean z +2.920 against −0.057 for the rest). That is why dropping them moves p from 0.0676 to 0.611.
  - The 20 uL population test fails either way, so the outcome stands.

**Text corrected**
- **fig5c:** the Result cell and notes now say the count of 14 significant rats is weak support. Five of them are in the opposite direction, and three have differences near 0 (E008, S042, M044).
- **fig3l:** added the verifier's caveat. The paper's N = 116 cannot come from a refit with 128 rats at the lambda bounds, so the failure may be the refit's. The 40/60 split, which has no ties, also fails.
- **Timings (fig3j, suppfig8, fig3f, fig3l):** the record, the blocked-claims cell and the Summary now give this run's numbers beside the verifier's. That is about 3.3 h on one core here and about 5.5 h on the verifier's machine; both are beyond the 1 h limit. The timings depend on the machine: this run was 24.0 min, the verifier's 45.3 min.
- **Earlier estimate:** the record now says it was 138 h in my earlier run and 162 h in the verifier's round-1 run.
- **Loading time:** cell 2 and the README now say 6 to 14 minutes.
- **fig2f:** the text now says the code reading has the opposite sign to the legend's r.
- **entry.yaml:** `runtime_minutes` is now 45.
- **Record:** round 2 is added under `verifications`, with the verifier's reasons and my responses for all 33 claims.

**Not done**
- I did not enlarge the fig3i noise-only control beyond 20 replicates. The verifier says it cannot reverse the outcome.
- The verifier reported no new misreading of the claims file, so nothing was added to `questions/mah-2023.yaml`.
- After the final run I reworded two markdown cells (the loading and timing wording) so they no longer depend on one run's numbers. No code changed, so the executed copy differs from the committed notebook only in those two cells.
- Some untracked dotfiles and folders I didn't create (`.bashrc`, `.vscode`, `scripts` and others) are in the working tree. I left them alone.
