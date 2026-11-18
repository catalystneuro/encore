The claims file is ready for an attempt (`ready: true`). Several criteria described the code's method wrongly, and I corrected them from the paper and its code. I cloned the flywalk repository at the pinned commit 4b92add to check this; the pin is right, since it is the last commit before v1.

**Checker:** `claims/okuno-2025.yaml: 30 claims, 29 quotes, 9 statistical values, 0 problems`. There are 9 statistical values now, not 10, because I removed one (fig4e below).

**Changes, by claim**
- **Shared methods**
  - **M4:** every figure uses the code's second SC layer ("Traced", rows 7 and 9). For FlyEM that means traced neurons only. The file did not say this.
  - **M6:** added the null synapse counts the code fixes for each target (normal draws such as rd185-20 for unsegregated synapses), and the fully random draw.
  - **M7:** `makeNeuralSC.m` defaults to a 1000 nm radius, but the paper's 3 um is followed. A selected synapse needs both its pre and post side to meet the bound.
- **fig2b-distkm-smoothing-optimum:** ROI counts changed to the seven the code's Figure 2 block is built for (20 to 1000, without 300). The pinned commit's six-count list is kept as a variant.
- **fig2c-smoothing-plus-poltcomp:** rewritten. The code runs six Mann-Whitney tests (SCKm and DistKm at 20, 100 and 1000 ROIs, SC neuron), which is where 0.001/6 = 1.67e-4 comes from, not 16 pairs. The fifth test has an index slip in the code; I named it. Statistics `n` corrected to match.
- **figs2-1d-highpass-degrades:** the code smooths at 23 voxels (not none), uses 7 cut-offs (not 9) and 6 ROI counts. "Any cut-off" is now "every cut-off".
- **fig2d-log-decline:** the measure is now the code's: the largest r over 12 settings (6 smoothing sizes, each with no nuisance removal or Poly-tCompCor), at 20 to 20,000 ROIs. It was r at the smoothing that maximises the Figure 2b score, which the code does not use.
- **fig2d-fly-values, fig2d-ten-thousand-rois:** dropped the SC (synapse) reading; Figure 2d plots neuron SC only.
- **discussion-twenty-rois:** the readings are now the largest Pearson and Spearman r, over either the Figure 2b grid or the Figure 2d grid.
- **fig4c-segregated-ranking:** the statement put both FlyEM cells first; the legend has AOTU019_R first and DNa02_R second.
- **fig4e-unsegregated-higher:** removed the p=0.832 entry from `statistics`. It checks how the null was built, not the finding, so it stays in the criterion as a validity check. Selection made exact.
- **fig4f-segregated-lower:** the code's selection differs from "cPPSSI of 0.9–1", so both are named as readings.
- **fig4i-reciprocal-higher:** selection made exact (code uses "< 2 um", the legend "≤ 2 μm").
- **fig4h-reciprocal-distances:** the mode and more-than-half thresholds are now marked as choices made here.
- **fig3c-regional-detection:** added a criterion, with "mushroom bodies (aL, bL, etc.)" left open.
- **fig5-wagn:** added a criterion that names the connectome threshold (sc50 or sc140) as open.

**Still open**
- **Figure 2 ROI counts:** the pinned code's active list (six counts) and the layout of its test block (seven) disagree. Both are run.
- **fifth Mann-Whitney test:** what it was meant to compare is my inference.
- **figure-only values:** there is no PDF, so values shown only in figures (Fig. 1d–f, the Fig. 2b curves, Fig. 3d detection) could not be checked.

The main findings all have a claim, and every claim comes from this paper. Only `claims/okuno-2025.yaml` was changed; nothing is committed or pushed.
