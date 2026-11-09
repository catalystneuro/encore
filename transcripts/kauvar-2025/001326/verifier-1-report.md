**A. Outcomes** (54 claims in the claims file: 40 tested across the two notebooks, 14 not tested)

| Claim | My outcome | Reason |
|---|---|---|
| fig1e-human-ketamine-late-closure | reproduced | Saline 0.706, ketamine 0.426, both within tolerance; t = 3.703, p = 0.0342, the same as table S3 (behavior cell 35). |
| figs1b-human-early-closure-unchanged | reproduced | 0.839 against 0.777, p = 0.2032 ≥ 0.05 (behavior cell 37). |
| fig1k-mouse-ketamine-late-closure | reproduced | 0.262 against −0.068, t = 4.737, p = 0.009 (cell 14). |
| fig1l-dissociatives-preinfusion | reproduced | All six means within tolerance; corrected p 0.504, 0.002, 0.041, the same as the paper (cell 16). |
| figs2bc-mouse-early-late | reproduced | t = 6.854 and 4.951, the same as the paper. All values within tolerance, though late saline is 0.203 against 0.34 ± 0.14, just inside (cell 18). |
| fig1m-accumulation-persistence | partially_reproduced | Accumulation holds (puff 8: 0.517 against puff 1: 0.244, intervals do not overlap). Kaplan-Meier median is 13.05 s on the criterion's 100 preinfusion trials, outside 15.16 ± 1.5. It is within only on the code's 200 trials, which include infusion trials (cell 20). |
| figs2g-scaling-puff-number | reproduced | Puff 1 vs 8 corrected p 0.0038, 0.0001, 0.0000; pressure comparisons p ≥ 0.46; all six means within tolerance (cell 22). |
| figs2h-dose-response | reproduced | Under both FDR families, ketamine 35/50 and PCP 10/20 have q < 0.05 and every lower dose q ≥ 0.05 (PCP 5: 0.110 / 0.0735). Expected values within (cell 24). |
| fig1p-anesthesia-abolishes-both | reproduced | K/X q = 0.006 and 0.0016. All six values within tolerance, including ketamine reflexive 0.436 and PCP 0.428 (cell 26). |
| figs5-other-drugs | reproduced | q: ketamine 0.0053, PCP 0.0092, buprenorphine 0.934, diazepam 0.304, the same as table S3 (cell 28). |
| figs6-vpm-muscimol | reproduced | 0.602 against 0.105, both corrected p = 0.0289, the same as the paper; 0–40 ms closure unchanged (cell 30). |
| fig5hi-behavior-model-doses | reproduced | Variance explained 0.917 (ketamine) and 0.886 (PCP); τP falls at every dose step. The data assembly is an assumption the notebook states, and the ketamine τB sits at its 100 s bound (cell 32). |
| fig4b-recorded-eye-closure-ketamine | partially_reproduced | Without normalization, Pre − Ket = 0.026 [−0.030, 0.082]. With each condition divided by its own maximum it is 0.308 [0.243, 0.373]; divided by the Pre maximum it is −0.033. Only 10 of the 13 sessions are in 001347 (behavior cell 6). |
| fig5b-recorded-accumulation | partially_reproduced | Pre accumulation is above 0 in every reading. Without normalization, Ketamine accumulation (0.040 [0.012, 0.067]) neither includes 0 nor lies below the Pre mean. It meets the criterion only under per-condition max normalization (cell 8). |
| figs34c-tone-no-eye-closure | reproduced | Upper bound of tone closure ≤ 0.006 in every split, below the puff value and below 0.1. Only 6 of the 7 sessions are available (cell 10). |
| fig4-recordings-scale | reproduced | 13 sessions, 10 mice; 6698 puff-modulated units (6491 with the spike-count reading), both within 6969 ± 697; median 32 regions per session (cell 6). |
| fig4de-response-clusters | not_reproduced | 11 clusters, which is within ±1, but 7 of the 12 sizes are outside tolerance and the 12th is missing. Only 1 cluster is persistent where the criterion needs 3 (cell 8). |
| figs31b-cluster-overrepresentation | partially_reproduced | At FDR 0.05: PAG in cluster 5 (fast), VPM in cluster 2 (5th fastest of 11), frontal regions in slow clusters. At 0.01, VPM is only in cluster 8 (slow half). Problem 6 makes even the 0.05 result fragile (cell 10). |
| fig4g-ketamine-alters-slow-clusters | not_reproduced | Spearman ρ = −0.023 (p = 0.95) for cosine distance and −0.018 (p = 0.96) for the 1–2 s difference (cell 12). |
| fig4i-rise-times-unchanged | reproduced | Median change in rise time is −0.005 or −0.007 s under all 8 readings, within one bin; Pre rise < 0.1 s in 30/35 and 28/31 regions (cell 14). |
| fig4h-decay-shortened | reproduced | Median bootstrap change −0.18 to −0.19 s; 33/35 and 31/31 regions shorter (cell 16). Problem 5 is an unchecked risk to this result. |
| fig4h-decay-anatomical-progression | reproduced | Frontal/limbic 0.488 / 0.532 against midbrain 0.311; VPM 0.541 and MD 0.590, both above the overall median 0.445 (cell 18). |
| fig5d-emotion-dimension-accumulates | partially_reproduced | Before puff 8 > 0 and > puff 2, 10–11 s after > 0, and Ketamine includes 0, in all 24 readings. But "last 5 s includes 0" fails in all 24 (e.g., 0.303 [0.203, 0.403]) (cell 32). |
| fig5e-late-reduced | partially_reproduced | Holds with the code's 3–4 s target window: q = 0.0056–0.040 under pooled variance and unit-vector scaling. Fails in every session reading with the Methods 5–6 s window and per-unit variance (q = 0.105–0.113) (cell 34). |
| fig5e-rapid-unchanged | partially_reproduced | q ≥ 0.05 with the Methods window. With the code window and per-unit variance, q = 0.023, 0.031, 0.048, so the absence fails (cell 36). |
| fig5g-tau-persist-model | reproduced | Variance explained 0.81–0.95 and Ketamine τP (0.12–0.38 s) far below Pre (20–34 s) in all 24 readings (cell 40). |
| figs33-alternative-models | partially_reproduced | τP model best in 22 of 24 readings; saturation is best for sub-3 with the code window and pooled variance, by 0.001–0.006. The variance explained is also computed on the wrong segment (problem 1) (cell 42). |
| figs32c-regional-emotion-dimension | partially_reproduced | 7/7 areas pass with the notebook's mean-to-mean comparison with puff 2. Under the criterion's wording (the interval above the puff-2 value), some areas fail, e.g., OLF with the code window (lower bound 0.048 against 0.164), HPF and MB. Most still pass (cell 38). |
| fig6b-persistent-dimension-distributed | reproduced | Every division with ≥ 30 units holds top-10% units; the largest share is 0.21–0.32 (cell 26). |
| fig6d-mouse-persistent | partially_reproduced | Pre vs Ket q ≤ 0.002 everywhere, and means within tolerance with first-puff projections. Post vs Ket fails without sub-1 (q = 0.051), and under the Methods-literal epochs (cell 22). |
| fig6f-mouse-fast-unchanged | reproduced | Pre vs Ket q ≥ 0.27 in all 12 readings. Pre values (4.01–4.47) are partly outside 4.48 ± 0.25, which the criterion does not require (cell 24). |
| fig6h-mouse-timescale | partially_reproduced | Without sub-5, both ways of combining series pass (p ≤ 0.016) with means within tolerance. Without sub-1 or sub-3, per-series fits fail (p 0.34–0.56), driven by degenerate fits (problem 2) (cell 28). |
| fig6j-mouse-coupling | partially_reproduced | With pooled variance, both readings pass (p ≤ 0.013; ratio 0.51–0.59, within). With the Methods per-unit variance, reading (a) gives p = 0.086 and 0.058 in two session readings, ratio 0.75–0.82 (cell 30). |
| figs34d-tone-fast-unchanged | reproduced | Judged without sub-5, the only exclusion that leaves table S3's 7 tone sessions from 7 mice: q ≥ 0.14 everywhere. Without sub-1 the absence fails (q = 0.0275) (cell 44). |
| figs34e-tone-persistent | reproduced | Both q < 0.05 with Ketamine lowest under every reading except the code split with pooled variance without sub-1 or sub-3 (q = 0.054). Means within tolerance (cell 46). |
| figs34f-tone-shorter-than-puff | reproduced | Puff half-peak fall 0.90–0.99 s against tone 0.16–0.17 s; 1–2 s intervals do not overlap (cell 48). |
| figs34g-tone-timescale | partially_reproduced | Without sub-5, every test passes (p ≤ 0.037). Ketamine means are within tolerance only for concatenated fits; per-series Ketamine is 0.140–0.161 against 0.089 ± 0.024. Without sub-1 or sub-3, per-series fails (cell 50). |
| figs34h-tone-coupling | not_reproduced | Reading (a) p ≥ 0.28 in every case; reading (b) passes once. Only the notebook's extra (b′, puff windows) passes (cell 52). |
| figs30-correlation-structure | not_reproduced | Within-region change 0.0063, p = 0.052; between-region change −0.0001, p = 0.89. The RSP (9/10) and ORB (5/7) increases hold, but the Ketamine window may be wrong (problem 3) (cell 54). |
| figs29-rsp-oscillations | reproduced (marginal) | RSP has the largest pooled rise at 5 and 10 min. Per-session rises: 7/9 at 5 min, but only 5/9 at 10 min (the notebook prints 5 of 10) (cell 56). |
| link-001347-condition-labels | reproduced (notebook says not tested) | All 99 ids are present with the trial counts the code reads. fig. 1K t = 4.737 and fig. S5 C–E t values (8.4882, 6.0804, 0.0878, 1.6120, 8.6017, 12.0602) are the same as the paper (behavior cells 3, 14, 26, 28). |
| link-001347-recorded-sessions | partially_reproduced (notebook says not tested) | 10 of 13 sessions have a file, and every matched series is within 14 ms of the clock fit. sub-3_ses-20230225 and both sub-5 sessions have no file (behavior cell 3). |
| fig1f, fig2d, figs14g | blocked, data_missing (agree, with limits) | No CADSS or report data were found, but the notebook searched only the `sub-SD*_puff_behavior` files, not `sub-H` or the ecephys files. The API metadata lists no measured variables. |
| figs4-reward-licking | blocked, data_missing (unverified) | The statement "only eye_closure" in behavior cell 3 is a hard-coded print, not a computed check. |
| fig2g, fig2i | not blocked | 001347 holds `sub-H_ses-sgramNMFLoadings.nwb` and `sgramNMFFactors.nwb` (0.3 MB each) and `sgramPerChannelPerTrial` (5.2 GB). fig2i, and fig2g at least from the deposited factors, look testable. The notebook gives no reason. |
| fig3b | not blocked | `sub-H_ses-ketChangePermutationClusterTest.nwb` (1.9 MB), `sgramPerYeoPerTrial` (107 MB) and `sgramPerRegionPerTrial` (624 MB) are on the archive. |
| fig6c, fig6e, fig6g, fig6i, figs12 | not blocked by absence | iEEG ecephys per participant and session (Baseline, Pre-, Infusion, Postinfusion; 207–434 MB each; 16 GB for the whole dandiset) are deposited. Whether figs12's spontaneous-blink events are there is unknown. |

