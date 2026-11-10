**A. Outcomes** (all 22 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| rsc-dataset | not_reproduced | Sessions 14 and mice 3 match, but the files hold 638 units (main cell 9). That is 11.9% above 570, outside the 10% band. Exactly 570 units enter the Fig 5F test (cell 11), so the paper's "570 recorded" is probably the analysed count. The archive description copies 570, but its "31–71 per recording" matches the files. |
| fig5f-rsc-pmr-onset | reproduced | Reading (a): tau = −0.2748, p = 8.1e-21, n = 570, within 0.028 of −0.28 (cell 11). Reading (b) could only be run on its rate half: tau −0.33 to −0.34, p < 1e-18. All 14 sessions are negative with p < 0.05 (cell 12). |
| fig5c-posub-pmr-onset | reproduced | tau = −0.1772, p = 3.7e-17, n = 1,096, within 0.019 (posub cell 9). With A3708 dropped: −0.1945. With the event files used as they are: −0.126, outside tolerance. |
| fig5d-isomap-pmr | reproduced | \|R\| = 0.865 under the Methods window and 0.875 under the code's window, p ≈ 0 (posub cell 11). |
| fig1e-delay-range | reproduced | Reading (b), 1st to 99th percentile: exactly 5 to 100 ms. Reading (a): 0 to 110 ms (posub cell 13). |
| fig1g-dv-sequence-du | reproduced | Main: DU W = 1, p = 6.1e-5; UD W = 38, p = 0.13; U = 51, p = 0.004. This matches the paper almost exactly (posub cell 15). Fragile: see problem 3. |
| fig1h-ventral-down-longer | reproduced | Ventral is longer with all units (W = 12, p = 0.011) and with EX units only (W = 3, p = 0.0019) (posub cell 21). |
| fig1b-no-dv-tuning-gradient | not_reproduced | HD information as the Methods formula gives it (bits/s) varies with depth: tau = 0.082, p = 5e-5. Speed, AHV, RVL and peak rate behave as claimed (RVL 0.061 / p = 0.003, peak rate 0.077 / p = 1.4e-4) (posub cell 23). The bits/spike variant is not significant (p = 0.099), so the outcome turns on the unit; see problem 5. |
| figs1j-dorsal-ventral-same-hd | reproduced | All 4 readings give p ≥ 0.05 (0.19 to 0.98), on 14–15 sessions; 1–2 sessions had fewer than 10 usable bins (posub cell 25). |
| figs1i-du-more-stable | blocked (methods_underspecified) | The readings disagree: first/second-half Pearson gives W = 51, p = 0.40, while the other three readings give p < 0.05 (posub cell 17). The two odd/even readings are also invalid (problem 1). |
| figs1kl-not-firing-rate | blocked (methods_underspecified) | Only z-scored with signed comparison holds. z-scored with absolute comparison gives p = 0.065 for position against rate; both raw readings fail (posub cell 19). |
| fig2f-gamma-travels | blocked (methods_underspecified) | DU-aligned readings: DU differs from 0, but UD also differs (p ≈ 6e-5) wherever it can be tested. Delta-peak readings: DU does not differ (p 0.39 to 0.60). No reading meets the full criterion (lfp cell 7). |
| figs2d-lfp-spike-agree | blocked (methods_underspecified) | 6 of 8 readings are positive with p < 0.05; the two |Hilbert| delta-peak readings are not (p 0.13, 0.07). Only one reading is within tolerance: R = 0.59 (lfp cell 10). |
| figs2e-speed-similar | not_reproduced | Spike speed matches the paper only when computed as the slope of depth on delay (6.97 against 6.72 mm/s). Under that definition all 8 LFP readings differ (p ≤ 0.028), and no LFP mean falls within 9.89 ± 5.51 under any of the 16 readings (lfp cell 12). It inherits the LFP problems in 2 and 9. |
| fig5e-fc-pmr-onset | blocked (too_large), not established | The 66 min estimate assumes reading all 27 archives one after another from a single stream (main cell 15). See section C. |
| figs2g-adn-synchronous | blocked (metadata_insufficient), confirmed | In DANDI:000056 the units table is only id/spike_times; electrode-group locations are "unknown"; Mouse32-140822 is absent. Only the PoSub half could be computed. |
| fig1j-down-resets-hd | blocked; not supported by the archive | DANDI:000939 holds spikes, head direction (HD), wake epochs and UP states, and makeRing.py exists in the code. This claim could be tested. |
| fig1k-hd-stable-at-onset | blocked; not supported by the archive | Same data as fig1j; the claim is testable. |
| fig3-other-gradients-fail | blocked (other) | MATLAB model, no data. |
| fig3f-ih-gradient | blocked (other) | MATLAB model, no data. |
| fig4d-sag-gradient | blocked (data_missing) | Ex vivo data not deposited. A DANDI search for "Peyrache" finds only 000056, 000939, 000987, 001676 and 001699. |
| figs4-no-other-gradients | blocked (data_missing) | As fig4d. |

**B. Problems**

1. **[does not affect a conclusion]** posub cell 7, `halves(..., "odd_even")`. The UD PETH (`peth_events(sp, hd[k]["start"], hu[k])`) keeps only spikes from the same-parity UP states. The UP state just before each DOWN start belongs to the other half, so the −150 to −5 ms part of the PETH is empty or badly depleted.
   - A synthetic test confirms it: the full data and first/second halves recover UD; odd/even gives a pre-event PETH of 0.00 and NaN for every unit.
   - This explains the two NaN sessions and the low UD correlations (median 0.28) under odd/even, which bias that reading towards "DU more stable".
   - The figs1i outcome stays blocked, because the first/second-half Pearson reading already fails.
2. **[affects a conclusion]** lfp cell 3. In A3705 and A3711 the LFP is shorter than the spike record (11,168 vs 16,199 s; 9,499 vs 12,177 s), and there is no gamma rise after DU (ratio 1.000 and 1.007, equal to the 0.5 s-shifted control). A3708 is the same (1.045 vs 1.048 shifted).
   - All three sessions are still used in figs2d, figs2e and fig2f. Their DU delays span the whole search window (A3705 and A3711: 0 to 148.8 ms, lfp cell 8).
   - This changes the figs2d R values and the figs2e speeds.
3. **[affects a conclusion]** posub cells 4–5 and 15. The fig1g result depends on how A3708 is handled. With the event file as it is, or with the session dropped, UD gives p = 0.048 and the criterion fails. The pass relies on DOWN/UP states re-detected with the RSC procedure (not detectDOWNs_PoSub.py) for that one session. Replacing the event file is justified by the failed clock check (rate in DOWN 455 Hz vs 335 Hz NREM), but the result should be reported as fragile. fig5c is also sensitive: −0.126 with the event files as they are.
4. **[does not affect a conclusion]** posub cell 5. The event-file clock was checked only coarsely: rate inside DOWN states against the same intervals shifted by 0.5 s.
   - Re-detection matches only 5–11% of the file's DOWN states in A3701, A3710 and A3716, and 38% in A3713.
   - The fine offset scan was run only for A3708.
   - A constant offset of tens of ms would pass the coarse check but shift every delay in a session. That would bias the pooled measures (fig5c, fig5d, fig1e), though not the per-session depth correlations.
5. **[affects a conclusion]** `hd_metrics` / posub cell 23. The fig1b outcome turns on the unit of HD information.
   - The Methods formula gives bits/s, and under it the claim fails.
   - The paper itself filters cells by HD information in bits/spike (Isomap: "0.2 bins/spike") and cites Duszkiewicz et al. for it. Under bits/spike all five correlations come out as the paper reports them.
   - The claims file does not name this as an open detail. This is a gap in the claims file, not a coding error; the notebook ran both.
6. **[affects a conclusion]** Depth convention (posub cell 14). "Larger rel_y is dorsal" is assumed from probe convention and from Figure1H.py's `pd.cut` labels; no file metadata was checked. If it is reversed:
   - fig1g would show ventral units first;
   - fig1h would show dorsal DOWN states longer;
   - the RVL and peak-rate correlations in fig1b would change sign.

   That every claim matches the paper under this convention supports it, but this is not independent evidence.
7. **[does not affect a conclusion]** posub cell 19, figs1kl.
   - The raw reading (from the claims file) compares coefficients in different units (s/µm against s/Hz), which is not a meaningful comparison.
   - Position was oriented "ventral = positive" so that the claim's direction gives a positive coefficient. This choice decides the signed reading.
   - The outcome stays blocked either way, because the two z-scored readings disagree.
8. **[does not affect a conclusion]** fig5f reading (b): the trough-to-peak half of the EX rule cannot be applied. I confirmed the RSC units table holds only electrode_group, group, id, location and spike_times. Every subset tested is strongly negative.
9. **[does not affect a conclusion]** `lfp_event_averages`, delta peaks. The Methods are applied literally (positive peaks above 3 s.d., middle channel chosen by the author). This yields only 0.37–4.76 peaks per minute (23 in A3706), against thousands of DOWN states. The delta-peak readings are therefore noisy, which feeds the disagreement in fig2f and figs2d.
10. **[does not affect a conclusion]** posub cell 3. In A3711, A3717 and A3723, NREM epochs extend 3,500–5,100 s past the last spike; this is printed but not discussed. Intersecting with the home-cage epochs hides it. The version's release note says sleep-scoring indexing was fixed, so the time base may still be off. It feeds `nrem_rate` (figs1kl) and the A3708 re-detection.
11. **[does not affect a conclusion]** Main cell 0 and posub cell 0 list fig1b, figs1j, fig2f, figs2d and figs2e as blocked, but they are tested in posub_000939.ipynb and posub_lfp_000939.ipynb.
12. **[does not affect a conclusion]** `load_fcx_session` would use UPDOWNINtervals, whereas the fig5e criterion says SlowWaves events (as Figure5E.py). This would be a deviation if fig5e were run.

**C. What I could not check, and the output that would settle it**

- **Depth convention.** Needs the description of the electrodes `rel_y` column, or the probe channel map with the index of the most dorsal site, printed for 000939.
- **Event-file alignment in every session.** Needs a cross-correlogram of the re-detected DOWN starts against the file's DOWN starts, in 5 ms steps over ±0.5 s, for each session.
- **Whether the A3708 NWB file is the recording of event file A3708-200317b.** Needs `session_description` and `session_start_time` printed, with the recording length set against the event file's time span.
- **LFP alignment for A3705, A3711 and A3708.** Needs the LFP `starting_time` and rate, plus a DU-triggered gamma average per session against its shifted control. Also needed: fig2f, figs2d and figs2e rerun without those three sessions.
- **Whether fig5e really exceeds the time limit.** Needs the tar member order in one fcx-1 archive, and a timing of parallel streams. Within this round I could query only DANDI, not CRCNS.
- **fig1b under bits/spike as the main measure, and the smoothing of the tuning curves.** I could not check these against the paper's figures; the plots were not inspected.
