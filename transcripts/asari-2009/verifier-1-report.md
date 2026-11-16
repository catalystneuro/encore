**A. Outcomes**

The claims file has 21 claims. No attempt record was supplied, so I took the list of claims from `asari-2009.yaml`.

| Claim | My outcome | Reason |
|---|---|---|
| methods-recording-counts | partially_reproduced | Cell 13 matches the paper exactly for the natural-sound A1 data (39 cells, 305 probes) and for MGB (14 cells, 93 probes). The A1 cells meeting the rule come to 133, against 123 with tolerance 0. DMR has 15 cells against 6 and MHT 26 against 39. The voltage-clamp counts cannot be tested because those recordings are not in the archive. |
| a1-mgb-firing-rates | partially_reproduced (borderline) | Cell 15: A1 means are below 1 Hz under every detector. MGB evoked is 5.07 Hz on all files and 4.99 Hz on context files only, against 11.4 Hz. No reading gets all four means within 10%; the best is A1 dvdt/all, with spontaneous 0.474 (in) and evoked 0.695 (out). The partial rule's "MGB evoked > 5 Hz" holds in only one reading, by 0.07 Hz. |
| fig2-example-reliability | reproduced | Cell 17, pairs reading, over cells: 0.310 ± 0.092, against 0.31 ± 0.09. File 20051222-ha1-001-002: 0.611 ± 0.081 against 0.61 ± 0.07, and its best probe 0.737 against 0.74. |
| fig2-example-long-context | reproduced | Cell 19: candidate 20060105-ha1-001 probe 4 meets the rule strictly, with runs before 2 s, none from 2 to 4 s, and one at 4.00–4.06 s. 20051222-ha1-001 probe 4, the same cell as the reliability example, fails the strict rule only because of a run at 3.97–4.01 s. The match was found among 20 candidates, so it is a selected example. |
| fig3a-proportion-significant | reproduced | Cell 21, reading with_silence/all: 186 of 305 significant (204 ± 20.4), fraction 0.610 (0.669 ± 0.067), late fraction 0.252 (0.237 ± 0.024), cumulative peak at 4.78 s (paper 4.72 s). The noise floor is 2.2e-3 under the "all" reading and 2.8e-3 under "running"; the paper gives 2.8e-3. |
| fig3a-significance-decay | partially_reproduced | Cell 26: two exponentials are selected under the with_silence readings, and τ2 (0.97–1.08 s) is in tolerance under "all". α1 (0.149), τ1 (0.25 s) and α2 (0.079) are outside tolerance in every reading. |
| fig3b-fractional-power-decay | not_reproduced | Cell 28: α1 is 0.45–0.47 (in tolerance), but τ1 is 1.29–1.78 s against 1.04 ± 0.10 s in all 8 readings. |
| timescale-longer-than-membrane | reproduced | Cell 31: 1/e lags are 73 ms (noise), 78 ms and 77 ms (spontaneous), all under 150 ms and under 347 ms. |
| fig4-predictability-upper-bound | not_reproduced | Cell 33: no reading has τ1 within 1.04 ± 0.10 s (range 1.46–2.81 s, plus two fits stuck at the 100 s bound). 1 + α1 is within 0.51 ± 0.05 in several readings. |
| fig4-strf-performance-low | blocked (other: not attempted) | The notebook marks it blocked, gives no reason and has no cell for it. The archive does hold the data (problem 1), so the block is not justified. |
| fig5-example-conductances | blocked (data_missing) | Confirmed. Cells 4 and 9 find no current-unit files and no result files outside Summary.mat. `crcns-ac1.zip` `asari/Results` holds only a README, and Wehr's data are current clamp (`Methods.txt`). No part can be tested. |
| fig6-conductance-decay | blocked (data_missing) | Same evidence as fig5. No part can be tested. |
| fig7-example-frequency-context | blocked (other: search incomplete) | The notebook's "no recording with that design" is not established (problem 5). A partial test is possible on the 20 DMR frequency probes the notebook already formed. |
| fig8a-proportion-by-property | partially_reproduced (fragile) | Cell 37: every count is outside tolerance. Where the denominators match the paper: amplitude 56/95 against 77, higher-order 45/137 against 59. The order amplitude > frequency and AM > FM > higher-order holds, but the AM and FM probe sets are wrong (problem 2), so their part of the order is not a valid comparison. |
| fig8b-decay-by-property | partially_reproduced | Cell 41: τ1 is within tolerance for frequency (0.88), AM (0.100) and higher-order (0.186), but not for amplitude (1.40 against 0.66) or FM (0.113 against 0.15). The partial pattern holds (amplitude and frequency > 0.4 s; the others < 0.3 s). AM and FM rest on the wrong sets. |
| fig8a-significance-fits | not_reproduced | Cell 39: none of the five α1 values is in tolerance, and the size order fails (amplitude 0.124 < frequency 0.147). |
| fig8c-relative-effects | not_reproduced (as run) | Cell 43: the amplitude interval [0.61, 0.83] and frequency interval [0.57, 0.83] exclude 1. The without-silence reference reading was not run and could change the outcome (problem 3). |
| fig8-natural-synthetic-probes-alike | reproduced (weak) | Cell 45: all Bonferroni-corrected p are 1.0. FM is untestable (0 synthetic probes) and AM has 14 synthetic probes from 2 cells. |
| fig9-mgb-fast-decay | reproduced | Cell 47: τ1 is 0.080 s ("all") or 0.056 s ("running"). The mean SD after 0.5 s is within 25% of the fitted κ. Sizes are well off: α1 5.6 against 15, κ 0.8 against 2.0. |
| fig9-example-first-bin | reproduced | Cell 49: in 4 of the 12 Figure 9-design probes (cell 20071010-ha2-003, 10 repeats), the first bin is at least twice every later bin. Over all MGB probes the fraction is 36/93. |
| figs1-silence-probe | reproduced | Cell 51: 19 cells have a significant period starting within 0.5 s. Eq. 17 power falls below 10% of its onset value by 0.55 s. Not every later bin stays below 10% (mean over 2–2.5 s is 0.45, against an onset value of 5.6 mV²). |

