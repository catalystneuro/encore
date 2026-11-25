**Verifier report: kim-2026-learning, round 1 (DANDI:001868 v0.260715.2016)**

The claims file has 39 claims. The notebook tests 21 and treats 18 as blocked; 21 + 18 = 39. I did not re-run the notebook. Two things I did instead:
- **Helper tests on synthetic inputs** (in a temporary venv with numpy, scipy and pandas):
  - `trough_to_peak_ms` and `time_to_max` give the right values.
  - `latency_jitter` (a) recovers a 4.0 ms locked latency.
  - `pulse_locking` labels Poisson spikes with no locking as pulse-locked 2–3% of the time, against a nominal 1%.
  - `cluster_test` gave 0 of 40 false positives under a paired null.
- **Archive queries:** dandiset and asset metadata only, through the DANDI API.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| fig2a-threshold-decrease | reproduced | Cell 19, reading (b): early median 5.78 µA, late 4.07 µA, both within tolerance; p = 1.0e-7. Under reading (a) the late median (3.69 µA) is outside tolerance. |
| figs1e-response-time | reproduced | Cell 21: late response times are lower. Trials pooled: 192 → 179 ms, p = 2.8e-11. Channel-session medians: p = 0.0026. |
| figs5-movement-onset | reproduced | Cell 23 (5 mice): Mouse 1 is the fastest at 128 ms (125 ms at 4–6 µA). All hits 148 ms (143), late 137 ms (135); all within tolerance. Late is lower than early, p = 2e-76. This rests on an estimated wheel threshold (problem 7). |
| fig4h-unit-counts | not_reproduced | Cell 25: 999 recorded units, 724 pyramidal and 275 interneurons by trough-to-peak, all within tolerance. But 588 modulated units (tolerance 436–532) and 402 modulated pyramidal (280–342) are outside it, under every variant run. Both histograms are bimodal. |
| figs3-modulation-all-cells | partially_reproduced | Cell 27: modulation is higher late at 4, 5 and 6 µA (p = 7e-5, 0.009, 4e-4), and latency is lower at 5 µA (p = 0.004). At threshold, modulation is not stable: p = 2.6e-5 under reading (a), 5e-6 under (b). Two of three parts hold. |
| fig4g-modulated-count-mouse1 | not_reproduced | Cell 29: Mouse 1 at 4 µA gives one-sided p = 0.057 (the n of 8 and 21 match the paper). The pooled group test gives p = 0.08, as required. The Mouse 1 condition fails, so it is not even partial. |
| fig4ij-pyramidal-drive | reproduced | Cell 31, stored cell-type label. Pyramidal modulation rises at all three currents (p ≤ 9e-4). Pyramidal latency falls at 5 µA (p = 3e-4) and 6 µA (p = 0.025). Interneuron modulation p is 0.33, 0.88 and 0.089. With trough-to-peak recomputed, pyramidal latency at 6 µA gives p = 0.059, which would make it partial (problem 5). |
| fig5d-pl-identity-stable | reproduced | Cell 33: 0.839 of pairs keep their identity, 0.839–0.852 across the 5 seeds, all above 0.8. There are 906 pairs against the paper's 729, and the pulse-locked share is inflated (problem 2). |
| fig5e-pyramidal-in-pl | partially_reproduced | Cell 35: pulse-locked units are 73.9% pyramidal (within tolerance) and Fisher p = 8.7e-5. Non-pulse-locked units are 55.7% pyramidal, outside the 44.8–54.8 band in 4 of 5 seeds. The criterion defines no partial outcome; I chose partial because direction and significance hold. |
| figs4b-conduction-velocity | not_reproduced | Cell 37: latency slopes are about zero or negative (4 µA: −0.66 ms/mm and −1.04 ms/mm under the two readings). No velocity is in 0.18–0.30 m/s under either reading or any seed. The contact-to-unit distance mapping was never checked (problem 6). |
| fig5fg-pl-modulation-latency | partially_reproduced | Cell 39: pulse-locked modulation rises at all three currents (p ≤ 0.0016). Latency falls at 5 µA (p = 0.003) but not at 6 µA (p = 0.058–0.083 across seeds). |
| figs4de-npl-no-change | reproduced | Cell 41: 0 of 6 tests are significant at the main seed. Two of the four other seeds give 1 of 6 (4 µA modulation, p = 0.044 and 0.046), so the result is fragile. |
| fig5h-pl-spike-probability | partially_reproduced | Cell 43: 6 µA rises (p = 0.011; 0.006–0.014 across seeds). 5 µA does not (p = 0.39–0.67). |
| figs5-pre-movement-window | reproduced (reading-dependent) | Cell 46, reading (i): pulse-locked modulation rises at all three currents, and no non-pulse-locked current is significant. Reading (ii), which is closer to the code's recomputation, has non-pulse-locked modulation significant at 4 µA (p = 0.037) and 6 µA (p = 1.9e-4), so it fails. |
| figs7-control-no-change | not_reproduced | Cell 49: at 5 µA, pulse-locked peak spike probability falls, p = 0.001 (1 of 6 tests significant). The non-pulse-locked arm has n = 1 per phase and cannot be tested. The control windows are assumptions (problem 3). |
| fig6c-kl-divergence | partially_reproduced | Cell 51: non-pulse-locked separation exceeds pulse-locked in both phases under both readings. Pulse-locked KL *falls* from early to late (p_FDR around 1e-108, all seeds). Non-pulse-locked KL rises only under reading (b). |
| fig6d-npl-hit-miss-divergence | not_reproduced | Cell 53: pulse-locked responses have significant clusters in both phases (340–380 ms early; 580–620 ms late). Non-pulse-locked onsets are 170–180 ms early and 70 ms late, against 65 ± 10 and 35 ± 10, under both bin readings. |
| fig6f-pl-coupling-increase | reproduced | Cell 58: pulse-locked coupling rises 0.27 → 0.68, p_FDR = 0.0016. Non-pulse-locked p_FDR = 0.18. Same pattern across all 5 seeds. |
| fig6f-npl-higher-coupling | reproduced | Cells 58 and 60: non-pulse-locked coupling is higher than pulse-locked early (p_FDR = 4e-12) and late (1e-10), at all seeds. |
| figs9-coupling-controls | partially_reproduced | Cell 62: (A) pulse-locked-to-pulse-locked coupling rises, p_FDR = 6e-4. (B) In the 120 ms window, non-pulse-locked exceeds pulse-locked in both phases (p_FDR ≤ 5e-7). (C) The controls have 1 non-pulse-locked response, so it cannot be tested. |
| figs2ef-control-stable | not_reproduced | Cell 64: the control count of activated neurons falls from 12.5 to 2.0 (p = 0.0038), so the claimed stability fails. The density test is blocked, and the comparison is confounded by which mice fall in each phase (problem 9). |
| fig2b, fig2c, fig2d, fig2e-density-200um, fig2e-activation-radius, fig2g | blocked (metadata_insufficient) | Cell 10: volumetric dF/F has 6–8 samples per trial with −1 placeholder values, and no labelling of which samples are pre-stimulus. No stimulation-site position is given. I accept this, with the reservation in C. |
| fig3b, fig3df, fig3e, fig3i, fig3j-subgroup-increase, fig3j-subgroup-divergence, fig3lm, fig3n-new-vs-enhanced, fig3n-vs-week0, figs6 | blocked (metadata_insufficient) | Planar ROIs have no identity across sessions. The archive lists no image series (variableMeasured has only PlaneSegmentation, ImagingPlane, OpticalChannel), so PatchWarp cannot be run. |
| fig4d-waveform-separation, figs8-tracked-units | blocked (data_missing) | Units hold one single-channel 90-sample mean waveform each (cell 4), and asset metadata list only Units. Files are about 67 MB each, 7.5 GB in total, with no raw or per-spike data. |

