No outcomes changed, and nothing is under `proposed`. The verifier agreed with all 21 outcomes in round 2, and nothing I found argues for a change. I re-ran the entry with `python tools/entry.py all` and it passes. The numbers behind each claim are unchanged (378 HD cells, 391 with the misaligned session realigned, ratios 8.33 and 0.87, scaled ratio 16.69). `tools/entry.py check` reports 0 errors.

**Added or corrected:**
- **Unsorted spike times:** the verifier pointed out that the HD-cell check tested units with more than 2^20 spikes, which are not the unsorted units. `hd.py` now flags each unsorted unit and records how its times are split. The data check prints all 36 such units. Each holds exactly two sorted runs, and all 36 break at an index of the form k × 65536 − 1. They fire at 2.8 to 167.0 Hz (median 58.7). In 10 of them, 821 to 22281 times of the second run also appear in the first. The HD-cell check now uses the flag: 0 HD cells among the 34 unsorted units in open-field sessions. Cell 10, the hd-cell-fraction notes and the format_error finding now say only what this output shows.
- **fig2f-sws-tenfold-faster:** the conclusion, notes, summary and README now give the scaled ratio of 16.69. They say the data fit a speed-up below, at or above tenfold, so the fold is not determined.
- **fig2f-rem-similar-to-wake:** "consistently" is removed. The text now gives REM faster in 581 of 1509 pairs, Mouse20 at 1.07 and the decoder variant at 1.05.
- **hd-cell-fraction:** the conclusion and notes now also say the count match may be coincidental, since the unit rows cannot be brought down to the paper's 1077 cells.
- **Cell 18:** the shifts now read −10 s in 9 sessions, +10 s in one and +30 s in one.
- **README run time:** now 10.1 min with 322 s of streaming, from the final run.
- **fig4b, round-1 reason:** corrected so that "a tenth" refers to the relative scale (+0.08 against +0.81), not to the +3.6 Hz².
- **Round 2 in the record:** added under `verifications`, with the verifier's reasons and my response for each of the 21 claims.

**Not done:** nothing the report asked for was left out. The workflow will commit the changes, so I did not commit. Some untracked dotfiles and folders I did not create (`.bashrc`, `.idea`, `scripts` and others) are in the repo root; I left them alone.
