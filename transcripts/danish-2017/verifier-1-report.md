**Verifier report, round 1: Danish, Aronov & Fee 2017 (PLoS ONE 12:e0169568) on CRCNS aa-3**

The claims file has 26 claims. The notebook tests 20 of them and blocks 6. The archive's checksums match the ones the notebook pins (`checksums.md5`: Electrophysiology 0a93b3d4…, Lesion 0d4f55eb…).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| lesion-directed-song-abolished | blocked (metadata_insufficient) | The lesion archive has only Pre-lesion and Post-lesion folders, with no directed-song label (cells 39, 57). The data description says directed song was recorded, so it may be in the folders unmarked. That makes this missing metadata more than missing data. |
| lesion-undirected-rate-similar | not_reproduced | Post-lesion rates are lower: syllables/h p = 0.031, bouts/h p = 0.047, singing time/h p = 0.031. Post/pre ratios run from 0.08 to 1.4 (cell 44). The result is fragile (problem 6). |
| fig2g-maturity-index-drop | partially_reproduced | Only one of 16 forms matches: "log centred", gap 300, reading a gives pre 0.235, post 0.096, 7/7 birds decreasing, p = 0.016. The literal "correlation of power spectra" form rises after the lesion in 6/7 birds (cell 46). The matching form is the author's own and not from the paper (problem 2). |
| fig2f-closer-to-exponential | partially_reproduced | Gamma falls in 7/7 birds (p = 0.0156) and stays above 2. The values do not match: pre 30.4 against 16±6, post 15.2 against 3.7±1.2 (reading a; reading b is similar) (cell 48). |
| fig2c-small-syllable-peak | partially_reproduced | With the claims file's 5 ms bins, 7/7 birds have a peak; the paper says 6, tolerance 0. The 10 ms variant gives 6/7 (cell 50). The local maxima include noise bumps (problem 5). |
| fig2d-gaps-broader | reproduced | Under reading (a), all 7 birds have more than 10% of post gaps outside the pre 5–95% range (p = 0.0156). Long fractions exceed 5% in 7/7 birds and short fractions in 6/7; from the printed values, a signed-rank test on short fraction minus 0.05 gives p ≈ 0.047 (cell 52). |
| fig2e-rhythmicity-drop | partially_reproduced | R falls in 7/7 birds (p = 0.0156), but the values are outside tolerance: pre 4.84 against 3.3±1.1, post 2.44 against 1.7±0.3. The other null reading gives 5.87 and 2.41 (cell 55). |
| fig2e-residual-rhythm-peak | not_reproduced | The test finds a peak in 7/7 birds under every reading; the paper says 6, tolerance 0 (cell 56). In 3 birds the "peak" is the band edge (3.17 Hz), and the thresholds of about 1.1 to 1.3 mean the test cannot fail (problem 4). |
| figs1-control-lesions-no-effect | blocked (data_missing) | The archive holds 7 lesioned birds, the paper's Uva lesion count, and no control-lesion birds. |
| fig3-antidromic | blocked (other: not attempted) | This was testable. The helper already extracts stimulation-artefact snippets: 147 files flagged `with_stim`, and the spreadsheets give intensities of 150, 200 and 320 µA (cell 3). |
| single-unit-spontaneous-rates | blocked (metadata_insufficient) | EventTimes is empty and no units are sorted or identified. Raw "spontaneous activity" files do exist (32 spreadsheet rows), but nothing says which units are HVC-projecting. |
| fig4c-call-premotor | partially_reproduced | Peak latency is 15 ms (13 and 17 ms per bird), which matches. Baseline latency is undefined in b871: its peak never exceeds the band (0.049 against 0.071). The printed "22 ms mean" is Uva4 alone (cell 12). |
| fig4b-introductory-note-premotor | partially_reproduced | Under shuffle (a) no bird crosses the band. Under shuffle (b), 35.5 ms and 23.3 ms fall within tolerance, but only 2 of 3 birds cross (nanmean). The shuffle-(b) band is contaminated for these events (problems 7 and 9). |
| fig4a-elevated-during-song | reproduced | MUA is higher inside bouts at 18/18 sites; paired t-test p = 1.8e-6 (cell 16). |
| fig5-consistent-across-renditions | partially_reproduced | No reading has both values within tolerance. Reading a: correlation 0.701 (limit 0.70), coherence 0.585 (limit 0.59). Reading c: correlation 0.829 (out), coherence 0.730 (in) (cell 23). |
| fig5-consistent-across-sites | partially_reproduced | Coherence between single renditions is 0.688, within tolerance. Correlation is 0.705 for single renditions and 0.893 for site averages; tolerance is 0.62±0.03 (cell 24). The "no variation across sites" part was not tested. |
| fig6-peak-before-onset | partially_reproduced | Paired t-tests give p ≈ 0 in every bird under both readings, and the rise time (28–29 ms) is within tolerance. The peak is at 17.0 ms against 20±2 (cell 18), and it depends on the channel choice (problem 3). |
| fig6-dip-before-offset | reproduced | Under shuffle (b): minimum at 18.0 ms (tolerance 18±1), drop below the band at 40.3 ms (48±8), and tests p < 1e-8 in every bird (cell 19). Shuffle (a) gives 36.3 ms, outside tolerance. |
| fig7a-correlation-with-amplitude | reproduced | Under motifs with amplitude reading (c): 0.382 at 40.7 ms, MUA first (cell 27). This is one of 6 combinations. |
| spectral-features-weak | blocked (other: not attempted) | The raw sound channel is in the archive, so this could be tested. |
| fig7b-10hz-power-peaks | partially_reproduced | The MUA peak falls within 8.8±0.88 Hz under several readings (8.91, 9.40 Hz). The song peak does not under any reading (best is 9.03 Hz against 8.0±0.8) (cell 29). |
| fig7d-10hz-coherence | reproduced | Under motifs with amplitude reading (b): 9.03 Hz, coherence 0.789, phase −0.721π, p = 0.001 (cell 30). The phase convention matches Chronux `coherencyc`. The cross-spectrum peak was not shown. |
| fig8-no-gte-relation | blocked (other) | The notebook says no implementation is public. A copy of the authors' lab's GTE extraction code from 2015 is public (problem 12), so this may be testable. |
| fig9-long-syllable-gamma | not_reproduced | 6 of 18 syllable types are long (0.33 against 0.43±0.043). One significant peak is at 10.7 Hz, below the 15.3 Hz bound. The coherence is not significant without a break from 1.1 to 49.5 Hz. Both nulls have a bug (problem 1): the count fails regardless, but the coherence and peak parts cannot be judged from these outputs. |
| bout-offset-suppression | partially_reproduced | Activity falls below the band after offset in 3/3 birds. It returns into the band after 30, 309 and 42 ms (mean 127 ms; tolerance 180–220) (cell 34). |
| no-motif-bout-signal | not_reproduced | In Orange150, activity before motif onsets is higher than before other onsets, p = 0.0012, although the difference is small (0.0635 against 0.0607). No band excursion follows motif or bout offsets (cell 36). |

