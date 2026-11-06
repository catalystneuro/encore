**A. Outcomes**

None of the 14 claims is blocked. I take reading (s) (sub-networks) as primary, because the claims file says the paper's stated purpose supports it (M-SUB). Every data outcome below from fig4ac to fig6 depends on the significance test in problem 1, which I found to be anti-conservative.

| Claim | Outcome | Reason |
|---|---|---|
| data-recordings | reproduced | Cell 6 gives 25 recordings, 7735 neurons, 309.4 per recording, and 2.103 Hz (over 60 min) or 2.132 Hz (over recording length). All four are within tolerance, and the deposit already applies the 100-spike threshold. |
| fig4ac-te-lognormal | not_reproduced | Cell 12: the fit on the average distribution has R² of 0.08 to 0.61, against the 0.9 required, under both (f) and (s). The spread criterion passes. The low-TE mode (minimum 1.3e-9 bits, fitted σ of about 3 decades) is very likely spurious connections from problem 1, so this outcome is unreliable. |
| fig4bd-heavy-tailed-degree | reproduced (unreliable) | Cell 15: 21% (f) and 6% (s) of neurons lie above the random 99.9th percentile, against the 1% threshold, and the real maxima are well above the random ones. Problem 1 adds connections that depend on firing rate, which may shape the tail. |
| fig4bd-out-tail-longer | partially_reproduced | Cell 18: passes under (s) at both scales. Under (f) at 3.5–14 ms the largest in-degree (480) exceeds the largest out-degree (449). The Wilcoxon test is p ≤ 0.0015 everywhere. |
| fig5a-in-degree-uncorrelated | partially_reproduced | Cell 20, (s): 9 positive vs 41 negative (Pearson, binomial p = 2.8e-6) and 10 vs 40 (Spearman), so a significant negative skew, which the criterion grades as partial. Only (f, Spearman) is non-significant (20 vs 30, p = 0.10). The notebook has 50 correlations per panel; the paper has 40. |
| fig5b-out-degree-positive | reproduced | Cell 20, (s): 44/50 positive (p = 1.6e-8) and 39/50 (p = 4.5e-5). Under (f), Pearson is 35/50 (p = 0.003) and Spearman 26/50 (not significant). |
| fig5ab-correlations-beyond-null | reproduced | Cell 23: under (s), 94% to 100% of correlations lie beyond the null's 99th percentile. Under (f, Pearson) the in-degree panel is 84%, which fails. |
| fig5cd-pooled-trends | not_reproduced | Cell 25, (s): out-degree at 3.5–14 ms has ρ = 0.14 (p = 0.34). In-degree medians fall steeply (ρ = −0.96 and −0.94), which contradicts "no trend" even though the criterion only forbids a positive trend. Under (f), out-degree at 1.6–6.4 ms is negative. |
| fig6-information-gain-not-rising | reproduced | Cell 27: k < 0 at both scales under every reading of normalization and starting n, with no interval above zero. This was run only under (f), with sampled receivers and combinations. |
| table1-pid-examples | reproduced | Cell 29: all four checks are True. For example, synergy in the synergistic-and-redundant example is 0.4569 with II = 0.0001, and in the single-and-redundant example \|II\| = redundancy = 0.2502. |
| fig7b-connectivity-patterns | reproduced | Cell 33: upper-half fraction is 0.988 (Hebbian), 0.79 (firing rate) and 0.505 (degree). |
| fig7c-degree-modified-rule-matches | partially_reproduced | Cell 32: under (s) both modified rules match and the Hebbian and random rules do not. The firing-rate rule is nearer the real data than the degree rule (0.111 vs 0.169 for Pearson, 0.065 vs 0.142 for Spearman), so "degree-modified more closely" fails. The full criterion passes only under (f, Spearman). |
| fig7d-degree-rule-highest-conditioned-mi | not_reproduced | Cell 34: Hebbian has the highest unconditioned MI, but the random model has the highest conditioned MI (0.0023) and the degree rule the lowest (0.00153). I reran a few models at 50,000 runs and the ranking holds, so this is not estimator bias. |
| figs1-larger-model | not_reproduced | Cell 35, under both α/β readings: the degree rule's conditioned MI is below the random model's. The Hebbian and firing-rate conditioned MI are smaller at N = 40 than at N = 20, the opposite of the claim. |

**B. Problems**

