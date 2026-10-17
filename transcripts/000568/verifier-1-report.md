# Verifier report, round 1: Valero et al. 2022 (doi:10.1126/science.abm1891) on DANDI 000568 v0.230705.1633

The claims file has 22 claims: 16 are tested in the notebook and 6 are listed as blocked. There was no attempt record in the directory, so I took the counts from the claims file and the notebook. My outcomes are 5 reproduced, 5 partially reproduced, 6 not reproduced and 6 blocked.

The paper text is the PMC author manuscript (PMC9632609), saved under `paper/` as `paper/PMC9632609_bioc.json` and `paper/PMC9632609.txt`.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| cohort-counts | partially_reproduced | Reading (a), cell 15: 4 mice and a mean of 48.2 per session (within 43.3 ± 8.37), but 1351 pyramidal cells against 822 ± 82. Reading (b) has only 3 mice. |
| fig1c-pulse-protocol | partially_reproduced | Cell 17: median duration 19.75 ms and per-uLED median intervals of 0.281 to 0.383 s pass. The end-to-start gap medians of 60.4 and 80.0 ms fail the 18 to 44 ms band. The likely cause is uLEDs whose pulses were not deposited (problem 1). |
| fig1e-responsive-fraction | reproduced | Cell 19: reading (b) gives 66/91 = 72.5%, within 74.3 ± 7.4. Reading (a) gives 62.6%, outside. Only 91 cells from one mouse. |
| fig1i-swr-decrease | reproduced | Cell 22: n = 57. Reading (a) has a median paired difference of -2.13 Hz, lower inside ripples in 49/57, p = 6.8e-9. Reading (b) also holds, and so does each session. |
| figs10-swr-gain-vs-baseline-rate | partially_reproduced | Cell 24: reading (a) gives rho = -0.437 (p = 1.8e-55), outside -0.19 ± 0.068. Reading (b) gives rho = -0.002. Negative and significant, but not within tolerance. |
| fig2b-theta-trough-gain | not_reproduced | Cell 26: trough minus peak gain has a median of -0.09 Hz and p = 0.14. In the 6-bin variant the largest gain is at +30°. |
| figs11-place-cell-fraction | not_reproduced | Cell 29: place cells are 78.9% of responsive cells (within tolerance) and 52.9% of non-responsive cells (outside 71 ± 7.1). The chi-squared test with Yates' correction gives p = 0.018, so it finds a difference. |
| fig2e-infield-gain | reproduced | Cell 31: 64 fields, median in-field minus out-of-field gain 2.74 Hz, p = 9.1e-8, both sessions significant. The ratio variant goes the other way (problem 6). |
| figs12-gain-rate-correlations | not_reproduced | Cell 33: rho = 0.051 against out-of-field rate (target 0.17 ± 0.084) and -0.065 against home-cage rate (target 0.25 ± 0.084). Neither is within tolerance. |
| fig3a-place-cells-more-excitable | reproduced | Cell 35: medians 2.07 Hz for place cells and 0.94 Hz for non-place cells, Kruskal-Wallis p = 0.0041. Below the median baseline rate the difference is not significant (p = 0.32), which the paper says rate does not explain. |
| fig3c-unmasked-fields | not_reproduced | Cell 37: reading (a) gives 10/12 = 83.3% and reading (b) gives 12/28 = 42.9%, both outside 69.3 ± 6.9. Reading (a) has only n = 12. Reading (b) is barely above the 35.7% that randomly thinned control maps give. |
| fig3e-ghost-fields | partially_reproduced | Cell 40: place fields r = 0.857, p = 1.3e-18. Unmasked fields r = 0.31, p = 0.2 (n = 19). The shuffle variant gives p = 0.002 in both. |
| fig3f-light-stability | not_reproduced | Cell 42: light stability is lower than control in both groups (place p = 6.2e-5 in the wrong direction; unmasked p = 0.087). The time-matched control variant shows no difference. |
| fig3g-spatial-information | partially_reproduced | Cell 44: the control-light correlation holds for place fields (p = 2e-6) but not for unmasked fields (p = 0.093). The increase is larger for unmasked fields (p = 0.0019), but that disappears against time-matched control (p = 0.64) and is partly a selection effect (problem 7). |
| fig4c-swr-cofiring-place-pairs | not_reproduced | Cell 46: place-cell pairs give rho = 0.041, p = 0.21, so part 1 fails. Place/non-place pairs give rho = 0.112, p = 0.0008, so the claimed absence also fails. |
| fig4d-light-unmasked-cofiring | reproduced | Cell 48: rho = 0.124, p = 0.035, meeting the criterion as written. The same pairs with control maps give a stronger rho (0.191, p = 0.001), and sess12 alone gives -0.13, so the claim that the relationship appears only with light is not supported (problem 8). |
| fig1j-light-intensity | blocked (data_missing) | Agreed. Each uLED's pulse series stores a single constant value (cell 9 output), and no other session has pulse series. |
| fig1km-intracellular | blocked (data_missing) | Agreed. The archive holds 56 NWB files and 82 AVI files from 4 mice, with no intracellular or rat data (asset list and assetsSummary). |
| figs9-excitatory-vs-inhibitory-swr | blocked (metadata_insufficient) | Agreed as stated, but a proxy test was possible (problem 11). |
| fig3h-position-decoding | blocked (methods_underspecified) | Agreed. The data needed (spikes, laps and position in 2 sessions) are present, so only the method is missing. |
| fig4ef-assemblies | blocked (methods_underspecified) | Agreed. Data present; the ICA bin size and chance level are unknown. |
| fig4gh-replay | blocked (methods_underspecified) | Agreed. Data present; the decoder and shuffle settings are unknown. |

