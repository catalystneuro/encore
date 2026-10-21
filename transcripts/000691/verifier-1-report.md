**A. Outcomes** (23 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| abstract-thousands-of-neurons | reproduced | Main nb cell 19: 2948 EXTRACT footprints, all in one movie on shared timestamps. The mouse tracked over 47.7 loops of the maze; `cellfind_min_snr` = 2. |
| ed6a-curated-footprints | blocked (metadata_insufficient) | The only PlaneSegmentation columns are `image_mask` and `ROICentroids` (cell 3), so nothing marks the curated footprints. The claim's criterion says it then cannot be tested. |
| ed6bcd-other-mice | blocked (data_missing) | The DANDI API lists 2 assets and 1 subject (I checked this myself). |
| ed5-songbirds | blocked (data_missing) | No bird data in the archive. |
| birds-singing-rate | blocked (data_missing) | No bird data in the archive. |
| fig2d-lman-sparse-bursting | blocked (methods_underspecified; the data are also missing) | The claims file gives methods_underspecified. The notebook's table says only "data missing". |
| abstract-kiloscope-fov | reproduced | Cell 23: 808×608 px gives 4.80×3.61 mm at 5.94 µm/px and 4.32×3.25 mm at 5.35 µm/px. Both sides are within tolerance under both pixel sizes. |
| abstract-weights | blocked (data_missing) | No dataset could hold the hardware weights. |
| fig1e-featherscope-psf | reproduced | Cell 26, reading (a): 3.919 µm at the centre and 6.433 µm at the edge; reading (c): 3.887 and 6.884 µm. Both readings are inside 4±0.4 and 7±0.7, and they are stable under the Jacobian variant (cell 27). |
| fig1f-kiloscope-psf | partially_reproduced | No reading meets the criterion with either optimizer. Under (a) the edge is 5.441 µm (within tolerance) but the centre is 4.422 µm, 0.022 µm above the bound. With Jacobian scaling the centre is 3.578 µm, 0.022 µm below the other bound. The claims file has no partial rule; I call it partial because the centre is about 4 µm and the edge about 5 µm, rising with radius. |
| ed1cf-field-curvature | blocked (methods_underspecified) | As the criterion says. Best-focus slice against radius is shown in cell 30. |
| ed1-ed4-resolution | blocked (data_missing) | No USAF target images, in the dandiset or in the repository listing (cell 21). |
| ed2b-featherscope-flat-illumination | reproduced | Cell 32: corrected vs total-vignetting profile 0.511 vs 0.193 at 0.5 mm and 0.628 vs 0.257 at 0.45 mm. The corrected profile falls less from the centre at both radii. Robust to moving the centre (cell 33). |
| ed2c-kiloscope-flat-illumination | reproduced | 0.557 vs 0.180 at 1.8 mm and 0.420 vs 0.148 at 2.0 mm; the comparison holds for all 6 centres tried. |
| ed7-motion-small | not_reproduced (tentative) | Motion nb cell 6: RMS 0.037, 0.038 and 0.026 px under readings (a), (b) and (c), all far below 0.13±0.013. This rests on the deposited movie being raw, which nothing checks (problem 1); if it is motion-corrected, the right outcome is blocked (metadata_insufficient). |
| fig2-quadrant-direction-decoding | reproduced (null n1 only) | Quadrant nb cells 6–7: median accuracy 0.437 ≥ 0.375 (reading a; reading b fails, min 0.239). Null (n1): max 0.227 over 1000 shuffles, so p = 0. Null (n2), which the criterion also requires, was not run; its one sample (0.136) and the margin make a disagreement very unlikely. |
| fig2k-decoder-size | blocked (other: not run, compute) | Cell 10 only times the fits (4.2 h on 4 cores). The data are present, so this is not a data block. |
| fig2l-local-decoding-map | blocked (other: not run, compute) | Cell 12 only counts the map points used (5411/5905) and times the fits (about 4 h on 4 cores). |
| ed8-coactive-distributed | blocked (methods_underspecified) | Cell 36: all four quarters are covered in 8 of 8 events under reading (a) but 7 of 8 under reading (b) (component 1 at 1000 s has 0 footprints in the lower left). The criterion says that when the readings disagree the outcome is methods_underspecified. |
| ed9b-octant-decoding | reproduced (null n1 only) | Octant nb cell 6: 0.326 > 1/8, above the n1 null maximum of 0.229, p = 0. As for fig2, n2 was not run; its one sample is 0.110. |
| ed9c-local-decoding-map | blocked (other: not run, compute) | Cell 9 times it only (10–11 h on 4 cores). |
| ed10-localized-activity | blocked (methods_underspecified) | As the criterion says. Maps, entropies and peaks are shown in cell 39. |

**B. Problems**

1. **[affects a conclusion]** motion nb, cell 6 / `normcorre_rigid`: nothing checks that the deposited movie is raw, and the API metadata do not say. The paper says shifts were corrected with NoRMCorre before EXTRACT. Several outputs fit an already-registered movie:
   - the largest shift in 36,596 frames of a freely moving mouse is 0.16 px;
   - the per-window RMS is flat at 0.03–0.05 px (cell 7);
   - block 0 contains values of exactly 0 (cell 3).
   
   The ed7 outcome depends on this. Also, the registration is a Python re-implementation built from NoRMCorre defaults "as recalled here", not NoRMCorre itself.
2. **[affects a conclusion]** quadrant nb cell 8 and octant nb cell 7: the n2 null (1000 decoders of 200 fits each) was not run, though both criteria require it. The n1 comparison also sets a 200-fit averaged real matrix against single-fit null matrices: the n1 null median is 0.074, below chance, while the averaged null sample is 0.136. So n1 overstates the separation, though not enough to matter here.
3. **[affects a conclusion]** fig2k, fig2l, ed9c were not attempted. The estimated costs are 4–11 h on 4 cores, so this is a compute choice, not a data block. A reduced run was possible within limits, e.g. fig2k reading (b) with fewer fits, or fig2l with one fit per null decoder.
4. **[affects a conclusion]** `fit_bead` / cell 27: the main PSF fits often stop short of the least-squares minimum. The Jacobian variant finds a lower cost for 49 of 118 Kiloscope beads and 68 of 155 Featherscope beads. For fig1f the centre value swings from 4.42 to 3.58 µm depending on the optimizer. One edge bead is fitted at 27.77 µm, which inflates reading (c) at the edge (7.373 µm). No result is reported using the lower-cost fit for each bead.
5. **[affects a conclusion]** cells 36–37 (ed8):
   - The quarters split at the midlines of the footprints' extent leave 85 of 2948 footprints in the lower left, so the test turns on one sparse corner.
   - Under reading (b), the code's event times land where temporal weights are only 0.04–0.13 of their maxima for four components. Those times are not events of this NMF run.
6. **[does not affect a conclusion]** All decoding claims and ed8 use all 2948 footprints, not the curated 2382. The claims file names this as a variant, so it is allowed, but it is not the paper's set.
7. **[does not affect a conclusion]** `behaviour`: position is unwrapped by the loop length rather than with the code's MATLAB unwrap. About 0.6–0.9% of labels differ (cell 9). My synthetic loop test confirmed the quadrant, octant and unwrap logic.
8. **[does not affect a conclusion]** Cell 12: quadrant decoding peaks with labels shifted +2 s (0.519, against 0.495 at 0 s), so there may be a small clock offset. Any such offset would only make the decoders look worse.
9. **[does not affect a conclusion]** abstract-kiloscope-fov: both pixel sizes come from the authors' code, not the data. With 5.94 µm/px the test reduces to 808 px × a constant that yields exactly 4.80 mm, so it is close to circular.
10. **[does not affect a conclusion]** The Kiloscope bead stack's image order (file number) is not confirmed: only 72% of beads have their brightest slice within 5 slices of the listed one (cell 25). The Featherscope order is confirmed (155 of 155).
11. **[does not affect a conclusion]** The fig2d status in the notebook table ("data missing") differs from the claims file's methods_underspecified.
12. **[does not affect a conclusion]** Main nb cells 28 and 34 still hold the author's "Result" verdicts, although conclusion cells were meant to be removed.

Helper functions I tested on synthetic inputs all behaved as documented: `shuffle_columns`, `_split` (49/49 with a 1-frame buffer for n = 100), `confusion` (normalized by actual class), `decoding_matrix` (0.98 on separable data, about chance 0.26 on noise with 4 classes), `nmf_groups`, and `behaviour`.

**C. What I could not check, and the output that would have let me**

- **Whether the movie is raw:** for example, per-frame counts of zero-valued pixels at the frame edges, any NWB attributes or comments on the series, or the shifts estimated on the movie after a known synthetic jitter is added.
- **The n2 null distributions** for fig2 and ed9b (even 100 decoders), and the distribution of single-fit median accuracies for the real decoder, to put the n1 comparison on equal terms.
- **Any output at all for fig2k, fig2l and ed9c.**
- **PSF readings using, for each bead, the lower-cost of the two fits**, plus the Kiloscope readings with the 27.77 µm outlier listed.
- **Which images `sf3/*/analysis.m` actually loads for ed2b/ed2c**: the lines of the script that name the files. The notebook hard-codes one file per folder without showing that the script uses those files.
- **For ed8:** the active-footprint counts per quarter with the quarters split at the image midlines rather than the footprints' extent.
