I've finished the attempt on DANDI:001277 at version 0.250701.1610 and built the handover; the verifier has not seen it yet. That is the only published version, and the draft is identical to it. `entry.py check` reports 0 errors and the notebook runs from a clean environment in 590 s. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig6b-peak-900ns-not-significant | reproduced (rests on an assumption about which wells) |
| fig6c-normalized-decline-similar | not reproduced |
| fig6d-longer-pulses-sharper-peak | blocked, methods_underspecified |
| fig6d-600-900-differ-from-300 | blocked, methods_underspecified |
| fig6d-900ns-fwhm | blocked, methods_underspecified (only because it depends on the claim above) |
| fig5-yp-lorentzian-pr-gaussian | not reproduced (rests on an assumption) |
| fig5-yp-spot-slightly-larger-than-pr | not reproduced (rests on an assumption) |
| fig5-raised-electrodes, fig3 ×2, fig4b ×2, fig4c, fig7 ×3, fig2 | blocked, data_missing (10 claims) |

- **fig6b:** 900 ns has the highest centre value and no test is significant (ANOVA p = 0.54).
- **fig6c:** under every reading, at least one distance shows a gap between error bars, mostly 300 against 900 ns at 1–2 mm from the centre.
- **fig6d slope:** the readings differ, so the criterion blocks it. Fitting the 15 per-well values with contiguous ROIs gives p 0.002–0.004 against the paper's 0.003; most fits to the 3 means are not significant.
- **fig6d 600/900 against 300:** with contiguous ROIs, 900 against 300 ns is significant (p ≈ 0.006 against the paper's 0.0072); with 1-mm steps it is not. 600 against 300 ns is significant under no reading.
- **fig6d-900ns-fwhm:** its own criterion would be met (1.69–1.71 ± 0.08 mm with contiguous ROIs), but the protocol blocks a claim whose dependency is blocked.
- **fig5:** propidium (Pr, the cell-killing stain) is broad in these wells. A Lorentzian fits it better than a Gaussian, and its spot (6.4–8.9 mm) is wider than the YP spot (1.7–2.7 mm).

## 2. Dataset, assumptions, questions

**What the dataset holds:** only the pulse-duration experiment (Fig. 6). That is 18 CT26 wells on 3 plates, each with a Hoechst image before exposure and a YP image after it, plus 2-h Pr and Hoechst images on plates P1 and P2.

**Findings recorded:**
- Every well's description says "9 packets at 0.2 MHz" whatever the pulse duration, including the sham well.
- There are 7 wells at 600 ns where the paper reports n=5, and nothing says which five were used. This decides the Fig. 6D trend: p ≈ 0.003 without the two extra wells, p 0.83–1.00 with all seven.
- Two wells on plate P1 row B take up dye over the whole array. P1-B3 also loses cells over the centre by 2 h.
- One Pr image (well P2-B3) is deposited twice with identical pixels.
- The metadata say 12 significant bits, but pixel values reach about 65,400.
- There are no ROI coordinates.
- The electrode geometry in the files is consistent with the paper. The "10 mm" spacing is the edge-to-edge side, which matches the paper's 15.3-mm diagonal.

**Assumptions (marked `assumed: true`):**
- Fig. 6 uses the five plate rows that each hold one well of 300, 600 and 900 ns. This is the only basis in the data that does not depend on the results; all 7 wells and all 21 five-well choices are shown.
- The 600-ns wells are the 0-mm group of Fig. 5. Their counts (7 YP, 5 Pr) match the Fig. 5 legend's n=6–7 and 4–5.

**Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
- Which 600-ns wells were used?
- Are those wells Fig. 5's 0-mm group?
- How far apart were the ROIs along the diagonals?
- Was the Fig. 6D trend fitted to the 15 values or to the 3 means, and was it linear or logarithmic?

**Questions to a reader:** none.

## 3. Protocol issues

1. **Dependency blocking.** The rule that a claim depending on a blocked claim is also blocked (step 1.5) blocks fig6d-900ns-fwhm. That claim depends only on the fitting method, not on the parent's result. I followed the rule and gave the values in its notes.
2. **Criterion against step 1.6.** The criterion says "blocked when readings differ", while step 1.6 lets the author adopt the best-supported reading. I followed the criterion, since the claims file binds.
3. **No clock to check.** Step 2's clock check does not apply to single-time-point images. I substituted a spatial check: in 16 of 17 exposed wells the YP peak lies within 0.42 mm of the array centre, against 1.7 mm to random points.
4. **Unidentified wells.** The protocol has no rule for a dataset with more recordings than the paper analysed and no record of which were used. I treated it as an assumption with every subset shown and logged a `selection_undocumented` finding.
5. **Develop on a subset.** I cached reduced images in `$TMPDIR` during development only. The notebook streams everything.

## 4. Runtime and failures

The run took about 1 h 15 min, from 19:35 to 20:47 UTC. The notebook takes about 10 minutes, most of it streaming roughly 13 GB of images.

Nothing failed in the final runs. During development, the first footprint detector failed on faint wells; I fixed it by correcting the tile shading of the stitched images. The sham well has no footprints and is not used.

The new files are in `entries/001277-silkuniene-2025/` and `attempts/001277-silkuniene-2025-01.yaml`; the verifier's package is in `executed/001277-silkuniene-2025/handover/`.
