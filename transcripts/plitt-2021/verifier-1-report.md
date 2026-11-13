**Verifier report, round 1: Plitt & Giocomo 2021 on DANDI:000054 (0.260415.1712)**

The claims file holds 29 claims. My outcomes: 13 reproduced, 4 partially reproduced, 10 not reproduced, 2 blocked. No attempt record was available to me, so the counts come from the claims file and my own judgements.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| cells-per-session | reproduced | Reading (a), R and F mice, sessions 1, 3 and 8 to N: 161 to 3,653 cells (nb1 cell 9). Both ends are within tolerance. |
| session-and-trial-counts | not_reproduced | Rare 26 sessions and 2,800 trials, frequent 21 and 1,986: all within tolerance. Decision-mouse trials are 3,217 under reading (a) and 2,022 under (b), against 2,460 ± 246 (nb1 cell 11). |
| vr-deposit-link | reproduced | 89 of 89 NWB files match exactly one deposit file of their own mouse, offset 0, difference 0 (nb2 cell 5). |
| training-intermediate-fraction | reproduced | Reading (a), pooled: rare 3.49% (below 4%), frequent 59.83% (within 0.06 of 60%) (nb2 cell 7). Reading (b) fails, because R4 (4.1%) and R6 (5.7%) are above 4%. |
| place-cell-fractions | not_reproduced | No combination comes close: counts 25,053 / 17,025 (reading a) and 21,945 / 14,345 (reading b), against 15,829 / 8,933. Fractions 0.60–0.70, against 0.43. Total recorded cells (36,550 / 30,018) match what the paper implies (nb1 cell 13). |
| edf4a-fewer-place-cells-frequent | reproduced | Frequent is below rare for any S-tilde, S-tilde = 0 and S-tilde = 1, under all four readings (nb1 cell 16). |
| edf4a-overlap-above-chance | partially_reproduced | t = −10.1 (a) and −7.7 (b), 47 sessions, actual overlap above chance. But actual and chance are 0.164 / 0.147 (rare) and 0.085 / 0.069 (frequent), against the paper's 0.0607 / 0.0478 and 0.0198 / 0.0106. The chance level, defined the same way, is about 3 to 6 times the paper's because there are more place cells (nb1 cell 18). |
| edf4bc-overlap-cells-at-ends-and-reward | not_reproduced | 4 of 48 combinations fail, all with reference (b) and end-point reading (a). Overlap-cell counts are 5,997 / 2,552 (a) and 3,759 / 1,272 (b), against 2,219 / 594 (nb1 cell 20). |
| fig2eh-place-cell-similarity-differs | not_reproduced | No z-scored entry lies outside the range of the 923 permutations, under either speed reading. The raw matrix does pass at the 95% level. Only the 2020-code variant that counts R6 as frequent passes (nb1 cell 22). |
| edf5-umap-rare-frequent-separable | reproduced | 17 of 20 clusters beat 100 shuffles and 16 of 20 beat 1,000, so both readings hold. 18,742 cells were kept, against the paper's 18,230 (nb1 cell 26). |
| edf6-nmf-confirms-remapping | not_reproduced | The rare mean step share (0.763) is below the frequent mean (1.072), and the difference is not significant (nb1 cell 24). |
| fig3ab-block-versus-gradual-similarity | not_reproduced | Difference 0.042, inside the 95% band of ±0.116 (nb2 cell 13). |
| edf7-checkerboard-sessions | not_reproduced | R5 session 8: 0 of 16 S-tilde = 0.25 trials have SF above 0.5 (range 0.424 to 0.465). The other five named sessions pass (nb2 cell 15). See B3. |
| fig3f-zscored-difference-at-025 | reproduced | Entries (0.25, 0.5) at −0.409 and (0.25, 1.0) at −0.367 lie outside the 2.5–97.5 percentiles. All variants agree (nb2 cell 17). |
| fig4-sf-stable-along-track | reproduced | 44 of 44 bins separated in both groups. Rare 0.75 and 1.0 curves overlap in 45 of 45 bins, and 0.25 is nearer 0 in 45 of 45. Frequent 0.25 lies between 0 and 0.5 in 45 of 45 (nb2 cell 19). |
| fig6a-dkl-sign | partially_reproduced | The test passes (−0.817, outside the permutation range) and the signs are right. 43 of 47 sessions is within tolerance and rare −0.66 is within −0.88 ± 0.23. But 8 mice falls outside 9 ± 0.9, and frequent 0.158 falls outside 0.50 ± 0.11 (nb2 cell 21). |
| fig6bc-pooled-dkl | partially_reproduced | Rare −0.464 is within tolerance; frequent 0.125 is not (0.42 ± 0.042). Signs hold under both readings (nb2 cell 23). |
| fig6d-prior-reconstruction | not_reproduced | The test passes (−0.902), but the rare mean is +0.223 and only 2 of 6 rare mice are negative. Frequent 1.125 is outside tolerance. The measure is biased in the rare-negative direction's disfavour; see B1 (nb2 cell 25). |
| map-estimate-values | reproduced | All four values are within 10% under both readings and all three likelihoods (nb2 cell 27). |
| edf9-early-sessions | reproduced | Session 3 has the expected sign in 8 of 11 mice under both readings. Every mouse has a majority sign in sessions 8 to N (nb2 cell 29). |
| edf9k-null-models-rare | reproduced | All five Wilcoxon tests give p = 3e-8 with the rare posterior closer, n = 26 (nb2 cell 31). |
| edf9l-null-models-frequent | not_reproduced | The uniform-prior null gives p = 0.12 and a median of −0.018; the frequent posterior is closer in only 5 of 21 sessions (nb2 cell 31). |
| edf10-decision-mice-like-frequent | reproduced | Pooled Delta D_KL is +0.042 (a) and +0.125 (b). Every FD mouse's reconstructed prior is positive. Reading (b) carries no evidence; see B1 (nb2 cell 33). |
| edf1-licking-before-reward | reproduced | In all three reward bins the lick rate rises and peaks within 50 cm of the reward. 12 of 12 mice lick less over 0–225 cm, under both speed readings (nb1 cell 29). |
| edf2-fh-best-predictor | blocked (data_missing) | The API lists 126 assets for this version, all NWB, with no scene renders. Nothing could be tested. |
| fig7-model-reproduces-remapping | reproduced | Median Delta D_KL is −0.564 for rare-trained models and +0.093 for frequent-trained ones (10 of 50 below 0). All likelihoods agree (nb2 cell 35). |
| fig7g-model-prior-reconstruction | partially_reproduced | The signs are right (−0.098 and +0.626 bits). The magnitude test passes as written, but only because the neural rare mean it is compared with (+0.223) has the wrong sign. The "less closely matched than neural" half is therefore not shown for rare (nb2 cell 36). |
| edf3-simulated-posterior-population | not_reproduced | Reading (b) gives +0.030 at entry (0.25, 1.0), where the recorded value is −0.367. Reading (a) gives −0.036. Both are near zero (nb2 cell 38). |
| supp-earlier-morph-studies | blocked (other) | It is a simulation that uses no data from this paper; correctly blocked. |

