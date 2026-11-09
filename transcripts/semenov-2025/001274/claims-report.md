I wrote `claims/001274/10.1016-j.xcrp.2025.102660.yaml`. The quote checker reports 26 claims, 26 quotes, 8 statistical values and 0 problems. Nothing was committed.

**Text read.** I read the NIH author manuscript (NIHMS2098259, PMC12320893) from Europe PMC: main text, figure legends, STAR Methods, and the supplement (Figures S1 to S4 and Table S1). I did not read the version of record. There was no PDF of the main text, so I could not look at Figures 1 to 6, and numbers shown only in figures are not used. The paper says it reports no original code, so there was no code to read.

**What this dataset holds.** The paper put its raw images in ten dandisets without saying which figure is in which. Going by its title and description, 001274 holds the strobe recordings of sine-wave polarization, the sine-wave part of Figures 5, 6 and S3. I assigned the other figures to the other dandisets from their titles alone:
- 001032 to 001035: Figures 1, 2, 3A and 3B
- 001030: Figure 3C
- 001271: Figure S2
- 001272: Figure S1
- 001273: Figure 4

Those 18 claims are marked `data: elsewhere`. The 8 claims on Figures 5, 6 and S3 are marked `dataset`. They also need the 2-µs pulse recordings of the same cells, which may be in 001274 or in 001273.

**Counts.**
- 26 claims, all with quotes, none inferred.
- 5 claims carry statistics, 8 entries in all: the t tests for Figure 2D (four), Figure 4 (three), and the regression for Figure 6C. For Figure 6C the paper prints the p-value as "<0.01%", recorded as `p: 0.0001`. The checker passed it, probably by matching another "p < 0.0001" in the text, so that value needs checking by reading.
- All 26 claims have a criterion.

**Details the paper leaves open, and the readings named:**
- **ROIs (O1):** their size and position are not given. The ROIs must come from the dataset. If it has none, the claims are blocked as `metadata_insufficient`, and an ROI rebuilt from the RATIO image is shown only as a variant.
- **LOESS fit (O2):** span and degree are not given. Readings are R's loess defaults (span 0.75), since Table S1 lists RStudio, plus spans 0.5 and 0.25.
- **How the field enters the Figure 6C regression (O3):** (a) frame by frame against the signed instantaneous field; (b) per carrier cycle, oscillation amplitude against the cycle's peak field, with and without an intercept.
- **Which recording is cell C7 or C8 (O4):** to be found from the dataset, using the pulse field, the peak field and the session count.
- **Debris scaling:** the paper processed data both with and without it, so both are run.
- **AP detection:** the paper says only "brief emission upticks" in neurons whose APs exceed 5% ΔF. Readings are a peak above 5% over F0, or a rise of 5% within 5 ms.
- **"Up to 90%" smaller (Figure 5):** read either as the ratio of the two ROIs' sensitivities, or as the largest per-cycle reduction.
- **Pulse asymmetry measure:** ΔF averaged from 1 to 2 µs into the pulse (Figure 6B), or the peak of the 5-point running average (Figure 5B).
- **Figure 4:** the legend gives n = 3 parallel and n = 6 perpendicular cells, yet the comparison is a paired test, so it is read as using cells with both orientations. The pooling for "discharging slower" and for the "ALL" averages has two or three readings each.
- **Figure 6D legend:** it says "ratio of (D) and (C)"; I read it as Figure 6C over 6B.
- **Volts to V/cm:** the paper shows the conversion only in Figure S4C. The dataset metadata is used (the 001030 description says 1 V = 36 V/cm).
- **Thresholds I set myself:** some criteria use windows or thresholds the paper does not fix. They are named in the criteria, not presented as the paper's:
  - the 5% depolarization block test
  - the "near the beat peak" window with an 80% share
  - the Spearman test of latency against field
  - the paired t test on AP counts in Figure 2C, which applies the paper's general test because it reports none for that panel

**Missing from the paper.** Nothing that blocks writing the claims; the full text, Methods and supplement were all present. Group sizes for Figure 2D and per-cell values for Figures 4 and 6 appear only in figures, so they could not be used. Which dandiset holds which figure is not stated anywhere. I left out the heating estimates, which are calculations and not measurements.
