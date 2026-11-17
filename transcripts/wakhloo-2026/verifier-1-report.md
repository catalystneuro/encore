## A. Outcomes

The claims file lists 27 claims. The notebook tests 15 of them on DANDI:000978 and treats 12 as blocked.

| Claim | My outcome | Reason |
|---|---|---|
| eq1-generalization-error-formula | blocked (other) | A theoretical result with no data to test. Its fit to the rat data is tested under fig7f. On synthetic data, Eq. 5 (`theory_error`) equals Eq. 1 built from `geometry` to machine precision (0.19289 vs 0.19289). |
| eq1-sample-dependence | blocked (other) | A property of the form of Eq. 1, per the claims file. |
| fig3bc-mlp-theory-tracks-error | blocked (other) | A simulation, not in the archive. |
| fig3dg-mlp-geometry-tradeoff | blocked (other) | A simulation, not in the archive. |
| fig4bf-pose-network-geometry | blocked (data_missing) | The DeepLabCut data are not in the archive (checked, see section C). |
| fig4g-pose-theory-r2 | blocked (data_missing) | Same as fig4bf. |
| fig5d-macaque-theory-and-ventral-stream | blocked (data_missing) | The Majaj/Brain-Score data are not in the archive. |
| fig5e-macaque-dimension-correlation | blocked (data_missing) | Same as fig5d. |
| fig5h-macaque-snf-it | blocked (data_missing) | Same as fig5d. |
| optimal-code-disentangled | blocked (other) | Theory. |
| eq2-optimal-spectrum-flattens | blocked (other) | Theory, checked in the paper by numerical optimisation. |
| fig6ce-optimal-early-low-dim-high-corr | blocked (other) | A theoretical prediction. Its rat counterpart is late-trends-match-optimal. |
| svc-hebbian-correlation (PFC and CA1 part) | reproduced | Cell 44: theory against SVC gives r² = 0.926 (PFC) and 0.832 (CA1), P < 1e-24. Both readings (a) and (b) hold in both areas. The SVC was run on only 4 of the 500 subsets per session (see B1). |
| fig7d-behavioral-error-learning | reproduced | Cell 15: mean error 0.668 at session 1, 0.157 at session 4, 0.180 at session 8. The 1→4 drop (0.511) is much larger than the 4→8 change (0.023). All 8 rats are lower at session 4. Mixed-model slope over sessions 1–4 is −0.166, P = 5.8e-18. |
| fig7e-readout-error-learning | reproduced | Cell 17: the criterion holds in all six combinations of area, unit count and reading. Example, PFC theory: 0.363 → 0.317 → 0.332. |
| figs12c-behavior-readout-r2 | reproduced | Cell 19, theory reading: r² = 0.508 in PFC (expected 0.51 ± 0.051) and 0.493 in CA1 with 24 units (expected 0.48 ± 0.048). With the code's 19 CA1 units it is 0.475, against the code's 0.477. The Hebbian reading misses for CA1 (0.579). |
| fig7f-theory-vs-empirical | reproduced | Cell 21: r = 0.983 (PFC) and 0.948 (CA1, 24 units), both ≥ 0.9 with p < 1e-30. Theory sits above the empirical error by 0.034 and 0.031, more so in the lowest-error quarter (0.048 and 0.044), which is the small bias the legend describes. |
| fig7g-total-dimension-drops-early | reproduced | Cell 23: dimension falls from session 1 to 4 (PFC 15.83 → 14.52, CA1 19.54 → 18.13), in 8 of 8 rats. Mixed-model slopes are negative, P ≤ 3.5e-8. |
| fig7h-task-dimension-increases | reproduced | Cell 25: under reading (a), PFC goes 7.13 → 9.04 → 9.54 and CA1 6.89 → 9.13 → 9.01 (sessions 1, 4, 8). Reading (b), strict monotonicity, fails in both areas. The claim is judged on (a), as the claims file says. |
| fig7hk-measures-increase-early | reproduced | Cell 27: PFC 4 of 4 measures rise; CA1 3 of 4 (SSF falls slightly, 0.6905 → 0.6787). Both meet the "at least 3" bound. |
| fig7-late-reversal | reproduced | Cell 29: both readings hold in both areas. Dimension rises after session 4 (+0.94 PFC, +0.78 CA1) and correlation falls. Mixed-model slopes have the right signs, P ≤ 0.0022. |
| mixed-quadratic-dim-corr-snf | reproduced | Cell 32: all 12 P values are below 1e-5, raw and BH-adjusted, in every variant (largest 1.5e-6). The signs are opposite in all six models. |
| mixed-quadratic-ssf-not-nonmonotonic | reproduced | Cell 34: η P = 0.366 (PFC) and 0.313 (CA1), above 0.05 in every variant. |
| mixed-quadratic-task-dim | reproduced | Cell 36: every term has P < 0.01 in both areas, raw and adjusted. The largest is PFC η, P = 0.0025. |
| mixed-linear-ssf-task-dim | partially_reproduced | Cell 38, main reading (24 CA1 units): CA1 SSF γ has P = 1.06e-3 raw (1.34e-3 adjusted), just missing the 10^-3 bound. All signs are positive with P < 0.05. With the code's 19 CA1 units the full criterion holds (P = 6.5e-4), matching the paper's results/rat_stats.csv (5.5e-4). |
| late-trends-match-optimal | partially_reproduced | Cell 40: holds in PFC under both readings. Fails in CA1 under both, because task-relevant dimension falls from session 4 to 8 (−0.126; slope −0.015, P = 0.82). With 24 CA1 units it also falls (10.286 → 10.260, cell 25). |
| glm-cross-validated-d2 | partially_reproduced | Cell 42: PFC mean 0.279, CA1 mean 0.245 and CA1 s.d. 0.1005 are within tolerance. PFC s.d. across rats is 0.057–0.066 under every reading, against 0.022 ± 0.0022; rat KL8 is at 0.161. The criterion requires all four, so this is not a full reproduction. |

