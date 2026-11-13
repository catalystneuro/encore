The author run is complete: 28 claims recorded, the entry's checks pass with 0 errors, and the handover is built. The notebook ran from a clean environment in 1,178 s (about 20 minutes), with peak memory around 1 GB.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| gaze-anticipates-action | reproduced (rests on an assumption about the eye signal's sign) |
| gaze-anticipates-landmarks | reproduced (same assumption) |
| learning-trials | reproduced (monkey S 12.26, monkey K 16.53 / 15.82) |
| learning-to-90 | reproduced (0.898) |
| probe-transfer | not_reproduced (monkey K 28% → 58%, p = 0.07; monkey S has no probe sessions in the data) |
| probe-faster-criterion | blocked, methods_underspecified |
| cells-recorded | partially_reproduced (only the 189 analysed cells are deposited, not all 270 recorded) |
| state-space-most-responsive | not_reproduced (57 cells against 84) |
| direction-center-vs-periphery | not_reproduced |
| direction-tuning-not-maintained | partially_reproduced (15 of 40 low, the paper's 36%, but counts outside tolerance) |
| sparsity-state-vs-direction | reproduced (main reading only, assumed) |
| sparsity-state-vs-position | not_reproduced |
| state-space-selectivity | not_reproduced |
| landmark-identity-distance | not_reproduced (distance count at most 24 or 31 against 64) |
| responsive-cells, multi-space-coding, state-space-ic-higher, sparsity-gaze-vs-state, spatial-selectivity-fraction, landmark-identity-center, path-selectivity, gaze-aligned-dynamics, latency-skew, eccentricity-modulation, foveation-selectivity, gaze-map-landmarks | blocked, metadata_insufficient |
| fields-per-cell, dimensionality-control | blocked, methods_underspecified |

## 2. Dataset, assumptions, questions

**What the data show:**
- The eye signal has no units, calibration or sign. It is on a ±5000 scale in some sessions and ±5 in others. Without it the point-of-gaze space cannot be built, and that is behind 12 of the blocked claims.
- The learning-curve columns are probability, lower bound, upper bound, not the order the descriptor gives. The undocumented field `learningtrial` equals the paper's learning criterion.
- Eye samples are 200 Hz, not the 250 Hz the descriptor states.
- The rewarded arm is code 53 in only 32 of 66 sessions.
- Two hc-12 files have no new-maze data.
- hc-12 holds 12 of monkey K's 15 probe sessions and none of monkey S's 9.
- 87 of the 101 hc-21 files hold the same spike trains as hc-12 files, under other names. No claim rests on hc-21; I used it only for this overlap check and to look for the missing probe sessions.

**Assumptions:**
- A negative horizontal eye value is rightward. This rests on the optokinetic shift during turns.
- Eye values are standardized within each session before sessions are pooled.
- The main reading includes returns in the trial window and permutes the order of the 5 s chunks for the surrogates.
- The three rotational moves are the 36° alignment and 72° turns right and left.
- Counts over the paper's responsive set are bounded between the cells responsive in three spaces and all cells. I used those bounds for three claims (state-space-most-responsive, state-space-selectivity, landmark-identity-distance).

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How the surrogate chunks were shifted, and whether maps include the returns. These readings change the significant counts about two-fold.
- Which method reference 60 is, for the learning curves.
- How a positional field is defined, and how the dimensionality control was done.
- Which moves enter the state-space selectivity index, and which laps the two-way ANOVA used. The ANOVA's residual df of 756 matches only all 193 laps of session sn20110624.

**Questions to a reader:** none.

## 3. Protocol points

1. The datasets are tar.gz files, not zips, so they cannot be opened in place. I streamed each archive with `tarfile` in `r|gz` mode, reducing each member in memory as it was read.
2. The protocol doesn't say how to judge a count over a selection that cannot be formed. I used lower and upper bounds and blocked a claim only when the bounds include the expected value; it is stated in the notebook.
3. The protocol doesn't say what to do when part of a criterion can't be tested (monkey S's probe sessions). I judged probe-transfer on monkey K's values, which already fail the criterion.
4. During development I cached reduced arrays, not raw files, in `$TMPDIR` to avoid re-streaming. The protocol doesn't address dev caches; the entry itself streams the data.
5. The protocol says what a `partially_reproduced` covers only loosely. I used it for a correct proportion with counts outside tolerance (direction-tuning-not-maintained) and for cells-recorded.

## 4. Runtime and failures

The run took about 1 h 50 min, 11:51 to 13:42 UTC. Two full runs of the entry passed: 1,231 s, then 1,178 s. During development the loader failed twice, on files whose camera data or eye channels sit in other layouts; I fixed both and nothing failed after. `entry.yaml` still says 30 minutes of runtime where the actual run takes about 20; I left it so as not to invalidate the executed copy. As instructed, nothing was committed or pushed.
