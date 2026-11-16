**A. Outcomes** (31 claims, taken from the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| model-amplification-increases | blocked (other: not attempted) | Nothing was run; cell 0 says only "network simulations… blocked". The claims file sets `data: elsewhere` and gives a criterion that can be run (see B1). |
| model-equal-connectivity-ablation-increases | blocked (other) | As above. |
| model-increased-connectivity-ablation-decreases | blocked (other) | As above. |
| model-all-or-none-robust | blocked (other) | As above. |
| model-more-ablation-larger-decline | blocked (other) | As above. |
| model-slow-input-sensitive | blocked (other) | As above. |
| model-response-similarity | blocked (other) | As above. |
| neurons-per-mouse | reproduced | Cell 12: 8126.3 ± 2435.6, and all 16 per-mouse counts equal Extended Data Table 1. The raw-count variant (8188.5 ± 2340.3) is also within tolerance. |
| representation-sizes | reproduced | Cell 14, reading (a): touch 900.6 ± 538.8 (fraction 0.108) and whisking 864.6 ± 364.4 (0.106). All four values are within tolerance. |
| touch-ablation-size | partially_reproduced | Cell 16: 16.78 ± 12.77 neurons and 5.85% are within tolerance. The percentile (70.3 ± 35.0) uses a rule that differs from the criterion's "rank" (B2), so the criterion's percentile was never computed. |
| touch-ablation-reduces-touch | reproduced | Cell 20: 0.123 → 0.100, signed-rank p = 0.004, decline in 9 of 9 mice. 7,121 neurons were analysed against the paper's 8,392; the count is only reported, and 8,392 equals the sum of the score > 0.1 counts. |
| touch-ablation-touch-count | reproduced | Cell 20, reading (a): 932.4 → 715.8 with ablated neurons kept, 918.3 → 712.6 with them left out. Both are within tolerance. |
| touch-ablation-whisking-unchanged | reproduced | Cell 22: p = 0.820, 0.116 → 0.115, counts 775.0 → 721.2. |
| whisking-ablation-size | partially_reproduced | Cell 16: 12.71 ± 5.68 neurons pass. 4.43% is outside 4 ± 0.4; the tolerance was set on the paper's rounded "approximately 4%", and 12.7/287 is 4.43%. The percentiles (68.8 ± 36.2; variant 65.9 ± 36.5) carry the same rule issue as touch (B2). |
| whisking-ablation-no-effect-touch | reproduced | Cell 24: p = 0.109 (≥ 0.05), counts 838.0 → 898.9. The paper's 0.095 is explained by its zero-filled matrix (cell 30: 0.112 → 0.096). |
| whisking-ablation-no-effect-whisking | reproduced | Cell 25: p = 0.938 with the Methods cylinder and 0.812 with the code's. |
| silent-ablation-size | reproduced | Cell 16: 16.25 ± 2.55. 118 of the 130 ablated neurons were below 0.025 Hz (maximum 0.079 Hz), which is reported as the criterion asks. |
| silent-ablation-no-effect-touch | reproduced | Cell 27: p = 0.383. |
| silent-ablation-no-effect-whisking | reproduced | Cell 28: p = 0.844, counts 960.5 → 904.4. |
| ablation-type-specificity | reproduced | Cell 32: Rtouch p = 0.002, 0.031, 0.152; Rwhisking p = 0.743, 0.837, 0.955. Every test falls on the side the criterion requires. |
| ablation-size-correlation | reproduced | Cell 34: R = −0.790 over all 24 ablations (p = 4e-6) and −0.761 over the 9 touch ablations (p = 0.017). Both are within tolerance. |
| distance-dependence-touch | reproduced | Cell 36, reading (a): proximal −0.133, distal −0.056, p = 0.012, λ = 87.3 µm. Reading (b) fails (p = 0.359); the criterion needs only one reading. |
| distance-dependence-whisking-absent | reproduced | Cell 36, per-mouse means: p = 0.164 (Methods cylinder) and 0.129 (code's). Proximal −0.004 / +0.000 and distal −0.023 are within tolerance. |
| behaviour-unchanged | not_reproduced | Cell 38, with the paired signed-rank test the legend names: silent-ablation fraction correct p = 0.008 and whisking-ablation touches per trial p = 0.047. The sample KS tests give p < 0.05 in 23–24 of 24 ablations. The criterion allows neither. The code's rank-sum variant gives the paper's exact P values, so the paper probably used that test. |
| response-similarity-touch-ablation | not_reproduced | Cell 40, main reading: touch slopes 7 of 9 negative, sign test p = 0.180, not < 0.05. Whisking slopes 1 of 9 negative, p = 0.039, not ≥ 0.05. The paper's numbers (p = 0.039 / 0.508, 2,768 / 1,085 neurons) come out only with the code's right-trials-only average plus the code's cylinder. |
| response-similarity-example | not_reproduced (narrow) | Cell 42: slope of the Methods fit is −0.393, just outside −0.44 ± 0.044 (limit −0.396). It falls within only under the code's right-trials-only average (−0.433 / −0.426). |
| response-similarity-whisking-ablation | reproduced | Cell 40, main reading: touch p = 1.000, whisking p = 0.688. Only 6 of the 7 mice enter (B4). |
| ablation-no-off-target-event-rate | reproduced | Cell 45: 0.0141 → 0.0140 Hz, p = 0.0547, 1,035 neurons (1,028 with the code's cylinder, as in the paper). |
| ablation-success-rate | reproduced | Cell 47: 320/474 = 0.675; 300 successes leaving out the two named mice, against 293 ± 29. |
| glial-reaction-local | blocked (data_missing) | Confirmed against the archive: filelist.txt and the S3 listing hold only the 16 `an*.tar.gz`, docs and checksums. The members listed in cell 4 are session, log and curation `.mat` files, with no histology. |
| per-mouse-table | partially_reproduced | Cell 49: with the Methods cylinder (main reading) 23 of 24 rows match; 275801 touch gives ΔRtouch −0.071 against −0.065. With the code's cylinder 24 of 24 match. |

**B. Problems**

1. **[affects a conclusion]** Cell 0: the seven model claims are marked blocked without one of the allowed reasons. The Methods give every LIF parameter (τ, ΔV ± 50%, τexc/τinh, tref, delays, connection probabilities, PSPs, input waveform, background rates, dt, 20 s runs). The claims file supplies readings for the parameters the paper leaves open (input strength under readings a–c, reset pulse, slow-input strength). The simulations could have been run; the scale is about 30 networks × a few conditions.
2. **[affects a conclusion]** Cell 16, `pct`: when no included neuron scores above an ablated neuron (or its score is NaN), the percentile comes out as 1/N, about 0, instead of 1. The cell's markdown says "(1 when none exceeds it)", which misdescribes this. A synthetic check confirms it: with 100 members, a score above them all gives 0.01. This probably copies ablation_summ_stats.m, which would explain the exact 70 ± 35 match. But the claims file defines the percentile as a rank, and that rule was never run. This affects touch-ablation-size and whisking-ablation-size.
3. **[does not affect a conclusion]** `behaviour`: fraction correct takes `trial_type_counts[:2]` over `[:4]` and assumes the trial-type order without printing `trial_type_str`. The rank-sum P values match the paper exactly, so the order is probably right.
4. **[does not affect a conclusion]** `trial_avgs` / cell 43: the pre directory of 278939 for its whisking ablation (postablate_silent) has no trial-averaged dF/F (cell 3). That mouse therefore enters with 0 neurons, and the whisking-ablation similarity analysis has 6 mice, not the paper's 7. The notebook never states this.
5. **[does not affect a conclusion]** `bursts`: the 50 ms merge rule is an assumption, and it is stated. It bears only on touches per trial, and the whisking-ablation paired p = 0.047 sits at the threshold. The silent fraction-correct failure (p = 0.008) does not depend on it.
6. **[does not affect a conclusion]** `reduce_sess`: `theta_at_touch` and `kappa_at_touch` take `[0::2]` of the event-property values, assuming one value per event edge. Their lengths are never checked against `touch_on`. That "kappaMaxAbsOverTouch" is the "net curvature change at touch" is assumed, not checked.
7. **[does not affect a conclusion]** Cells 20–28: the adjusted MADs come out about half the paper's ± values (for example 0.011 / 0.016 against 0.021 / 0.037), and the notebook does not comment. A different MAD definition in the paper (MATLAB's `mad` defaults to the mean absolute deviation) is a likely cause, but this was not checked.
8. **[does not affect a conclusion]** `targets_and_successes`: the criterion defines targets as the logged attempts, but the notebook takes them from the curation-file lists. The 510 NYU attempt logs are never reconciled with the 279 NYU targets.
9. **[does not affect a conclusion]** `trial_avgs` cuts 75-frame trial averages to 70 frames without naming the files. `rejects_by_shuffle` never rejects neurons with a NaN event rate (8 of them).
10. **[does not affect a conclusion]** Claims-file readings that the outputs contradict:
    - The Extended Data Table 1 touch and whisking counts equal the analysed members (union of pre and post, code's cylinder: 21 and 22 of 24 rows equal). They follow neither reading (a) nor (b).
    - The "neurons" figures in the text (8,392, 6,975, 5,866, 6,161, 7,110, 7,684) are sums of the score > 0.1 pre counts, not the analysed neurons. Their tolerances therefore test the wrong quantity.
    - The paper's whisking and silent grand medians are artefacts of its pooled 24-row matrix (cell 30).
    - The behaviour P values come from an unpaired rank-sum test, not the paired test the legend names.
    - The Fig. 3 numbers come from the right-trials-only bug.
11. **[does not affect a conclusion]** Cell 32: touch against whisking gives p = 0.031 against the paper's 0.042 under both cylinders, unexplained. The likely cause is a rank swap: 278937 whisking is −0.003 here against −0.006 in the table, and 257220 touch is −0.005 against −0.004.

**C. Not checked**

- **Extended Data Table 1 transcription (cell 12):** no PDF renderer was available. Only the means of the 16 first rows (779.6 touch, 623.7 whisking) were checked, and they agree with the claims file.
- **Percentile under the claims-file rank rule:** needs, per ablation type, that percentile and the number of ablated neurons that score above all members or have a NaN score.
- **Trial-type order:** printing `trial_type_str` for one file of each format would settle B3.
- **Touch-property lengths:** lengths of `theta_at_touch` and `kappa_at_touch` against `touch_on` per file, and the list of property keys, would settle B6.
- **Missing trial averages for 278939:** the feature keys of the 278939 postablate_silent files would show whether the averages exist under another name.
- **Full list of "other" archive members:** the cell 4 output is cut off, so I could not fully rule out histology inside the archives. The archive-level listing holds none.
- **Model claims:** there are no outputs to check.
- **Analysis code:** the MATLAB code (ablation_summ_stats.m, ranksum, mad) is not in my materials, so the code-based choices (B2, B7, B11) could not be confirmed against it.
