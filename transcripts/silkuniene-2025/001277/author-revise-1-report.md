Round 1 is answered and the entry has been re-run: `python tools/entry.py all` reports 0 errors and the notebook passes in 776 s. Nothing is committed.

**Outcome changes**
- **fig5-yp-lorentzian-pr-gaussian** and **fig5-yp-spot-slightly-larger-than-pr**: changed from not_reproduced to blocked (`metadata_insufficient`), as the verifier gave them. Nothing in the dandiset links its 600-ns wells to Fig. 5, and Pr images also exist for three 300-ns and three 900-ns wells. The notebook still shows what the claims would give if those wells were Fig. 5's 0-mm group.
- **fig6d-900ns-fwhm**: kept blocked, and the verifier's disagreement (it would give reproduced) is recorded. The claims file makes this claim depend on fig6d-longer-pulses-sharper-peak, which is blocked. The protocol (Author, step 1.5) blocks a claim that depends on a blocked claim. The notes say the claim's own criterion would be met.
- The other 14 outcomes are unchanged, and the verifier agreed with all of them.

**Added or corrected**
- **Channel check:** the OME metadata of each Cy3-DAPI file names channel 0 Cy3 (565 nm, which is Pr) and channel 1 DAPI. This settles point 3.
- **Distances without the 9.05-mm rescaling** (`diagonal_profiles` now has a `scaled` option). The 900-ns FWHM is 1.69 to 1.71 mm with contiguous ROIs and 1.81 to 1.83 mm with 1-mm steps, inside tolerance in 6 of 12 readings. The Fig. 6D slope and pairwise tests show the same pattern as before, so no outcome changes.
- **Pr images:**
  - Per-well profiles now show a broad level: within 5 mm of the centre, Pr is 40 to 53% of the centre value in the main-row wells and about 100% in the two P1 row B wells.
  - The weakest footprint is much fainter in two wells (rim contrast 74 to 76, against 193 to 416 in the other three), so footprint placement is less reliable there.
  - With a constant offset added to the fit, the Gaussian fits Pr better than the Lorentzian in all 8 readings shown. This supports the block.
- **fig6b variant with plate rows paired:** paired t-tests give Bonferroni p of 0.415 and 1.000, and a repeated-measures ANOVA gives p = 0.071. Still no difference, so it stays reproduced.
- **Stated in the notes and the notebook:**
  - The fig6d-longer block depends on leaving out both P1 row B wells. Keeping either one makes that claim not_reproduced.
  - Contiguous ROIs overlap, and the fit p-values treat them as independent.
- The notebook conclusions, summary and README now match the new outcomes, and round 1 is recorded under `verifications`.

**Not done**
- No question was added to `questions/001277.yaml`. The verifier's point 9 says the fig6d criterion includes a regression on the 3 means that is nearly impossible to pass, but it does not say the claims file misreads the paper, and the outcome would be the same without that reading.
- I did not use the Hoechst images taken before exposure, which the verifier listed as something it could not check. No conclusion depends on them.
