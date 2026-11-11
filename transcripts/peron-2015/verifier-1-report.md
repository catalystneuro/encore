**A. Outcomes** (all 43 claims in `peron-2015.yaml`; the notebook tests 2 and blocks 41)

| Claim | My outcome | Reason |
|---|---|---|
| results-trials-per-session | reproduced | Cell 24: the pooled mean over 5 sessions is 290.2 and the mean of 3 per-mouse means is 272.5. Both are inside 245 ± 71 = [174, 316], and so is the "trials with imaging" variant (238.6). This rests on only 5 sessions from 3 mice, far fewer than the paper's imaging sessions, so the agreement is weak evidence. |
| results-whisking-amplitude | partially_reproduced | Cell 26: none of the three listed readings lands in [42.2, 68.8]. They give (a) 74.7, (b) 29.0 and (c) 26.9. Two unlisted variants do (cell 27): the 1–99 percentile range gives 49.2 and 2 × the Hilbert peak gives 53.7. Reading (a) is inflated by ±90° tracking errors (problem 1). The qualitative part, "well above ~20°", holds for every full-sweep measure. n = 3 of 8 mice. |
| table-s1-roi-counts | blocked (data_missing) | Archive checked: 5 sessions from 3 of the 8 mice. Cell 21 counts 72%, 20% and 63% of the Table S1 values, because most sessions are not deposited. The spared-whisker part can be tested for those 3 mice, and D2, D3, D2 match (cell 7). |
| fig2-core-counts | blocked (metadata_insufficient) | The ROIs carry no class or layer labels (cells 5 and 22). The contents of `idStrs` and `idStrsDetailed` were never printed (C1). |
| results-gaba-fraction, fig2e-fraction-imaged, fig1e-days-to-criterion, fig1g-early-stereotypy, supp-trim-all-chance, figs4-dendrite-soma | blocked (data_missing) | The archive listing confirms that the Gad2 mouse, the high-resolution stacks, training sessions and training videography, the trimming data and the L5 soma–dendrite pairs are all absent. |
| fig4d-gaba-reward-cue | blocked (data_missing / metadata_insufficient) | No GABAergic mouse and no column labels. |
| fig3a, fig3b, fig3c, fig3d ×4, discussion-principal-exclusive-classes, fig4d-sample-epoch-principal, fig7 ×3, fig8b, fig8de, results-di-magnitude-similar, discussion-correlation-more-touch (17 claims in the notebook's row, including figs3d) | blocked (metadata_insufficient + data_missing) | There are no layer, class or column labels (M6 rule). There are no calcium events, which M2, M3 and the M5 shuffle null need, and M1 forbids re-running the detector. |
| figs3d-neuropil-correction | blocked (too_large / metadata_insufficient) | The notebook's reason ("no events") is incomplete. The criterion allows events to be re-extracted, and the archive holds registered TIFFs (165 GB) plus ROI masks, so raw ROI and neuropil fluorescence could in principle be rebuilt. It stays blocked because the claim needs L2/3 labels. |
| fig4-neuropil-sample-principal, figs5-l4-neuropil-correlation, fig8e-l4-neuropil-direction-map | blocked (data_missing / metadata_insufficient) | There are no L4 axon mice. Neuropil ROIs could be drawn from the TIFFs, but the claims also need column labels. |
| fig6 ×7, figs7-direction-stable | blocked (data_missing) | No imaging during learning. an197522 is a learning mouse, but its deposited sessions are volume-imaging sessions with no training-day index. |
| fig8h, fig8i, fig8jk | blocked (data_missing) | No anesthetized mice. |
| methods-event-detection | blocked (data_missing) | The data are outside this data set (the claims file says `data: elsewhere`). |

**B. Problems**

1. [affects a conclusion] `whisking_amplitudes` (reading a), cells 26 and 27. The max − min range is computed on angles that contain tracking-error samples at ±90°. My synthetic test confirms that one ±90 pair turns a 40° range into 180°. The data show the same pattern: the per-trial maximum is 179.8°, and an229717 has 0.063% of samples above 85°, where its range is 99.2° against 60.3° when trimmed. Fixing this needs a reading (a) that drops only the artefact samples. The notebook substitutes a 1–99 percentile trim instead, which also clips real whisk peaks. The outcome depends on this choice: 74.7 fails, 49.2 passes.
2. [affects a conclusion] `whisking_amplitudes` (reading c). The per-trial maximum of |hilbert(filtfilt(...))| over the whole trial is inflated by filter and Hilbert edge effects (about 10% on a clean synthetic sinusoid: 22.0 for A = 20) and by artefact spikes (per-trial maximum 92.3). The 2 × Hilbert variant that passes (53.7) is therefore biased upward. The 6–30 Hz band is an assumption; other bands are shown (22–30), which is adequate.
3. [does not affect a conclusion] Cells 26 and 27. The variants that pass are not readings the criterion lists, and the notebook marks them as such. My partial outcome rests on them plus the qualitative part, not on the criterion's own rule. Under the strict criterion the outcome would be not_reproduced.
4. [does not affect a conclusion] Cells 19 and 20. For an197522_2013_03_10 the imaging and trial clocks could not be confirmed to agree (only 3 of 9 subvolumes peak at the true alignment). No tested claim uses dF/F, but any future dF/F analysis would inherit this.
5. [does not affect a conclusion] Cell 0. The blocked reason for figs3d skips the raw-TIFF route the archive offers.
6. [does not affect a conclusion] Claims file. The opening comment gives a 1 s sample epoch, while the Figure 1C legend says "1 to 2 s". The data show 0.84–1.18 s (cell 9), so nothing tested changes.
7. [does not affect a conclusion] Cell 24 / results-trials-per-session. The 5 deposited sessions may not be a representative sample of the paper's imaging sessions. The notebook does not discuss this.

**C. What I could not check**

1. Whether `idStrs`, `idStrsDetailed` or the `dffTSA` `descr` strings carry layer, class (red nucleus) or column information. The notebook lists the field names but never their values. Printing the unique values per subvolume would settle the M6-based blocks.
2. Reading (a) after removing only the |angle| > 85° samples, the count of affected trials per mouse, and per-mouse medians of each reading. These would settle problem 1.
3. Reading (c) with edge-trimmed windows, for example excluding 0.2 s at each end of the trial (problem 2).
4. Whether the session `.mat` trial list covers the whole behavioral session or only the imaged part. The trial-ID range against BControl numbering, or a printout of the first and last trial IDs, would show this.
5. The contents of one imaging tar beyond the notebook's note that it holds "45 TIFFs and nothing else". I did not download any data. The archive listing I queried (146 files, 165 GB) matches cell 3.
