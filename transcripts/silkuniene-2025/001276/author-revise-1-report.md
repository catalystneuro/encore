No outcome changed. Three outcomes are now marked as resting on an assumption. I re-ran the entry with `python tools/entry.py all`: 0 errors, and the notebook passed in 1445 s. Every number in the record, notes and conclusions comes from that run. I did not commit anything.

**Outcomes**
- **Unchanged, now marked as resting on an assumption:**
  - **fig7be-center-linear-with-bursts** stays partially reproduced. With the three left-out wells added, the CT26 slope p is 0.00098 (individual experiments). That is just under 0.001 and would make the claim reproduced. I kept the exclusion as the adopted choice, because footprints are not found in these wells and their placement is less certain.
  - **fig7-offtarget-40-50-fold** and **fig4b-40-fold-at-02mhz** stay not reproduced. Both rest on the background being the median of the four footprints. With some single footprints the 6 mm ratios fall in range: 42.3 and 53.7 for the first claim, and 35.75, 38.41 and 40.38 for the second. I tried every way of taking one footprint per well: 62.5% of the 64 ways, and 42% of the 1024 ways, put at least one reading in range. I added "which footprint gave the background" to the question for the paper's authors.
- **Kept, with the disagreement recorded:**
  - **fig3a-cancan-center-enhanced** stays partially reproduced; the verifier would give not reproduced. My reason: the CANCAN part holds and the control part fails, which is "holds only in part".
  - **fig5c-irreversible-center** stays blocked as `other`; the verifier would give `methods_underspecified`. The paper says its Hoechst check was made after exposure, to show cells had not detached (Methods 2.4, Results 3.2), and a pre-exposure image cannot show that.
  - **The other cross-dataset blocks** keep `other` where the verifier said `data_missing`. The data appear to be public in DANDI:001047, 001277 and 001284, which `data_missing` excludes.

**Added or corrected**
- **Pixel size:** it is in the OME-XML appended to each description (1.625 µm). I parse it now, together with exposure (FITC 200 ms, DAPI 600 ms), camera and objective, and stage position. The Hoechst and YP images of all 52 wells that have both share a stage position. I corrected the helper docstring and the finding.
- **Background readings:** results under each single footprint, the lowest, the highest, and every per-well assignment.
- **Left-out wells:** refitted with the angle fixed at that of their plate and day, shown in a figure, and run as a variant wherever they enter a claim.
- **Camera saturation:** at most 5.4e-4 of the pixels in any diagonal ROI are at full scale, and none at the center, so it does not explain the CT26 6-burst plateau.
- **YP half of fig5b:** R² is 0.979 for the Lorentzian and 0.975 for the Gaussian. Both are within tolerance and the Lorentzian fits better. The claim stays blocked for lack of propidium images.
- **Pre-exposure Hoechst (fig5c):** inside the footprints it is 0.74 to 0.99 of the monolayer level and 20 to 60 times the camera offset.
- **Smaller checks:**
  - The Lorentzian p with two fewer degrees of freedom is 0.0027 for 1 Hz sides at 1 mm spacing; all eight fits pass at 0.5 mm.
  - The deviation measure restricted to ROIs inside the array still holds.
  - The fig7cf notes now say the pass is fragile, and the fig3/fig4 notes give where the wells come from.
  - The helper docstring now notes the verifier's center bias.
- **Text fixes:** the 4-burst ratios are "7.7 and 7.9", not "7.7 and 2.9"; CT26 comes from three experiment dates, not two; the runtime is now 25 minutes. I also recorded the round under `verifications` and updated the README.

**Not done**
- No questions file: the verifier found no place where the claims file misreads the paper.
- I did not correct the center bias of the square fit. I state it instead, since the verifier found it cannot change an outcome.
