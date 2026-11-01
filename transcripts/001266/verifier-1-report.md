**Verifier report, round 1: Park, Wong-Campos et al. 2025 on DANDI:001266 (0.250710.0758)**

There are 55 claims in the claims file. Notebook outputs are cited by cell index: `reproduce_park_2025.ipynb` as [n] and `simulations_park_2025.ipynb` as [S n].

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| source-data-index | reproduced | [11]: all 83 index names are found among the 81 subject folders (84 files); the sha256 matches. |
| fig2a-dspike-dichotomy | reproduced | [18]: 8 trials with a dSpike under both filters (k=5, >300 µm) and 0 on a first spike. However, 6 of the 8 dSpikes fall on a third detected spike (see B6). |
| fig2b-bimodal-distal-amplitudes | blocked (methods_underspecified) | [20]: the readings disagree on the distal amplitudes. Dip test p = 0.96–0.99 (unimodal), while BIC prefers 2 components (Δ 55–125). The soma is unimodal under both. |
| fig2e-f-dspike-maps | not_reproduced | [22]: beyond 300 µm, the −dSpike distal/soma ratio is 0.72, above the 0.5 limit. In the 300–400 µm variant the −dSpike ratio passes (0.50) but the +dSpike ratio is 0.81–0.86, below 1. The raw variant also fails (+dSpike 0.38). |
| fig2h-length-constant | not_reproduced | [24]: λ is about 1440–1490 µm for A·exp(−x/λ) and 54–58 µm with an offset, against 255 ± 10. The raw variant gives 356–404 µm. No reading comes near. |
| fig3-subthreshold-no-dendritic-initiation | not_reproduced (weak) | [26]: at the claims settings (k=5, >300 µm), 2–3 distal events have no somatic spike in the 15 ms before them (D4 at 20.7 ms; D4+soma at 126 and 170 ms). These events were never inspected (B7), and only 1 of the 17 neurons is in the dataset. |
| fig3-two-motifs-location-independent | not_reproduced | [28]: +dSpike profile pairs with r ≥ 0.9: 0/15 normalized and 12–13/15 raw. −dSpike: 7–9/15 normalized. +dSpike exceeds −dSpike in only 88–94% of distal segments in two files. |
| fig3h-dspike-peak-distance | blocked (data_missing), partly testable | The dandiset holds the Fig. 3 neuron's soma and branch recordings: 1 neuron of 17, several regions. |
| fig3g-later-bap-ratio | blocked (data_missing), partly testable | Same single neuron. |
| figs12-bap-velocity | blocked (data_missing), partly testable | The soma file of the one neuron gives 1 velocity, which can be compared with that neuron's per-neuron value in the Source Data sheet. |
| fig3e-soma-third-bap | not_reproduced | [30]: at k=5, 2–3 second bAPs carry dSpikes. The Butterworth filter fails in every variant (2/54 on the second bAP). Only median, k=4, 300–400 µm gives 0/0/6. |
| fig3d-distal-first-bap | blocked (methods_underspecified) | [30]: file D4 is identified by its 84 bAPs at k=5. Median gives 32/54, inside 31.5–38.5; Butterworth gives 31/54, just outside. The filter readings disagree. |
| fig3f-soma-plus-distal | not_reproduced | [30]: at the claims settings, third-bAP counts are 31 and 30 (below 48.6), and 26% of second bAPs carry dSpikes. It passes only at k=4 with the author's 300–400 µm region (51, 49). At k=4 and >300 µm it gives 46. |
| fig3i-distance-dependence | blocked (metadata_insufficient) | 4 dendrite stimulations of one neuron exist, but there are no stimulus masks or positions to give distances. |
| fig3-predepolarization-rule | not_reproduced | [32]: only 44–48% of dSpikes follow ≥15 ms of distal depolarization (90% required), and 87–89% of bAPs after <15 ms fail (90% required). |
| figs13-ramp-first-spike | blocked (data_missing), partly testable | Ramp files 141936, 144133 and 145100 (soma-step-ramp) exist: 2–3 cells. |
| fig4a-step-example | reproduced | [38]: one epoch reads FDDF… under all 8 readings. |
| fig4b-dspike-window | blocked (data_missing), partly testable | 180146 (already loaded) and 175751 (opto-D2) are step recordings. |
| fig4b-few-late-dspikes | blocked (data_missing), partly testable | The 180146 sequences in [38] already give the before/after-100 ms percentages. |
| fig4ce-period-doubling | blocked (data_missing), partly testable | 174900 is 1 of the 9 cells. [40] prints its last dSpike at 14–18 ms, far from 180 ms, but the detection there is unreliable (B1, B12). |
| fig4d-example-alternation | not_reproduced (inconclusive) | [40]: 0 of 5 epochs match FF(DF)×5, and most epochs are all failures. bAP counts swing 58–160 across readings, so detection is unvalidated. |
| figs15-stochastic | not_reproduced (inconclusive) | [42]: no dSpike beyond 300 µm in any reading, and spike-time spread per position is 14–85 ms against a 2 ms limit. Whether the 20 stimuli are true repeats was not checked (B13). |
| figs14-low-rate-attenuation | blocked (data_missing), partly testable | 192452 (Cell1-patch-freq) is one patch-pulse cell. |
| figs14-high-rate-window | blocked (data_missing), partly testable | Same file. |
| figs16-ba-increases-dspikes | blocked (data_missing), partly testable | The 145801/152100 pair (BaCl₂ 150 µM): 1 of 9 cells, comparable with the per-cell Source Data. |
| figs16-4ap-increases-dspikes | blocked (data_missing), partly testable | The 171335/181403 pair. |
| figs17-ttx-decreases-dspikes | blocked (data_missing), partly testable | The 084032/090755 pair (TTX 20 nM). |
| figs17e-ttx-high-dose | not_reproduced (inconclusive) | [44]: the baseline has 0 dSpikes in 7 of 8 readings. This is because its threshold is NaN, which turns into zero dSpikes (B1), not a measured absence. |
| figs18e-ni-no-effect-on-dspikes | blocked (data_missing), partly testable | 142407, 144213 and 150422: one cell at baseline, 100 µM and 500 µM Ni²⁺. |
| figs18-ni-blocks-calcium-spikes | blocked (data_missing), partly testable | The 130550/134251 pair (wide-field ramp, Ni²⁺ 500 µM). |
| figs18g-ba-increases-calcium-spikes | reproduced (fragile) | [46]: baseline 0, Ba²⁺ 2–3.75, Ba²⁺+Ni²⁺ 0 under every claims-setting reading. Each file has its own threshold, which confounds the comparison (B9). |
| fig4f-g-model-accelerometer | not_reproduced | [S5]: the soma step gives SSSSF, not F S S F…. Wide-field gives SSSFSFSFSFSFS, with no terminal run of failures. The run used NaV 48 rather than Table 1's 47 (B15). |
| figs20-model-robustness | blocked (too_large), disputed | [S9]: about 60 min for the 154 runs of Fig. S20c (23 s each). That is feasible, so this is not a convincing too_large. |
| figs20ab-model-patch-vs-opto | reproduced | [S7]: the patch run crosses 0 mV first at apic[23] and the soma never does. The optogenetic run crosses first in the axon, then the soma at 25.35 ms, and the stimulated site never crosses. |
| figs21-izhikevich | blocked (other), disputed | A two-compartment Izhikevich `.m` script can run in Octave or be ported in a few lines. |
| fig5a-plateau-collision | not_reproduced | [50]: duration 146 ms, outside 108–132. The spike-count and single-stimulus parts pass (9–14 vs 3 spikes; 9 and 33 ms). |
| fig5b-supralinear-auc | blocked (data_missing), partly testable and should have been tested | The notebook already loads about 10 cells with optical, combined and electrical epochs (9 Fig. S22 files plus 174622) [48], and the Source Data gives per-cell values. No fig5b ratio was computed. |
| fig5d-timing-window | blocked (data_missing), partly testable | The 30 ms series of one cell (194538, 194824, 195518, 195743) is deposited. |
| fig5d-single-bap-no-plateau | blocked (methods_underspecified) | [52]: window (a) gives ratios 2.58 and 3.77 (>2); window (b) gives max 1.59 but negative denominators (ratios −2.03 and −9.90). Only 1 of 5 cells. |
| fig5ef-late-efs-no-plateau | blocked (data_missing), partly testable | 173841 (3 s ramp + EFS): 1 cell. |
| fig5gh-weak-step-equal | blocked (data_missing), partly testable | 174015 (3 s constant step + EFS): 1 cell. |
| fig6-dap5-reduces-plateau | blocked (data_missing), partly testable | The 134424/152103 pair (one cell). |
| fig6-ni-reduces-plateau | blocked (data_missing), partly testable | The 232334/233448 pair. |
| fig6-ttx-reduces-plateau | blocked (data_missing), partly testable | The 204403/211716 pair. The likely vehicle pair is 152756/153417. |
| figs24-drugs-selective | blocked (data_missing), partly testable | The same pairs give per-cell drug/baseline AUC ratios. |
| figs23-dendrite-drives-soma | not_reproduced (measure unreliable) | [54]: longest persistence 206 ms against 270–330; the difference is positive in 8 of 9 cells. One cell (160204) gets 0 ms despite a +2.7% mean difference (B8). |
| figs25-temperature | blocked (data_missing), partly testable | 123242/125334 and 181648/183952 are 2 of the 6 cells. |
| figs1-no-perturbation | blocked (data_missing) | There are no patch recordings of non-expressing neighbour cells in the archive. |
| figs2-imaging-fidelity | not_reproduced | [60]: sensitivity passes (11.7%). Noise-equivalent voltage (NEV) fails: 3.5/3.3 mV at 1 kHz against 1.2 ± 0.5, and 11.4/5.2 mV at 2 kHz against 2.5 ± 0.8. At 1 kHz there are 6 false negatives and 19 false positives. |
| figs2d-frame-rate-same-sensitivity | reproduced | [62]: paired t-test p = 0.14 (the Source Data gives p = 0.87). |
| figs3-eyfp-dosimetry | blocked (data_missing) | There are no eYFP images and no intensity series for 18 cells. |
| figs4-stimulus-localization | blocked (data_missing), partly testable | 132253 (dmd-yaxis) and 163225 (soma-488-shift-yaxis) are single examples. Whether offsets are recoverable from the DAQ is unknown. |
| figs5-focal-selectivity | blocked (data_missing), partly testable | Transverse ROI shifts can be made on any loaded bAP recording, at the cost of hand-placing branches. |
| fig1-denoising-variance | not_reproduced (reading missing) | [34]: the first 5 components hold 10–30%, against ≥86.4% required. Only a pixel-centred PCA was run (B11). |
| fig3-cheriff-current | blocked (data_missing) | There are no eYFP images or Fig. S3e calibration data in the dandiset. |

