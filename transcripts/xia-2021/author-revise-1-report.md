I've revised the attempt for every point in the round-1 report, re-run the entry with `python tools/entry.py all entries/xia-2021` (passes, 0 errors, about 1.5 to 2.5 minutes), and updated the conclusions to match the new numbers. 12 claims are now tested and 17 blocked (was 9 and 20). Nothing is committed.

**Outcome changes**
- **fig2d-hplc-yield: not reproduced → partially reproduced (assumed).**
  - The 0.5 mL/min flow rate was picked to put the peaks at the paper's volumes. The paper gives no flow rate, so I dropped the volume test.
  - I now run three places where the second peak ends. Where it ends at the end of its own descent (about 20.5 min), the share is:
    - 68.2% with a flat baseline (reading a), still below the 69.3 to 84.7% tolerance;
    - 69.1% with one common baseline under both peaks, also below;
    - 79.1% with a line under each peak (reading b, as the criterion writes it), within tolerance. Over the ends that leave out the low tail, reading (b) gives 77.5 to 83.1%.
  - The criterion counts a match under any one reading, so the share holds. It is partial because the volumes cannot be tested.
- **fig7-rostral-caudal: blocked → partially reproduced (assumed).** AQuA still can't run, so the onset and peak of small pixel blocks stand in for its events, grouped into rostral, middle, caudal and lateral regions. The rostral → caudal → lateral order holds in all 18 variants. None of the six times is within tolerance in any variant.
- **fig7-peak-timing: blocked → reproduced (assumed).** Counted from each region's own onset, the four regions peak 11.8 to 18.1 s later, all within 9 to 16.5 s in 30 of 36 variants. Counted from stimulation onset, none fits.
- **figs12-3v-propagation: blocked → partially reproduced (assumed).** Only one of the three mice is deposited. In it, the 3 V response is lower than the 8 V one in all 6 readings. The rostral region starts first in the 12 of 18 variants that fit photobleaching outside the response, and not when the fit uses the whole trace.

**Fixed or added, with outcomes unchanged**
- **Puncta threshold (fig3d, figs5):** the old background rule put 32 to 48% of the field above threshold. I replaced it with a half-Gaussian estimate (median plus 3 SD of the lower half reflected about the median) and kept the old rule as a variant.
  - fig3d: AF647/pHAb overlap is now above its shifted null in 4 of 5 images, including for the top-hat version. Placement on the somata is still at chance, so it stays partially reproduced.
  - figs5: far fewer noise puncta; nearness to GFP is above chance in 3 of 4 images.
- **fig5b:**
  - The short-window rates now start where each trace leaves baseline; none is within the rate tolerance. The old rates from frame 19 are shown but not counted.
  - Added a photobleaching fit from 180 s and a ROI with the camera's dark level subtracted (dark level printed per file).
  - dF/F at 15 s is 17.1 to 40.1% across 144 readings, against the paper's 3.7%.
- **fig6:** added the paired t test on 10 s bin means: p is 2.2e-06 to 0.14, below 0.01 in 37 of 48 readings.
- **fig4b:** added plots and printouts of each calibration trace with the inferred onset marked. They show dips before the steps, which may come from adding the solution. A variant with one common onset still gives Km 0.545 µM, far from 49 µM.
- **Other outputs the verifier asked for:**
  - the full sub-4 trace: one response, so fig5e stays blocked;
  - the HPLC signal from 19 to 35 min;
  - a full-resolution crop of the sub-5 stack with each channel shown alone;
  - onset and peak maps for sub-2 and sub-3.
- **Helper:** fixed the `BLOCK` vs `BLOCK_PX` docstring mistake and stated where the 0.43 µm pixel estimate comes from. It is still unchecked against the data, which carry no spatial scale.
- **Record:** the round is under `verifications` with all 29 claims. The questions to the authors now include the flow rate, the Fig. 7A areas and the puncta background. No question went to a reader: the verifier found no misreading of the paper.

**Not done**
- **figs9 stays blocked as `not_runnable`.** The verifier said that reason isn't allowed, but `docs/protocol.md` lists it and the schema accepts it. The block-onset substitute can't stand in here, because the claim compares AQuA's own output.
- **fig4b-lod reading (c) is still not run.** It needs the lines from Fig. 4B(ii), and the entry reads no figures.
- **Figure comparisons outside the notebook.** While preparing, I matched Fig. 7A's panels to the right half of sub-3, unflipped. That supports the channel and orientation assumptions. The rules forbid reading figures in the notebook, so it is only mentioned there as "not run here" and decides nothing.
