I didn't reproduce the paper's ECAP latencies, velocities or threshold order. The colonic-pressure result is also not reproduced, and neither are the awake ECAP latencies. The six Table 1 values and the comparison with published values are reproduced, and impedance is partially reproduced. One claim (fig2c-p3-above-p1) passes its criterion only narrowly. The claims file lists 31 claims, and the notebook's status table names the same 31: 13 tested and 18 blocked. I see no place where the claims file misreads the paper.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| anes-ecap-recorded | reproduced | Cell 31: under both artefact-end readings, all 5 rats have a peak passing 0.05 µV that is below it at the lowest current. Top-current peaks are 0.15–15.7 µV. The files have no 0 mA trace, so the lowest current (17.5 µA, or 106.5 µA in 12-007) stands in for 0 mA. |
| anes-ecap-latencies | not_reproduced | Cell 33: 0 of 72 combinations have all three latencies within 10%. P2 is always about 2.1–3.0 ms against 3.48 ms. This rests on the notebook's own peak-identification rule (problem 1). |
| anes-conduction-velocity | not_reproduced | Cell 35: 0 of 216 combinations. Follows from the latencies. |
| anes-threshold-order | not_reproduced | Cell 37: 0 of 96 combinations have rising central values with Friedman P < 0.05; none is within tolerance. The lowest is P = 0.105 (n = 4). |
| fig2c-p3-above-p1 | reproduced (weak) | Cell 41: unadjusted Dunn P3 vs P1 gives P = 0.0339 with P3 higher (paper: 0.034), meeting the criterion's reading (a). Only 4 of 48 readings pass and 0 after Bonferroni. In those same readings the omnibus Friedman P is 0.105 and n = 4, not 5. |
| fig2ab-one-rat-p2-below-p1 | not_reproduced | Cell 43: 0 of 48 readings give 4 rats with P1 lowest plus 1 rat with P1 above P2. |
| awake-ecap-latencies | not_reproduced | Cell 45: three peaks are found in at most 5 of 7 recordings (12-057 never has any), so "three peaks in every rat at both weeks" fails. 0 of 216 rows have all six values within tolerance. |
| awake-threshold-increase | blocked (metadata_insufficient) | I agree. The archive's animal_subject metadata (checked via the API) has no link between the day-0 and day-7 IDs, and every Friedman reading needs rat as block. |
| impedance-increase | partially_reproduced | Cell 49: the pzfx gives 4.192 ± 0.166, 7.245 ± 0.793 and 12.044 ± 1.149 kΩ. These match the paper to rounding (the printed spread is the SEM), and so do the ranges. There is no 8-week value: the archive has no impedance file for 15-759 or 15-760. The notebook lists this claim as plain "tested". |
| electrode-failures | blocked (data_missing) | I agree for 40 electrodes. A subset is testable: of the 32 CSV electrodes, R18-273 E3 reads 252 kΩ on three dates 14–16 days after surgery (an open), and nothing looks like a short (cell 51). The notebook did not state this as a partial result. |
| colonic-pressure | not_reproduced | Cells 53 and 55: 3 of 3 rats respond under reading (a), 1 of 3 under (b). The one (b) responder, 12-020, has 1.44 ± 0.70 mmHg; under the shifted-time variant it is 15-758 with 0.64 ± 0.09. Neither is within 2.6 ± 0.1, and no rat has 13 trains. |
| no-fecal-expulsion-or-erection | blocked (data_missing) | Confirmed from the archive file list (91 files): there are no observation notes. |
| table1-minimum-pressure | reproduced | Cell 60: 11.74 mmHg, inside 7.4–13.2 under every reading. |
| table1-threshold-pressure | reproduced | Cell 62: 6.96, inside 4.7–8.4. |
| table1-peak-pressure | reproduced | Cell 64: 46.59, inside 39.5–63.0. |
| table1-contraction-duration | reproduced | Cell 66: 32.19 (a1), 26.06 (a2), 30.30 (pooled), all inside 17.1–37.5. |
| table1-intervoid-interval | reproduced | Cell 68: 6.66, inside 5.9–9.4. |
| table1-hfpo-frequency | reproduced | Cell 70: 9.82, inside 8.3–13.0, but from 7 rats, not 9 (12-081 and 12-083 have no HFPO values). |
| table1-comparable-to-published | reproduced | Cell 72: all 4 CIs overlap the Wiedmann CIs, under both a1 and a2. |
| stim-evoked-voiding | blocked (data_missing) | Agree for the full claim: only 4 of the 8 stimulated 18-* rats have trains. A partial test was possible (problem 6). Cell 74 already shows a marked void within 30 s of train onset in all 4 rats (4 of 9 trains). |
| stim-void-trials | blocked (data_missing) | Agree: only 9 trains are deposited, against the paper's 27 trials. |
| stim-early-void | blocked (data_missing) | Agree for the full claim. A partial test on 4 rats from the /Voids times was possible. |
| stim-nonvoiding | blocked (data_missing) | Mostly agree, but the criterion's reading (a) uses pressure alone and could have been run for the 4 rats with trains. |
| stim-voiding-to-nonvoiding | blocked (data_missing) | Agree. Only 18-294 has more than 2 trains. |
| fig3e-eight-week-responses | blocked (data_missing) | Confirmed: there is no stimulation or stimuli file for 15-759 or 15-760. The "parameters similar" half could be tested from their /Voids tables. |
| fig4-atf3-rare | blocked (data_missing) | Confirmed from the archive file list: no histology images. |
| fig4ef-axons-intact | blocked (data_missing) | Same as above. |
| fig5-cfos-distribution | blocked (data_missing) | Confirmed: the README promises a c-Fos summary, but no such file exists. |
| fig5-cfos-no-side-difference | blocked (data_missing) | Same as above. |
| fig5-no-lamina1 | blocked (data_missing) | Same as above. |
| macroscopic-no-pathology | blocked (data_missing) | Confirmed: no post-mortem notes. |

