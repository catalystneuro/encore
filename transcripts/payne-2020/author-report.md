I've finished the author steps for payne-2020 (steps 1 to 6). The entry lock, check and clean run all pass with 0 errors. The notebook runs in 29 s with a peak memory of 0.74 GB. The handover copy was built from a fresh executed notebook, and nothing was committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| anes-ecap-recorded | reproduced (rests on an assumption) |
| anes-ecap-latencies | not reproduced (assumption): medians 1.60, 2.50, 4.19 ms against 1.80, 3.48, 3.77 |
| anes-conduction-velocity | not reproduced (assumption): 1.82, 1.14, 0.68 m/s against 1.60, 0.82, 0.78 |
| anes-threshold-order | not reproduced (assumption): Friedman P = 0.105 under the main reading; no combination of readings passes (0 of 96) |
| fig2c-p3-above-p1 | reproduced under one reading (assumption): unadjusted Dunn P = 0.034, n = 4; Bonferroni-adjusted P = 0.10 |
| fig2ab-one-rat-p2-below-p1 | not reproduced (assumption) |
| awake-ecap-latencies | not reproduced (assumption): three peaks in at most 5 of 7 recordings |
| awake-threshold-increase | blocked, metadata_insufficient |
| impedance-increase | partially reproduced: the first three time points match exactly; the 8-week value is not in the data |
| electrode-failures | blocked, data_missing (only 8 of 10 arrays have per-electrode values) |
| colonic-pressure | not reproduced |
| table1-* (6 claims) | reproduced (HFPO frequency from 7 rats, not 9) |
| table1-comparable-to-published | reproduced (with_inputs) |
| 6 stimulation-response claims, 6 histology/c-Fos/post-mortem claims, no-fecal-expulsion-or-erection | blocked, data_missing |

## 2. Dataset, assumptions and questions

**Dataset (version 1, the only one):**
- **ECAP recording settings:** the files are sampled at 200 kHz with a 500 to 3000 Hz filter; the Methods say 100 kHz and 300 to 5000 Hz.
- **Acute ECAP currents:** they go up to 1.6 mA in logarithmic steps, with no 0 mA trace; the Methods say 0 to 2 mA in 0.1 mA steps.
- **Stimulating pair:** some files stimulate on E3-E4 or with reversed polarity, where the Methods give E1-E2.
- **Awake ECAPs:** seven subject IDs, four at day 0 and three at day 7. Nothing links a day-7 recording to a day-0 rat, so week 0 cannot be compared with week 1.
- **Colonic rat 15-758:** the pressure response sits in the 10 s before each recorded stimulus time, so the times look offset by one train. The colonic stimulation settings in all three files differ from the Methods.
- **Cystometry derivative table:** it disagrees with the files' own void tables in most cycles. It does not give Table 1's exact means, though each lies inside Table 1's CI.
- **Impedance:** the per-array file reproduces the paper's means, spreads and ranges exactly, from 12, 12 and 10 arrays. The paper describes these as 38 electrodes in 10 arrays, and its spreads are SEMs.
- **Missing data:**
  - There is no histology, no c-Fos data (the README lists c-Fos summary data, but no file holds it) and no observation notes.
  - No file records urine release after stimulation.
  - Stimulation trains exist for 4 rats only, against 8 in the paper.
- **Subject count:** the dataset lists 29 subjects; the paper reports 24 rats.

**Assumptions:**
- **ECAP peak detection:** P1 to P3 are the first three positive peaks after the artefact ends that stand above 3 noise SDs, read at the highest current. Margins of 2 and 5 SD were also run.
- **Baseline:** taken from 7 to 8.6 ms, because the traces start 0.6 ms after the pulse and have no pre-stimulus segment.
- **Dunn's test:** fig2c rests on the unadjusted reading of Dunn's P.

**Questions for the paper's authors** (recorded as methods_unavailable findings):
- How were P1 to P3 picked, and at which current and time origin were latencies read?
- How was the 0.05 µV amplitude measured, given that it sits within the noise of every file? Is Dunn's P adjusted?
- Which rat and which 13 responses give the 2.6 mmHg colonic increase?

**Questions to a reader:** none.

## 3. Protocol points

1. **Lowest current as zero:** the "absent at 0 mA" criterion assumes 0 mA traces exist. I used the lowest current and recorded it as a deviation.
2. **Detection rule as a sensitivity axis:** the readings rule did not say what to do when an author-chosen detection rule underlies every reading. I treated the detection margin and artefact end as extra readings, and marked all ECAP outcomes `assumed`.
3. **Partial data with an all-or-nothing criterion:** impedance-increase says "reproduced when all four within tolerance", but the 8-week point is absent. I used partially_reproduced; the protocol gives no explicit rule for this case.
4. **Block versus partial count:** electrode-failures has data for 32 of 40 electrodes. I blocked it as data_missing and gave the partial count in the notes; the protocol is unclear on blocking versus partially testing.
5. **Outside values from the paper itself:** the Wiedmann et al. values are printed in this paper's Table 1, so I recorded the paper's DOI as their source under `inputs`.
6. **SHA-256 in the header:** the header lists hashes for all non-binary metadata and data files, but not for every HDF5 file. The archive guidance asks for "each file read", and the 33 HDF5 files are read without their hash being printed.
7. **Reused runs:** `entry.py run` reused the earlier executed copy after a markdown-only edit, so the first handover held the old conclusion text. I re-ran with `--fresh` and rebuilt the handover.

## 4. Runtime and failures

The work took about 25 minutes (00:02 to 00:26 UTC), and nothing failed in the final runs. During drafting, three conclusion sentences contradicted the printed numbers; I corrected them before the final run. The device-node entries at the repo root (`.bashrc`, `scripts` and others) are sandbox mount points, not my files.