### B. Problems

1. **[affects a conclusion]** `dendrite.first_min_threshold` returns NaN in two cases: when the dSpikes outnumber the failures, and when there is no density minimum above the main mode. NaN then silently means zero dSpikes, because `distal > nan` is False and `find_peaks(height=nan)` finds nothing.
   - I checked this on synthetic data. With 20 failures and 60 dSpikes it returns NaN, while the unused `trough_threshold` gives 1.80.
   - The rule also departs from the claims file's "trough between the two modes", and the notebook does not state this as an assumption.
   - It drives the zero results for figs17e (181900), figs15 (001459, >300 µm) and the Ni²⁺ file in figs18g, and probably fig4d.
2. **[affects a conclusion]** The claims file is wrong where it says, in shared-method item (4), that the 5-robust-s.d. somatic threshold "cannot change the outcome". In [13], k=5 finds 150 bAPs where the legend has 167 and 170, which shifts the bAP order. That changes fig3e and fig3f. The notebook ran k=4 as a variant, which is right.
3. **[affects a conclusion]** Trunk tracing (`trace_trunk`), cells [3], [15]: the author says the traced line leaves the trunk beyond about 400 µm. The claims-setting region (>300 µm) still includes those segments, so background is averaged into the "distal" region. No overlay image or coordinates validate the ROI. This affects fig2e-f, fig2h, fig3-two-motifs and fig3f, and the plateau files (>200 µm, trunk to 656 µm) as well.
4. **[affects a conclusion]** The notebook's summary table in [0] marks about 30 claims "blocked, pooled samples not deposited". The archive holds single-cell examples for most of them (file list in A). Most notably, fig5b's inputs are already loaded in [48] and never analysed.
5. **[affects a conclusion]** Both blocked simulation claims are blocked on weak grounds (figs20 and figs21; see the table).
6. **[does not affect a conclusion]** In fig2a [18], 6 of 8 dSpikes sit on order 2 (a third spike), and 9 trials have 3 spikes. The paper says two spikes per trial with the dSpike on the second. A dSpike echo may be counted as a somatic spike, or a distal peak more than 5 ms late may be assigned to a later spike. This was not investigated.
7. **[affects a conclusion]** fig3-subthreshold [26]: the orphan distal events were never plotted. The D4 one disappears at k=4, which points to a missed somatic spike.
8. **[affects a conclusion]** figs23 [54] has two problems:
   - Persistence is the first frame that comes back within 2 s.d. of baseline. That is noise-sensitive and gives 0.0 ms for 160204, whose mean difference is +2.7%.
   - The "largest plateau" region landed at 88–146 µm in 6 of 9 cells, which is proximal rather than distal dendrite.
