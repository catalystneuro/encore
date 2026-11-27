No outcome of a tested claim changed. The entry ran clean with `tools/entry.py all`: the main notebook took 57.6 min and the new subsample notebook 14.8 min. The check passes with 0 errors.

**One thing to know first.** In two conclusion cells I had written the fit timings from my development run, and the final run timed slightly differently: 1.89 s per fit against 1.62 s, and 1.08 s against 1.15 s of wall time per fit. Every other output was identical. A second 73-minute run would not have fit in the time left. So I corrected those two sentences by hand, in the source notebooks and in the executed copies, editing markdown only. Because of that edit and the `runtime_minutes` change in `entry.yaml`, the run stamp no longer matches, so the next `run` will execute the entry again.

**Outcomes**
- **Unchanged:** `data-zebrafish-coverage` (reproduced) and `figs6-train-test-uncorrelated` (reproduced, resting on the bout-threshold assumption). The verifier agreed with both.
- **fig6f-reticulospinal-behavior:** the block reason moves from `too_large` to `data_missing`, as the verifier said. 000238 holds no backfill annotation and the claim names no outside input.
- **9 simulation claims and 5 mouse claims:** the block reason moves from `too_large` to `other` (not attempted). For the mouse claims I did not use the verifier's `data_missing`, because the protocol keeps that for data that are public nowhere, and the CSHL data are public. The disagreement is recorded.
- **6 anatomical claims:** kept as `too_large`, with the disagreement recorded. The claims file marks them `with_inputs`, and the registered centroids are public on Zenodo, so the MINE fits are what blocks them.
- **12 fit claims:** still `too_large`, now with measured costs. One fit takes 1.89 s on one thread; run in parallel, the full set comes to about 130 h on four CPUs, and 261 h with the rotated controls. The record had said 2.08 s per fit, which did not match the notebook; that is corrected.

**Added or corrected**
- **Linear model on every component.** The paper's comparison model is now fit to all 434,648 bright components, matching sklearn's Ridge on synthetic data. It finds 26,326 at sqrt(0.5); the paper's figures imply about 25,300.
- **New notebook, `mine_fits_subsample.ipynb`.** It fits MINE to a seeded random subsample of 600 components. Scaled up, about 54,500 neurons are found by either model, against the paper's 42,229 (95% interval 26,700 to 86,600). The split is 37% only MINE, 51% both and 11% only the linear model, against the paper's 40/54/6. MINE is above the linear model at every cutoff from 0.05 to 0.95. These are estimates in the notes; no outcome rests on them.
- **Clock check fixed.** The collapse the verifier flagged came from my circular shift, which put a step into the last test rows on every advance. Without wrap-around the curve is smooth, with a median best displacement of +3.4 s.
- **Clock outputs the verifier asked for.** The notebook now prints the stored start times and rates (all start at 0 s) and the held-out curve at 0.2 s steps. It shows the temperature trace's extra 10.5 s lies at its end (98.3% of planes).
- **Tail timestamp finding (record finding #5).** Each of the 10 odd planes holds one 128.004 s jump in its tail timestamps. Its severity goes from minor to major, since part of each plane's tail data is misplaced by 128 s relative to the imaging.
- **Other outputs asked for:**
  - the channel descriptions (Ch0 is green GCaMP);
  - the 000238 red-channel movies (175 of 175 planes);
  - 20 timed fits, with the core count;
  - an orthogonalized-predictor variant of the inter-trial correlations, which gives the same result.
- **Behavior binning (verifier point 6).** I kept it: the paper's own `bin_time_discrete` also keeps the later bout's value when two bouts share a bin. The helper now cites this, and the notebook prints how often it happens (1,866 bins).
- **Question for a reader.** `questions/costabile-2023.yaml` asks whether the train-test criterion should test the size of the correlations, not their signed median (verifier point 4).
- **Record.** The round-1 verification is written under `verifications` for all 35 claims.

**Not done**
- The simulation and mouse claims were not attempted.
- I did not estimate the shuffle enrichment, because a 600-fit subsample would leave an expected 0.5 fits in the rotated data.
- Taylor-based estimates for `temperature-nonlinear-behavior-linear` and `interaction-terms-small` were not computed.
- The subsample was not repeated under the protocol's four extra seeds; a bootstrap over planes gives the sampling error instead.
- The subsample is 600 fits, not the 2,000 I planned. The first try's worker pool was killed while it ran alongside the main notebook, and a wait loop of mine then cost about an hour.
- The main notebook's 57.6 min is close to the 60-minute limit.

Nothing is committed.
