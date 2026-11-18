The verifier agreed with both proposed changes in round 3, so I applied both. `python tools/entry.py all entries/van-der-molen-2025` passed: 0 check errors, and both notebooks ran (1658 s and 1318 s). The re-run outputs still match the numbers quoted in the record (cells 51, 125 and 129).

**Outcomes that changed**
- **ed4d-gabazine-rank-order**: reproduced to blocked (`methods_underspecified`). Under the z-score gabazine is higher by 2.0 (p printed as 0). Under the (A - B)/(A + B) ratio it is lower by 1.15 (p 0.6). The criterion requires both readings to pass.
- **supp10b-rank-order-by-model**: reproduced to blocked (`methods_underspecified`). Of the four combinations of normalisation and recording length, it passes only under the z-score with the code's lengths.

**Proposals that stand:** none. The record now has 29 reproduced, 11 partially reproduced, 7 not reproduced and 3 blocked.

**Other edits**
- On both claims I removed `proposed` and also `assumed: true`, because the schema does not allow `assumed` on a blocked outcome.
- I rewrote the notes and deviations of both claims to describe the blocked outcome. The supp10b deviations now say that the second reading has 5 shuffles per recording.
- I updated the notebook's two conclusion cells (52 and 126), its summary table and the README's counts. The README now says why these two claims are blocked.
- Round 3 is recorded under `verifications` with one result per claim: `agrees: true`, `outcome: blocked`, the verifier's reasons in its own words, and my response.

Nothing is committed.
