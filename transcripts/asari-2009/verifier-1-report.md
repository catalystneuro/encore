**Verifier report, round 1: Asari & Zador 2009 (doi:10.1152/jn.00577.2009) on CRCNS ac-1**

The claims file has 21 claims. My outcomes: 8 reproduced, 6 partially reproduced, 3 not reproduced, 4 blocked. Of the 4 blocked, one (fig4-strf) has its data in the archive but was not run, and one (fig7) is likely testable.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| methods-recording-counts | partially_reproduced | Cell 11 matches 305 probes in 39 cells under both silence readings, and 93 MGB probes in 14 cells. The A1 total is 132 cells against 123. The two voltage-clamp counts are blocked because the data set has no voltage-clamp recordings. |
| a1-mgb-firing-rates | partially_reproduced | Cell 13: no reading puts all four means within 10%. A1 means are below 1 Hz (0.39 and 0.44 Hz at -20 mV). MGB evoked is above 5 Hz with the mad:5 (13.6) and mad:8 (10.4) detectors, but only 4.99 Hz with the main getspikes detector. |
| fig2-example-reliability | reproduced | Cell 15, over cells with the pairwise reading: 0.310 ± 0.092 against 0.31 ± 0.09. The example cell 20051222-ha1-001 gives 0.611 ± 0.081 and its probe 4 gives 0.737 ± 0.075. |
| fig2-example-long-context | reproduced | Cell 17, matched probe 20051222-ha1-001 probe 4: significant before 2 s, nothing between 2.2 and 3.6 s, and a period starting at 3.97 s. |
| fig3a-proportion-significant | not_reproduced | Cell 19: 183 of 305 (0.600) against 204 ± 20.4 (0.669 ± 0.067). This misses the bound by 0.6 probe. The late fraction (0.237, peak at 4.718 s) and the noise floor (0.0028) match. The criterion's partial outcome needs the count within tolerance, so it does not apply. |
| fig3a-significance-decay | partially_reproduced | Cell 21: unbounded fits give a negative fast term. With sizes kept non-negative (the notebook's reading), two exponentials are chosen with tau2 between 0.90 and 0.97 s. a1, tau1 (0.25 to 0.26 s) and a2 fall outside tolerance. |
| fig3b-fractional-power-decay | reproduced | Cell 23, silence counted: a1 is 0.487 to 0.495 and tau1 is 1.01 to 1.05 s under all four readings. With silence left out, tau1 is 0.55 s. |
| timescale-longer-than-membrane | reproduced | Cell 25: the 1/e lag is 71 ms for noise and 77 or 75 ms for spontaneous activity. The 0.1 lags are 115 to 121 ms. All are under 150 ms and under 347 ms. |
| fig4-predictability-upper-bound | not_reproduced | Cell 27: 1 + a1 is within tolerance (0.45 to 0.50), but tau1 is 1.26 to 2.33 s with the smoothed denominator, and 1.20 or 0.70 s unsmoothed. Two fits stop at the bound of 100 s. See problem 3 for a reading the claims file missed. |
| fig4-strf-performance-low | blocked (other) | The analysis was not run ("see the record"). The archive has the data: 25 folders under `wehr/Results` plus `wehr/Tools/STRFanalysis.m`. It is testable. |
| fig5-example-conductances | blocked (data_missing) | All 172 analysed files are whole-cell or cell-attached (cells 6 and 31). The archive's file list holds only these Asari folders, the 15 "unpublished" files and Wehr's 2002–2003 data. |
| fig6-conductance-decay | blocked (data_missing) | Same as fig5. |
| fig8a-proportion-by-property | partially_reproduced | Cell 33, probe reading (Table 1 counts probes): 58/95, 62/110, 25/39, 16/25 and 64/131. Most counts are outside tolerance, but the order holds: amplitude > frequency, and AM 0.641 > FM 0.640 > higher-order 0.489. The AM/FM order rests on a 0.001 margin. |
| fig8b-decay-by-property | partially_reproduced | Cell 36: only AM (0.109 to 0.118 s) is within tolerance. Amplitude (1.35 s) and frequency (0.78 to 0.84 s) are above 0.4 s, and AM, FM and higher-order are below 0.3 s, under every reading. |
| fig8a-significance-fits | not_reproduced | Cell 38: no property is within tolerance under any reading. Amplitude a1 (0.12) is below frequency (0.15), so the size order also fails. |
| fig8c-relative-effects | partially_reproduced | Cell 40, probe population: the amplitude and frequency intervals include 1 and the AM and FM intervals lie below. The higher-order interval [0.637, 0.826] overlaps the frequency lower bound of 0.792. The point estimates are ordered as claimed. All interval conditions pass only under the notebook's "entry" population, which is not the criterion's (problem 1). |
| fig8-natural-synthetic-probes-alike | reproduced | Cell 42: Bonferroni p is 0.80 to 1 for all four testable properties. FM has no synthetic probes, so it was not tested (problem 1). |
| fig9-mgb-fast-decay | reproduced | Cell 44: tau1 is 0.060 to 0.090 s under every reading. The plateau matches the fitted constant, and the paper's 2.0 under mad:5. |
| fig9-example-first-bin | reproduced | Cell 46: all 4 probes of 20071010-ha2-003 have a first-bin SD at least twice every later bin. 38 of 93 probes pass overall. |
| fig7-example-frequency-context | blocked (metadata_insufficient as run); likely testable | The search in cell 48 needs three separate band pairs. Five DMR recordings store `ff = (625, 2500, 10000, 40000)`, which is exactly the Figure 7 band edges written as one vector (problem 2). |
| figs1-silence-probe | reproduced | Cell 50: 22 silence probes in 19 cells have a significant period starting within 0.5 s. Eq. 17 power falls below 10% of its onset value at 0.541 s. |

### B. Problems

1. [affects a conclusion] The property populations for Figure 8 do not match Table 1 (`property_classes`, cells 33–34).
   - Table 1 rows are probe types. Against those rows, the notebook finds MHT probes with 0, 0, 14 and 0 for amplitude, frequency, AM and FM, against the paper's 25, 25, 71 and 57. It finds natural probes with 45 and 46 for amplitude and frequency, against 23 and 25.
   - The amplitude and frequency totals (95, 110) match only by coincidence.
   - Cell 34 then picks a reading per property so that the denominators match: "entry" for AM and FM, "probe" for the others. Table 1 counts probes, so the "entry" totals of 96 and 82 (82 natural entries + 14 MHT, and 82 natural + 0) are not the paper's populations.
   - This affects fig8a, fig8b, fig8a-significance-fits, fig8c and the FM part of fig8-natural-synthetic. The family counts in cell 11 (DMR 15 against 6, MHT 26 against 39) point the same way.
2. [affects a conclusion] The fig7 block rests on an exact match of band tuples (cell 48). The edge vector (625, 2500, 10000, 40000) appears in 5 DMR recordings, the same 5 cells as the DMR frequency row (20 probes, 5 cells, which matches Table 1). The fragment descriptions and the other parameters of these recordings were not printed, so the block is not established.
3. [affects a conclusion; claims-file issue] For fig4-predictability, the Figure 4 legend gives the same fit as Figure 3B (0.49 and 1.04 s). Under the paper's Eq. 19 that is consistent with plotting 1 − Q(t). The claims file only offers Eq. 43 with a smoothed or unsmoothed denominator. Cell 23's Q fit gives 1 + α = 0.512 and τ = 1.040, which is within tolerance. Under the criterion as written the claim is not reproduced; the claims file should decide whether 1 − Q is an allowed reading.
4. [affects a conclusion] fig4-strf-performance-low was not run (cells 28–29) although the Wehr data and the authors' `STRFanalysis.m` are in the archive.
5. [does not affect a conclusion] The cell 42 Fisher tests for fig8c and fig8-natural-synthetic follow the paper's "1000 samples" literally. That is about 10 times the number of probes, so the intervals are roughly 3 times narrower than an n-sized resample would give. The "entry" population also counts one probe's response several times. The trial-resampling reading of the criterion was not run.
6. [does not affect a conclusion, as far as I can tell] `kw_significance` ranks with a stable `argsort`, so tied values get ranks in context order, with no tie correction. On synthetic null data quantized at 1 SD, this raised pointwise P < 0.01 from 0.005 to 0.023, and runs from a 0.0003 floor to 0.0034. At 0.5 SD or finer there was no visible effect. The int16 `scale` is never printed, and I could not read CxtDep.m to see whether it does the same.
7. [does not affect a conclusion] fig3a-significance-decay: the partial outcome rests on the notebook's non-negative bound on the sizes. The paper gives no bounds, and the bound is reasonable for a decay.
8. [does not affect a conclusion] fig9-mgb-fast-decay: comparing the plateau with the fitted κ is nearly circular, since κ is fitted to that same plateau. The claim passes on τ alone.
9. [does not affect a conclusion]
   - `running_mean_0_2t` becomes a cumulative mean for t greater than half the curve length (about 3 s). This is stated as an assumption.
   - `psth_sd` keeps the histc degenerate last bin, which adds a 0 to each probe under the "running" reading.
   - One synthetic file has a 308-ms trigger mismatch and was cut with its stored durations.
10. [does not affect a conclusion] methods-recording-counts: the criterion asks for the probes or cells behind any count that differs. The notebook does not list the cells that make 132 against 123.
11. [does not affect a conclusion] The voltage-clamp check (cell 31) covers only the 172 analysed files. The 15 experiment-3 files ("unpublished, various acoustic stimuli") and the tuning-curve files were not checked for recording type.

Helper functions tested on synthetic inputs gave correct results: `fit_exponentials` and `choose_n_exp` recover known parameters, and `running_mean_0_2t`, `psth_sd` and `frac_power` behave as expected (Eqs. 17 and 18 match the paper). Chance level: the Figure 3A noise floor is 0.0028 under the "running" reading, the same as the paper. The Figure 8A floors are 0.0033, 0.0022, 0.0021, 0.0020 and 0.0025, against the legend's 2.8, 2.3, 2.3, 2.1 and 3.6 × 10⁻³.

### C. What I could not check, and the output that would have let me

- CxtDep.m and GetSpikes.m, the source of the tie handling, trial centering and power estimators: a cell printing the relevant lines, and `resp.scale` for each file.
- How MHT probes are classified: a table per MHT recording of each fragment's `fragment_kind`, parameters and description, plus Table 1 rebuilt by probe type with cell counts.
- fig7: per-fragment `ff` and descriptions for the 5 DMR recordings that store (625, 2500, 10000, 40000).
- The voltage-clamp block: `param.recording.type` for the experiment-3 and tuning-curve files.
- fig4-strf: the attempt record says why it was not run, and I do not have it.
- The cells behind 132 against 123: a list of the A1 cells counted, by family.
- The figures, which I did not view (only the printed ranges).
