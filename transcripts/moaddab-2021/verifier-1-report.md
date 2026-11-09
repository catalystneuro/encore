**A. Outcomes** (all 30 claims in the claims file were tested; none were blocked)

| Claim | Outcome | Reason |
|---|---|---|
| units-and-sessions | reproduced | Cell 7: 743 units, 228 sessions, 11 rats. All match exactly. |
| behavior-discrimination | reproduced | Cell 11: F(2,20) = 103.57, p = 2.8e-11, as printed. All three CIs exclude zero. Means 0.422, 0.398 and 0.821 are within tolerance. |
| cue-responsive-units | reproduced | Cell 9: 423 units, 190 sessions, fewest per rat 11. The per-rat counts equal Figure S1. The unfloored-rate variant gives 461, still within 423 ± 42. |
| kmeans-elbow | reproduced | Cell 15: under z-b, all four of the claims file's combinations (start 12 or 12.5 s, best of 10 or mean of 10) meet the criterion. Under z-a, 3 of 4 do. The code's single run on the code normalization fails "decreasing" (mean squared distance rises from 11.829 at k = 12 to 11.981 at k = 13). |
| kmeans-clusters | reproduced | Cell 17: sizes 33/59/18/63/58/61/64/67 equal the paper's, and all 8 patterns are found. This needs the emulated MATLAB `rng(1)` run on the code normalization. Under z-a or z-b, sizes are within 10% for only 2 and 1 of 8, and scikit-learn runs reproduce 0 of 100. |
| cluster-firing-characteristics | reproduced | Cell 19, main reading: baseline F = 2.48 (p 0.017), CV 2.28 (p 0.027), skewness 2.65 (p 0.011). Location, half duration and amplitude ratio are not significant. Under the variant reading, skewness p = 0.051 would make this partial. |
| k1-k3-low-baseline | reproduced | Cell 21: t(421) = −3.28, p = 0.0011, with k1 and k3 lower. |
| table1-cue-interaction | reproduced | Cell 23: the interaction has p < 1e-30 in all 8 clusters. F values equal Table 1 except k4 (8.09 against 7.93). |
| fig3b-excitatory-clusters | reproduced | Cell 26: 8/8 CIs agree and 8/8 means are within tolerance (e.g. k1 D−U 0.514 against 0.51). |
| fig3d-inhibitory-clusters | reproduced | Cell 27: 8/8 CIs and 8/8 means. k8 U−S is borderline at [−0.002, 0.131]. |
| figs4-onset-and-ramp | reproduced | Cell 29: 6/6 CIs have the paper's sign and 6/6 means are within tolerance. |
| fig4abc-threat-bias | partially_reproduced | Cell 31: part (1) holds. Part (2) holds in 5 of 7 clusters: k4 has \|U\| ≥ \|D\| (−0.324 against −0.319), and k7's uncertainty mean has the wrong sign (−0.002). |
| fig4def-danger-uncertainty-correlation | reproduced | Cells 33–34, code normalization: R² 0.483, 0.214 and 0.210, with p equal to the paper's (3.25e-62 and so on). Under z-a and z-b, which the criterion names, one or two R² values fall outside tolerance, so it would be partial there. |
| fig4ghi-danger-safety-correlation | reproduced | Cell 35, code normalization: r = 0.378, −0.183, −0.129; R² 0.143, 0.0337, 0.0167, all within tolerance; p values match the paper. Under z-a or z-b it would be partial. |
| fig4-correlations-differ | reproduced | Cell 36: Z = 7.69, 8.95, 8.20. Also within tolerance under z-b. |
| fig5a-tuning-peaks-exaggerated | reproduced | Cell 40: under the code's periods and z-scores, the peaks are 0.375/0.375/0.375/0.500. The other three readings fail. |
| fig5a-tuning-peaks-inhibited | reproduced | Cell 42: 0.875, 0.625 and 0.25 under all four readings. |
| fig5a-tuning-anova | reproduced | Cell 44: F(6,357) = 4.14, F(8,2856) = 24.84, F(48,2856) = 7.22. All three equal the paper. |
| fig5e-peak-probability-over-fear-output | reproduced | Cell 47: the full CI pattern matches and 28/28 means are within tolerance. Regressor F(1,357) = 31.40 (paper 28.57 on 355 df); regressor × bin p = 5.6e-8. |
| fig5-regressor-cluster | reproduced | Cell 49: regressor × cluster p = 0.027; three-way p = 0.25. |
| table-s3-cluster-regression | partially_reproduced | Cell 51: with all 364 units, k3 shows a regressor × bin interaction (p = 0.047; Table S3 gives 0.09). So 6 of 7 clusters agree on both terms. |
| fig5f-fear-output-vs-peak-probability | reproduced | Cell 53: r = −0.656, R² = 0.430, p = 4.18e-46, and the per-cluster R² equal Figure S6. Readings f-a (0.419) and f-b (0.430) also pass. |
| table1-outcome-anova | reproduced | Cell 55: every cluster has an effect, and 16/16 significance tests match Table 1. |
| fig6a-k1-shock | not_reproduced | Cell 60, 0–8 s window from the claims file: the danger and uncertainty-shock CIs include zero (5/7 CIs agree), so even the partial condition fails. With 0–4 s, it would be 7/7 and 4/4 (see problem 1). |
| fig6b-k2-anti-ppe | partially_reproduced | Cell 62: the omission CI [−0.093, −0.005] excludes zero, where the paper's includes it (6/7). The partial conditions hold. |
| fig6c-k3-continued-threat | reproduced | Cell 64: 7/7 CIs and 4/4 means. |
| fig6de-k4-k5-persistent-threat | partially_reproduced | Cell 66: k4 gives 7/7 and 4/4. For k5 all 7 CIs agree, but the omission mean is 0.156 against 0.25 ± 0.08. The omission signs hold in both clusters. |
| fig6f-k6-ppe-then-valence | reproduced | Cell 68: 7/7 CIs and 4/4 means. |
| fig6g-k7-valence-then-ppe | reproduced | Cell 70: 7/7 CIs and 4/4 means. |
| fig6h-k8-ppe-then-unsigned | reproduced | Cell 72: 7/7 CIs and 4/4 means. |

