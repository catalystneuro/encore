**Verifier report, round 1: Drieu, Todorova & Zugaro 2018 (doi:10.1126/science.aat2952) on CRCNS hc-18**

The claims file has 35 claims. The travel/sleep notebook tests 16; the decoding notebook tests 14 and marks 5 as blocked. My outcomes: 9 reproduced, 9 partially reproduced, 10 not reproduced, 7 blocked. For 2 of the 7, the run exists but a bug invalidates it. For the other 5, I do not accept the stated block reason.

### A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| figs1-travel-similar | not_reproduced | Velocity (reading b) and laps match within tolerance, and their ANOVAs give P = 0.49 and 0.053. The duration ANOVA gives P = 0.023, and Passive 1 at 9.21 min is outside 8.24 ± 0.69. The moving-time variant puts all three means within tolerance but still gives P = 0.045 (cell 11). |
| fig1c-field-size-similar | not_reproduced | Kruskal-Wallis P ≤ 0.05 under 3 of the claims file's 4 readings (P = 0.0065, ≈0, 0.0017). Only reading b, peak field, gives P = 0.070 (cell 13). |
| fig1c-peak-rate-lower-passive1 | reproduced | Passive 1 median 2.51 Hz against Active 3.82 Hz. Rank-sum with Bonferroni P = 1.7e-6, Kruskal-Wallis P = 2.6e-6. Holds under every reading (cell 14). |
| figs2b-place-cell-count | not_reproduced | Totals are 207/203/228 (reading a) and 183/195/207 (reading b) against 94/150/135; none is within tolerance. ANOVA P = 0.055 and 0.128 (cell 9). |
| figs2c-track-coverage | reproduced | 100% coverage pooled and per rat in all conditions (cell 15). This is trivial given the oversized fields (problem 5). |
| fig1d-no-remapping-p1-active | partially_reproduced | No reading gives bootstrap P < 0.01. One reading of 8 (fields b, cells in both, linear correlogram) gives bootstrap P = 0.014, Rayleigh 1.2e-4, V-test 1.1e-5. The other 7 give bootstrap P = 0.09 to 1.0 (cell 18). |
| fig1e-no-remapping-active-p2 | partially_reproduced | Reading b/both/linear gives bootstrap P < 0.0005, Rayleigh 1.6e-6, V-test 1.5e-7: all below 0.001 but not below 1e-9 or 1e-10 (cell 19). |
| figs2d-stability-p1-p2 | partially_reproduced | Reading b/both/linear gives bootstrap P = 0.016 and V-test 1.6e-3. But the Rayleigh test, which the claim treats as an absence, is significant under every reading (P = 0.004 to 0.011) (cell 20). |
| fig2b-theta-frequency-unchanged | reproduced | ANOVA P = 0.13 to 0.41 under all four readings (cell 23). The test is weak (problem 6). |
| fig2b-theta-power-reduced | partially_reproduced | Active is highest under every reading. Best per-rat ANOVA P = 0.035 (LFP b, moving samples); post hoc tests are not significant; per-window P = 1.7e-3. Nothing reaches P < 0.001, and the harmonic is not reduced (cell 24). |
| fig2b-theta-asymmetry-reduced | reproduced | Kruskal-Wallis P = 3.8e-22 (LFP a) and 2.2e-78 (LFP b). Both passive conditions are closer to 0 than Active, with Bonferroni P ≤ 1e-16 (cell 25). |
| fig2cd-spike-bursts-slower | not_reproduced | Median modes are 0.9999, 1.0003 and 1.0000. Kruskal-Wallis P = 0.62 (phase a) and 0.024 (phase b) (cell 28). |
| figs4b-proportions-oscillating-precessing | not_reproduced | The oscillation binomial tests fail: Active vs Passive 1 P = 0.058 and Active vs Passive 2 P = 0.091 (phase a); 0.015 and 0.20 (phase b). The precession half is invalid (problem 1) (cell 29). |
| fig2f-phase-precession-degraded | blocked (other) | In-field spikes are selected from the wrong track bins (problem 1), so cell 30 does not test the claim. The data suffice; it needs a rerun. |
| figs4de-precession-range-similar | blocked (other) | Same bug (cell 31). |
| fig3b-average-theta-reconstruction | partially_reproduced | All three scores are within tolerance (0.178, 0.245, 0.205) and Active is highest. Slopes: Passive 1 23.0 cm/cycle against 6 ± 3, Passive 2 17.3 against 21 ± 3, both outside; Active 46.1 is within (cell 8). |
| figs5b-per-rat-reconstruction | partially_reproduced | Score P = 0.0075 and quadrant P = 0.028, Active highest. Slope P = 0.079 (cell 10). |
| fig3c-theta-scores-above-chance | reproduced | All three signed-rank P ≤ 4.7e-238 with medians above 0; Kruskal-Wallis P = 4.2e-25 (cell 12). |
| fig3c-proportion-significant-theta | not_reproduced | Only 2 of 6 values are within tolerance. Active vs Passive 2 gives P = 4.8e-3, not < 0.001. All proportions do exceed the shuffled control (cell 15). |
| fig3d-theta-slopes-steeper-active | partially_reproduced | Signed slopes: the Active comparisons give P = 1.4e-17 and 3.6e-12, but Passive 1 vs Passive 2 gives P = 0.019 where the paper reports > 0.05 (cell 17). |
| fig3e-joint-score-slope-theta | reproduced | Under all three grid sizes the summed z is highest in Active (303.8 against 39.7 and 123.4). Region proportion 8.82% against 0.25% and 2.99%, P ≤ 3.7e-46. This rests on the claims file's own region bounds (cell 20). |
| fig3f-quadrant-scores | reproduced | Kruskal-Wallis P = 2.7e-47. Active exceeds both passive conditions at P ≤ 5.3e-23; Passive 2 exceeds Passive 1 at P = 1.3e-3 (cell 22). |
| fig3g-theta-self-consistency | blocked (too_large, not supported) | Not run. The 219 h estimate assumes a pure-Python loop over every pair with 1000 surrogates (problem 4). |
| figs7-control-cell-count | blocked (too_large, not supported) | Not run. The notebook's own timing contradicts too_large (problem 4). |
| figs8-control-firing-rate | blocked (too_large, not supported) | As figs7. |
| figs9-control-decoding-quality | partially_reproduced | Slopes and quadrant scores hold (KS P = 7.5e-11 and 6.3e-10; Passive 1 vs Passive 2 P = 0.084). The normalized scores still differ (Kruskal-Wallis P = 9.1e-15), and the errors (0.41 to 0.54 m) are far from 0.80 m (cell 24). |
| figs10-control-lap-variability | blocked (too_large, not supported) | As figs7. |
| figs11-sleep-sessions-similar | not_reproduced | All ANOVAs give P > 0.05. But one KS test of event-to-ripple timing is < 0.05 under each threshold reading: sleep after Passive 1 vs after Active P = 0.011 (SWS threshold); after Passive 1 vs after Passive 2 P = 0.025 (whole-session threshold) (cell 33). |
| fig4b-replay-scores-vs-baseline | partially_reproduced | After Active: median 0.274, P = 6e-223. After Passive 2: median −0.055, below 0. After Passive 1: median 0.028, P = 8e-20, above 0 where the paper finds no improvement (cell 30). |
| fig4c-replay-slopes-steeper-active | not_reproduced | Best Kruskal-Wallis P = 3.9e-5 (significant events). Active vs Passive 2 shows no difference in absolute slope (KS P = 0.13 to 0.19). The passive pair differs (P = 5e-4) (cell 33). |
| fig4d-joint-score-slope-replay | reproduced | Summed z is largest after Active for every grid; region proportion 11.1% against 0.6% and 3.3%, P ≤ 1e-56. This rests on the claims file's own region bounds (cell 35). |
| fig4e-replay-proportion-vs-baseline | not_reproduced | After Passive 1: not different from baseline (P = 0.27). After Active: higher (P = 4.4e-7). After Passive 2: lower than baseline (12.66% against 14.17%, P = 0.021) where the claim needs higher at P < 0.01 (cell 38). |
| fig4f-forward-replay-after-active | reproduced (recomputed) | Computed from the printed counts, reading (a): after Active 514 forward against 397 reverse, exact binomial P = 1.2e-4. After Passive 1, 389 against 356 (P = 0.24); after Passive 2, 312 against 334 (P = 0.41). The notebook's own test gives P = 5e-3 because of problem 2 (cell 41). |
| fig4g-theta-replay-correlation-active | blocked (too_large, not supported) | As fig3g. |
| figs12-ripple-restricted | not_reproduced | None of the four sub-analyses holds under either ripple reading. For example, the Kruskal-Wallis of absolute slopes is P = 4.4e-3 against the legend's 1e-27, and after Passive 2 is not above baseline (cell 43). |

