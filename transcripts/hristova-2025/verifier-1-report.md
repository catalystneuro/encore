**A. Outcomes** (34 claims in the claims file: 12 reproduced, 9 partially reproduced, 3 not reproduced, 10 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig2b-swd-hourly | reproduced | Cell 20, main: genotype p = .0045 (Het about 30/h, WT about 2/h), hour p = .069, interaction p = .9998. With 132 as WT or as Het, hour reaches p = .041. |
| fig2c-swd-number | reproduced | Cell 22: W = 1, p = .047 (normal approximation because two Het tie at 816), Het higher. |
| fig2c-swd-mean-duration | partially_reproduced | Cell 24: Het 4.54 s vs WT 1.47 s, p = .16. One WT is left out (GRIN2B-238 has no SWDs), so this is a t test against one animal. |
| fig2c-swd-total-duration | reproduced | Cell 26: W = 1, exact p = .033, Het higher. |
| disc-het-swd-minutes | partially_reproduced | Cell 28: Het 57.77 min is within 59.97 ± 6. WT 1.37 min fails "< 1 min". |
| figs5a-swd-light-dark | reproduced | Cell 30: phase p = .29, genotype p = .0045, Het higher. |
| figs8-swd-sex | reproduced | Cell 32: sex p = .29, .94 and .78. Both WT are female, so sex is tested within Het in effect. |
| fig2d-swd-spectrum-peak | reproduced | Cell 36: all 15 animals with ≥ 5 SWD epochs have f0 at 7 to 8 Hz and a harmonic within 1 Hz of 2·f0. This includes the one WT (GRIN2B-240, only 18 epochs). |
| fig2e-swd-delta-power | blocked (data_missing) | Only one WT has SWDs (cell 70). The archive confirms 2 WT files (238, 240). See C for a partial test. |
| fig3d-rem-hourly | reproduced | Cell 38: genotype p = .048 (Het lower), interaction p = .096. Fragile: with 132 as WT, p = .19. |
| fig3g-rem-total | reproduced | Cell 40: t = 2.16, p = .048, Het lower. Same fragility (p = .19 with 132 as WT). |
| fig3g-rem-bouts | reproduced | Cell 42: p = .001, Het 37.9 vs WT 74. |
| fig3g-rem-bout-duration | partially_reproduced | Cell 44: Het longer (71.9 vs 56.8 s), W = 2, p = .067. |
| fig3h-nrem-total | reproduced | Cell 46: p = .22 (Het +31 min). |
| fig3h-nrem-bouts | partially_reproduced | Cell 50: bouts are fewer in Het but p = .10; bout duration is longer, p = .017. |
| fig3i-wake-total | partially_reproduced | Cell 48: Het lower by 111 min, Welch p = .35 (df 1.1). |
| fig3i-wake-bouts | partially_reproduced | Cell 52: Het have more bouts (p = .067) and shorter bouts (Welch p = .31). With the stored scores both directions reverse (see B3). |
| fig4a-rem-spectrum | reproduced | Cell 54, main: genotype p = .073, interaction p = .998. Fragile: genotype p = .034 with contiguous bands and < .0001 with SWD epochs from the scorer flags. |
| fig4b-nrem-beta | not_reproduced | Cell 56: Het beta is lower than WT (−0.078), interaction p = .90. Beta is lower or about equal in every variant. |
| fig4c-wake-power | not_reproduced | Cell 58: Het minus WT averaged over bands is +0.081, so Het are not lower (genotype p = .45). |
| fig5a-swd-state-distribution | partially_reproduced | Cell 60: reading (a) gives 94.2 / 5.5 / 0.27 %. Wake is within tolerance and the order holds; NREM and REM are outside it. No reading meets all three, including (c), the rule the Supplementary Methods describe. |
| fig5a-het-more-nrem-swds | blocked (data_missing) | Only one WT has SWDs. Its NREM share is 0% against roughly 6% mean in Het (cell 60), which is the paper's direction but cannot be tested. |
| fig5c-transition-swds | partially_reproduced | Cell 62: Het 13/14, WT 0/2, Fisher p = .025. Not every Het counts: GRIN2B-228 has 2 SWDs in two days. |
| figs5b-transition-percent | not_reproduced | Under the criterion's readings, (i) gives 36.3% and (ii) gives 2.2% (cell 64), both outside 24.2 ± 2.42. The Supplementary Methods' six-epoch NREM rule gives 22.9%, inside the tolerance (see B2). |
| fig5f-swd-wake-correlation | reproduced | Cell 66: R = −0.81, p = .0005 (inside −0.51 ± 0.3). Largely produced by the way wake time is computed (see B3). |
| fig5def-no-other-correlations | partially_reproduced | Cell 68: 2 of 8 tests have p < .05 (wake bouts p = .046, wake bout duration p = .028). Both come from the same mechanism as B3. |
| fig1c, fig1df, figs4, figs1, fig6b, fig6c, fig6d, fig7c (8 claims) | blocked (data_missing) | Confirmed in the archive (API, draft modified 2026-07-31): 17 NWB files of 73 to 99 h baseline EEG/EMG. There are no 4-h pharmacology sessions, blots, development measures or visual scores, so no part of these claims can be tested. |

**B. Problems**

1. [affects a conclusion] The dandiset's animals do not match the paper's analysed groups (cells 4, 18).
   - GRIN2B-238 (WT) has no SWDs. The paper's mean-duration test (df = 22) and Fig. 5A (n+/+ = 9) imply every analysed WT had SWDs.
   - GRIN2B-228 (Het) has about 1 SWD per day. The paper says all 15 Het had transitional SWDs.
   - The Supplementary Methods say 4 Het and 9 WT from one founder line were recorded and excluded, and the dandiset does not say which rats were analysed.
   - Effect: fig5c fails only because of 228, and the disc WT mean and every two-WT comparison depend on 238. No sensitivity run without these two animals is shown.
2. [affects a conclusion] figs5b (claims file, cell 64): reading (i) uses the epoch-before rule for NREM. The Supplementary Methods use "the first 30 seconds (six epochs) prior … to assess SWD initiation in NREM and wake-NREM transitions", and Fig. S5B uses "SWDs in NREM" as the denominator. The notebook's any6 variant follows that rule and gives 22.93%, which would make the claim reproduced.
3. [affects a conclusion] In `scored_states(mode="events")`, each SWD removes at least one whole 5-s epoch from wake and splits wake bouts.
   - For Het, the SWD epochs total 110.6 min against 57.8 min of actual SWD time (cell 28).
   - So wake minutes, wake bout counts and wake bout durations partly measure SWD counts. With the stored scores: R = −0.06 for fig5f (cell 66), the wake-bout direction reverses (cell 52), and 0 of 8 fig5def correlations are significant (cell 68).
   - This follows the paper's "SWD times were excluded", but the fig5f and fig3i outcomes are partly built in by this definition.
4. [affects a conclusion] Spectra (cell 12, `raw_windows`, `window_epochs`):
   - They cover about 10% of the baseline (12 windows of 24 min).
   - GRIN2B-129 has 4 usable REM epochs. GRIN2B-238, one of the two WT, has 72.5% of epochs with bad samples.
   - The spectral-slope and offset rejection in the Methods is not applied.
   - The channel is fixed at S1_Tr_R, while the lab's scorer chose the cleaner S1 channel per animal.
   - With n = 2 WT, the fig4 outcomes rest on these choices, and fig4a changes with the band definition or the SWD-epoch definition (cell 54).
5. [does not affect a conclusion] `band_anova` (cells 54 to 58) treats the 5 bands per animal as independent observations, so its p-values are anti-conservative. The paper does the same, and the main results are not significant anyway.
6. [does not affect a conclusion] `split_plot_anova` decomposes the interaction with group-weighted marginals. With unequal groups it is not the sequential decomposition. On synthetic data (9 vs 3 animals) the within and interaction F differ from the OLS sequential F by under 0.5%, and the between F matches a one-way ANOVA on subject means exactly. `event_epochs`, `runs`, `state_measures` and `swd_onsets` behaved correctly on synthetic inputs.
7. [does not affect a conclusion] The claims file's opening comment says a two-sided rank-sum test with 2 WT cannot reach p < .05 unless both WT rank below all Het. That is wrong: U = 1 gives exact p = .033 (cell 26).
8. [does not affect a conclusion] Cell 0 says the scorer's flags "sit one epoch after the events". Cell 6 shows every flagged epoch overlaps an event, mostly as its last epoch.
9. [does not affect a conclusion] fig2c-swd-mean-duration is a t test with n_WT = 1 (cell 24), which is uninformative.
10. [does not affect a conclusion] The dandiset's `assetsSummary` reports 16 files and 16 subjects, but there are 17 assets.

The paper states no chance levels, so there was nothing to compare.

**C. Not checked, and what would have helped**

- Whether the deposited rats are among the paper's analysed 24: this cannot be settled from the archive. Re-running every genotype claim without GRIN2B-228 and GRIN2B-238 would show how much outcomes depend on them.
- fig2e and fig5a-het-more-nrem-swds could be partly run with 132 as WT (132 and 240 have 20 and 18 SWD epochs). That output is not in the notebook, and 132's genotype is unknown.
- figs5b and fig5a: an output using the Methods' combined rule (wake and REM from the epoch before, NREM from the six epochs before) as the stated main reading.
- Spectra: per animal, the fraction of each state's baseline epochs covered by the windows, how many epochs the spectral-slope rejection would remove, and the fig4 results with the per-animal cleaner S1 channel.
- `split_plot_anova` against a fitted mixed model (statsmodels MixedLM) on the real hourly tables.
- The data-check facts (flag placement, the 32767 dropouts, the clock alignment) could not be verified independently without reading the files. The figures were checked only through their printed plotted ranges.

I saved the paper text and Supplementary Methods text under `paper/` and deleted the downloaded figures and video.
