The verifier agreed with both proposed changes, so both outcomes changed and no proposals remain.

**Outcomes changed:**
- **fig2d-npx-ccg-hva-input**: reproduced → blocked (`methods_underspecified`). Seven of the eight combinations meet the criterion as written. In the eighth (boxcar smoothing, raw flank, number of connections) the two medians are both 1, and equal medians fail the "higher median" rule. I removed the tie-break assumption and its deviation, because the outcome no longer rests on them. The notes still say the effect appears in all 8 combinations.
- **fig3d-npx-areas-inference**: partially reproduced → reproduced. It meets the criterion in 5 of 6 runs. The verifier had a reservation: deciding by the majority of seeds is a rule chosen after the first seed's result. As it asked, that rule is now recorded as an assumption in the deviations. The deviation says that requiring every seed would give partially reproduced, and that averaging the scores over seeds was not computed.

**Other changes:**
- The record now has 14 reproduced, 3 not reproduced and 23 blocked outcomes, and no partial reproductions.
- The notebooks' result cells and summaries, the README table and the attempt notes now match the new outcomes.
- Round 3 is recorded under `verifications` with results for the two claims.
- Checks cell 16 had an out-of-date network timing, which the verifier pointed out. It now refers to the printed timing and gives the range seen so far: 2.5 to 4.4 ms per epoch, about 11 to 18 hours. This run measured 2.54 ms per epoch and about 10.6 h.

`python tools/entry.py all entries/000248-shin-2025` reported 0 check errors, and all five notebooks ran. The executed outputs match the values in the record: 7 of 8 combinations for fig2d, and four areas significant then five and five across the three seeds for fig3d. After the timing edit I ran the check again and it still reports 0 errors. Nothing is committed.
