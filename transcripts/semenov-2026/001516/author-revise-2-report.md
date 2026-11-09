No outcome changed. The verifier agreed with all 32 (one `not_reproduced`, fig5b-conductivity-calibration, and 31 `blocked` for missing data), so I proposed no changes. I re-ran `python tools/entry.py all entries/001516-semenov-2026` after the edits and it passed; `tools/entry.py check` reports 0 errors. The fig5b numbers are unchanged: 1.33% and 1.20% for a 10-fold rise, 11.87% and 11.75% for a 100-fold rise.

**Added and corrected:**
- **First-frame dimming:** cell 15 now also prints the range of the frame-0 ratio over files and how many fall below 0.9. The range is 0.52 to 1.11, with 65 of 72 files below 0.9. So "every set" was wrong, and the summary (cell 29), cell 16, the record's finding and the helper docstring now say "in 65 of the 72 files" with the median and range.
- **Touching cells (cell 10 against cell 12):** the overlay shows c11 cell 1 touching a neighbouring cell that was left out. Both cells were right: cell 10 lists the pairs that were split, and cell 12 now names the split pairs in c2, c3, c10 and c12 and the c11 contact separately.
- **Finding about the falls in the sham sets:** it now says the 12.1 and 12.2 points are pulse frames 20–29 against 50–59, and the 15.9 and 16.3 points are baseline frames 1–9 against 10–19. It no longer says "first and last 10 frames".
- **fig5b response:** I removed the by-eye reading of the Fig. 5B curve, since no output supports it. The response now says the paper_inconsistency finding rests on the text of Results 3.5 and on Eq. (2) with the Methods 2.3 constants. The finding itself never cited the figure.
- **Old cell numbers:** where the round-1 reasons cite cells that have since moved, the current numbers follow in brackets (cell 18 for fig5b, cells 25 to 28 for the pulse pairs).
- **Round 2 recorded:** it is under `verifications` with all 32 claims. Each has `agrees: true`, the outcome, the verifier's reason paraphrased from its report, and a `response`.

**Not done:**
- **Whether the Fig. 5B curve used the stated constants:** still not shown. The protocol allows no numbers read from figures, and the outcome follows from the claims file's criterion, so I added no figure reading.
- **The claims-file header (round-1 point B1):** it stays as a question in `questions/001516.yaml`, and the claim is unchanged.
- **Mapping of pulse amplitudes to field strengths (B7):** it stays flagged as an assumption. It is used only in the variants and decides no outcome.

Nothing is committed.
