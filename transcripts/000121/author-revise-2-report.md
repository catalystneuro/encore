No outcomes changed and none are proposed. The verifier agreed with all 20 outcomes, and nothing in the new outputs calls for a change. The entry passes `python tools/entry.py all` (0 errors, notebook runs in about 8 minutes). I ran it a second time after the last text edits, and the numbers were the same both times.

**Outputs added**
- **Trials per distance (cell 41):** it now prints the trial count per distance within each task and session: R 152 to 182, J 106 to 164.
- **Fig 4d inset comparison (cell 73):** it now compares the distance error against arc errors limited to the 4 cm ring's range, as the inset does.
  - The full-activity error is still lower than every ring's arc error (p at most 3.1e-05).
  - After projection onto the plane, the error matches the arc error for J's 4 and 8 cm rings (p = 0.46 and 0.11). It does not match J's 12 cm ring or any of R's rings.
  - So the part of the claim that projection brings the error "to the level of the direction errors" holds for 2 of 6 rings with the limit, and 1 of 6 without it. Cell 74 and the record's notes now say this.
  - The outcome stays reproduced because the criterion is met.

**Text corrected**
- **plane-timecourse (cell 36 and the notes):** they now say that by the letter of the criterion the result is reproduced, and that partially reproduced is a judgment beyond it. "J's times are robust" is gone. They now say both monkeys' times depend on the threshold: J falls outside tolerance at thresholds 0.8 (150 ms) and 0.05 (390 ms), and R's variant convergence of 310 ms is also outside tolerance.
- **Cell 39:** "p at most 3.0e-21" is now 3.1e-21.
- **Cell 42:** the unsupported "110 to 180 trials per distance" is replaced by the ranges cell 41 now prints.
- **Summary and the electrode_group finding:** "no target signal" now reads "almost no target information in the decoding", and both mention that 40 of 96 channels of R's labelled array regress on target position when sessions are pooled.
- **delays-and-times notes:** they now say only R's mean (340 ms against a bound of 342 ms) is just inside, and J's 342 ms is well within tolerance.
- **Round 2 under `verifications`:** recorded for all 20 claims, with the verifier's reasons as written in its report and what I changed under `response`.

**Not done**
- **pca-variance:** no change, since the verifier said nothing more was needed.
- **Unsettled questions:** the horizontal/vertical swap and the paper's trial subsets cannot be settled from the available data. They are recorded as such.
- **Stray files:** the working tree has untracked files I did not create: `.bashrc`, `.bash_profile`, `.profile`, `.zprofile`, `.zshrc`, `.gitconfig`, `.ripgreprc`, `.mcp.json`, `.idea`, `.vscode` and `scripts`. The workflow should leave these out when it commits.