## B. Problems

1. **[affects a conclusion] Most pulses are not in the files** (`all_light_intervals`, `control_onsets`, cells 17, 20, 27). The paper's probes have 12 uLEDs (4 shanks × 3). The files hold series for 6, and 2 of those have only 120 to 221 pulses. I simulated 12 uLEDs fired at random with 20 to 40 ms gaps and kept 4 of them. This gives a median gap of 86 ms, 33% of gaps in 20 to 40 ms, and 13.3% light-on time. The notebook shows 60 to 80 ms, 30 to 32%, and 12.6 to 13.6%. So about two thirds of pulses are probably missing, and the "no uLED on" control time (`ctrl_mask`, 88 to 90% of lap time) likely contains light from undeposited uLEDs about 27% of the time.
   - This contaminates the control maps behind place-cell calls (figs11, fig3c, fig3e to g, fig4c), the control rates in fig2e and figs12, and the fig1c gap test.
   - Cells marked non-responsive may respond to uLEDs that are not in the files (figs11, fig1e).
   - The 20 ms pre-onset control windows used in fig1i and fig2b stay dark under the stated protocol and are unaffected.
   - The notebook never examines this.

2. **[affects a conclusion] `find_fields` differs from buzcode's `bz_findPlaceFields1D`.** It leaves out the sub-field rule (re-threshold at z − 0.2·peak and keep the sub-field when it is under half the size) and the check that the map dips between fields. On a synthetic map with an 8-bin 6 Hz bump on a 1.5 Hz floor, `find_fields` returns no field, while buzcode's rule gives bins 20 to 27. Higher-rate cells and light maps, whose rates are raised everywhere, are therefore pushed toward "no field". This bears on figs11, fig3a, fig3c and fig4c/d. The docstring says it follows the buzcode defaults.

3. **[affects a conclusion] The whole optogenetic test rests on 2 sessions of one mouse** (fig1e and every claim after it). Sample sizes are 57 to 91 cells and 12 to 28 non-place cells, against the paper's 485 to 822 cells and 417 non-place cells. In fig3c reading (a), the 95% interval for 10/12 runs from about 52% to 98% and includes 69.3%. The criterion's ±10% tolerance does not account for this.

