**Verifier report, round 1: Scherrer et al. 2023 (doi:10.1038/s41592-023-01806-1), dandiset 000691 v0.260827.1358**

The paper is not open access, so I used its abstract and Extended Data legends from the publisher page (saved under `paper/`). The claims file lists 15 claims. No separate attempt record was among my materials, so the counts below come from the claims file and the notebook outputs. The DANDI API shows 2 assets: the NWB file (15.2 GB) and the behaviour AVI, for one subject.

My outcomes: 5 reproduced, 2 partially reproduced, 1 not reproduced, 7 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| abstract-thousands-of-neurons | reproduced | Cell 16: all 2948 footprints have non-zero traces. No pairs merge, since the largest trace correlation is 0.77 (cell 13). The mouse visits all 4 arms. |
| ed6a-curated-footprints | blocked (metadata_insufficient) | The PlaneSegmentation has only `image_mask` and `ROICentroids` (cell 3), so there is no curation flag. 2948 is the uncurated count and cannot be compared with 2382 ± 238. |
| ed6bcd-other-mice | blocked (data_missing) | The API confirms 1 subject and 2 assets. |
| ed5-songbirds | blocked (data_missing) | No bird data in the archive (API: species is mouse only). |
| abstract-kiloscope-fov | blocked (metadata_insufficient) | The NWB file and the asset metadata give no pixel size or `grid_spacing`. At the code's 5.94 µm/px the frame would be 4.80 × 3.61 mm (cell 5), which is outside 4.0 ± 0.4 mm. That value comes from outside the dandiset, and "FOV" may mean the usable circular field, so I agree it is blocked. |
| abstract-weights | blocked (data_missing) | Weight is not data. The only weight in the file is a wrong device description ("1.0 g"). |
| ed1-ed4-resolution | blocked (data_missing) | No USAF target images in the archive. |
| ed3-adc | blocked (data_missing) | No ADC test recordings in the archive. |
| ed8-coactive-distributed | reproduced | Cell 28: all 8 events have 196 to 320 active footprints with spread ratios of 0.95 to 1.06, so 8 of 8 pass (6 needed). The same holds at thresholds 0.3 and 0.7. See problem 4 for why this test is weak. |
| fig2-quadrant-direction-decoding | reproduced | Cell 18: the median per-decoder median class accuracy is 0.415. That is above chance (0.125) and above the null 95th percentile (0.145); 50 of 50 decoders exceed it. The paper gives chance only as "white is set at chance level" (ED9b), which matches 1/8. |
| ed9b-octant-decoding | reproduced | Cell 21: median 0.313, against a null 95th percentile of 0.144 and chance of 0.125; 50 of 50 decoders above. |
| ed9c-local-decoding-map | not_reproduced | Cell 23: 0 of 151 grid points are significant at BH 5%. The best z is 1.87 (p = 0.031, q = 0.61). The code's variant (64 footprints within 50 px) gives 4 of 77 significant with a score range of 0.054 (cell 24), which would pass. The result is fragile (problems 2 and 3). |
| ed10-localized-activity | reproduced | Cell 26: 100 of 2948 footprints are localized against 29 expected, binomial p = 4.5e-25. The binomial p is overstated (problem 5), but the excess is large. |
| ed2b-featherscope-flat-illumination | partially_reproduced | Cell 30: the corrected profile drops to 0.742 at 400 µm, below 0.8. It is above total vignetting there (0.342). |
| ed2c-kiloscope-flat-illumination | partially_reproduced | Cell 30: the corrected profile is 0.797 at 1500 µm, just under 0.8. It is above total vignetting (0.253). The 0.003 margin depends on pixel size and centring. |

### B. Problems

