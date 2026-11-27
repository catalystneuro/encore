**A. Outcomes**

The claims file has 27 claims.

| Claim | Outcome | Reason |
|---|---|---|
| fig1d-assemblage-day-night | blocked (data_missing) | The Dryad file list (38 files, checked against the API) and the Zenodo listing in cell 16 contain no video visit log or Table S2. |
| fig1e-bagged-fewer-fruit | reproduced | Cell 20: 0.794 and 0.114, exact. Holm p = 1.71e-10 (Table S4 gives 1.7e-10). |
| fig1e-nocturnal-exclusion | reproduced | Cell 20: 0.477, Holm p = 0.00824, within 10% of 0.0082. |
| fig1e-groups | reproduced | Cell 20: all 10 pairs agree with the letters, and all 10 Holm p match Table S4. |
| nocturnal-share-of-fruit | reproduced | Cell 23, reading (1): share 39.9% and reduction 28.1% (live flower) or 28.5% (floral odor), both within tolerance. Its dependency, fig3d-visits-per-night, is reproduced. |
| fig2a-gcead-monoterpenes | blocked (data_missing) | The archive has one GC-EAD trace per moth species. The paper used 8 Manduca and 13 Hyles antennae. |
| table-s6-emission-rates | blocked (data_missing) | Neither archive has the 35 headspace samples or the calibration standards needed to get ng/h. |
| fig2d-no3-degrades-monoterpenes | reproduced | Cell 27, code windows, NO3 vs clean: −32.5, −83.9, −29.8, −66.8%, all within tolerance, max p 5e-54. All four p values and test choices match Table S9 exactly. |
| fig2d-other-compounds-unchanged | reproduced | Cell 28, deciding reading: smallest p is 0.065. The p values match Table S9 (0.07, 0.49, 0.95, 0.20, 0.78, 0.48). Benzaldehyde is +0.4% and +2.1%, which matches Table S9; the Fig. 2D inset's −9% and −12% are not matched. |
| figs5-blend-oxidation | partially_reproduced | Cell 31: monoterpene falls 33–34% (p < 1e-60). Eucalyptol rises 7–9% with p < 1e-74 under both window readings, so the "no change" half fails the criterion. The raw aldoxime trace also changes by −22 to −24%. |
| fig2-dose-dependent | blocked (data_missing) | Neither archive has flowtube runs at a second NO3 dose. |
| figs6-oxidation-products | partially_reproduced | Cell 34: the three nitrates rise 17–23× in the NO3 segment, and both C10 ions rise in both segments. In the O3 segment the nitrates also rise 1.2–1.5×, with one-sided p < 0.001 (r1) and C10H17NO6 above mean+3SD (r2). The claim holds only under the author's own ≥2× threshold (r3). |
| fig3b-hyles-no3-eliminates | partially_reproduced | Cells 37–38: 0/19 and 0/42, as stated. Floral odor (5/35) vs NO3 gives p = 0.084 (z-test) or 0.216 (Yates), so the p < 0.05 part fails under both readings. |
| fig3b-manduca-no3-halves | reproduced (on the sheet as deposited; see problem 1) | Cells 37–38: decrease 54.1% relative or 49.6 points, p = 0.0058 or 0.017, NO3 vs control p = 0.60 or 0.87. The paper's p = 0.047 is not matched by any reading. |
| fig3b-o3-no2-no-effect | reproduced | Cell 37: p = 0.066 (O3) and 0.156 (NO2) by uncorrected z-test; 1 after Holm. |
| fig3b-proxy-mixture | reproduced (see problem 1) | Cell 37, reading (a): proxy vs floral p = 0.0026, proxy vs control p = 0.83, proxy vs NO3 p = 0.74. |
| figs7-manduca-sensitivity | reproduced (marginal) | Cell 41: Manduca EAG is larger than Hyles at all 9 concentrations. 0.01x vs 1x gives p = 0.19, and 0.001x vs 1x gives p = 0.046, under reading (i) only. Under (ii) that p is 0.11. The paper's 0.09 is not matched. |
| fig3d-field-no3-fewer-visits | reproduced | Cells 44–45: coefficient −1.253, SE 0.567, p = 0.027; NO3 vs control p = 0.74. Matches Table S11. |
| fig3d-real-and-synthetic-alike | reproduced | Cell 45: p = 0.944 and 0.858 under reading (a); 0.931 and 0.863 under (b). |
| fig3d-visits-per-night | reproduced | Cell 46: 1.928, 0.566 and a 70.7% drop. These are recomputed from the Table S10 summary counts, since there is no per-night data. |
| fig4ab-no3-shortens-recognition | blocked (data_missing) | The GEOS-Chem .mat file has no wind, so no distances can be computed. The wind-free "more severe" part is in cell 51 and holds only under some readings (share 1.0 under (ii), 0.506 under (b)(i), 0.374 under (a)(i)). |
| table-s13-recognition-distances | blocked (data_missing) | The distances need wind. The three percentage values (Hong Kong, Tokyo, Kinshasa) do not need wind and could have been computed (problem 3). Three values cannot reach the 6-of-8 needed for partial. |
| fig4c-preindustrial-change | not_reproduced | Not blocked: the present/preindustrial ratio does not depend on wind (cell 50 says so). Cell 51: under all 8 readings only 0 to 0.4% of Greenland land cells are above 75% (medians 34–66%). The criterion's Greenland condition therefore fails whatever the city majority turns out to be. |
| interannual-similar | blocked (data_missing) | Neither archive has the 13.2.1 runs for 2019 or 2021; there are only the pi/pd factor maps. |
| figs8-no3-faster-than-o3 | partially_reproduced | Cell 49: NO3 3.48 ppt (expected 2.6 ± 0.26) and O3 43.0 ppb (expected 37 ± 3.7), both outside tolerance. The rate comparison holds at both the recomputed and the paper's concentrations: NO3 faster for 17 of 23, both sesquiterpenes faster with O3, most reactive compound a monoterpene. |
| figs9-urban-regressions | blocked (data_missing) | Depends on the distances, which need wind. Regression B (impact on population) does not need wind (problem 3). |
| table-s1-field-conditions | partially_reproduced | Cell 54, nightly means: O3 34.2, NO2 0.99 (at the edge of 0.72 ± 0.28) and RH 47.5 are within tolerance. Wind is 1.70–2.11 m/s against 1.14 ± 0.48 under every reading. The rows cannot be placed in time, and "stable conditions" is undefined. Only 2018 data are deposited; Table S1 averages 2018 and 2019. |

