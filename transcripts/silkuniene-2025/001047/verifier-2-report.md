## Round 2 verifier report: Silkuniene et al. 2025 on DANDI:001047

**1. Outcomes**

The claims file has 20 claims and the attempt record gives 20 outcomes: 8 not reproduced, 1 partially reproduced and 11 blocked. I agree with all 20.

| Claim | Record | Agree? | Notes on assumptions |
|---|---|---|---|
| fig2-heating | blocked, data_missing | yes | |
| fig3a-centre-enhanced | not_reproduced | yes | Fails under both label readings (cell 18), so it does not depend on `assumed`. |
| fig3bc-rate-suppresses-off-target | not_reproduced | yes, conditional | Depends on the label reading. Under the total reading, both bracket pairs (x2\|x1 and x2\|x3) pass every place under the shorter-arm F8 reading (cell 21). The record says so. |
| fig3-lorentzian-profile | not_reproduced | yes | Fails under both readings (cell 24). |
| fig3-tail-deviation-falls-with-rate | not_reproduced | yes | |
| fig4b-centre-no-rate-effect | partially_reproduced | yes | Read literally, the criterion gives "reproduced" on the one available comparison (p = 0.93). "Partially" is a stated judgement: four rates are missing and neither rate stains the centre. That is reasonable. |
| fig4b-near-electrode-decline | not_reproduced | yes | Depends on two assumptions: labels read as repeats, and F8 read as the longer arm. The mean-arm reading gives the same outcome; only the shorter-arm reading flips it (cell 33). t-test p = 0.17 and 0.33. The record states this. |
| fig4b-40-fold-ratio | not_reproduced | yes | No label comes near 36 to 44 (cell 36). |
| fig4c-fwhm-falls-with-rate, fig4c-log-trend | blocked, data_missing | yes | |
| fig5-raised-electrodes-weaken-centre | blocked, metadata_insufficient | yes | |
| fig5ab-yp-spot-slightly-larger-than-pr | not_reproduced | yes | Rests on the assumption that the electrodes touched the monolayer, which is stated and cannot be checked. The single x1 well decides through its YP profile, which has no spot; its flagged Pr centre does not matter for that. |
| fig5b-gaussian-pr-lorentzian-yp | not_reproduced | yes | Same assumption as fig5ab. |
| fig5c-nuclear-yp-centre | blocked, data_missing | yes | I withdraw my round-1 reason (metadata_insufficient). The criterion's own block clause names missing full-resolution images. This rests on the inferred pixel size of 3.25 µm (cell 9 suggests 3.40 µm); either value is far too coarse. |
| fig6b, fig6c, fig6d | blocked, data_missing | yes | |
| fig7be-peak-grows-with-bursts, fig7cf-fwhm-bursts | blocked, data_missing | yes | |
| fig7-sharpest-one-burst | blocked, metadata_insufficient | yes | This matches my round-1 conditional. There is a slight tension: the record uses the adopted reading to decide other claims but treats it as unknown here. Under the adopted reading the block would be data_missing. The outcome is the same either way. |

The label reading adopted for every rate claim (labels count repeats after the first burst) is stated and reasonable. It is the literal sense of "repeated 2, 3, or 5 times" upon completion. It is also the only reading under which the dataset has both rates at one burst number, as the paper's set S1 does, and under which x5 is the paper's 6 bursts.

**2. Text against outputs**

Every number in the "Result:" cells (19, 22, 25, 28, 31, 34, 37, 42, 45, 48, 51, 54), the Summary (cell 55), the README and the record notes matches the printed outputs. I also checked the truncated tables in cells 21, 27 and 50. The exceptions:

- **Finding `data_missing` in the record:** "no raised electrodes … so 11 of the paper's 20 findings cannot be tested."
  - The record's own fig5-raised notes say raised wells, "if any are in the dandiset, cannot be identified".
  - Two of the 11 blocks are not missing data: fig7-sharpest is blocked on labels and fig5-raised on missing metadata.
- **Finding `other` and cell 13:** "Whole-well images also have backgrounds several times those of the two-well images." No output prints background by image type; cell 12 gives it by label only. The only indirect support is the two-well-only variant in cell 33.
- **Cell 11:** "Four areas have a centre that is visibly misplaced." At the displayed scale of the cell 10 grid, two more areas look misplaced. I am judging by eye at reduced resolution.
  - Panel 62, 013Control-x1_obj-1pihpj7 R (1 Hz CANCAN x1, centroid, match 0.022): the circles sit at the top edge, above the stain.
  - Panel 63, 013Control-x1_obj-6stwj8 W (1 Hz control x1, centroid, 0.015): the circles look offset from the pattern.
- **Finding `selection_undocumented`:** "No well was found deposited twice." Cell 14 compared only pairs with the same channel and condition (121 pairs), so a well deposited under a different label would not be found.

The verification section of the record states my round-1 reasons accurately and almost word for word, with the cell references removed. The fig7be reason keeps my cross-reference "(B6)". That was my own error: it should have been B2.

**3. Round-1 points**

All are resolved:

- B1: both label readings are run, and the rule "holds at one label = partial" is gone.
- B2: the CT26 halves of fig7be and fig7cf are tested, and fig7-sharpest is reasoned on CT26.
- B3: x1 decides; pooling is shown and described as not the S2 condition.
- B4: the three F8 readings are shown, and the flip is disclosed.
- B5: the voltage question is recorded as a finding.
- B6: all 77 areas are now displayed.
- B7: the Hoechst acquisition times are printed. My round-1 suggestion that Hoechst was re-imaged at 2 h was wrong; they were taken before exposure.
- B8, B9, B10 and B11: corrected or disclosed.
- Section C: raw profiles of the 0.2 MHz x1 areas are now printed (cell 16). They sit at background, so "unstained" holds whatever the centre placement.

What remains and bears on a conclusion:

1. **Possible misplaced centre in a deciding group.** Panel 62, which looks misplaced, is in the 1 Hz CANCAN x1 group. That group decides fig3bc, fig4b-centre and fig4b-near-electrode. A misplaced centre lowers the 6 and 7 mm values and widens their standard error, and fig4b-near-electrode already turns on how F8 is read. It should be flagged, or the x1 tables shown without it. (Plausible, not confirmed.)
2. **Label reading.** fig3bc and fig4b-near-electrode would point the paper's way under the total reading with the shorter-arm F8 reading. This is stated in the record and cannot be settled from the archive.
3. **Applied voltage.** It is unknown whether the wells were exposed at 3.2 or 7.2 kV. This is stated as a question for the authors.
