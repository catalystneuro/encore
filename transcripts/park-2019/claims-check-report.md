I checked the claims file for park-2019. I made six corrections, and it is ready for an attempt (`ready: true`).

**Checker result:** `claims/park-2019.yaml: 22 claims, 22 quotes, 32 statistical values, 1 problems`. The one problem is p = 1e-9 in fig1d-preference-change. The Figure 1D legend prints it as "p = 10�9": the minus sign was lost when the text was extracted from the PDF, the same garbling as the other exponents in the file. The value is the paper's, so I left it.

**Changes, by claim:**
- **fig1c-speed:** I removed the reading that uses each cell (n = 115) as the unit. The degrees of freedom, F(2.02, 74.68), imply about 38 units; 115 cells would give a denominator near 230.
- **fig1c-directionality:** the criterion now requires both stable trials to be above the room frame, as the legend's order "stable1 = stable2 > rotating-room frame" says. Before, it required only stable2.
- **fig2-decoding-stable-vs-rotating:**
  - The paper gives no summary measure of decoding error, so it is now named as open, with two readings: median or mean absolute circular error.
  - The "at least four of seven ensembles" threshold is now marked as an assumption.
  - Stable2 is now compared with the room frame and the arena frame separately, since the paper says room-frame decoding was similar to stable2 in some ensembles.
- **fig4-internal-tuning-preserved:** the file said the Methods put the second cell's spikes after the reference spike. They don't specify a side. I read the linked code (Spike_triggered_FR_curve.py, commit 545a738), which takes the second cell's spikes before the reference spike. Under protocol step 2 (code settles what the Methods leave open), the code's side is now the main reading and the other side a variant.
- **fig4c-arena-registration-short-lived:** the legend prints the two one-way ANOVA bounds with the inequality signs reversed ("F ≥ 1.59, p > 0.19" and "F ≤ 23.73, p < 10^-14"). The file had silently swapped them; the statistic strings now say they are read as a misprint.
- **fig5c-error-minima-at-cues:** I reworded the statement to follow the Figure 5C and 5D legend. The minima match the cue edges in the room frame but not the arena frame; the old wording read as if the minima were absent in the arena frame.

**Still open (recorded in `checks`):**
- **figs2-frame-preference:** the cut-off for "no frame preference" is not in the paper, which says only "clear" preference. The file's two readings (a factor of 2, or both probabilities below 0.05) remain assumptions.
- **fig2c-proximity-anticorrelation:** the paper gives two averages for the same correlation (−0.141 ± 0.029 and −0.132 ± 0.024) without saying how they differ. The criterion accepts either.
- **fig4c-arena-registration-short-lived:** the paper does not define "strength" of the internally referenced tuning. The only reading given is the Rayleigh vector length.
- **figs5 and figs6:** I did not read the Gaussian process model code (pfgp), so the lattice resolution and time bin are still left to it.

Every main finding has a claim, and every claim comes from this paper. I did not commit anything, and I left the existing change to `tools/entry.py` alone.
