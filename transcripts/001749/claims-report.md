I wrote `claims/001749/10.1038-s41586-022-04507-5.yaml`. The checker reports 46 claims, 46 quotes, 123 statistical values and 0 problems. The earlier claims run stopped because the Methods were missing; they are now present, so this run could write claims.

**Text read:** `paper/10.1038-s41586-022-04507-5.txt`.
- **Main text:** the PMC author manuscript (PMC9576144). It has the main text and the legends of Figures 1 to 4 and Extended Data Figures 1 to 10.
- **Supplement:** the Nature supplementary information, which holds Methods sections 1 to 17. Its equations are garbled; only the alignment index was needed, and I read it from the cited source (Miri et al. 2017).
- **No PDF:** there is no main-text PDF, but every number used is printed in the legends.

**Code read:**
- **HMMGLM** (github.com/Tyelab/HMMGLM, commit 3fc3567). It fixes 6 states, 100 epochs, the learning-rate schedule, the initialisation and penalty, contiguous 10-fold blocks, one-step prediction, and per-fold AUCs with and without the one-bin shift. The repository also holds the paper's processed input (`dataset_forHMMGLM_proc.mat`), which I did not open.
- **AlphaTracker** (head 43e1264). It holds only tracking and clustering, no analysis of ranks or neurons.
- **Not linked:** there is no code for the PCA trajectories, SVM decoding, responsive-cell analysis, phototagging or behavioural statistics.

**Counts:** 46 claims, all with quotes and all with criteria. 39 claims carry statistics (123 values in total), and 9 have expected values.

**Pinned from the paper's own numbers:**
- Each SVM p = 2×10⁻⁴ is a Wilcoxon rank-sum of 10 fold AUCs against 10 shuffled AUCs, using MATLAB's normal approximation.
- p = 0.004 is a sign test with all 9 behaviours above chance.
- p = 4×10⁻⁵ is an exact rank-sum of 9 against 9.

**Open details and the readings named:**
- **Trajectories:** 148 PCs as printed, or as many as reach 90% of variance; neuron matching by one subsample, or a new one per iteration. Baseline and event are read as −5 to 0 s and 0 to 5 s.
- **SVM:** feature window −5 to 5 s or −30 to 30 s; classes balanced or all trials used. Label permutation for the shuffle and 100 ms bins are taken as standard choices. For the "~30 s before" claim: one pre-cue model, or 5 s windows.
- **Responsive cells:** signed-rank level 0.05 or 0.01; z-score against the −5 to 0 s baseline or the whole window; Fisher denominator all cells, or cells at 0.05 Hz or above.
- **HMM-GLM:**
  - Spike threshold on negative crossings only, or both directions; counts or z-scored rates per bin.
  - AUC with or without the one-bin shift; folds contiguous or random.
  - The 14 s window's alignment (−2 to +12 s) is taken from the dandiset description; the paper gives only the length.
- **Number of states:** "plateau" read as within one SEM of the best, or the highest mean; states tried read as 1 to 10.
- **Alignment index:** number of PCs is 90% of variance, 8 or 3.
- **Firing-rate variance and rate of change:** the time span and whether variance is across bins or across trials.
- **Fig. 1c "time displaced":** displacing the competitor, or being displaced.
- **Fig. 4b:** "reward delivery (0–2 s)" is after delivery or after tone onset; z-scored or raw rate; the alone-against-competition test is unnamed (read as a rank-sum) over 0–10 s or 0–5 s.
- **Ext. Data Fig. 7:**
  - Distance window for 7b; close/far split by median or by port contact range.
  - Significance level for the "distance-correlated" cells in 7f; the event of 7f's second panel is unnamed.
- **Other:**
  - The common subspace for alone against competition trajectories.
  - Hierarchical-clustering linkage method.
  - How ties count in competitions won.
  - Early against late trials.
  - Winner and loser panel order in Ext. Data Fig. 8d.

**Missing or inconsistent in the paper:**
- **Ext. Data Fig. 10c:** the legend's Fisher test (p = 0.011) names no event, and no event's printed counts give 0.011 (the closest are 0.006 and 0.06), so every event is listed as a reading.
- **Two counts that differ:** mPFC-LH tagged neurons are 42 in Fig. 4b and 43 in Ext. Data Fig. 10c; both are accepted.
- **A likely copy error:** Ext. Data Fig. 7d–e prints the same F and p for "win far" and "lose close"; I recorded it as printed.
- **No deposited evaluation frames:** the AlphaTracker precision claim needs the annotated frames, which the paper does not deposit.
- **Not checked against the dataset:** whether it holds the unimplanted cohort, the alone sessions, the ex vivo data and the optogenetic data. That is for the author to find.
