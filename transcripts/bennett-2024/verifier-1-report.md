# Verification report: SHIELD (Bennett et al. 2024) on DANDI:001051 v0.260922.1827, round 1

The claims file has 46 claims. The notebook tests 30 and treats 16 as blocked.

My outcomes: 13 reproduced, 7 partially reproduced, 5 not reproduced and 21 blocked. The blocked count is the 16 the notebook blocks plus 5 claims I judge methods_underspecified.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| link-code-tables | partially_reproduced | All 87 sessions are found, and type, mouse and genotype agree for 99 of 99. The sessions failing are named in the next sentence. Five sessions have a different unit count (1176989662, 1178693650, 1179911454, 1180266229, 1181096406), and in those five plus 1178460518, 55–99% of units differ on max_drift and firing_rate (cell 11). |
| fig3b-surgical-outcomes | blocked (data_missing) | The archive holds only 666 ephys/LFP NWB files; there are no surgery records. |
| fig3c-isi-through-implant | blocked (data_missing) | No ISI images in the archive. |
| fig3d-histology-intact | blocked (data_missing) | No histology in the archive. |
| tracks-rare-bleeding | blocked (data_missing) | No histology in the archive. |
| fig3fh-mri-deformation | blocked (data_missing) | No MRI in the archive. |
| fig3i-learning-similar | blocked (data_missing) | Only EPHYS_1 to EPHYS_4 sessions; no training sessions. |
| fig4b-units-areas-per-session | reproduced | 1821.0 (SD 341.9) units and 28.11 (SD 5.12) areas over 44 six-probe sessions (cell 18). |
| figs4ab-insertions-per-mouse | partially_reproduced | Insertions per mouse are 20.28 under reading (a) and 21.41 under (b), both within 20 ± 4.1. Implant holes are not in the data (metadata_insufficient). |
| scale-mice-sessions-insertions | reproduced | 25 mice, 87 sessions and 507 insertions, which is within 467 ± 46.7. The 467 insertions also present in the code's table match exactly (cell 14). |
| penetration-success | reproduced | 5.83 under (a) and 5.84 under (b), both within 5.46 ± 0.546. The value 5.46 itself is not recovered by any count. |
| fig4b-trajectory-consistency | blocked (metadata_insufficient) | The NWB probe and electrode-group attributes, and the asset metadata, have no hole or orientation (cell 76; archive API). |
| fig4c-drift-discontinuities-rare | blocked | Judged by eye with no rule. Also, the NWB has no per-spike depths, so no drift map can be built; data_missing applies as well. |
| fig4d-unit-drift | reproduced | Medians 25.05 µm (SHIELD) and 22.82 µm (VBN) against 25.1 ± 0.1 and 22.82 ± 0.05 (cell 22). |
| fig4d-qc-metrics-comparable | not_reproduced | Reading (a): 0 of 7 metrics non-significant. Reading (b): 5 of 7 medians within 10% (amplitude_cutoff ratio 0.891, isi_violations 0.787). Both readings fail (cell 24). |
| qc-pass-fraction-similar | reproduced | 41.09% and 40.69% against 41.1% and 40.7%. |
| fig4e-unit-yield-stable | reproduced | Kruskal-Wallis p = 0.333, day medians 308, 302, 287.5 and 277, all within 300 ± 30. Insertions in the code's table: p = 0.477 and counts 129, 126, 121, 91 exactly. |
| fig4e-vbn-yield-drops | reproduced | VBN day-2 median 261 against 321 on day 1. p = 1.2e-24 under reading (a), 1.2e-19 under (b). |
| fig4e-firing-rate-stable | reproduced | p = 0.223 (paper text 0.21, code 0.26); sessions per day 23, 24, 22, 18 as in the paper. |
| fig4ef-rf-fraction-stable | reproduced | p = 0.671 with p values computed here, 0.864 with the code's, at 0.01; sessions per day 12, 11, 12, 11. |
| fig4f-rf-match-retinotopy | blocked (data_missing) | RF centres could be computed, but the ISI maps and insertion images are absent. |
| fig4g-visual-responses-similar | reproduced | Units 595, 482, 534, 446 (paper 595, 482, 536, 446). Kruskal-Wallis p = 0.343 under (a), 0.70 under (b). |
| behavior-stable-across-days | partially_reproduced | Kruskal-Wallis p ranges 0.73–0.82, so the absence holds. But days 1 and 4 miss the ±10% tolerance in both 87-session readings (73 and 53.5 for all rewards, 67 and 48 for earned rewards), and every reading misses at least one day. |
| figs4i-insertion-suppression | not_reproduced | tau = 36.0 and 35.4 min against the 22.5–33 min range; per-session median 34.8 min. See problem 3. |
| figs4de-retraction-reduces-drift | blocked (metadata_insufficient) | No retraction flag in the NWB, the asset metadata or the code's session table; the paper gives no date rule. |
| figs4f-retraction-yield-similar | blocked (metadata_insufficient) | Same as above. |
| figs4gh-sharpened-probes | blocked (metadata_insufficient) | No sharpening flag or failed-attempt record in the archive. |
| figs3d-duragel-yield-stable | blocked (data_missing) | The Dura-Gel mice (optotagging and dual-hemisphere) are not in the dandiset. |
| fig5-bilateral-recordings | blocked (data_missing) | All annotated units are in the left hemisphere (cell 6). |
| fig6bc-cortical-silencing | blocked (data_missing) | No VGAT-ChR2 genotype among the 27 subjects (archive and cell 76). |
| fig6ef-optotagging-mrn | blocked (data_missing) | No Vglut2-Cre genotype. Optotagging tables exist, but only for Sst and Vip;Ai32 mice. |
| fig7a-mop-higher-frequency | reproduced | Holds by the letter of "under a reading": reading (b) passes in 8 of 8 combinations (VISp 4.0 Hz, MOp 4.5 Hz, p ≤ 1.6e-3). Reading (a) fails in all 8. Fragile, see problem 4. |
| fig7b-low-arousal | partially_reproduced | Pupil is smaller and running lower for both areas in every combination (p < 1e-5). No reading gives −25 ± 2.5%: VISp area −13 to −15%, MOp area −31 to −37%, MOp diameter −17 to −22%, pooled −14 to −16%. |
| fig7b-visp-offset-locked | reproduced | VISp chi-square p ≈ 0 with the largest bin at 100–150 ms. MOp p = 0.41–0.53 (chi-square) and 0.28–0.62 (KS) in all combinations. |
| figs6-replay | not_reproduced | r = 0.21–0.63 in all 32 combinations, none within 0.77 ± 0.077. Significance depends on the event window (cell 51). |
| fig7cd-visp-coupling | blocked (methods_underspecified) | The CCG part holds everywhere. The coherence part holds in all 8 R1 combinations but fails in 6 of 8 R2 combinations, where SSp (and PO under L2 E2) become significant. |
| fig7cd-mop-coupling | blocked (methods_underspecified) | Holds in all 8 E2 combinations, coherence and CCG. Under E1, PO has fewer than 25 events and is not tested. |
| fig7e-lags-straddle-zero | not_reproduced | 94 of 102 pair tests are significant; only VISp-VISl under L1 is not. The criterion likely misreads the paper, see problem 9. |
| fig7f-visp-network | blocked (methods_underspecified) | "Any subdivision": 14 of 16 combinations hold (CP has q = 0.095 under L1 E2 R1). "All subdivisions": 8 of 16. |
| fig7f-mop-network | blocked (methods_underspecified) | Holds in 6 of 16. Under E1, PO, MRN and SCiw are untested; under L2 E2 R1, MRN has q = 0.12. MRN and SCiw each come from 1 session of 32 events. |
| fig7-hippocampus-not-engaged | not_reproduced | VISp–DG is significant and positive in all 16 combinations, as are others in many (CA1, SUB, ProS); MOp–CA1/DG under L2 E1 R2. |
| fig8bc-cp-rf-location | partially_reproduced | CP-RF units are more dorsal (p = 1.9e-58) but more lateral, not medial (z 4075 against 4350 µm, two-sided p = 1.8e-33). |
| fig8d-cp-rf-larger-response | partially_reproduced | The response test holds: 53 significant bins, all with CP-RF higher. Under the Methods QC filter the counts are 70 and 162, outside 80 ± 8 and 205 ± 20.5; only the code's presence 0.9 variant gives 76, 209 and 239. |
| fig8d-response-latencies | blocked (methods_underspecified) | Half-peak reading: lags 16 and 20 ms, within tolerance. Peak reading: 34 and 9 ms (QC) or 43 and 0 ms (variant), outside it. |
| fig8e-cp-rf-more-modulated | reproduced | Significant bins at the VISp troughs and a larger CP-RF range under both readings in all 8 combinations. L2 E2 gives 439 events, as the paper does. |
| fig8f-cp-rf-higher-coherence | blocked (methods_underspecified) | R2: p = 1.2e-14 to 6.5e-11 (L2 E2 R2 with 439 events: p = 1.9e-10). R1: p = 0.36–0.75, and CP-RF is not higher. |

