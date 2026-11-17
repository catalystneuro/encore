I re-ran the claims the answer changed, but most of them are still blocked. The Cohort 1 LN model hit the 60-minute limit for a notebook cell and its outputs were lost. What did get tested: fig1b was reproduced from the figshare deposits, and two of the new head-fixed eye claims were tested on the dandiset (one reproduced, one not). The check passes with 0 errors, all three notebooks pass, and the handover is in `executed/mallory-2021/handover/`. Nothing is committed and I did not verify my own work.

**How the run was done.** The three notebooks take about 130 minutes together, more than the 2-hour limit on one foreground command, so I ran them in three separate runs with `entry.yaml` cut down to one or two notebooks each time. I then restored `entry.yaml` and joined the three results into `executed/mallory-2021/result.json` by hand. I wrote the conclusion cells after the runs and made the same markdown edits in the source and executed copies; no code or output was changed. One development run was briefly started in the background by mistake; it finished, and no recorded number comes from it.

**The question** (fig1c-head-direction-cells: should the freely moving claims be `data: elsewhere`?). The reader said yes. Every freely moving claim moved to figshare Datasets 1 and 2, and supp3, supp4, supp5 and supp9 were each split into a head part (figshare) and an eye part (dandiset).

| Claim | Before | Now |
|---|---|---|
| fig1b-head-posture-distributions | blocked, data_missing | **reproduced**: 8 of 8 values within the sem (pitch 11.45 / -23.03 / 55.57 deg, roll -0.76 / -50.92 / 43.63 deg, head velocity -389.82 / 385.01 deg/s over 25 mice) |
| fig1c-head-direction-cells, fig1c-pitch-roll-cells, fig1c-pitch-roll-velocity-rare, fig1d-conjunctive-head, fig2-pitch-roll-shapes, fig2a, fig2b, fig2-pitch-roll-stability | blocked, data_missing | blocked, too_large: the Cohort 1 LN model under the four readings stopped at 3600 s, with no time left to split or repeat it |
| fig1c-azimuthal-velocity-cells, the five fig2c claims, fig3ab, fig3c, fig3e | blocked, data_missing | blocked, too_large: they also need the LN model on the 1021 Cohort 2 cells, estimated at about an hour per reading on four cores, and the Cohort 1 model did not finish |
| supp3-low-false-positives | blocked, data_missing | head part: too_large (six more Cohort 1 LN runs). Eye part: too_large (six more head-fixed runs, about 3.5 h) |
| supp4-ln-conservative | blocked, data_missing | head part: too_large. Eye part: **not reproduced**. Shuffling finds more cells than the LN model for all four eye variables, but within-cell shuffling recovers only 0.72, 0.61, 0.79 and 0.78 of the LN cells, where the criterion needs 0.9 |
| supp5-model-raw-tuning-agree | blocked, data_missing | head part: too_large. Eye part: **reproduced**, with medians 0.911, 0.930, 0.850 and 0.896, all four within tolerance where three were needed |
| supp9-correlation-contributions | blocked, data_missing | head part: too_large (depends on fig3ab). Eye part: too_large, because it needs a rerun of the 35-minute head-fixed LN fits with a changed fitting routine |

**What else changed in the entry**
- **New notebook and helper:** `freely_moving_mallory_2021.ipynb` (7 min) and `mec_free.py`. The helper loads the figshare data and holds the open field LN model, which ended up not being run.
- **`mec_ln.py`:** `forward_search` now takes a list of variables (the default behaviour is unchanged), and there are new shuffle and raw tuning curve helpers.
- **Main notebook:** new supp4-eye and supp5-eye sections.
- **Record:** the README, `entry.yaml`, and the record's inputs (the two figshare deposits) are updated.

**New findings in the record**
- In figshare Dataset 1, head direction is in radians, although its description says degrees.
- Two sessions from different mice (Fuschia 052001 and Daisy 052001) have identical body position, speed and head direction.

**Clock check.** The check of a shared clock between spikes and the freely moving behaviour was inconclusive; the notebook says so. fig1b uses behaviour only, so it does not depend on the clock.
