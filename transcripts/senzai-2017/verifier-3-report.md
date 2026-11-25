# Verifier report, round 3: senzai-2017-02 (Senzai & Buzsáki 2017, DANDI:000003 0.261122.2143)

I agree with both proposals. The reason for each block should change from `metadata_insufficient` to `methods_underspecified`.

The counts come from the files. The claims file has 31 claims. The attempt record has 31 outcomes: 17 reproduced, 8 partially reproduced, 4 not reproduced and 2 blocked. Two outcomes carry a `proposed` change: gc-mc-distance and gc-backpropagation. I reviewed only these two.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| gc-mc-distance | blocked, `methods_underspecified` (was `metadata_insufficient`) | Yes | — | See points 1 to 4 below. |
| gc-backpropagation | blocked, `methods_underspecified` (was `metadata_insufficient`) | Yes | — | Same as gc-mc-distance: the site order can be read from the list place (cell 102), and the claims file gives no criterion. The delay was not computed, which is right when no criterion exists. |

**Reasons for gc-mc-distance:**

1. **The test is sound and its result comes from the data (cell 102).** It sums the absolute differences between neighbouring sites of the DS2 profile in list order. It compares that sum with 1000 random orders of the same sites, one-sided, with P = (1 + count) / 1001. As a control it runs the same test on the order of the LFP columns.
   - The list order is smoother than random on 0.83 of the 261 shanks where the DS2 reverses, under all five seeds. Chance gives 0.05, and the column-order control gives 0.26 to 0.28.
   - The smooth fraction is 0.92 on shanks with a positive Spearman correlation and 0.71 on shanks with a negative one.
2. **The test was not chosen to reach the result.** It is the one I proposed in round 2, run as I specified it.
3. **The site spacing is known.** The probe's 20 µm vertical spacing is stated in the files and in the paper. The paper's Methods give 20 µm vertical separation for both the 8-site (Buzsaki64) and the 10-site (Buzsaki64sp) shanks.
4. **So the metadata do not block the claim; the claims file does.** Its entry (claims file, lines 590–593) has a statement, source and quote, but no `expected` value and no `criterion`, so no outcome can be judged.

**Caveats. None of these changes either outcome:**

- **The direction of each list is not shown by the data.** The test shows order only, not which end is up. "First place at the top" is the lab's convention. Cell 102's example shank fits it: place 0 is at −793 µV and place 9 at +1323 µV, so the top site is above the reversal. On the 111 reversing shanks with a negative correlation, the record explains the reversed slope as the shank reaching the infrapyramidal blade. That explanation is plausible but was not tested.
- **The figure of 13 ± 49 µm (cell 102, cell 103, and the record's notes) is descriptive only.**
  - It places each unit at the electrodes-table site (`site_table`), which matches the wide-band site for 0.891 of units (cell 6). It does not use the wide-band site that the attempt adopted for mc-deeper.
  - It applies one direction to every shank.
  - The automatic pair test gives 7 ± 59 µm.
  - It should not be read as a failure to reproduce 59 ± 35 µm.
- **Finding 1 in the record still contradicts the proposals.** It is still kind `metadata_insufficient`, rated major. It also says the spacing of the 10-site shanks "is not given", which the paper's Methods contradict (see point 3). It should be brought into line with the proposed reason.
- **The claims file misreads the materials (reported, not corrected).**
  - Its header says the supplementary figures S1 to S7 were not available. But `paper/` contains a supplement, `10.1016-j.neuron.2016.12.011.supp.pdf`, and gc-backpropagation rests on Figure S3D to S3F.
  - I could not extract text from that PDF, because no PDF tool is installed here. So I have not checked whether it describes the method.
  - Whoever writes the missing criterion for gc-backpropagation should use it.
