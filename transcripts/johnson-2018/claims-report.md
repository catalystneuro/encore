I wrote the claims file at `claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml`. The quote checker reports 21 claims, 21 quotes, 33 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (PMC5895055, open access): main text, Methods, the legends of Figures 1 to 8, and the captions of the supporting information. There was no PDF. Of the supplement, I read the S1 and S2 Fig legends. S1 to S4 Table are DOCX files of model outputs, and only their captions were supplied.

**Code:** the paper says its MATLAB scripts are deposited with the data on CRCNS, in the dataset's `analysis_scripts` folder. Because they are among the dataset's files, I did not read them. The author may find some of the open details below settled there.

**Claims:** 21, all with quotes; 13 report statistics, 9 have expected values and all 21 have criteria. They cover:
- behaviour: proficiency, and no difference in difficulty between conditions
- electrode and correct-trial counts
- event-related potentials (ERPs): no condition differences
- theta power: sustained theta, and the 8 electrodes excluded for condition differences in power
- phase locking: theta peak
- theta directionality (phase slope index): shift from precue to postcue
- theta phase-to-amplitude directionality: shift in seven systems, counts of phase-directing electrodes and pairs, and equal strength across frequencies and directions
- individual theta peak bands
- phase-amplitude coupling (PAC): ten effects across the MTL, PFC, OFC and the MTL-PFC and MTL-OFC directions, including the two models that compare directions

All claims use the dataset alone.

**Details the paper leaves open, with the readings named:**
- **Precue delay segment:** (a) 600 to 1500 ms after first stimulus onset, or (b) 400 to 1300 ms, if the two stimuli ran back to back.
- **Behaviour model:** the printed F(1,28) does not fit a three-level factor. (a) Each relation condition tested against identity, or (b) one three-level term. Accuracy is (a) over all trials or (b) over the trials kept after artifact rejection.
- **Power z-score:** (a) on trial-mean power, or (b) on single trials. For the power condition test, (a) z-scored or (b) raw single-trial power.
- **"Sustained" theta and the alpha drop:** no count is given. Unit (a) region average per subject or (b) per electrode. The "at least half the time points, in most subjects" threshold is my choice and is marked as one.
- **Phase locking "from the imaginary part":** (a or b) imaginary PLV, or (c) phase-lag index.
- **Group models for directionality:** (a) z-scored or (b) raw values.
- **PAC surrogate shuffle:** (a) trials permuted against phase, or (b) amplitude-frequency labels shuffled.
- **Electrodes for the theta peak:** (a) all analysed electrodes, or (b) the phase-directing ones only.
- **Fixed as standard choices and marked as such:** filter band edges, combining the sliding-window spectra, random-effects structure, frequency and time as categorical factors, and m = 7 or 15 in the Bonferroni correction.
- **My thresholds, marked in the criteria:** at most 5% of electrodes significant in the precue delay, and 5 of 7 counts within tolerance.

**Missing:** the contents of S1 to S4 Table. No claim's expected value needs them; the equal-strength claim rests on the main-text sentence "uncorrected p > 0.11". Without a PDF, I could not read values shown only in figures (the Fig 4B percentages, the Fig 8A means, the Fig 3B per-subject values).