Totals: 25 reproduced, 4 partially reproduced, 1 not reproduced, 0 blocked.

**B. Problems**

1. [affects a conclusion] Cells 56–58, `rrf.FIG6_WINDOW`, and possibly a misreading in the claims file. The claims file reads the Figure 6 gray boxes for k1, k3, k5 and k6 as 0–8 s after shock offset. But Table S4's means are matched to within 0.008 by a 0–4 s window in all four clusters; at 0–8 s the gap is 0.04–0.15. The text never states the window, and I could not render the figure to check it. This decides fig6a: not reproduced at 0–8 s, reproduced at 0–4 s. For fig6de, k5 stays partial either way (6/7 CIs at 0–4 s). The notebook applied the claims-file window and reported 0–4 s as a variant, which is correct handling.
2. [affects a conclusion] Normalization, cells 12–13. The main reading is the code's trial z-score over all trials and bins, which is neither z-a nor z-b. The claims file's last check allows following the code, and the exact agreement with printed statistics supports it (Table 1 F values, correlation p values, tuning-ANOVA F values, Figure S6 R²). I find the assumption reasonable. Still, kmeans-clusters, fig4def, fig4ghi, fig5a-tuning-peaks-exaggerated and every Table S1/S4 mean test rest on it. Under z-a or z-b, the k-means sizes and most means fail.
3. [affects a conclusion] table-s3, cells 47 and 51. The search for which units to drop (to explain 355 error df) is fitted to the target F values. It points to one k3 unit and one k5 unit, which give F = 9.35 and 2.02 exactly. Without that k3 unit the k3 interaction p becomes 0.092, which would make the claim reproduced. But the notebook gives no independent reason for dropping those units. It also never re-runs the 362-unit pooled ANOVA, so there is no check that F(1,355) = 28.57 and F(13,4615) = 4.13 come out. I kept partial.
4. [affects a conclusion] `rrf.boot_ci`. The SE is s/√n. The docstring says MATLAB's bootci uses a jackknife here; I believe bootci's studentized default is a nested bootstrap (Nbootstd = 100), but I could not check. All CIs also come from a single seed. Several CIs sit at the zero boundary: k2 omission upper bound −0.005 (this decides fig6b), k8 U−S lower −0.002, k3 D−S lower −0.003, k6 omission lower −0.000.
5. [does not affect a conclusion] Cell 15. The main single-run elbow curve is non-monotone. The "code mean(sumd)" measure (a sum at k = 2 and a mean otherwise) is an odd quantity I cannot verify. The scikit-learn "best of 10" uses greedy k-means++, which is not MATLAB's seeding. The verdict holds under z-b anyway.
6. [does not affect a conclusion] Cell 17. The claims file's kmeans-clusters readings were run only with a 13 s outcome start and the code's single run. The 12 s and 12.5 s starts and both e-b readings were never run with z-a or z-b.
7. [does not affect a conclusion] `rrf.TUNE_COLS`. k5 uses regression bins 8–12, which leave out the delay. That differs from the claims file's t-a reading and from k5's Figure 3 interval used elsewhere (bins 101–128). It is attributed to the code, and the exact match to the tuning ANOVA supports that.
8. [does not affect a conclusion] Claims file, fig4abc. Part (2) requires k4's uncertainty firing to be smaller than its danger firing, but the paper itself describes k4 as inhibited equally to danger and uncertainty. One of the two failures (k4) is therefore expected from the paper; k7 still fails.
9. Checked and found fine:
   - `mixed_anova` equals statsmodels AnovaRM and pingouin for balanced designs. With unequal groups it deliberately uses the Type III weighting SPSS uses, and it reproduces the paper's F values.
   - `boot_ci` has 0.95 coverage on synthetic data.
   - `regress_betas` equals lstsq.
   - `meng_z` gives Z = 0 when the two correlations are equal.
   - The behavior variant equals the main reading by construction, since every session has the same 16 trials.
   - There is no training/test split, so leakage does not apply.

**C. What I could not check**

- The MATLAB code (`rrfAnalysis.m`, `cubeScriptPR25.m`) that the helper cites line by line, because I did not download the dataset. A cell printing the cited excerpts would settle: the normalization, the k5 tuning bins, the label map `CODE_IDX`, the 13 s outcome start, the elbow measure, and whether the code computes a Table S4 window.
- The Figure 6 gray boxes. No PDF renderer was available here.
- Whether the borderline CIs are stable across seeds. A cell repeating the boundary CIs over about 20 seeds, and with a nested-bootstrap SE, would settle fig6b.
- The 362-unit pooled ANOVA with the two candidate units removed (problem 3).
- The k-means variants for kmeans-clusters under all the claims file's readings (problem 6).
