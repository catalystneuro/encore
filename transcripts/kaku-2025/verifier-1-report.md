**Verification report, round 1: Kaku, Liu et al. 2025 (doi:10.1101/2025.01.27.635041) on DANDI:001619 v0.251027.1953**

The claims file has 48 claims. I checked the archive through the API. It holds 335 files, all `*_behavior+core.nwb`, and the draft version is the same. All 31 subjects are VGAT-ChR2-EYFP mice, and no other species or genotype appears. Notebook cell 5 shows the files have no cue or photostimulation times and no videos.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| code-dataset-link | reproduced | Every input exists. 20,109 units pass get_good_units, 0.9% below 20,300 (cell 13). |
| fig1d-lick-breath-frequencies | not_reproduced | Mean lick frequency is 26.96 Hz under (a) and 8.06 Hz under (b), against 6.23 ± 0.62. Breathing is within tolerance under (a). The value under (b) is distorted by the defect in B2. |
| fig1f-inspiration-between-licks | not_reproduced | Pooled, 30.4% of in-bout inspirations fall inside a protrusion; no session has none (cell 20). Unchecked alignment, B6. |
| fig1g-lick-delayed-before-slow-breath | partially_reproduced | Over sessions: +22.0 ms, p = 4.5e-4, n = 71. Only 16 of 20 mice are positive, and over mice p = 0.18 (cell 21). |
| fig1f-licking-mode-switch | not_reproduced | The inter-breath interval rises with lick count in 116 of 117 sessions. The latency from last lick to next inspiration differs by 62.5% across groups (133, 92, 82 ms); the limit is 20% (cell 22). |
| fig1i-breath-delayed-before-slow-lick | reproduced | Over sessions: +10.5 ms, p = 1.5e-9, n = 86 (cell 23). |
| ed1-unidirectional-models-fail | reproduced (weak) | Breathing model: Fig 1i difference is 0.0 in all 162 sessions. Licking model: the Fig 1g measure exists in only 2 of 169 sessions, so "not significant" holds only by default (cell 24, B8). |
| ed2-rats-similar | blocked: data_missing | The archive has mouse data only. |
| ed1bc-licks-pause-at-swallows | not_reproduced | Lick probability is lower after swallows in only 4 of 90 sessions; it is higher (0.031 vs 0.021 per bin, Wilcoxon p = 4e-16) (cell 25). See B5. |
| fig1k-rhythms-follow-swallow-at-fixed-latency | reproduced | The latency difference is smaller than the cycle -1 difference for licks and breaths under O5 (a) and (b) (cell 26). |
| fig1l-lick-interval-preserved | not_reproduced | Under O5 (a), Δ(1,-1) = +117.9 ms, p ≈ 0. Every variant also gives p ≈ 0 (cell 27). See B4. |
| fig1l-lick-cycle-prolonged | reproduced | Under O5 (a), Δ(0,-1) = 33.36 ms, p ≈ 0 (paper 33.3 ± 3.3). Under (b) it is 4.0 ms and under (c) 11.0 ms. |
| fig1n-breath-interval-preserved | reproduced | Under O5 (a), Δ(1,-1) = -1.8 ms, p = 0.26 (cell 28). |
| fig1n-breath-cycle-prolonged | reproduced | Under O5 (a), Δ(0,-1) = 48.13 ms, p ≈ 0 (paper 48.0). |
| units-count | partially_reproduced | Total (20,109), units per probe (60.0) and mice (31) match. Insertions are 335, not 339. CB 4,157, P 3,021 and MY 8,992 are all outside tolerance (cell 15). The criterion defines no partial outcome; this is my judgement. See B11. |
| region-spike-rates | not_reproduced | CB is 21.3 and MY without VNC is 10.9, both within tolerance. VNC is 27.2 against 38 ± 3.8 under every reading (cell 17). |
| fig2-licking-breathing-tuned-counts | partially_reproduced | V3(a) matches under (i) for every V2 reading (for example 3517/1021/177). V3(b) gives 2757/602/69. The both-tuned ratios (≤5.4%, ≤18.7%) hold under every reading (cell 31). The header's disagreement rule would instead call this methods_underspecified; I followed the claim's own two-level criterion. |
| fig2-swallow-modulated-counts | not_reproduced | No combination matches. The denominator under (a), 18,494, fits; the swallow-only count is 187 to 355 against 427 ± 43 (cell 32). |
| fig2f-breathing-units-location | reproduced | PreBötC: Fisher p ≤ 0.0032 under all readings, but n = 16 (B3). Posterior-ventral IRN: p ≈ 0 (cell 33). |
| fig2g-licking-units-location | reproduced | XII, V and IRN are each enriched (p ≈ 0). The pons fraction is 15 to 20%, above the 1% threshold (cell 34). |
| fig2h-swallow-units-location | blocked: methods_underspecified | V4(a) gives 3 of 5 regions (partial) and V4(b) gives 2 of 5. Lateral of NTS and above AMB are not enriched under either reading (cell 35). |
| ed6e-swallow-latencies | reproduced | Median peak for V+IRN is -1 ms (V4(a)) and -4 ms (V4(b)); for IC+NLL it is +16 ms; Mann-Whitney p ≈ 0. IRN alone is only -1 to -3 ms, within one video frame (cell 36). |
| ed7-glm-separate-clusters | blocked: too_large (contested) | The inputs are all in the files. The O8(a) unpenalised GLM, or a subset of units, was feasible (B12). |
| ed7g-cae-better-than-features | blocked: data_missing | The files hold no raw videos. |
| ed7h-prebotc-exception | blocked: data_missing | Same reason as ed7g. |
| ed8bc-prebotc-inspiration-phase | not_reproduced | Only 4 to 5 units qualify; 2 prefer the inspiration half; Rayleigh p = 0.13 to 0.22 (cell 37). The selection is very small (B3). |
| ed8e-licking-units-protrusion | reproduced | 70.5% of units (639 of 906) prefer a phase within π/2 of protrusion. Chance is 50%, which the "more than half" threshold equals (cell 38). |
| ed8i-ipsilateral-lick-selectivity | blocked: metadata_insufficient (partly testable) | The hemisphere label is consistent: it is opposite to ccf_x in 99.3% of units, so hemispheres can be separated. Only the sign of the lick direction is unknown. A two-sided between-hemisphere test was possible (B13). |
| ed4c-licking-map-insensitive-to-sorting | reproduced | 2,366 units above 500 µV (paper 2,223 ± 222). Spearman ρ = 0.94, p ≈ 0 (cell 39). |
| fig3a-premotor-regions | blocked: data_missing | The premotor data are from reference 43 and are not in the dandiset. |
| fig3b-licking-units-in-premotor-regions | blocked: data_missing | Needs the premotor contours from reference 43. |
| fig3ce-descending-stimulation-rhythmic-licking | blocked: data_missing | No ALM or latSC mice; the cued task is absent. |
| fig3dfh-projections-and-rhythm-site | blocked: data_missing | No Phox2b mice and no fibre-site data. |
| ed10-site-classes | blocked: data_missing | Same reason as fig3dfh. |
| fig4b-artificial-licking-keeps-lick-timing | blocked: data_missing | The cued task with ALM photostimulation is absent. |
| fig4c-artificial-licking-breath-timing | blocked: data_missing | Same reason as fig4b. |
| ed11b-alm-breathing-rate | blocked: data_missing | Same reason as fig4b. |
| fig4e-licking-units-anticipate-breath | reproduced, under the header's rule that one O2 reading suffices | Under O2(a), all O1 and V3 readings give +54.5 to +60.7 ms with p ≈ 0 (for example 660 positive vs 40 negative). Under O2(b) only 2 to 9 units qualify. The measure is biased by construction (B1). |
| fig4f-breathing-units-anticipate-lick | reproduced, as fig4e | +33 ms, p ≈ 0 under O2(a); 1 unit under O2(b) (cell 40). Same bias (B1). |
| fig4d-simultaneous-recordings | blocked: data_missing (my reading) | The notebook finds only 1 to 2 recordings in 1 to 2 mice, against 43 in 21. ED Fig 12c and the claims header place these recordings in the cued task, which is not deposited. Under the notebook's O3 box it would be not_reproduced. |
| fig4g-licking-breathing-pairs-correlated | blocked: data_missing | Depends on the fig4d pairs. The notebook gives no reason in the record available to me. |
| fig4g-symmetric-lags | blocked: data_missing | Same reason as fig4g. |
| ed12c-correlation-without-licking | blocked: data_missing | Needs the cued-task baseline period. |
| fig4h-fewer-correlations-outside-oscillator | blocked: data_missing | Same reason as fig4g. |
| fig5b-voluntary-lick-latency | blocked: data_missing | The cued task is absent. |
| fig5c-preemptive-breath-adjustment | blocked: data_missing | Same reason as fig5b. |
| fig5e-photostim-lick-latency-longer | blocked: data_missing | Same reason as fig5b. |
| fig5f-artificial-licking-late-breath-adjustment | blocked: data_missing | Same reason as fig5b. |

