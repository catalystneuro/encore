I checked the claims file against the paper. The file is ready for an attempt (`ready: true`). Nothing is committed.

**Checker:** `claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml: 34 claims, 33 quotes, 43 statistical values, 0 problems`. It also passed with 0 problems before my edits (39 statistical values then).

**Changes, by claim:**
- **fig1-example-pair:** added the two per-pair Pearson tests (p = 0.04 visual, p = 0.3 vestibular) under `statistics`. The statement already reported them.
- **fig2a-behavioral-learning:** the expected value 2 ± 1.3 covered 0.7 to 3.3 degrees, but the criterion and the protocol's range rule give 0.9 to 3.3. Changed it to 2.1 ± 1.2.
- **fig4-tuning-width-visual:** the selection now says tuning "in the horizontal plane", as the Results do, and gives the group sizes from the Figure S4 legend.
- **fig4dh-lateral-more-sensitive:** the Poisson variance was cited to Gu et al. 2010, which is not this paper. It now comes from equation 4. Two details the paper leaves open are now named, each with readings: how the preferred heading is computed, and whether the ANOVA was run per condition or once with condition as a factor.
- **fig8ab-choice-probability-lateral:** now uses the preferred-heading readings of fig4dh.
- **figs4-population-sensitivity-any-reference:** the legend's "100 neurons were resampled with replacement" can be read two ways. Both are named: populations of 100 neurons, or 100 resamples of the whole group.
- **fig5-regression-coefficients:** added a third reading, where the slopes from the naive fit are used for both groups, as the Results describe the naive structure.
- **fig6a-population-thresholds:** the tuning amplitude and baseline (30 on 10 spikes/s) are now marked as a choice, not taken from the paper.
- **fig6b-slope-not-intercept:** the grid range was said to be "read from Figure 6B", but the figure could not be rendered. It is now marked as a choice.
- **fig8cd-noise-not-preference:** the only reading (89 trained pairs under 1 mm, 178 points) does not fit the legend's 328 fixation points. I widened the readings to all trained pairs and all 179 pairs, with and without the 55 discrimination-task points. The claim is judged under the reading whose counts come closest to 328 and 55.
- **figs5-congruency:** the ANCOVA part of the statement had no criterion. I added one from the Figure S5 legend, plus its two other terms (p > 0.7 and p > 0.8) under `statistics`.
- **discussion-stimulus-reduces-correlation:** now says the paired t test is a standard choice, since the paper names no test.

**Still open (recorded in `checks`):**
- **Trained intercept tolerance:** fig5-regression-coefficients keeps the protocol's 10% tolerance on the trained intercept of 0.005 (± 0.0005). No estimate from 89 pairs can meet it, so the claim will likely only reach its partial criterion.
- **Figure-only details:** the PDF could not be rendered in this run either. The Figure 6B axes and the garbled "approximately" signs before "5-fold" and "8%" were not checked against the figures.
- **Data from earlier studies:** Figure 2A, Figure 4, Figure S4 and Figures 8A and 8B use the authors' earlier single-electrode recordings and training histories. Whether stc-1 holds them is for the author to find.

Coverage is complete: every main finding has a claim, and every claim comes from this paper.
