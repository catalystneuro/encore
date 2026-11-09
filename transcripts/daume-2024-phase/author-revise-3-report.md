The verifier agreed with both proposals in round 3, so both outcomes have changed. No proposals are left standing.

**Outcomes changed**
- **fig2f-rt-single-trial-pac:** from not_reproduced to blocked (`methods_underspecified`). The verifier asked for `assumed: true`, but the attempt schema does not allow it on a blocked outcome. A deviation now says the outcome assumes artefact reading (a), and that under reading (b) every RT scale and both single-trial PAC readings meet the criterion.
- **fig3h-pac-category-firing:** from not_reproduced to reproduced. It keeps `assumed: true`.

The `proposed` blocks are removed from both claims.

**Other updates**
- **Rounding:** I fixed the verifier's two rounding slips: the amygdala minimum p is now 0.479 for fig2f and 0.326 for fig3h.
- **Notebook, README and record:** the conclusions and summary in `reproduce_daume_2024_lfp.ipynb`, the entry README (outcome table, explanation and run times) and the outcome notes in the record now match the new outcomes.
- **Round 3:** recorded under `verifications` with a result for each of the two claims, the verifier's reasons and my response.
- **New question for a reader** in `questions/000673.yaml`: the verifier noted that Table S2's PAC estimate of −49.07 can only come from the raw single-trial MI, which would fix that reading for fig2f. Under that reading the outcome would be not reproduced. The claim stays as tested on the claims file.

**Run:** `python tools/entry.py all entries/000673-daume-2024` passed with 0 check errors, and all four notebooks ran (3.1, 42, 21 and 9 minutes). The re-run printed the same numbers the record quotes.

The README still says the 42-minute LFP notebook is "over the 30-minute limit". The working tree's `tools/entry.py` already had that limit raised to 60 minutes before I started; I left that change and the other `tools/` edits alone. Nothing is committed.
