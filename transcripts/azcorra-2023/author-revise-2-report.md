No outcome changed: the verifier agreed with all 29 in round 2, and nothing in the re-run gave a reason to propose a change, so nothing is under `proposed` and no third round is needed. I re-ran the entry with `python tools/entry.py all entries/001038-azcorra-2023` after the edits. It passes in 2.3 min, `check` reports 0 errors, and every number the conclusions use is the same as before.

**Corrected statements** (report items 1 to 9)
- **Summary (cell 93):** the Calb1 trough lag with the code's timing (0.160 against 0.17 s) is now described as within tolerance, not equal. The "response means to the decimal" claim now covers only the reward means and the Vglut2, Calb1 and Anxa1 air puff means. It also gives the DAT air puff mean (2.46 against 5.3) and the DAT reward-size difference (1.83 against 1.9).
- **code_mismatch finding** in the record is narrowed the same way.
- **fig4g-reward-response:** "the paper's numbers come from the code's windows" is now an inference ("suggests"), and the text says it fails for the DAT air puff mean.
- **ed6f-dec-peak-timing:** cell 40 now also prints the mean, skewness, the paper's tolerance and the counts above and below it. The conclusion now says:
  - Vglut2 is later as a whole: 31 of 50 recordings peak after 0.385 s, and the cause is not found.
  - Calb1's gap comes from a right tail: skewness 1.48 and 13 of 28 recordings above 0.253 s, while its median of 0.25 s is within tolerance.
- **ed8f-rest-reward-same:** all the count differences are now listed (Calb1 8/10, Anxa1 36/42, DAT 33/42, plus the mouse counts). Cell 61 now prints the paper's mouse counts. I also added the omitted Anxa1 and DAT counts to the round-1 reason, using the verifier's round-1 wording.
- **fig3a-overlap-locomotion:** "the same mice" is replaced: Calb1 has 4 mice as in the paper, Anxa1 has 6 against 5, and the counts cannot show whether the mice are the paper's.
- **recording-counts-locomotion:** the claim that the excess is "spread over every split" is removed. The paper gives no per-split counts, so where the excess lies cannot be measured. The text now notes that every Anxa1 recording is from a dual-fiber file and every Calb1 recording is labelled DS.
- **Run time:** the README and cell 0 no longer say "about three minutes"; the run time is printed at the end.

**Outputs added** (report item 10)
- **Cell 13:** the number of values per fiber in `normalized_fluorescence` (two values in 123 files), and the related-resource links and asset summary of both the published and draft versions. This shows the malformed DOI link in the published version and the generic asset-summary fields.
- **Cells 46 and 73:** the paper's conflicting reward P-values and its two sets of Extended Data Fig. 9k percentages. I checked these against the paper's PMC full text, which I saved under `paper/`. That folder is gitignored, so the text is local only.
- **New helper:** `version_metadata` in `azcorra.py`, which cells 13 uses.

**Recorded:** round 2 under `verifications`, with each of the 29 claims' agreement, outcome, reason in the verifier's words, and my response. The two points not tied to any claim are answered in the round's `reviewed` text, since the schema has no round-level response field.

**Not done**
- The causes of four remaining differences are still unexplained:
  - the locomotion overcount;
  - the Vglut2 peak timing;
  - the DAT air puff mean;
  - the count mismatches in fig4i, ed8f and the SNc selection.

  I found no new analysis to explain them, so the record says the cause is not found.
- I did not commit, as instructed.
