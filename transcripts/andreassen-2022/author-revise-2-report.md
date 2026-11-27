No outcome changed. The verifier agreed with all 28 (17 reproduced, 2 partially reproduced, 9 blocked), and I'm not proposing any change. The entry re-runs cleanly with `python tools/entry.py all entries/andreassen-2022` (0 errors, 27 s), and `check` passes. The numbers are the same as before.

**Text corrected to match the outputs:**
- **Cell 11:** it said the hypoxia counts of Table S8 (14) and Fig. 5D (12) both hold without Fish33. It now says only Table S8's count holds without that fish; the 12 hypoxic fish of Fig. 5D include it.
- **Cell 61 (figs3d):** "the onset frames support 0.3 °C/min" is gone. It now gives the implied start temperatures (median 27.0 °C, range 19.7 to 29.0) and says they only show that 0.3 °C/min is compatible with the first medulla bins. It also says that in hyperoxia the last complete bin (0.40) is already below half.
- **Record, figs3d notes and finding 4:** the claim that the drop below half falls in the partial onset bin is now limited to normoxia and hypoxia, with the hyperoxia exception stated.
- **Notebook summary:** it no longer says "every model reproduces the estimates of Tables S1 and S3 to S10". It now says the estimates the claims file quotes are reproduced and the other terms of those tables are not compared. The figs3d sentence there is also limited to normoxia and hypoxia.

**Output added:** the cell for finding 3 (`finding-fish-ids`) now also prints where the Fish27 and Fish29 light recordings end against their onsets, and the row counts of `CTmaxData_Total.csv` (90 rows, 2 without a treatment, 12 more without a temperature). That cell now shows the whole finding.

**Record:** I added round 2 under `verifications`, with all 28 results agreeing, the verifier's reasons and my responses. It includes the verifier's correction of its own round-1 reason for fig5a: the overall-quartile variant does not pass (hypoxic mean 38.972 °C). I left the round-1 reason as the verifier wrote it. No finding is rated `critical`, so the round has no `findings` list. The verifier agreed with all the severities.

**Not done:** nothing in the report needed a new question for a reader, because it found no misreading by the claims file. No assumption was judged unreasonable, so figs3d stays `assumed: true`.

The working tree also has untracked files I didn't create (`.bashrc`, `.zshrc`, `.idea`, `.vscode`, `scripts`, and others). If the workflow commits everything, these may go in with my changes.
