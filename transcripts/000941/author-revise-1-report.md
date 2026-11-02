I changed one outcome. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, notebook passes in 57 s), and every conclusion matches the new numbers. Nothing is committed.

**Outcome change**
- **table2-movement-time** went from `not_reproduced` to `blocked` with `metadata_insufficient`, as the verifier suggested. The checks it asked for show the dataset's `move_onset_time` is not the paper's movement onset M:
  - **Movement time:** in all four monkey L sessions the files give medians of 180 to 200 ms. That is 52 to 58 ms shorter than the authors' own medians for the same sessions (238 to 255 ms, J Neurophysiol 2016, Table 2), about three times the 20 ms step of the event times.
  - **Cue to onset:** 300 to 320 ms in the files, which is 57 to 77 ms longer than the shortest median the J Neurosci 2016 paper gives for monkey L (243 ms).
  - **Cue to contact:** 500 to 520 ms, which agrees with the papers to within 4 to 25 ms. So cue and contact match, and the dataset's onset comes about 55 ms after the paper's, consistent with a later event such as release of the center object.
  - **EMG aligned on the dataset's onset:** the shoulder and elbow muscles (DLTa, BCPs, TCPlat) reach half their peak 40 ms before it, and 8 of 16 muscles reach half their peak before it. This fits a later onset, but EMG always rises before movement, so it does not decide on its own.

  The face-value 200 ms is kept in the notes. Monkeys X and Y are still missing from the dataset.

The other 25 outcomes are unchanged (all blocked), and the verifier agreed with each of them.

**Added or corrected**
- **Notebook:** a new section with the three checks above, a two-panel EMG figure, and a rewritten conclusion. The per-session medians now print as whole milliseconds (the verifier had flagged floating-point residue). There is also a note that the "preceding trial number present" approximation drops more trials than the paper's rule would, since many absent trial numbers are probably trials held back in other benchmark splits. Header and summary tables are updated.
- **Attempt record:** new notes and deviations for table2-movement-time, and the finding on undefined event times now says the onset is not the paper's. The round is recorded under `verifications`, with 26 results quoting the verifier's reasons and my responses.
- **README and `entry.yaml`:** updated to match. Since no outcome is now `not_reproduced`, I removed the "failure to reproduce" sentence from the README and the notebook summary, as the protocol requires it only when one is.

**Not done**
- I added no question to `questions/000941.yaml`: the verifier reported no place where the claims file misreads the paper.
- The verifier's remaining points were marked as not affecting a conclusion: the object naming, the archive check, the duplicate-data and clock checks, and whether the evaluation trials held back from DANDI would complete the session. They needed no change.
