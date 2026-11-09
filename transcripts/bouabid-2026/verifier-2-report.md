**Verifier report, round 2: Bouabid, Vu et al. 2026 on DANDI 001692 (0.260303.1724)**

The claims file has 33 claims. The attempt record has 33 outcomes: 21 reproduced, 8 partially reproduced, 3 not reproduced and 1 blocked. I saved the preprint full text (HTML and extracted text) under `paper/` and checked the Figure 8 legend statistics against it. Cell indices below refer to the re-executed notebook, which has 121 cells.

### 1. Outcomes

I agree with all 33 stated outcomes.

- **fig8e-cocaine-region** is now reproduced. In round 1 I disagreed because the notebook used Type II sums of squares. Cell 111 now uses Type III and gives 199.86, 36.37 and 10.75. The legend gives 199.9, 36.37 and 10.75, so this matches.
- **The other 32 outcomes** are unchanged from round 1. Where the numbers moved (fig2-magnitude-correlations, fig2b, ed3e, fig6a, fig6c, ed2, fig1h, ed9), each outcome still follows from its criterion.
- **fig7f** (reproduced, cell 105): the test now also holds against the OR-exclusion hotspot (p = 0.0003). The statement's second part, that the dips' own hotspot overlaps the cohort hotspot, gives p = 0.065. The criterion treats that part as a variant, so the outcome stands.

### 2. Sentences the printed numbers do not support

- **Cell 45, and the fig2d-magnitude-in-out notes in the record.** They say "median -0.32 against -0.23", "-0.18 against -0.17, p = 0.12" and "Neither same-sign type differs (p = 0.12 and 0.21)". Cell 44 now prints -0.3252 / -0.2323, -0.1861 / -0.1626 with p = 0.1134, and same-sign p = 0.1079 and 0.2169. Rounded, those are -0.33, -0.19 against -0.16, p = 0.11, and 0.11 and 0.22. The text keeps the round-1 values. The record's response, "No change needed; the values are as before", is also wrong, because the random stream changed. The outcome is not affected.
- **README.** "It takes about fifteen minutes, a quarter of it streaming." Cell 120 prints 7.9 min. Cell 1 prints 138 s of streaming, which is about 29% of the run.
- **Cell 79.** "three to five times as many as each other mouse". The ratio is 501/149 = 3.4 up to 501/92 = 5.4.
- **README table, first row.** "132 negative (DA leading), 42 positive (ACh leading)". In the paper, 127 of the 132 have DA leading and 31 of the 42 have ACh leading (cell 17).
- **Summary (cell 119).** "The excitation source descriptions are copied from another setup". Cell 4 shows that the descriptions differ from the Methods, not that they were copied. The record's finding words this correctly.
- **Two minor wording points:**
  - Cell 88's "troughs next to a NaN were missed (2197 of 30341 site-trials have a NaN in the range searched)" can be read as 2197 misses. 2197 is the number of site-trials with a NaN in the search range, not the number missed.
  - Cells 103 and 106 and the ed9 notes say that with AND "most stimulation responses stay in the data". This follows from how the AND mask is defined, but the notebook prints only the overall fractions removed (6.5% and 32.7%), not the fraction of post-stimulation samples kept.

All other "**Result:" sentences, the rest of the Summary, and the remaining record notes match the printed outputs.

I checked these Figure 8 statements against the paper's legend, and all hold:
- F(8,36) for the cocaine effect in Figure 8c;
- the DLS stimulus F of 34.46 in Figure 8f;
- "n = 5 slices per region from 5 mice" for Figure 8b.

**My round-1 reasons in the record.** The verification entries state my round-1 reasons faithfully and in my own words, including the B-point cross-references and the disagreement on fig8e. Two small gaps:
- The `reviewed` field omits that I also read the paper and the Zenodo Figure 8 source data and queried the DANDI asset list.
- For fig6a and fig6c, the entries do not say that I classed B6 as not affecting a conclusion.

### 3. Round-1 points

**Resolved:**
- **B1, hotspot false positives.** Cells 22 and 35 now run the procedure on the real site coordinates with values shuffled across sites. In fig1f, 67 of 100 shuffles produce a hotspot, but none reaches the real 1010 voxels or its mean. In ed1, 73 of 100 produce one, and none reaches the 551 voxels. fig2b, fig3e and ed9 rest on the overlap test, which I found calibrated in round 1.
- **B2, Type III ANOVA.** Cells 108, 111 and 114 use Type III. The DLS stimulus F now matches the legend's 34.46.
- **B3, chance-corrected pairing.** Cell 47 adds the cross-session null. Every site keeps an excess over chance, and the overlap p values are 0.030, 0.005, 0.015 and below 0.005.
- **B5, ADS exclusion mask.** The record now gives the fraction each mask removes, and fig7f has been rerun with the OR-exclusion hotspot.
- **B6, NaN trough bug.** The fix in `daach.py:352` is correct. The synthetic check in cell 87 would fail without it.
- **B7, rank-sum test.** `in_out` now follows MATLAB's ranksum rule and reports exact p for small groups.
- **B8, rate denominators.** Rates now divide by usable time (`daach.py:741`).
- **B9, docstring.** The `Grid` docstring is corrected.
- **Section C requests.** The cue null pool size, the NaN trial count, the exact p values and the Figure 8c descriptive ratios are all added.

**Remaining, bearing on a conclusion:**
- **fig4-cue-sequence (B4).** The not-reproduced label comes only from the criterion's wording: 58 of 75 sites is above the tolerance, and the criterion has no band for counts above it. The qualitative claim holds, and the code's percentiles give 52, which is within tolerance. The attempt kept the criterion as written, which is correct; readers should take the label in that light.
- **ed1-controls-no-organization.** The new shuffle result shows the control hotspot (551 voxels) is larger than any of the 100 shuffles. So by the paper's own test the controls do show organization, and the record's "the outcome rests mainly on the strength of the correlations" understates this. Two deviations could produce correlated red-green signal in the controls and bear on this outcome:
  - the high-pass series used has no artifact removal, since the files hold none for these mice;
  - only the 15 reward sessions are used, where the paper used all ITI data.
- **fig4c-cue-correlation.** It is still unexplained why the paper reports 65 cue-responsive sites where every site here responds.
- **fig7f-ach-dip-in-out.** The statement's overlap part is not supported (p = 0.065), although the criterion scores it as a variant.
- **fig2-magnitude-correlations.** The second count (69, 3.9 below its bound) changes by several sites between random streams. The partial outcome held in both runs.
