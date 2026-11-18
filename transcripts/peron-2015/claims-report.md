I wrote `claims/peron-2015.yaml` with 43 claims, and the checker passes: 42 quotes found word for word, 18 statistical values, 0 problems.

**Text read:** the version of record with its full Supplemental Information (Figures S1 to S7 legends, Table S1, Supplemental Experimental Procedures), from `paper/10.1016-j.neuron.2015.03.027.txt`. The paper links no analysis code. It names only ScanImage, the Janelia Whisker Tracker, BControl and an unnamed MATLAB package, and none of these settles an analysis choice. I could not render the PDF here (no renderer was available and installing one failed). So numbers printed only inside the figures were not read, and no claim rests on them: the per-population percentages of Figure 3 and the Pearson r and p of Figures 8E, 8I and 8K.

**Counts:**
- 43 claims, 42 with quotes. The one without is `table-s1-roi-counts`, marked `inferred` because Table S1 has no sentence stating it.
- 10 claims carry 18 statistics entries.
- 41 have criteria and 27 have expected values.
- One claim, the event-detector validation, uses data from elsewhere: the Chen et al. 2013b recordings, for which the paper gives no archive. All others use the dataset.
- The dataset description mentions the eight volume-imaging mice. Whether it also holds the learning mice, L4 axon mice, anesthetized mice, L5 soma–dendrite pairs, high-resolution stacks and column outlines is left for the author to find.

**Details the paper leaves open, with the readings named.** Shared methods M1 to M7 are in the opening comment.
- **Task-related test:** the time bin (one 7 Hz frame), and whether events are shuffled within each trial or across the session.
- **Trial-type discrimination:** whether the trial itself is left out of the mean PSTH (in or out).
- **Encoding model:**
  - penalty scale: one value chosen by cross-validation on a random subset of ROIs, or one per neuron;
  - tent knots: equally spaced over the variable's range, or at its quantiles;
  - kernel lags: causal, or centred on zero;
  - frames entering the fit: all imaged frames, or trial frames only.
- **Summaries:** mean of per-mouse fractions or fractions pooled over mice; ± read as SD, with SEM as a variant.
- **Whisking amplitude:** range over the trial, range over the sample epoch, or peak Hilbert amplitude.
- **Days to criterion:** day 1 counted from the first training day, or from the first day of the full task.
- **Learning statistics:** the rank-sum test over 8 day values per group, with per-mouse means as a variant. For the trimming and neurometric tests, which the paper does not name, I read them as rank-sum tests.
- **Neurometric decoder:** its input (sample epoch, or up to the reward cue); the score per day (best of 100 groups, or their mean).
- **Pseudo-session splits:** random pairs of consecutive trials, or random halves. Rfit-vector neuron set: all neurons imaged on both days, or those passing on either day.
- **Directionality index:** "maximal" curvature change read as the end knots, or the 1st and 99th percentiles.
- **Tuning-stability shuffle:** a null of random neuron pairs on the same day pairs, or on any days.
- **Map voxels entering the L4 and neuropil correlations:** all shared voxels, or those within one barrel width of the centre.
- **Anesthetized response window:** 1 s or 2 s after deflection.
- **F0 percentile by skew:** 5th percentile for all, or the median for all.
- **The Discussion's "correlation-based approach":** two possible definitions, given in the claim.
- **Other open details:**
  - the mouse sets behind the "n = 5 volumes" and the "3 trimmed mice";
  - the nucleus-matching parameters for the fraction of neurons imaged (that claim is blocked as underspecified unless the dataset carries the nuclei counts);
  - the clustering threshold for the pairwise-distance test (the paper names no test, so a threshold is set in that claim).

**Missing or inconsistent in the paper:**
- The p-values for several tests are given without the test named (surround whisking against touch, the L5 and GABAergic comparisons, trimming, neurometric). I read them as the test of the neighbouring sentence and said so in each claim.
- The r and p for the directional maps are printed only in the figures, which I could not read.
- Apical dendrite counts disagree: 2,469 in the Results, 2,496 in Figure 3. The claim accepts either.
- Principal and surround column labels and the row axis are needed by many claims; without them in the dataset those claims are blocked.

As instructed, I committed nothing.