### B. Problems

1. **[affects a conclusion]** `morph.reconstruct_prior` (fig6d, fig7g, edf10 reading b). The formula is coded as the criterion states it. Z(f̂) is the row sum of the unnormalised Q, which equals the density of the trials, not the marginal under the prior.
   - The formula recovers the prior only when the f̂ values are drawn from that prior. My synthetic test confirms this: Delta D_KL −1.1 in that case.
   - On this task's design (five S-tilde levels, equally frequent, plus jitter), an ideal observer sampling the rare posterior gives a reconstructed-prior Delta D_KL of **+0.55**. An ideal frequent observer gives +0.94. Yet its Q-based Delta D_KL is correctly −0.21.
   - So the rare mice's positive values in fig6d, the all-positive FD reconstructions in edf10 (b), and the neural magnitude used as the yardstick in fig7g do not tell the data apart from the method.
   - The paper reports −0.46, so either the paper's code defines Z or the f̂ range differently, or this reading is wrong. The notebook never checked the measure against an ideal observer.
2. **[affects a conclusion]** Place cells (`spatial_info`, `place_cells`; place-cell-fractions, edf4a-overlap, edf4bc, fig2eh, and edf4a-fewer through its cell set).
   - Detection runs about 60% above the paper, while the cell totals match. The authors' 2026 masks stored in the files are also high (0.615 / 0.486, nb1 cell 14), so this may come from the data or the method rather than a bug.
   - One variant was never run: the 2020 code's place-cell signal, activity divided by the 95th percentile (header M2). Because the code adds 0.001 before the log, spatial information depends on scale. In my synthetic test, SI went from 3.91 to 3.75 to 0.79 as the map scale went from 10³ to 1 to 10⁻².
   - The claims file's M2 says a per-cell scale "changes … not spatial information". That is a misreading of the code it cites.
   - Under the raw signal used here, whose values run into the thousands, the +0.001 regularisation does nothing.
