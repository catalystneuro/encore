I've built the new attempt, written `attempts/000691-scherrer-2023-02.yaml` and run the handover; nothing is committed. The dandiset has only one published version, 0.260827.1358, and the draft holds the same files, so the version did not change. Every difference from `-01` comes from the rewritten claims file, not from the data.

The entry now has four notebooks, all of which pass a clean run: the main one (7 min), two decoding notebooks (19 min each) and a motion notebook (22 min), each kept under the 30-minute limit. After that run I changed only markdown text, copied it into the executed copies, and checked that every code cell is identical to what ran.

## 1. Outcome per claim (earlier outcome in brackets)

| Claim | This attempt | `-01` |
|---|---|---|
| abstract-thousands-of-neurons | reproduced (2948 footprints) | reproduced |
| abstract-kiloscope-fov | reproduced (4.800 × 3.612 mm at the code's 5.94 µm per pixel) | blocked, metadata insufficient |
| fig1e-featherscope-psf | reproduced (3.92 / 6.43 µm) | new |
| fig1f-kiloscope-psf | partially reproduced (4.42 / 5.44 µm; the centre misses its bound by 0.02 µm) | new |
| ed2b-featherscope-flat-illumination | reproduced | partially reproduced |
| ed2c-kiloscope-flat-illumination | reproduced | partially reproduced |
| ed7-motion-small | not reproduced (0.037 px RMS against 0.13) | new |
| fig2-quadrant-direction-decoding | blocked, not runnable | dropped in `-01` |
| ed9b-octant-decoding | blocked, not runnable | reproduced |
| fig2k-decoder-size, fig2l-local-decoding-map | blocked, not runnable | new |
| ed9c-local-decoding-map | blocked, not runnable | reproduced |
| ed8-coactive-distributed | blocked, methods underspecified | reproduced |
| ed10-localized-activity | blocked, methods underspecified | reproduced |
| ed1cf-field-curvature | blocked, methods underspecified (data shown) | new |
| ed6a-curated-footprints | blocked, metadata insufficient | same |
| ed6bcd, ed5, abstract-weights, ed1-ed4, ed3 | blocked, data missing | same |
| birds-singing-rate, fig2d-lman-sparse-bursting | blocked, data missing | new |

Why outcomes changed:
- **Decoding:** the paper's null leaves two readings open: one fit per shuffled decoder (n1), or 200 fits each (n2). Under (n1) both decoding claims hold: 0.437 and 0.326 median accuracy, against the largest of 1000 shuffled decoders at 0.227 and 0.229. The criterion needs both readings, and (n2) is 200,000 fits, about 38 hours here, so these claims are blocked; fig2k, fig2l and ed9c also need 4 to 11 hours each and depend on blocked claims.
- **ed8:** passes 8 of 8 events when each event is taken at its component's largest weight, and 7 of 8 with the code's event times. The two readings disagree, so the criterion makes it methods underspecified.
- **ed2b, ed2c, ed10:** `-01`'s criteria were chosen by its author (a 0.8 level; a shuffle test); the new criteria come from the paper and code.
- **abstract-kiloscope-fov:** the criterion now accepts the code's pixel sizes.
- **ed7:** the high-pass variant gives an even lower value (0.019 px), so a fixed background is not what keeps the shifts small. One explanation that fits is a movie already motion-corrected before deposit.

## 2. Findings of `-01`
All nine are still present, with output in the data check. For the code mismatch, only the footprint count (64 in the code against 32 in the legend) is a clear mismatch. The 50-pixel radius is about 270 µm at the code's other pixel size (5.35 µm), so that part depends on which size you use. The Extended Data Fig. 8 inconsistency ("Figure 3", "Fig. 2d") is confirmed in the full text.

## 3. New findings
- Nothing says whether the movie is raw or motion-corrected, and its shifts are about a quarter of the paper's.
- `ROICentroids`, described as centroids, equal each mask's peak pixel for 84% of footprints and the rounded weighted centroid for only 43%.
- The tracking code's MATLAB `unwrap` lets position drift by up to π cm per lap, which changes about 1% of labels.
- The bead scripts order images by file date, which the repository does not keep.

## 4. Where the protocol did not fit a repeat attempt
- `tools/entry.py check`, and so `all`, fails on 11 errors, all in the deprecated `-01` record: it has no outcomes for the new claims, and its ed9b and ed9c tags point to cells that moved. Since `-01` must stay unchanged, `all` cannot pass. I ran `run` directly after confirming `-02` itself has no errors.
- The repeat-attempt section assumes the claims file is kept and the dataset changed; here the claims file was rewritten and the data were not.
- The claims file sets decoding methods that need 10⁵ fits. With a 30-minute limit per notebook, those claims cannot be decided, whatever the data.
- I added no questions, and did not set `superseded_by` on `-01`.

The untracked root entries (`.bashrc`, `scripts` and others) are `/dev/null` mounts from the sandbox, not mine, so I left them.
