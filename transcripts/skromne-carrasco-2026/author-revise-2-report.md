I've answered the round-2 report. No outcome changed and nothing is proposed: the counts stay at 18 reproduced, 6 partially reproduced, 3 not reproduced and 5 blocked. The verifier agreed with all 32. The full re-run passed (main notebook 35.3 min, `decoding.ipynb` 40 min) and `entry.py check` reports 0 errors. Nothing is committed.

**Fixed and added**
- **`assumed` flags:** now set on edf2-no-registration-confound, edf4ij-pv-decay and edf1h-ring. The notes, conclusions and Summary say what each outcome rests on:
  - edf2 rests on reading "all cells" as every CellReg score. With score > 0.8 only it would not reproduce.
  - edf4ij rests on HDI computed from the smoothed curve. With raw HDI, mouse 5's mean at the longest interval is 0 or below.
  - The edf9 Summary row now names its assumptions where it used to say "no".
- **Negative CellReg scores:** the data check now prints CellReg scores below 0. There are 102 of 5,190 rows, down to −1.24, which a CellReg score cannot take, so I added it as a new finding. edf2 now drops these cells. That removes two cells under raw HDI (106 cells, absence-test p 0.084 to 0.24); the main reading had none and is unchanged.
- **fig2g, new control:** I added the shuffle the verifier asked for, which keeps which cell pairs are present and permutes only the correlation values. It gives 0.59 against 0.64 for the data, lower in 5 of 5 mice (W 15, p 0.031). So the correlations add a little beyond the presence pattern. Presence alone still reaches 0.70.
- **Stale or wrong sentences, all corrected:**
  - fig1k figures now match this run: 2.56 s per fit, 80 min for all pairs and 51 min for the partial reading, plus the loading time.
  - The README run times are updated and `entry.yaml` runtime_minutes are now 41 and 40. Main cell 2 now points to the printed loading time.
  - The Summary and the HD-rule `methods_unavailable` finding now list fig1f and edf4ij among the claims raw HDI affects.
  - The shuffle-median sentence now says unsigned shuffle medians (39 to 57 degrees) are close to the paper's 51 to 57, while signed ones give 72 to 90.
  - The edf7 medians are now "one third to one half" of the paper's.
  - Cell 10 now says edf1h uses smoothed HDI only. I also corrected a claim there that raw HDI is closer to the paper's 72 cells: the 72 lies between the two readings (49 and 106).
- **Record:** round 2 is under `verifications`, with all 32 results marked as agreeing, the verifier's reasons and my responses.

**Not done**
- I added nothing to `questions/001676.yaml`, because the verifier found no place where the claims file misreads the paper.
- I copied the edited text cells into the executed copies so they match the source. The code cells were already identical, so the printed outputs are from this run.
