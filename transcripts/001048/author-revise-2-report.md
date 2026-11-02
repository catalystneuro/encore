I've answered every point in the round-2 report. No outcome changed. For fig6-sine-less-than-pulse I've proposed a change to blocked for round 3. The entry ran twice from clean with `python tools/entry.py all` (about 20 minutes each), both runs gave the same numbers, and the checks report 0 errors.

**Outcomes**
- **fig6-sine-less-than-pulse**, the only outcome the verifier disagreed with, stays partially reproduced. I've proposed blocked, `metadata_insufficient`, for the verifier's reason: as with fig4-pooled-time-constants, its values depend on hand-drawn ROIs and on which cells are the paper's nine, and the dandiset gives neither. I added a check with smaller and larger boxes (6 x 6 and 20 x 20). The values move with box size (pulse mean 13.3 to 17.4 %), and smaller boxes do not bring them nearer the paper's 28. The text now calls the sizes "cannot be judged" where it said they fail. The direction (sine below pulse) holds in 15 to 18 of 18 ROIs.
- **fig2d-modulated-thresholds-higher** is now marked `assumed: true`, resting on the crop ROI. The one significant test needs the crop ROI with O3 a; with O3 b no test is significant, and under ROI b one comparison goes the other way.
- **fig2-modulated-locks-to-beats** stays reproduced. The notebook now prints the levels for the one session that decides it: 5.96 % against 4.72 % (O4 a) and 6.10 % (O4 b), so it rests on O4 b by 0.14 % in one session. The deviation cites the paper's "merge into sustained depolarization" as the basis for O4 b and says plainly that the choice was made after the first run. It also shows that O4 b decides no other claim.

**Corrections and added output**
- Text the outputs did not support is fixed in the notebook, the record and the README:
  - The most 100-Hz sessions in any cell is five (2_20240522), not four.
  - The two ROIs are near antiphase in 7 of 9 cells, not all. The two other cells are named, and the explanation for the positive correlations is no longer stated as shown.
  - The AP peak holds in 12 of 16 crop-ROI readings, not all of them, and the unsupported "lengthened by the noise" phrase is gone.
  - The round-1 reply on 20-kHz excitation is corrected.
  - The unused stimuli now include 40 kHz and 100 kHz.
  - The Summary row for figs2 now names the crop ROI.
  - The README no longer says all ten dandisets were used (001031 is not used, and 001034 only serves to show it is a copy).
- The figs1 notes now give the two neurons' rho values (-0.03 and -0.69).
- The data check now prints the TTX wording the findings quote: 71 TTX session descriptions in 001271 say TTX "caused sustained depolarization", while the dandiset's own description says it "completely prevented sustained depolarization". All 65 sessions in 001272 say "vehicle control".
- Round 2 is recorded under `verifications` for all 20 claims, with the verifier's reasons and my responses.

**Not done, and why**
- **Crop-ROI rule:** I kept it. The claims file's header would block a claim whenever the ROI readings disagree, but protocol step 1.6 lets the author adopt a defensible choice as an assumption, and the verifier found the crop reasonable. I quoted step 1.6 in the record, since the verifier said it could not check it.
- **No reader questions:** I added nothing to `questions/001048.yaml`, because the verifier reported no place where the claims file misreads the paper.
- **Bleaching:** still not corrected, following the claims file. The verifier agreed this does not change any outcome.