## B. Problems

1. **[affects a conclusion] figs6-replay, cell 51 and `session_spike_products`.** Every qualifying event is assigned to the last presentation starting before it, including events during a stimulus (since_offset < 0) and after omitted flashes. About a third of VISp events lie outside 0–0.5 s after an offset (1034 of 1518 inside, cell 49). The S6 legend speaks of post-stimulus events. Leaving those events in may lower r.
2. **[affects a conclusion] fig7a, `session_spike_products` (`freq_auto`).** The spectrum of a 2 s autocorrelogram has 0.5 Hz resolution, so the MOp median (4.5 Hz) sits exactly on the inclusive lower bound of the widened range, and the significant MOp > VISp test is on heavily tied values.
   - The reproduced outcome rests on this quantisation.
   - Separately, my synthetic tests of `find_events` show the specified detector (width ≥ 100 ms, ≥ 4 maxima in 1.25 s) only finds sinusoidal rhythms of about 3.3–5 Hz. So a 5–7 Hz MOp band cannot come out of reading (a). This follows from the method as the claims file gives it, not from a notebook bug.
3. **[affects a conclusion] figs4i, cell 40.** The fit window is the author's own choice and is not stated as an assumption. It is the shortest session's length, 77.3 min from the first stimulus, so it runs past the ~65 min active block into the Gabor and flash epochs and spans the no-reward block. tau depends on this window.
4. **[affects a conclusion] link-code-tables, cell 12.** RF significance agreement is reported only pooled (98.8% agreement, i.e. 1.2% differing), not per session. The "≤1% per session" condition is not evaluated.
5. **[does not affect a conclusion] Alpha claims, `session_spike_products`.** The autocorrelogram threshold, CCGs and coherence use the unsmoothed 10 ms rate, while the header defines the population rate as smoothed. This is not stated. On synthetic Poisson noise the smoothed rate passes the 0.1 threshold 45% of the time against 0% unsmoothed. The notebook's qualifying counts (L2 E2: 1643–1660 VISp, 119–122 MOp) match the code's 1653 and 113, so the choice appears to match the code.
6. **[does not affect a conclusion] `pair_table`, cell 43.** The Benjamini-Hochberg family includes CP-RF, CP-noRF and non-areas ("Track not annotated", "VIS"). This shifts marginal q values (PO 0.049–0.05, SSp 0.035–0.047, MRN 0.04), but only in combinations whose claims are already split.
7. **[does not affect a conclusion] cells 54 and 56 (`area_state`).** An area that is "absent" (fewer than 25 events) counts as "not significant" in the negative parts of the coupling claims; for example MOp–VISl under L1 is never tested. VISl is also merged with the ISI label VISlm without saying so.
8. **[does not affect a conclusion] fig8d variant, cell 68.** Noise CP units have no RF p value, because `rf_pvalues` covers only good units, so they fall into CP-noRF.
9. **[does not affect a conclusion] Claims file, fig7e (reported, not corrected).** The Figure 7E legend shows a "distribution of time lags". Judging "straddled zero" with a signed-rank test of the median against zero over ~100–1100 events goes beyond what the paper claims. Under a descriptive reading the median lags are small (−23 to +14 ms), but VISp-VISal is 96% positive and MOp-PO is 12% positive.
10. **[does not affect a conclusion] behavior-stable-across-days, claims file.** The paper's medians end in .5 on days 1 and 3, which needs an even number of sessions those days. The 87-session set has 23 on day 1 and the 99-session set has 25 on day 3, so the paper used neither set.
11. **[does not affect a conclusion] shield.py docstring.** It says the analytic chi-square p value is used for RFs, but the code uses the AllenSDK-style bootstrap; the code is right. My synthetic test of `rf_pvalues` gives p = 0 for a tuned unit and 0.885 for an untuned one, with the correct peak position.

## C. What I could not check

- **Eye-tracking and running clocks (fig7b-low-arousal).** Their alignment to the spikes is not established. An event-triggered pupil and running trace against a stimulus- or lick-locked reference would show it.
- **fig7f and fig7cd area lists.** I could not see whether L1 has SSp-* or RSP subdivisions that A3 and A4 leave out. A list of the area labels and unit counts per session under L1 and L2 would show it.
- **figs4i.** A fit restricted to the active-behavior block, and the per-session fit range, would show whether tau falls in 25–30 min.
- **figs6-replay.** A run keeping only events with 0 ≤ since_offset < 0.5 s would test problem 1.
- **penetration-success and figs4gh.** The code's probes table has an `inserted` column that the notebook never prints. Its value counts for the 87 and 99 sessions would give a direct penetration count, and perhaps failed attempts per probe.
- **The 6 sessions whose metrics differ.** Whether the dandiset or the code table holds a re-sort could not be told. Spike counts per unit compared with the code's firing_rate × duration would show it.