No chance level is stated by the paper for any selection, so there is nothing to compare there.

## B. Problems

1. **[does not affect a conclusion]** Cells 7–8, SVC subsampling. The SVC was fitted on 4 of the 500 subsets per session, whereas the code fits it on every subset; this is recorded as a deviation. It makes the session means noisier, which can only lower r². The r² values are 0.83–0.98, far above both readings' bounds.
2. **[affects a conclusion: mixed-linear-ssf-task-dim]** Cell 30/38, unit count. The outcome turns on the 24 vs 19 CA1 unit count:
   - 24 units, which the Methods give and the claims file makes the main reading, gives P = 1.06e-3 and a partial outcome.
   - 19 units, which the code used to produce the paper's numbers, gives P = 6.5e-4 and a full reproduction.

   The notebook ran both readings, which is correct. The miss is marginal and comes from the paper's own Methods/code inconsistency, not from an analysis error.
3. **[affects a conclusion: glm-cross-validated-d2]** Cell 42, PFC s.d. The PFC s.d. is about three times the paper's value under every reading run (unit's own D2, nan-mean, null units counted as 0; ddof 0 and 1).
   - The cause is not diagnosed: nothing compares the per-rat GLM D2 with the paper's, and rat KL8 at 0.161 drives most of the spread.
   - I checked the s.e.m. as an extra reading. It would match PFC (0.021–0.023) but not CA1 (0.036–0.038), so no single reading gives all four values.
   - The paper's figure notebook does not compute this s.d., so the paper's definition cannot be checked against code.
4. **[does not affect a conclusion]** `wtrack.glm_summary`, best-score selection. It picks the best alpha with a nan-safe argmax, while the code's `format_glm_results` uses `np.argmax`, which selects a nan entry if one is present. The docstring calls the two the same; they differ only for units with a nan alpha, and only 1 nan best score occurred (PFC).
5. **[does not affect a conclusion]** Cells 27 and 40, CA1 task-dimension unit count. For the "CA1" (24-unit) row, the task dimension uses 19-unit subsets (`TD[("CA1", 19)]`), not 24. The 24-unit values in cell 25 lead to the same conclusions: a rise from session 1 to 4, and a fall from session 4 to 8.
6. **[does not affect a conclusion]** Cells 30–38, missing comparison table. The claims file says the code's results/rat_stats.csv "is shown for comparison"; the notebook never loads it. I fetched it myself, and the notebook's 19-unit variant matches it closely (for example CA1 quadratic dim γ −0.414 vs −0.409, PFC linear SSF P 3.0e-6 vs 1.4e-6).
7. **[does not affect a conclusion]** Cell 20, criterion change. The fig7f criterion was changed after this attempt queried it: a bound of mean |difference| < 10% of the mean empirical error was dropped. The old bound would have failed here (11.6% PFC, 10.7% CA1). It also fails on the paper's own file (11.55% PFC), so dropping it is defensible. Still, it is a criterion changed after outcomes were visible, and the next round should know.
8. **[does not affect a conclusion]** `readout_subsets` / `process_session`, train/test split. Train and test bins are drawn at random from temporally autocorrelated 500 ms bins, and unit normalisation uses all bins. This is exactly the paper's method (utils.emp_error), so it reproduces the paper faithfully. It does mean the empirical errors are optimistic, which the paper shares.

What I checked and found faithful:
- **Against the paper's code (commit 9674a6c):** session selection (behavioural error matches the paper's file to 1e-14), unit areas, binning, smoothing (`nadaraya` matches the code's to 4e-16), speed threshold, normalisation, task filter, and the Hebbian readout.
- **Formulas:** Eqs. 5–9 are identical to the code, participation ratio identical to `get_pr`, the GLM basis and grid as in the code, and mixed models as in `fit_quad_mixed`, with BH over 24 P values.
- **Against the paper's own results files:** per-session means agree with r ≥ 0.995 (cell 10).
- **On synthetic Gaussian data:** theory tracks the Hebbian error and sits above it at low error (0.135 vs 0.112 at low noise; 0.263 vs 0.262 at high noise), the same direction of bias as Fig. 7f.
- **Archive:** the 9 assets and 8 subjects match the notebook, and the clock checks pass (cell 6).

## C. What I could not check

- **Blocked claims:** I queried the archive for version 0.240511.0307. It holds 9 NWB files (8 rats, about 323 GB) with only spikes, LFP, position and trials. There are no macaque, DeepLabCut, MLP or simulation data, so none of the 12 blocked claims can be tested on it, in whole or in part.
- **The GLM fits themselves:** I could not check them against the paper. An output comparing per-rat, per-session D2 and task dimension with the paper's GLM results would show whether the PFC s.d. gap (B3) is a fitting difference or a reading difference. That output would need the paper's glm_results files or the figure notebook's `test_scores_pfc`. Printing the s.e.m. reading would also help.
- **SVC on all subsets:** I could not check whether running the SVC on all 500 subsets changes r². Given the margins, it would not change the outcome.
- **Supplementary Fig. 12c and Table 2:** neither is in the text read. A cell printing results/rat_stats.csv next to the notebook's mixed-model table (B6) would have made the comparison visible inside the notebook.
