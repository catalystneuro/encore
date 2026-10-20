I checked the claims file for 000691 against the paper and against the paper's code at the recorded commit (d596646b). I corrected eight claims, and I've marked the file ready.

**Checker:** `claims/000691/10.1038-s41592-023-01806-1.yaml: 23 claims, 22 quotes, 3 statistical values, 0 problems` (same result before and after my edits).

**Changes, by claim**
- **fig1e-featherscope-psf, fig1f-kiloscope-psf:** reading (c) said "the mean of the two axes' means", but the code's error-bar plot shows each axis's mean separately. I replaced it with (c) the mean major-axis width and (d) the mean minor-axis width.
- **fig2-quadrant-direction-decoding, ed9b-octant-decoding:** the Methods don't say how many fits make one null decoder, and the code has no null for these panels. The file had picked one fit. Both readings are now named (one fit, or 200 fits as for the real matrix), and the claim is `methods_underspecified` if they disagree.
- **fig2k-decoder-size:** the statement claimed that decoders of every size beat shuffled decoders, which is only one of the criterion's two readings. It now says what the paper says: accuracy depended on size, P ≤ 2.7 × 10⁻⁴ for all sizes.
- **fig2l-local-decoding-map:** the file placed footprints at their centroids. The Methods say nothing on this, and the code uses each footprint's peak pixel, so the peak pixel is now the method and the centroid is a variant. I added the null-fit count as an open detail and stated the outcome when readings disagree.
- **ed9c-local-decoding-map:** the 0.05 spread threshold had no source in the paper or code, so I removed it. The claim is now judged on whether significant and non-significant points are both present, and the spread is reported. The null-fit count is open, as for fig2l.
- **ed8-coactive-distributed:** a percentile test against 1,000 random footprint sets, and an "at least four components" rule for partial reproduction, came from neither the paper nor the code. I removed both. I kept the plain reading of "from across the FOV": active footprints in all four quarters of the field of view.
- **ed10-localized-activity:** the shuffle and binomial tests were invented; the paper picked footprints by eye. The claim is now `methods_underspecified`, like fig2d. The code's maps, entropy and peak values are still reported.

The other code details the file cites match the code.

**Still open** (all recorded under `checks`):
- **Which footprints the decoders use:** the code loads a file that may hold all 2,948 footprints, not the 2,382 curated ones. The file follows the Fig. 2 legend (2,382) and names 2,948 as a variant.
- **ed7-motion-small:** the paper doesn't give the NoRMCorre settings. The file's rigid-registration default is a choice that could move the value.
- **fig2k-decoder-size:** the paper doesn't say whether the Mann-Whitney tests are one- or two-sided. The file uses two-sided.
- **Not added as claims:** the replication in a session a month earlier (from the reporting summary), and minor design numbers in the Methods (about 20% light loss at the prism, about 3× SNR gain from the heatsink, irradiance). I judged none of these main findings.

**Ready:** yes. I made no commit and changed nothing outside `claims/000691/`.
