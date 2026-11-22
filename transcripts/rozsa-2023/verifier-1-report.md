**Verifier report, round 1: Rozsa et al. 2023 on DANDI:000341 0.241220.1312**

The claims file has 31 claims. The two notebooks test 19 of them (7 in the induction notebook, 12 in the slices notebook) and treat 12 as blocked. Cell references below are `ind[n]` for the induction notebook and `sl[n]` for the slices notebook.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1ab-raf-patterns | not_reproduced | The best reading matches 2 of 8 values (ind[9], RA-APs including interstimulus intervals, epoch reading ii). The continuous-only reading, which the criterion names, gets 0 or 1 of 8. Both RAF patterns occur. The RA-AP set is suspect (problems 1 to 3). |
| fig1c-ra-lower-threshold-slope | reproduced | Under reading (c), human RA-APs have lower median threshold (−59.8 vs −44.2 mV persistent, −61.2 vs −44.5 sporadic) and lower slope, with P≈0. The per-cell variant agrees (P = 0.002 and 3e-16) (ind[11]). This depends on problem 5. |
| fig1d-human-raf-proportion | not_reproduced | 0.547 (continuous only), 0.528 (reading b) and 0.984 (with interstimulus intervals) against 0.226 ± 0.023 (ind[13]). |
| fig1f-human-raf-ngfc | blocked (metadata_insufficient) | The archive's asset metadata has no cell class. The notebook searched only `pharmacology` keys for one (ind[5]). |
| figs1b-rat-raf-proportion | not_reproduced | 0.746 to 0.975 against 0.394 ± 0.039 (ind[13]). |
| figs1d-rat-raf-values | not_reproduced | At most 1 of 4 values matches under any reading (ind[16]). |
| fig1g-rat-raf-ngfc | blocked (metadata_insufficient) | Same as fig1f. |
| fig1hk-bleb-initiation-order | not_reproduced (unreliable) | NGFC 220504: AIS-AP latency is negative (−0.22 ms at threshold). NGFC 220505-2: no RA-APs (sl[16]). The classification rests on somatic thresholds of −14 to −29 mV (problem 6). |
| fig2c-zd7288-reduces-raf | not_reproduced | RAF duration rises under ZD7288 (mean 131.6 → 360.5 s, 1 of 7 cells decreasing). The RA-AP count change has paired t P = 0.83 (sl[10]). Epoch reading (ii) was not run (problem 9). |
| figs2-zd7288-passive-properties | not_reproduced | Input resistance 146 → 141 MΩ (median), P = 0.78. Only the 2 resting potential values are within tolerance (sl[13]). |
| fig2e-sag-species | partially_reproduced | Human is higher, Mann-Whitney P = 1.5e-26. The medians miss under every reading: human 0.198 to 0.248 against 0.15, rat 0.071 to 0.083 against 0.04 (ind[19]). |
| fig2e-sag-raf-smaller | not_reproduced (incomplete) | Under the one RAF reading run: human P = 0.8 (301 RAF cells against 11 without); rat 0.062 vs 0.125, P = 0.0028, which is above 0.001 (ind[20]). Two other allowed RAF readings were not run (problem 8). |
| fig2h-bleb-sag-higher | partially_reproduced | Bleb higher, two-sample t P = 0.0082 (most hyperpolarizing step, formula a). Soma 0.024 and bleb 0.115 against 0.1 and 0.4. Distance median 106 µm matches (sl[18]). Problem 7 applies. |
| fig2il-kcl-induces-ra-aps | blocked (data_missing) | No folder, keyword or session description in the archive mentions KCl or potassium (my scan of all 787 assets). Absence inside the files is unverified (part C). |
| fig3-human-ap-states | partially_reproduced | With the pre-AP potential: 10 of 11 cells have all AIS-APs in up states, and 11 of 21 RA-AP cells have RA-APs in down or transition states (sl[21]). The criterion's partial rule (one exception) is met. Counts are 11 and 21 against exact 7 and 6. The mixture's "RA" class has the steeper slope (problem 4). |
| fig3f-human-pre-ap-fluctuation | partially_reproduced | AIS-APs higher, pooled P = 7e-9 (window to threshold) and 1e-11 (window to peak). Medians 6.42/3.78 and 7.35/5.64 mV against 1.49/0.78 (sl[23]). Among isolated APs, RA-APs are higher. |
| fig3i-rat-lfp-rhythm | reproduced | Spectral peak median 1.06 Hz (36 recordings) or 1.19 Hz (30); cycle rate 1.01 or 1.03 Hz. All are within 1.1 ± 0.11 (sl[28]). Weakly diagnostic (problem 12). |
| fig3l-rat-spontaneous-ra-proportion | not_reproduced | 30 of 36 or 24 of 30 cells have RA-APs, against 13 ± 1.3 (sl[30]). |
| fig3k-rat-pre-ap-fluctuation | reproduced (fragile) | Window to peak: AIS 9.90 > RA 8.76 mV, P = 1e-33. Window to threshold gives RA higher (7.97 > 7.70). Per-cell P = 0.22 (sl[32]). Problem 11 applies. |
| fig3m-rat-ais-phase-coupling | partially_reproduced | Carbachol + SCH23390 only: angle 321° (within 31.4° of 314), P = 5e-14, but vector length 0.508 against 0.093. All modulator files: angle 245° fails (sl[35]). n = 111 APs from 7 cells or 2476 from 12, against 534 from 22. Problem 10 applies. |
| fig3m-rat-ra-no-phase | not_reproduced | Rayleigh P = 2.7e-186 (all) and 9.3e-145 (modulators only), against the criterion P ≥ 0.05 (sl[36]). |
| figs3-no-modulators | blocked (data_missing) | The folder holds 2 of the paper's 90 recordings (sl[38]). Their 0.05 Hz "peak" is the lower edge of the band, so no peak was found. The criterion applied mechanically would give partially_reproduced on 2 cells. |
| fig4b-invivo-ra-proportion | not tested; block not justified | Marked too_large (383 GB). The same pipeline read 260 GB of induction files in 66 min (ind[1]). The largest in vivo file is 7.2 GB and the median is 1.15 GB (API). |
| fig4i-invivo-frequencies | not tested; block not justified | As fig4b. |
| fig4g-invivo-ra-share | not tested; block not justified | As fig4b. |
| fig4f-invivo-pre-ap-fluctuation | not tested; block not justified | As fig4b. |
| fig4j-invivo-ais-phase-coupling | not tested; block not justified | As fig4b. Asset keywords list LFP. |
| fig4j-invivo-ra-no-phase | not tested; block not justified | As fig4b. |
| fig4-invivo-up-down-balance | not tested; block not justified | As fig4b. |
| figs4i-ais-ra-frequency-correlation | not tested; block not justified | As fig4b. |
| figs5-not-genotype-or-anesthesia | blocked (metadata_insufficient at archive level) | Asset metadata has no genotype or anesthesia field. Whether the files carry them was never checked. |

