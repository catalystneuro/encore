I wrote `claims/000139/10.1016-j.neuron.2010.09.015.yaml`. The quote checker passes it with no problems: 22 claims, 22 quotes found word for word, 9 statistical values.

**Text read:** the NIH author manuscript in PubMed Central (PMC2991102), not the version of record. That covers the main text, Methods, figure legends and the one supplement (Supplemental Figures 1 to 5, Supplemental Text, Supplemental Experimental Procedures). The paper links no code, so every method comes from the Methods, the legends or the supplement.

**Claims:**
- **Quotes:** all 22 have one, so none needed an `inferred` note.
- **Statistics:** 7 claims carry them. These are the p-values for the mean tuning correlations, the regressions on anterior-posterior (AP) location, and Figure 6E's p < 0.001. The paper doesn't name the tests behind the mean-correlation p-values or the Figure 6E asterisks.
- **Expected values:** 6 claims.
- **Criteria:** all 22 have one. A shared method section in the opening comment gives the trial selection, time windows, neuron thresholds, the preferred-direction (PD) model, the cross-validated performance measure, and the PCA and task spaces, each with its source.
- **What this dataset can test:** the archive describes array recordings of monkey J in the maze task, so the claims for that dataset (Figure 4D, 4E, 6D, 7A to 7D, Supplemental Figure 1, the AP analyses) are testable. Five claims rest on data the archive doesn't describe: the speed-task monkeys A and B, the single-electrode monkey J recordings, EMG, and the Figure 6E summary. One is a simulation (Figure 8).

**Details the paper leaves open, and the readings named:**
- **Maze trial selection:** the "proto-trial" is either the condition's mean velocity profile or one representative trial. The r > 0.9 test applies either to the horizontal and vertical profiles separately or to the two joined.
- **Movement onset detection:** either the dataset's own onset times or a hand-speed threshold.
- **Tuning strength** (for the 5 spikes/s threshold and the 1.5× peri-movement rule): either the range across conditions or the standard deviation across conditions.
- **Preparatory window for the PD analyses:** I use the only window the Methods define (200 ms before the go cue to 100 ms after) and mark it as a reading.
- **Test of mean r against zero:** a one-sample t-test, a Wilcoxon signed-rank test, or a t-test on Fisher z.
- **Kinematic space:** the window ends either at 800 ms after onset or at the end of the reach. "Each neuron contributed one kinematic variable" means either repeating the six signals once per neuron or using them once.
- **Segment directions:** the three segments are equal either in time or in path length.
- **Figure 4E:** which neurons enter (both thresholds, or the preparatory threshold only). "Near zero" means either not significantly above zero or an absolute value below 0.1; the 0.1 is not from the paper.
- **Supplemental Figure 1:** the difference at movement onset must be either smaller than in the preparatory window or less than half of it.
- **"Almost always" (Figure 6, per dimensionality):** read as at least 80% of comparisons; the paper gives no count.
- **The maze task space that "did not perform well":** it is compared either with the 3-D peri-movement space or with the other task spaces.
- **Shuffled control:** "poorly" means either below the unshuffled peri-movement space, or also below the kinematic and task spaces.
- **Figure 7B:** "monkey J" (97%) either includes the J-array dataset or doesn't. When the window start slides, either the window end stays fixed or the whole window shifts.
- **AP location of an array unit:** either the electrode's position along the axis or which array it sits on.
- **Figure 7C:** the dimensionality used for the upper limit is either 6 or its best value.
- **Prevalence of preparatory activity at anterior sites:** the paper shows no data, so the readings are either any higher fraction or a Fisher exact test.
- **Figure 8 simulation:** the distribution of initial states, how long the simulation runs, and the averaging interval.
- **Standard choices that can't change the outcome:** random seeds and the number of draws, and whether the variance divides by c or c - 1.

**Missing from the paper that a claim needed:**
- The values plotted only in Figures 4, 6 and 7 are not in the text, so no claim rests on them.
- The trial count per neuron for J-array is 2166 in the Results and 2155 in the Methods; the claim accepts either.
- The archive limits the dataset to 250 training and 100 test trials, far fewer than the paper's. Whether it is the same recording as J-array, and how many conditions it holds, is left to the author.

I have not committed or pushed anything.
