I've revised the attempt for every point in the round-1 report and recorded the round under `verifications`. The entry's final `all` run passed with 0 check errors in 1,685 s (about 28 min, peak memory 2 GB), and the conclusions match the new numbers. I committed nothing and pushed nothing.

**Outcome changes** (from 26 reproduced, 4 partial, 5 not reproduced, 3 blocked to 35 reproduced, 2 partial, 1 not reproduced, 0 blocked):

| Claim | Before | Now |
|---|---|---|
| units-recorded | partial | reproduced (CeN 783 vs 782, Pir 1,575 vs 1,560) |
| fig3c-decay | not reproduced | reproduced (3.04, 1.78, 1.69%, all windows p < 0.05, Kruskal-Wallis p = 0.024) |
| figs5a-hpc-bla-all-cells | partial | reproduced (window 2 p = 0.011) |
| fig3d-pir-weaker-than-bla | not reproduced | reproduced (0.87% vs 3.09%, p = 0.027) |
| fig6a-safe-trajectory | not reproduced | reproduced (p = 0.060) |
| fig6b-airpuff-greater-than-safe | not reproduced | reproduced (p = 0.035) |
| fig3d-pir-reactivation | blocked | reproduced (NREM p = 0.042, REM p = 0.18) |
| fig3e-cen-no-reactivation | blocked | reproduced (p = 0.73 and 0.90) |
| figs4-intra-structure-rem-absent | blocked | reproduced (all four p ≥ 0.31) |

Still partially reproduced: fig1b-dz-speed-anova and fig1b-dz-speed-posthoc. Still not reproduced: airpuff-location-no-bias.

**Main corrections:**
- **Sleep states (problems 1 and 6, and the REM item):** I dropped the immobility substitute. Its speed came from unsmoothed positions, and pixel jitter made still periods look like movement. Each 5-s epoch now gets the state from the authors' per-state firing-rate table (StatesFR) that best explains the spike counts, inside still periods of pre- and post-sleep.
  - The check is against the authors' pair correlations, which the decoder does not use. NREM correlations match at r = 0.88 and 0.90 (the old substitute gave 0.64 and 0.59). Per-session reactivation (EV − REV) averages 3.13% against the authors' 3.21%. REM correlations match at r = 0.78 and 0.81.
  - Decoded minutes per session are shown next to the minutes implied by StatesFR (median ratio 0.95 for NREM, 1.05 for REM), as the verifier asked.
  - The 20-min decay windows now count decoded NREM time, and the authors' pre-NREM table is run as a variant.
  - This decoding is an assumption, so every outcome resting on it is marked `assumed`.
- **Rat08 structures (problem 2):** the labels are in the text of the "All" sheet of `StructureMapping.ods`, not only in cell colours, and are now read from there.
- **Air puff location (problem 3):** added a corrected-location variant (the file value where one exists, elsewhere the estimate moved back by the 7.3-cm median offset) and ran it through every behaviour claim. The estimate stays the main reading.
- **Smaller fixes:**
  - The previous-zone carry-over is fixed (4). That leaves 50 sessions, and the notebook now lists why each excluded session lacks a speed (11).
  - The mixed table-vs-substitute variant is removed (5).
  - Evidence for column 5 as REM is added: decoded column-5 epochs track the authors' REM correlations (8).
  - `_zbins` no longer drops a bin where two intervals touch, with a synthetic check in the notebook (10).
  - Laps per direction and track extent are now printed per session.
  - Problems 7 and 9 needed no change; the notes state them.

**What the round-2 verifier should weigh:**
- Several of the new outcomes sit near p = 0.05 and change with the decoder's smoothing:
  - fig3d-pir-reactivation goes partial at 30-s smoothing (REM p = 0.032).
  - fig6a-safe drops to not reproduced (p = 0.048) under both the 30-s variant and the old substitute.
  - fig3c-decay is partial with the authors' pre-NREM or 30-s smoothing, and not reproduced on the old substitute.
  - fig6b is not reproduced on the old substitute (p = 0.15).
- With the corrected air puff location and all samples:
  - fig1b-speed-ratio would be partial.
  - fig1b-dz-speed-posthoc and figs1b-ratio-each-rat would be not reproduced.

  These dependencies are in the notes, the README and the notebook summary.

**Not done:**
- Rescoring sleep from the LFP: the archives total about 470 GB, which does not fit in the 60-min notebook limit.
- No reader questions: the report found no place where the claims file misreads the paper, so `questions/crcns-hc-14.yaml` is unchanged.
- The record also has one new finding: Rat08's two structure lists disagree on one shank-day.