**B. Problems**

1. **[affects a conclusion]** figs33, cell 42: variance explained is computed on the whole Ketamine half, series plus 25–70 s afterwards. The criterion asks for the Ketamine puff-series segment only. The margins between models are 0.001–0.006, so this choice can change which model is best.
2. **[affects a conclusion]** fig6h and figs34g, cells 28 and 50, and `K.extract_timescale`:
   - The exponential fit is unbounded, so degenerate per-series fits (Ketamine b = 833 s and 1.71 s) enter the session means while the notebook reports "failed fits 0". These single fits decide reading (a) without sub-1 or sub-3.
   - The autocorrelation is taken without subtracting the mean. On synthetic AR(1) data with τ = 0.1 s, the zero-mean estimate is 0.114 s; with a 2 s.d. offset it is 0.278 s. A mean level that differs between conditions can therefore bias the timescale comparison.
3. **[affects a conclusion]** figs30, `process_session` and cell 54: the Ketamine window starts at the code's onset (30 s after the last puff of series 20). In every session that is 94–420 s before the file's "Ketamine infusion start" (cell 4), and the Methods say "10-minute period following the onset of ketamine infusion". The window therefore includes up to 7 min before infusion, and no variant using the file's infusion time was run. The claims file's choice of onset is itself a questionable reading of the paper.
4. **[affects a conclusion, unchecked]** Epochs in all Ketamine comparisons: the notebook never shows that series 23 starts after the file's infusion time. With infusion up to 420 s after the code's onset (sub-7, sub-1_ses-20230226), early Ketamine series could be pre-drug.
5. **[affects a conclusion]** fig4i and fig4h, `region_times` and `rise_decay` (cell 14):
   - A cluster whose rise or decay is NaN (peak after 750 ms, or no fall below 25%) adds 0 to the weighted sum through `nansum`, with no renormalization of weights. The criterion instead drops such regions.
   - NaN rates may differ between Pre (40 replicates) and Ketamine (20 replicates), so the −0.185 s decay change may be partly an artifact. NaN fractions are not printed.