9. **[affects a conclusion]** figs18g `ca_spikes` [46]: the thresholds differ about 2× between files of the same cell (1.60% baseline against 0.74% Ba²⁺), and the "time above threshold" duration reading depends on that threshold directly. The Ni²⁺ file's threshold is NaN under the median readings. A single shared threshold, as [44] uses for TTX, was not run.
10. **[affects a conclusion]** fig5d-single `auc` [52]: reading (b) gives negative optical and EFS areas (−0.041, −0.013), so the ratios are undefined. In reading (a) the denominators are tiny (0.007–0.015), which inflates the ratios.
11. **[affects a conclusion]** fig1 `pca_share` [34]: it subtracts the across-pixel mean waveform, which removes the shared signal, and it runs on unbinned shot-noise pixels. The paper's ">96% of the variance in the recordings" more plausibly means an uncentred SVD of pixel waveforms. That reading was not run.
12. **[affects a conclusion]** Somatic detection is unstable in the wide-field and ramp files ([36]: 174900 gives 58–160 bAPs, 181900 gives 18–62, 001459 gives 71–132). Nothing validates it, yet fig4d, figs15 and figs17e rest on it.
13. **[affects a conclusion]** figs15 [42] treats the 20 stimuli as repeats without checking that the 488 nm amplitude is equal across them.
14. **[affects a conclusion]** figs2 `patch_measures` [60] has three weaknesses:
    - Electrical spikes are 0 mV crossings at least 3 ms apart. That gives impossible maximum rates (333 and 263 Hz), and the total of 2265 against the paper's 2212 suggests false electrical spikes, which inflate the optical false negatives and false positives.
    - NEV reading (a) uses the first second of the recording, where bleaching is fastest.
    - The ROI is the top 20% of pixels, unweighted. Maximum-likelihood weighting, which the claims allow, was not run, and the NEV result may hinge on it.
