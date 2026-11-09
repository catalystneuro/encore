I've revised the attempt for round 1. Two outcomes changed, both to the verifier's view, and the other 29 claims keep their outcomes. The entry re-ran cleanly with `tools/entry.py all` (374 s, check reports 0 errors), and every conclusion, the README and the attempt record now match the new numbers.

**Changed outcomes**
- `fig2a-fluovolt-saturation`: partially_reproduced → **not_reproduced**. The criterion requires both values, and under the adopted far background both miss (49.4% against 66, and -69.8% against -83). The saturation shape still holds.
- `fig3-dye-sensitivity`: not_reproduced → **partially_reproduced**. The two correlations (0.964 and 0.762) and the ratio between the two slopes (2.92 against 2.86) match. The slopes themselves, 21.6 and 7.4, are 17 and 19% low.

**Fault found while making the outline images.** The outline images the verifier asked for showed three outlines traced on the wrong structure: Di-8-ANEPPS cell c7 at 300 and 350 V (traced on a bright body inside the cell) and FluoVolt cell c2 at 300 V (traced on a neighbouring cell). A fourth, c1 at 400 V, is not used. Any set whose radius is more than 15% off its cell's median is now traced again within a narrow window. This changed some 1200 and 1400 V/cm values but no outcome:
- `fig4b-cathodic-asymmetry`: the anodic value at 1400 V/cm is now -21.6%, where it was -18.5%.
- Under the near background (2 to 4 µm out), `fig4b-cathodic-asymmetry` and `fig4b-first-10-pulses` now pass. Both outcomes are judged on the far background (8 to 10 µm out), so they stand, and this is recorded in their notes.

Several Di-8-ANEPPS outlines are still wavy along part of the cell edge. I describe this in the notebook but did not correct it.

**Added in reply to the report**
- **File contents:** a dump of what one file holds. There is no imaging-plane or device record, field of view or pixel size, so the pixel size really is missing.
- **Outline images:** pictures of each cell's outline, with how sharply each outline sits on the membrane, set by set.
- **Volts mapping:** going from 25 to 50 V triples the response in both dyes (3.05 and 2.90). The paper's in-order field strengths predict 3.49 and a field proportional to the volts predicts 2.0, so the data support matching in order. If the field is taken as proportional to the volts, `fig7b-charging-during-pulse` fails. It stays reproduced, marked as resting on the in-order matching. That alternative was also run for the fig3, fig4 and fig7b claims.
- **Background distance:** every claim now shows a sweep from 8 to 44 pixels outside the membrane, plus a separate background for each pole. One band, 4 to 5 µm out, would bring several paper values within tolerance:
  - the FluoVolt saturation values (`fig2a-fluovolt-saturation`);
  - both slopes of `fig3-dye-sensitivity`;
  - the Di-8-ANEPPS first-10-pulse maximum.

  At that distance the cell's own glow is still about a sixth of its excess. I kept the far band because it is the one free of the cell's light, and I did not pick the distance to fit the paper. This is stated in the notebook and in the finding about the background.
- **Bleaching control** for `fig2b-di8-decline-within-set`: the drop within the 780 V/cm set is about the size of the bleaching drift seen at lower fields. The drops at 1000 to 1400 V/cm are larger than that drift.
- **Other variants:**
  - the 8-µm pixel for `fig3-fluovolt-nonlinear` and for the measured-against-calculated tests in fig4a and fig4b;
  - the equal-area radius for fig4a and fig4b;
  - the share of five-cell subsets that pass, for `fig2b-di8-bleaching` (38 of 56, now called fragile) and fig4c (0 of 56).
- **Question for a reader**, in `questions/001517.yaml`: whether the criterion of `fig2a-fluovolt-stable` should correct for running 24 tests. As written, a stable recording fails it about 70% of the time. The claim is tested as written.
- **Record:** round 1 is recorded under `verifications`. The two changed claims are marked `agrees: false`, with what I changed in reply.

**Not done**
- I did not identify which five Di-8-ANEPPS cells the paper used. The verifier also notes that neither the paper nor the files can settle this.
- None of the 15 blocked claims was unblocked. The verifier confirmed that their data are not in the dandiset.

`matplotlib` was added to the requirements and the lock file for the outline images. Nothing is committed.
