**Verifier report, round 1: Tingley et al. 2021 (doi:10.1038/s41586-021-03811-w) on DANDI:000233 v0.250624.0414**

The claims file holds 35 claims. My outcomes: 7 reproduced, 3 partially reproduced, 5 not reproduced, 20 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig2-ripple-rate-predicts-glucose | reproduced | Cell 18: mean R holds in every combination (Spearman −0.21, Pearson −0.18). The lag holds in 3 of 16 combinations, all with the −100..+100 lag range (e.g. raw/Pearson/per rat: R −0.176, lag 14.2 min). 18 rats, not 30. Fragile: see B1. |
| fig2ef-correlation-beyond-shuffle | reproduced | Cell 22: observed median R at +10 min is −0.076 (Pearson) and −0.106 (Spearman), against a shuffled median of about 0.00. KS p = 1.5e-4 and 4.0e-6. |
| fig2g-clustered-ripples | reproduced | Cell 24, reading (a), more than 150 SPW-Rs per epoch: −0.191 nA against +0.050 nA after isolated epochs, 3.9 times the magnitude. Reading (b) fails (−0.032). No test is required; Welch p = 0.059, and the curve is not monotonic. |
| edfig4-ripple-features | partially_reproduced | Cell 26, deciles: interval > duration > frequency > amplitude, so interval is largest but the rest of the order differs. With 5-percentile bins duration comes first (0.0967 against 0.0966). The margins are within noise (B7). |
| fig2h-phase-reset | not_reproduced | Cell 28: all 4 readings fail. Spearman rho is −0.24 (p = 0.51) or 0.55 (p = 0.098). |
| edfig5-cross-frequency-coupling | partially_reproduced | Cell 30: power-power paired t-test p = 9.5e-5 and Rayleigh p = 1.4e-13. The comodulogram peak is on the diagonal (glucose 51.9 min, SPW-R 51.9 min), and the means above and below the diagonal are equal (0.082). The claimed asymmetry is absent. |
| edfig1-glucose-rhythm | not_reproduced | Cell 32: the residual peaks at 51.4 min (tolerance 54–66). The first side peak of the autocorrelogram is at 70 min. The residual is negative at 15–21 min, so power is not elevated across 15–90 min. |
| edfig1-glucose-circadian-meals | not_reproduced | Circadian part, cell 34: ANOVA p = 0.986. The meal part is blocked (data_missing, no meal times). |
| edfig1-sensor-decay | reproduced | Cell 36: current slope is negative in 31 of 31 placements. The relative slope of \|delta\| is smaller in 18 of 31; median −0.047 against −0.107 per day. |
| supp-ripple-rate | reproduced | Cell 38, reading (a): 10.19 per minute and 14,671 per day, both within tolerance; maximum 258 per minute. CGM1 alone falls outside tolerance (10.76 per minute). |
| supp-ripples-stable-across-days | reproduced | Cell 40: amplitude is consistent in 15 of 15 rats under the criterion's "or". Only 5 of 15 stay within 20% (B14). |
| edfig3-ripple-rate-rhythms | partially_reproduced | Cell 42: there are local peaks at 24.0 h and 3.8 h. Hours are 1,889.8, against 1,568.5 ± 156.9. The largest peaks are at 42.3 h and 19.5 h (B13). |
| edfig2-refractory-period | not_reproduced | Cell 44: the shortest interval is 28.8–39.2 ms in all 22 rats, and 0 of 22 fall in 18–22 ms. Only one reading was run (B5). |
| edfig3e-ca1-firing-decrease | blocked (data_missing) | There are no units tables (cell 4), and the archive's variableMeasured lists no Units. |
| edfig4-fasting-fed | blocked (data_missing) | No meal times. |
| edfig4-nrem-wake | reproduced | Cell 46: no test gives p < 0.05 (blocks p = 0.057; paired p = 0.27; transitions p = 0.15 and 0.23). Only 3 of the paper's 8 rats, so the test of absence has little power. |
| edfig4-no-hour-differs | not_reproduced | Cell 48: smallest Student's t-test p = 0.010, with 10 of 276 pairs below 0.05. The paper gives a minimum P of 0.53. |
| edfig6-ripple-rate-best-predictor | blocked (too_large, contested) | Not attempted; see B3. |
| edfig6d-pairwise-predictors | blocked (too_large, contested) | Same as above. |
| edfig6ef-latent-variables | blocked (too_large, contested) | Same as above. |
| fig3d, fig3-induced-effect-size, fig3ef, fig3f, edfig7ab, edfig7jm, edfig7-ppc | blocked (data_missing) | No stimulation times. The archive's variableMeasured has no optogenetic series, and no subject metadata names opto or PPC rats. |
| edfig8-lateral-septum-rectified | blocked (data_missing) | No units. |
| edfig9-dorsal-ventral | blocked (data_missing) | Only Vanessa has ventral SPW-Rs with glucose, on 2 days. The rate-correlation part can be tested: r = 0.13, 0.44 and 0.83 in 3 rats. In Vanessa the per-day dorsal R is positive (0.115, 0.239), the opposite of the main claim. |
| fig4-cno-controls-no-change, fig4-ls-dreadd-decouples, fig4-ls-dreadd-chance-level, fig4e-dreadd-time-course, fig4c-medial-septum-no-effect | blocked (metadata_insufficient) | DREADD recordings may be in the files, but subject metadata has no genotype or cohort. Session descriptions say only "Consult Supplementary Table 1" or "no description". That table has no subject names, and there are no CNO, vehicle or injection labels. |
| edfig10-expression-correlates-effect | blocked (metadata_insufficient; scores data_missing) | As above. The histology scores exist only in the figure. |

