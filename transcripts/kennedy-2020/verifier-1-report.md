# Verifier report, round 1: Kennedy, Kunwar, Li et al. 2020, Nature 586, 730–734, on DANDI:001182 v0.240827.1656

The claims file (`kennedy-2020.yaml`) lists 39 claims. The notebook tests one, `imaging-cell-counts`, and treats the other 38 as blocked.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1de-rat-persistent, fig1de-toy-weaker, fig1fgh-headfixed-rat-strongest, ed1-urine-looming, ed3c-openfield-photometry, ed3de-openfield-vs-headfixed, ed3fi-kinetics-track-thigmotaxis, fig1r-tettox-faster-decay, fig1q-tettox-peak-unchanged (9) | blocked, data_missing | These are fiber photometry claims, and the claims file says photometry is not part of the dataset. I queried the archive: it holds only the 15 `sub-M*-session*_behavior.nwb` files, all with the same layout (cell 7), and the only deposit is the microendoscope traces. A DANDI search found no other dandiset for this paper. |
| fig1km-thigmotaxis, ed2abc-no-lingering-odor, ed2e-chr2-thigmotaxis, fig1j-silencing-reduces-avoidance, fig1lmn-silencing-before, fig1lmn-silencing-after, ed3b-velocity-unchanged, ed3j-eyfp-control (8) | blocked, data_missing | Open-field, home-cage and optogenetic behaviour are not in the dandiset. The only annotation channel is "Ch1: baseline" (cell 7). |
| ed4d-glutamatergic-connectivity, ed4g-follower-cells | blocked, data_missing | Slice physiology and slice imaging are not in the dandiset. |
| ed6-ephys-heterogeneous | blocked, data_missing | Silicon probe data are not in the dandiset. |
| imaging-cell-counts | partially_reproduced | Summed over the 5 mice, cells per day are 203, 183 and 176. That is a mean of 187.33 with an SEM of 8.09 over the 3 days, against 187.3 ± 8.1, so this part is within tolerance (cell 20). The 78 tracked cells cannot be measured: the files hold no cross-day registration, no IDs and no footprints, and cell 17 finds no index-matched identity (0 of 15 day pairs at p < 0.05). The criterion needs both counts, so the claim is only partly reproduced. |
| fig2cd-population-persistent, fig3ab-uss-persistent, fig2jo-diverse-peak-times, fig2hi-rat-mouse-overlap, fig3gj-uss-intermingled, fig3k-few-stimuli-per-cell, fig3l-mostly-excited, ed7b-habituation, fig4cd-autocorrelation, fig4g-rat-uss-specificity (10) | blocked, metadata_insufficient | Each needs stimulus onset times and stimulus identity, and the files have neither: `stimulus/presentation`, `stimulus/templates`, `intervals` and `acquisition` are all empty (cells 5 and 7). M3–M5 have no annotation at all. The steps the notebook finds at about 100 s spacing could at most suggest segment edges, not stimulus labels; I agree that inferring the stimuli from the responses would be circular. fig3gj also has no footprints. |
| fig3n-pca, fig3m-decoder, ed9-persistent-decoding, ed7cd-identity-across-days, ed7e-strong-cells-stable (5) | blocked, metadata_insufficient | Same as the row above, and these also need cells tracked across days, which the files lack. |
| fig4e-models-dynamics, fig4h-models-specificity, fig4ijk-two-models (3) | blocked, other (depends on blocked claims) | Each depends on fig4cd and/or fig4g, which are blocked. The model side (code inputs) could be simulated, but the criteria score models against the mouse curves, so no outcome can be reached. |

That makes 38 blocked and 1 partially_reproduced. The paper states no chance level for a selection that applies here.

## B. Problems

1. **[does not affect a conclusion] Header table, cell 0.** `imaging-cell-counts` is listed only as "Tested (tracked count not measurable)", with no outcome. Under the criterion, which requires both counts, it can only be partially_reproduced.
2. **[does not affect a conclusion] Cells 5–6: dataset identity rests on the cell count alone.** The file metadata contradict the paper: "VMHvl" against VMHdm/c, "GCaMP6m" against GCaMP6s, and "DF/F" against an "a.u." unit. Every file also states 11 Hz, and no mouse stands out as the 20 Hz one. The notebook reports these mismatches but does not test them further, for example by comparing the frame-to-frame autocorrelation timescale across mice to find a resampled mouse. The near-exact match of 187.33 ± 8.09 is good evidence that these are the paper's cells, so the count holds.
3. **[does not affect a conclusion] Cells 13–14: segment counts not reconciled with the protocol.** Each file shows about 13–20 large shared steps at about 100 s spacing. The protocol gives 10 presentations plus 3 baseline epochs per day, and the notebook never checks whether those numbers fit. Doing so would show whether segments could map to trials, but without stimulus labels the blocked outcomes would stand either way.
4. **[does not affect a conclusion] Cell 7 prints dataset names but not values.** The values of `general/subject/description`, `identifier`, `general/keywords` and `general/experimenter` are never shown. Any of them could hold a stimulus order or a note; the asset metadata I fetched (keywords "ophys, behavior, male") suggest they do not.
5. **[does not affect a conclusion] Cell 20: upper bound only.** The tracked-cell bound of 158 (the fewest cells on any day, summed over mice) is correct and is not used as a test.
6. **[does not affect a conclusion] Claims file reading.** No misreading found. The summed-over-mice reading of 187.3 is confirmed by the data.

## C. What I could not check

- **Helper functions not tested on synthetic inputs.** There is no numpy, h5py or remfile in my environment. I checked `cells_per_day` by hand from the printed table: mean 187.33, SD 14.01, SEM 8.09 with ddof = 1, all correct. I did not run `step_counts`, `mean_step` or `max_cross_file_correlation`.
- **File contents seen only through the notebook.** Without downloading I could not open the NWB files. I rely on cell 7's tree dump to confirm there are no stimulus or ROI entries. The archive API (asset list, version and asset metadata) agrees with it: 15 files, approach "behavioral approach", variables BehavioralEpochs and ProcessingModule only.
- **Outputs that would have helped:**
  - The values of every string dataset in `general/` and of `identifier` for each file.
  - A per-mouse estimate of the effective sampling rate, to identify the 20 Hz mouse.
  - A count of the ~100 s segments per file set against 10 trials plus 3 baselines.
