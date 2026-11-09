No outcome changed in this round, and none is proposed for change. The entry re-ran cleanly with `python tools/entry.py all` (pass, about 53 minutes), and every number the conclusions cite came out the same as before. Nothing is committed.

**Outcomes now marked `assumed: true`**, each with a deviation saying what was assumed and why:
- **Which evoked recording (E) is used:** fig4a-lognormal, fig4-median, fig4bc, supp4, fig5a-evoked and fig5cd now rest on E being the first 10 minutes of the 1-hour recording. The deviations say that the 10-minute 40 kHz recording cannot be tested, because it has no sorting. The basis for the assumption: the deposited sorting matches E's ground truth (250 units) and not the 40 kHz recording's (0), and it reproduces the code's printed 0.655. I added a `methods_unavailable` finding that asks the authors to confirm this. The verifier listed fig4-median, fig4bc and fig5cd; I added supp4 myself, because its deciding comparisons include E.
- **Using "partially reproduced" when the tested parts hold and the rest cannot be tested:** this is now stated as an assumption on fig4-median, fig4bc, fig5a-single-unit-fraction-differs, fig5a-single-unit-counts and fig5b. Each deviation says the claim would otherwise be blocked, and for what.

**Outputs added to the notebook:**
- **DS3 lag scan:** it now covers every sorter against all three dense probe ground truths. No sorting rises more than 0.011 above its median over lags.
- **fig5a-single-unit-counts:** the H against DS test, for every number of single units that depth 1 could add. It stays at p ≥ 0.05 if 37 or fewer of the 81 missing units are single, and drops below 0.05 from 38. The paper's own total gives p = 0.177. So this test is recorded as undetermined, and "the fractions do not differ" is withdrawn.
- **Reference values using the paper's NS-2X counts:** the three-way test gives p = 0.33, and fraction readings (ii) and (iii) give 0.367 and 0.405. These use the paper's numbers, not the dandiset's, and decide nothing.

**Text corrected:**
- **fig6gh:** the measured value is now 9.98 (Kilosort2.5, 1 hour), not 8.07, and the notes list all the ratios, including 13.3 for Kilosort over 10 minutes.
- **fig3e:** the electrode counts per distance band now match what cell 39 prints.
- **DS3 statements:** the notes, finding, cell 9, the Summary and the round-1 response now say exactly what was scanned.
- **Cell 78:** it now says the tags are computed over every sorted unit.
- **Cell 93:** "weights close" is replaced with the actual differences.
- **fig5b:** the notes say that only DS's theoretical yield stops a full reproduction.
- **README:** it now states both assumptions.

**Recorded:** the round-2 entry under `verifications` covers all 39 claims, with the verifier's reasons and my responses. The verifier's point that the claims file may misread the code's "npx_evoked … 10 minutes" (it may mean the sorted length) is added to `questions/001250.yaml`. The claims file itself is unchanged.

**Not done:**
- No outcome was changed to blocked. The verifier said it would accept "partial" for these claims once the convention is stated as an assumption, so I recorded it as agreeing with those outcomes.
- The untracked dotfiles at the repository root were already there and are not part of this work.
