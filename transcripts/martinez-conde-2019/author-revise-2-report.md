No outcomes changed and nothing is proposed for a third round. The round-2 verifier agreed with all 19 outcomes (9 reproduced, 3 partially reproduced, 4 not reproduced, 3 blocked). I re-ran the entry with `python tools/entry.py all entries/martinez-conde-2019`: it passed in 47 s, `check` reports 0 errors, and every result number is the same as before.

**Outputs added**
- **The file missing from the 5 + 21 + 11 count:** it is Corners ABC051000J3. Its `smoothed_image_norm` has NaN in 6,304 pixels, so it landed in no group. The helper now compares over the pixels that are not NaN and the cell names that file. The counts are now 5, 21 and 12.
- **File format:** cell 3 prints the MAT-file format of every map file and the two ABS files left out of the units check. The finding now says "all 75 files checked" in place of "all 75 version 5 files".
- **Registration offsets:** cell 3 prints them. The largest is 385 DU (370 along one axis), and the finding now gives those numbers.

**Text corrected (notebook, attempt record, README)**
- **Zero pixels:** the BaseActivity wording now says "appears to keep" the zero pixels and gives the Corners correlation (0.859 against 0.850) next to the Star one.
- **Baseline deviation:** the 0.72 figure (n = 19) and the 0.75 against 1.21 figures (n = 17) are now labelled with their subsets, in all 14 places the deviation appears.
- **BaseActivity:** "not reproduced by any placement tried while preparing (not run here)" is replaced by what the notebook prints: no placement matches exactly (median absolute difference 0.43 to 2.56 spikes/s).
- **Descriptor count:** "the descriptor says 53" is removed, since nothing in the notebook prints it.
- **fig7a:** the reading (b) fit is now described as near-linear with parameters as degenerate as reading (a)'s, not as a good fit.
- **fig7c:** the notes and conclusion give the two places where the Edge response dips instead of saying it rises throughout. The README now says the claim would pass on the other reading of "one step" only under the RMS reading of contrast.
- **fig6:** the conclusion and notes add the reading (ii) signed rank result for S90 against the median (p = 0.0115).
- **Round 2 record:** added under `verifications`, with the verifier's reasons and my responses for each claim.

**Not done, and why**
- **Remaining points on conclusions:** I did not change anything for them. These are the after-the-fact baseline placement, how fragile table1-s52 is, the "one step" reading in fig7c, the RMS contrast definition in fig7a, and the Star having 12 of 30 neurons. All are already stated, and the data cannot settle them. The baseline placement and the RMS contrast definition are already questions for the paper's authors in the record's findings.
- **Verifier's note B9b:** I added no new reader question. That point (the claims file still lists Corners S40 averaging as open) was already asked in round 1 in `questions/martinez-conde-2019.yaml`, and the round-2 record now points to it.

Nothing is committed, as instructed.
