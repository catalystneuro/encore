No outcomes changed and none are proposed. The verifier agreed with all 25 outcomes in round 2, including blocked (data_missing) for fig5-anxa1-dls-inhibited, which it had disputed in round 1. Every point in its report was wording. I fixed each one, re-ran the entry, and `tools/entry.py check` passes with 0 errors.

**Re-run.** `python tools/entry.py all entries/001528-hadjas-2025` passed in 425 s, and the notebook printed 6.9 min. The numbers the verifier cited came out the same:
- 2 of 6 Anxa1 DLS tests significant;
- in the variant with the unsuffixed recordings, STN 4 s W = −36 with p 0.0078;
- dual-mice t values 3.13, 3.98, 7.26, 4.72, 8.35 and 3.33.

**Corrections:**
- **fig5-anxa1-dls-inhibited (cell 70 and the record's notes):**
  - "Cannot be tested by its criterion" now reads that "reproduced" (6 of 6) cannot be reached at the deposited 5 and 4 mice.
  - It now says "partially reproduced" (3 to 5 of 6) could be reached and was not. The 2-of-6 result is shown, with PPN 4 s p = 0.13.
  - The W comparison now says the variant's STN 4 s W = −36 matches the paper; only the other two W values and the three t values differ.
- **"Exactly" changed to "closely"** in the data_missing finding and in the notes for fig5-anxa1-dls-inhibited, now stated as "p to two digits, t within 0.08".
- **Cell 0 status table:** fig5-anxa1-dls-inhibited is now "blocked: data missing (analysis shown)" where it said "tested".
- **README:** the run time is now "about seven minutes" (was five).
- **Record:** round 2 is added under `verifications` with all 25 claims. Each has `agrees: true`, the verifier's outcome, its reasons paraphrased from the report, and my `response`.

**Not done:**
- **fig3g-da-ppn-duration:** the cause of the failure is still unexplained (the paper's Friedman F of 11.5 against 4.07 here). The verifier also says nothing more can be checked from the dandiset, so the record says that and the outcome stays not_reproduced.
- **B9 and B10** (the helper-function tests and the leakage check) are still not in the record. The verifier said leaving them out is acceptable because they bear on no claim.
- **Untracked files:** dotfiles such as `.bashrc`, plus `.idea`, `.vscode` and `scripts/`, showed up untracked at the repo root. They are not mine and I left them alone.

Nothing was committed or pushed.
