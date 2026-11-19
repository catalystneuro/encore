**Verifier report, round 1: Asari & Zador (2009), CRCNS ac-1**

The claims file has 21 claims. Every one is either tested in `reproduce_asari_2009.ipynb` / `strf_wehr.ipynb` or treated as blocked. Below, "cell N" means the main notebook unless marked STRF.

### A. Outcomes

| claim | my outcome | reason |
|---|---|---|
| methods-recording-counts | partially_reproduced | Cell 7 matches 39 natural-sound cells, 305 natural probes (silence counted), and MGB 93 probes in 14 cells. It does not match on 133 vs 123 qualifying cells, DMR 15 vs 6 cells, MHT 26 vs 39 cells, or 303 probes with silence not counted. The voltage-clamp counts (14 cells, 29 probes) cannot be tested because those data are not in the archive. |
| a1-mgb-firing-rates | partially_reproduced | Cell 9: no reading puts all four means within 10% (0 of 16). The partial rule (A1 under 1 Hz, MGB evoked over 5 Hz) holds in 12 of 16. Best case is A1 0.33 / 0.46 Hz and MGB 0.82 / 7.1 Hz. |
| fig2-example-reliability | reproduced | Cell 11: the population mean is 0.310 ± 0.092 over cells (pairs reading), against 0.31 ± 0.09. The matched example cell gives 0.611 and probe 4 gives 0.737, against 0.61 and 0.74. |
| fig2-example-long-context | reproduced | Cell 13, matched probe 4: significant periods before 2 s, none between 1.6 and 3.97 s, and periods again from 3.97 to 4.60 s. All three parts of the criterion hold. |
| fig3a-proportion-significant | partially_reproduced | Cell 15, silence counted: 187 of 305 probes (0.613) is within tolerance of 204 / 0.669. The late fraction is 0.276 or 0.295, outside 0.237 ± 0.024. With silence not counted the count is 165, which fails. |
| fig3a-significance-decay | partially_reproduced | Cell 20: no reading has every value within tolerance. With sizes held at zero or above and silence counted, two exponentials are chosen with a slow constant of 1.11–1.47 s, which meets the partial rule (4 of 16 readings). The noise floor is 0.0028 under the running reading, matching the paper's 2.8 × 10⁻³. |
| fig3b-fractional-power-decay | not_reproduced | Cell 22: 0 of 16 readings within tolerance. Under the code's per-trial centering, α ≈ 0.46 is within tolerance but τ is 1.5–2.0 s against 1.04. The author's per-probe centering gives τ of 0.30–0.59 s. |
| timescale-longer-than-membrane | reproduced | Cell 24: the 1/e lags are 71 ms (noise) and 77 ms (spontaneous); the 0.1 lags are 115 and 121 ms. All are under 150 ms, and 71 ms is under a third of 1.04 s. |
| fig4-predictability-upper-bound | partially_reproduced | Cell 26: 1 + α ≈ 0.50 is within tolerance in the trial-centred unsmoothed readings, so "about half" holds. τ is never within tolerance under the paper's centering (1.6–2.8 s). The only 2 of 32 readings that pass use the author's own per-probe centering (problem 2). |
| fig4-strf-performance-low | not_reproduced | STRF cell 6: validation performance stays at or below 0.143, but the fixed one-sided Wilcoxon test finds a significant STRF improvement from 180 to 4052 ms (p = 0.003). It stays significant under both variant readings (p = 0.004 and 0.015). The run used 16 cells, not 20. |
| fig5-example-conductances | blocked (data_missing) | I checked the archive: its zips hold 346 result .mat files, all of which the notebook read, all in mV. Summary.mat lists no voltage-clamp experiment. Nothing can be tested. |
| fig6-conductance-decay | blocked (data_missing) | Same as fig5. |
| fig8a-proportion-by-property | not_reproduced | Cell 28: all five counts are outside tolerance (56, 62, 27, 16, 88 against 77, 73, 62, 47, 59). The order AM > FM > higher-order fails (0.640 < 0.642). The AM and FM probe sets are far smaller than the paper's (39 vs 96, 25 vs 82). |
| fig8b-decay-by-property | partially_reproduced | Cell 30: no τ is within tolerance. The partial rule holds in every reading: amplitude and frequency 0.58–1.36 s; AM, FM and higher-order 0.03–0.10 s. This rests on the reduced AM/FM probe sets (problem 3). |
| fig8a-significance-fits | not_reproduced | Cell 32: 0 of 5 properties within tolerance in every reading, and the sizes are out of the printed order. |
| fig8c-relative-effects | not_reproduced | Cell 34, probe resampling: the amplitude and frequency intervals (0.59–0.78 and 0.51–0.66) exclude 1, and the point estimates (0.67, 0.58) are below 1, so neither the full nor the partial pattern holds. The trial-resampling reading that "holds" is biased (problem 1). |
| fig8-natural-synthetic-probes-alike | reproduced (rests on the claims file's Fisher test) | Cell 36: no difference after Bonferroni in the 4 properties testable (all p ≥ 0.29). FM could not be tested because there are 0 synthetic FM probes. |
| fig9-mgb-fast-decay | reproduced | Cell 38: τ = 0.055–0.067 s (under 0.1 s), and the plateau after 0.5 s (1.27) equals κ (1.27). Sizes are 5.2–15.8 against 15, and κ is 1.27 against 2.0 (reported only). |
| fig9-example-first-bin | reproduced | Cell 40: 4 of 12 probes with the Figure 9A design meet the factor-of-two rule, all from cell 20071010-ha2-003; 35 of 93 overall. |
| fig7-example-frequency-context | blocked (data_missing) | Cell 42: no DMR-frequency file found has 0.625–2.5 / 2.5–10 / 10–40 kHz contexts with a natural probe. The weaker check finds 2 of 5 natural probes after 2-octave DMR contexts with significance lasting past 3.6 s (4.58 s and 3.82 s). The search did not cover every file (problem 7). |

I found no place where the claims file misreads the paper. Its "DMR" for Figure 7 is right: the Methods say "Figure 7A … DMR frequency variants".

### B. Problems

1. **[affects a conclusion] Cell 34, `boot_trials`:** it resamples trials with replacement, then applies Eq. 17. Eq. 17's unbiasedness assumes independent trials, and duplicated trials leak noise power into it. I tested this on synthetic data: Eq. 17 went from 4.97 to 6.76 and Eq. 19 from 0.98 to 2.77 (true 0.98). This is why 0 of 5 trial-resampling intervals contain their own point estimate. The "pattern holds: True" from that reading is an artefact and cannot support fig8c.
2. **[affects a conclusion] Cells 22 and 26, `power_from_x1(center="probe")`:** this centering is the author's stand-in, not a reading the claims file or the paper gives. The Methods centre each trace as r(t) − ⟨r(t)⟩ₜ, which is the per-trial centering the shipped `CxtDep.m` uses. The only fig4 readings within tolerance (silence not counted, running probes, smoothed) depend on this centering. Under the paper's centering, 0 of 16 fig4 readings and 0 of 8 fig3b readings pass.
3. **[affects a conclusion] Synthetic property selection, `asari.property_groups` / `property_tests`, cells 7 and 28:**
   - AM has 39 probes against the paper's 96, and FM has 25 against 82. MHT probes for AM are 14 against 71; for FM, 0 against 57.
   - DMR has 15 cells against 6.
   - The criterion asks that the probes making the difference be reported; this was not done, and no per-file classification is printed.
   - One possible cause: the parser for note groups drops any group whose name lacks "amplitude-modulation", "frequency-modulation", "amplitude" or "frequency" (e.g. a note reading "AM variants").
   - This affects fig8a, fig8b, fig8a-significance-fits, fig8c, and the FM row of fig8-natural-synthetic.
4. **[affects a conclusion] `property_tests`, colored-noise branch:** it pools every natural fragment of a file into one context and every colored noise into another. That is the author's choice; the paper pairs each natural sound with its own colored noise. No alternative was run (each pair, or each fragment as its own context). Higher-order comes out at 88 of 137 (64%) against 59 of 137 (43%), and this decides the AM > FM > higher-order order.
5. **[affects a conclusion] Cell 44 (figs1):** the stimulus-related power first drops below 10% at 0.688 s, but it averages 1.41 mV² over 2.0–2.5 s. That is 31% of the onset value (4.59). The onset reference, the mean of the first 10 ms, is also far below the curve's maximum (12.75). "Faded within about 1 s" holds only under a first-crossing reading; there is no check that the power stays down. I kept the outcome as reproduced because it meets the criterion's wording, but it is fragile.
6. **[affects a conclusion] STRF cells 3 and 6, `wehr.fit_cell` / `lowess_fit`:**
   - 16 cells are used, not 20, and 6 of them have only 2 trials per sound.
   - The window gain is larger in the 2003 two-trial cells (0.121 → 0.173) than in the 2002 cells (0.098 → 0.124). No per-set test is shown.
   - LN validation falls below STRF on average (−0.068), with SD up to 0.49, which suggests an unstable lowess step. This is not investigated, and it contradicts the paper's "LN slightly better".
7. **[affects a conclusion] Cell 42 / `run_pass` (fig7 blocked):** the search only covers experiment-2 records with kind "dmr" and property "frequency". Experiment 3 (27 files, 12 cells, including files that combine DMR and natural-sound triggers) is never analysed for context–probe structure, so "not in the data set" is not fully established.
8. **[does not affect a conclusion] Cell 20:** fig3a-significance-decay's partial outcome rests on the stated assumption that sizes are zero or above. Fits with free sizes pick a negative fast term that fits the response-latency rise. The assumption is reasonable.
9. **[does not affect a conclusion] `asari._runs`:** it needs 51 consecutive points (5.1 ms), not 50; I confirmed this on synthetic masks. The Kruskal-Wallis statistic and `running_02t` match reference values in my tests.
10. **[does not affect a conclusion] Cell 26:** four fits ("all probes", smoothed, 6 s range) hit the τ = 100 s bound and are reported without a flag.
11. **[does not affect a conclusion] `wehr.spectrogram`:** band centres run 0.4–16 kHz, not up to 22 kHz. The comment promises a shift to align frames to [jΔt, (j+1)Δt), but none is applied, so each frame reaches about 6 ms into the future.
12. **[does not affect a conclusion] Cell 32:** the noise floor is averaged over 0–4 s here but over 0–6.07 s in cell 15. The AM, FM and higher-order floors (0.0048–0.0071) are 2–3 times the legend's chance levels (0.0021–0.0036), which fits the pooled two-context tests.

### C. What I could not check, and the output that would settle it

- **Cause of the AM/FM/DMR shortfall:** a per-file table for experiment 2 (stimulus descriptions, the notes lines, which property tests were chosen, probe counts).
- **Whether experiment 3 holds context–probe sequences or the Fig. 7 cell:** the number of sequences and the trigger types for each experiment-3 file.
- **Whether `asari.py` follows `CxtDep.m`** (trial-mean removal, ordinal ranks, pooling of contexts): I did not download the shipped MATLAB code. Quoting the relevant lines in the notebook would settle it.
- **Whether the STRF window gain is driven by the 2-trial cells:** the Wilcoxon test run separately on the 2002 and 2003 cell sets, plus per-cell LN fits.
- **Whether the figs1 power really fades:** the Eq. 17 silence curve printed in 100-ms bins, and the time of its peak.
- **The size of the fig8c bootstrap bias in this data:** the trial-resampling intervals computed with the bias-corrected statistic, or set beside the point estimates.
- **Whether ordinal ranking matters:** the share of tied values per time point in the Kruskal-Wallis test.
