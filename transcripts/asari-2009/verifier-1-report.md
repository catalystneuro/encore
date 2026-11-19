**Verifier report, round 1: Asari & Zador (2009) on CRCNS ac-1. The claims file has 21 claims.**

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| methods-recording-counts | partially_reproduced | Cell 10 matches 305 natural probes in 39 cells and 93 MGB probes in 14 cells, under both silence readings. It finds 133 A1 cells meeting the criterion, not 123, and the synthetic counts don't match (MHT 26 cells vs 39, DMR 15 vs 6; Table 1 rows differ, see B1–B2). The voltage-clamp counts can't be tested because those recordings aren't in the data set. |
| a1-mgb-firing-rates | partially_reproduced | Cell 12: no reading puts all four means within tolerance, because MGB evoked is at most 7.07 Hz against 11.4 ± 1.14. The A1 15-mV reading (0.481 / 0.547 Hz) and the half-threshold MGB reading (spontaneous 0.768, evoked 7.07 > 5 Hz) meet the partial rule. |
| fig2-example-reliability | reproduced | Cell 14: mean over pairs of trials, averaged over cells, is 0.310 ± 0.092 (paper 0.31 ± 0.09). The matched cell gives 0.611 and its probe 0.737. |
| fig2-example-long-context | reproduced | Cell 16, matched probe (20051222-ha1-001-002, probe 4, contexts [0,2,3], 6 repeats): significant periods up to 1.60 s, none in 2.2–3.6 s, then periods from 3.97 s. |
| fig3a-proportion-significant | reproduced | Cell 18, silence counted, all-probes reading: 186 of 305 (within 204 ± 20.4), 0.610 (within 0.669 ± 0.067), late fraction 0.255 (within 0.237 ± 0.024). Noise floor 0.00281 matches the paper's chance level of 2.8×10⁻³. This holds narrowly; the probes-running reading gives 0.270, which is out. |
| fig3a-significance-decay | partially_reproduced | Cell 20: no reading has all four values within tolerance. Two exponentials with the slow constant between 0.5 and 2 s are selected in many readings (e.g. 0.159/0.26 s and 0.072/1.05 s). |
| fig3b-fractional-power-decay | not_reproduced | Cell 22: α is 0.45–0.47 but τ is 1.29–1.78 s in every reading (tolerance 1.04 ± 0.10). The criterion has no partial clause. |
| timescale-longer-than-membrane | reproduced | Cell 24: lag below 1/e is 71 ms for noise and 77/75 ms for spontaneous activity; lag below 0.1 is 115–121 ms. All are under 150 ms and under 347 ms. |
| fig4-predictability-upper-bound | not_reproduced | Cell 26: 1+α is within tolerance in some readings (0.50, 0.53), but τ is never within 1.04 ± 0.10 (1.46–2.8 s; two fits stop at the 100-s bound). |
| fig4-strf-performance-low | blocked (other: not run) | Blocked only "for time". The archive has Wehr's data: `wehr/Results` holds 26 cell folders and 1626 files, plus Tools and Stimuli. The claim is testable. |
| fig5-example-conductances | blocked (data_missing) | Confirmed in the archive: the data set's Methods.txt describes current clamp only, with a K-gluconate internal solution (no QX-314 or BAPTA). No Summary.mat experiment is voltage clamp, and all 151 files read are in mV. |
| fig6-conductance-decay | blocked (data_missing) | Same evidence as fig5. |
| fig8a-proportion-by-property | partially_reproduced | Cell 28: only frequency (70/120) is within tolerance, and its denominator is wrong. The proportion order (amplitude > frequency; AM > FM > higher-order) holds under both readings. The probe selection doesn't follow Table 1 (B2). |
| fig8b-decay-by-property | partially_reproduced | Cell 30: only AM's τ (0.112 s) is within tolerance. The partial pattern holds: amplitude 1.35 s and frequency 0.84 s are above 0.4 s; AM 0.11, FM 0.28 and higher-order 0.23 s are below 0.3 s. |
| fig8a-significance-fits | not_reproduced | Cell 32: no property has both values within tolerance. The sizes aren't in the paper's order (amplitude 0.121 < frequency 0.150; FM 0.013 < higher-order 0.035), so the partial rule fails too. |
| fig8c-relative-effects | partially_reproduced | Cell 34: the point estimates follow the pattern, but the amplitude (0.58–0.78) and frequency (0.55–0.73) intervals don't reach 1. Two readings the criterion calls for weren't run, and one of them could change the outcome (B3). |
| fig8-natural-synthetic-probes-alike | blocked (other: test run on mislabelled probes) | Cell 36 finds no difference, but its natural/synthetic split contradicts Table 1. FM is "only natural (82)" where the paper has 57 MHT probes, and AM has 14 synthetic where the paper has 71 (B1). Mixing the labels pushes the test toward finding no difference. Testable once the labels are fixed. |
| fig9-mgb-fast-decay | partially_reproduced | Cell 38: τ is 55–61 ms, below 0.1 s, so the τ condition passes. The level after 0.5 s is 1.27–1.38 spike/s, more than 25% below the paper's κ of 2.0, so the plateau condition fails. |
| fig9-example-first-bin | reproduced | Cell 40: 4 of the 12 probes with the Figure 9A design have a first-bin SD at least twice every later bin's (e.g. 31.4 against at most 7.2). Over all 93 probes the fraction is 35/93. |
| fig7-example-frequency-context | blocked (other: unsupported) | The notebook contains no search for the example cell. The data set has DMR frequency/bandwidth-variant files (cell 10: DMR in 15 cells, 20 DMR frequency tests), so a match may exist. |
| figs1-silence-probe | reproduced | Cell 42: 24 silence probes in 21 cells have a significant period starting within 0.5 s. Stimulus-related power first falls below 10% of its onset value at 0.72 s. |

