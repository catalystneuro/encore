I wrote `claims/000140/10.1016-j.neuron.2010.09.015.yaml`. The quote checker reports 20 claims, 20 quotes, 9 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the NIH author manuscript in PubMed Central (PMC2991102), not the version of record. That covers the Results, Discussion, Methods, figure legends and the one supplement (Supplemental Figures 1 to 5, the Supplemental Text and the Supplemental Experimental Procedures). The paper links no code, so every method comes from the Methods, the legends or the supplement. The archive names this dandiset MC_Maze_Small, which the file reads as part of the monkey J maze-task array data ("J-array"). The opening comment describes all four datasets as the paper reports them.

**Claims.**
- **Quotes:** all 20 claims have one, so none needed `inferred`.
- **Statistics:** 6 claims record them:
  - the mean tuning correlation tests (p = 0.03 for J-array; 0.01, 0.01 and 0.12 for A, B and J);
  - the regressions on anterior-posterior location (four r and p pairs);
  - the Figure 6E asterisks (p < 0.001).
- **Expected values:** 5 claims carry them: mean Pearson and Spearman r per dataset, the 7 to 10 dimensions for 90% of preparatory variance, the 97% and 94% ratios in Figure 7B, and the simulated r = 0.08.
- **Criteria:** 18 claims have one.
- **Data elsewhere:** the claims for monkeys A, B and single-electrode J, and those needing EMG (Figures 6A to 6C and 6E), are listed but are probably not in this dandiset. The Figure 8 claim is a simulation and uses no recorded data.

**Details the paper leaves open, with the readings named:**
- **O1, "spikes/s of preparatory tuning":** the range across conditions, or the standard deviation across conditions.
- **O2, peri-movement tuning "1.5 times as strong":** O1 applied to the epoch means, or to the largest value over time within the window.
- **O3, movement onset:** the dataset's marker, or a speed-threshold onset.
- **O4, the maze "proto-trial" filter:** the best-matching trial, the condition mean, or no filter if the trials are already curated.
- **O5, time step of the matrices:** 10 ms, a standard choice.
- **Test behind the correlation p-values:** one-sample t-test on r, the same on Fisher-z values, or Wilcoxon signed-rank.
- **Test behind the Figure 6E asterisks:** paired t-test or Wilcoxon signed-rank.
- **Range of PCA dimensions:** 1 to 14 or 1 to 20.
- **Kinematic matrix:** each of the six kinematic variables repeated to match the neuron count, or each used once; the window ending at 600 ms or 800 ms.
- **Units in Figure 4E:** those of Figures 4A to 4D, or all tuned units.
- **Intermediate conditions in Supplemental Figure 1:** taken at the 1/3 and 2/3 ranks.
- **Shuffle in Figure 7A:** drawn per unit and condition, or per condition only.
- **"Monkey J" in the 97% figure:** the array data, the single-electrode data, or both.
- **Space used for each half in Figure 7C:** built from that half's units or from all units.
- **Normalisation for the dimensionality count:** none, or z-scored units.
- **Simulation settings:** the initial-state distribution and averaging interval.

Where the paper gives no test (the broad distribution in Figure 4, "near zero", "almost always", "poorly"), the criterion sets its own threshold and says so.

**Missing from the paper.** Values shown only in the figures (the Figure 4 histograms, the Figure 6 and 7 performance curves) are never stated in the text, so no expected value rests on them. Unit counts after the inclusion criteria are not given. Anterior-posterior locations for the units are not given. The "more preparatory activity at anterior sites" finding is "data not shown", so the method used to test it is set in the criterion.
