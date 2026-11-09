No outcome changed in this round. I'm proposing one change, for fig2c-face-best-predictor-calcium, which a third round needs to review. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook passes in 17.1 min), and the numbers came out the same in both runs.

**Proposed change of outcome**
- **fig2c-face-best-predictor-calcium:** the record keeps `partially_reproduced` and proposes `reproduced`. The verifier was right that the paper's speed is signed. The Methods define it as "a differential of distance", and the code's `wheel_changepoints.m` keeps the sign. My switch to |speed| after round 1 was a mistake.
  - The main regression now uses the signed WheelSpeed, and |speed| is a variant.
  - With signed speed, face PC1 is the best single variable in all 4 mice (Friedman p = 0.018). Its unique contribution is also the largest in all 4, though in grabAM05 only by 0.002 over pupil.

**Comparison with the paper's own values**
- I added a check against `Fig2RawData.mat` from the paper's code repository, with a small loader in `meso.py`. Rows are matched to mice by comparing full-model R² across the 23 left parcels.
- Rows 1, 3 and 4 match grabAM05, grabAM07 and grabAM08 closely (Spearman 0.94 to 0.98 for both signals). grabAM06 has no clear row.
- For those three mice, our mean full-model R² is close to the paper's. This is the first outside check of the ridge regression port.
- grabAM05 is the one mouse where the two speed readings differ clearly, and it matches signed speed: calcium wheel R² is 0.0246 in the paper's file, 0.0253 here with signed speed and 0.0483 with |speed|. grabAM07 and grabAM08 don't favour either reading.

**Corrected text**
- **Robustness without grabAM06:** the conclusion, summary and record now say:
  - calcium locomotion above high face stays significant (p = 0.019);
  - the calcium sustained-state gradient becomes significant (p = 0.037). With 2 mice that would meet the calcium half of the s7-ap-gradient-sustained criterion; the outcome stays because the criterion fixes 3 mice.
- Runtime is now given as about 17 minutes in the notebook, README and `entry.yaml`. I removed the unbacked "110 GB" figure.
- Added a data check that lists the archive's 16 NWB files by mouse and type, which backs the "6 visual stimulus sessions" statement. The text now says one per mouse is opened.
- Removed the unsupported "saturated pixels" sentence. Rewrote the unclear clock-alignment sentence so it rests on the printed lags.
- The face-onset variant now states that grabAM08 drops from 30 to 29 onsets, and says why: the thresholds are percentiles over all quiescent frames, so adding a period moves them.
- The record notes for fig2a, fig2b and fig2c-ach are updated to the signed-speed numbers. Round 2 is recorded under `verifications` with the verifier's reasons and my responses.

**Not done**
- grabAM06's row in the paper's file could not be established, so its values were not compared.
- The paper text is saved under `paper/`. That folder is gitignored, so it won't be in the commit.
- Nothing was committed or pushed, as instructed.