**B. Problems**

1. **[affects a conclusion]** `pelvic.find_peaks_maxcurrent`, cells 29 and 45. P1–P3 are taken as the first three positive maxima at the top current, with prominence above k×noise. This is the notebook's own assumption (it is stated), and it is the only identification rule run; k = 2, 3 and 5 are variants of the same rule. The paper's P2 and P3 centres are only 0.29 ms apart and their ranges overlap, so how peaks are assigned decides all six ECAP outcomes. Other rules were not tried, for example the three largest peaks, or matching to the paper's latency windows.
2. **[affects a conclusion]** `thresholds` and `amp_at`, cells 37 and 47. The paper's 0.05 µV pass level sits inside the noise in 8 of 12 files (SD 0.2–0.7 µV, cell 6).
   - In a synthetic test, band-passed noise of 0.2 µV SD passes the two-recording test 65% of the time (0% at 0.02 µV).
   - That is why thresholds land on the lowest current (17.5 µA) or on 0 µA in the awake files.
   - The not_reproduced outcomes therefore reflect noise. They still follow the criterion.
   - The 3×noise variant (cell 39) was never put through the Friedman test. By hand, its 4 rats give χ² = 6.5, P = 0.039, and Dunn P3 vs P1 P = 0.013. Its medians are 107/498/691 µA, still outside tolerance.
3. **[affects a conclusion]** fig2c, cell 41. The pass rests on dropping 12-008, which has only two peaks at k = 3. With all 5 rats (k = 2), Dunn P is 0.11. The Friedman test in the passing readings is not significant.
4. **[does not affect a conclusion]** Cell 31. The criterion's "absent at 0 mA" is replaced by the lowest current in the file without saying so as an assumption. In 12-007 that current is 106.5 µA.
5. **[does not affect a conclusion]** `latencies_at`, reading (b). It takes the first current at or above the largest first-pass threshold. Because pass sequences are noisy and not monotone, all three peaks need not pass at that current.
6. **[affects a conclusion: blocked versus partial]** Cells 73–74 and 17. Several stimulation claims were declared blocked without trying what the data allow:
   - Stim-nonvoiding reading (a) uses pressure alone.
   - /Voids marks voids near the trains in the 4 rats that have them.
   - Both would give partial tests on 4 of 8 rats.
   - The notebook never shows whether /Voids means urine release (from `hdf5_cystometry_schema.json`).
7. **[does not affect a conclusion]** Table 1 cells 57–70 use the authors' derivative table.
   - Its values do not equal Table 1 (minimum 11.74 vs 10.3; inter-void interval 6.66 vs 7.6).
   - Its peak pressure matches the primary /Voids table in only 4 of 27 cycles (cell 15).
   - The criterion's definitional readings (threshold at onset vs at urine release; the two duration definitions; the two HFPO methods) were not recomputed from the pressure traces.
   - The outcomes hold under the derivative's definitions, but which criterion reading those definitions match is unverified.
8. **[does not affect a conclusion]** Colonic-pressure reading (a), peak minus the pre-train mean, is biased upward. In cell 53 the null mean (5.48) is about the same as the observed mean (5.68) in 12-019, so "3 of 3 respond" under (a) is an artefact of the measure. The response rule ignores the null. This choice comes from the claims file.
9. **[does not affect a conclusion]** Cell 3 does not print the `pool_id` or `experimental log file name` columns of subjects.xlsx. These might link the day-0 and day-7 chronic files, so the awake-threshold block is not fully shown from the data. The public metadata record has no such link.
10. **[does not affect a conclusion]** The impedance pzfx has 12 values per stage before implantation and on day 1, not "38 electrodes in 10 arrays". It matches the paper anyway; the notebook does not comment on the n mismatch.

**C. What I could not check, and the output that would settle it**

- **Time origin of the ECAP traces.** Whether `StartTime` = 0.6 ms is measured from pulse onset. Printing `files/docs/hdf5_ECAP_schema.json` would settle it. Even so, a shift of 0.25 ms or less cannot close the ~1 ms gap in P2.
- **Amplifier gain.** Whether the ECAP files are before or after the 10² gain. Printing all trace attributes would show it; a factor of 100 changes every comparison with 0.05 µV.
- **Signal polarity.** Cell 7 shows anti-correlated waveforms across files (r down to −0.90). The figure suggests this partly reflects artefact-recovery curves (12-057), but a per-file polarity check, with peak picking under inverted polarity, would settle it.
- **Missing outputs:**
  - per-rat peak latencies overlaid on the mean traces, to judge problem 1;
  - the Friedman/Dunn test on the cell-39 variant;
  - the /Voids column definitions;
  - the full subjects.xlsx, including `pool_id`;
  - the stim-nonvoiding reading (a) table for the 4 stimulated rats;
  - Table 1 parameters recomputed from the primary pressure traces under each definitional reading.
