No outcome changed and none is proposed. The verifier agreed with all 36, and the round-2 analysis turned up no reason to change one. The tally stays at 23 reproduced, 2 partially reproduced, 2 not reproduced and 9 blocked. The final re-run of the entry passed its checks, and every conclusion matches the new numbers.

**Corrected**
- **fig3supp-doi-iti-slower-than-odor:** the fitted-clock difference is now −3.57 cm/s in the record and −3.6 in the result cell (they said −3.54 and −3.5).
- **HTR timecodes (cell 13 and both timecode findings):** the stored times are early by up to 0.2 s, not "late or early". The code's times are early by up to 0.9 s, which is 0.7 s earlier than the stored times.
- **fig5e:** the rate peaks at 6.76 HTR/min in the 800 px bin and is 5.65 in the last bin, at 1100 px (it said "about 6.5 at the odor end").
- **README:** it now says the fitted clock is good in 30 of 44 sessions.
- **Record:** all nine blocked Figure 2 outcomes now have `notebook` and `output` fields.

**Added**
- **Question for a reader on fig1c:** `questions/001863.yaml` now asks whether the criterion should also require the 25–30 min bin, which the paper's sentence covers. The claim's notes say it is asked. It would not change the outcome: that bin gives p = 0.018 with saline higher.
- **Checks for the two not-reproduced speed claims (fig3c, fig3d), in a new notebook cell:**
  - **The test itself:** R isn't installed here, so R was not run. Instead the exact signed-rank p was recomputed by counting the null distribution directly, and it matches our implementation (0.0634 and 0.0794).
  - **The cleaning:** I fetched the authors' `CleanTracking` from their repository at the cited commit. Our tracking cleaning matches it line for line.
  - **Sensitivity to the cleaning thresholds:** the outcomes depend on them. The cleaning interpolates about 80% of nose frames. A likelihood cutoff of 0.90 gives p = 0.013 within trials and 0.043 in the ITI, both under 0.05, while 0.99 gives 0.13 for both.
  - **Why the outcomes stay:** the Methods state 0.95 and 8 px, and the claims were tested with those values, so no change is proposed. The notes and result cells now report this dependence.
  - **Helper change:** to run these variants, `clean_nose` now takes optional threshold arguments. Its defaults are unchanged.
- **Round 2 under `verifications`:** all 36 claims, with the verifier's reasons in its own words and my responses.

**Not done**
- **The trial-table clock:** I can't settle which clock it is on from the data. The question is already put to the authors in the record, and the outcomes follow the claims file's clock.
- **R itself:** R is not available in this environment, so the exact-distribution check above stands in for running it.
