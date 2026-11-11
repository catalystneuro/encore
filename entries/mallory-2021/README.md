# Mallory, Hardcastle et al. (2021) from dandiset 000053

Tests the findings of [Mallory, Hardcastle et al. (2021)](https://doi.org/10.1038/s41467-021-20936-8)
that can be tested on [DANDI:000053](https://dandiarchive.org/dandiset/000053/0.210819.0345). The
head-fixed Neuropixels recordings with eye tracking (Figures 4 to 7) are tested with the paper's LN
model. The freely moving findings (Figures 1 to 3) rest on head pitch and roll, which the dandiset lacks,
so they are tested on the paper's figshare deposits (Dataset 1, doi:10.6084/m9.figshare.13425392.v1,
and Dataset 2, doi:10.6084/m9.figshare.13425017.v1): the head posture distributions and the claims on the
Cohort 1 LN model (one reading of its open details) are tested, and the claims that need the LN model on
Cohort 2 are blocked as too large for the time limit.

| Claim | Outcome |
|---|---|
| The paper's 11 head-fixed recordings can be found in the dandiset (link) | Reproduced |
| Eye movement ranges (Fig. 4f to i) | Reproduced |
| 711 of 2861 cells encode eye movements (Fig. 4j) | Reproduced |
| Eye cells conjunctive with body position or speed (Fig. 4k) | Reproduced |
| No nasal or temporal preference of Eh cells (Fig. 5a) | Partially reproduced |
| No up or down preference of Ev cells (Fig. 5b) | Reproduced |
| Stability of eye position tuning against body position (Fig. 5) | Partially reproduced |
| Linear Eh cells most stable (Fig. 5a v) | Reproduced |
| Low-order Ev cells more stable (Fig. 5b v) | Partially reproduced (rests on folds in turn; reproduced under random folds) |
| Linear eye velocity cells and their nasal preference (Fig. 6) | Partially reproduced (rests on folds in turn) |
| Nonlinear asymmetric Eh dot cells prefer temporal movement (Fig. 6) | Not reproduced |
| Eye velocity stability against body speed (Fig. 6) | Not reproduced |
| Asymmetric eye velocity cells more stable (Fig. 6 v) | Partially reproduced (rests on folds in turn) |
| Body variables contribute more than eye variables (Fig. 7a, b) | Reproduced (rests on folds in turn and one held-out fold; fails under random folds) |
| Model fit over 2191 cells (Fig. 7c) | Reproduced |
| No clustering of eye tuning curves (Fig. 7e) | Not reproduced |
| Peaks and valleys of eye velocity curves near 0 (Supp. Fig. 7e) | Partially reproduced |
| Shuffling finds nearly all LN eye cells (Supp. Fig. 4, eye part) | Not reproduced |
| Model and raw eye tuning curves agree (Supp. Fig. 5, eye part) | Reproduced |
| Correlation contributions, eye part (Supp. Fig. 9) | Partially reproduced |
| Shuffle false positives, eye part (Supp. Fig. 3) | Blocked: too large |
| Head pitch, roll and azimuthal velocity distributions (Fig. 1b, figshare) | Reproduced |
| 63 of 179 Cohort 1 cells encode head direction (Fig. 1c, figshare) | Reproduced |
| 46 pitch and 53 roll cells (Fig. 1c) | Not reproduced (37 and 43) |
| Few pitch and roll velocity cells (Fig. 1c) | Reproduced |
| Conjunctive coding in Cohort 1 (Fig. 1d) | Partially reproduced |
| Pitch and roll tuning shapes (Fig. 2a, b iii) | Not reproduced |
| No up or down pitch preference, no left or right roll preference (Fig. 2a, b) | Reproduced |
| Pitch, roll and head direction equally stable (Fig. 2a, b v) | Reproduced |
| Shuffling finds nearly all LN head cells (Supp. Fig. 4, Cohort 1 part) | Not reproduced |
| Model and raw head tuning curves agree (Supp. Fig. 5, Cohort 1 part) | Reproduced |
| Freely moving findings that need the Cohort 2 LN model (azimuthal head velocity, Figs. 2c, 3, Supp. Fig. 9) and Supp. Fig. 3 head part | Blocked: too large |
| No-landmark track (Fig. 8c, e) | Blocked: data missing |
| Left and right hemispheres | Blocked: metadata insufficient |
| No false detection of eye tuning in simulated data (Supp. Fig. 12) | Blocked: too large (now run; reproduced, proposed for the next round) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The dandiset does not say which of its 20 head-fixed files are the paper's 11 recordings; the paper's
figshare deposit (doi:10.6084/m9.figshare.13426103.v1) is read in place to find them. In two files
the spike index of the first unit has wrapped at 2**16; the helper repairs it. The attempt record,
with the reasons and the differences from the paper's method, is
[`attempts/mallory-2021-01.yaml`](../../attempts/mallory-2021-01.yaml).

- `freely_moving_mallory_2021.ipynb`: the freely moving data on figshare, their check, the head
  posture distributions and the Cohort 1 LN model claims (about 44 minutes). The Cohort 1 LN outcomes rest on the deposit's clock alignment, which the notebook's check could not establish, and on readings (1a, 2a) only.
- `reproduce_mallory_2021.ipynb`: the data check, the link, and every tested claim under the main
  readings of the LN pipeline (about 48 minutes, most of it the LN fits of 2861 units).
- `readings_folds_mallory_2021.ipynb`: every head-fixed LN claim again with 10-s sections assigned to
  folds at random (about 42 minutes). Under it fig7ab no longer holds and fig5bv would be reproduced, so both, with fig6 linear and fig6v, are marked as resting on folds in turn. The reading with each variable clipped to its range was not run, for time.
- `simulated_eye_mallory_2021.ipynb`: Supp. Fig. 12, spike trains simulated from each eye cell's model without its eye terms and the LN pipeline rerun (about 41 minutes).
- `mec_ln.py`: loading, the spline LN model with its forward search, model-derived tuning curves,
  stability, contributions and shape measures. Other notebooks on this dandiset can import it.
- `mec_free.py`: loading of the figshare freely moving data and the open field LN model (spline 2D
  position, circular head direction), run here on Cohort 1.
