**A. Outcomes** (all 39 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig3k-nt-sensor-sucrose-increase | not_reproduced | The US comparison is p ≥ 0.05 in all 8 readings (cell 22: "0 of 8"). With the per-trial z-score the direction matches (late − early AUC +3.0, 4 of 5 mice up, p = 0.08). With the session z-score the effect is about zero. The criterion needs p < 0.05 under every reading. |
| fig3l-nt-sensor-airpuff-decrease | not_reproduced | 0 of 8 readings have p < 0.05 (cell 25). With the per-trial z-score the direction matches (AUC −5.5 and −4.7, p = 0.07–0.09). With the session z-score, first 16 trials, it is near zero (p = 0.76). |
| fig3-nt-sensor-early-dip | not_reproduced | 0 of 8 readings have both early US means below zero (cell 27). Sucrose is negative in the per-trial z-score readings, but airpuff is positive there (+0.11 to +0.19). |
| fig4-recording-count | partially_reproduced | Mice: 31, inside 30 ± 3. Neurons: 1902 before the 0.3 Hz exclusion and 1739 after (cell 29), both far outside 685 ± 68.5. Six sessions (H09–H14) have no neutral CS, so the 2:1:1 ratio holds in only 25 of 31 sessions (cell 5). |
| fig4d-seven-clusters | blocked (methods_underspecified) | Seven clusters appear only with reading (a) at a 41-bin smoothing window. The other 12 windows give 6–12 clusters, and reading (b) never gives 7 (cell 31). The window that "smoothing factor 0.85" implies cannot be recovered from the paper, and the count also moves with the cut fraction (cell 32: 5 to 14 clusters). The units are also not the paper's sorted neurons (cell 7). |
| fig5dh-behavior-clusters | blocked (metadata_insufficient) | The pose has no timestamps, and the best pose-to-trial lag drifts within sessions (cell 13). I accept the block only provisionally; see problem 2. |
| fig4c-photoidentification | blocked (metadata_insufficient) | No file gives the projection (NAc or CeA) per mouse, so the per-projection counts of 39 and 32 cannot be checked. I confirmed in the archive's asset metadata that genotype is "Wild type" for every subject and there is no group or projection field. The total of 71 could have been compared (problem 1). |
| ed8d, ed8fg, fig4e, ed8i, fig4fg-projector-sucrose-responses, fig4fg-control-projector-valence, fig5a, fig5b, fig5c, ed8e, fig5fi, ed8os | blocked (metadata_insufficient) | Each needs CRISPR vs control labels, projection labels, or both. Neither the asset metadata (wasAttributedTo: genotype, sex, age only) nor the dandiset description has them. |
| fig2c-pvt-bla-cko-reduces-reward | blocked (metadata_insufficient, not data_missing) | Session reading (b) is in the files: port entries on the last discrimination day, in the trial tables. Group labels are missing (problem 6). |
| fig1c, ed1c, ed2, ed3, ed5f, fig1g, fig1h, fig2d, fig2g, fig2h, fig3bc, fig3e, fig3f, ed6, fig3h, ed9, ed9kl, ed10b, ed10 | blocked (data_missing) | The archive's 85 assets are 31 ecephys NWB files, 2 pose-only NWB files, 20 NT-sensor photometry files and 32 videos. There is no anatomy, histology (despite the description), slice physiology, sequencing, freely-moving cKO or photostimulation behaviour, or GCaMP photometry. For fig3bc, the NT-sensor mice have licks but are a different cohort (N = 5, not 13) with no eye-closure data, so data_missing stands. |

**B. Problems**

1. **[affects a conclusion]** Cell 34 / `photoresponsive`: the fake-session test was never applied. Cell 11 already splits the light events into two blocks of about 427, and the Methods put the fake session first, so in H01–H29 the fake block can be identified (in H31–H42 both orders could be run as readings). Instead the pulses of both blocks were pooled, which also halves any real response. With the fake test applied, the total tagged count could be compared with the paper's 39 + 32 = 71. The figure of 1355 tagged units is therefore not a valid result of the Methods' rule.
2. **[affects a conclusion]** Cell 13 (fig5dh block): only fixed lags were scanned. A linear clock fit (offset plus frame rate) to the port entries was not tried, yet the lag drift (for example H01: −6, −31, −77 s across thirds) looks like a constant frame-rate error that such a fit would remove. Many sessions have dist_ratio ≈ 0.9–1.0, so the head-to-port minimum is poorly defined there. The video files' own frame counts and durations were not checked. Calling the pose "cannot be aligned" goes further than the evidence shows.
3. **[does not affect a conclusion]** Cells 31–32 (fig4d): clusters are dominated by single sessions. Cluster 2 is all 38 units of H27, and cluster 7 draws heavily from a few mice. Combined with the shared spikes and ISI violations in cell 7, a count of 7 would not show functional types even under the "right" window.
4. **[does not affect a conclusion]** `photometry_trials`: the regression coefficients are fitted on the trial-averaged −5 to 0 s baseline, as the Methods say, but they are never printed. On synthetic data with a nearly flat averaged baseline, the fit returned a slope of −0.07 where the true slope was 2. The motion correction may effectively be absent, which is unverified.
5. **[does not affect a conclusion]** The notebook adds a "session z-score" reading the claims file does not list. Even under the per-trial readings alone, every photometry test fails (p = 0.07–0.27), so the extra reading does not change any outcome.
6. **[does not affect a conclusion]** fig2c is given the wrong block reason (data_missing instead of metadata_insufficient).
7. **[does not affect a conclusion]** Text errors:
   - Cell 19 says "415 regressed on 470", but the code correctly regresses 470 on 415.
   - Cell 24 gives the paper's airpuff US effect as −3.52; the paper's statistics say −3.657.
   - Cell 16 says cues are "at least 29 s apart", but the M-0 airpuff early session has a 4.7 s gap (cell 15), which may be a spurious cue. That session also has only 29 cues.
8. **[does not affect a conclusion]** Cell 9: the CS-onset alignment check fails or is ambiguous in H17, H22, H27, H34 and H39. Four of these (H17 is dropped for low rate) are still used in the fig4d clustering.
9. **Possible misreading in the claims file (reported, not corrected):** fig3-nt-sensor-early-dip judges a "transient" decrease by the mean over 2–7 s. A brief dip could be averaged away; for example, the plotted early-airpuff trace reaches −0.63 even though the window mean is positive.

**C. What I could not check**

- **Group and projection labels in the NWB files:** whether `units`, the subject description or session_description hold quality, group or projection labels. The notebook printed only `genotype`. A cell listing all units-table columns and subject/session text fields would settle it.
- **Regression coefficients:** the slope and intercept of the 415→470 regression for each photometry session.
- **Fake/real tagging counts:** tagged-unit counts with block 1 as fake and block 2 as real, and the reverse.
- **Pose clock:** a per-session linear fit of pose time to trial time (offset and rate, with residuals), and the frame count and duration of each video asset.
- **Smoothing window:** MATLAB's `smoothdata` window heuristic for SmoothingFactor 0.85 on a 100- or 300-bin trace. Printing the window MATLAB actually chooses would fix the fig4d reading.
