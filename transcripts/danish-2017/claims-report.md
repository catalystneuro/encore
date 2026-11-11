I wrote `claims/danish-2017.yaml`. The quote checker passes it: 26 claims, 26 quotes, 10 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record (PMC5472270, Europe PMC full-text XML), with main text, figure legends and Materials and methods. The supplement is only legends (S1 Video, S1 to S5 Figs), and those are all in the text. No PDF was supplied, and none was needed. The paper links no code. It names Chronux and the GTE method of Boari et al. without versions. I did not read the dataset's own scripts, because they are part of its files.

**Claims.**
- **Coverage:** 9 claims on lesions (Fig 2, S1 Fig) and 17 on recordings (Figs 3 to 9, S2 to S5 Figs).
- **Quotes:** all 26 have one, so none needed an `inferred` note.
- **Statistics:** 8 claims carry 10 entries: the three Wilcoxon tests with p < 0.025 (n = 7), the three control comparisons with p > 0.50, the paired t-tests with p < 0.01, the Bonferroni-corrected feature correlations, and the coherency at p < 0.01.
- **Expected values:** 19 claims have them. Tolerances follow the paper's SD or SEM where it gives one, and 10% otherwise.
- **Criteria:** all 26 claims have one.

**Details the paper leaves open, and the readings named for each:**
- **Sound amplitude:** (a) Sound analysis amplitude (1 to 4 kHz, squared, 2.5 ms Gaussian) in dB; (b) the same without the log; (c) rectified audio smoothed at 2 ms, as the Rhythmicity section says.
- **Shuffled baseline:** (a) averages at random times during singing; (b) a circular shift within each bout.
- **Spectral segments:** (a) each bout; (b) each motif rendition.
- **Taper setting:** "1 tapers, 2 time half-bandwidth" is read as Chronux [2 1], named as a standard choice.
- **Maturity index:** two ways of forming the lag correlation function. Also the bout gap (300 ms or 350 ms) and the post-lesion day (first day of singing, or all days pooled).
- **Goodness of fit Γ:** its scale is undefined: (a) the Lilliefors distance D times √n; (b) D divided by the critical value at alpha 0.05.
- **Null spectrum for rhythmicity R:** (a) an exponential fit to syllable durations and a log-normal fit to gaps from the bird's own song; (b) the same fits taken from its post-lesion song.
- **Peak tests:** the rule for a significant rhythm peak (3 to 8 Hz, or the legend's 4 to 8 Hz) and for a peak at 50 to 100 ms in the syllable-duration distribution.
- **Paired t-test around syllable onsets and offsets:** the window compared with (a) the rendition's bout mean or (b) a window around the neighbouring syllable boundary.
- **Correlation pairing across renditions and sites:** zero-lag pairs, peak cross-correlation, or one against the mean of the others.
- **Spectral features:** correlated per rendition or per time bin.
- **Spectrum normalization:** by the sum or by bout length.
- **Unnamed tests:** the measure and test for "sang at rates similar", "gaps more broadly distributed", the control-lesion comparisons (read as Wilcoxon), and the motif and bout absence claim.
- **Standard choices:** histogram bins, peak-search windows, the multiple-comparison form for coherency, and the number of GTE surrogates.

**Missing from the paper.**
- No code is linked, so the GTE claim depends on Boari et al.'s implementation being public.
- The paper gives no test or measure for the directed-song claim (shown only by video) or the singing-rate claim.
- The paper reports 5 recorded birds and 7 lesioned birds. The archive's description says the dataset holds multiunit recordings from 3 birds. It does not say whether control lesions, directed-song recordings, antidromic stimulation recordings or single units are included. I noted this in the opening comment and made the count criteria allow for fewer birds.
