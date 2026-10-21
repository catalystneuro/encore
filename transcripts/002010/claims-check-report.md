There's no claims file to check. `claims/002010/` doesn't exist, and nothing has ever been committed there on any branch. So I didn't run `tools/claims_check.py`, there was nothing to correct, and I wrote no `checks` entry.

**Why there's no file.** The earlier reader run (`transcripts/002010/claims-report.md`) stopped at Reader step 1 and wrote 0 claims. It said the supplement and part of the Methods were missing. I checked that against `paper/10.1101-2023.04.19.537568.txt` and it holds:
- **Supplementary Tables S1 to S18 aren't in `paper/`.** The text points to them about 60 times for its statistics ("Supplementary Table S18", "Table 15S", and so on). There's no supplement file and no PDF.
- **The Z-score equation is gone.** At line 279 the Methods say "Z-scores of the change in gait metrics were then calculated as follows:" and the next sentence starts straight after, with no equation. Every subgroup in the paper (slomo, shuffle, fast and their opposites) is defined by Z_SwT or Z_StrV thresholds, so no criterion could say how mice are grouped.
- **The legend of Figure 7-Figure supplement 3 is cut off after its title**, as the reader reported. I did not check this one.

**What remains open.** Someone needs to add the bioRxiv supplementary file (Tables S1 to S18) and the preprint PDF, so the equation can be read. After that, a new claims run can write the file and a claims-check run can check it. The paper's code (the two SourceForge projects, gait-analysis-gui and gait-emg-step-trigger) hasn't been read yet either.

**Ready:** no, since there's no file.