### B. Problems

1. **[affects a conclusion]** Peak-difference measures (`_peaks`, `unit_peak_diffs`, `peak_diff_lick_behv`). The slow-group window starts later than the fast-group window: 0.16 vs 0.12 s (Fig 1g), 0.16 vs 0.10 s (Fig 4e), 0.02 vs 0 s (Fig 4f). Any peak falling in the gap gives a positive "slow minus fast" with no real effect.
   - I tested this on synthetic units with identical firing in both groups and a random split. With the peak at 0.11, 0.13 or 0.15 s, the difference was about +170 ms in 200 of 200 runs. With the peak at 0.18 or 0.22 s it was about 0.
   - The windows come from the claims header (the paper's code). The notebook ran no random-split control, so fig1g, fig4e and fig4f cannot be told apart from this artefact. This is a weakness in the claims file's method, which I am reporting, not correcting.
2. **[affects a conclusion]** Cell 19, `within_trial_freq` with `in_bouts`. Under fig1d reading (b), two consecutive onsets in adjacent bouts are counted as one interval. Adjacent bouts are often split by a 1 to 2 frame likelihood flicker, which produces 147 Hz intervals; the lick SD is 14.9 Hz. Per-session median lick frequency is 6.13 Hz, so dropping between-bout pairs could bring the mean within tolerance.
3. **[affects a conclusion]** Cell 33, `prebotc`. The AMB box is built from the positions of 87 labelled units, which gives a medial-lateral extent of only 180 µm (|ML| 1320 to 1500), not from the CCF annotation. The notebook does not state this as an assumption. The preBötC region ends up with 16 units, identical at 300 and 500 µm. This drives ed8bc (n = 5), fig4d, and fig4e/f under O2(b).
4. **[affects a conclusion]** `swallow_intervals`, cycle 1 = `post[1] - post[0]`. For licks, Δ(0,-1) matches the paper exactly (33.36 vs 33.3 ms) and the breath values match too, yet lick Δ(1,-1) is +118 ms against the paper's P = 0.649. This points to a different cycle-1 definition or to unfiltered pauses after the swallow. It was not investigated.
5. **[affects a conclusion]** ed1bc, a criterion issue in the claims file. `detect_swallows` keeps a swallow only if a lick follows the swallow peak within 0.25 s. The criterion's window (0 to 100 ms after onset) therefore partly selects for licks. The notebook shows only the window mean, not the full trace.
6. **[affects a conclusion]** Cells 10 and 20, airflow-to-video alignment. The share of inspirations inside a protrusion ranges from 8.5% to 42% by subject, and is about 10% in DL029 to DL034. The shifted-trial check failed to establish the clock for breathing in 4 subjects. No lag check was done. This bears on fig1f and every lick-breath timing claim.
7. **[does not affect a conclusion]** `peak_diff_lick_behv`. `unit_fast = i1[:40]` and `unit_slow = i2[-40:]`, with cycles sorted longest first, select the 40 cycles nearest the median on each side. The claims header asks for the 40 fastest and 40 slowest.
8. **[affects a conclusion]** Cell 24, the ed1 simulation.
   - The licking-model Fig 1g measure exists in 2 of 169 sessions, and the reason is not shown.
   - The `keep` line is dead code (`| True`).
   - Inter-lick intervals come from fig1d reading (b), which includes the flicker intervals of B2, while inter-breath intervals come from reading (a). This mix is not stated.
9. **[does not affect a conclusion]** Cells 40 and 41 run only filter order 4. V2(b) was not run for fig4e, fig4f or fig4d.
10. **[does not affect a conclusion]** Cells 6 and 7. In 19 files the histology table has more rows than units (up to 67 extra), and rows are matched to units by position.
11. **[affects a conclusion]** units-count. 1,222 units in the arbor vitae, plus the cerebellar peduncles and sptV, are counted in no division. With the arbor vitae, CB is 5,385, within tolerance. The paper's three counts sum to exactly 20,300, so the paper assigned every unit to one of CB, P or MY. The criterion's "with their subregions" may misread the paper.
12. **[affects a conclusion]** ed7 is blocked as too_large with no estimate of the cost, and no subset or O8(a) run was tried.
13. **[affects a conclusion]** ed8i is blocked, although `process_session` already computes `lick_tips` and `lick_counts` and the hemisphere labels are internally consistent. The between-hemisphere difference was testable without knowing the left-right sign.
14. **[does not affect a conclusion]** fig4g, fig4g-symmetric-lags and fig4h are marked "blocked (see the record)" with no reason in the notebook.

### C. What I could not check, and what output would settle it

- **Fidelity of the code port.** I could not see the paper's analysis code, so I could not confirm the lick cycle-1 definition, the `n_trial` selection, or the bout and swallow logic. Showing the cycle -1, 0 and 1 distributions for lick events, and the fraction of cycle 1 above 1/3 s, would settle B4.
- **fig1d.** Frequencies with between-bout pairs and intervals under 2 frames excluded, plus a count of such pairs.
- **fig1g, fig4e, fig4f.** The same statistics with a random split of cycles in place of the fast/slow split, as a null.
- **ed1bc.** The full lick-probability trace from -300 to 300 ms around swallows and around expirations.
- **fig1f.** Per subject, the cross-correlation lag between the airflow and the jaw or tongue traces.
- **ed1.** For the licking model, the per-session counts of two-lick cycles per half and whether a peak was found in each window.
- **O3 regions.** The AMB and IRN extents from the CCF annotation volume. For fig4d, the number of two-probe sessions with any units near the preBötC on one probe and in the posterior-dorsal IRN/PARN on the other, regardless of tuning.
- **3D tracking.** Whether the 3D `idx` field counts from 0 or 1 relative to the DLC `trial` field (this matters for ed8e and lick angles), and why only 211 of 335 files have (trials - 1) × 1471 rows.
- **Archive.** The API metadata cannot show whether any of the 162 two-probe sessions are the paper's 43 simultaneous recordings.
