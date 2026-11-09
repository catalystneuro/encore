I've revised the attempt after the verifier's round-1 report and re-run the entry: `python tools/entry.py all` passes in 133 s with no errors, and every number quoted in the conclusions matches the new run. The record now has 4 claims not_reproduced and 31 blocked.

**Outcome changes (the verifier's three disagreements, all adopted)**
- **subjects**: partially reproduced → not_reproduced. The counts are still 6 and 6 (paper: 16 and 12) under every reading, but the "none extra" condition fails:
  - every S1 file lists a 64-channel A1x64-Edge probe (or H9), where the paper used 32-channel probes;
  - two rats (BH648, BH658) are in both groups, though the paper's AC rats are "another group";
  - none of the 10 rats in the two groups is in dandiset 000946, the repository the paper names.
- **fig4-unit-counts**: blocked → not_reproduced. A typed count can't exceed the untyped count of its area and condition. With the claims file's 5 V sessions plus every 2025 file, at most 4 of the 8 counts can be within 10%; a partial result needs 6. Each now has its own notebook section.
- **fig5-unit-counts**: blocked → not_reproduced, the same way: at most 3 of 8.

**Corrections and added outputs**
- The main unit-count table is now the 5 V files plus every 2025 file, with all voltages as a variant. The notebook now states that the 2025 files give no voltage and are all kept, which can only raise the bounds.
- Subject counts now take a session's areas from units with more than 2,000 spikes, with every unit as a variant and another variant that leaves out 2025 (counts 2 and 0).
- **2025 trial timing**, as the verifier asked:
  - Trial tables and spikes cover the same times (both end near 1,250 s), except four sham files whose spikes stop early.
  - Over lags of −60 to +60 s, spikes peak within 0 to 400 ms of the trial start in only 4 of 108 stimulated 2025 files, against 39 of 92 in 2024. No other lag fits.
  - The untyped S1 positive control found no increase in 2025, or at 3,000 Hz in the 2024 5 V files, so it can't tell missing responses from wrong trial times.
- **fig11b** stays not_reproduced, as the verifier agreed. It is now marked low confidence, and its timing and voltage assumptions are written out.
- The notebook now prints `celltype_label` value counts per file (no 1 or 2 in any of the 96 files). It also checks that the 26 files without a PD are exactly the 26 sham files.
- fig6-unit-counts and fig7-9-unit-counts stay blocked. Their notes and the notebook give the bounds: fig6 can't be fully reproduced, but 2 of 4 counts could still match, so a partial result is possible.
- I updated the header table, summary, README, entry description and findings to match, and added an `onset_correlogram` helper to `tfus.py`.
- Round 1 is recorded under `verifications` for all 35 claims.

**Not done, and why**
- I kept `data_missing` on the 17 typed-unit claims where the verifier gave `metadata_insufficient`. The waveforms the paper types from aren't in the files, and the label column holds no type to read. The disagreement is in the record.
- I added no question to `questions/001199.yaml`. The verifier reported no misreading of the paper. Its note that one way of normalizing rates (per trial) is biased low is allowed by the paper and doesn't change the outcome.

I didn't commit, and I left the existing changes in `tools/` and the untracked files at the repository root alone; none of them are mine.
