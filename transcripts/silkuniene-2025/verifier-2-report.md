**Verifier report, round 2: Silkuniene et al. 2025, claims file `silkuniene-2025.yaml`**

The claims file has 28 claims and the attempt record has 28 outcomes, one for each claim.

## 1. Outcomes and assumptions

**Outcomes I agree with (23):**
- All 11 blocked claims: fig1e, fig2, and the nine fig3/fig4 claims.
- fig5-raised-electrodes-weaken-centre, not_reproduced. It fails with all wells and with the August batch.
- fig5-killing-focused-centre, fig5b-gaussian-pr-lorentzian-yp, fig5b-reversible-beyond-2mm, fig6b, fig6d-900ns-fwhm, fig7-sharpest-peak-one-burst and fig7-cho-replicates-ct26.
- fig5ab, fig6c, fig5c, fig6d-600-900 and fig7b, each as stated.
- fig6d-600-900 is partial in all 21 subsets of the 600-ns wells, so it does not depend on the well choice and needs no `assumed` flag.

**The four outcomes marked `assumed: true`:**

- **fig7be-center-linear-with-bursts, partially_reproduced: agree.** The flag is not needed. The outcome is partial under both O4 readings: on group means the CT26 p is 0.036, which falls in the criterion's p < 0.05 case (cell 70). It is also partial on experiments, because only 38.4% of the paper-size subsets give p < 0.001 (cell 71).

- **fig7cf-fwhm-with-bursts, reproduced (assumed): I now agree.**
  - The assumption is stated in the record.
  - The legend gives p < 0.001 for panel B, which is fitted to three group means. With one degree of freedom that needs t greater than about 636, so per-experiment points are the better-supported reading.
  - The record's wider wording is too strong for panel C (see section 2).

- **fig7-offtarget-40-50-fold, reproduced (assumed): agree under the criterion's one-combination rule.**
  - The assumption is stated. I confirmed that "upper-left" is corner 0 in the corner order of `cc.find_array`.
  - The evidence is weak. For CT26 at 1 burst and 6 mm, the choice of background footprint alone moves the ratio from 23.6 to 57.0 (cell 86), so a value inside 36 to 55 is close to guaranteed.
  - This claim also uses a different background from every other claim (the darkest footprint is used elsewhere).

- **fig6d-longer-pulses-sharper-peak, reproduced (assumed): I do not agree.**
  - My round-1 label of partially_reproduced was wrong: this criterion has no partial case. The two possible outcomes are reproduced or not reproduced.
  - The O4 per-experiment assumption is reasonable. Three group means would need t of about 212 for p = 0.003.
  - The well-selection assumption is the one that decides the outcome, and it is weak:
    - B2 has an independent reason to be left out: its spot is 5.39 mm off the array centre.
    - B3 does not. Its spot is 0.33 mm from the centre and its centre value of 748 is within the 600-ns range (391 to 1387). Its only printed anomaly is its FWHM of 5.49 mm, which is the quantity being tested (cell 19).
    - Every subset that keeps B3 gives p of 0.79 or more (cell 58). Leaving out B2 alone (n = 6) was not run.
  - I would record not_reproduced, unless B3's lack of a central peak is shown by a measure other than its FWHM.

## 2. Sentences the printed numbers do not support

1. **Cell 72 and the fig7be record note:** "on group means neither cell line has p below 0.001 in any draw." In cell 71, `be_CHO_means` has a minimum of 0.0000 and a 5th percentile of 0.0004, so CHO is below 0.001 in at least 5% of draws. Only CT26 never is, and the outcome is unchanged.

2. **Cell 54 and the fig6c record note:** with all seven 600-ns wells, the gaps are said to be "all 300 against 900 ns". Cell 53 also lists 600 against 900 ns at ±0.81 mm under the contiguous-ROI readings. The outcome is unchanged.

3. **Cell 59 and the fig6d-longer deviation:** "B2 and B3 are the only 0.2-MHz CANCAN wells without a central peak", and "(FWHM 16.1 and 5.5 mm), unlike every other 0.2-MHz CANCAN well". In cell 19, CT26 wells at 6 bursts have FWHM 5.51 to 8.05 and CHO wells at 1 burst have 5.29 and 5.40. "No central peak" for B3 rests on the montage image, which has no text output. This bears on the conclusion.

4. **Cell 78 and the fig7cf note:** "a slope through 3 or 4 group means can hardly reach that". With four group means, the CT26 p reaches 0.0005 (cell 77, contiguous ROIs, 4-mm range). The argument holds only for panel B.

5. **Cell 91, Summary:** "the FWHM claims are shown with this difference taken out". Only fig6d-900ns-fwhm (cell 65) and fig7-sharpest (cell 81) are shown this way. fig6d-longer, fig6d-600-900 and fig7cf are not.

6. **The 001277 metadata_error finding** ("Every 001277 file states '9 packets...'"): in cell 12 the text "(every file: '9 packets of pulses')" is a fixed string in the print statement. The printed values show only the packet rate, so the finding has no computed output behind it.

7. **fig5-raised record note:** the October centre "falls to 38.0% and 7.1% of the 0-mm mean". The 0-mm mean here is that of all wells; October's own 0-mm value is 121.8% of it. Cell 29 says this correctly and the record does not.

Every other sentence in the Result conclusions, the Summary, the README and the record notes matches the printed outputs. I could not check two README statements from outputs: "about 45 GB", and "about 40 minutes" (the printed run time is 35.5 min).

The verifications block states my round-1 reasons accurately. Where it merges my problem points B2 to B9 into the claim entries, it keeps their substance.

**Where the claims file misreads the paper or the data (reported, not corrected):**
- It assigns the Fig. 3 and Fig. 4 series to 001047, which holds a 3.8-mm array, and leaves out the 001276 wells at 1 Hz, 0.2 MHz and control. This is unchanged from round 1.
- O1 calls the choice of background footprint "any one, a standard choice". The data show it changes the ratio claims by a factor of 2 or more.

## 3. Round-1 points

**Resolved:**
- **B2:** the August batch is now run for every Fig. 5 YP claim, and no outcome changes.
- **B4:** a per-well geometry table was added, and the FWHM sensitivity is shown for fig6d-900 and fig7-sharpest. Both claims hold under contiguous ROIs.
- **B5:** every footprint is run as background.
- **B6:** subsets of the paper's size were run, and fig7be was changed to partial.
- **B7, B8, B9:** resolved. The OME channel names are printed as (Cy3, DAPI).
- **The section C requests:** answered, apart from the montage judgements.

**Open, and bearing on a conclusion:**
- **B1, the 001047 assignment:** asked of a reader. If the 001276 wells are assigned, fig3a, fig3bc, fig3-lorentzian and fig4b-40-fold-ratio could be decided:
  - fig3a would probably fail on its control part (cell 23).
  - fig4b-40-fold-ratio would be reproduced (36.7 to 45.7 at 6 mm, cell 23).
- **B3, the 600-ns well choice:** fig6d-longer is reproduced only when B2 and B3 are both left out, and B3's exclusion is not independent of its FWHM. The record should drop or support the "no central peak" statement for B3 (section 2, item 3). It should also run the fit with only B2 left out.
- **fig7-offtarget:** "reproduced" depends on which footprint gives the background, and that choice spans the whole tolerance band. The authors' answer about the footprint would decide it.
