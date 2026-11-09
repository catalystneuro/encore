I wrote `claims/001273/10.1016-j.xcrp.2025.102660.yaml`. The quote checker reports 15 claims, 15 quotes, 9 statistical values and 0 problems. Nothing is committed.

**Text read:** the NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC: main text, figure legends, STAR Methods, and the supplement (Figures S1 to S4 and Table S1). I did not read the version of record. There was no main-text PDF, so I could not look at any figure; the only PDF was the supplement's. The paper says it reports no original code, so there was no code to read. The dataset's title points to the Figure 4 experiment: strobe imaging of membrane charging by 2-µs pulses, by cell shape and orientation to the field.

**Claims:** 15, all with quotes.
- **Tested on this dataset (6), all from Figure 4:**
  - the most polarized membrane faces the electrodes;
  - time constants double when elongated cells are aligned with the field;
  - no difference between the two poles (a claim of absence, judged by a paired t test at p < 0.05);
  - discharging is slower than charging;
  - the pooled time constants (0.7, 0.91, 0.65 and 0.8 µs);
  - membranes are 95% charged within 3 µs.
- **On the paper's other dandisets (9):** these cover the other main findings, at Figures 1, 2D, 3B, 3C, S1, S2, 5/S3 and 6, plus the 5 to 15 mV threshold estimate. The paper does not say which figure is in which dandiset, so I assigned them from the dandisets' titles. Two of them, the Figure 5/S3 and Figure 6 claims, take their readings from the 001274 claims file.
- **Statistics:** 4 claims carry 9 entries. For both the orientation effect and the charging/discharging difference, the text and the legend give different tests or p-values, and both versions are recorded.
- **Criteria:** all 15 claims have one; 7 also have expected values.

**Details the paper leaves open, and the readings named:**
- **ROIs:** taken from the dataset if it holds them. Otherwise they are rebuilt from the RATIO image, either (a) as a 12 × 12 pixel square on the extreme pixel or (b) as the pixels beyond half the extreme.
- **Debris-ROI scaling:** run with and without, as the paper did.
- **Fit weighting:** unweighted, or weighted by 1/SEM².
- **Discharge amplitude:** a free parameter, or fixed at the charging fit's ΔFmax.
- **Cell shape and orientation labels:** the paper judged them by eye. Without labels in the dataset, the claims that need the groups are blocked as `metadata_insufficient`.
- **What the 19 experiments count:** averaged per fit or per cell. The paired against unpaired test for the orientation effect is also open, since the parallel and perpendicular groups (n = 3 and n = 6) cannot all be paired.
- **Pooling for the charging/discharging test:** all experiments, all but the parallel group, or each pole alone.
- **The "<3 µs" bound:** applied to the parallel group's mean or to every fit.
- **Measure for electrode-facing polarization:** the paper gives none, so I named a standard choice.

**Missing or inconsistent in the paper:**
- The Results give 1,440 images per experiment, and 1 µs before to 6 µs after the pulse; the Methods give 160 images per replicate, 1 µs before to 5 µs after. The dataset's frames decide, and the opening comment records the discrepancy.
- The group means of Figures 4D and 4E appear only in the figure, which I could not see, so they are not used as expected values.
- It is not known whether the 257 V/cm pulse recordings of the nine cells in Figures 5 and 6 are in 001273 or 001274.