### B. Problems

1. **[affects a conclusion]** fig2 (cells 18–19). The lag match is fragile.
   - It holds in only 1 of 16 combinations once rats with less than 6 h are dropped. CGM48 has 2.25 h of data and peaks at −40 min.
   - Per-rat lag s.d. is 30–42 min, against the paper's ±4.5. The mean lag in tolerance comes from averaging peaks at −40 and −30 min with peaks at +55 to +65 min. My median of the per-rat lags is about 7.5 min.
   - "R negative in most rats" holds by construction, since R is the minimum over 41 offsets.
   - The outcome also depends on the author's assumption about how a bin's count pairs with its glucose change. Under "delta to the next reading", all four −100..+100 combinations pass; under "rate after the reading", none do. The variants are shown.
2. **[does not affect a conclusion]** fig2 selection (cells 14, 16). Reading (a) excludes CNO days and stimulation periods. The notebook uses every day of every rat, because nothing is labelled, and does not say so.
3. **[affects a conclusion]** edfig6 blocks (cells 51–53).
   - The timing printed is 4.3 h of LFP plus 1.6 h of accelerometer reading, about 6 h serial. The markdown says "about 9 h".
   - The 0.5 h limit is the notebook's own, and the reading was not parallelized, although `read_all` already uses 16 processes.
   - A subset matching the paper's 8 rats was not tried. Three claims are left untested on a weak basis.
4. **[affects a conclusion]** edfig1-glucose-rhythm (cell 32). Only a log-log fit over all frequencies was run; the legend says "linear best fit" and does not give the axes. The mean residual is flat from about 40 to 60 min (1.36–1.46), so the peak could move into 54–66 min under linear axes, another fit range or another segment length. The autocorrelogram's first trough at 30 min fits a period of about 60 min, but the criterion does not use troughs.
5. **[affects a conclusion]** edfig2 (cell 44).
   - Only peak-to-peak intervals were run. The legend does not name the time point, and the stored tables have start and stop times, so start-to-start and stop-to-start were possible.
   - All 22 rats show a floor of about 29–39 ms and zero counts below 20 ms. That pattern suggests an event-merging rule in the detection that made the stored tables, not physiology. This was not checked.
   - Minor claims-file misreading: the legend shows "auto-correlograms of all inter-ripple intervals", not a histogram. The minimum interval is the same either way.