3. **[affects a conclusion]** edf7 (nb2 cell 15). The claims file says the author has to show how the paper's session numbers map onto the dataset. The notebook assumes file "day" equals the paper's session number without showing it. That matters here because R4 has a day-6 file, the R5 files were replaced in this version, and the failing session is R5 session 8. The deposit link (dates and session numbers) could have established the mapping.
4. **[does not affect a conclusion]** `step_share` / `row_step_share` (edf6, fig3ab). The share has no upper bound when a row is not monotone. My synthetic row gives 5.0, and F5 day 10 gives 12.26, which pushes F5's mean to 3.4. I recomputed from the printed session values with the share clipped at 1 (difference 0.025, band ±0.157) and with medians (0.056, band ±0.267). Neither is significant, so the outcome stands.
5. **[does not affect a conclusion]** The analyses use 47 sessions (26 rare), where the paper has 45 (24 rare). The notebook does not try to identify the two extra rare sessions. All counts stay within tolerance.
6. **[does not affect a conclusion]** edf9k/l (nb2 cell 31) were run with the Methods likelihood only. The claims check asks that outcomes differing between the likelihood widths be reported, and edf9l's uniform-prior null is borderline.
7. **[does not affect a conclusion]** fig2eh (nb1 cell 22) does not run the 2020 code's unsmoothed variant listed in M5.
8. **[does not affect a conclusion]** The fig7 criterion misreads the code. It says the test stimuli lie "all between 5.5 and 38.5 f_h". In fact `wallmorphx` folds for S below −0.1, down to 0.04 f_h at S ≈ −0.2, so 25% of the test stimuli lie outside S −0.1 to 1.1. The notebook prints "0.04 to 38.45 f_h" without comment.
9. **[does not affect a conclusion]** nb1 cell 3 labels sessions with `k[0]`, which is "t" for both training and testing, so the session listing cannot be read. Separately, `asset_table` silently drops any path its pattern does not match; the API confirms all 126 assets match, so nothing was lost.
10. **[does not affect a conclusion]** In edf4bc, reference (b) includes the overlap cells themselves in the reference population. This pulls share and reference together and is what makes the four failures marginal (ratios 0.955 to 0.986). This is allowed by the criterion's wording.

### C. What I could not check, and the output that would settle it

- **How the paper's code computes Z or limits the f̂ range in prior reconstruction.** An ideal-observer check of `reconstruct_prior` on each session's real trial design, printed in the notebook, would have shown the bias in B1 directly.
- **Whether the over-count of place cells comes from the signal.** Place-cell fractions under the 95th-percentile-normalised signal would settle it.
- **The numba shuffle against a direct implementation.** Shuffle counts from `_shuffle_counts` next to a plain numpy shuffle for about 50 cells of one session would verify it. The 0.91–0.97 agreement with the stored masks is only partial reassurance.
- **The session-number mapping for edf7.** A per-mouse table of file day against the ordinal of its date among the deposit's task-track days would show it.
- **Which decision-mouse sessions give 2,460 trials.** A per-session FD trial table by kind (training or testing) would allow other readings to be tried.
- **Whether edf5's separability reflects condition or mouse identity.** Logistic regression with mice left out would answer that.
- **edf9k/l under the 0.3- and 0.4-unit likelihoods.** Those runs were not in the notebook.
- **The plots.** I could not view them; I relied on the printed ranges.