### B. Problems

1. **[affects a conclusion]** `uva.scrambled_ffts` (cell 32). `gauss_smooth` uses `mode="same"` with zero padding, so every positive scrambled MUA window gets the same edge dip. On synthetic stereotyped amplitude with a positive-mean MUA, the 95th percentile of the null maximum over 1–60 Hz is 0.94; with an edge-free scramble it is 0.17. The notebook's coherence threshold is 0.451, while the real coherence is about 0.28 to 0.49 across 1–55 Hz. A correct null would probably pass the coherence part. The same artefact lowers the power null's maximum above 10 Hz by about 20%, which inflates the 5/6 significant-peak count.
2. **[affects a conclusion]** Cell 46, maturity index. The four spectrum "forms" (log, and centring per frequency across the condition's slices) are the author's additions, not readings in the claims file. Only one of the 16 combinations matches, and the literal form reverses the effect. The claims file asks that Aronov et al. 2008 settle open details; the notebook did not consult it.
3. **[affects a conclusion]** Cell 6, channel choice. The channel used is the one with the largest onset-aligned modulation, which selects on the outcome later tested in fig6 and fig4. The peak latency depends on the channel: b871 gives −13 ms on channel 6 and −18 ms on channel 7. The notebook's `_dbase` does not read `dbase.ChannelFiles`, which the dataset's own `process_recording.m` uses to list the valid neural channels. In Orange150, channels 5 and 6 are identical (r = 1.000).
4. **[affects a conclusion]** Cell 54/56, residual-peak test. A band-edge maximum (3.174 Hz in Purple94, LPink13 and LPink15; 4.15 Hz in the 4–8 Hz band) is counted as a peak. The synthetic null has no within-syllable amplitude texture, so its ratio thresholds of 1.1 to 1.3 are passed by any real song.
5. **[affects a conclusion]** Cell 50, small-syllable peak. Local maxima on 5 ms histograms pick up count noise (LPink15 has 4 "peaks" between 50 and 100 ms). Reading (a) is nearly guaranteed, because an exponential density falls monotonically.
6. **[affects a conclusion]** Cell 44, singing rate. Recording hours are taken as the span from the first to the last file, which reaches 36 to 42 h on the two-date post folders and is 2 to 3 h for LPink13. Only selected segments are counted, and the selected fraction differs before and after the lesion (Purple53: 59% pre, 34% post). Using all segments from cell 39, my calculation gives a post/pre Wilcoxon p ≈ 0.08, which is not significant.
7. **[affects a conclusion]** Cells 12 and 14. "Mean over birds" for the baseline latency is a nanmean over 1 or 2 birds, and the printout does not say so.
8. **[affects a conclusion]** `circ_shift_band` (cell 10). The 150 ms padding on each side of a bout is never shifted. For introductory notes at bout start, the pre-onset part of every shuffle is the real data, so the shuffle-(b) band that fig4b relies on is invalid there.
9. **[does not affect a conclusion]** Cell 29, fig7b. Each bird's spectrum is re-normalized over 3–30 Hz, which overrides the "length" normalization reading. The song peak misses tolerance either way.
10. **[does not affect a conclusion]** Cell 54. The null spectrum is the mean of only 5 synthetic draws, the 30 Hz upper bound is the author's choice, and the peak test uses 200 draws where the claims file asks for 1000. R's maximum may be inflated by noise, but the values are well outside tolerance regardless.
11. **[does not affect a conclusion]** Cell 48. Gamma reading (a) scales with √n, and the per-day n differs (2,129 to 20,127 syllables). Subsampling to the paper's n would not bring the post values to 3.7.
12. **[affects a conclusion]** Cell 57, blocked reasons. fig3 and spectral-features are "not attempted", not blocked by the data. For fig8, the GTE extraction code is public as a third-party mirror of the authors' lab code ([kylerbrown/mindlin_auto](https://github.com/kylerbrown/mindlin_auto), which cites Boari et al. 2015 and names lsd.df.uba.ar as its source). I did not check whether it compiles.
13. **[does not affect a conclusion]** Cell 36. The onset comparison uses a 40 ms window mean where the criterion says peak, and it uses no shuffled band for onsets.
14. **[does not affect a conclusion]** Cell 21. For the 5 ms smoothing, only the "5 ms total SD" reading is run. Adding 5 ms on top of the 2 ms kernel would only raise the correlation further.

### C. What I could not check, and the output that would settle it

- **Maturity index definition:** whether Aronov et al. 2008 log-scales or centres the spectra. A cited quote of its definition would settle problem 2.
- **Gamma scale:** ref 41's definition, which the notebook also did not read.
- **Neural channel:** which channel is the Uva electrode. Printing `dbase.ChannelFiles` and `SoundFiles` per bird would settle it, as would fig6 latencies per channel.
- **Directed song:** whether directed song is hidden in the post-lesion folders. A per-file listing with names and times would show it.
- **Long-syllable nulls (fig9):** the coherence and peak results under an edge-free scramble, and the null threshold printed per type.
- **Syllable-duration peaks (fig2c):** the 5 ms histograms with the exponential fit and its bound plotted, to judge the peaks.
- **Residual rhythm peak:** the per-bird rhythm ratio spectra, with a local-maximum requirement added to the test.
- **Singing rate:** rates computed from all segments, and recording hours from summed file lengths in place of the time span.
- **Event-aligned averages (fig4, fig6, bout offsets):** plots of each bird's average with its band. Only summary numbers were printed.
- **Post-lesion day:** whether it is the first day of singing after surgery. The data do not say.

Sources: [kylerbrown/mindlin_auto](https://github.com/kylerbrown/mindlin_auto), [Boari et al. 2015 (CONICET PDF)](https://ri.conicet.gov.ar/bitstream/handle/11336/47891/CONICET_Digital_Nro.182022d9-e4e8-4631-a239-0c964d3092ff_A.pdf?sequence=2)
