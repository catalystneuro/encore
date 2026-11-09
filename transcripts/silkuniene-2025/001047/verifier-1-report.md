**A. Outcomes** (20 claims in the claims file. The attempt record was not among my materials, so all counts come from the claims file.)

All rate and burst work is limited by one fact about the dataset, confirmed from the asset metadata on the API. It holds only rate codes 011 (0.2 MHz) and 013 (1 Hz), all with 600-ns pulses. CT26 burst labels are x1, x2 and x3/x5, but not at both rates: x2 exists only at 1 Hz and x3 only at 0.2 MHz.

| Claim | Outcome | Reason |
|---|---|---|
| fig2-heating | blocked (data_missing) | None of the 88 assets is a thermochromic film image; all are CT26 or CHO monolayer images. |
| fig3a-centre-enhanced | not_reproduced | Cell 18: 1 Hz CANCAN peaks at 4 to 7 mm, not at 0, under every reading at x1 and x5. Cell 12 shows 1 Hz x2 also has y6 (887) above y0 (516), so 1 Hz fails at every label. The control's centre-below-6/7-mm gap also fails the F8 rule. |
| fig3bc-rate-suppresses-off-target | not_reproduced | Cell 20, x1: 0.2 MHz is 17 to 35 times lower at 6 and 7 mm, but the 7-mm gap fails F8 and perimeter reading (b) fails (t-test p = 0.16 to 0.85). x5: 0.2 MHz is higher at 6 and 7 mm. |
| fig3-lorentzian-profile | not_reproduced | Cell 22: R ranges from −0.89 to 0.72 for 1 Hz. The 0.2 MHz x1 fits hit the 100-mm width bound. R > 0.9 with p < 0.001 holds only in a few 0.2 MHz x5 fits. |
| fig3-tail-deviation-falls-with-rate | not_reproduced | Cell 24: reversed at x5. The x1 "holds" measures deviation from a 0.2 MHz fit stuck at the width bound with negative R. With two rates the Spearman coefficient is ±1 by construction, and the Lorentzian fits it depends on failed. |
| fig4b-centre-no-rate-effect | partially_reproduced | Cell 26: the one available comparison has p = 0.93 (x1) and 0.54 (x5). The 1 kHz and 10 kHz comparisons are missing. At x1 both rates show no centre uptake at all (1.0 and −1.4 a.u.), so "no effect" there carries little information. |
| fig4b-near-electrode-decline | not_reproduced | Cell 28, x5: k > 0 and 0.2 MHz is higher. x1: k < 0, but t p = 0.17 and 0.33 and the 7-mm F8 gap fails (the x1 result depends on how F8 is read, see B4). |
| fig4b-40-fold-ratio | not_reproduced | Cell 30: the ratio is −0.29 to −0.15 at x1 and 1.4 to 2.5 at x5. From the cell 12 means, x3 gives about 4.7 (6 mm) and 2.4 (7 mm). No 0.2 MHz label comes near 36 to 44. |
| fig4c-fwhm-falls-with-rate | blocked (data_missing) | No 1 kHz or 10 kHz files (confirmed from the session descriptions). |
| fig4c-log-trend | blocked (data_missing) | Same: two of the six rates. |
| fig5-raised-electrodes-weaken-centre | blocked (metadata_insufficient) | No session description mentions electrode elevation. |
| fig5ab-yp-spot-slightly-larger-than-pr | not_reproduced | Cell 34: the YP/Pr FWHM ratio is 0.52 to 0.77 at x3, x5 and pooled. At x1 there is no spot (fits at the bound). This rests on the unchecked assumption of 0 mm elevation, and the pooling over labels is not the S2 condition (B3). |
| fig5b-gaussian-pr-lorentzian-yp | not_reproduced | Cell 36: pooled R² values are outside tolerance and the Pr ordering fails under every reading. No single label passes every reading; only x5 under O2 b is within tolerance. |
| fig5c-nuclear-yp-centre | blocked (metadata_insufficient) | The block is right but the stated reason is not (B7): 12 CT26 Hoechst images paired with the Pr images exist. The pixel size (about 3.25 µm, inferred) is too coarse for 2 to 4 µm cytoplasm rings, and elevation is unknown. |
| fig6b-900ns-peak-not-significant | blocked (data_missing) | Every description says 600-ns pulses. |
| fig6c-normalized-decline-similar | blocked (data_missing) | Same. |
| fig6d-fwhm-falls-with-duration | blocked (data_missing) | Same. |
| fig7be-peak-grows-with-bursts | blocked (data_missing) | All 17 CHO wells carry the single label r1, so there is no CHO series. The CT26 half was not tested (B6). |
| fig7cf-fwhm-bursts | blocked (data_missing) | The CHO series is missing, as above. The CT26 half was not tested. |
| fig7-sharpest-one-burst | not_reproduced (conditional) | This claim is CT26 only, so the notebook's reason for blocking it (no CHO series) does not apply. If x1 means one burst, cells 32 and 38 show centre YP −1.4 ± 6.3 and mean FWHM 55.7 mm (2 of 4 fits at the bound), far from 1.1 mm and a ratio of 36 to 55. If x1 means two bursts, the condition is absent and the claim is blocked (metadata_insufficient). |

**B. Problems**