### B. Problems

1. **[affects a conclusion]** Travel/sleep notebook cell 27, field entry. The code sets the entry bin as `sh = np.flatnonzero(~fld)[-1] + 1`. For any field that does not touch bin 0 or 249, this returns 0, so the "in-field" spikes are those in the first `size` bins of the track. On a synthetic field at bins 100–120, the selected bins were 0–20, with no overlap. This invalidates the precession slopes, the significant-precession proportions, fig2f, figs4de and the precession part of figs4b.
2. **[affects a conclusion]** Decoding notebook `fig4f`. The forward proportion is `fw/n`, where `n` includes zero-slope events, and it is tested against 0.5. That is not the criterion's forward-against-reverse comparison. Excluding the zero-slope events gives P = 1.2e-4 after Active, and the claim reproduces.
3. **[affects a conclusion]** The decoding and replay claims ran only one of several readings that the claims file lists for details the paper leaves open: field reading a, theta channel reading a, and SWS-normalized candidate-event threshold. Field reading b and the whole-session threshold (run only for figs11) were never decoded. Several outcomes are near their bounds (fig3c, fig4b, fig4e).
4. **[affects a conclusion]** Decoding notebook cell 0 and cell 45, the blocked claims.
   - figs7, figs8, figs10: cell 5 decoded all 21,579 cycles with 200 shuffles in 286 s. figs7 needs at most 30 × 300 × 2 × 5 = 90,000 cycles, roughly 20 minutes. figs8 and figs10 are each about one more decoding pass.
   - fig3g, fig4g: the 219 h estimate times an unvectorized Python bias matrix with 1000 surrogates over every pair, before the ≥3-common-neuron filter. A vectorized version, or a random sample of pairs, would estimate the proportions.
   - The archive listing (hc-18/live/data, five tar.gz files plus code.zip) shows all five use only spikes, positions and LFP, which are present and already loaded.
