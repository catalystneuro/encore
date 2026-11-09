**Verifier report, round 1: Tarduno, Cottrell & Zhou 2024 (FIGSHARE:24639285 v1)**

The claims file has 17 claims. The notebook tests 16 and treats `interpretation-impact-no-dynamo` as blocked. I checked the archive through the Figshare API: version 1 is the only version, and its 16 files (13 xlsx, 3 pdf) have the same IDs and MD5s as notebook cell 1.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| glass-specimen-set | reproduced | Cell 8: 22 of 22 Table 2 glass specimens and 12 of 12 Table 1 crystals are present with step, moment, Dec and Inc. 10 glass specimens have AF steps, the same set as the Table 2 marks. Four of the glass sheets are not real replicate measurements (problem 1). |
| glass-success-rate | reproduced | Cell 10: 3/(3+22) = 12.0%. Without AF: 12+1 = 13; with AF: 10+2 = 12, which matches Methods paragraph 2. |
| table2-fit-statistics | partially_reproduced | Cells 12–13: n matches for all nine. With replicates averaged, 23 of 29 values match (79%), just under the 80% bar. The misses are ss10 MAD (33.3 vs 42.9), R2 for ss9, ss10 and ss34, and pTRM checks for ss19 at 250 °C and ss30 at 450 °C. Using only the first measurement gives 38%. Holding a single pTRM reading fixed gives about 66% (19/29), so the outcome is partial either way. |
| table2-no-fit | reproduced | Cell 16: 11 of 11 are irregular under reading (a) and 9 of 11 under (b). ss36 and ss39 grow away from the origin over their last step (1.77→6.00 and 2.31→9.67 ×1e-9 emu). Reading (b) passes exactly at the threshold, and 3 of its 9 are synthetic sheets (problem 1). |
| fig1-linear-components | reproduced | Cell 19, averaged replicates, free-line MAD: ss43 MAD 10.3 vs 10.0 and R2 0.902 vs 0.90; ss19 MAD 30.1 vs 30.1 and R2 0.956 vs 0.94. Nominal paleointensities are 9.6 and 23.0 µT (8.5 and 23.7 µT with first measurements). They cannot be compared with Figure 1 because the figure was not seen. |
| fig2-changing-field | reproduced | Cell 21, averaged replicates: both specimens pass readings (a) and (b), and R2 is 0.384 and 0.378 against 0.38. Both readings are weak tests (problem 6). The "curved Arai plot" part of the statement is not tested. |
| glass-directions-not-random | partially_reproduced | Cell 23: 8 of 22 specimens reject randomness with averaged replicates and 9 of 22 with first measurements. Inside the Table 2 ranges it is 8 and 7 of 22. Every count falls in the claim's quarter-to-half band. |
| glass-af-no-change | reproduced | Cell 25: 8 of 10 show no significant change under readings (a) and (b), which is the allowed maximum of two exceptions. The exceptions are ss38 (moment ratio 0.49) and ss48, a synthetic sheet. |
| table1-max-intensity | reproduced | Cell 27: 24 of 24 values match under readings a_ii, b_i and b_ii. Table 1's M590 equals the plain magnitude of the 590.1 measurement for all 12 crystals to 4 significant figures (problem 4). Applying the formula to Table 1's own M590 column gives 4 of 12 values equal to two places, and 10 of 12 if Table 1 rounded up. |
| baseline-range | reproduced | Cell 29: the values run from 0.200 µT (12040g1) to 0.500 µT (14053g1), inside 0.18–0.22 and 0.45–0.55. |
| example-14053g1-threshold | partially_reproduced | Cell 31: for 14053g1 the TRM is 3.2e-12 A m² and the threshold 0.50 µT, so the example as written fails. For 12040g1 the numbers are 8.0e-12 A m² and 0.20 µT, so it matches only if the crystal name is a misprint. |
| fig3-nrm-consistent | reproduced | Cell 33: NRM replicates are consistent for 10 of 12 crystals under reading (a) and 8 of 12 under (b), including 12040g1 and 14053g2. Most crystals have only n = 2 NRM measurements. |
| fig3-590-inconsistent | reproduced | Cell 33: 590.0 replicates are inconsistent for 12 of 12 under reading (b) and 10 of 12 under (a), including both named crystals. |
| fig3-alteration-check-inconsistent | reproduced | Cell 33: 590.3 replicates are inconsistent for 12 of 12 under reading (b). |
| crystal-14053g1-400c-stable | reproduced | Cell 35: the three 400 °C replicates give k 78 and Watson p 0.0003; 590.0 gives k 1.0 and p 0.785. Reading (a) holds. Reading (b) fails (9.3° from the NRM mean against an α95 of 4°), but the criterion needs only one. |
| no-alteration-recording-efficiency | reproduced | Cell 37: all 12 pass reading (b), with TRM40/(2·TRM20) between 0.77 and 1.17. Reading (a) passes only 11 of 12 (first measurement) or 10 of 12 (mean). The result rests on a loose cutoff (problem 7). |
| interpretation-impact-no-dynamo | blocked (other) | The claims file marks it as an interpretation resting on ref. 1 and impact-plasma models. Nothing in the deposit can test it beyond the four claims it depends on, which are tested above. |

