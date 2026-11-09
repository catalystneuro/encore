**Verifier report, round 1: Goncalves et al. 2013 (doi:10.1038/nn.3415), CRCNS ssc-8**

One process note first: the notebook's "Summary" table and the "How the analysis differs" text in cell 34 were not removed. I saw them, but the outcomes below come from the outputs and the claims-file criteria only.

The claims file has 28 claims. The notebook tests 11 of them and treats 17 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| group-sizes | not_reproduced | Cell 10: the data set has 13, 8, 7 WT and 9, 10, 6 KO mice, against 12, 9, 8 and 9, 10, 8. Only 2 of 6 groups match, at tolerance 0. |
| fig1d-distance-dependent-decorrelation | partially_reproduced | Cell 12, xcorr0: the differences are 0.191, 0.105 and 0.025, against 0.223±0.022, 0.159±0.016 and 0.067±0.0067, so all three are outside tolerance under both ANOVA readings. The rest of the criterion holds: Bonferroni p is below 0.05, 0.05 and not significant, and the difference falls with distance. The criterion defines no partial outcome; I call it partial because the pattern and the tests hold and only the sizes miss. |
| fig1e-age-decrease | reproduced | Cell 15: under both readings E-a and E-b, p is 1.8e-7 for WT and 8.1e-8 for KO, and the P9-11 mean is above the P30-40 mean in both. |
| genotype-pooled-ages | partially_reproduced | Cell 17: the genotype effect has p = 0.0064 with KO higher. No reading puts both means within tolerance (P-a/M-a: WT 0.245 is out; P-b/M-a: KO 0.251 is out; M-b: both are about 0.013 low). |
| pearson-genotype | partially_reproduced | Cell 19: p = 0.023 with KO higher. No reading puts both means within tolerance; under M-b both are about 0.017 low. |
| fig1ef-p14-16-difference | not_reproduced | Cell 21: both means are within tolerance (WT 0.169, KO 0.204), but Student p = 0.057. The test does not hold, so the claim cannot be partial. The KO minus WT difference at P14-16 (0.035) is also smaller than at P9-11 (0.062). Welch p is 0.049. |
| p30-40-no-difference | reproduced | Cell 23: Student p = 0.215. WT 0.119 is within tolerance; KO 0.134 is just outside 0.144±0.008, which is reported only and does not decide the claim. |
| fig2b-peak-frequency | reproduced | Cell 25: p is 0.52, 0.64, 0.13 and 0.45 under the four R × S readings, so no difference under any. Under R-a, both means are within tolerance (WT about 0.054–0.056, KO about 0.060–0.061 per s). |
| fig2c-participation | not_reproduced | Cell 27: none of the 8 readings (R × S × Q) gives p < 0.05; the lowest is 0.153. Q-a means are 0.40–0.44 against 0.30 and 0.38. |
| imaging-firing-rate-no-genotype-difference | reproduced | Cell 29: Student p is 0.73, 1.00 and 0.76 at the three ages. |
| unanesthetized-p14-16-values | reproduced | Cell 31: under U-a, WT is 0.304 Hz and KO 0.304 Hz, both within ±0.03. WT correlation of pairs under 100 µm is 0.169, within 0.17±0.01. |
| wholecell-updown-firing, wholecell-state-modulation, fig3f-foa-time, ap-kinetics-similar, fig4-updown-properties-similar, fig4f-spikes-per-up-state, fig4g-up-state-firing-probability | blocked (data_missing) | The archive listing has no whole-cell data (see below). |
| fig5c-firing-vs-lh-p14-16, p30-40-firing-vs-lh, fig5d-correlation-vs-lh, fig5ef-slow-wave-epochs, fig5g-lh-power-similar | blocked (data_missing) | There is no EEG in the archive. |
| suppl4a-firing-vs-correlation | blocked (metadata_insufficient) | No EEG is needed, but the claim's sample is the 13 WT and 10 KO 3-min recordings of the EEG subset. The data set holds one concatenated recording per mouse and does not mark which recordings were in the subset. The cell 33 variant on 720-frame segments is not the paper's sample. |
| fast-imaging-control | blocked (data_missing) | All movies are in "4Hz" folders; there is no 15.6 Hz imaging. |
| fig6-isoflurane-wt-correlation, fig6-isoflurane-ko-correlation, fig6-isoflurane-firing | blocked (data_missing) | There is no isoflurane imaging. Only the unanesthetized arm can be tested; it is covered by unanesthetized-p14-16-values. The KO unanesthetized value is 0.204, consistent with 0.21 (reading I-b). |

**Archive check.** An S3 listing of `ssc-8/` returns only `Ca2+_imaging_TIFFs.tar.gz`, `firingrates_and_distances.mat`, `checksums.md5`, `filelist.txt` and `docs/` (the descriptor as docx and pdf). The descriptor names only the movies, the rates and the distances. This confirms that every blocked claim lacks its data, apart from the sample question for suppl4a.

