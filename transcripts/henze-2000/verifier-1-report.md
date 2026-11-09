**A. Outcomes** (21 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| sample-cells | not_reproduced | Cell 17: 21 tetrode folders against 33 ± 3.3. The kept count (21) and pyramidal count (21) are within tolerance, but no tetrode interneuron is labelled (0 against 1). The criterion's partial outcome needs the total too. Every tetrode folder passes the −55 mV rule, so the deposit looks like a curated subset. The paper's Fig. 6A labels a cell D107 that has no folder in the archive. |
| fig1c-start-end-timing | not_reproduced | Cell 21: 0 of 16 readings put both means in tolerance. The start lead runs from −0.17 to +0.16 ms against 0.01 ± 0.02. This uses 8 somatic cells, not the paper's 11, and the cell set is doubtful (problem 1). |
| ap-duration-match | reproduced | Cell 23: 6 of 16 readings have both means in tolerance, e.g. spont/a/a/thr gives 1.45 and 1.20 ms. The extracellular duration SD (0.48 to 0.61) is much wider than the paper's 0.19. |
| duration-correlation | partially_reproduced | Cell 25: 4 readings give positive R with P < 0.03, but R is 0.76 to 0.94, outside 0.594 to 0.726. The one in-tolerance R (0.644) has P = 0.085. All spontaneous-spike readings are non-significant. |
| neg-peak-precedes-intra-peak | reproduced | Cell 27: 0.207 ± 0.094 ms with all spikes, 0.208 with spontaneous spikes (n = 8). The result holds on every channel. Adding the probable missed somatic cells (latencies 0.20 to 0.31) would not move it out of tolerance. |
| fig1c-derivative-mismatch | reproduced | Cell 29: reading (a) holds in 6/8 (all) and 5/8 (spont) cells, reading (b) in 7/8. |
| notch-and-ahp-landmarks | not_reproduced | Cell 32: the notch agrees in at most 4 of 9 to 11 cells that have one, and the slope change in at most 1 of 20, at every prominence and window. |
| fig2-interneuron-narrow | blocked (metadata_insufficient) | The only labelled interneuron is d17212, a silicon-probe cell. None of the tetrode folders carries a cell type, and Fig. 6A does not label the basket cell. |
| fig3b-latency-vs-amplitude | reproduced | Cell 34: Pearson r is about −0.70 (P ≤ 0.0006) and Spearman about −0.55 (P ≤ 0.016). The dendritic median latency (0.28 to 0.30 ms) exceeds the somatic one (0.20). This holds under all 8 readings and survives the site reassignment in problem 1. |
| fig3a-example-pair | not_reproduced | Cell 37: d11221→d11222 gives 0.25 / 0.975 ms against 0.28 / 0.55, and d13521→d13522 gives 0.21 / 0.245. Fig. 6A labels D11221 and D11222 as cells used in other figures, which supports this pairing. The 0.975 ms value is suspect (problem 3). |
| fig3c-backprop-velocity | not_reproduced | Cell 39: 0 of 24 readings fall within 1.61 ± 0.161 m/s. Fits give 0.23 to 0.49 m/s. Points read from the paper's own Fig. 3C give a similar slope (about 0.5 m/s), so the paper's 1.61 m/s probably comes from a computation the paper does not describe. |
| fig4bc-burst-attenuation | partially_reproduced | Cell 43: all parts hold in 9 of 17 tetrode cells under one reading (a/·/b), a majority by one cell. It is lost at ≥20 trains (6/13) and when silicon-probe cells are included (10/24), and it returns at ≥50 trains (5/8). The amplitude parts hold robustly (12/17). |
| fig4d-amplitude-correlation | partially_reproduced | Cell 45: the two in-tolerance rows (d12821 O6a 0.431, d15121 O6a 0.367) rest on a biased per-spike threshold (problem 2). Under the unbiased O6 b, positive R with P < 0.0001 is 0.33 to 0.76, all outside 0.36 to 0.44. |
| fig5-theta-smaller-spikes | blocked (data_missing) | Confirmed from the bucket listing: only anesthetized `Data/d*.zip`, docs and software; no behaving-animal recordings. |
| theta-higher-rates | blocked (data_missing) | Same as fig5. |
| fig6-amplitude-vs-distance | blocked (data_missing) | No histological distances in the files or the spreadsheet. Fig. 6A reads off distances for only 4 data-set cells (D53, D11221, D11222, D81), far short of 19. |
| tetrode-cell-count-estimate | blocked (data_missing) | The radii depend on fig6. The arithmetic itself checks: πr²h × 300,000/mm³ gives 141.4 (r = 50 µm), 1108.4 (r = 140 µm) and 12.7 displaced (r = 15 µm). The notebook did not report this. |
| silent-cells-inference | blocked (other) | An interpretation; nothing in the data set bears on it. |
| fig7-vertical-spread | not_reproduced | Cell 47: both parts hold in 3 of 10 cells (1 of 4 with a listed order). Amplitude and slopes fall in 9/10, but the spike reaches ≥100 µm in only 3. |
| propagation-velocity-range | not_reproduced (reading a only) | Cell 49: 2 to 3 of 10 pyramidal cells fall in range. Three cells with clean troughs give earlier negative peaks away from the soma site, and the rest are slower than 0.36 m/s even taking absolute delays. Reading (b), which the n = 25 and n = 6 imply, is blocked (data_missing). |
| fig8-neighbouring-shanks | blocked (data_missing) | Behaving-animal recordings are not in the archive. |

**B. Problems**

1. [affects a conclusion] Cells 15 and 19, `cell_row` (somatic/dendritic split). Somatic requires peak ≥ 0 mV and the author's own fast-AHP test, on potentials that are not offset-corrected. The spreadsheet has an `offset(mV)` column with values up to 39 mV, which is ignored. The result is 8 somatic and 13 dendritic cells against the paper's 11 and 9.
   - The paper's Fig. 1 legend identifies its somatic example as D53 (d5331, n = 849 spikes, which matches file d533101's 878). The notebook calls d5331 dendritic (peak −7.6 mV).
   - Five more cells (d12821, d13522, d5611, d8131, d15121) have amplitudes of 44 to 60 mV, inside the paper's somatic range in Fig. 3B, and peaks between −8.4 and +6.5 mV.
   - None of the timing claims was rerun on an alternative somatic set. Outcomes at risk: fig1c-start-end-timing, duration-correlation, ap-duration-match, fig1c-derivative-mismatch.
