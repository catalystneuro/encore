I've corrected 11 claims and added 3, and the file is ready for an attempt. Nothing was committed or pushed; only `claims/costabile-2023.yaml` changed.

**Checker:** `claims/costabile-2023.yaml: 35 claims, 35 quotes, 0 statistical values, 0 problems`. It was 32 claims before my additions.

I read the full paper and the linked code at the cited commit (`mine_pub` 368d756). The code details the criteria cite match the code: the Bonferroni rule (5 SDs for about 39,700 fit neurons, matching the printed 1.26e-6), the UpSet minimum of 10, the cluster minimum of 25, the 5000-draw enrichment over all fit neurons, and the 3 SE significance rule for the mouse data, among others. The code indeed lacks the analysis behind `lm-recovers-fewer-clusters`. All quotes and sources were correct.

**Changes, by claim**
- **fig1f-mine-fits-ground-truth:** the "simple model fails in most types" test counted the pure-noise type, which no model can predict. It now counts the other seven types.
- **fig3-receptive-fields-slow-stimuli:** "within 0.1 of MINE's or below it" was met by any Ridge result below MINE's. It now requires the best Ridge result to be no more than 0.1 below MINE's for each filter.
- **fig4-taylor-metric-ranks-predictors:** the full-expansion fit is now reported, and marked as not deciding, since the paper gives no level for it.
- **fig5fh-cortex-maps:** the whisk map and the per-session maps from the statement are now shown and marked as not deciding; the paper judges them by eye.
- **fig5i-cortex-receptive-fields:** added tests for "biphasic" (second peak at about 1.5 s, widened by 10%), "excitation stronger than inhibition" and "much sharper". The grab future lag was 0.2 s; it is now the paper's 100 ms, widened by 10%, plus one 15 Hz frame (`processMusall.py`).
- **fig6f-reticulospinal-behavior:** the 0.75 level is now marked as set in this file, not the paper's.
- **fig6g-linear-model-bias:** added the low-complexity part of the statement (the complexity 2 fraction against the all-neuron fraction).
- **figs6-stimulus-neuron-regions:** now says the code restricts enrichment to its list of overview regions. For the olfactory epithelium, two readings are named: the code's pure stimulus neurons, or any temperature-driven neuron (the Results cite the mixed-selectivity panel).
- **fig7a-behavior-feature-regions:** "forebrain" can mean telencephalon only, or telencephalon plus diencephalon; both readings are now named.
- **fig7c-receptive-field-types:** "enriched in the forebrain" was judged by a ranking among four clusters, which the paper never does. It now uses the paper's own enrichment test, against all pure stimulus neurons, with both forebrain readings.
- **fig7f-complexity-anatomy:** the Results cite a "Figure 7G" that does not exist; the criterion now says Figure 7F is meant.
- **New claims** for three Results findings that had none, with methods from `cnn_nonlin_test.py` and `cnn_sta_test.py`:
  - `fig2s1-nonlinearity-metrics-agree`
  - `fig3s1-white-noise-benchmark` (the number of simulations is open: 100 in the Methods, 10 in the code)
  - `fig3s1-training-length`

**What remains open**
- I couldn't render the PDF here, so the values the first reader took from figures are unchecked: the Figure 6F counts behind 0.86, the Figure 6G fractions, the Figure 7E cluster values and the Figure 6E fish counts.
- The figure supplements are online only and not under `paper/`. The claims on them rest on the Results sentences and the code.
- Several criteria still use levels set in this file because the paper gives none. Each criterion says so.

**Ready:** yes. The `checks` entry records all of this with `ready: true`.