### B. Problems

1. **[affects a conclusion]** `is_natural` and the Table 1 rows (cells 10 and 36). Natural-sound rows are AM 82 and FM 82 (paper 25 each); MHT rows are AM 14 and FM 0 (paper 71 and 57). Yet the totals are exactly the paper's 96 and 82. Separately, MHT 26 cells plus "natural variants" 14 cells is about the paper's 39 MHT cells. Most likely the MHT stimuli in the "naturalistic" files lack "Modulated Harmonic" in their description, so they are labelled natural. This invalidates the fig8-natural-synthetic-probes-alike test and the Table 1 rows in methods-recording-counts.
2. **[affects a conclusion]** Fig. 8 unit of analysis (cell 28; `synthetic_tests`). The main reading counts each (probe, class) pair as a test: higher-order 354 (paper 137), amplitude 104 (95), frequency 120 (110). Counting each probe once gives exactly 95, 110 and 137, so that is the reading the criterion's "columns of Table 1" points to. fig8b, fig8a-significance-fits and fig8c were run only on the per-class tests.
3. **[affects a conclusion]** fig8c (cell 34): the natural-sound denominator uses only the silence-counted reading, while the synthetic tests leave silence out. Estimated from cell 22's fits, the silence-not-counted area is about 0.45×1.29×(1−e^(−4/1.29)) ≈ 0.55, against 0.76 measured. That would scale the ratios by about 1.37: amplitude ≈ 0.92 (upper bound ≈ 1.07), frequency ≈ 0.87 (upper ≈ 0.99), higher-order ≈ 0.50, still below their lower bounds. This could move the claim to reproduced. The trial-resampling reading the criterion names was also not run.
4. **[affects a conclusion]** fig4-strf-performance-low is marked blocked for lack of time, which is not a blocking reason; the data are in the archive.
5. **[affects a conclusion]** fig7-example-frequency-context is declared blocked with no cell showing a search.
6. **[affects a conclusion]** fig9 (cell 38): the plateau test isn't printed. Read against the paper's κ, it fails. MGB spikes look under-detected (`extract_spikes` sets its threshold at two-thirds of the recording's largest filtered value; evoked rate 4.99 Hz against 11.4), which lowers κ and α. This also affects a1-mgb-firing-rates.
7. **[does not affect a conclusion]** methods-recording-counts: 133 cells against 123. The criterion asks for the probes that make the difference to be listed; they aren't.
8. **[does not affect a conclusion]** Cell 26: two fits stop at τ = 100 s. Every other reading also fails on τ.
9. **[does not affect a conclusion]** `kw_significance`: ties are broken by trial order (which follows context order), there's no tie correction, and the shuffles reuse the fixed ranks, so the noise floor doesn't capture any tie bias. On synthetic null data quantized at 1 SD, the pointwise false-positive rate rises from 0.0046 to 0.024. This copies the authors' `KWtest` in CxtDep.m (sort/sort ranks, `r(randperm(N),:)`), which I checked, so it is faithful to their method.
10. **[does not affect a conclusion]** `runs` keeps runs of 51 or more points, not 50. This matches CxtDep.m's `>= dt` on the index difference.
11. **[does not affect a conclusion]** fig2: the example cell is chosen by the very correlation values being tested, so those values match by construction. The population value decides the claim.
12. **[does not affect a conclusion]** A1 firing rates come from 133 cells, not the paper's 194. Of the three A1 thresholds tried, only 15 mV fits.
13. **[does not affect a conclusion]** figs1: the 10% threshold is crossed on a noisy curve (−0.58 mV² at 1.0 s), and the mean over 1.1–2.5 s is 13% of the onset value. The criterion is met literally.
14. **[does not affect a conclusion]** Cell 10 has dead code (`... if False else ...`) and an unused `typ()`.
15. **[does not affect a conclusion]** The results zips hold 161 cell folders; Summary.mat lists 145 A1 and 14 MGB cells. The notebook selects files only through Summary.mat and doesn't account for the difference.

I tested these helpers on synthetic inputs and they behave correctly: `kw_significance` matches `scipy.stats.kruskal` (largest difference 7×10⁻⁶); `frac_power`'s stimulus-related power is unbiased; `smooth_0_2t`, `fit_select` (recovers 0.175/0.21 s and 0.084/0.92 s) and `psth_sd` are correct. `FracPow` and `psth` match CxtDep.m.

### C. What I could not check, and which output would settle it

- **The MHT labelling (B1):** the stimulus descriptions and trigger type of each synthetic file, and the Table 1 row of each probe.
- **Whether ties matter in the real data (B9):** `response.scale` and the fraction of tied values per time point.
- **Fig. 8 with each probe counted once:** fig8b, fig8a-significance-fits and fig8c re-run on that selection.
- **fig8c:** the silence-not-counted natural denominator and the trial-resampling reading.
- **fig9:** the plateau result printed against κ = 2.0.
- **fig7:** the list of DMR frequency-variant files with natural-sound probes and their significant periods.
- **methods-recording-counts:** the 10 extra A1 cells and their files.
- **The 15 "other" files and 2 unlisted folders:** their recording type.
- **The detector details** `asari.py` attributes to the authors' code (`ExtractSpikes`, the cutting into context–probe pairs): I read only CxtDep.m's KWtest, FracPow, psth and pairing code, not GetSpikes.m in full.
