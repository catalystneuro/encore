**Verifier report, round 1: Quattrocolo & Maccaferri 2013, CRCNS hc-9**

The claims file holds 26 claims. The notebook tests one (fig7a-olm-sag) and marks the other 25 blocked for missing data. I listed the archive myself: the bucket's `filelist.txt` and `checksums.md5` hold only the two description documents and `Maccaferri_data.zip`. The notebook's zip listing (cell 3) shows three ATF files of O-LM current steps and nothing else.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| fig7a-olm-sag | reproduced | Cell 14 measures the -100 pA step. Reading (a) finds a sag in 3 of 3 cells: 8.0 to 17.6 mV, or 44 to 94 baseline SD against a threshold of 2. Reading (b) also finds 3 of 3, with sag ratios 0.21 to 0.45 against a threshold of 0.1. Both readings agree, and every variant in cell 16 (end window, smoothing) gives 3 of 3 at the criterion's thresholds. The peak hyperpolarization comes 88 to 126 ms after step onset, which fits a real sag and not a noise minimum. |
| fig1-spontaneous-amplitude | blocked (data_missing) | No Cajal-Retzius recordings in the archive (archive listing, cell 3). |
| fig4-upsc-amplitude | blocked (data_missing) | No paired recordings in the archive. |
| fig4-upsc-kinetics | blocked (data_missing) | Same as above. |
| paired-presynaptic-neurogliaform | blocked (data_missing) | No reconstructions or pair records in the archive. |
| upsc-gabazine-block | blocked (data_missing) | No paired recordings in the archive. |
| fig5-no-gabab-component | blocked (data_missing) | No paired recordings in the archive. |
| fig6-spontaneous-larger-than-unitary | blocked (data_missing) | No Cajal-Retzius recordings in the archive. |
| fig6-spontaneous-faster-than-unitary | blocked (data_missing) | Same as above. |
| fig7-chr2-olm-light-firing | blocked (data_missing) | 24October2012_C2 is likely one of the nine ChR2 cells, but its file has only the current-step protocol: the signals are "2CC mV" and "AO #1" (cell 4). There is no light channel and no voltage-clamp record, so no part of the claim can be tested. |
| fig8-light-evoked-psc | blocked (data_missing) | No Cajal-Retzius recordings in the archive. |
| fig9-opsc-rise-time | blocked (data_missing) | Same as above. |
| fig9-opsc-amplitude-decay | blocked (data_missing) | Same as above. |
| fig10-dhpg-increases-frequency | blocked (data_missing) | Same as above. |
| fig10-dhpg-amplitude-unchanged | blocked (data_missing) | Same as above. |
| fig10-reduced-slice-no-effect | blocked (data_missing) | Same as above. |
| fig11-slm-inhibition | blocked (data_missing) | No cell-attached recordings in the archive. |
| fig11-slm-inhibition-gabazine | blocked (data_missing) | Same as above. |
| fig11-slm-excitation | blocked (data_missing) | Same as above. |
| fig11d-baseline-frequency-dichotomy | blocked (data_missing) | Same as above. |
| gabazine-baseline-firing | blocked (data_missing) | Same as above. |
| fig12a-slow-conductance-depolarized | blocked (data_missing) | No dynamic-clamp recordings in the archive. |
| fig12a-slow-conductance-hyperpolarized | blocked (data_missing) | Same as above. |
| fig12b-fast-conductance-depolarized | blocked (data_missing) | Same as above. |
| fig12b-fast-conductance-hyperpolarized | blocked (data_missing) | Same as above. |
| no-age-dependence | blocked (data_missing) | The claim concerns synaptic events in Cajal-Retzius cells. Three O-LM cells cannot test it. |

The archive check confirms every block. None of the 25 blocked claims can be tested even in part.

**B. Problems**

1. [does not affect a conclusion] `hc9.sag_measures`, reading (a): taking V_min as the raw minimum during the step biases the test toward finding a sag. I made a synthetic trace with no sag (a 40 mV exponential hyperpolarization plus 0.2 mV Gaussian noise). Its "sag" came out at 4.0 baseline SD, which passes the 2 SD threshold. With the 1 ms running mean the same trace gives 0.7 SD, correctly no sag. On the real cells the margins are 22 to 47 times the threshold, and the smoothed variant in cell 16 agrees, so the outcome holds. As written, though, the 2 SD test cannot discriminate near threshold.
2. [does not affect a conclusion] Cells 8, 9 and 14 take the mapping of files to Figure 7 panels (A versus D) from the superseded `hc-9/old/` description, matched by age and mouse line. The files themselves carry no age, line or panel. The criterion judges every cell alike, so the mapping does not change the outcome.
3. [does not affect a conclusion] Cell 18: as the criterion directs, the "similar firing pattern" of the 7D cell is judged only by the sag. The +50 pA firing table (15, 15 and 18 spikes; first ISI 49 to 59 ms) is shown but not assessed. That follows the claims file, so it is not an error by the author.
4. [does not affect a conclusion] Cells 6 and 7: the data set description gives the current steps as -100:30:+250 pA, but the data have 25 pA increments. It also says the step starts about 0.5 s into the sweep, but the step starts at 75 ms. The notebook found and reported both. The claims-file header repeats "30 pA increments" from the description. That is a misstatement of the data description, not of the paper.
5. [does not affect a conclusion] Units and step timing check out: s, mV and pA from the ATF header; voltage leaves baseline 0.1 to 4 ms after step onset; the shifted-window control in cell 12 holds. All numbers in cell 14 come from the loaded data. There is no train/test split or statistical test, so leakage and statistics do not apply.

I found no place where the claims file misreads the paper for the tested claim. The Figure 7A and 7D legends ("-100/50 pA", "Notice the presence of a sag", "Notice the similarity") match the claim.

**C. What I could not check**

- I could not visually compare the deposited traces with the printed Figure 7A and 7D traces. The notebook's plot (cell 19) is not set against the figure, and I did not view the PDF image. A zoomed plot of the first 300 ms of the -100 pA step per cell, next to a crop of Figure 7, would settle that the files are the figure's cells.
- I could not measure the noise floor of reading (a) on these recordings. Running `sag_measures` on each cell's 0 pA sweep, which is present as sweep 5, would show the false-positive level of the raw-minimum measure on real noise.
- I did not re-run anything on the real data. My synthetic test covered only `sag_measures`; `parse_atf` and `step_table` I checked only through the notebook's outputs.
