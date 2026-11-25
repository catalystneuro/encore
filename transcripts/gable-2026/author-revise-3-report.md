The verifier agreed with both proposals in round 3, so two outcomes changed and no proposals remain open.

**Outcomes changed:**
- `figs4-lowest-couplers-correlated`: partially reproduced is now blocked (`methods_underspecified`). The effect is significant under all 16 readings, but `bba` puts its size inside tolerance (0.0548, against a lower edge of 0.054) and `baa` does not (0.048). Those two readings differ only in O2, the firing-rate measure.
- `figs4-high-couplers-correlated`: partially reproduced is now blocked (`methods_underspecified`). With units counted once, `baa` gives not reproduced and `bab` gives partially reproduced. Those two differ only in O3, the trial set.

For both claims I removed `proposed` and updated the notes. I also removed `assumed: true` from both. The verifier found that blocked holds whichever reading is taken, including either handling of the units stored twice, so the outcome no longer rests on an assumption. You only asked me to change `outcome` and `blocked_by`, so put the flag back if you want it kept. No other outcome changed.

**Other changes:**
- **Notebook:** the conclusion cells for both claims, the method note, and the summary table now say blocked.
- **README:** the claims table and the paragraph on the earlier reading now say blocked.
- **Attempt record:** round 3 is under `verifications`, with one result for each of the two claims. Each gives agrees: true, outcome blocked, the verifier's reason in its own words, and my response.

`python tools/entry.py all entries/gable-2026` finished with 0 errors, and the notebook passed in 211 s. Nothing is committed.

Some untracked files I did not create are in the working tree (`.bashrc`, `.profile`, `.idea`, `.vscode`, `scripts` and others). I left them alone; they should probably stay out of the workflow's commit.