**B. Problems**

1. [affects a conclusion] Cells 12 and 37, `wind_tunnel_fig3b`. The Fig. 3B sheet's Manduca "odor blend" row (11/12) is identical to the 1x row of the Fig. S7C file. The Methods say Fig. 3B used 1/100 floral equivalent, which is the S7C 0.01x row (10/14). The notebook records this finding but runs Fig. 3B only with 11/12. I reran with 10/14 as the floral reference:
   - NO3 vs floral: decrease 41%, p = 0.094 (z) or 0.187 (Yates). fig3b-manduca-no3-halves would fail.
   - Proxy vs floral: p = 0.049 (z) or 0.107 (Yates). fig3b-proxy-mixture becomes marginal.
   - O3 and NO2 vs floral: p = 0.58 and 0.97.

   Both readings should be run. The Methods' 15–42 moths per stimulus also excludes n = 12. The sheet totals 113 Manduca where the paper says 138, and the notebook never checked that count.
2. [affects a conclusion] Cell 55, fig4c. The notebook marks it blocked through its dependency, but its own cell 51 already decides the Greenland condition without wind. It should be not_reproduced. The cell-51 statistic "share of land cells ≤ 25%" is not one of the criterion's readings, which are based on the Table S13 cities.
3. [does not affect a conclusion] table-s13 and figs9. The wind-free parts were not attempted: the Hong Kong, Tokyo and Kinshasa percentages, and regression B. City coordinates (UN WPP 2019) are public. These parts cannot change the blocked outcomes.
4. [does not affect a conclusion] fig4ab, fig4c, table-s13. "Data missing" for wind is arguable: the model was driven by MERRA-2, whose 2013 bottom-level winds are public at NASA GES DISC (login required). The notebook does not consider this source.
5. [affects a conclusion] Cell 34, figs6.
   - The segment-to-oxidant labels are inferred from the outcome being tested ("only in the second do the nitrates rise"). The run order clean, O3, NO3 supports the same assignment, but the notebook does not cite it.
   - The ≥2× threshold (r3) is the author's own, and it is the only reading under which the claim holds. That should be stated as the deciding assumption.
   - r1 is a one-sided Welch test on 5 vs 9 points.
6. [affects a conclusion] Cell 31, figs5. The trace is not normalized to the reagent ion, which the Dryad notebook does; that file is not deposited. The eucalyptol +7–9% and the raw aldoxime −22% look like drift: detrending the aldoxime takes it to −1.2%. Tests on autocorrelated 1 s points push p toward zero. The outcome may therefore reflect the missing reagent-ion file rather than chemistry. This should be recorded as a limitation.
7. [does not affect a conclusion] Cells 26–28, `VOCUS_CODE`. The index windows are taken from the Dryad notebook, which I could not read. The exact match of all 12 Table S9 p values strongly supports that they were transcribed correctly. The aldoxime result depends on testing clean air over 100:200 when the mean uses 0:300: the same windows with 0:300 give p = 5e-5. `vocus_trace` detrends with `m*(t - s)`, mixing time in seconds with the section's start index. This shifts the level and so the ratio if t[0] ≠ s, but the aldoxime change is under 1% either way.
8. [does not affect a conclusion] Cell 54, `night_mask`. The time zone of the O3 and CAPS logs is assumed to be local and never checked; only the iButtons state "Timezone −7". The NO2 (0.995 against a limit of 1.00) and RH (47.51 against 47.6) passes sit at the tolerance edge, so the time zone could tip them.
9. [does not affect a conclusion] Cell 49, figs8. The means are unweighted over cells. Area or volume weighting was not run (`Gridvolume_Y0` is in the file). A 34% shortfall in NO3 is unlikely to close.
10. [does not affect a conclusion] Helper checks on synthetic inputs all passed:
    - `r_prop_test` agrees with scipy `chi2_contingency` (1.714e-11).
    - `holm` agrees with R on a 4-value test.
    - `z_prop_test` handles a zero cell.
    - `step_onset` finds the step at index 20.
    - `number_density` gives 2.69e19 cm⁻³ at STP.

**C. Could not check, and the output that would settle it**

- The Dryad notebook's windows and percent formula: print its Table S9 cells (29–33) next to `VOCUS_CODE`.
- Fig. 3B with the 0.01x floral row (problem 1): add that variant to cell 37, plus a check of the Manduca total against the paper's 138.
- The factor-map layout behind the Greenland result: print the `SpeciesConc_*` dimension names, lat/lon order and a few values over Greenland. Map pct over the Greenland box.
- The Fig. S6 segment labels: print the README.md text, which might name the segments or the sheet's oxidants.
- The O3/CAPS time zone: print the README lines on the clocks, and per-hour NO2 and O3 means.
- The table-s6 partial: list the contents of the Zenodo `.RES`/`.XLS` integration files for the single field sample.
- The fig2a partial: compare FID peak retention times in the `.atf` traces with the Fig. S2 peak labels.
