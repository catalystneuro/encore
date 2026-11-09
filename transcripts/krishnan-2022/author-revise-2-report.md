No outcome changed. The round-2 verifier agreed with all 41, so the record still has 9 reproduced, 8 partially reproduced, 14 not reproduced and 10 blocked, and nothing is listed under `proposed`. I re-ran the entry with `python tools/entry.py all entries/000462-krishnan-2022` after the last edit: 0 errors, the notebook passes, and all existing numbers are the same as before. Nothing is committed.

**Outputs added (the report's "shown in no output" points):**
- **Old reward zone:** the lick stops under the first version's zone are now printed. They are the same as under the main zone in every mouse for L1 to L3, so "changed no lick stop" is now backed by an output.
- **File metadata and offset:** a new cell after the data checks prints, for every file:
  - the indicator ("GFP", while the imaging plane's own description says GCaMP6f);
  - the shared session_start_time and the age P12W;
  - the session description, "Reward expectation extinction", which the 4 DREADD files carry too.
  It also prints dF/F for each DREADD file with and without the offset. Keeping the offset makes dF/F 8.0 to 12.1 times smaller, and the finding now gives that range in place of "about ten times".
- **NR6 cut to 24 R laps (the paper's code):** NR6 still fails fig2a under every reading, so fig2a stays at 0 of 2 mice. I did not compute NR6's Figure 2 and 3 field values on those 24 laps, because that needs the field search re-run from the raw data. The notes and the record say so.

**Text corrected:**
- **Field width:** "about twice as wide" is now "1.1 to 1.7 times" in the README and the fig3b-width deviation, with the numbers.
- **Turnover:** the notebook and the notes no longer say every count is outside tolerance. They now name the two new-RR counts that fall inside (0 to 50 cm, and 100 to 150 cm under L1 and L2), and the paper's percentages read 21 to 28%.
- **Candidate regions:** the finding and the Summary now give 31.4 to 43.2 cm, narrower than the paper's 53 to 61 cm. They had said "31 to 41 cm, close to the paper's widths".
- **Smaller fixes:**
  - fig2a's RR probabilities now read 0.02 to 0.33.
  - The supp18 cell now gives half the DCZ drop as 0.068.
  - The timing cell now says the paper's 7.34 s is below both mean lap times, and names the 3 mice whose running time is below it.
- **Missing deviations, now added:**
  - the reward-zone assumption to fig1d, fig1g, supp6b, disengaged-laps-uniform and every Figure 2 to 4 outcome that uses RE low;
  - the volts-to-cm assumption to the place-field outcomes;
  - the sub-014 realignment to supp16, supp18, fig4h and fig4m.

**Record and questions:**
- **Round 2:** recorded under `verifications`, with the verifier's reasons in its own words and my reply under `response`. Both rounds now say that their cell numbers refer to the notebook they reviewed, since two cells have been added since.
- **fig4m question:** the existing reader question now notes that the change after DCZ is itself positive (+2.1). I added no new question, because the report found no new misreading of the paper.

**Not done:**
- **Engagement split:** the report's main remaining concern was the split. It finds 46% of RE low laps engaged against the paper's 70%, which leaves 2 mice for Figures 2 and 3 against the paper's 3. The claims file requires this reading of the Methods, so I left it as is. The record states it as an assumption, and the approach-ratio question to the authors is filed.
- **Still open, with questions to the authors already filed:** why laps take longer than the paper's, and the dF/F, transient and field rules behind the wide fields.
