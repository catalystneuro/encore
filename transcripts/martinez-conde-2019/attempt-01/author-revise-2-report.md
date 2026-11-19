I made the text corrections and added the outputs the verifier asked for. No outcome changed, and I proposed no changes. The entry re-ran cleanly with `python tools/entry.py all entries/martinez-conde-2019` (passed, about 6 min), every number that was already reported came out the same, and `check` reports 0 errors.

**Outcomes:** none changed; the verifier agreed with all 19.
- **fig7c-fold-edge-equivalence** stays "not reproduced". The notebook conclusion and the record now call it borderline. They no longer call the distance-from-90 reading "the most literal", treat the two ways of counting "one step" as equally literal, and say the claim would be reproduced under the level-based count.
- I proposed no change there because the criterion fixes neither way of counting, and the verifier agreed with the outcome.

**Added or corrected:**
- **`smoothed_image_norm` count:** a new data check cell prints the right number, absent from 39 of 77 files, not 35. It also compares the field with `smoothed_image` in each of the 38 files that hold it:
  - in 5 it is `smoothed_image` minus `BaseActivity`, including the one file with an eye time map, so there it is not normalised by eye time;
  - in 21 it is a linear rescaling;
  - in 11 it is not a linear function of `smoothed_image`, with 26% to 77% of pixels at exactly -1;
  - in 1 it holds non-finite values.

  This replaces the unsupported "baseline-subtracted in some, scaled -1 to 1 in others" in the data check text, the Summary and the finding.
- **Corners frame sizes:** the fig5 cell now prints them (273 x 209 in 20 files, 257 x 193 in 6), and the deviation gives these counts.
- **table1-edge:** the Edge on the 18 complete files is now shown under every baseline reading.
  - With the squares inside the corners it keeps all five values within tolerance, and the Corners placements leave it unchanged.
  - On the 6 of those files that have `BaseActivity`, none is within tolerance, whether using the files' values or the main reading.
  - So the result depends on which neurons are included more than on where the squares are placed. The notes and the Table 1 conclusion now say so, and the conclusion also says the 12 Star recordings are picked by the files, not at random.
- **Round-1 reasons:** I added the two points the verifier said had been left out: the border-cut Edge files were also kept for fig7c, and standard deviation over mean cannot reach 0.943 without a black-level offset.
- **Round 2 in the record:** recorded under `verifications`, with the verifier's reasons and my response for each claim.

**Not done:**
- I added no questions to `questions/martinez-conde-2019.yaml`, because the verifier found no place where the claims file misreads the paper.
- I made no outcome changes for s4-baseline-no-difference, table1-s52 or table1-s90. The notes already state what the verifier raised: each depends on baseline placement and on which neurons are included. The Star selection cannot be fixed with this data.
- Nothing is committed, as instructed.
