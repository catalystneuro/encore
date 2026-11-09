I've worked through every point in the round-2 report. No outcome changed and none is proposed. I re-ran the entry with `python tools/entry.py all entries/001882-yuan-2025`: it passed with 0 errors, `check` passes, and every number came out the same as before.

**Outcomes**
- **table3-destabilizing:** still not reproduced, but now marked `assumed: true`. It rests on the claims file's reading that iMutant is run from sequence, which the paper never states. That dependence is now written in the cell 71 result, the notes, a new assumption deviation, the summary and the README. I asked a reader about the possible misreading in the new file `questions/001882.yaml`; the claim itself is unchanged.
- **The I-Mutant sign disagreement covers three variants, not two.** The re-run shows the regression and the classifier also disagree for p.Leu740Phe (+0.19 against "Decrease"), as well as p.Cys1019Tyr and p.Leu249Phe. The text now names all three.
- **m73-vmd-phenotype:** I removed its `assumed` flag, because it is partial under every reading. The notebook, summary and README no longer say it rests on the assumption; only m73-f57-similar-lesions does.

**Corrections and new output**
- **`desktop.ini` count:** corrected from six to five in cells 0 and 10, the summary and the finding. Cells 3 and 9 now print the count.
- **Draft assets:** cell 3 now compares the draft with the published version. They have the same 13 paths, sizes and asset ids.
- **UniProt versions:** cell 61 now prints the release dates. Both pinned versions came out on 2 October 2024 and were replaced on 27 November 2024, so they were current on the paper's access dates.
- **gnomAD version:** the API reports no release number, so it can't be printed. The text now says v4.1 comes from gnomAD's documentation, not from an output.
- **Word document against Table 3:** the summary and finding now say it holds 23 of the 25 values. Three differ by more than 10% and three more differ within 10%, including DUET p.Leu249Phe, which was missing before.
- **Background discs:** the description now says they sample the perimacular ring, not the general fundus. This is fixed in cells 42, 49, 50 and 56, the summary, the README and all five FAF deviations.
- **Table 1 claims:** the four Table 1 claims now carry a deviation saying they show the deposit agrees with the paper, not independent evidence. The notebook and README say the same, and the round-1 record now gives that point in full.
- **Rounding:** the m75 value 0.89 is now 0.90.
- **Round 2 record:** added under `verifications`, with the verifier's agreement, outcome, reason and my response for all 26 claims.

**Not done**
- I-Mutant's structure mode was not run, because the I-TASSER models it needs are not deposited.
- ExPASy's own pI code was still not run; the verifier said this does not affect a conclusion.

Nothing has been committed. The repository also shows untracked dotfiles and folders (`.bashrc`, `.idea`, `scripts` and others) that I did not create, and I left them alone.
