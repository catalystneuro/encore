I've applied round 3. One outcome changed and no proposals remain. The re-run (`python tools/entry.py all entries/001828-mantas-2024`) passed with 0 errors, the notebook took 208 s, and `check` also reports 0 errors.

**Outcome changed**
- `fig4b-speed-correlation-dcp` went from partially reproduced to not reproduced, and its `proposed` block is removed. The verifier agreed for the same reason it gave in rounds 1 and 2. The dLight-dCP part passes, but Anxa1 is the main subject of the claim and misses p < 0.05 in every reading (p = 0.064 to 0.21). This follows the same rule as fig3e.
- I updated the matching text in the notebook's cell 48 conclusion and its Summary table, the entry README table, and the claim's notes in the attempt record.
- The verifier pointed out one small gap: after the kinematics lag move, dLight-dCP is 6 of 8 positive with Wilcoxon p = 0.0547 against permutation. I added this to the conclusion and the notes. It doesn't affect the outcome, and the re-run output shows the value.

**Proposals that stand:** none. This was the only proposal, and the verifier agreed with it.

Round 3 is now recorded under `verifications`, with one result for this claim (agrees: true, not_reproduced), the verifier's reason, and my response. Nothing is committed.
