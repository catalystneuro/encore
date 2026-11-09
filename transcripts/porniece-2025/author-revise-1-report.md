I've worked through the round-1 report. One outcome changed. The entry re-runs cleanly (`tools/entry.py all`: 0 errors, the notebook passes in 69 s), and the conclusions match the new numbers. Nothing is committed.

**Outcome change**
- **supp3q-hfd-ncd-weight-loss-meal-length**: reproduced (assumed) → **partially_reproduced (assumed)**, as the verifier argued. The "no neural correlation" part is a claim of absence, and under Z1 (one of the claims file's readings) mid-meal response does correlate with meal size (p = 0.039 and 0.043). The meal-length correlation also holds only under the C/B reading, which rests on my guess at what the `ad lib bw` field means. The notebook now prints the criterion for every weight-change, Z and window combination. The README, header and summary tables say partially reproduced.

**Added or corrected**
- **The 58 recordings with an inferred trial start (problem 1).** The tone itself causes a fast rise in the raw signal, in triggered and untriggered trials alike, so I used it to check where the trials sit in each raw trace (new `pvh.alignment_check`):
  - The 58 recordings behave like the 285 aligned by correlation. The tone response peaks within 1 s of the trial grid in 40 of 58, against 218 of 285; most of the rest peak 1 to 11 s later in both groups, where the consumption response is.
  - The tone response is absent in the five slots before the first trial and present in the first five trials (49 of 58, against 242 of 285), so no recording is off by whole trials.
  - Correctly aligned files also have long traces after the last trial (up to 2869 s), so a long trace does not mean a different start.
- **Rerun without those 58 recordings.** I wrapped the 20 response-based claim cells in functions and re-ran them without these recordings, in a new section before the summary. Every outcome comes out the same except **fig2c**: there HFD rises to 0.20–0.23, out of tolerance, which would make it partially reproduced. I kept it as reproduced, because the check supports the inferred starts. This sensitivity result is in the notes of each affected claim.
- **Points 3 to 7:**
  - A new comparison shows the depositors' Z-score tracks Z2 trial by trial (median r 0.935 in matched files). How it was computed is still unknown.
  - supp3m now prints which trial threshold decides (at least 30 triggered trials).
  - The notes for fig2c, fig2d, supp2fg, fig2s and fig3k now say where their passes sit at an edge or rest on one reading.
  - The MPK191 file dated 2024-01-02 is now flagged in the notebook.
- **Notes fields.** The raw notes of one first-phase and one second-phase file per diet-switch group are now printed, for the `fasted` and `ad lib bw` questions.
- **Record.** The round is recorded under `verifications`, with the verifier's reasons in its own words and my responses. I added one finding: the paper describes the diet-switch recordings as 30 of 90 triggered trials, but the dataset includes 60-trial sessions.

**Not done, and why**
- **No question added to `questions/001474.yaml`.** The 90-trial point is not a misreading by the claims file: the paper itself says "30/90", so I recorded it as a finding instead.
- **fig2km left out of the verification results.** The report gives no outcome for this claim, so I noted that under `reviewed`.
- **Points 6 and 10 needed no change.** The verifier marked both as not affecting a conclusion. The supp1cd notes already explain the division readings.
