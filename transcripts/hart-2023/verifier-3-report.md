# Round 3 verifier report: Hart et al. 2023 (DANDI:000467), proposed outcome changes

The attempt record proposes one change of outcome (one `proposed` entry in the record). I agree with it: figs5c-mho-rarely-overlaps should be not reproduced.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| figs5c-mho-rarely-overlaps | not_reproduced (from reproduced, assumed) | Yes | — | See below. |

## figs5c-mho-rarely-overlaps

**The numbers come from the data.** The analysis is in `alarm_pheromones.ipynb`, cells 18, 21 and 22.
- Cell 18 builds the counts. For each ant and each of the eight readings, `mho_any` counts ROIs that respond to 6MHO and to heptanone, heptanol or hexanol. Overlaps at different depths are left out, as the claims file and the Methods say.
- These are the same responding sets (`resp`, `depth`) that figs5b uses. They come from the maps and ROIs built in cell 9.
- The test in cell 21 (`judge_mho`) is "median == 0 and count > 0 in fewer than half the ants". That is the criterion's wording.
- The record's reason quotes cell 21's output correctly:
  - **Readings using the ROI mean** (aix, aiy, bix, biy): met at both concentration readings. Median 0, with a shared ROI in 0 to 2 ants.
  - **Readings using the ROI maximum** (aiix, aiiy, biix, biiy): fail at both. At the higher concentration the medians are 2, 2, 1, 1 and 11 of 13 ants have a shared ROI. At 48% the medians are 3, 3, 1, 1 and 6 of 8 ants have one.
  - **Summary line:** cell 21 prints "met under 4 of 8 readings; under every reading: False" for both "higher" and "48%".
- Leaving out the flagged trials gives the same result. So does restricting to heptanone or hexanol only, the statement's own wording.

**The criterion is applied as written.**
- The criterion says "Reproduced when, under each M2 reading and under (a) or (b)…".
- The claims file's M2 also says "Every claim built on M2 is judged under each reading."
- The four maximum-value readings fail at both (a) the higher concentration and (b) 48%. So the claim fails whether "(a) or (b)" means "either suffices" or "each is checked".
- The round-1 outcome rested on the ROI mean, which set the criterion aside. The proposed change corrects that. It also makes the claim consistent with figs5b-shared-glomerulus and fig4b-vehicle-no-response, which were judged under every reading (cells 18 and 12).

**The choice was not made to reach a result.** The change applies the claims file's own rule and moves the outcome away from success. It should not be marked "assumed": the failure comes from the criterion as written, not from a reading the attempt adopted.

**Effect on fig6.** fig6-shared-panic-pathway (imaging half) is already not reproduced because figs5b fails (cells 24 and 25). This change does not alter it.

**Possible claims-file issue (reported, not corrected).**
- Under drawing (a), using the ROI maximum makes responses easy to call: one pixel at 0.2 or above is enough.
- Most drawing-(a) regions are sub-glomerular fragments; my round-2 report, citing cell 9, found 356 of 436 regions under 10 µm across. With these fragments, overlaps become nearly universal. One ant (ant1-m4-d27) has 27 shared ROIs under biix, against 0 under bix.
- The paper drew glomerular ROIs by eye. It gives no basis for a maximum-pixel ROI value, which is the reader's own reading.
- Requiring every reading to pass, when one reading is this permissive, may make a claim that something is rare close to untestable.

This does not change my verdict, because the criterion is applied as the claims file states it.
