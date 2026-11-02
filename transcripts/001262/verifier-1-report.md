**A. Outcomes** (23 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| table1-animals-units | reproduced | Cell 13: 60 (32) / 13 (7) / 31 (11) animals, 759 / 87 / 314 units, totals 104 and 1160. All eleven counts match exactly. |
| table1-age-abr-weight | reproduced | Cell 15: all 9 means are within tolerance (5.55 / 22.49 / 38.33 months; 18.10 / 34.17 / 49.03 dB; 74.61 / 83.35 / 86.41 g). The SDs and ranges also match Table 1. |
| table1-bf-range | reproduced | Cell 17: 428–15825, 350–15091 and 620–15762 Hz, an exact match for all three groups. |
| fig3-abr-age | reproduced | Cell 19: the mean rises 18.1 < 34.2 < 49.0, and the old group has the largest SD (18.0). Old range is 20–85 dB SPL. |
| females-fewer-in-old | reproduced | Cell 21: 11/31 (0.355) is below one half and below young adults (0.533). |
| oxygen-78 | reproduced | Cell 23: 78 yes, 26 no. |
| complex-stimuli-experiments | reproduced | Cell 25: 21 / 5 / 17 experiments. |
| recording-type-counts | partially_reproduced | Cell 27: 5 of 6 counts match under both readings. CLICK is 271 (reading 1; 272 with the 5 ms delay) or 275 (reading 2), against 261. |
| fig7-sampling-by-age | reproduced | Cell 29: no middle-aged unit has SR, SPS or CVC, and SPS is young-only (22). |
| isi-exclusion | not_reproduced | Cell 31: units fail under every reading: (a) 370, (b) 391, (c) 148 of 1160. The criterion gives not_reproduced when all readings fail. 140 units still fail even with a 0.3 ms limit. |
| no-prepotentials | blocked (methods_underspecified) | The check was visual and has no rule (claims file). |
| rlf-monotonic | blocked (methods_underspecified) | The check was visual and has no rule. Cell 34 gives the description only: 249 of 952 recordings have a drop larger than the SD. |
| fig5b-example | reproduced | Cell 36: BF 7620 Hz, threshold 19.0 dB SPL. The BF recording is at 30 dB with 5 repetitions; the RLF has 10 repetitions with levels 10–79 dB (40 dB included). |
| fig6a-young-two-sensitive-regions | reproduced | Cell 38, reading (b): the highest mean between the sensitive regions is 27.6 dB in the bin plotted at 3.48 kHz, with neighbours at 25.4 and 24.4 dB. Reading (a) fails (36.7 dB at 0.72 kHz, n=3), but the criterion needs only one reading. |
| fig6b-young-bf-gap | not_reproduced | Cell 40: the 2423–2936 Hz bin has 34 units, tied with 1363 and 2000 Hz, with neighbours 34 and 35. Neither reading (a) (minimum of the span is 1) nor reading (b) (local minimum) holds. |
| fig6c-sr-distributions | reproduced | Cell 42: the low-BF modes are 0–5 (27) and 55–60 (21), separated by a bin of 5. The high-BF largest local maximum is 0–5 (66), below 18 spikes/s. |
| fig6d-max-phase-locking-bf | reproduced | Cell 44: the highest young BF with p<0.001 is 4598 Hz, against 4.6 kHz. |
| fig6d-highest-vs-low-bf-low-sr | reproduced | Cell 46: readings (a) and (b) both hold for young adults and for all ages. The top unit has BF 428 Hz and SR 1.25; the low-BF/low-SR median is the highest. |
| fig7a-cf-matches-bf | reproduced | Cell 48 (n=114): Pearson r=0.973, p=2e-73. Median CF/BF is 1.003 (95% CI of log2: −0.011 to 0.040). |
| fig7b-click-latency-bf | reproduced | Cell 50: Pearson −0.882 and Spearman −0.864 (n=268), both p≪0.05. Both stay negative with the 5 ms delay (−0.662, −0.820). |
| fig7ab-representative-sampling | not_reproduced | Cell 52: no reading holds for both CF and CLICK. The CF subset fails both the KS test (p=0.018 and 0.003) and the median rule (ratio 0.75). CLICK passes KS but its median ratio is 1.13. |
| old-success-rate | blocked (data_missing) | The denominators are animals operated on without success. I checked the archive: 1160 NWB files only, from 104 subjects that all have units, and the description mentions no unsuccessful experiments. No part can be tested; only the numerators are in the data. |
| psth-primary-like | blocked (methods_underspecified) | The check was visual and has no rule. The spike times needed are in the files, but no criterion can be fixed from the paper. |

For the three visual-check claims, the archive holds the inputs (the voltage traces in `acquisition`, and the spike times). The block comes from the missing rule, not from missing data. No selection here has a chance level stated in the paper.

**B. Problems**

1. **[affects a conclusion]** Cell 27 and `click_latency_2bins` (recording-type-counts). The CLICK count, the only mismatch, rests on latencies recomputed with an assumed click delay of 7.75 ms. The notebook never checks this delay against the data, for example with a CLICK PSTH split by trial length.
   - Some CLICK trials last only 10 ms, which would leave 2.25 ms after a click at 7.75 ms. Yet the reported maximum latency is 2.78 ms.
   - The notebook reads `click_polarity` but never uses it.
   - It does not check whether the 500-trial CLICK recordings (96 units) are two original recordings merged during conversion to NWB. `check_dataset_units.m` would drop units with more than one CLICK recording, which could explain 261 against 271/275.
   - So partially_reproduced may reflect the conversion or the recomputation rather than the data. The fig7b result does not depend on the delay.
2. **[does not affect a conclusion]** `cf_from_cf_recording(level_from="tag")`. Taking levels from the nominal ABI in the tag rather than the calibrated `level` column is the author's choice, and the notebook never shows the other reading. The recomputed CF is also only the automatic first pass. Given r=0.973, median ratio 1.003 and an exact count of 119, this is unlikely to matter for fig7a or table1-bf-range.
3. **[does not affect a conclusion]** Cell 38. Reading (b) defines the two sensitive regions as the minima below and above 3.48 kHz, which assumes the answer. I checked the printed bin means: the two lowest overall (20.9 at 1.73 kHz, 21.2 at 8.34 kHz) are the same bins, so the result stands.
4. **[does not affect a conclusion]** Cell 31. 1171 of the short ISIs are below 0.1 ms (about 2–5 samples at 48.8 kHz) and may be double detections of one spike rather than evidence of multi-unit recordings. The notebook does not inspect them. Even with a 0.3 ms limit, 140 units fail, and with a 0.1 ms limit, 5 units still fail, so not_reproduced holds. The paper says such units were met "only rarely", against 370 of 1160 here.
5. **[does not affect a conclusion]** Cells 6–7, `abr_decoded`. Reading the ABR threshold as a character's code point is an assumption. The exact match of all three means, SDs and ranges to Table 1 supports it strongly.
6. **[does not affect a conclusion]** `local_maxima` in cell 42 also lets the last bin count as a maximum, which the criterion does not provide. It has no effect on the reported modes.
7. **[does not affect a conclusion]** In `vs_calc`, p is NaN when N ≤ 50, following the code, while the Methods say N < 50. Only the N=50 edge case differs.
8. **[does not affect a conclusion]** Claims file, fig7ab. The KS test and the 10% median rule are the file's own tests, not the paper's (the checker noted this). With these tests, the outcome depends on CLICK's median ratio of 1.13, just outside the 10% bound. This is not a misreading of the paper.

I found no place where the claims file misreads the paper. Its age groups agree with the paper's <12, 12–36 and >36 months, and the bin edges follow the cited code.

Synthetic tests of the helper all behaved as specified: `vs_calc` (locked spikes give vs=1; the N=50 cutoff), `short_isis`, `age_group` boundaries, `weight_g`, `abr_decoded`, `cf_from_cf_recording` (V-shaped tuning gives the right CF under both level readings) and `click_latency_2bins`. The click latency shifts by a constant with the delay and becomes NaN when the delay is after the response.

**C. What I could not check, and the output that would have let me**

- **What the NWB analysis table holds.** I could not confirm that it lacks the CF, vector strength, p-value and click latencies. A printed list of the `analysis_table` columns for one file would settle it.
- **The click onset.** A population PSTH of the CLICK trials, split by 10 ms and 20 ms trial length, would settle it. Also missing: `click_polarity` counts per recording, trial counts per CLICK recording against the original recordings, and latencies by trial length.
- **The effect of the CF level source.** The notebook would need fig7a and the CF count rerun with `level_from="level"`.
- **Whether the very short ISIs are artefacts.** A histogram of ISIs from 0 to 0.6 ms in 0.02 ms bins, and the spike waveforms around sub-0.1 ms pairs, would show this.
- **The figures.** I could not compare the plots with the paper's Figs. 3, 6 and 7 (images not inspected). The fig6b bin counts per age group, and with BF from CF added, would show whether the paper's histogram used another population.
