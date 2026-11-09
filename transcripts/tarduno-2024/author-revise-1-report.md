I've finished the round-1 revision. The entry re-runs cleanly (`tools/entry.py all`: 0 errors, notebook passes in 25 s), and `tools/entry.py check` passes on the final versions.

**Outcome change**
- **example-14053g1-threshold:** changed from reproduced to partially reproduced, as the verifier suggested. The criterion counts the claim as reproduced only when the example matches for 14053g1 as written. Here it matches only if the crystal name is a misprint for 12040g1, so I recorded it as a partial match. I updated the notes, the result cell, the summary and the README.
- All other outcomes stay as they were, and the verifier agreed with each of them.

**Outputs added to the notebook (the verifier asked for all of these)**
- **table2-fit-statistics:**
  - Per-step replicate scatter for ss9, ss10 and ss6.
  - The score with one pTRM reading held fixed: 14 to 19 of 29 (48 to 66%), partial or lower under every reading.
  - The score with ss6 counted as a miss: 22 of 29 (76%).
  - None of the nine specimens is from a synthetic sheet, so dropping those sheets changes nothing here.
- **Two-cluster steps:** a scan of every glass step found 11 steps in 7 sheets whose replicates fall in two direction groups more than 45° apart, the way ss6 250.1 does. Nine of them are inside a Table 2 range. This is now in the deviations and a finding.
- **fig2-changing-field:**
  - How often readings (a) and (b) hold when there is no changing field: (a) 61 to 96%, (b) 51 to 57%. Both are weak tests.
  - An Arai curvature from a circle fit. It does not tell ss41 and ss22 apart from ss19 and ss43, which the paper presents as linear. The "curved" part of the claim is reported but not judged.
- **no-alteration-recording-efficiency:**
  - TRM40/TRM20 without the factor of 2: it ranges from 1.54 to 2.35, and three crystals are above 2.
  - The 590.0 replicate moments per crystal, which show the null state sits above the 8e-11 emu threshold.

**Other corrections**
- I updated the notes and deviations for table2-fit-statistics, fig2-changing-field and no-alteration-recording-efficiency.
- I added the two-cluster steps to the finding on repeated measurements.
- The summary now says the Table 1 maximum intensities rest on a threshold that is below the null level.
- Round 1 is recorded under `verifications`. All 17 claims are listed with the verifier's reasons in its own words and my responses.

**Question for a reader**
I created `questions/figshare-24639285.yaml` with one question on no-alteration-recording-efficiency. The criterion's text says the 40 µT TRM should be "about twice" the 20 µT TRM. But its cutoff only fails a crystal when the 40 µT TRM is more than four times the 20 µT TRM. With a cutoff of 2 on TRM40/TRM20, three crystals fail and the claim would not pass under either reading. I left the claim unchanged and tested it as the claims file has it.

**Not done**
- I kept the outcomes for problems 2 to 8, since the verifier said none of them affects a conclusion. Their analysis is now in the record.
- Comparing against Figures 1 to 3 and the deposit's supplementary PDFs is still out of reach: no figure PDF was supplied, and the PDFs were not read in this revision.
- `git status` shows untracked `.bashrc`, `.idea`, `scripts` and similar entries in the repo root. They are `/dev/null` device mounts from the sandbox, not files I created, and I left them alone.