### B. Problems

1. **[affects a conclusion]** `raf.ra_aps_induction` and `extract` (reading c). An AP counts as an RA-AP when its current at threshold is ≤ 5 pA relative to the holding current at the start of the sweep. So APs driven by a steady depolarizing holding current, and all spontaneous APs after the first induction sweep, become RA-APs. The holding current is never summarized for the induction files, and spontaneous firing before induction is never measured as a baseline. 98% of human cells end up "with RAF". This inflates fig1d, figs1b, fig1ab, figs1d and fig2e-sag-raf-smaller.
2. **[affects a conclusion]** ind[5]. The induction folders contain files bathed in in vivo-like ACSF ("Calcium" in 96 files) and active-slice modulators (carbachol in 60, SCH23390 in 58), plus TTX, 4-AP, Cd, TEA and others. None are excluded. Spontaneous AIS-APs in active slices count as RA-APs under reading (c). The same drug fields also show where the missing no-modulator recordings for figs3 might sit; this was not checked.
3. **[affects a conclusion]** `raf.gmm_classes` (reading b). The features are z-scored with means and SDs taken over all APs, and the AP table includes artefacts (threshold −1033 to 240 mV, peak up to 1030 mV, ind[5]). On synthetic data, 0.5% outliers take a whole component, and that component becomes "RA". In human induction data, the "RA" component has the higher median threshold (−38.9 vs −45.3 mV) and the steeper slope (9.4 vs 1.9 mV/ms), the opposite of RA-APs. Reading (b) results in ind[7] to ind[16] are not meaningful.
4. **[affects a conclusion]** sl[20], sl[25] and sl[16]. The mixture's RA component is never checked against the paper's description of RA-APs (lower threshold and lower slope). In human active slices, "RA" has the higher slope (3.72 vs 2.58). In rat active slices, "RA" is 84% of APs, while the paper reports 76 RA-APs against 534 AIS-APs. This affects fig3-human-ap-states, fig3f, fig3k, fig3l and both fig3m claims.
5. **[affects a conclusion]** `raf._ap_table`. The threshold is found by walking back from the steepest point to the first sample of the run above 5 mV/ms, so one noise dip stops the walk early. Synthetic test at 100 kHz with 0.2 mV noise: threshold +5 mV too high, slope 2.7× too high. At 20 kHz the bias is negligible. The files mix 5 to 200 kHz (ind[5]). Sampling rate is never compared between AIS-AP and RA-AP sweeps, so part of the fig1c difference and the mixture features may come from sampling rate.
6. **[affects a conclusion]** sl[15] and sl[16], `bleb_latency`. Somatic AIS-AP thresholds are −14 to −29 mV in human and +17 mV in rat. These are implausible and were not examined; possible causes are an unbalanced bridge during current injection or problem 5. Soma and bleb sweeps are paired by index (1319 soma sweeps against 641 bleb sweeps) and not by start time, and the pairing was never checked.
7. **[affects a conclusion]** sl[18]. The most hyperpolarizing steps are −700 to −950 pA, and sweep minima reach −434 mV. Bleb electrode artefact or bridge error was not examined. The variant using the bleb trace during a somatic step, which the claims file names, was not run. Two rat files are the same cell with two blebs, so its somatic value enters the two-sample test twice.
8. **[affects a conclusion]** ind[18] and ind[20]. RAF status for fig2e-sag-raf-smaller uses only reading (c) with interstimulus intervals (301 cells with RAF, 11 without). The criterion allows readings (a) to (c), but the continuous-only split (168 of 307) and reading (b) were not run, and they could change the human result.
9. **[affects a conclusion]** sl[9], `split_raf`. Only epoch reading (i) was run, one epoch spanning a whole period that contains several hundred induction sweeps. The criterion ("as in fig1ab") allows reading (ii), per induction run. One human file is 20 µM, not 30 µM, and is kept.
10. **[affects a conclusion]** sl[7]. The clock check finds no LFP–spike correlation at lag 0 (mean −0.05), no better than at shifts of 2 to 10 s. Alignment of the Vm and LFP clocks is therefore unverified, yet both fig3m claims and fig3i's synchronization rest on it.
11. **[affects a conclusion]** sl[23], `sd_compare`. The "window to peak" SD includes the AP's own upstroke and any preceding spikes, which explains SDs of 6 to 10 mV against the paper's ~1 mV. fig3k is reproduced only under this reading. The claims file allows the reading; I report it here and do not correct it.
12. **[does not affect a conclusion]** sl[27]. 14 of 39 spectral "peaks" sit at the 0.5 Hz band edge. The cycle rate of a 0.5 to 4 Hz band-passed signal is close to 1 Hz by construction, so fig3i's match is weak evidence.
13. **[affects a conclusion]** sl[25]. The variant meant to drop APs fired under steady current removes nothing (18808 of 18808 APs remain), because currents are measured relative to the holding current. The paper says RA-APs were absent during steady-current periods in 16 cells.
14. **[does not affect a conclusion]** `raf.paper_test`. For non-normal paired data it uses a Wilcoxon test, where the paper's rule gives Mann-Whitney U. The ZD7288 runs used the paired t test anyway.
15. **[affects a conclusion]** sl[0]. The in vivo block (too_large) is contradicted by the notebook's own throughput (problem-free reading of 260 GB in 66 min). All 9 in vivo claims could be tested, at least on a subset of files.