6. **[affects a conclusion]** edfig5 (cell 30).
   - `rate_f = rate.fillna(mean)` fills SPW-R rate across glucose-only stretches. "18 rats with a run of at least 24 h" therefore includes CGM48 (2.25 h of SPW-Rs) and CGM49 (6 h). Constant stretches and their edges enter the envelopes.
   - The Rayleigh test pools 20,017 autocorrelated 5-min bins, so its p is anti-conservative.
   - 20 shuffles were used instead of 100; this is stated.
7. **[does not affect a conclusion]** edfig4-ripple-features (cell 26). The range-of-bin-means measure has no uncertainty, and events sharing a 5-min bin share one delta value. The most clustered decile has the least negative delta (+0.004 against −0.027), which is the opposite direction to Fig. 2g. Per rat, amplitude has the largest range most often (7 of 18 rats).
8. **[does not affect a conclusion]** edfig4-no-hour-differs (cell 48). `np.nansum` turns a rat-hour with no valid correlation into 0 instead of NaN. With 276 uncorrected pairs, 10 below 0.05 is fewer than chance alone would give, so the not-reproduced outcome reflects the criterion's design as much as the data. The hourly R is strongest at 17–22 h, consistent with the paper's "slightly larger during the dark period".
9. **[affects a conclusion; claims-file criterion]** edfig1-circadian (cell 34). The ANOVA runs on per-rat hourly means of absolute current, without removing between-rat offsets or sensor decay. Hourly means run from 28.6 nA (06:00–07:00) to 31.3 nA (20:00). A within-rat test was not shown.
10. **[does not affect a conclusion]** Date repair (`repaired_glucose`, cells 12–13).
    - The repair is inferred from the data, not documented in the dataset.
    - The rule leaves CGM32 with readings dated up to 2021-12-02, so its 1–12 February dates are still swapped. The archive file list shows no CGM32 ephys files for 1–12 February, so the SPW-R analyses are unaffected.
    - The repair changes R at +10 min in CGM39 (−0.123 repaired against +0.012 as stored) and CGM58 (−0.021 against −0.117).
11. **[does not affect a conclusion]** `highpass` (cell 17). Subtracting a 24-h running mean before differencing hardly changes delta, so reading (b) repeats reading (a).
12. **[does not affect a conclusion]** fig2h (cell 28). Taking the minimum over 7 offsets against a single baseline value biases the decrease upward. The claim fails anyway.
13. **[does not affect a conclusion]** edfig3 (cell 42). On a 400-point grid of a noisy Lomb-Scargle spectrum, a "local peak within ±10%" almost always exists. The prominence of the 3.8-h peak is not reported.
14. **[does not affect a conclusion]** supp-ripples-stable (cell 40). Spearman over 3–5 days rarely reaches p < 0.05, so the "or" makes the criterion close to automatic. In CGM30 the overall median `peak_amplitude` is 0, which gives an infinite deviation.

I ran the helpers on synthetic data: `binned`, `lagged_pairs`/`xcorr` (lag sign: a planted +10-min effect is recovered at +10), `coverage`, `circular_shuffle` and `swap_day_month`. All behave correctly. I found no train/test leakage, since no models were fitted.

### C. Not checked

- **Whether the files hold condition data in groups the reader skips.** `read_file` does not look at `/intervals`, `/stimulus`, `general/optogenetics` or the electrode and channel names of `ElectricalSeriesRaw`, which might include a TTL or stimulation channel. It prints `experiment_description` cut to 40 characters. Needed output: the full HDF5 path list per subject and the full description strings.
- **Detector parameters.** The Methods say these are stored with each session's ripple events; the notebook does not print the tables' attributes. They would settle B5 and the per-subject thresholds.
- **Clock alignment of glucose and ephys within a day.** There is no independent check.
- **Details behind B1, B6, B8 and B13:**
  - which fig2 combination passes with at least 6 h per rat, with per-rat lags;
  - per-rat hours of real (unfilled) SPW-R data in the edfig5 runs;
  - the count of empty rat-hours in edfig4-no-hour;
  - the prominence of the 3.8-h peak.
- **The edfig1 rhythm under a linear-axes fit** (B4).
- **The figures.** I read only the text outputs; I did not view the plotted images.
