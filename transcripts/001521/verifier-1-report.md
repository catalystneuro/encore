**Verifier report, round 1: Semenov et al. 2026 on DANDI:001521 (v0.261006.1845)**

The claims file has 27 claims. The notebook tests 6 and treats 21 as blocked for missing data.

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| fig6a-ca-entry-1000-1200 | reproduced | Cell 17: under M1 (1000 V/cm = 250 V, 1200 V/cm = 300 V), three readings hold at both fields: end dF against sham (p < 1e-6), peak against zero (p < 1e-5) and peak against sham. The 1000 and 1200 means also exceed every field of 650 V/cm or less. M2 gives the same result. |
| fig6a-ca-sustained | not_reproduced | Cell 20: the mean of the last 10 frames is −5.4 ± 0.6 % at 250 V and −3.8 ± 0.7 % at 300 V, and +1.2 % with p = 0.53 at 350 V under M2. None is above zero. This rests on a −12 % drift in the sham group that the paper's Fig. 6A does not show (problem 1). |
| fig6a-780-not-significant | reproduced, but only formally | Cell 23: the main reading (one-sample test of end dF) finds no increase, because the mean is −7.4 % at 200 V. That same test also finds no increase at 1000 and 1200 V/cm, so it cannot detect anything here. Every variant finds a significant increase at 780 V/cm: against sham p = 1e-6, peak against zero p = 0.009, peak against sham p = 0.02. The sham-corrected variant in cell 21 gives +4.8 %, p < 1e-5. |
| fig6b-train-threshold | not_reproduced | Cell 32 covers 24 combinations of region size, conversion and rule. The 780 V/cm fraction is never within 28 ± 2.8 %, and the fields above 780 V/cm never reach 90 % responders (best 79.5–87 %). The expected total of 224 cells (tolerance 0) is not met: the data have 311 train exposures and 82 distinct cells. |
| fig6b-650-weak-but-significant | not_reproduced (the notebook says blocked: methods_underspecified) | Both tests the statement names are fully specified, and both conversions fail at least one (cell 28). M1 (170 V): the count of 2 cells (5.6 %) matches under one rule, but the end mean is −9.2 %, so it is "significant" in the wrong direction, and the single-tailed test against 230 V/cm gives p = 0.20. M2: against zero p = 0.27. |
| fig5b-conductivity-calibration | partially_reproduced | Cell 35, and I re-derived Eq. 2 independently. A 10-fold increase gives a 1.33 % reduction (1.20 % in the variant), outside 2 ± 0.2. A 100-fold increase gives 11.87 % (11.75 %), inside 12 ± 1.2. |
| The 21 potentiometric claims (fig1, fig2a×2, fig2b, fig2cd, fig2c, fig3×2, fig4a, fig4b×3, fig4c, fig4d, fig5a×2, fig5c, fig7a, fig7b×2, fig7c) | blocked: data_missing | I queried the archive API. The version holds 73 NWB files in 15 subjects. Each is one Fluo-4 TimeLapseImaging series; there is no pulsed-laser FluoVolt or Di-8-ANEPPS imaging. The dandiset title and description cover only Ca²⁺ uptake. No part of these claims can be tested on this dataset. fig5c also needs the Fig. 5A data. |

**B. Problems**

1. **[affects a conclusion] Sham drift does not match the paper (cells 10–11, 20, 23, 25–32).** The notebook's dF in sham recordings falls to −12 % (single pulses) and −16 % (trains). The paper's Fig. 6 (PDF page 8, which renders) shows 0 V/cm drifting to about +1 % and 230 V/cm flat near 0. Either the paper's processing differs (for example a bleaching correction or a different region or background) or the data differ. The notebook notes the drift but never compares it with the figure. Every end-of-recording reading inherits the drift: the "sustained" failure, the null in the 780 V/cm main reading, the train thresholds and the 650 V/cm tests. No output separates bleaching from background handling, such as a raw F trace and the background trace for the sham group.
2. **[affects a conclusion] The 780 V/cm main reading cannot detect an increase (claims file, fig6a-780-not-significant; cell 23).** The one-sample end-value test it prescribes also misses the clear 1000 and 1200 V/cm entry, so a "reproduced" from it carries no information. Every reading that does detect 1000/1200 V/cm finds 780 V/cm significant too. I report this against the claims file; I have not corrected it.
3. **[does not affect a conclusion] The field conversion was built without the figure (fluo4.py `FIELD_PER_VOLT`; cell 15).** Fig. 6 labels its fields and gives group sizes:
   - Fig. 6A: 0, 570, 780, 1000 and 1200 V/cm.
   - Fig. 6B: n = 28, 37, 34, 54, 35, 36 at 230, 570, 650, 780, 900 and 1000 V/cm.

   The dataset's train groups at 70, 150, 170, 200, 230 and 250 V have 28, 38, 36, 68, 47 and 39 cells. That fits M1 (about 3.9 V/cm per V; 230 V → 897 ≈ 900) and rules out M2. Every outcome above holds under M1. M2 should not count as an equal reading. The 1.00 mm electrode gap stated in the files, against 1.6 mm in the paper, is never reconciled.
4. **[does not affect a conclusion] Wrong comparison set and counts for Fig. 6B (cells 25, 32).**
   - "Every field above 780" includes 210, 220 and 300 V, which are not in Fig. 6B. Under M1 the paper's higher fields are only 230 and 250 V, and those fail too (at most 87 %).
   - The 224-cell total is compared with 311 and 82. The six groups that correspond to the figure sum to 256 in the dataset. That is still not 224, but it is the relevant count.
   - The figure's group sizes suggest the paper counted exposures as cells, despite "each cell tested once".
5. **[does not affect a conclusion] Strong-response rule (b) (cell 25).** It is read as mean + 3 s.d. The literal reading ("above 3 s.d.", a threshold of about 21 %) was not run. It cannot rescue the claim, because the 90 % condition already fails at a lower threshold (−1.45 %).
6. **[does not affect a conclusion] The cell-28 printout omits the sign.** It gives p = 6e-13 "against 0" at 170 V without saying the mean is negative, while the statement says "above zero".
7. **[does not affect a conclusion] Repeated cells treated as independent (cells 7, 17).** The same cells are exposed up to 7 times and nested in 6 or 9 fields of view, and the t-tests treat each cell-recording as independent. The per-field-of-view table in cell 18 shows the same direction in every field of view, so the conclusions stand.
8. **[does not affect a conclusion] Wrong file counts in the docstring (fluo4.py).** It says 30 single-pulse and 43 train files; the data have 31 and 42 (cell 4).
9. **[does not affect a conclusion] Helpers check out on synthetic data.** I tested `segment`, `cell_traces`, `delta_f`, `end_value`, `peak_value`, `parse_description` and `voltage_for` on a synthetic stack. Touching cells were split, background drift was removed, and a 50 % step was recovered exactly. The peak reading has a slight upward noise bias, about 0.05 %.

**C. What I could not check**

- **Whether the sham drift comes from the data or the processing.** I would need the mean raw (not background-subtracted) sham trace and the background trace against time, plus the dF under a Fig. 6-style comparison.
- **Segmentation quality on the real images.** Region overlays on one pre-pulse image per field of view would have shown it.
- **The train end-dF values by voltage.** The notebook prints only fractions; a table of n, mean, s.e. and the p-values against zero and against 70 V per voltage would have let me check the 650 V/cm tests under every mapping.
- **Which 14 cells Fig. 6A averages.** The data cannot tell; a match of per-field-of-view counts against 14 would have helped.
- **Whether 001515–001526 hold the potentiometric data.** They are separate targets, so I did not check them.
