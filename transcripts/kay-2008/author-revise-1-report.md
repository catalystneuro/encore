I couldn't finish the main ask: the re-run of the entry never completed. I started `python tools/entry.py all entries/kay-2008` at 08:05 and the 2-hour command limit killed it with no notebook written. I can't tell which notebook stalled or why. That left too little time to run it again (about 85 minutes), so I put the entry's code and analysis cells back to the verified version, and every number in the record still comes from the verified run.

**What changed in the outcomes**
- **suppfig4-500-voxels:** blocked → partially reproduced. The verifier was right that the existing output already meets the rule in both repeated-trial conditions, and the criterion calls two of four conditions "partially". The single-trial conditions stay blocked.
- **suppfig11-rf-size-eccentricity:** reproduced → partially reproduced, marked as resting on an assumption. I took the verifier's point that Figure 2's legend calls the white circle "the bounds of the stimulus", so a circular bound is the better-supported reading. Under it the V1 < V2 < V3 order holds in only 3 of 6 one-degree bins. Size rising with eccentricity still holds in every area.
- Everything else is unchanged.

**What I added or corrected**
- **supptable1-predictive-power-by-area:** counting voxels with missing values as not significant is now a stated assumption, with the reason. The result over only voxels without missing values (3 of 6 within tolerance) is now given too.
- **Retinotopy-only model:** the luminance channel is measured from the grey background, where the paper subtracts the mean luminance. This is now recorded as a deviation; the paper's reading did not get run.
- **Tuning-curve ratios:** I corrected the false docstring on grating amplitude in `vim1.py`. The fig2 and suppfig7 conclusions no longer rely on the curves that include the DC offset, and suppfig7 now says it is not reproduced only for the readings that were run.
- **New deviations on fig3:** the O1 (a) voxel p-values use the image being identified, and about 30% of initial fits stop at iteration 0 and give the voxel no model.
- **Single-trial and SNR notes:** they now admit the cost estimate was overstated, and say how far the revision got.
- **Questions for a reader** in `questions/kay-2008.yaml`, both on the noise ceiling:
  - The data have 13, 14 or 15 trials per image, where the claims file says 13 or 14.
  - The claims file samples the predicted patterns one trial at a time; the paper's wording suggests averaging all of an image's trials.
- **Round 1 recorded** under `verifications`, with the verifier's reasons and my responses.
- I edited the conclusion text in both the notebook and its executed copy without re-running. No fresh run stamp exists, so the workflow's run will execute the notebook again. `entry.py check` passes with 0 errors.

**What I did not do**
- **Single-trial identification, noise ceiling and SNR:** these stay blocked as too large. I wrote a fast time-series fit and tried it on two sessions of S1 outside the notebook, where it closely matched the data set's own response estimates. The second notebook built on it was part of the run that never finished. That code was only in a temporary folder and is gone.
- **Written but never run, so removed with the reverted cells:** the paper's luminance reading for the retinotopy-only model, the stricter suppfig11 filter and per-area receptive-field sizes, the Gaussian-centre and grating-amplitude checks for fig2, the printout of all four suppfig4 readings, and the extra-seed checks.
- **Not attempted:**
  - The bootstrap variant for the main field-of-view reading: about 100 minutes.
  - The model-I reading for suppfig7: it needs the constrained models, which aren't built.
  - The set-size-120 orderings for suppfig8.
- **The verifier's point on errors-similar-images:** I didn't change it, because the claims file itself counts the selected image among "the other 119 images".
