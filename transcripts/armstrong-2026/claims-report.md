I wrote `claims/001341/10.1073-pnas.2514107123.yaml`, and the quote checker passes it: 32 claims, 31 quotes, 6 statistical values, 0 problems. Nothing is committed.

**Text read**
- The version of record as the PubMed Central author manuscript (NIHMS2207436, PMC13142948), with its SI Appendix: Figs S1–S12, Table S1 and the SI Methods and Data Analysis. The main text's Methods only points to the SI, so the methods come from the SI.
- The paper's title is "Neural correlates of perceptual decision-making in the primary somatosensory cortex". The title in the task is the dataset's title.
- I searched the bioRxiv preprint (v1) for extra method details. It has none, and no claim rests on it.
- The paper links no analysis code of its own, only third-party tools (Kilosort 3, ecephys, Phy, the Pillow lab GLM tutorial, PyDDM, SLEAP). I read none of them, and no method detail is settled by code.

**Counts**
- 32 claims: 31 have quotes, and one (`table-s1-recordings`, the per-animal unit and trial counts) is marked `inferred`.
- 22 have expected values.
- 2 have statistics, 6 entries in all: the Fig. 5E two-sample t tests (p = 0.109, 0.140, 0.970) and the Fig. 3J–L legend tests (p < 0.0001).
- All 32 have criteria. Every claim uses the dataset's own data; there are no outside inputs.

**Details the paper leaves open, and the readings named**
- **Ramp slope (12.25):** the units could be min-max normalised rate per second or Hz per second. The fit window could be 0.12–0.17 s, 0.12–0.18 s, or from ramp onset to the peak at 0.25 s. The normalisation range is also open.
- **Ramp onset:** either the minimum of the epoch 3 dip, or a rise of 10% of the range above it. The second reading is mine; the paper only says "end of epoch 3".
- **Epoch 1 baseline window:** −0.5 to 0 s or −1 to 0 s. No smoothing is named, so the main reading is unsmoothed 5 ms bins.
- **Success at "±1 cm clearance":** either displacement in the turn direction or absolute displacement. Which of animal 503's trials make up the "414" is not said: all of its OL turn trials, or the first 414.
- **Running speed of 21 ± 4 cm/s:** animal 503's session (all samples, or running only), or the mean over animals in Table S1.
- **Lateral distance:** its reference point is open, and so is which animal each of the 2.30 and 1.49 SD values belongs to.
- **Reaction time:** run-angle derivative or lateral-velocity derivative, searched over 0–1 s or 0–1.8 s. First touch is counted with or without touches of the retracting wall.
- **Turn angle:** the mean of θ over the turn, or the displacement angle at t = 1 s.
- **Whisking set point:** the mean angle per whisk cycle, or the mean angle before t = 0.
- **GLM:** the significance threshold (p < 0.05 or 0.01), ridge penalty, Savitzky-Golay settings, lags and segment are not given, and the trial count is 40 in the SI against 55 in the legend.
- **Dimensionality:** whether the 2 ms kernel is an SD or a FWHM, and over what period the 1 Hz rate cut is taken.
- **DDM:** which parameters were free (σ free or fixed), and whether K/B is taken from the GDDM or the DDM.
- **VarCE and CorCE:** whether units are summed or averaged, and which bins the CorCE matrix covers.
- **Streak index:** a raw switch count (the SI's description) or a z-scored runs statistic. Also open: where the 40 ms window sits, whether counts are summed over units or kept per unit, and how ties with the median are handled.
- **Fig. 2L:** which animal is shown, and how "sitting" is defined.
- **Jitter of 30 ms:** not defined. I named two readings, and it is reported but does not decide the claim's outcome.
- **Claims with no test in the paper:** for psychometric trend, lateralisation, staged modulation and similar claims, the windows come from the paper but the judging test was chosen in the file, and the criterion says so.

**Missing from the paper, or self-contradictory**
- **Tables S2 and S3 (fitted DDM parameters) could not be read.** They are images with no extracted text, and no PDF renderer was available in this run. Only the values the main text repeats are used.
- **Paper inconsistencies,** listed in the file's header comment:
  - Unit totals: 634 in the SI against 668 in Table S1. The difference is animal 579.
  - Trial counts differ between figures for animals 489 and 503.
  - Unit 489101 is given as layer 5A in one figure and 5B in another.
  - The number of animals for Fig. 2C–D is given as 5, 7, or 4.
  - The reported drift and bound give K/B = 4.93, while the text gives 11.12.
  - The text calls the whisking parameters "statistically identical", while the legends of Fig. 3J–L report p < 0.0001.
  - Epoch 2 peaks at 0.026 s, while first touch is at 0.06–0.07 s, yet the text says the two are within 10 ms.
  - The streak index's mean of 0.06 is impossible for a switch count.
