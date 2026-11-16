**A. Outcomes** (26 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| behav-no-context-baseline | blocked (data_missing) | I listed the zip's central directory: 132 entries, all ECoG, stimuli, BIDS sidecars and code. There is no behavioural file, and the README and participants.tsv describe only the 7 patients. |
| behav-context-enhancement | blocked (data_missing) | Same as above. |
| supp1a-linguistic-context | blocked (data_missing) | Same as above. |
| supp1a-speaker-no-difference | blocked (data_missing) | Same as above. |
| supp1b-filter-type | blocked (data_missing) | Same as above. |
| supp5a-behaviour-over-trials | blocked (data_missing) | Same as above. |
| speech-r-count | partially_reproduced | Cell 8: 3 of 12 readings fall inside 92 ± 9.2 (96, 99, 101), and all three use the non-event z-score. The electrode total is 377 good of 416, against 468 ± 46.8, so the fraction is 26.8% against 19.6%. |
| fig3b-hfb-increase-after | reproduced | Cell 11: positive cluster from 0.36 to 1.28 s, P = 0.0001, n = 101. It holds under both z-scores and both electrode sets. |
| supp3a-pink-noise-no-hfb-change | reproduced | Cell 12: no cluster below 0.05 (smallest P = 0.0895, n = 36, reading (b)). Reading (a) has 0 electrodes. The mean pink-noise effect (0.041 z) equals the speech effect, so this absence reflects low power, not evidence of no effect. |
| supp5b-hfb-stable-over-session | not_reproduced | Cell 14: the slope is negative and its 95% interval excludes 0 for both units, and in 6 of 7 subjects. This was run only under the non-event z-score (problem 1). |
| fig4a-coherence-after-higher | reproduced | Cell 15, set (a), n = 84: P = 0.0023 (0 to 1 s), 0.0053 (1 to 2.5 s), 0.137 before onset. Set (b), n = 251, fails at 0 to 1 s (P = 0.65). |
| fig4b-coherence-sentence-specific | reproduced | Cell 16, set (a): late window P = 0.038 (mean over all trials subtracted) and 0.0025 (mean per condition subtracted). The 0 to 1 s window is also significant, unlike the paper's 0.241. |
| strf-r-count | not_reproduced | Cell 19: 9 STRF-R (13 at most under any reading) against 53 ± 5.3. |
| included-electrode-count | not_reproduced | Cell 20: 9 included under the adopted reading, at most 13, and 0 of 72 readings within 41 ± 4.1. Only S01, S02 and S04 contribute. |
| fig8-mtf-matches-filter | not_reproduced | Cell 22, n = 9: the AFTER − BEFORE shift has no in-region cluster under either reading (shift_a's only significant cluster is out of region; shift_b has no cluster below 0.69). BEFORE (P = 0.0078) and AFTER (P = 0.043) pass only on a crude centroid rule, and most significant clusters lie outside the expected region. |
| fig9-rms-increase | partially_reproduced | Cell 23: AFTER > BEFORE with P = 0.034 / 0.031 (mean-eSTRF readings) and 0.077 / 0.073 (z-eSTRF readings). The absolute increase is 12.0, not 0.12 ± 0.03, because the unit is not comparable (problem 4). n = 9. |
| fig9-middle-generalizes-after | reproduced | Cell 24, concatenated reading: improvement 0.0506, P = 0.021. This rests on n = 9, not 41. |
| fig10-partial-correlation | partially_reproduced | Cell 25: direction and significance match (P = 0.011 / 0.0042), but the mean difference is 0.31, outside 0.18 ± 0.018. n = 9. |
| fig10b-similarity-correlates | not_reproduced | Cell 26: r = 0.52 to 0.63 with P = 0.067 to 0.147 under every reading. That is outside 0.42 ± 0.042 and P > 0.05. |
| fig10c-stg-location | reproduced | Cell 27: reading (a) gives 0.517 > 0.5; reading (b) gives exactly 0.500. It is marginal: 4 of the 9 electrodes are on STG (base rate 0.44). |
| supp3b-pink-noise-no-pcorr-change | blocked (other) | Cell 28: 0 included electrodes in S07, S08 and S13, because the STRF-R selection fails upstream. The data exist (28 pink-noise triplets per subject, and the noise eSTRFs are fit in cell 17), so a test on another electrode set could run, but the criterion's set is empty. |
| supp6a-connectivity-increase | not_reproduced | Cell 29: frontal P = 0.0312, temporal P = 0.094, from 6 seeds. With 6 seeds the smallest P the test can give is 0.031. |
| supp6a-after-closer-to-middle | reproduced | Cell 30: AFTER is closer in both regions (frontal 0.089 vs 0.156; temporal 0.207 vs 0.214, a tiny margin). 6 seeds. |
| supp6b-no-pac-change | reproduced | Cell 31: 3 to 8 Hz P = 0.14 (4 to 8 Hz P = 0.055, 2 to 12 Hz P = 0.54). n = 9, so power is low. |
| supp7-envelope-coherence | not_reproduced | Cell 32: the temporal MIDDLE − BEFORE test has no theta cluster (best P = 0.093, at 1.7 to 2.3 Hz). The frontal set does show a significant cluster at 6.7 to 8.3 Hz (P = 0.0012). |
| supp4-hfb-power-increase | reproduced | Cell 33: frontal HFB increase P = 0.0001, frontal drop at 4.2 to 19.4 Hz P = 0.0001, temporal HFB increase P = 0.0005. |

**B. Problems**

1. [affects a conclusion] supp5b, cell 14. Only the non-event z-score is run. That z-score is fixed over the whole session, so a slow drift in HFB shows up as a slope on trial number. A per-trial baseline (open detail 3, readings a and b, which match the paper's "z-score over baseline") would remove the drift. The not_reproduced outcome may come from this choice. Separately, the bootstrap for unit (a) resamples electrode × sound pairs as if independent, which makes its interval too narrow.
2. [affects a conclusion] supp6a, cell 29. Seeds are restricted to included electrodes on the temporal lobe (6), while the criterion says "the included electrodes" (9). The notebook's choice follows the Supplementary Methods ("located on the temporal lobe, hereafter called Temporal seeds"), so here the claims file misreads the paper. Its explanation of 39 vs 41 seeds is also unsupported. The notebook does not state the deviation, and with n = 6 neither test can do better than P = 0.031.
3. [affects a conclusion] Coherence uses `mt_coherence` with nw = 2 (cells 15, 16, 29) and nw = 3 (cell 32). Open detail 10 sets MNE's multitaper defaults as the standard (half-bandwidth 4, 7 tapers), and the notebook does not state its choice as an assumption. On synthetic independent noise, the residual bias after jackknife correction is 6.3 bits/s at nw = 2 against 3.8 bits/s at nw = 4. This could move fig4a/b (set a), supp6a and supp7.
4. [affects a conclusion] fig9-rms, cell 23. The RMS scale (about 105) is set by standardizing a 672-column design and the eSTRF. The paper's 0.12 has no stated unit, so the claims file's absolute tolerance compares quantities in different units. This is a claims-file problem to report. The notebook's `relative_increase` (0.126) is not in the criterion.
5. [affects a conclusion] Cells 6, 17 and 19, all eSTRF claims. STRF-R comes out at 9 and 0 in four subjects. Nothing checks that the spectrogram and HFB are aligned, for example model R2 as a function of a spectrogram time shift. The audio before onset is not silent in S07 and S13 (onset ratios 11.1 and 2.7), and S03's HFB onset contrast is 0.029. So nine claims rest on a selection whose failure has not been separated from a pipeline problem.
6. [does not affect a conclusion] Cell 17, `ALPHAS`. The mode of best alphas sits at the top of the grid (1e8: 2751 of 11860 values). The notebook drops the top value instead of extending the grid; this is disclosed. Alpha is also chosen on the same leave-one-trial-out R2 that selects STRF-R, which would raise the count, not lower it.
7. [does not affect a conclusion] Cell 22. The "filter region" is judged by comparing a cluster's centroid with the grid median (11.9 Hz, 0.234 cycles/band). The filter cutoffs are 3 Hz and 0.5 cycles/kHz, and the spectral axis is in cycles per band, not cycles/kHz. The shift test fails either way.
8. [does not affect a conclusion] Cell 15, `WIN_CENTRES`. The "-1 to 0 s" bin includes the window from -0.3 to 0.1 s, which runs 100 ms past onset. Only 2 pre-stimulus windows exist.
9. [does not affect a conclusion] Cell 12. The pink-noise and speech AFTER − BEFORE means are both printed as 0.041 z on the same 36 electrodes. The supp3a absence therefore reflects power, and the identical values should be printed with more digits to rule out a bug.
10. [does not affect a conclusion] Cell 33. Wavelets run from 3 to 200 Hz, against the claims file's standard 1 to 200. 5-cycle wavelets below about 6 Hz reach the epoch edge at -1 s, so edge effects enter the low-frequency baseline.
11. [does not affect a conclusion] Cell 31. The included frontal-inferior electrode is both an amplitude and a phase channel, so it adds within-channel PAC.
12. [does not affect a conclusion] "Frontal" is defined inconsistently: the region label in cell 4 gives 64 electrodes, while `startswith(frontal, premotor)` in cells 29 and 31 to 33 gives 90.
13. [does not affect a conclusion] Claims file, speech-r-count. It lists the total of 468 ± 46.8 as an expected value, while the criterion says the total is only reported. The data set's grids (64, 64, 64, 48, 60, 52, 64 channels) differ from the paper's (48 to 110), so the total cannot match.

**C. What I could not check, and what output would have let me**

- Whether the low STRF-R count comes from the data or from the pipeline. Needed: held-out R2 of the MIDDLE model against a spectrogram shift of ±0.5 s, per subject, plus each subject's distribution of R2.
- supp5b under the per-trial and pooled-baseline z-scores, and with a per-subject or clustered bootstrap.
- fig4, supp6a and supp7 at NW = 4.
- Per-subject included counts against the paper's Figure 6b (not printed).
- The two 0.041 z means in cell 12, printed at full precision.
- The data set ships the authors' per-subject notebooks (`data/code/results/results_S0x.ipynb`). They might fix the electrode selection or the ridge parameter. I did not read them, and the notebook does not say whether it used them.