1. [affects a conclusion] Cells 15 to 30, burst-label readings. The notebook tests S1 ("2 bursts (x4)") at labels x1 and x5 and counts agreement between them. Neither reading of the labels makes x5 two bursts: x5 is 5 or 6 bursts, near the CT26 saturation shown in Fig. 7. So x5 is a different condition, not a reading of S1. The two readings that do fit are:
   - x1 is two bursts (one repeat after the first);
   - the label is the total burst count. The dataset text says the protocol "was either repeated 2, 3, or 5 times". Under this reading 2 bursts exists only at 1 Hz (x2), and 1 Hz x2 was never analysed.

   The "holds at one label = partial" rule is the author's own and appears nowhere in the claims file. My outcomes above rely on cases that fail at every label.
2. [affects a conclusion] Cell 37 and the cell 0 table: fig7-sharpest-one-burst is blocked "no CHO series", but the claim uses CT26 only. The fig7be and fig7cf CT26 halves (centre YP at x1/x3/x5 is −1.4, 353 and 2275) were also left untested.
3. [affects a conclusion] Cell 34: the S2 analysis pools 0.2 MHz wells with labels x1, x3 and x5 (n = 1, 2, 2). That mixes burst numbers whose amplitudes differ by a factor of over 1000, so the pooled profile is in effect x5. Two of the five Pr areas were located by centroid. One of them, kvqdb2 R, has match score 0.006, and its circles are visibly misplaced in cell 10. The 0 mm elevation is an assumption the data cannot check.
4. [affects a conclusion, for fig4b-near-electrode-decline at x1] `gap_significant`: "gap exceeds the mean of the two s.e. arms" is the author's own reading of F8 and was not run under the alternatives. At x1, 7 mm (gap 35.2, arms 130.9 and 2.9) the result passes if the shorter arm is used and fails for the mean or longer arm. At 6 mm it fails under the longer arm. fig3a and fig3bc are not changed by this (checked on the printed numbers).
5. [does not affect a conclusion, but is unchecked] Cell 4: the dataset text gives a 3.2-kV first pulse and 4-step 75/50/25% packets. The notebook dismisses the whole protocol text as "wrong" on geometry alone. The voltage cannot be checked from images. If the CT26 data were taken at 3.2 kV, they are not the paper's 7.2-kV experiments. The empty 0.2 MHz x1 CANCAN wells, against the paper's sharp one-burst peak, are consistent with that.
6. [does not affect a conclusion] Cell 10: a 9×7 grid is zipped over 77 areas, so 14 areas are never shown. These include 013Control-x5_obj-oezvi9 R (0.2 MHz CANCAN x1) and all of 013Control-x2 and x5. Several displayed panels have clearly wrong centres or footprints, for example 011CC-x1_obj-1drpw33 L, 011CC-x5_obj-96qypk L and 011Control-x5_obj-kvqdb2 R. These areas are kept in the analysis.
7. [does not affect a conclusion] Cell 0 and the fig5c reason: "no full-resolution post-exposure Hoechst" contradicts the helper, which hard-codes CT26 DAPI as phase "post". The 12 DAPI files pair one-to-one with the Cy3 files, which fits Hoechst being re-imaged at 2 h.
8. [does not affect a conclusion] Cell 6: "the CHO images cannot show the array" is wrong. At 13.0 × 13.8 mm the half-extents (6.5 and 6.9 mm) contain the footprint centres at ±6.40 mm; only the footprint discs are clipped. The CHO data still lack a burst series, so no outcome changes.
9. [does not affect a conclusion] Cell 9: the pixel-size check is conditional on the assumed pixel size. With 3.25 µm, the best half-side is 6.11 ± 0.32 mm against an expected 6.40. Whole-well images give 7.0 mm (n = 3), 9% high, and this was not followed up.
10. [does not affect a conclusion] `parse`: the subject 011C_x5 ("Unknown protocol type") is classed as control without comment. Cell 13 notes that the a.u. scales differ several-fold between the 23 May and 24 May sessions, yet both are pooled into the same means and s.e.
11. [does not affect a conclusion] Cell 12: the label check gives CANCAN above control in 11 of 18 images, which is chance level, and the notebook says nothing about it. Visually (cell 10), the 1 Hz control "donut" and the CANCAN four-lobe patterns do match their sides.

Helper functions tested on a synthetic image (Lorentzian spot with a 2-mm FWHM plus four footprints):
- `locate` finds the centre to within 1 pixel;
- background is exact;
- the fitted FWHM is 2.04 mm under all four O1/O2 readings;
- the Gaussian fit returns the true sigma;
- `pool` and the `gap_significant` arithmetic are correct.

A fit to pure noise returns a narrow spurious width (0.64 mm), so a per-area FWHM on an unstained well means nothing.

**C. What I could not check, and the output that would have allowed it**

- Whether x1 means one burst or two: nothing in the archive settles it. The fig4b and fig3 tables for 1 Hz x2 against 0.2 MHz x1/x3 would at least have covered the second reading.
- Centre placement for the 14 areas never displayed: a complete version of the cell 10 grid.
- Whether the 0.2 MHz x1 CANCAN wells are unstained or mis-centred: per-area raw, unsubtracted, profiles and background values for those four areas.
- The applied voltage: no file states 7.2 kV, so this needs the depositors.
- How the F8 gap rule is read: cell 18/20/28 tables under the shorter-arm, mean-arm and longer-arm readings.
- Whether the CT26 Hoechst images are at full resolution and pre- or post-exposure: their stated or derived pixel size and their acquisition times relative to the Cy3 images.