### B. Problems

1. **[does not affect a conclusion] Synthetic replicate rows (cell 5, `synthetic_steps`).**
   - In g2, ss8, ss39 and ss48, every step's "replicates" are one row multiplied by factors of 0.95 to 1.03. This applies to declination too: ss8 has an NRM declination of 361.7°.
   - I checked `scaled_copies` on random 4-significant-figure data: it gave 0 false positives in 2000 sets, so the detection is sound.
   - The notebook keeps these sheets in all counts. Dropping them changes no outcome: af-no-change becomes 8/9, not-random 7/18, no-fit (a) 8/8. However, ss39 is one of the two specimens the no-fit "trend out of origin" condition depends on.
   - The deposit therefore does not hold real replicate measurements for 4 of the 22 glass specimens. That should be reported alongside glass-specimen-set.
2. **[does not affect a conclusion] Combining replicates by their mean is an assumption the author chose (cells 12 and 19–21, `step_table`).**
   - The data support it: averaged replicates reproduce Table 2 almost exactly (MAD 30.10, 35.36, 24.06; R2 0.384, 0.378), while first measurements do not.
   - The fig2-changing-field and fig1 R2 results depend on this choice. With first measurements, ss41 R2 is 0.16, ss22 is 0.44 and ss43 is 0.99, all outside tolerance.
3. **[does not affect a conclusion] ss6 step 250.1 has 19 rows in two direction clusters (cell 14).**
   - The clusters sit at inclinations of about −13° and +71°. Their mean vector has no physical meaning.
   - ss6 R2 is 0.89 with averaged replicates and 0.09 with first measurements. Counting it as a miss gives 22/29 (76%), still partial.
4. **[does not affect a conclusion] Table 1's M590 is not the TRM (cell 27).**
   - M590 is the raw magnitude of the 590.1 measurement. The Methods define TRM as the field-on minus field-off vector, and Technical Validation calls this value "TRM590".
   - This is a discrepancy in the paper itself; the claims file's reading (b) covers it.
5. **[does not affect a conclusion] The stated 8e-11 emu threshold is well below the measurement noise (cell 33).**
   - All 37 of the 590.0 measurements are above it (1.2e-10 to 5.7e-10 emu) while their directions are random. The real noise floor is several times 8e-11.
   - So the Table 1 "max intensity" values understate what the data can exclude.
   - Reading (a) of no-alteration compares 590.3 minus 590.0 moment differences with 8e-11, which is below the replicate scatter. 14053g1 fails it by 4e-11.
   - This bears on the interpretation claim, not on how the arithmetic criteria are scored.
6. **[does not affect a conclusion] The fig2 readings cannot discriminate (cell 21; I checked `mad_plane` and `mad_line` on synthetic data).**
   - Random 3-point sets pass reading (b) 58% of the time.
   - A single noisy line passes (a) 38% and (b) 30% of the time.
   - The criterion is met, but it is weak evidence of a changing field.
7. **[does not affect a conclusion] The no-alteration cutoff in the claims file is very loose (cell 37). This is a claims-file wording issue, reported and not corrected.**
   - The claims file's reading (b) fails only when TRM40 exceeds 4×TRM20, although its own text says "no more than about twice".
   - Under a cutoff of TRM40/TRM20 > 2, three crystals would fail (b): 12053g1 at 2.35, 14053g3 at 2.08 and 12053g2 at 2.06. Since (a) also fails at least one crystal, no reading would pass every crystal.
   - The paper's actual claim is "≫100%", and the largest apparent efficiency here is 117%, so the substance holds.
8. **[does not affect a conclusion] Matching pTRM checks on any one of four readings is permissive (cell 13).**
   - A pTRM value counts as matched if any of four readings lands within 10%. No single reading matches more than 5 of 11.
   - The partial outcome holds under a fixed reading.
9. **[does not affect a conclusion] Helper checks.**
   - `mad_line`, `mad_plane` and `step_kind` behave correctly on synthetic inputs.
   - `watson_p` gives a false-positive rate of 6–7% at n = 2 and n = 4 (300 trials), consistent with 5%.
   - `fisher` returns NaN for k when the directions are identical. No data hit this case.
   - Units are consistent: emu converts to A m² by ×1e-3 in cell 31, and the formula uses emu throughout.

### C. What I could not check
- **Figures 1–3:** no PDF was supplied, so the nominal paleointensities and the arrow-marked step ranges could not be compared.
- **Deposit PDFs:** "SupplFig1 - other Thelliers March 2024.pdf" (27.7 MB) and "SuppFig2 - All Stereonet.pdf" are in the deposit but were not read. They would show which steps the authors fitted for ss9 and ss10 (the MAD and R2 misses) and the Fig 2 intervals.
- **Outputs that would have helped:**
  - per-step replicate tables, with the scatter of each step, for ss9, ss10 and ss6;
  - the table2-fit-statistics score with a single fixed pTRM reading and with the four synthetic sheets excluded;
  - TRM40/TRM20 printed without the factor of 2;
  - a check of whether other glass sheets have two-cluster steps like ss6 250.1;
  - an Arai-curvature measure for ss41 and ss22, to test the "curved plot" part of fig2-changing-field.