**B. Problems**

1. [affects a conclusion] fig4-strf-performance-low (cell 0 table; no cell tests it): marked blocked with no reason. `crcns-ac1.zip` contains `wehr/Results` (25 cell folders, 1626 files), `wehr/Stimuli`, `wehr/Tools/STRFanalysis.m` and `ridgesvd1.m`, and `wehr/Contents.m` gives a sample STRF pipeline (10-fold cross-validation, ridge grid). The claim is testable.
2. [affects a conclusion] `asari.property_families`, MHT ("synthetic") branch, shown in cell 35:
   - AM has 14 synthetic probes in 2 cells; Table 1 gives 71.
   - FM has 0; Table 1 gives 57.
   - MHT amplitude and frequency have 0 each; Table 1 gives 25 each. The "naturalistic" rows happen to fill these 25 + 25.

   The notebook does not flag this mismatch. It invalidates the AM and FM results in fig8a, fig8a-significance-fits, fig8b and fig8c, and leaves the AM and FM comparisons in fig8-natural-synthetic-probes-alike without data or power.
3. [affects a conclusion] fig8c (cell 43): the natural-sound reference uses only the with-silence reading. The synthetic property sets never include silence, and the claims file leaves silence open for Figure 3B. The without-silence Q from cell 28 (α 0.446, τ 1.32 s) gives a 0–4 s area of about 0.56 s against 0.75 s. That would move the amplitude and frequency ratios to roughly 0.97 and 0.89, so the intervals could include 1. This is my estimate from the printed fits, not a run. The trial-resampling reading was also not run.
4. [affects a conclusion] Cell 43, `pt_ok`: the check for the partial outcome tests only that AM, FM and higher-order lie below amplitude, frequency and 1. It leaves out the criterion's requirement that amplitude and frequency reach 1, so it reports "point estimates in that pattern: True" when they do not.
5. [affects a conclusion] fig7 (cell 53): the search reads only `param.ff` and collapses stimuli with `set()`. `DMRipple2.m` treats a 4-element `ff` as two bands, so (625, 2500, 10000, 40000) is 0.625–2.5 kHz plus 10–40 kHz. The paper makes frequency variants by shifting a generated DMR, and a shift may not show up in `ff`. Stimulus names and descriptions were never printed. The weaker test (a natural probe after DMR frequency contexts, significant until at least 3.6 s) could be run from `SY` and was not.
6. [affects a conclusion] a1-mgb-firing-rates (cell 15, `asari.mgb_spikes`):
   - The window readings the criterion names (pre-stimulus baseline for spontaneous, probe periods for evoked) were not run; only intersequence silence and all sound periods were.
   - The MGB threshold is 2/3 of the largest filtered value in each file. Evoked 5.07 Hz against 11.4 Hz points to undercounting, and no other MGB detector was tried.
   - The partial outcome hangs on a 0.07 Hz margin.
7. [does not affect a conclusion] methods-recording-counts (cell 13): the criterion asks for the cells and probes behind the 133-versus-123 difference. They are not listed, and the DMR (15 vs 6) and MHT (26 vs 39) gaps are not explained.
8. [does not affect a conclusion] Cell 19 shows only the first 12 runs per probe. The strict 2–4 s test fails the most likely example over a run that starts 30 ms before 4 s.
9. [does not affect a conclusion] Cell 33: two fits sit at the τ = 100 s bound, and the smoothed Eq. 43 reaches 2.12. Neither is flagged.
10. [does not affect a conclusion] `asari.pop_curve("running")` returns 0, not NaN, where no probe runs. The MGB bin 60 (0 probes) enters the fit as 0.
11. [does not affect a conclusion] `asari.long_runs` keeps a run only from 51 consecutive points; I tested it, and a 50-point run is dropped while a 51-point run is kept. The paper says 50, but this matches `CxtDep.m` KWtest (`k(end) - k(1) >= dt`), which I read.
12. [does not affect a conclusion] `asari.a1_file_pass`: the without-silence variant uses 200 shuffles, not 1000. The notebook text does not say so.
13. [does not affect a conclusion] `asari.synthetic_file_pass`: property-set contexts are cut to the smallest trial count over all contexts, silence included.

Checks that passed:
- `kw_significance` matches `scipy.stats.kruskal` on untied synthetic data.
- `frac_power` is unbiased on a synthetic signal plus noise.
- `fit_exp` and `fit_paper_rule` recover (0.17, 0.20, 0.09, 0.90) and (0.49, 1.04) on synthetic curves.
- KWtest, FracPow and the blank-period lengths match `CxtDep.m`, which I read.

**C. What I could not check**

- Whether the MHT property sets are wrong because of the parser or because of the data. A per-file printout of `property_families` output, the stimulus names and descriptions, and the notes lines for each MHT recording would settle it.
- Whether a Figure 7 recording exists. A printout of the DMR files' stimulus names, descriptions and SoundTrans shift parameters, plus significant-run end times for DMR frequency probes with natural probes, would settle it.
- fig8c under the without-silence natural reference, and with trials resampled within probes.
- MGB and A1 rates under the pre-stimulus baseline and probe-period windows, and MGB rates with a second detector.
- The full run lists for the fig2 candidates.
- The list of the 10 cells that make 133 against 123.
- I did not view the plotted figures.
- The STRF claim needs its own analysis before any outcome is possible.
