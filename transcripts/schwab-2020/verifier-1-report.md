**A. Outcomes**

The claims file lists 21 claims. The notebook tests 18 and marks 3 blocked; no separate attempt record was in the directory. My outcomes: 6 reproduced, 5 partially reproduced, 7 not reproduced, 3 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| unit-link | reproduced | 364 of 394 records found (92.4%). SDF r > 0.9 for 94.6% of 724 unit-directions (cell 17). Trial counts are equal for only 62.6%, and 25 of the matched paper-VLa units are labelled "Thalamus". |
| table1-unit-counts | not_reproduced | 268 GPi and 279 VLa units, against 209 and 185 or 218, all outside 10% (cell 19). Counting one unit per file counts a neuron recorded across several files more than once. The channel-per-day variant gives 132 and 186. |
| table1-rest-rate | reproduced | GPi 75.65 (tolerance band 63.1–77.1) and VLa 12.78 (12.15–14.85) spikes/s; rank sum p = 1e-171 (cell 21). The two animals differ in GPi (p = 0.04), where the paper says they are consistent. |
| table1-ap-width | reproduced | 0.247 and 0.509 ms, both in tolerance; p = 2.9e-37 (cell 23). |
| hold-period-ramps | partially_reproduced | The fractions, 98.5% and 98.6%, are in tolerance. The slopes differ between areas (rank sum p = 0.0415; means −0.60 and +0.23 against the paper's −0.05 and −0.14), which fails the no-difference condition (cell 25). The fraction also sits at its own chance level (problem 2). |
| mvt-responsive-fraction | reproduced | GPi 98.5%; VLa 97.5% is outside 88.1 ± 8.8 but inside the text's 94 ± 9.4, and either reading counts (cell 27). The chance level is high (problem 1). |
| increases-most-common | partially_reproduced | Monophasic increase is the most common form in both areas, and increases exceed 50% of changes. VLa monophasic increases (50.9 against 65.3) and VLa increases as a share of changes (60.2 against 68.8) are outside tolerance (cell 29). |
| monophasic-more-in-vla | not_reproduced | VLa 76.7% is outside 88.9 ± 8.9, and the difference is not significant (chi-squared p = 0.051, cell 31). The paper's-records variant would pass (69.0 against 81.2, p = 3.6e-4). |
| integrated-change-positive | partially_reproduced | Both means are significantly positive (p = 1e-10 and 4e-18), but 3.07 and 1.50 spikes are outside 3.89 ± 0.39 and 1.75 ± 0.18 (cell 33). |
| fig3a-vla-leads-gpi | not_reproduced | GPi −48 ms is in tolerance; VLa −67 ms is outside (−99 to −81). Two-sided p = 0.079 (cell 35). In Gaia the medians are equal. |
| fig3b-gpi-decr-lag-vla-incr | reproduced | −29.5 ms (band −29.7 to −24.3) and −84 ms, p = 2.1e-4 (cell 37). This is fragile: the GPi median is 0.2 ms from the edge, Isis alone gives p = 0.055, and the p-value is inflated (problem 3). |
| fig3c-vla-decr-lead-gpi-incr | not_reproduced | The order is reversed: VLa decreases at −19 ms against the paper's −108, GPi increases at −69 ms, p = 0.17 (cell 39). The paper's-records variant is not significant either (p = 0.2). |
| gating-conflict-fraction | reproduced | 95.4% conflicting, within 96 ± 9.6 (cell 41). Shuffling onsets across unit-directions gives 95.1%, so the figure equals its chance level. The paper states no chance level for it. |
| directional-units | partially_reproduced | 46.2% and 24.3% are outside tolerance; GPi is directional more often than VLa (chi-squared p = 1.7e-7, cell 43). Chance at p < 0.005 is 0.5%, so both are far above it. |
| fig4-ccf-rare | not_reproduced | KS permutation p = 0.003 for whole recordings and 0.045 for movement, 0.705 for rest (cell 47). The paper's chance level of 5% significant pairs holds (5.6%, 3.4%, 6.5%; binomial tests not significant). Significant peaks are mostly positive (+15/−4). |
| fig4-noise-corr-rare | not_reproduced | KS p < 0.0025 in both periods. 10.1% and 10.8% of pair-targets are significant, about twice the paper's 5% chance level (cell 49). |
| fig5-vla-decrease-after-gpi-bursts | not_reproduced | For all three event types the population average never falls below the corrected band (dips of −1.9 to −2.5%, cell 51). Bursts last 67 ms against the paper's 24 ms, so this is weak evidence. |
| behavior-rt-mt | partially_reproduced | The movement-duration part holds: right longer, G slower, both p ≈ 0. Reaction time has an animal effect (p = 1e-4, cell 53). |
| figs3-emg-onset | blocked (methods_underspecified) | I agree. The S3 legend and Methods give no onset criterion. The EMG is in the Zenodo mirror (S3_EMGdata_NHP_G/I.mat) and not in the dandiset. A qualitative "onset before movement" could be tested there with any detector, but not the −123 and −135 ms values. |
| fig1-vla-localization | blocked (data_missing) | Confirmed in the archive. The asset metadata list only ElectricalSeries, ElectrodeGroup, ProcessingModule and Units, and no stimulation files are on Zenodo. A proxy (VLa- against VLp-labelled electrodes in electrode coordinates) is possible only if the electrode table has coordinates, which the notebook never shows. |
| fig6-simulation | blocked (other) | `Data_Fig6.mat` (the simulation output) is on Zenodo. The growth with c, the decline with N, and the fit to ((N−1)/N)c + 1/N could be checked on that stored output; that is a re-analysis of the authors' output, not a reproduction. |

**B. Problems**

1. [affects a conclusion] `detect` / `unit_direction` have a high false-positive rate. On synthetic stationary Poisson trains (5–70 spikes/s, 30–60 trials), the increase detector fires on 5–12% of unit-directions, the ISI decrease detector on 17–37%, and either one on 22–44%. The spurious onsets fall late (median between +2 and +127 ms). With two directions per unit, the chance level of "responsive" is roughly 40–70%. The notebook never measures it. This weakens mvt-responsive-fraction and the form claims, and probably explains late VLa decreases such as Gaia's +12.5 ms median. The notebook's decrease detector is also more liberal than the paper's stored output (330 against 286 decreases, 80.7% agreement, cell 17).
2. [affects a conclusion] `control_fit`: the OLS confidence interval on a smoothed, autocorrelated SDF calls 82–89% of slopes significant on stationary synthetic input. The 98.5% / 98.6% in hold-period-ramps is therefore indistinguishable from chance.
3. [affects a conclusion] Pseudo-replication (cell 13 onward). One unit per file, while 97 of the paper's records span 2–5 files. Both directions of a unit, and every pair built from a shared unit, are treated as independent. The counts are inflated (547 units against 394) and the p-values of all rank-sum, chi-squared and KS tests are anti-conservative. This bears on the borderline calls: fig3b p = 2e-4, monophasic p = 0.051, CCF movement p = 0.045.
4. [affects a conclusion] Cell 47 leaves out the Methods' exclusion of pairs with c0 > 0.3, so it runs on 338/298/306 pairs against the paper's 427/183/172. The lag and timing of the mostly positive significant peaks are never checked for shared artefacts.
5. [affects a conclusion] Cell 49 does not control for slow drift across the session, which trial shuffling destroys and which inflates |r|. Its significance band is pooled across pair-targets with different trial counts, not set per pair-target.
6. [affects a conclusion] Cell 51 / `bursts`: bursts come out 67 ms long against the paper's 24 ms. The choice of natural log was made partly because it moved durations toward the paper's (helper docstring). The paper's `Fig5_S14.m` is in the deposit but is not cited as read. Per-pair "significant" fractions of 44–51% against the paper's 8–12% suggest the per-pair test also differs from the paper's.
7. [affects a conclusion] Cell 53 runs the ANOVA on all 250 pre-MPTP files with trials, including M1, SMA and VLp-only files. The paper's degrees of freedom (452) imply about 228 sessions, so the reaction-time animal effect may come from file selection. Movement durations exist for only 32 Gaia files.
8. [does not affect a conclusion] `_lag_counts` bins with `np.floor(d*1000)` on floating-point differences. With ms-quantized spike times this makes every independent pair significant (my synthetic test: 100% significant, KS p = 0). Sample-resolution (24414 Hz) and continuous times behave correctly. The observed 5.6% suggests the dandiset's times are not ms-quantized, but the notebook never shows their resolution.
9. [does not affect a conclusion] Windowed CCFs (cell 47): jittered spikes can leave the 500 ms analysis windows. Synthetically this adds an offset of +0.0035, and 4 null runs gave non-significant KS tests.
10. [does not affect a conclusion] `valid_trials`: errors cannot be excluded in the files without `error_onset_time`, about half of them (cells 7–8).
11. [does not affect a conclusion] `ap_widths`: widths of 0.000 ms are kept in the means, 15 units are NaN, the 1.2 ms post-window caps the width, and the trace is 200 Hz filtered against the paper's 300 Hz. The channel-to-series match takes the first series with exactly one matching electrode and is not checked for channel ids repeated across probes.
12. [does not affect a conclusion] fig3a uses two-sided p = 0.079; one-sided (z = 1.75) would be p = 0.04 and make it partially reproduced. The paper's own z = 3.31 with p = 2.4e-5 is internally inconsistent.
13. [does not affect a conclusion] gating-conflict-fraction reproduces, but its value equals the shuffle reference (95.1%), so it carries no information about gating (cell 41).
14. [does not affect a conclusion] The clock check could not confirm 34 of the 163 files (cell 11). The rate criterion uses the span from first to last spike, not the recording length.

**C. What I could not check, and the output that would have settled it**

- Spike-time resolution: the fraction of `spikes*1000` that are integers, per file. This settles problem 8.
- Chance level of response detection on the real data: `detect` run on alignments to random times in the hold period, or on trial-shuffled data, reported as a chance responsive fraction and a chance onset distribution.
- Effect of pseudo-replication: every test re-run with one record per neuron, merging consecutive-file units with the same channel and sort letter, or using the paper's records.
- CCF artefacts: the lag of each significant peak, and the count of identical spike times in GPi–VLa pairs.
- Noise-correlation drift: the correlation of trial counts with trial index, and r after detrending.
- Electrode channel mapping for AP widths: the number of electrodes sharing a channel id per file.
- A fig1 proxy: the electrode-table columns, to see whether coordinates exist.
- Behaviour: the ANOVA restricted to the paper's files.
- Burst detector: a side-by-side of the helper's `bursts` with the code in `Fig5_S14.m`.

The paper's full text (PLOS JATS XML and a text extract) is saved under `paper/`.
