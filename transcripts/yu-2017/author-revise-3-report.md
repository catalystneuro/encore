Round 3 is applied and recorded. The re-run passed: `python tools/entry.py all entries/crcns-hc-13-yu-2017` ran the notebook in 712 s with 0 errors, and `check` also gives 0 errors. The re-executed cell 64 prints the same numbers the record quotes.

**Outcomes changed**
- **fig2s1cd-theta-autocorrelation:** changed from partially_reproduced to reproduced, and `proposed` is removed. The verifier agreed for two reasons:
  - Under the claims file's own reading of entries and exits, every immobility period (O1 (b)), all four depth comparisons hold.
  - The partial outcome came only from the well-visit variant, which is not a reading in the claims file.
- The totals are now 12 reproduced, 6 partially reproduced, 11 not reproduced and 3 blocked.

**Proposals that stand:** none. This was the only proposal, and the verifier agreed with it.

**Other changes**
- **Notebook cell 65:** the verifier noted that this cell gave the peak range as 0.105 to 0.125 s, but that figure only appears in the well-visit variant. It now gives 0.115 to 0.125 s. It also now says:
  - the IAP depths are small (14 IAPs, from T1 and S2);
  - the entry and exit windows cover about half of task time, so the test only weakly isolates the periods around transitions;
  - the claim should be tested again if the claims file's O1 (b) is revised to well visits.
- **Notebook summary:** the table row now reads "reproduced (foraging rats)".
- **Attempt record:** the claim's notes now say the same as cell 65.
- **Round 3 under `verifications`:** recorded with one result for this claim (agrees: true, outcome reproduced), the verifier's reason and my response.
- **Entry README and questions file:** neither needed a change, since neither mentions this outcome.

Nothing is committed or pushed. The untracked files in the working tree (`.bashrc`, `.idea`, `scripts` and others) were already there and I did not touch them.