4. **[affects a conclusion] The theta phase assumes an LFP rate of exactly 1250 Hz and a start at 0 s** (`read_lfp`, cell 26). Neither value is read from the file. The clock check uses ripples 600 s into BaselinePre, about 2 to 4 h before the Maze epoch. A rate error of 0.01% would shift the clock by about 0.8 s by the Maze epoch and scramble theta phase. The notebook also does not confirm the trough convention, for example by showing that control spikes prefer ±180°, and does not check light artifacts in the 6 to 10 Hz band.

5. **[affects a conclusion] No chance level for the responsiveness test** (`responsive_sites`, cells 13 and 19). The test is never run on sham onsets, such as shifted or random times, so the false-positive fraction behind 62.6% and 72.5% is unknown. Reading (b) passes and reading (a) does not, so a few points of false positives matter. N_BOOT is 100 where the source code uses 500.

6. **[does not affect a conclusion] fig2e: additive and multiplicative gain disagree** (cell 31). The light/control ratio is lower inside the field (2.16 vs 2.89, p = 0.0004), so the in-field excess may only reflect scaling with rate. The claim is about the difference, so the outcome stands.

7. **[affects a conclusion] Selection bias in fig3f and fig3g** (cells 38, 42, 44). The unmasked group is chosen for having a light-map field and no control field. That inflates light spatial information and deflates control spatial information by construction, and light maps rest on about 8× less time than control maps. Part 2 of fig3g should count only with the time-matched control, where p = 0.64.

8. **[does not affect a conclusion] The fig4d criterion does not test the claimed contrast** (cell 48). The claim is that the relationship appears with light. The notebook's own control-map rho for the same pairs (0.191) is larger than the light-map rho (0.124), and the effect is carried by sess9 alone.

9. **[does not affect a conclusion] figs10 uses the first epoch even when it is unlabelled** (cell 24). In fCamk2 and some other sessions the first epoch is named only by a timestamp. The change and the baseline rate also share spikes, but the out-of-ripple variant (-0.466) rules that coupling out as a driver.

10. **[does not affect a conclusion] The fig3f halves include stimulation-free laps in sess9** (cell 42). Laps 11 to 60 and 71 to 120 include baseline laps 52 to 60 and 102 to 111. This only affects the control maps.

11. **[does not affect a conclusion] figs9 is declared blocked while the same proxy is used elsewhere.** The notebook defines pyramidal cells by a rate threshold throughout. The 130 units at 5 Hz or above could have served as putative interneurons for an in-ripple versus out-of-ripple gain comparison, labelled as a proxy. The blocked claims have no cells at all: there is no output showing the constant intensity values per file or the units table's columns.

12. **[does not affect a conclusion] The paper's counts don't agree with each other.** 417 non-place cells out of 822 (51%) conflicts with 71 to 73% place cells. The reading of the fig3c denominator is therefore uncertain.

## C. What I could not check

- **Whether 12 uLEDs actually ran.** Outputs that would settle it:
  - the `stimulus/presentation` keys and their descriptions in each file;
  - the probe and device metadata;
  - the total pulse rate per second in PreStim, compared with the about 20/s the protocol implies.
- **The units table columns.** Absence of a cell type rests on the notebook's statement. The asset metadata lists "Units" only and the loader reads `spike_times` and `unit_name`. Printing `f["units"].keys()` would settle it.
- **The LFP rate and start time.** Printing the `ElectricalSeriesLFP` rate and starting time, and repeating the ripple-power check inside the Maze epoch, would verify the theta phase.
- **The phase convention.** A phase histogram of control spikes would confirm which phase is the trough.
- **The false-positive rate of the responsiveness test**, from the same test run on onsets jittered by ±200 ms.
- **How many cells the missing sub-field rule changes.** Counting maps rejected only because the region above 0.2 of the peak covers more than 60% of the track would show how many cells problem 2 moves between place and non-place.
- **Methods.** I could not read the supplement's Methods (paywalled), so the response test, field definition and control-window rule could not be checked against the paper. I did not open any NWB file, per the instructions.
