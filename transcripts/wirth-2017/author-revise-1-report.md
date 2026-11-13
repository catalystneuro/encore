I've revised the attempt for round 1, re-run the entry from a clean environment with `python tools/entry.py all entries/wirth-2017` (passes in 24 min, peak memory 1 GB), and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes changed**
- **direction-center-vs-periphery:** not reproduced → partially reproduced, as the verifier proposed. Over the three-space responsive cells, which stand in for the paper's responsive set, IC is higher in the centre at p = 0.045 and sparsity at p = 0.0074. This holds only with permuted chunks, and the outcome is marked as resting on that assumption.
- **direction-tuning-not-maintained:** partially reproduced → not reproduced, as the verifier proposed. The criterion has no partial level, and the count of cells with a low correlation misses 18 to 22 under every reading.
- **state-space-ic-higher:** blocked → partially reproduced, as the verifier proposed. Two of the three comparisons need no gaze, and both give p < 0.01 under all six readings.
- **state-space-selectivity:** stays not reproduced, now marked as resting on the permuted-chunk reading. With the corrected shifted chunks the counts could fall in the target range, so under that reading the claim can't be decided.

**Disagreement kept**
- **gaze-anticipates-landmarks:** I kept it reproduced where the verifier gave partially reproduced, and recorded the disagreement. The sign of the eye signal now comes from a check that doesn't use eye position. During a turn the eyes drift with the scene, which moves opposite to the turn. The median eye velocity is positive in right turns and negative in left turns in 40 of 40 sessions of monkey K and 20 of 20 of monkey S. So a negative value is rightward, the sign the analysis assumed.

**Fixes and added outputs**
- **Shifted-chunk surrogates (the verifier's main bug):** chunks overlapped, so a cell that codes nothing came out significant. Each 5 s chunk is now rotated within itself. On synthetic spike trains that code nothing, 3.3% now come out significant at p < 0.01, against 100% for the old version. Every analysis was re-run with the fix.
- **Tail p-values:** both tails are now stored and the upper tail is shown alone. At most 3 cells are significant on the low side.
- **Third trial window:** start to reward plus the return that follows. It is almost the same as the full trial, because the trial ends at the reward.
- **State-space selectivity:** run under three groupings of the turns at the centre. The outcome does not depend on the grouping.
- **Landmark ANOVA:** the MATLAB default sums of squares (type III) are shown alongside. The distance count is at most 33 against 64 ± 6.4, so the outcome holds.
- **Gaze tests:** per-session signed-rank tests added, so the result does not rest on pooling turns within a session.
- **File layout:** checked per file. All 187 files use the 12-column camera layout. The odd orientation and abscissa ranges in two files are explained in the notebook and don't affect any analysis.
- **Learning:** the upper confidence bound at the criterion trial is added. Only one session reaches 0.9 at the criterion trial itself.
- **Probe sessions:** start-arm sequences and four variants are added. No variant brings monkey K's two means within tolerance.
- **New data finding:** in 3 of the 12 probe sessions the first entries lie on both sides of the rewarded arm. The paper describes them as the northeastern and southeastern entries.

Notes, findings, the notebook conclusions and summary, and the README now match the new numbers. Round 1 is recorded under `verifications` with the verifier's reasons and my responses.

**Not done:**
- The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/wirth-2017.yaml`.
- I did not try the vertical-channel test the verifier suggested for the eye sign; I used the eye-velocity check above.
- latency-skew stays blocked. A substitute cell set would not test the claim, which depends on gaze-aligned-dynamics.
- `tools/build_site.py` and two `tools/site_assets` files were already modified before this run. I left them alone.
