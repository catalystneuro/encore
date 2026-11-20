I checked `claims/markowitz-2023.yaml` against the paper and corrected it, and the file is ready for an attempt (`ready: true`).

**Checker:** `claims/markowitz-2023.yaml: 44 claims, 44 quotes, 38 statistical values, 0 problems`. Before my changes it read 41 claims with 0 problems.

I also cloned the paper's code at commit 14ed714 to check the code details that matter most below.

**Changes, by claim**
- **ed2a-syllable-repertoire:** Extended Data Fig. 2a,b,d include the 2 mice that failed photometry quality control (16 mice in all). The readings now include their experiments.
- **fig1h-syllable-dlight-differs:** added a reading taken from the Methods and Extended Data Fig. 4f: the 0 to 0.3 s peak of each shuffle-normalised average waveform.
- **fig1j-weak-kinematic-correlation:** the criterion used the code's mean over each syllable instance. The legend names syllable-associated dLight, which the Methods define as the maximum from onset to 0.3 s. That is now the first reading and the code's mean the second.
- **fig2b and fig2i:** removed the "p < 0.05" entries. The text names a one-sided shuffle test but prints no P for these panels, so the bound was not the paper's.
- **fig2g-usage-crosscorrelation:** the 7.5-min lag range was credited to the figure, which was never read. It comes from the axis limits in the fig_2g notebook, now cited as such.
- **ed6b-encoding-model-average:** both the Methods and the legend give a velocity lag of 10. That is now the main reading, and the code's 5 is a variant.
- **fig3i-optoda-entropy:** added the controls' P > 0.05 from the legend.
- **fig3jk-post-predictable:** the Fig. 3k legend says stimulation day, while the Results and the code use the day after. The stimulation-day reading is now a variant.
- **fig3l-no-kinematic-effect (and fig3m, which follows it):** the main test now uses the Methods' pre-onset subtraction and z-scoring to catch trials. The code's version without the subtraction is the variant.
- **ed10-target-specific:** the legend could be read as comparing learners with shuffled data, but the code compares learners with controls. The code's comparison is kept and the other is a variant.
- **fig4h-decoding-model:** the source pointed at Fig. 4h, but its numbers come from the Methods' baseline model. Source corrected.
- **New claims:**
  - **fig1f-dip-then-peak:** the dip-then-peak in dLight at syllable transitions. The window is my assumption and is marked as one.
  - **fig2b-across-experiments:** the Results' second finding for Fig. 2b.
  - **fig4h-additive-model-optoda:** the Fig. 4h finding on Opto-DA experiments.
- **fig4i-extra-da-matches-calibration:** added the cross-validation scheme from the Methods, and linked it to the new Fig. 4h claim.

**Open**
- The r and P values for Fig. 2b, 2i and 5b are printed only inside the figures. No PDF was supplied, so they are not recorded.
- The Methods (baseline model) and the Fig. 4h legend (Opto-DA model) print the same P = 7e-18, U = 2,500, f = 1, n = 50. Whether this is one test reported twice can't be settled from the text.
- Extended Data Fig. 10c reports one significant bin of behavioural similarity to the target (P = 0.006). The target-specificity claim does not test similarity bins.
- Some minor findings have no claim: the 67 ms rise and 100 ms decay times, "nearly every syllable instance" having a transient, Extended Data Fig. 5d to i, and reward versus reward-prediction error in Fig. 5e.
- The paragraph numbers in sources can't be checked exactly, because the text has no paragraph breaks.
- I did not re-read every code citation, only those listed in the checks entry.

Nothing is committed or pushed.
