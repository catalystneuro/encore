**A. Outcomes** (32 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| fig1b-faster-novel-learning | blocked (data_missing) | The archive API lists 5 assets, one per rat. Each holds only the N, F and N' epochs, so there are no de novo sessions. |
| fig1-denovo-final-performance | blocked (data_missing) | Same reason. |
| fig1c-session-performance | blocked (data_missing) | Same reason. A three-session ANOVA is not the claim's test. |
| fig1c-familiar-above-novel | not_reproduced | N-F-N' part (cell 14): Tukey F vs N p = 0.70; ZT2 does worse in F (0.40) than in N (0.68). The F-N-F'-N' part is blocked (data_missing): those 3 rats are not in the dandiset. The test uses 3 groups instead of the paper's 5. |
| figs1b-first-session-inbound-outbound | blocked (data_missing) | Needs the de novo sessions. |
| cells-per-session | reproduced | Cell 16: CA1 27.5 per session (paper 30.5 ± 9.8), PFC 36.5 (paper 37.4 ± 19.3). |
| figs3a-ca1-global-remapping | reproduced | Cell 21: CA1 F-N' vs shuffle Tukey p = 0.075. Across 100 shuffle draws, 87% are n.s. The margin is thin (difference +0.074). |
| figs3a-pfc-similar-ca1-lower | partially_reproduced | Cell 22: spatial correlation meets the criterion (PFC p = 0.52; CA1 lower, p < 1e-4). Rate overlap does not: CA1 F-N' is not below N-N' (p = 0.32 and 0.45). |
| fig2d-pv-similarity | reproduced | Cell 18: RM-ANOVA p = 8.8e-8; CA1 F-N' < N-N' p = 0.0001; PFC p = 0.99. Same result at 4 and 2 cm smoothing and with the > 3 Hz peak rule. |
| fig2e-ca1-error-familiar | partially_reproduced | Cells 30–31: CA1 error is higher in F than N (Dunn p = 2e-140). But CA1 F does differ from its shuffle: it is worse than chance (Wilcoxon (a) p = 2.4e-8, (b) p = 0.042), so the "no difference" part fails. |
| fig2e-pfc-error-stable | partially_reproduced | Cell 32: PFC is below its shuffle in N and in F. But PFC N vs F differs (Dunn p = 7e-6; F 186 cm vs N 149 cm), so "similar across environments" fails. It differs in every variant. |
| fig2f-switch-dynamics | partially_reproduced | Cell 34, reading (a): CA1 trial −1 vs 1 p = 0.002 (rise); PFC p = 0.12 (n.s.). Reading (b) cannot be judged because of a labelling bug (B1). The code-decoder variant fails under both readings. |
| figs3c-pfc-assimilation | reproduced | Cell 24, 8 cm: PFC F-N' > F-N p < 1e-4; CA1 F-N vs F-N' p = 0.065; CA1 F-N' < N-N' p < 1e-4. Same at 4 and 2 cm. |
| figs3d-pfc-similarity-over-trials | partially_reproduced | Cell 26: PFC rises from first to last trial under all three readings. CA1 stays flat only under reading (a), and that test is cut at K = 9 (B3). CA1 falls under (b) (p = 0.0014) and (c) (p < 1e-4). |
| figs4-ramping-fraction | not_reproduced | Cell 36: CA1 3.0% (pooled) and 3.7% (N') vs 16.4%; PFC 3.1% and 3.0% vs 18.1%. Denominators are 1652/596 vs 495 (CA1) and 2192/728 vs 636 (PFC). |
| figs4-ramping-generalization | blocked (other) | Ramping cells were not found as the paper finds them (claim above). Only one animal-trajectory population per region has ≥ 3 ramping cells. The main reading meets the criterion's partial clause; the pooled variant fails part (1) (p = 1). |
| figs4d-reward-location-similarity | reproduced | Cell 28: Grubbs p ≥ 0.4 in every test, for both readings (all bins, per trajectory) and both pairs (F-N', F-N). |
| figs5d-path-equivalence | reproduced | Cell 46: PFC > CA1 in N, F and N' (p ≤ 0.0004), at all three smoothing widths. |
| figs5e-path-equivalence-stable | partially_reproduced | Cell 48, 8 cm, F vs N': PFC r = 0.572, just below the 0.576 tolerance floor; CA1 r = 0.231 (within tolerance); Fisher z p = 0.0012. At 4 cm both r are within tolerance (fully reproduced). |
| figs5f-path-equivalence-vs-selectivity | blocked (methods_underspecified) | Cell 50, 8 cm: signed SI gives no correlation; absolute SI gives correlations in both regions (CA1 SI(IN) p = 0.025; PFC p ≤ 9e-5). The criterion calls this methods_underspecified. |
| fig3d-selectivity-index | not_reproduced | Cell 42, 8 cm: no reading puts CA1 within tolerance (r ≈ 0.28 vs 0.56). Reading (c) F has CA1 p = 0.41, so the partial clause fails too. Only 2 cm meets the partial clause. |
| fig3e-selectivity-stable | not_reproduced | Cell 44, 8 cm: CA1 is significant under both readings (r = 0.318, p = 0.012; r = 0.384, p = 0.0009). PFC r = 0.437 is just out of tolerance. Only 2 cm meets the partial clause. |
| manifold-cell-counts | reproduced | Cell 52, code reading (b): 99 CA1 and 171 PFC cells (paper 98 and 171). The Methods reading (a) gives PFC 151, out of tolerance. |
| fig3fg-manifold-shapes | reproduced (per criterion) | The criterion makes this follow fig3h and fig3i, which both reproduce. The plotted embedding (cell 54) shows one thread per pass, not a ring or a double V. |
| fig3h-inseq-outseq-distance | reproduced | Cell 56: CA1 OutSeq < InSeq p = 0.0098; PFC InSeq < OutSeq p = 0.0012. All seeds and alignments agree. |
| fig3i-phase-location-distance | reproduced | Cell 58, Methods reading: holds in both regions and all 3 seeds. The code variant fails (seed 0: CA1 reversed, PFC p = 0.19). |
| fig3j-familiar-novel-manifold | partially_reproduced | Cell 60: PFC holds. CA1 F-N' is below its shuffle at p ≤ 2e-47 in every seed, not n.s. as claimed. |
| figs6-high-dimensional-distances | partially_reproduced | Cell 64: the 3H and 3I relations hold in neural space. 3J fails: CA1 p = 7.5e-78. |
| fig4d-pfc-ccgp | not_reproduced | Cell 67: 12 of 16 PFC decoders at p < 0.001; 2 of those 12 are artefacts (B2), so 10 of 16 are real. |
| fig4d-ca1-ccgp-chance | not_reproduced | Cell 68: 8 of 16 CA1 decoders at p < 0.05. Six are real: environment decoders with CCGP 0.58–0.68 against a 95th percentile of 0.50–0.55. |
| figs7b-geometric-null | not_reproduced | Cell 70: PFC CCGP does not exceed its null under either reading (p 0.05–0.85). Using the median of decoders instead of the mean does not change this. |
| figs7d-dichotomies-decodable | not_reproduced | Cell 72: "most decodable" holds (CA1 35/35, PFC 32/35). The regions differ: rank-sum p = 1.2e-9, CA1 higher. |

Chance levels: the CCGP null medians are 0.50, as in the paper. Decoding chance is the cell-ID shuffle, as the paper defines it.

**B. Problems**

1. **[affects a conclusion]** Cell 34, `trial_tests`, reading (b): N trials with index k ≥ 11 get labels 1 to 10 and are pooled with F trials 1 to 10. The output shows this: "n 1" is 358 under (b) against 191 under (a) for CA1, and 449 against 269 for PFC. The reading (b) results for fig2f are invalid.
2. **[does not affect a conclusion]** `nfn.svm_ccgp`, p = mean(null > acc): when the decoder predicts one class for every point, accuracy equals the whole null (0.500), every shuffle ties, and p = 0. The IN_R/IN_L sequence decoders (`p_ge` = 1.0) are counted as significant in both regions. On synthetic input, constant predictions gave p_ge = 0.965. The fig4d outcomes stand without these decoders. `decode_dichotomy` uses the same rule.
3. **[affects a conclusion]** Cell 26, figs3d: K is the smallest number of kept trials over animals. For CA1 under reading (a), K = 9 (set by JS34), so "last" is the 9th kept pass, not the last trial. Reading (b) for CA1 has only 3 animals (JS34 and ZT2 have 0 kept trials).
4. **[affects a conclusion]** fig3d, fig3e, figs5e: the outcome depends on the open smoothing width (4 cm fully reproduces figs5e; 2 cm makes fig3d and fig3e partial). The notebook gives no rule for deciding these. If the claims file's fig2d rule (main reading unless the variants disagree, else methods_underspecified) were applied, these would be methods_underspecified.
5. **[affects a conclusion]** `nfn.single_trial_matrix`: filling empty bins within each pass is an assumption the notebook states. Together with 8-cm smoothing at 1-cm bins, the embedding is made of per-pass threads (cell 54 figure). The CCGP, null-model and fig3j results depend on this, and no unfilled variant was run.
6. **[affects a conclusion]** Cell 38, figs4-ramping-generalization: requiring ≥ 3 cells per population is the author's assumption. The main and pooled variants give opposite results for part (1).
7. **[does not affect a conclusion]** `decode_session` (cell 30): the main decoder's median error in N is 149–172 cm against a shuffle of about 220 cm, so most bins are decoded onto the wrong trajectory even in the same room. The clock check (cell 11) only tests the restricted decoder, in-sample. The PFC N-vs-F difference changes sign between the main and restricted decoders (F higher, then F lower), though it is significant in both.
8. **[does not affect a conclusion]** Cell 14: the rm-ANOVA has 3 groups where the paper has 5. ZT2 F has only 24 trials in 1554 s, against 42 in N and 60 in N'; the notebook does not comment on this.
9. **[does not affect a conclusion]** Deviations forced by the data or stated: no SWR or theta exclusion (no event times in the files); interneuron lists not applied; region read from the tetrode-number interpretation (the cell counts match, which supports it); 100 shuffles instead of 1,000 in figs7d.
10. **[does not affect a conclusion]** `pv_cells`: the ≥ 3 Hz peak is taken on the 101-bin resampled maps, not the native maps.

The helpers that matched references on synthetic input:
- `grubbs` detects an injected outlier.
- `rm_anova_tukey` matches statsmodels' AnovaRM exactly.
- `fisher_z_compare(0.64, 171, 0.21, 99)` gives z = 4.26, against the paper's 4.25.
- `ramping` is correct for both directions.
- `dichotomies()` returns 35.

**C. What I could not check, and the output that would settle it**

- **fig2f reading (b):** a re-run with N trials labelled k − 10 restricted to k < 10.
- **fig1c:** whether ZT2's F trials table is complete. Needed: well-to-well transits counted from position per epoch, next to the trials-table counts.
- **Decoder:** whether it works properly. Needed: the cross-validated N' error of the unrestricted decoder, and the fraction of bins decoded onto the correct trajectory in N and F.
- **CCGP:** the fraction of test points predicted as class 1 for each decoder, to confirm the constant-prediction cases.
- **figs3d:** results with "last" taken as each animal's final kept trial, and the epoch each kept trial comes from.
- **Manifolds:** the embedding and the CCGP without gap filling, or with fewer threads per pass.
- **fig2e scale:** the error magnitudes in Figure 2E, to compare with 150–230 cm. The figure image is not in `paper/`.
