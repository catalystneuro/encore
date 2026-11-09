I re-ran the claims affected by the three answers. One outcome changed: imaging-depths went from not reproduced to reproduced. The other two answered claims stay blocked, for clearer reasons now. `entry.py check` and `all` pass, the notebook ran in 695 s, and the handover is built in `executed/000037-gillon-2023/handover/`. Nothing is committed or pushed, and I did not verify my own work.

| Question | What the answer changed | Claim | Earlier outcome | Outcome now |
|---|---|---|---|---|
| imaging-depths: is 60 µm meant to fail? | L2/3 dendrites now pass at any depth from 50 to 75 µm, not only 50 or 75 | imaging-depths | not reproduced | reproduced |
| fig5-example-responses: which Gabor panel does the rule use? | The criterion now has three readings (panel a, panel b, both) and blocks the claim if they disagree | fig5-example-responses | blocked (methods underspecified) | blocked (methods underspecified) |
| | Nothing in its own test; it stays blocked because its parent does | fig5-consistent-vs-inconsistent | blocked, through fig5-example-responses | blocked, through fig5-example-responses |
| fig7c-high-correlation-fraction: the number of mice, and what "each session" means | Reading (a) pools over the two analysed mice; reading (c) needs every local session inside the range; per-mouse sessions are no longer a reading | fig7c-high-correlation-fraction | blocked, through fig7c-correlations-similar | blocked, through fig7c-correlations-similar |

- **imaging-depths:** all 50 sessions now pass. The three sessions of mouse 433414 are at 60 µm, which is inside the range; under the old criterion only 47 passed. Table 2 still gives 75 µm for that mouse, and that difference stays recorded under table2-sessions and as a finding.
- **fig5-example-responses:** with robust-scaled traces the rule holds in 2 of 4 planes with panel a and 3 of 4 with panel b, both partially reproduced. With both panels it holds in 1, which is not reproduced. The readings disagree, so the claim stays blocked, now because the criterion says so. With unscaled traces (the variant) they also disagree: 2, 4 and 2 planes. I added a cell that computes the rule under each reading.
- **fig5-consistent-vs-inconsistent:** its own test would give partially reproduced under either reading (2 of 4 and 3 of 4 planes).
- **fig7c-high-correlation-fraction:**
  - The test already used the two mice, so the deviation saying the criterion counted three is gone.
  - No reading is inside 0.005 to 0.015%. Pooled it is 0.0178%; the mean of the sessions is 0.0176%; the three sessions are 0.0211, 0.0276 and 0.0043%.
  - The two mouse sessions inside the range (0.0054 and 0.0067%) no longer count, now that per-mouse sessions are not a reading.
  - Its own test would give not reproduced, but it stays blocked because fig7c-correlations-similar is blocked.

Each of these claims' notes in `attempts/000037-gillon-2023-01.yaml` says what its answer changed. I also updated the notebook's conclusions, header and summary table, and the README. The run took 695 s against the 431 s recorded before, so I raised the runtime in `entry.yaml` from 8 to 12 minutes.

The totals are now 24 reproduced, 1 partially reproduced, 1 not reproduced (table2-sessions) and 9 blocked.
