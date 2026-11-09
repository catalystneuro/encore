I changed one outcome: figs5b-transition-percent goes from not reproduced to reproduced. I worked through every point in the round-1 report and recorded each in the `verifications` block of the attempt record. The entry re-runs cleanly with `python tools/entry.py all` (336 s, check passes), and I checked every conclusion against the new outputs. Nothing is committed.

**Outcome changes**
- **figs5b-transition-percent:** now reproduced, measured 22.93% against 24.2 ± 2.42. The Supplementary Methods judge whether an SWD started in NREM using the six epochs before it (wake and REM use only the one epoch before). The claims file had used the one-epoch rule for NREM too, which gave 36.3%. I corrected the criterion, and the claims file and a deviation both say this was done after the analysis had been seen. The verifier itself gave not_reproduced under the old criterion, so round 2 will review this change. The claim's wild-type part still can't be tested.
- **fig2e and fig5a-het-more-nrem-swds:** still blocked, but the reason is now `data_missing` instead of `other`, as the verifier gave. The paper's other seven wild-type rats are not in the dandiset.
- **All other outcomes are unchanged.** The verifier agreed with all 34 as they stood.

**Added outputs**
- **Two doubtful rats:** every genotype test is also run without GRIN2B-228 (a Grin2b+/- rat with almost no SWDs), without GRIN2B-238 (a wild-type rat with none), and without both. What changes:
  - Without 228, fig5c would meet its criterion (13 of 13, p = 0.0095).
  - Without 228, fig3d and fig3g-rem-total lose significance (p = 0.060).
  - Without 238, fig3d's interaction becomes significant.
- **How SWDs are taken out of the sleep states:**
  - Removing only the SWD time keeps fig5f at R = −0.74.
  - With bouts that SWDs do not split, the wake-bout differences reverse and none of the eight fig5def correlations is significant.
- **Mixed model check:** a fitted random-intercept model gives the same genotype and interaction statistics as the split-plot ANOVA for fig2b and fig3d.
- **Spectra:**
  - Per-animal coverage is a median of 5 to 10% of each state's epochs.
  - The spectral-slope rejection, as I read its units, removes no epochs.
  - Using whichever left or right S1 channel is cleaner per animal leaves the fig4 outcomes as they were.
  - I added a printed band-averaged difference for fig4c.
- **GRIN2B-132 counted as wild type,** for the two blocked claims, as an illustration only since its genotype is unknown.

**Corrections**
- The claims file wrongly said a rank-sum test with two wild-type rats needs both below all Het rats. With exact ranks it reaches p < 0.05 when U ≤ 1.
- The notebook header described the scorer's SWD flags wrongly ("one epoch after the events"). They overlap each event, mostly as its last epoch.
- The fig4b and fig4c notes overstated the variants. Without GRIN2B-238, Het beta is higher in 7 of 12 variants, by at most 0.147 and far from significant.
- New finding: the dandiset doesn't record which EEG and EMG channels the lab chose by eye for sleep scoring.

**Not done**
- The cleaner-channel variant uses fewer artefact epochs as a stand-in, because the lab chose by eye and didn't store the choice.
- The band ANOVA still treats an animal's five bands as separate observations, as the paper does. The verifier marked this as not affecting a conclusion; I state it in the notebook.

The paper text and Supplementary Methods are in `paper/`, which git ignores; I deleted the downloaded figures and video.