5. **[affects a conclusion]** `prepare` / `fields` (reading a). Every pyramidal cell with any firing becomes a place cell: per-rat counts are almost identical across conditions, and totals are 2.2× the paper's in Passive 1. Median peak-field size is 120–235 cm on a 6 m track, and cells have about 5 fields each. This drives figs2b and fig1c, makes figs2c trivial, weakens the remapping bootstrap (null mean ≈ observed), and gives every decoder about 200 weakly spatial cells.
6. **[affects a conclusion]** Cell 22, `mt_psd`. The 2-s windows give 0.5 Hz resolution, so 4 of 5 rats have the same mode in every condition. The theta-frequency absence is near-guaranteed and does not test P > 0.90. The window length is the author's choice and is not stated as an assumption.
7. **[affects a conclusion]** fig2cd and figs4b. The claims file's criterion says "a multitaper spectrum" of the phase-converted spike train. The paper's Methods say "spectrograms computed on the resulting spike trains" (Theta burst frequency). This is a misreading in the claims file, which I report without correcting. The whole-session spectrum gives modes at 1.000 ± 0.001, so the "> 1 cycle⁻¹" classification is close to a coin flip. On a synthetic precessing train, the helper did recover 1.10, so the function itself works.
8. **[affects a conclusion]** Rat 272 has negative per-rat reconstruction slopes and quadrant scores in all three conditions (cells 10 and 22) and reversed asymmetry ordering (cell 25). That pattern fits an inverted theta reference, a channel below the pyramidal layer chosen by `reduce_lfp` for largest theta power. It is never checked, and it feeds into all the pooled theta-sequence results.
9. **[affects a conclusion]** Remapping (cells 17–20). Eight readings were run, and fig1d, fig1e and figs2d each pass only under b/both/linear. The partial outcomes rest on a single reading out of eight.
10. **[affects a conclusion]** Decoding notebook cell 24 (figs9). The decoding error is measured in-sample, with the decoder trained on the same travel. The pooled error (0.41–0.54 m) is half the paper's 0.80 m. Whether the paper cross-validated is not stated, so the tolerance check is not comparable.
11. **[does not affect a conclusion]** Units are inconsistent. `linearize` measures a perimeter of 656–706 cm; field sizes and slopes use 2.4 cm per bin (6 m / 250), but the kernel uses L/250. A pixel-scale or aspect check is also missing: the y extent is 186 cm on a 130 cm-wide track.
12. **[does not affect a conclusion]** `vtest` is one-sided, while the paper says two-tailed throughout. Doubling the P values changes no outcome.
13. **[does not affect a conclusion]** The 200 shuffles in place of 5000 are disclosed. They resolve p ≤ 0.05, but z-scores and z-proportions are noisier.
14. **[does not affect a conclusion]** In cell 24, the per-window theta-power reading uses OLS with windows treated as independent, which is pseudo-replication.
15. **[does not affect a conclusion]** `classify_units`: the "methods" and "code" readings disagree for rat 292 (85 against 19 pyramidal). Waveforms are averaged over a group's channels and taken from only the first 80 MB of each .spk file.
16. **Checked, not a problem:** the L-ratio denominator (all spikes on the group) matches the paper's definition ("ns is the total number of spikes recorded on the tetrode"). The trajectory score (line recovered as D = 14 against a true 15), quadrant score sign, circular-linear regression, Rayleigh test and `fields` wrap-around all behaved correctly on synthetic inputs.

### C. What I could not check, and which outputs would have let me

- The paper's own scripts in code.zip (DiscriminateUnits.m, BatchPlaceFields.m, GetEventsManip1.m, BatchCandidateEvents.m, the Sequence/Replay reconstruction scripts). I did not download dataset files, so the notebook's statements about them are unverified. Printing the relevant lines would settle this.
- Whether the theta channel is in the pyramidal layer, especially for rat 272. Wanted: per-rat preferred theta phase of pyramidal spikes, and a cycle-averaged LFP.
- Whether the place-field definition matches the paper. Wanted: per-condition histograms of field size and fields per cell, plus spatial information per place cell.
- A precession rerun with the field-entry bug fixed. Wanted: the fraction of a cell's spikes that fall inside its peak field.
- The burst-frequency analysis on spectrograms, and on in-field spikes only.
- Decoding and replay under field reading b and the whole-session threshold.
- Measured timings of one figs7 subset, and of a vectorized pairwise-bias run on a sample of pairs.
- Cross-validated (leave-one-lap-out) decoding error for figs9.