**Chance level.** The paper defines the threshold for peaks of synchrony as the 95th percentile of shuffled peaks (p = 0.05). The notebook implements this; under R-a the thresholds are 23–37.5% of cells active, against a mean of 11.8% active per frame.

### B. Problems

1. [affects a conclusion] **`ssc8._active`, reading R-b.** "At least one spike in the frame" is coded as `rates / 3.9 >= 1`, which assumes the rates are in Hz (U-a). Under unit reading U-b (rates per frame), R-b would be `rates >= 1`. That was never run, so fig2b and fig2c were not run under every reading the open details allow. It is unlikely to rescue fig2c, but it is untested.
2. [does not affect a conclusion] **Cell 4, unit reading U-a.** U-a (rates in Hz) is chosen mainly because the means sit close to the paper's Hz values, which are the values being tested, so the argument is partly circular. The data were not checked for a unit signature, such as non-zero values falling on multiples of 1 or of 3.9. The criterion of unanesthetized-p14-16-values accepts "one reading of rate unit", so the outcome stands.
3. [does not affect a conclusion] **Cell 21, Student versus Welch.** The fig1ef outcome depends on the choice of t-test: Student gives 0.057, Welch 0.049. The claims file and the Methods give Student, and the variances are similar (s.d. 0.029 against 0.040), so Student is right. However, the Methods also say variances were checked "to ensure that a suitable statistical test was chosen", so the outcome is fragile. This is not a misreading in the claims file.
4. [does not affect a conclusion] **Cells 12–13, fig1d over-200 µm bin.** Only 4 of the 8 WT P14-16 mice have pairs over 200 µm, and one of those has a single pair. The non-significant third-bin result therefore rests partly on n = 4. The A-b post hoc uses all mice per bin, while the split-plot ANOVA uses the 16 mice that have all three bins; the inconsistency is minor.
5. [does not affect a conclusion] **Cell 17, pooled average.** The paper's pooled s.e.m. (0.008 and 0.009; 0.009 and 0.010 for Pearson) match the M-b s.e.m. closely (0.0088 and 0.0093; 0.0092 and 0.0107). The M-a s.e.m. are 0.024–0.030. This points to M-b, an equal-weight average of the age means, as the paper's form; under M-b both means miss tolerance. The notebook does not remark on it, but it supports the partial outcomes.
6. [does not affect a conclusion] **Cell 33, suppl4a variant.** Every P14-16 recording is cut at multiples of 720 frames, including ones that are not 2160 frames long (879, 1499, 1661, 1784 frames). Cell 6's own brightness-step ratios at frame 720k are about 1 or below for 5 of the 10 KO P14-16 recordings, so 3-min boundaries are not shown for them. The variant decides nothing.
7. [does not affect a conclusion] **Process (cell 34).** The author's summary and conclusions were left in the notebook given to the verifier.
8. **Helper functions checked on synthetic inputs, no problem found.**
   - `welch_james` with one row equals Welch's t² with Satterthwaite degrees of freedom.
   - With two rows within a genotype it equals `welch_anova` and statsmodels' `anova_oneway(use_var='unequal')`.
   - The genotype main effect has a null type-I rate of 0.048 with unequal variances.
   - `pair_corr` matches numpy Pearson, scipy Spearman and the hand-computed xcorr0.
   - Both shuffles keep each cell's mean.
   - Event edges, Q-a and Q-b are correct on a toy raster.
   - Pairs at exactly 100 or 200 µm go to the upper bin, as documented.

   Every number in the notebook comes from the loaded MAT file, whose MD5 matches `checksums.md5`. No train/test split is involved, so leakage does not apply.

### C. What I could not check

- **Rate unit.** A histogram of the non-zero rate values, or a test of whether they fall on multiples of 1 or of 3.9, would settle U-a against U-b, and with it the right threshold for R-b.
- **R-b under U-b.** Running fig2b and fig2c with `rates >= 1` would close problem 1.
- **Per-mouse P14-16 values.** The per-mouse correlations of pairs under 100 µm at P14-16 are not printed (only P30-40 are, in cell 23). Printing them would show whether one mouse drives p = 0.057.
- **Which mice differ from the paper.** The data set has one more WT P9-11 mouse and fewer mice in four other groups. There is no metadata, such as age in days, to show which mice those are, so I cannot judge how the different sample shifts the fig1d and fig1ef numbers.
- **Readings outside the claims file.** Reading T-b (correlation on filtered dF/F) cannot be run without cell contours. Cross-correlation at its peak over lags, rather than zero lag, was not run because the claims file fixes zero lag. No output shows whether it would bring the fig1d differences or the pooled means within tolerance.
