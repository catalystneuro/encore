**Verifier report, round 2: Weible & Wehr 2022 on DANDI:002035 at 0.261022.1829**

There are 33 claims in the claims file and 33 outcomes in the attempt record. All 33 are `blocked`: 32 as `metadata_insufficient` and `wt-no-label` as `data_missing`. No outcome carries `assumed: true`.

### 1. Outcomes

I agree with all 33 outcomes. No outcome rests on a stated assumption, so there is none to judge.

- **The block is now shown, not asserted.** Cell 7 shows the region coverage. Cells 10–13 show placement: 26 of 66 fields placed, none at the stated scale, and no overview aligned to the atlas. Cell 7 also prints that `samples.json` says "individual sections are not tracked".
- **The partly testable claims stay blocked.** These are fig3a, fig6cd, fig7b, mgb-cells-rare and soc-plaques-rare. Three things back this:
  - The claims file says "any automated detection used in place of counting by eye is a deviation".
  - There is no wild-type reference to tell label from autofluorescence.
  - Cell 15 shows 554 of the 561 region-labelled images have their scale assigned by rule, and the placed fields are 2–8 times off their stated scale.
- **fig6cd is the only claim whose outcome these images could have changed.** Its criterion makes it not_reproduced "when any is" found. I looked at the cell 16 panel of the 0136 CN field: it shows small bright puncta in the ventral cochlear nucleus. Leaving them unscored is defensible, but it rests partly on a statement the outputs don't show (see 2.3).
- **The claims file reads the paper correctly where I checked.** The paper (txt lines 117–119) gives 61 5XFAD mice as "31 females and 30 males" and 25 wild-type mice. It gives the overview range as "12.5X to 50X" (line 158). I found no misreading that bears on any outcome.

### 2. Sentences the outputs do not support

There are no "**Result:" cells, because no claim was tested. Every number in the Summary (cell 20) and the README matches cells 3, 7, 11 and 15. The following do not:

1. **Cell 17, and the fig3a note in the attempt record: "before p60 (11 mice)" / "the 11 younger mice".**
   - Cell 7's 200X Abeta42 table gives 1 + 2 + 1 + 4 = 8 subiculum mice before p60, and cell 15 lists the same 8: NN, 0324, 0334, 0294, 0214, 0219, 0241, 0248.
   - 11 is all subiculum mice except the five at p60, so it includes the three mice at p90–p150.
   - The outcome is not affected.
2. **Cell 13: "Most fields that fail are matched at the smallest pixel size tried … with peaks no higher than the null's."** The first half holds: 36 of the 40 failures are best at 0.3225 µm. The second half does not. From the cell 11 table, a failed field's peak height is at or below the null's in only 16 of 40, and its correlation in 25 of 40. Several failures beat the null clearly; for example, 0329 run 11989 has z 8.7 against 4.5 and ncc 0.912 against 0.586.
3. **The fig6cd note, and the record's response to it: the CN and VCN fields "lack" a red-channel reference.** No output lists the stains in the "0136 follow-up CN" or "0215 follow-up IC, VCN" subfolders. Cell 15 lists Abeta42 images only, and cell 18 covers only the subfolders with no region. The statement may be true, but it is not shown, and it is one of the reasons fig6cd was not scored.
4. **The fig7b note, and the record's response: "at least 0.645 µm per pixel, so a diameter over 40 µm cannot be measured."** The conclusion does not follow from that reason. At 0.645–2.58 µm per pixel, a 40 µm cell spans about 16–62 px, which is resolvable. What prevents the measurement is that the true scale is known only within a factor of 4 (cell 11, last table), not that the pixels are coarse. The outcome is not affected.
5. **The search grid has an edge, which no cell mentions.** The fields reported "at 8 times" (CN of 0136, PRNc of BrTNR and LTN) are best at 2.58 µm, the largest size tried. Their true ratio could be higher. The "at least 0.645 µm" lower bound still holds.

The visual statements I checked against the panels hold:
- The CN field of 0136 covers the whole ventral cochlear nucleus and the flocculus (cell 12).
- The SOC field of 0136 shows a large part of the brainstem at low magnification (cell 16).

**Do the reasons in the attempt record match mine?** Yes. The `reason` fields in `verifications.results` match my round-1 table almost word for word, in my wording. The `reviewed` text summarises my problems 1–6 fairly. One small inaccuracy: it describes problem 6 as "the extra mouse was not named". My point was that the counts were reported correctly and that naming the extra mouse did not matter.

### 3. Round-1 points

| Point | Status |
|---|---|
| 1. The block reason was asserted | Resolved. Cells 10–13 test placement against a null: 26 of 66 placed, none at the stated scale, no atlas alignment. |
| 2. The labelled images were not looked at | Resolved as "considered and not scored". All 561 images are listed, with one panel per mouse and region (cells 15–17), and the reasons are given part by part. |
| 3. Coverage counted DAPI-only images | Resolved. Cell 7 adds a table of 200X Abeta42 images per region and age; A1 has none. |
| 4. The position check sampled 20 images | Resolved. `samples.json` is printed and cited. |
| 5. The rule-assigned 200X images were not checked | Resolved in part. 10 rule-assigned and 36 region-labelled fields went into placement, which led to a new `metadata_error` finding. That finding is supported by the ratio table, including its ambiguity about whether the overview or the field class is wrong. |
| 6. Which mouse is the extra one | Answered: it cannot be told. |
| C. The 21 subfolders with no region | Resolved. Cell 18 lists them by magnification and stain. |

**Still open, bearing on a conclusion:**
- **fig6cd (2.3 above).** The cell 16 panel shows puncta in the CN-labelled field of 0136, and the claim fails on any label found. The record's case for not scoring them relies partly on there being no red-channel image, and no output shows that. One output listing the stains in the two CN/VCN subfolders would settle it. The outcome stays blocked whichever way it goes, unless such a reference exists.

**Still open, not bearing on a conclusion:**
- The count of 11 younger subiculum mice should be 8 (2.1).
- The "no higher than the null's" sentence in cell 13 overstates what the table shows (2.2).
- The fig7b reasoning about pixel size should be reworded (2.4).
- The grid-edge caveat for the fields at 8 times should be noted (2.5).
