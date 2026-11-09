**A. Outcomes** (the claims file has 14 claims; there was no attempt record among my materials, so this list follows the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| insertion-yield | blocked (data_missing) | The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted or failed sensors (API metadata, cell 3). Figure 3 names 4 functional Monkey T sites (c8dg, c8ds, c3bs, c3a) against the paper's "3/14", so "sensor" may mean probe. Neither count can be checked. |
| chronic-duration | blocked (metadata_insufficient) | Asset metadata gives only age (P11Y, P8Y) and no implant date. The one testable part agrees: the two Monkey T sessions are 13 days apart, and 496 − 483 = 13 (cell 3). |
| fscv-waveform | partially_reproduced | Lowest potential is −0.347 V against −0.4 ± 0.04 V, which fails. Highest is 1.3395 V, sweep rate 400.46 V/s and scan rate 10.0 Hz, all within tolerance (cell 22). Three of four is partial. The dandiset description also says −0.35 V. |
| ephys-acquisition | reproduced | 30 kHz for P, 32 kHz for T, and 0.1 Hz low cut are within tolerance. The high cut is 8000 Hz, which is within 7500 ± 750 (cell 24). The 32 kHz rate is also supported by the constant raw-to-LFP offset across the session (cell 15). |
| shape-task-structure | reproduced | Forced trials are 358/1468 = 24.4%. The 8 complete blocks are 71 to 273 trials long, all within 45 to 330 (cell 26). |
| zenodo-link | reproduced | Every trial list agrees on at least 99.8% of trials; the only difference is trial 1501, missing from the Zenodo lists. The beta power correlates at r = 0.943 at a 6 ms lag (cell 28). The claims file says this criterion was written after r = 0.94 was known. |
| fig3a-dual-channel | blocked (data_missing) | The archive has no c8ds. The c8dg half can be tested and passes: the large-reward median of re-referenced da over 0 to 3 s is +1.28 (n 85, cell 32), so more than half of those trials are positive. |
| fig3a-redox-peaks | blocked (metadata_insufficient) | The raw FSCV exists, but at the stored times it does not match the trial-aligned iox (r about −0.06 to 0). A search over the whole record finds only r ≈ 0.17 to 0.20, at offsets that differ from row to row (cell 13), so the raw current cannot be placed on the trial clock. I agree with blocking. |
| fig3b-beta-bursts | reproduced | At the 75th-percentile threshold, burst rate is 1.51/s before the cue and 1.21/s after (Wilcoxon p = 9.5e-10, n 570, cell 30). The direction of the change reverses at the 50th percentile (see B3). |
| fig4a-dopamine-reward | reproduced (weak) | Large median 1.28 against small 0.19, Mann-Whitney p = 0.023 (cell 32), which meets the criterion. Several variants that do not decide the outcome are not significant (B2). |
| fig4b-beta-reward | reproduced | Over 0 to 0.5 s, large median 275 µV² against small 327 µV², p = 1e-8 (cell 34). The direction holds within left-only and right-only trials. |
| fig4c-beta-side | reproduced | Over 0 to 0.5 s, left median 245 µV² against right 301 µV², p = 1.6e-6 (cell 36). Normalising to the pre-cue baseline makes the difference stronger (ratio 0.71). |
| fig5a-spike-reward | blocked (data_missing) | Monkey P's file has no trials or events table (cell 3; API variableMeasured lists none). The spike times are present. Cell 20 refers to a Monkey P events file in the Zenodo deposit, so the claim might be testable with outside data, but not from the dandiset. |
| fig5bc-unit-isolation | reproduced | 1 of 31,246 ISIs (0.003%) is under 1 ms. The trough is −30.64 µV against noise of 5.41 µV, a ratio of 5.66, above the required 3 (cell 38). The raw spike-triggered mean (−26.4 µV, cell 19) confirms the waveform units. |

The paper gives no chance levels and the notebook trains no decoder, so there is no chance level to compare and no train/test leakage to check.

**B. Problems**

1. [does not affect a conclusion] Cell 19 hard-codes `6800.66578`, which cell 20 says comes from the Zenodo events file. The notebook never loads that file, which contradicts cell 0's "Nothing else uses outside data". The offset is used only in the spike-triggered sanity check, not in fig5bc's criterion.
2. [does not affect a conclusion] fig4a (cell 32) passes, but the evidence is weak:
   - 0 to 1.5 s: p = 0.41.
   - `da` as stored: p = 0.3.
   - iox: p = 0.41.
   - Trials 368 to 734: p = 0.51.
   - The pre-cue window shows a difference in the opposite direction (−0.73, p = 0.064).

   The result relies on re-referencing to a single sample at the cue (`rereference`) and on the first half of the session.
3. [does not affect a conclusion] fig3b (cell 30): the burst rate rises after the cue at the 50th percentile and falls at the 75th and 90th. The power is already smoothed with a 0.25 s Hanning window, so the 50 ms minimum length is nearly always met. At the 75th percentile, the drop in "bursts" is largely the same event-related desynchronisation (ERD) measured in fig4b, not separate evidence for bursts.
4. [does not affect a conclusion] fig4b (cell 34): the difference appears only in 0 to 0.5 s. The 0 to 1 s window gives ratio 1.04 (p = 0.09) and 0.25 to 0.75 s gives 0.998 (p = 0.66). `beta_power` uses a zero-phase filter (filtfilt) and centred smoothing, so the 0 to 0.5 s mean includes about 125 ms of pre-cue signal. The effect may be a difference in when the ERD starts. This matches the paper's "brief time window".
5. [does not affect a conclusion] `beta_power` runs over the joined LFP series, which has 1,497 timestamp irregularities (cell 15). The notebook never checks for steps at those joins. In a synthetic test, a 50 µV step produced a transient of about 67 µV² lasting about 230 ms, against medians of about 300 µV². The contrasts compare conditions at the same trial times, so a join artifact would hit both groups equally.
6. [does not affect a conclusion] `raw_fscv` reads the applied voltage without checking the `conversion`/`offset` attributes of the data itself. Cell 11 prints only the series attributes. The values agree with the dandiset description, so the scaling is probably correct.
7. [does not affect a conclusion] Trial 1501 is in the large-reward and right-cue selections used for fig3b, fig4b and fig4c, but not in the Zenodo lists. With 570 or more trials per group, this cannot change a result.
8. [does not affect a conclusion] fig4c treats left as contralateral, which comes from the paper. The files do not record the implant hemisphere. The pre-cue baseline also differs between sides (left higher, p = 0.013; cell 36).
9. [does not affect a conclusion] zenodo-link: the beta amplitudes differ (maxima 2184 against 1560 µV², median ratio 0.943), so the paper's filter or envelope was probably different. The criterion tests only r, and it was set after r was known.
10. [does not affect a conclusion] Part of the case for blocking fig3a-redox-peaks rests on searches the notebook says were "run while preparing (not run here)" (cell 14), so they cannot be inspected.
11. [does not affect a conclusion] Cell 24: the electrodes table stores a 8000 Hz high cut, while the dandiset description repeats the paper's 7500 Hz. The metadata is inconsistent, but 8000 is within tolerance.

I tested the helpers on synthetic inputs and they work: `beta_power` (a 20 Hz sine of amplitude 2 gives power 4.0; 10 and 40 Hz give 0), `burst_onsets`, `window_mean`, `codes_per_trial`, `rereference`/`fscv_window_mean`, `best_lag` and `reward_blocks`. The image-code counts in cell 5 (1285 + 1293 = 2 × 1110 + 358) are consistent with forced trials carrying one image code each, which `reward_blocks` assumes.

**C. What I could not check, and the output that would settle it**

- **LFP joins (B5):** where the 1,497 joins fall relative to trial start and value cue, and the size of the step at each.
- **Applied voltage scaling (B6):** `fscv_excitation_series/data` attributes (`conversion`, `offset`, `unit`).
- **c8dg half of fig3a-dual-channel:** the fraction of forced large-reward trials with a positive 0 to 3 s change. It can be inferred from the median, but it is not printed.
- **Robustness of fig4a:** the large-against-small test with a pre-cue baseline mean (for example −1 to 0 s) instead of a single sample.
- **fig3a-redox-peaks:**
  - the criterion's background-subtracted voltammogram computed at the stored times, even with the clock in doubt;
  - the neighbouring-potential searches from cell 14.
- **Offset source (B1):** loading the Zenodo Monkey P events file in the notebook, which would document `6800.66578` and allow an outside-data attempt at fig5a.
- **fig4c contralateral label (B8):** implant hemisphere for c3bs and c3a. It is not in the files or the dandiset metadata.
- **insertion-yield:** an implant log of sensors per monkey. It is not in the archive.

The paper text I read is saved in `paper/PMC12183687.xml` and `paper/PMC12183687.txt`.
