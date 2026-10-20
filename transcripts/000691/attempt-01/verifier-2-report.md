**Verifier report, round 2: Scherrer et al. 2023 (doi:10.1038/s41592-023-01806-1), dandiset 000691 v0.260827.1358**

I took the counts from the claims file and the attempt record. There are 15 claims. The record gives 6 reproduced, 2 partially reproduced and 7 blocked. I downloaded no paper text this round, so `paper/` is empty, and I worked from my round-1 reading.

### 1. Outcomes

I agree with all 15 outcomes in the attempt record.

- **reproduced:** abstract-thousands-of-neurons, fig2-quadrant-direction-decoding, ed9b-octant-decoding, ed10-localized-activity and ed8-coactive-distributed.
- **partially_reproduced:** ed2b and ed2c.
- **blocked:** ed6a, ed6bcd, ed5, abstract-kiloscope-fov, abstract-weights, ed1-ed4 and ed3.
- **ed9c-local-decoding-map (reproduced, changed from not_reproduced): I agree, with a reservation.**
  - The exact solver follows MATLAB's documented default for 100 or fewer predictors.
  - Cell 28 meets the criterion: 19 points are significant and their scores range over 0.075.
  - The code's own variant, 64 footprints within 50 px, also passes: 22 of 34 points are significant (cell 29).
  - However, the outcome flips with the solver (1 point with SGD), and the solver was changed after the round-1 failure. The record and cell 30 both say so.

### 2. Sentences the outputs do not support

**Contradicted by the printed numbers:**
- **Cell 30, and the ed9c notes in the record:** "18 of them (12%) are significant". Cell 28 prints "significant at BH 5%: 19 (13%)".
- **Cell 30, and the ed9c notes in the record:** "liblinear reached its limit of 10,000 iterations in 2268 of the 3000 fits". Cell 28 prints "2264 of 3000".
- **Record, ed8 notes:** "The best of 4 NMF replicates was kept (errors 97.55 to 97.58)". Cell 35 prints errors of 97.79, 97.78, 97.79 and 97.8.
- **Record, ed9c response:** "with 10 per point it already takes 634 s on four cores". Cell 28 prints "computed in 358 s".
- **README:** "It takes about 24 minutes on four cores". Cell 40 prints "total run time 13.7 min".
- **Cell 36, and the ed8 notes in the record:** "The active footprints are as spread as random sets".
  - This is true only for 3 of the 8 components.
  - Cell 35 shows the event spread outside the random-set 5th to 95th percentile range for the other 5.
  - It is below that range for c1 (0.945 against a 5th percentile of 0.962) and c5 (0.956 against 0.962).
  - It is above it for c0 (1.042 against 1.037), c4 (1.055 against 1.042) and c7 (1.050 against 1.036).
  - The ed8 outcome does not depend on this, since every ratio is far above 0.5.

**Not shown by any output, though not contradicted:**
- **Cell 15:** the AVI's byte size (105,329,192) matching the Academic Torrents listing, and the session timestamp matching.
- **Cell 0:** "The draft holds the same two blobs".

**Checked and supported:**
- Every other sentence in the Result cells (18, 23, 26, 33, 39), the Summary (cell 41), the README table and the record's notes matches the outputs.
- The cell 11 statements about the sample frames match the cell 10 figure. The 102 s frame shows a gloved hand and a different view, and the 0 s frame shows the maze shifted. In the other six frames the crosses sit on the mouse.

**My round-1 reasons in the record:** they are faithful paraphrases of my report, with the problem numbers mapped correctly, and none is distorted.

### 3. Status of my round-1 points

**Resolved:**
- **Problem 4 (ed8 baselines):** random windows and random footprint sets were added. The text issue noted above remains.
- **Problem 5 (ed10):** the empirical false-positive counts reach a maximum of 62 against the observed 100. Slow non-stationarity is acknowledged.
- **Problem 6 (tracking):** jumps, small blobs, a sensitivity check and the overlay were added.
- **Problem 7 (opening frames):** shown in the cell 10 figure.
- **Problem 8:** the radius is now 45 px, and the use of the pixel size is explained.
- **ed2b/ed2c sensitivity:** radius and centre variants were added.
- **Problem 2 for fig2:** solver-checked. Part of my round-1 point was wrong: on these decoders SGD scores higher than the exact solver (0.44 to 0.54 against 0.26 to 0.32, cell 22). The claim still holds with either solver.

**What remains and bears on a conclusion:**
1. **ed9c rests on weak evidence.**
   - The outcome depends on the solver, and the choice was made after round 1.
   - The "exact" solver hit its iteration limit in 2264 of 3000 fits. In the 100,000-iteration check, 2 of 4 fits did not converge (cell 29).
   - Each z uses a null standard deviation from only 10 values. The smallest significant z, 2.53, is below the 3.40 a point needs on its own. A t-based test would mark fewer points.
   - The map was not rerun with more decoders per point.
   - The code variant uses a 60 px grid, where the claims file states 40 px.
2. **ed9b was not solver-checked.** The exact-solver check covers only the quadrant/direction decoders. With the exact solver the fig2 accuracies fall to about 0.6 of their SGD values. ed9b's margin (0.313 against a null 95th percentile of 0.144) is smaller in ratio, so its outcome under the exact solver is untested.
3. **Fig. 2 and ED9b have no paper value to compare.** The main text and the Fig. 2 legend remain unavailable.
4. **ed2c sits at the threshold.** It is 0.003 short of 0.8, and one of the four 100 µm centre shifts crosses 0.8. Partially reproduced stands under the stated criterion, but the call is marginal.
