I wrote `claims/000138/10.1016-j.neuron.2010.09.015.yaml`. The quote checker reports 15 claims, 15 quotes, 9 statistical values and 0 problems. Nothing is committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC2991102, NIHMS240235), not the version of record: main text, Methods, figure legends, and its one supplement (Supplemental Figures 1 to 5, Supplemental Text, Supplemental Experimental Procedures). The paper links no code, so none was read.

**Dataset.** By its archive description, 000138 (MC_Maze_Large) is maze-task array data limited to 500 train and 100 test trials. It can hold at most part of the paper's J-array dataset, which had about 2166 trials per neuron. Claims on monkeys A, B and J single-electrode data are included because they are main findings.

**Claims.**
- 15 claims, all with quotes, none inferred.
- 6 claims carry statistics: the mean-correlation p-values for each dataset, the four AP-regression r and p pairs, and the Figure 6E p < 0.001.
- 7 claims have expected values. The 10% default tolerance is used, except for the 7 to 10 dimensionality range (widened by 10% of each bound) and the oscillator r = 0.08, which comes from one random draw and is judged against a distribution of draws.
- 14 claims have criteria; Figure 4A-C is settled by its expected values.
- The Figure 8 oscillator claim is marked `with_inputs`, since it is a simulation that uses no recorded data.

**Details the paper leaves open, with the readings named:**
- **Movement onset detection:** the onset the data provide, or a speed threshold (threshold open).
- **Maze "proto-trial" for trial selection:** the condition's mean velocity profile, or its median trial.
- **"Spikes/s of tuning" for neuron inclusion:** range of condition means, or SD across conditions.
- **Test for mean correlation above zero (not named):** t-test on r, t-test on Fisher z, or Wilcoxon signed-rank.
- **Leave-one-out:** PCA space computed once from all conditions, or recomputed without the left-out condition.
- **Performance normalization:** per-neuron variance, or a pooled ratio.
- **Neurons entering the peri-movement matrix:** all units, or included units only.
- **Kinematic matrix:** window end (neural-window end or reach end), and how the six variables are replicated.
- **Task-space geometry:** reach end; halfpoint and segments split by path length or by time.
- **Range of dimensionality k:** 1 to 14, or 1 to 12.
- **AP location for array units:** electrode coordinate, or which array.
- **Figure 6E significance test (not named):** paired t-test, or Wilcoxon.
- **"Monkey J" in the Figure 7B 97% value:** J-array alone, or J and J-array averaged.
- **Figure 7C upper-limit normalizer:** taken at k = 6, or at its best k.
- **Figure 8 simulation:** initial-state distribution (uniform or Gaussian), and the gray interval (360 or 180 steps).

**Thresholds I set myself.** The paper gives no numbers for "near zero" (Figure 4E), "almost always" (set at 80%), "performed poorly" (Figure 7A) or "only slightly different" (Figure 7C). Each criterion says so.

**Missing from the paper:**
- The main-text PDF was not available, so Figure 6A-D (per-dataset performance curves and the k range plotted) and the per-dataset values in Figure 7 could not be read.
- No neuron counts are given after the inclusion criteria.
- The paper is inconsistent on J-array trials per neuron: 2166 in the Results, 2155 in the Methods. This is noted in the file's opening comment.