### C. What I could not check, and the output that would have let me

- **Holding current and spontaneous firing.** Not shown for the induction files. Needed: a per-file table of holding current in continuous sweeps, and the rate of APs without current before the first induction sweep.
- **Drug-treated and active-slice files in the induction folders.** Needed: RAF proportions and sag results recomputed without drug and in vivo-like ACSF files, and the drug fields for the rat files listing Calcium (possible figs3 recordings).
- **Mixture behaviour.** Needed: component means, SDs and weights, the result with the artefact APs (threshold outside −80 to −10 mV) removed first, and threshold/slope scatter plots per preparation.
- **Sampling-rate confound.** Needed: AIS-AP and RA-AP threshold and slope broken down by sampling rate, or a fixed resample to 50 kHz.
- **Bleb recordings.** Needed: example soma and bleb traces with detected thresholds marked, start times of the paired sweeps, and step traces with the sag components marked.
- **Vm/LFP alignment.** Needed: the starting times of Vm and LFP series side by side, and an AP-triggered LFP average.
- **Cell class, KCl, genotype and anesthesia inside the files.** Asset-level metadata on the archive has none of these, and I did not open the files. Needed: a dump of all `general/*`, `subject/*` and electrode description fields for one file from each folder, including `In_vivo`.
- **Missing readings.** Needed: fig2e-sag-raf-smaller under continuous-only and reading (b) RAF status; fig2c under epoch reading (ii); fig2h with the bleb trace during a somatic step.