2. [affects a conclusion] `hc1.per_spike_ic`: the threshold is set only when dV/dt > 10 V/s on the last sample before the peak. Otherwise it is NaN. On synthetic APs at 10 and 20 kHz it returns NaN for every spike. In real data it keeps a slope-selected subset (d12821: 95 of 438 spikes). Both of fig4d's in-tolerance rows come from this subset.
3. [affects a conclusion] `hc1.ec_measures` and `per_spike_ec`: the negative-peak search window is fixed at −1 to +0.6 ms from the intracellular peak.
   - A synthetic trough at −1.1 ms is returned at −1.0, and one at −1.3 ms at +0.6.
   - Dendritic cells sit at this edge: d11222 has t_neg ≈ −0.97 with the trace already 187 µV below baseline at −1 ms; d17111, d15712 and d18911 have site t_neg exactly −1.0.
   - The fig3a dendritic latency and the fig7 and propagation measures for 4 of 10 probe cells are therefore unreliable. The fig3b and fig3c outcomes do not depend on it.
4. [affects a conclusion] Cells 41 and 43: the train selection (≥10 trains reaching a 5th AP, tetrode only) is the author's own. The criterion's accommodating trains with a first ISI of about 10 ms are not checked. The majority flips with the threshold and electrode set, so I scored fig4bc partial.
5. [does not affect a conclusion] `hc1.scales`: the 1000× extracellular gain is never checked. The spreadsheet `gains` column reads "4@5k" and "6@5k". Fig. 6A amplitudes (D53 about 85 µV, D11221 about 72 µV) are 5 to 6 times smaller than the notebook's (506 and 398 µV). No tested outcome uses µV thresholds.
6. [does not affect a conclusion] Cell 32: the slope change uses local maxima of d2 only, where the criterion says "local extreme". The AHP minimum often sits at the edge of its 5 ms window or of the grid (7.5 ms).
7. [does not affect a conclusion] Cell 39, reading v_c: this is a mean of ratios with negative distances and near-zero or negative excess latencies, so it is unstable (0.79 to 2.46 m/s).
8. [does not affect a conclusion] `hc1.ec_channels`: d6811's README lists EC channels 2, 3 and 5, but the code uses 2 to 5. d13521's README gives 10 kHz and the xml 20 kHz; the xml value was used without comment. The d1392101/02 pair overlaps at 0.54 and both files are kept.
9. [does not affect a conclusion] Cell 47: the markdown promises a smoothness check of the assumed six-channel order, and none is computed. The printed profiles are smooth, which supports the assumption. d15712's listed order gives alternating-sign amplitudes and looks wrong.
10. [does not affect a conclusion] Cells 0 and 50: the summary table lists propagation-velocity-range as tested, and the closing cell lists it among the blocked claims.

**C. What I could not check**

- The d11222 and dendritic probe waveforms. A plot of the averaged extracellular traces over −3 to +3 ms for d11222, d17111 and d18911 would have settled problem 3.
- The timing claims on the paper's likely somatic set. A rerun of cells 19 to 29 with somatic defined by fast AHP only, or with d5331, d8131 and the other 44 to 60 mV cells added, would show whether fig1c-start-end-timing and duration-correlation change.
- fig4d with a corrected per-spike threshold, that is, the first dV/dt > 10 V/s point searched back from the maximum rate of rise.
- fig4bc with the criterion's selection. Per-cell step amplitude, duration and first ISI would have let me apply it.
- Whether the intracellular scale holds for the tetrode cells. Only 2 of the 21 are in the spreadsheet, so the 50× assumption is untested for them.