**Blocked claims, checked against the archive:**
- **Waveform claims:** confirmed that the data are not there.
- **Planar tracking:** confirmed that there are no mean images and no image series. Two parts could be partly tested without tracking, on all activated ROIs per session (a declared deviation from "tracked"):
  - fig3i readings (b) and (c);
  - the recruitment reading (b) of figs6.
- **Volumetric claims:** see C.

**Paper misreading:** none found in the claims file.

**Chance level:** the paper states none. The notebook's pulse-locking null is the 99th percentile; my synthetic test gives about 2–3% false positives rather than 1%.

### B. Problems

1. [affects a conclusion] **Pre-stimulus window length.** `PRE_S = 0.7` in `icms.py` is an assumption: the paper gives no length and the code's `timing_params.json` is missing. No other length was run. It sets every modulation call, z score and the delta spikes. This matters for fig4h (modulated count about 10% above tolerance) and fig4g (p = 0.057 against 0.05).
2. [affects a conclusion] **Pulse-locked share far above the paper's.** About 80% of selected responses are pulse-locked (cell 16, 0.805–0.811). The paper's n imply about 63% for units (Fig 6F: 1393 pulse-locked vs 816 non-pulse-locked) and higher pulse-locked n in Fig 5F. Here non-pulse-locked responses are 440 of about 2,260 (cell 39). The class imbalance inflates "PL all" in fig5d and shrinks the non-pulse-locked samples in figs4de, figs5 and fig6c/d. The notebook does not investigate it: no distribution of peak latencies, which would show artifact-like peaks just after blanking, and no check that spikes inside the blanked 0–1.5 ms window are absent.
3. [affects a conclusion] **Control stimulation table looks incomplete** (cells 6, 48; `control_responses`). In cell 6 the summed rates show 10 bursts at 0.5 s spacing (0 to 4.5 s), e.g. ICMS45 2022-03-04. The table lists 3 bursts per trial, ending at 1.2 s. The control analysis uses only the 3 tabled bursts and an assumed 600 ms pre-window. This bears on figs7 and figs9(C), and explains the high "+2 s" fractions in the cell 8 clock check for controls.
4. [affects a conclusion] **figs5-pre-movement-window turns on which responses enter** (cell 46). The claims file cites code that recomputes responses in the 120 ms windows, which is reading (ii), and reading (ii) fails. Reading (i) reuses the 700 ms selection and is the notebook's own construction. Only reading (i) passes.
5. [affects a conclusion] **Inconsistent cell-type rule** (cells 25 vs 31, 35). fig4h uses recomputed trough-to-peak as its main reading; fig4ij and fig5e use the stored label as main. The claims header specifies trough-to-peak ≥ 0.45 ms. The two agree for only 90% of units. Under trough-to-peak, fig4ij would be partial.
6. [affects a conclusion] **figs4b distance never validated** (cell 37). Distance assumes the stimulation table's `stim_channel` and the electrodes' `channel_name` number the same contacts. ICMS100's stimulation channels are absent from the electrodes table (cell 4), so the mapping is suspect. No check was made, e.g. that a unit's distance is 0 when it sits on the stimulation contact.
7. [does not affect a conclusion] **Wheel threshold is an estimate** (`movement_onsets`). It is the median deviation at the recorded response time, an assumption. All three medians land within tolerance (148 against an upper bound of 148.5), so the absolute values depend on it.
8. [does not affect a conclusion] **fig2a session-threshold comment is wrong** (cell 19). It says a session with a non-finite block has no threshold. Pandas `mean` skips NaN, so only infinite values propagate. As a result the "main" and "variant" agree under reading (b).
9. [does not affect the direction] **figs2ef phase composition** (cell 64). ICMS48 appears only in the early phase (medians 67 and 46), and ICMS56's week-0 session has 1 ROI. No 800 µm limit was applied. Per-mouse tests were not run.
10. [does not affect a conclusion] **Pulse-locking seed.** The classes use fig5d's seed for every claim rather than each claim's own seed. Results are stable across the 5 seeds, except the borderline cases in figs4de.
11. [does not affect a conclusion] **Effect-size sign.** `mw(late, early)` prints r negative when late is higher; magnitudes are comparable to the paper's.
12. [does not affect a conclusion] **fig6d smoothing** (cell 53). Each trial is smoothed with a 20 ms Gaussian before the median, an assumption. Smoothing can only move onsets earlier, and the notebook's onsets are already later than the paper's.
13. [may affect a conclusion] **figs3 at-threshold drops currents** (cell 27). Responses exist only at 4–6 µA, so channel-sessions whose rounded threshold is 3 µA (common late) are dropped, though that current was given.

### C. What I could not check, and what output would settle it

- **Volumetric block.** The full `DfOverF_Volumetric` description attribute: cell 10 prints only its first 200 characters. I also need the column list of the behavioural mice's PlaneSegmentation tables (any activation or distance columns). These would show whether the sample layout, or activation itself, is documented and fig2c/fig2g are partly testable.
- **Cause of the pulse-locked excess.** A histogram of `peak_ms` for pulse-locked responses and the share of stimulation-window spikes within 0–1.5 ms of a pulse.
- **Pre-window sensitivity.** fig4h counts and the fig4g Mouse 1 p with pre-windows of 0.3 and 0.5 s.
- **Control bursts.** The control spike rate for 0.5 s spacing over each tabled trial's full 5 s, plus the control trial table (`rep_num`, timing). This would decide whether the extra bursts belong to the trial.
- **Contact mapping.** For each mouse, the stimulation channel next to `electrodes.channel_name`, and the units whose peak channel equals the stimulation channel together with their computed distance.
- **Threshold reading.** psignifit's own threshold parameter (the midpoint of the sigmoid before guess and lapse rates are applied) for fig2a reading (a). psignifit is not installed here, so I could not test `fit_threshold`.