6. **[affects a conclusion]** figs31b, cell 10: the fast/slow split ranks clusters by decay of `cluster_means`, while cell 12 uses `cluster_trace`. Under the latter, VPM's cluster 2 (0.40 s) ranks 6th and leaves the faster half, and figs31b would fail at both thresholds.
7. **[affects a conclusion]** `emo_checks` (cell 32), used by figs32c: "puff 8 above puff 2" compares means only. The criterion's interval wording drops OLF, HPF, MB or STR in some readings.
8. **[affects a conclusion]** fig4b and fig5b: the outcome depends entirely on dividing each condition's trace by its own maximum. Without normalization, or with both divided by the Pre maximum, the ketamine effect disappears. Also, 3 of the 13 sessions are absent from 001347.
9. **[does not affect a conclusion]** fig1m: the event that ends survival is taken from the code only. The paper leaves it open, and the result is sensitive to the trial set.
10. **[does not affect a conclusion]** Leakage: the persistent, fast and emotion-like dimensions are trained on the same Pre series they are scored on, while Ketamine is out of sample. This follows the paper but inflates Pre-vs-Ketamine contrasts (fig6d, figs34e). No held-out check was run.
11. **[does not affect a conclusion]** Cell 56 counts sub-7 (no value) in the denominator ("5 of 10"). Cell 4 shows every unit's spike times stored out of order in the files; they are sorted on load and the clock check passes. Behavior cell 3's "only eye_closure" is a hard-coded print.
12. **[does not affect a conclusion]** The chance level for figs31b is 1/11 here against the paper's 1/12, because 11 clusters were found. fig6f Pre values are outside the expected tolerance under the Methods weights.

**C. Not checked**

- That `extract_timescale`, the `nansum` weighting and the max normalization match analysis.py. The code was not available to me.
- Whether series 23 starts after the file's infusion time. Needed: a per-session table of each series onset minus the infusion time.
- Whether tone or light stimuli fall inside the 50 s post-series windows or the 30 s pre-series baselines. A table of onsets relative to the puff series would settle whether the fig5d "last 5 s includes 0" failure, fig6h and fig6j are contaminated.
- The bias from unequal replicate counts in fig4h and fig4i. Needed: NaN fractions per condition, and a control with Pre subsampled to 20 replicates.
- fig6h and figs34g with median or bounded fits, and with the mean subtracted before autocorrelation.
- figs33 variance explained on the Ketamine series segment only, and figs30 with the file's infusion time.
- The contents of the `sub-H` files, the `sub-SD` ecephys and behavior files, and one `sub-mouse` file. Their HDF5 key listings would settle the blocked human and lick claims; the API metadata lists no measured variables.
