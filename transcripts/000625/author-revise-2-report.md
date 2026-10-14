No outcomes changed. The verifier agreed with all 28 in round 2, and all 28 are kept. I re-ran `python tools/entry.py all entries/000625-geiller-2020` twice, and both runs passed with 0 errors. The numbers that were already in the notebook are unchanged, and every conclusion now matches the new outputs.

**Outputs added to the notebook**
- **fig2c-most-positive (cell 20):** the smoothing and stated-clock variants now also show the fraction negative among the six subtypes, averaged and per session. The averaged value is 0.095 for every smoothing width. Per session, smoothing changes a fraction by at most 0.014.
- **fig4-fraction-negative (cell 41):**
  - It now prints the negative-field rate among ROIs that have a positive field: 0.784.
  - It now runs the rule on synthetic cells, using the real position from one session. A cell with only a positive field is also flagged negative. A cell with only a negative field is flagged positive under the rule without the peak, but not under the peak rule. This puts the coupling itself in the notebook.
- **fig4f-selectivity-no-difference (cell 47):** it now prints the tuning-curve minimum, mean and maximum for the selected subtyped cells (medians 0.158, 0.205 and 0.255 dF/F). It also prints the selectivity index after subtracting each curve's minimum: the median rises from 0.016 to 0.307.

**Text corrected (notebook, attempt record, README)**
- **fig2c-most-positive:**
  - The six-subtype reading passes only because the correlations are averaged over sessions. Per session it gives 0.055, 0.143 and 0.164, all outside the range.
  - I removed the statement that the all-ROI reading fails because of averaging. That reading is in range only in session 21322.
  - The smoothing sentence now covers both readings.
- **fig4-fraction-negative:**
  - The text now says the 55.8% and 10.6% use the positive rule without the peak. With the peak rule, the same variant gives 65.3%.
  - The coupling explains only part of the 66.4%: 37.7% of ROIs without a positive field still have a negative field, about 3.5 times the surrogate rate.
  - The negative-only variant leaves out real negative cells that get flagged positive.
- **fig4f-selectivity-no-difference:** the unsupported "baseline near 0.12" explanation is replaced by the new numbers. The text now says the test compares near-flat curves and has little power.
- **Summary table:** the fig2c and fig4-fraction-negative rows are updated to match.
- **README:** the blocked row now counts 11 claims, and fig4e-bic-recurrence (3 BiC, too few) has its own row.
- **Round-1 reasons:** these now include the two pieces of the verifier's evidence the record had left out. Those are the AR-noise false-positive rates (0.22 positive, 0.20 negative) under fig4-fraction-spatial, and the synthetic coupling test under fig4-fraction-negative.
- **Round 2:** recorded under `verifications` for all 28 claims, with the verifier's reasons and my responses.

**Not changed, and why**
- **fig4e-bic-recurrence:** I kept the blocking reason as "other". `docs/protocol.md` step 1 gives "too few units under the claim's own rule" as an example of "other", and the criterion needs 5 BiC where the data hold 3. The verifier's round-1 view that it should be "data_missing" stays on record.
- **s2-lags "0.82":** left as it is. It quotes the verifier's own round-1 wording, and 0.816 rounds to 0.82.
- **ROI identity across sessions and session order:** neither can be resolved from the files. Both are already stated in the notes, deviations and findings.

There are untracked files in the repo root that I did not create (`.bashrc`, `.bash_profile`, `.profile`, `.zprofile`, `.zshrc`, `.gitconfig`, `.ripgreprc`, `.mcp.json`, `.idea`, `.vscode`, `scripts`). I left them alone, so the workflow should not commit them along with these changes.
