**A. Outcomes (46 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| trial-counts | reproduced | Cell 10: 70 sessions, 6 rats, 60,211 trials (paper 60,221), and 39,175 / 12,707 / 8,329 choice, no-choice and error trials, which match exactly. |
| block-structure | reproduced | Cell 12, reading (a): 104.9 trials per block, 8.2 blocks per session, range 5–12. All four values are within tolerance. |
| reaction-time | reproduced | Cell 14: 72.1% under 1 s, median 0.754 s. |
| tone-discrimination-errors | not_reproduced | Cell 16: 0.81% / 1.02% from the events, 0.27% / 1.11% from result codes 5 and 4. No reading is within tolerance. The event count is probably inflated (problem 4), so this outcome could change. |
| fig2b-reward-stronger-than-noreward | reproduced | Cell 20: 0.68 / 0.62 / 0.39 / 0.30 and the order hold under both O7 readings. Every p is below 1e-5 under both O8 readings. |
| fig2b-two-back-history | blocked (methods_underspecified) | Cell 22: both values and the direction match. O8 (a) gives p ≈ 1e-6, but O8 (b) gives p = 0.032 and 0.012, not < 0.0001. The readings disagree. |
| fig2c-sequence-frequencies | reproduced | Cell 24, pair as sum: 6.78 / 2.94 / 2.64 / 1.29% under O7 (a) and 6.88 / 2.87 / 2.54 / 1.28% under O7 (b). The top three are in order. |
| fig2c-reward-effects-fade | reproduced | Cell 26: under O8 (a), p = 0.92 and 0.94. Both values are about 0.74, the rise L1 < L1L1 < L1×4 holds, and the last is within 0.075 of 0.75. |
| fig2d-switching | reproduced | Cell 28: every prefix is on the switching side of 0.5 under both O7 readings. |
| fig2e-persevering | reproduced | Cell 30: 0.46 < 0.575 < 0.70, and both last values are above 0.5, under both O7 readings. The mirror sequence does not show it (P(R\|R0R0R0) = 0.45). It is not in the criterion but is worth reporting. |
| fig3-lsq-switching | partially_reproduced | Cell 33: the order LM > Q > F-Q > DF-Q and the switching pattern hold under every reading. Only 2–3 of the 4 residuals are within tolerance (DF-Q 0.00025–0.00027 against 0.0002 ± 0.00002). |
| table1-lsq-parameters | not_reproduced | Cell 34: at most 8 of 14 values are within tolerance (O1 a); 10 are needed for partial. |
| fig5-markov-accuracy | blocked (methods_underspecified) | Cell 41: all values are within 0.005 under every reading, and order 3 is highest under O3 (a) and (b). Under O3 (c), order 4 (0.5334) beats order 3 (0.5332). O3 (a) gives exactly the paper's 19,986 training trials. |
| fig5-constant-models | blocked (methods_underspecified) | Cell 43: Q, F-Q and DF-Q are within tolerance and above the local matching law under every reading. With Qi(1) = 0, as the criterion fixes, the local matching law scores 0.500 (O1 a) or 0.41–0.43 (O1 b), out of tolerance. It reaches 0.506–0.507 only with the author's assumed Qi(1) of 0.1–1.0, and only under O1 (a). As the paper specifies it, the model is degenerate. |
| fig5-variable-models-best | partially_reproduced | Cell 45: all three values are within tolerance and above their constant versions in 48 of 48 readings. F-Q is best in 40 readings; DF-Q is best in 8 (O1 b, O5 b, splits a and b). |
| fig5-fq-dfq-beat-all-models | blocked (methods_underspecified) | Cell 47: all 18 comparisons pass only under O3 (b), O1 (a), O5 (a). Under split (a), the paper's split, they fail; for example DF-Q (variable) against DF-Q (constant) gives two-sided p = 0.073. |
| fig5-fq-dfq-no-difference | blocked (methods_underspecified) | Cell 48: two-sided p < 0.05 in 4 of 12 readings, including the main one (O3 a, O1 a, O5 a: p = 0.008). The filter's seed noise is about the size of the effect (problem 1). |
| binary-prediction-accuracy | reproduced | Cell 50: 67.0–68.0% in every reading. |
| table2-ml-parameters | not_reproduced | Cell 52: under O1 (a), 6–8 of 16 values match depending on O3–O5, so the criterion's 8 is not reached under every reading. The DF-Q constant parameters differ (split a: α2 0.05, κ2 −1.1, against 0.45 and 0.45). The sigma values are unreliable (problem 2). |
| table3-parameter-averages | blocked (methods_underspecified) | Cell 56: 9 of 9 means match under O1 (a) and 6 of 9 under O1 (b). The criterion requires every O1 reading (see problem 9). |
| fig4-strategy-tracking | reproduced | Cell 58: the criterion holds in 24 of 24 readings. |
| suppdata1-choice-vs-q-difference | reproduced | Cell 60: Spearman correlation is 1.0 for every model and version. |
| neuron-counts | reproduced | Cell 64: 148 NAc and 66 VP units. |
| firing-rates | reproduced | Cell 66: NAc 2.60 ± 2.59 Hz and VP 10.21 ± 9.14 Hz under both readings. |
| fig8b-state-coding | blocked (methods_underspecified) | Cell 68: O14 (a) gives 80 / 33, an exact match. O14 (b) gives VP 37 against 33 ± 3.3. |
| fig8b-action-value-psth | partially_reproduced | Cell 70: 9 of 12 counts are within ±2 neurons, and all are below 25% of their region. |
| fig8b-action-command-coding | not_reproduced | Cell 72: 15 and 14 neurons against 17 ± 1.7 and 12 ± 1.2. |
| fig8b-action-coding | reproduced | Cell 73: 63 and 26 neurons. |
| fig8b-reward-coding | reproduced | Cell 74: 96 and 44 neurons. |
| fig8b-nac-vp-same-event-coding | not_reproduced | Cell 76: action command differs between regions, p = 0.029. |
| fig8b-ql-vp-higher | partially_reproduced | Cell 77: phase 3 gives p = 0.009 with VP higher; phase 2 gives p = 0.18. |
| fig8b-qr-no-region-difference | reproduced | Cell 78: p = 0.35 and 0.19. |
| preference-balance | reproduced | Cell 80: none of the six tests departs from 50% (all p > 0.4). NAc action command is 46.7% against 53 ± 5.3, which is reported but is not part of the outcome. |
| nac-noreward-preference | partially_reproduced | Cell 81: NAc 72.9%, but the O11 (a) signed-rank test gives p = 0.003, not < 0.0001. The sign test gives 8e-6. The VP part holds. |
| core-shell-no-difference | blocked (metadata_insufficient) | Confirmed on the archive (see below). |
| fig8c-regression-action-value | not_reproduced | Cell 85: 6 of 12 values match. |
| fig8c-ql-vp-higher | reproduced | Cell 86: p = 0.0085 and 0.0041, VP higher in both phases. |
| fig8c-regression-detects-more | reproduced | Cell 87: 165 against 133 neurons, and VP has the larger QL share in phases 2 and 3 in both analyses. |
| fig8d-state-value-vp-higher | not_reproduced | Cell 88: 2 of 6 values match; the region test gives p = 0.55 and 0.08. |
| fig8d-policy | partially_reproduced | Cell 89: 5 of 6 values match. |
| fig8-above-chance | reproduced | Cell 91: 44 of 44 populations give p < 0.01 under both chance levels. The paper states no chance level. Where it does (50% for preferences), the notebook uses 50%. |
| fig9-state-information | reproduced | Cell 95: holds in every reading. |
| fig9-action-information | reproduced | Cell 97: holds in every reading. |
| fig9-reward-information | not_reproduced | Cell 99: reward information is above threshold before the L/R entry in 16–28 of 23–28 windows, in every reading (but see problem 5). |
| fig9-action-value-information-low | reproduced | Cell 101: holds in 48 of 48 readings. |
| action-information-outlasts-reward-peak | reproduced | Cell 103: holds in every reading. |

Totals: 24 reproduced, 6 partially reproduced, 8 not reproduced, 8 blocked (7 methods_underspecified, 1 metadata_insufficient).

**Archive check for core-shell-no-difference.** The asset metadata and the dandiset description name only NAc and VP. I range-read the electrode table of two files: its only columns are `location` (NAc or VP), `group` and `group_name`, with NAc_group on electrodes 1–16 and VP_group on 17–32. Units carry only `Area` and `Electrode_ID`. The NAc wires could be split 1–8 against 9–16 as a guess at the two bundles, but nothing assigns either to core or shell, so no part of the claim can be tested.

**B. Problems**

1. [affects a conclusion] `particle_filter` (cells 38, 54): every 5000-particle run uses a single seed. On synthetic F-Q data (35 sessions × 550 trials), I found a seed-to-seed per-session SD of about 0.00027. The F-Q vs DF-Q Wilcoxon p ranged from 0.37 to 0.93 across four seeds on identical data. That noise is as large as the real median F-Q − DF-Q differences (0.0001–0.0008). It bears on fig5-fq-dfq-no-difference, on the F-Q vs DF-Q ranking in fig5-variable-models-best, and on the borderline comparisons in fig5-fq-dfq-beat-all-models.
2. [affects a conclusion] Cell 38, sigma search: it uses 1000 particles (the paper uses 5000) on a 4×4 grid. The chosen σα is the grid maximum, 0.02, in most readings, so the optimum is not bracketed. The training scores across the grid differ by about 0.0001–0.0005, which is near the filter's noise. The sigma values compared in table2-ml-parameters, and the chosen-sigma scores in Fig. 5, therefore rest on a noisy search at the edge of the grid.
3. [affects a conclusion] Cells 36 and 43, local matching law: the criterion fixes Qi(1) = 0, and under it the model scores 0.500 or less. The headline row (cell 39) and the Wilcoxon inputs (cell 47) use the author's assumed Qi(1) = 0.5. The notebook does flag this as an assumption, which is right, but the main table reads as if the local matching law were reproduced.
4. [affects a conclusion] Cell 16, the `held` filter (`pokeC_off_time >= tone_off_time - 0.01`): some tone-A tones last under 1 s (1st percentile 0.458 s in cell 5, while the paper's cues run 1000–2000 ms). This suggests the tone stops when the rat exits early. If so, premature-exit errors pass the `held` test and inflate both event-based numerators (317 and 129). The result-code meanings are also inferred, not documented.
5. [affects a conclusion; this is a claims-file reading] fig9-reward-information: the criterion requires reward information to be below threshold before L/R entry. The paper says only that it "started to increase at the presentation" of the tone, and that reward information lasts into the next trial. Because rewards are correlated across trials within a block, pre-entry information above threshold is expected from the paper's own findings. Pre-entry values are about 5% of the peak (0.004–0.007 against 0.09–0.11), so the paper's qualitative statement is supported. In cell 99, "before entry" also uses the median reaction time, not each trial's entry time.
6. [does not affect a conclusion] Cell 93: QL/QR mutual information is computed only from the F-Q run under O1 (a) and O5 (a), although O1 (b) and O5 (b) runs are already in `tab2runs`.
7. [does not affect a conclusion] `_pf_session`: the O13 (b) "posterior mean after e(t)" is the weighted mean of Q *before* the update with r(t). For QL and QR, O13 (b) is therefore almost the same as O13 (a), so the O13 robustness check is weaker than it looks.
8. [does not affect a conclusion] Cell 93: the MI threshold uses independent random events, but QL, QR and previous reward change slowly and firing drifts within a session. "Above threshold in 100% of windows" for QL/QR may partly reflect that drift. This follows the paper's method.
9. [does not affect the computations; a claims-file inconsistency] The table1 and table2 criteria treat O1 as the parameterization (a match under one O1 reading suffices). The table3 criterion requires every O1 reading, yet under O1 (b) κ is on a different scale by construction. This alone is what blocks table3-parameter-averages.
10. [does not affect a conclusion] Cell 47: the partial-reproduction column is computed two-sided only. One-sided, the main reading would meet the partial condition. The readings disagree either way.
11. [does not affect a conclusion] Cell 32, `mirror_avg`: it pairs row 5 (L0 R0 L0 R0) as the "left" sequence instead of row 4. The squared error is unchanged, and the shared-optimum argument is correct.
12. I tested `class_index` (against brute force), `mi_bias_corrected` (≈0 for independent data, ≈1 bit for a deterministic 1-bit relation), `q_update` in both forms, `count_spikes` and `mw_indicator_p`. All are correct. `mw_indicator_p` reproduces all of the paper's region p-values from its counts (0.19, 0.80, 0.45, 0.81, 0.17, 0.03, 0.004). I found no leakage between training and test data: the Markov counts, constant fits and sigma choice all use training sessions only.

**C. Not checked, and the output that would settle it**

- Filter seed variability on the real data: per-session scores and the F-Q/DF-Q Wilcoxon p over 5 or more seeds.
- Test-set scores of the variable models at the paper's Table 2 sigmas. The runs exist but are not scored.
- A sigma search that extends past σα = 0.02 at 5000 particles.
- Training log-likelihood at the paper's Table 1 and Table 2 parameter values next to the fitted optimum, to tell a second optimum from a mismatch (DF-Q in particular).
- For tone-discrimination-errors: tone duration (tone_off − tone_on) for the counted error trials, and a recount that keeps only trials whose tone lasted at least 1 s.
- The local-matching-law Wilcoxon results under the other Qi(1) values.
- The QL/QR mutual-information curves under O1 (b) and O5 (b).
- The Fig. 3 residual of the local matching law at the paper's α = 0.05, Q0 = 0.07.