15. **[affects a conclusion]** fig4f-g [S1–S5]: the criterion says Table 1 parameters (NaV 47). The run used `parameters_list.py` (48) under NEURON 9, and with only 85 and 100 ms runs. The NaV 47 run was not done.
16. **[does not affect a conclusion]** fig2h [24] drops fits with λ > 5000 µm (36–45 of 109 spikes) and fits only to 400 µm, both the author's choices. Every reading is far from 255 µm anyway.
17. **[does not affect a conclusion]** The Fig. S8a (80/12) and S8c-d (85/11) panels match neither file D1 (102/10) nor file D2 (98/9) [13], and the notebook leaves this unaddressed.
18. **[does not affect a conclusion]** fig2b [20] measures high-passed amplitudes rather than −dF/F at the peak.
19. **[does not affect a conclusion]** The clock check [7] fails for 184232. 0.65 µm/pixel is assumed from the Methods and never verified against the data.

### C. What I could not check, and the output that would settle it

- **ROI validity:** a mean image per file with the traced trunk, the soma disk and the 200/300/400 µm marks.
- **Thresholds:** a distal-amplitude histogram with the KDE and threshold for each file, especially 181900, 184232, 001459 and 174900. Also the counts of dSpikes rejected by the FWHM rule against the height rule.
- **fig3-subthreshold:** traces around each orphan distal event, soma and distal together.
- **figs15:** the 488 nm modulation amplitude per stimulus in 001459.
- **figs23 and fig5d-single:** the dendrite−soma difference traces with the 2 s.d. band, and the cumulative-AUC curves per epoch.
- **fig4f-g:** a run with Table 1's NaV 47 and longer step durations.
- **fig1:** the uncentred PCA share.
- **figs2:** NEV with maximum-likelihood weighting, and electrical spike rates after a refractory check.
- **Blocked claims:** fig5b ratios for the about 10 loaded plateau cells, compared with the Source Data, plus the single-cell tests listed in A.
- **Not seen by me:** the Source Data index rows themselves (I did not download the xlsx), and any figure image beyond its printed value range.