1. [does not affect a conclusion] `decode_once`: I checked the split against the paper's code (`f3+sf8/quadrant_direction_decoding.m` at d596646). It uses train `1:N-buffer`, test `N+1:end-buffer`, a random circular shift and one-vs-all coding, and the helper reproduces this exactly. The 160-frame buffer is larger than the 30-frame smoothing windows, so I found no train/test leakage. On synthetic data the decoder reaches about 1.0 on separable classes, and its nulls fall to 0.00–0.06.
2. [affects a conclusion] `decode_once`, `SGD_EPOCHS = 10`: SGD at this very small alpha is noisy and was never checked against an exact solver on the real data. On a weak synthetic signal it gave per-decoder medians of 0.18–0.25, against 0.255 from `LinearSVC` with the same objective; 50 epochs did not help. This only lowers scores, so the passing decoding claims stand. For ed9c it lowers the real scores and widens the null spread used in the z-test, so it could explain why no point is significant.
3. [affects a conclusion] Cell 23 (ed9c): each grid point has 10 real and 10 null decoders, and all 2948 footprints are used. The paper used a curated 2382, so the 32 nearest footprints include ones the paper removed. Each point's z-test rests on a null standard deviation from 10 values. Across 151 BH tests, a point needs roughly z > 3.3 to pass. The not-reproduced result is therefore weakly powered, and the code's own variant passes (cell 24).
4. [does not affect a conclusion] Cell 28 (ed8): members are assigned by highest rank, so each component gets about 1/8 of all footprints. A random eighth already has a spread ratio near 1. 57–84% of members count as "active" in a 50 s window, and there is no comparison with a random window, so the test barely separates a real event from chance. Two event times (80.4 s and 122.9 s) fall in the first 153 s, which the behaviour analysis drops as experimenter handling.
5. [does not affect a conclusion] Cell 26 (ed10): the same 100 shifts serve as the null for every footprint, so footprint counts are correlated and the binomial p-value is anti-conservative. Circular-shift nulls also do not remove slow non-stationarity shared by activity and position. The excess (100 vs 29) is large enough that the outcome holds.
6. [does not affect a conclusion] `behaviour` / `track_mouse`: on a synthetic rectangular loop, `behaviour` gave the right rectangle, octant order 0→7, direction and speed (1.333 px/frame as expected). On the real data, though, the largest step between imaging frames is 62 px. At the 12.5 Hz video rate that is about 150 px between video frames, which looks like a tracking error. Blob areas go down to 3 px. These glitches feed into speed, and so into the "running" frames, and were not counted. The arena crop `ARENA_ROWS`/`ARENA_COLS` is hand-set, and the rectangle is fit to the 2nd–98th percentiles of position on an unrotated frame.
7. [does not affect a conclusion] Cells 1 and 9: dropping the first 1920 video frames matches the code's `CurrentTime = 64` s at the nominal 30 frames/s, which is 153 s on the true timestamps. The notebook says the experimenter is in view during those frames, but no output shows it.
8. [does not affect a conclusion] Cell 23: the radius is 45.45 px, where the criterion says 45 px. The notebook uses the code's 5.94 µm/px for ed8 and ed9c but treats the FOV claim as blocked for lack of a pixel size. Both choices are defensible, but they are not consistent with each other.
9. [does not affect a conclusion] Metadata errors in the dandiset, which the notebook correctly flags in cell 4: the device and dandiset descriptions say "optimized for weight (1.0 mm; 1.0 g)", the imaging is stored as `TwoPhotonSeries`, and the indicator and location are "unknown". The 808 × 608 frames and the 4 mm window support the notebook's reading that this is the large-FOV Kiloscope.

### C. What I could not check, and which output would have let me

- **Tracking quality:** an overlay of tracked centroids on sample AVI frames, the number of video-frame jumps above about 40 px, and the number of frames with blob area under 50 px.
- **SGD convergence on the real data:** for a few fig2 and ed9c decoders, the same split fit with an exact solver (`LinearSVC`, or more epochs) and the resulting accuracies.
- **ed9c power:** the null standard deviation per grid point, and the map rerun with more decoders per point.
- **ed8 baseline:** the fraction of members active in randomly placed 50 s windows, and the spread ratio of random footprint subsets.
- **ed10 dependence:** the count of "localized" footprints when one of the shifted nulls is treated as the observed data, which gives an empirical false-positive count.
- **ed2b/ed2c sensitivity:** the profiles at R ± 5% and under alternative centres, since ed2c misses 0.8 by 0.003.
- **Paper values for Fig. 2 and ED9b:** the main text and the Fig. 2 legend are paywalled, so I could not compare the notebook's accuracies with the paper's numbers.
- **The excluded opening frames:** frames 0–1920 of the behaviour video, to confirm the experimenter is in view.
