The file is fit for an attempt: I set `ready: true`. The checker's final result line is `claims/clark-2026.yaml: 30 claims, 30 quotes, 1 statistical values, 0 problems`. Before my changes it read 29 claims and 0 problems.

The paper's code is public at the commit the file cites (245726f). I cloned it to `$TMPDIR` and checked each claim's method details against it. Most matched. Nothing was committed, and only `claims/clark-2026.yaml` was changed.

**Changes, by claim**
- **fig6cd-eigenvalues-real-degenerate:** this was the one real error. The statement called the eigenvalues "products" of the Fourier coefficients. Equation (9), the mean-field section and the supplement give a ratio: the average activation slope times the input-current coefficient over the firing-rate coefficient. Corrected.
- **fig3c-correlation-approaches-circulant:** the statement said the eigenvectors "are" Fourier modes. The paper says they "converge to" Fourier modes. Corrected.
- **hd-cell-selection:**
  - The statement said nine mice "have an optogenetic file", which the paper does not say. It now says they underwent optogenetic manipulation in a separate epoch.
  - The 1,533 count was described as units with a non-zero tuning curve. That filter is a code step; the paper says all units carrying the head-direction label. The count is now reported with and without the code's filter.
- **Header comment:** reworded the `+ogen.nwb` remark. The code reads the square-environment epoch from that file when a session has one.
- **fig2b-sorted-weights-mexican-hat:** the criterion said the weights are computed in "dual form". The code takes its primal branch here; the result is the same. Corrected the label.
- **fig5c-peak-counts-match:** added that the code's histogram counts only curves with 1 to 5 peaks.
- **fig4-generative-fit:** added that the fitting script, as written, needs a GPU, so the paper's random draws may not be reproduced. The tolerances cover this.
- **fig2l-recorded-bump-tracks-hd:** said that leaving out bins without a tracked head direction is this file's choice; the notebook keeps them.
- **figs8-s9-lambda-and-c:** added the supplement's statement that any c above 0 prevents divergence, and named the code's c grid, initial-condition noise and 5-ms step.
- **figs14-data-spectrum-doublets:** changed the leading 11 eigenvalues to 10, the number Supplementary Fig. 14a plots.
- **fig8-grid-scores-and-torus:** said how the code sets σ (it uses a radius of 0.35, not σ directly), and that the convergence measure is this file's.
- **figs1-s2-spectrum-does-not-fix-symmetry:** marked the 5% eigenvalue test as chosen here, since the notebook computes no eigenvalues, and named the two initial amplitudes the code uses.
- **New claim fig7de-dmft-timescales:** covers the Fig. 7d,e convergence and divergence timescales, a main-text finding that had no claim. Its measures are chosen here and named as open.

**What remains open** (all recorded in the `checks` entry)
- The notebooks print none of the Fig. 5d counts (412, 55, 24,271, 1,043), so these are checked only against the figure legend.
- The code names no mouse; it picks sessions by head-direction cell count. The names A3707, A3716, A3711 and A3706 and their counts come from the legends of Figs. 1e and 2 and Supplementary Fig. 13.
- Whether each `+ogen.nwb` file holds the square-environment epoch cannot be told without opening the data. The author needs to confirm it.
- Words like "comparable", "match", "tracks" and "a few" still rest on thresholds this file chose. They are named as open in each criterion, because neither the paper nor the code fixes them.

All other statements, sources, quotes, the Kuiper statistics and the expected values match the paper.
