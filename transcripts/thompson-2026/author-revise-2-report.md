I've addressed every point in the round-2 report and re-run the entry. `python tools/entry.py all` passed (the notebook ran in 206 s), and the final check gives 0 errors. Nothing is committed.

**Outcomes:** none changed and none proposed. It stays 14 reproduced, 1 partially reproduced (figs1-raw-baselines-similar) and 2 not reproduced (range-baseline-lc-evoked-pupil, figs2-llr-cross-epoch). The verifier agreed with all 17, and the new outputs support them.

**Added or corrected:**
1. **Wrong reason in the Summary.** The cell 52 sentence saying all three shortfalls come from the evoked pupil is replaced.
   - For the range claim and the cross-epoch LLR counts, the Summary now says the paper's numbers need both the code's trial rule and its evoked pupil.
   - For figs1, it now says the difference comes from the trial set. The failing cell (row 6 in Ci) does not use the evoked pupil.
2. **Why the code reproduces figs1.** A new cell in the figs1 section shows it.
   - The code's rule keeps 85 unit-by-trial rows that the Methods' rule drops (20 Oz, 65 Ci). In each, the beep falls 7 to 69 ms before the trial ends.
   - Their evoked rates are lower (Ci 3.15 against 6.99 sp/s).
   - If the code reading also drops trials whose 200 ms window runs past the trial end, row 6 in Ci gives p = 0.12 with raw baselines, so it fails there too. With residuals it gives p = 0.028 (the code reading gives 0.0105).
   - One correction to the verifier: the code-rule trials whose beep comes after the trial end have no evoked pupil, so they enter no table.
   - The result cell, the figs1 and row 6 notes, and the code_mismatch finding now say all this.
3. **The Figure 3 z-scoring claim.** The code's output does print its Figure 3 values, so cell 13 now compares them. Z-scoring by within-session unit index (the code's way) matches 12 of 12 to three decimals; z-scoring per unit matches 2 of 12. Cell 14, the link claim's notes and the finding now state those counts.
4. **Unflagged assumptions.** `assumed: true` is now on all 16 paper claims.
   - The trial-start deviation is reworded as an assumption, and added to the 10 claims that lacked it.
   - Taking the stored pupil as already z-scored per session is now an assumption on both fig3 claims.
   - A new `methods_unavailable` finding asks the paper's authors three things: what the trial start marks, whether the stored pupil is already preprocessed, and which units and sessions they used (63 and 51 for Ci in the paper, 61 and 50 in the code's output).
5. **Minor points.** I removed the unprinted sentence about the draft from cell 0. The data-units-sessions notes now give 7 to 109 beep trials per unit under the Methods' rule and 7 to 111 under the code's.
6. **Round 2 is recorded** under `verifications`: all 17 claims, with the verifier's reasons and my responses.

**Not done, and why:**
- I left the round-1 reasons' cell numbers unchanged, though they no longer match the notebook. They are the verifier's own words, and the round-2 entry quotes the current numbers.
- I added no questions to `questions/002034.yaml`, because the verifier found no misreading of the claims file.
- Which units and sessions the paper used can't be settled from the archive, so it is now one of the questions for the paper's authors.
