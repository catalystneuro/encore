The checker reports `claims/wirth-2017.yaml: 28 claims, 28 quotes, 25 statistical values, 0 problems`, both before my edits and after. No claim id was changed, and nothing was committed.

**Changes, by claim**
- **Header (Method W) and path-selectivity:** the file said no chance rate gives the paper's p = 0.37 for 1 of 42 cells. That was wrong. At a chance rate of 0.05, the chance of 1 or fewer is 0.372. I corrected both places; the value is still reported, not judged.
- **gaze-anticipates-action and gaze-anticipates-landmarks:** the criteria demanded p < 0.001 in each monkey. The Results give a single p, so testing each monkey separately and pooling both monkeys are now two readings.
- **probe-faster-criterion:** both readings were flawed.
  - Reading (b), trials until the first correct trial from a new entry, is not the paper's learning criterion (lower confidence bound above 1/4).
  - Reading (a) used the session's running learning curve, which in most sessions is already past criterion when the new entries come in (trials 37 and 60 in the S3C examples).
  - The new readings start a learning curve when the new entries are introduced, using either all trials or only the trials from new entries.
- **sparsity-state-vs-position (also used by sparsity-gaze-vs-state):** the per-cell significance level of 0.05 had no source in the paper. It is now two readings, 0.05 and 0.01.
- **fields-per-cell and gaze-map-landmarks:** the source pointed to paragraph 4 of "What is encoded in hippocampal cell activity"; the sentences are in paragraph 3.
- **gaze-map-landmarks:** the "excess activity" measure is not the paper's. It is now marked as a standard choice and a deviation.
- **spatial-selectivity-fraction:** added a third reading, cells with significant position information among the 111 responsive cells.

The other claims' statements, statistics, expected values and methods hold against the paper.

**Still open**
- **S1 Appendix is missing.** It is a DOCX and is not under `paper/`. Without it, fields-per-cell and dimensionality-control cannot be judged, and the two gaze-behaviour claims rest on the S2 Fig legend alone.
- **Learning-curve method unknown.** The method comes from the paper's reference 60, but the stored text has no reference list, so it cannot be named.
- **landmark-identity-distance:** the paper gives p < 0.001 for 14 of 111 interaction cells, but at a chance rate of 0.05 the value is 0.0013. The chance rate for these counts is unclear; the criterion does not judge this test.
- **No claim for one minor finding:** that gaze was drawn to the rewarded path and the landmarks (Fig 1H). Its method is in S1 Appendix A1.

**Ready:** yes. I marked the file `ready: true`; supplying S1 Appendix would settle the claims that depend on it.
