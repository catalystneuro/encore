**A. Outcomes** (30 claims in the claims file: 17 reproduced, 3 partially reproduced, 2 not reproduced, 8 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| dataset-sessions-mice-labs | reproduced | Cell 17: 459 sessions, 139 mice, 12 labs. |
| dataset-probes-units | reproduced | Cell 19: 699 insertions, 621,733 units, 889.5 per probe (889 ± 1). |
| well-isolated-neurons | reproduced | Cell 21: 75,708 units, 108.3 per probe. The criterion's side check fails as worded: the score equals the fraction of metrics passed only with a noise cutoff below 5. With the Methods' 20, it matches 540,399 of 621,733 units (cell 10). |
| canonical-regions | reproduced | Cell 23: every inclusion step matches `inclusion_info.csv`; ends at 201 regions and 62,857 units. |
| brain-areas-279 | reproduced | Cell 25: 279. |
| mice-sex | reproduced | Cell 27: 94 M, 45 F. |
| mice-age-weight | partially_reproduced | Cell 29: weight is within tolerance under all readings. Age is not: maximum about 63 to 66 weeks against 178, mean about 28 against 44.96. |
| probe-versions | reproduced | Cell 31: 586 / 109 / 4. |
| trials-per-session | reproduced | Cell 33: mean 645.1, median 601, range 401 to 1525. |
| rf-mapping | blocked (data_missing) | Confirmed in the archive (see B13). |
| behav-performance | reproduced | Cell 36: only reading (c), 81.58%, is in 81.4 ± 0.4. The per-mouse reading (a), whose s.e.m. of 0.43 matches the paper's ± 0.4, gives 80.76% and fails. |
| behav-zero-contrast | not_reproduced | Cell 38 (a): t = 19.68 is within tolerance, but the mean of 58.26% misses 58.7 ± 0.4 by 0.04. Reading (b) fails both. A narrow miss (see B6). |
| behav-early-movements | reproduced | Cell 40 (a): 22.75%. |
| fig1d-contrast | reproduced | Cell 42: p = 1.5e-24 and 5.9e-24; the median rises at every step. |
| fig1ef-end-of-session | reproduced | Cell 44: 80.0% vs 85.0% (p = 7.9e-13); 279 vs 165 ms (p = 2.6e-22). |
| fig1g-block-switch | reproduced | Cell 46: tau of 3.86 is outside 4.5 to 11, but reading (b), 1 + tau ln 10 = 9.9 trials, is inside. The curve is noisy and the fit has no CI (B7). |
| fig1h-block-bias | reproduced | Cell 48: 9 of 9 contrasts, all p < 1e-8. |
| dec-stim-restricted | reproduced | Cell 55: VISp significant (Fisher p = 1.3e-8); 4 regions for stimulus, 5 for choice, 7 for feedback. The margin over choice is one region. |
| dec-choice-widespread | reproduced | Cell 57: GRN p = 6e-15, effect 0.277 (paper 0.28); choice 5 > stimulus 4. |
| dec-feedback-nearly-all | partially_reproduced | Cell 59: 7 of 10 significant, IRN included; 23 of 111 region-sessions above 0.9. The paper's own `region_info.csv` marks only 8 of these 10, so this region set cannot reach the threshold of 9. |
| sc-stim-fraction | blocked (methods_underspecified) | Cell 64: the null fraction is 2.68e-3 (CI 1.46e-3 to 4.49e-3), which excludes the band 1.7e-5 to 1.5e-4 around the paper's 5e-5. The other parts would pass: max 5.9% (CL), 14 of 14 within 0.02. |
| sc-choice-fraction | blocked (methods_underspecified) | Cell 64: the null fraction is 2.49e-3, same exclusion. The other parts would pass: binomial p = 3.8e-29, Spearman 0.84 (p = 1.6e-4). |
| traj-latency-visual | not_reproduced | Cell 70: the order fails (VISam 59.2 < VISpm 61.3 ms). VISp 46.5, LP 48.6 and VISam 59.2 are out of tolerance; LGd 31.7 and VISpm 61.3 are in. The paper's own `stim.pkl` also gives VISam 66 and LP 46.8, not the text's 78 and 42. |
| traj-latency-late | reproduced | Cell 72: IRN 118.3 ms, GRN 109.9 ms, both p = 0.001. The paper's `stim.pkl` puts both at 89.4 ms, and in the 0 to 100 ms window IRN has no latency (cell 68). |
| traj-stim-regions | blocked (other) | Not attempted. The data are present, and the notebook's own cost estimate says it fit in the time limit (B11). |
| fback-oscillation-licking | partially_reproduced | Cell 74: (i) fails, median peak 7.08 Hz is outside 9 to 11. (ii) holds: 20 of 27 sessions, p = 0.0042. (iii) holds: lick peak 7.23 Hz. |
| wheel-speed-decoding | blocked (other) | Not attempted. Wheel velocity is in every file (B13). |
| encoding-feedback-largest | blocked (other) | Not attempted. The inputs are present. |
| video-correlates | blocked (other) | Not attempted. Pose, pupil and motion energy are in most sessions (B13). |
| granger-interactions | blocked (other) | Not attempted. The spikes are present. |

**B. Problems**

1. [does not affect a conclusion, as far as can be checked] `bwm._logreg`: L1 is requested only through `l1_ratio=1.0` with liblinear and no `penalty`. That gives L1 on scikit-learn 1.8 or later. On 1.7.2 the same call silently fits L2: 50 of 50 coefficients nonzero at C = 0.01, against 1 of 50 on 1.9.1 (my synthetic test). The notebook never prints its scikit-learn version. The effects agree closely with `region_info.csv` (Spearman 0.91 to 0.98), but that does not establish which penalty ran.
2. [affects a conclusion] `bwm.decode` reuses the real labels' C for every null. In cell 60 this null is narrower than the full nested null for VISp stimulus (95th percentile 0.531 against 0.575), so stimulus p-values can be anti-conservative. VISp significance (dec-stim-restricted) has not been checked under the nested null. The design is fixed in the claims file, but its effect on the key region is untested.
3. [affects a conclusion] sc-stim-fraction and sc-choice-fraction: the paper's chance level of 0.001 × 0.05 = 5e-5 (Methods) assumes the two tests are independent. On i.i.d. Poisson null data, `ccmw_p` combined with `simple_mw_p` gives a joint rate of about 1.0e-3 (3,000 units), because a unit passing p < 0.001 nearly always passes the combined test. So the block comes from the paper's stated chance level more than from the notebook. The notebook's 2.7e-3 is about 2.7 times that i.i.d. rate.
4. [does not affect a conclusion] `bwm.ccmw_p` permutes the x and y labels independently, which gives 7.2% at p < 0.05 on i.i.d. null data, against 4.8% with one shared permutation. The paper's `Time_TwoNmannWhitneyUshuf` does the same, so the helper is faithful to the code. The method is mildly anti-conservative, consistent with the 0.069 and 0.061 rates in cell 64.
5. [affects a conclusion] Cell 74, test (ii): power is raw spikes/s squared, with no normalisation for the correct trials' larger evoked response. Six of 27 sessions peak at the 4 Hz band edge, so the correct > incorrect power difference may reflect the evoked transient more than an oscillation. The partial outcome rests on (ii) and (iii), and (iii) is the stronger evidence.
6. [could affect a conclusion] Cells 36, 38 and 42 use all 459 sessions. The Fig. 1d legend says 454 sessions. behav-zero-contrast misses its tolerance by 0.04 points, and the 454-session subset was never tried.
7. [does not affect a conclusion] Cell 46: an unweighted fit to a noisy mean curve (for example 0.364 at position 26), with no CI on tau. The per-mouse tau IQR is 1.9 to 11.3, so reading (b) passes on a point estimate only.
8. [does not affect a conclusion] `bwm.trajectory`: the canonical-window variant re-subtracts the minimum over the 48 points, while the paper's code reuses the full-window baseline. Only the variant column is affected. I checked the main latency on synthetic spikes with a 40 ms onset: it returns 38 ms on the bin-start axis, as expected. The distance, 70% crossing and significance rule match `state_space_bwm.py`.
9. [does not affect a conclusion] `bwm.analysis_mask`: a session that never passes 90% on easy trials is kept at 400 trials instead of being excluded. Two sessions are truncated, and cell 8 does not say whether either reached the floor.
10. [does not affect a conclusion] Cells 62 and 68 drop the 64 sessions whose block column is invalid (set by the claims file). The paper used them, which may explain part of the VISam latency difference (one session dropped).
11. [affects a conclusion] Cell 75 marks five claims "not attempted" for lack of time. Cell 76 shows a total run of 7.2 of 30 minutes, about 3 minutes to stream all 454 sessions, and trajectories costing about 6 s for 7 regions (about 13 times that for all regions). traj-stim-regions therefore fit the budget and was left untested without cause.
12. [does not affect a conclusion] `bwm.bh` and `bwm.fisher_p` are correct: BH matches statsmodels on 200 random sets. With 100 nulls, the per-session p floor of 1/101 gives a 2-session region a Fisher floor of 0.0010. That limits CL and LDT; LDT's non-significant choice result (p = 0.0154) may be partly a resolution effect.
13. Archive check of the blocked claims. In one processed file (sub-NYU-37), `passive_intervals` lists only spontaneousActivity (3084 to 3684 s) and taskReplay (4009 to 4340 s), with `stimulus/presentation` and `stimulus/templates` empty. The roughly 5-minute gap between them is presumably the RF mapping. Spikes in that gap could be used, but the pixel sequence is in neither the processed nor the raw file; the raw file has only frame2ttl pulses. So no part of rf-mapping is testable. Wheel, lick and spike data cover the other blocked claims. Left/right camera pose (paws, nose, tongue, pupil) is present in 3 of 4 sampled files.

**C. What I could not check, and the output that would have let me**

- Which penalty the decoder actually used. A printed `sklearn.__version__` and the number of nonzero coefficients for one fit would settle it.
- Whether VISp stays significant for stimulus with the nested null. The full cell-55 table rerun on VISp sessions with the nested null, or at least the per-session p under both nulls for those sessions, would show it.
- behav-zero-contrast and behav-performance on the paper's 454 sessions: the same cells restricted to the canonical sessions.
- Whether the IRN 7 Hz peak and the correct > incorrect power difference survive normalisation: the same table with PSTHs z-scored per unit, or with the mean evoked response subtracted.
- Whether the IRN and GRN latencies depend on where the window ends: the distance curves of cell 68 as numbers, or the latency for a 0 to 200 ms window.
- The single-cell null rate on i.i.d. shuffled labels (one permutation per region-session). It would separate the test's built-in joint rate from drift effects.
- The two truncated sessions in `analysis_mask`: whether either reached the 400-trial floor.