1. **[affects a conclusion]** `hdn.te_network` / `significant`: the jitter test counts a surrogate only if its TE is strictly greater than the real TE. When jitter cannot change the counts, every surrogate ties and the pair is called significant. This happens when no sender spike falls near receiver activity, or when all relevant spikes are "same". I ran the helper on synthetic independent Poisson pairs (numba stubbed out):
   - Sender 0.03 Hz, receiver 0.2 Hz: 38/40 significant.
   - Sender 0.03 Hz, receiver 2 Hz: 25/40 significant (91/150 in a larger run, all with zero exceedances in 5000 surrogates).
   - Sender 0.14 Hz, receiver 2 Hz: 5/40.
   - Sender 0.56 Hz, receiver 2 Hz: 1/40.
   - Two disjoint trains were "significant" with TE of 6e-4 bits.

   The nominal rate is 0.001. This likely explains the densities of 2–33% (cell 9; the notebook's "expected_by_chance" of 0.1% does not hold), the log-TE mode near 1e-9 to 1e-8 bits that breaks the fig4ac fit, and rate-driven degrees feeding fig4bd through fig6. The cell 8 exact-vs-approximate check cannot catch this, because both versions share the tie rule.
2. **[affects a conclusion]** `PAST_BINS = (2, 3)`: the docstring says [44] is internally inconsistent. Its text gives bins t−1 and t−2; its Table 1 delays imply t−2 and t−3. Only (2, 3) was run, and the receiver's own past also excludes bin t−1. This open detail should have been run both ways.
3. **[affects a conclusion]** `pid_from_table`: redundancy takes the minimum over sources per state of I_F, weighted by p(i_F), as I_spec(i_F; {R, I_P}) − I_spec(i_F; I_P). The claims file's M-PID reading takes the minimum within each (i_F, i_P), weighted by p(i_F, i_P). The notebook attributes its form to Eq 8 of the version of record but does not flag the departure from the claims file, and the two give different synergy, which feeds all of fig5.
4. **[affects a conclusion]** `subnetworks`: only M-SUB reading (a) was run, with [44]'s replacement of unconnected neurons and the strongest edges by normalized TE. Reading (b) (random 75 edges) was not run. Groups with fewer than 75 significant edges are kept, not redrawn as the claims file says. At DataSet13's 1.9% density a 50-neuron group expects about 47 edges, and the edge count per sub-network is never printed.
5. **[affects a conclusion]** cell 31, `model_correlations`: in the degree rule, 56/100 (N = 20) and about 50/100 (N = 40) models have uniform degrees, so their correlations are NaN. Their means are taken over the remaining models only, a selected subset, which feeds the fig7c distance comparison.
6. **[does not affect a conclusion]** cell 34, `fig7d_ok`: `deg_beats` checks only FDR p < 0.001, not direction. It prints True although the degree rule's conditioned MI is the lowest. The criterion still fails through `top_c`.
7. **[does not affect a conclusion]** cells 26–27: fig6 used only reading (f), 30 receivers per recording and 20 combinations against the paper's 100. Reading (s) was feasible: 19,205 and 14,814 sub-network receivers have six or more inputs.
8. **[does not affect a conclusion]** cell 35 prints the figs1 verdict only for (s, Pearson). It fails on its other parts under every reading anyway.
9. **[does not affect a conclusion]** The model's conditioned MI from 2000 runs carries about 6–7e-4 bits of plug-in bias, roughly 40% of the reported values. In my rerun the ranking did not change at 50,000 runs.

**C. What I could not check, and the output that would have let me**

- **Size of problem 1 in the real data.** I could not measure it. The notebook should print, per recording and scale, how many significant pairs had zero exceedances over all 5000 surrogates (`ran == 5000 & exceed == 0`) and how many had no relevant sender spikes. It should also show the correlation of degree with firing rate, and the networks re-thresholded with ties counted as exceeding (≥).
- **Eqs 8, 16–24 and [44]'s details.** Neither the version of record's equations nor [44] is in my materials. That blocks checking the redundancy form, the model's currents and score (Eqs 16–20), the fitted coefficients in `RULES`, and [44]'s past bins, jitter width and sub-network rule. Printing the equations' text as read, and [44]'s Table 1 row, would let me check them.
- **Sub-network edge counts.** The distribution of edges per sub-network, and the number with fewer than 75, would settle problem 4.
- **Approximation at the longer scale.** The normal-approximation check covers only the 1.6 ms bins on two small recordings. The same check at 3.5 ms is needed.
- **Archive check.** No claim is blocked, so I made no archive query. The streamed archive's MD5 matches `checksums.md5` (cell 1).
