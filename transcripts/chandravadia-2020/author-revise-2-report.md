I went through every point in the round-2 report. The verifier agreed with all 25 outcomes and none changed: 10 reproduced, 10 partially reproduced, 4 not reproduced, 1 blocked. Nothing needed a `proposed` change. I re-ran the entry with `python tools/entry.py all entries/chandravadia-2020`: the checks pass with 0 errors and the notebook runs in about 170 s. Every conclusion now matches the new outputs.

**Outputs added where the verifier said a sentence had nothing behind it:**
- **Isolation distance and SNR (units-table):** the notebook now prints which files hold the extreme values. All 11 infinite SNR values are in H28_48. The two isolation distances above 1e6 are 2.9e27 (H21_38) and 8.1e32 (CS26_66), so "two values above 1e27" was true and is now shown.
- **Missing encoding images:** the notebook now prints each short session's variant and the variants of the files that hold its missing old images. They are always the same variant, so that statement is now supported. The summary now gives 21 to 24 missing images for the seven sessions and 1 for session 123.
- **Reference time:** `nomem.py` now reads `timestamps_reference_time`, and the notebook prints that it equals `session_start_time` in all 87 files, with one example of a file using Unix time. This backs the session-dates finding.
- **Duplicated recognition data (fig5c-auc-all):** the hard-coded "none" is replaced by a check over every pair of the 87 files. No pair shares recognition onsets, or the same sequence of images and answers.

**Corrections:**
- **Stimulus duration:** "1 s in most files" was wrong. Only 43 of 87 files have a median near 1 s (0.95 to 1.05 s), and 44 are above 1.5 s. The text now gives these counts.
- **Clock check:** the text now says trial and spike times are consistent with one clock, and that for 5 small files the check cannot establish it.
- **A bug I found while adding the duplicates check:** three time comparisons used numpy's default relative tolerance. For times stored in Unix seconds that allows about 15000 s, and the first run wrongly reported CS51_119 and CS51_120 as having identical recognition onsets. They now compare within 1 ms. The earlier printed results of the existing checks did not change.
- **Wording:**
  - The 287 from the two papers' totals is now "within 1 of the paper's 288".
  - The README and summary now say the code's choices give 25 dual cells against the paper's 26, not "the paper's numbers".
  - The fig3 discussion no longer says the T103 unit fits the figure's cell number. It fits only if counted from 1, while the Figure 4 unit fits only if counted from 0.
- **Claims-file reading:** the fig4 criterion reads the figure's "cell number 4" as "electrode row 4". I added this as a question for a reader in the new file `questions/chandravadia-2020.yaml`, which also names the fig3 claim. The claim itself is unchanged.
- **Record:** round 2 is recorded under `verifications` with the verifier's reasons and my response for each of the 25 claims.

**Not done:**
- `helper.dynamic_split` is still unchecked against the paper's code. The verifier says only the fixed split decides that claim.
- The per-unit p-values cannot be compared with the paper's code output, because that output isn't available.
- The verifier said its round-1 point about how spike-time units were checked had been filed under session-dates instead of units-table. I left that round-1 entry as it was recorded, since the verifier said its content is right.

Nothing was committed or pushed.
