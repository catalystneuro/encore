I've handled every point in the round-1 report, re-run the entry, and recorded the round under `verifications`; nothing is committed. `entry.py all` still stops at its check step with 18 errors. All 18 are on the old `-01` record, which I left as the protocol says, so I ran the `run` step separately. The notebook passed from a clean environment in 461 s with no errors, and every conclusion now matches the new numbers.

**Outcome changes**
- **`grid-phase-orientation`**: changed from partially reproduced to blocked, methods_underspecified, for the verifier's reason. The criterion only names "reproduced", and both parts hold in every layer under 88 of 224 readings, not all. Under the claims file's rule that disagreement blocks the claim. The notebook's outcome line, conclusion, summary and the README now say this.
- **`speed-slope-steeper` and `speed-intercept`**: kept blocked. The verifier would call them partially reproduced and not reproduced. Both list `speed` under `depends_on`, and the protocol blocks a claim that depends on a blocked claim. The disagreement is recorded in the notes and under `verifications`.
- All other outcomes are unchanged, and the verifier agreed with them.

**Added or corrected**
- **Gridness control (problem 3):** I shifted each cell's spike train in time and recomputed gridness. 29.7% of the shifted maps have gridness above 0, against observed 0.634, 0.559, 0.314 and 0.359 in layers II, III, V and VI. So in layers V and VI the observed fractions are barely above chance. The outcome still rests on gridness above 0, as the claim says.
- **Each cell counted once (problem 4):** I repeated `layer2-grid` (all 56 readings and per rat), `hd-layers`, `deep-hd-conjunctive` and `hd-colocalized-distributed` with each (rat, depth, hemisphere, name) counted once. No outcome changes. In the ensembles, 92 of 225 cells also appear in another ensemble.
- **Rat 11265's two files (problem 2):** these hold every layer II head-direction and conjunctive cell. Their tracking looks normal: median LED separation 3.7 and 3.9 cm (4th and 6th smallest of 71 files), and fewer than 0.05% of samples have the LEDs more than 15 cm apart. Without them layer II has no such cells, which would make `hd-layers` and `deep-hd-conjunctive` partially reproduced. That variant picks files after seeing the result, so it does not decide the outcome.
- **New finding:** two other files, `11265_ses-09020601` and `11278_ses-31080502`, have the LEDs more than 15 cm apart in 71% and 62% of samples, so head direction there is doubtful. Leaving them out changes nothing in layer II.
- **Speed sign test (problem 5):** it now counts in the outcome. The head-direction count fails it in 2 of 448 rows, so the split becomes 119 reproduced, 325 partially reproduced and 4 not reproduced. The outcome stays methods_underspecified.
- **Electrodes table:** it has one row per file, location "MEC", and no coordinates, so `data_missing` stands for the two dorsoventral claims. The cue-rotation section now notes that every circular file spans 200 cm.
- **Other points:**
  - Every tested claim now prints its outcome (problem 9).
  - Pairs of cells from different layers are counted: 20 of 487 (problem 6).
  - The smoothing across the join between trials is recorded as a deviation (problem 8).
  - The rescaling caveat is added to `speed-intercept` (problem 7).
  - Stale counts in the old conclusions are corrected (for example Kruskal-Wallis 45 of 116, not 43).

**Not done**
- I did not change the position smoothing to stop at the trial join. The verifier marked it as not affecting a conclusion, and changing it would shift every number; it is recorded as a deviation instead.
- I did not test whether the rescaled positions explain the low rates at 0 to 3 cm/s.
- I could not establish which LED is the red one, because the files don't say. This stays a finding.
