The claims file for 000128 is ready for an attempt: the last check says `ready: true`. I changed eight existing claims and the header, and added one claim. Nothing is committed or pushed.

**Checker result:** `claims/000128/10.1016-j.neuron.2010.09.015.yaml: 22 claims, 22 quotes, 9 statistical values, 0 problems`. It was 21 claims with 0 problems before my edits.

**Changes, by claim**
- **Header, M6:** the thresholds now match the Methods' wording: more than 5 spikes/s for J-array, at least 10 spikes/s for the single-electrode datasets.
- **recordings-jarray:** the criterion now says why the condition count has zero tolerance: it is a count fixed by the task design, not a measurement.
- **recordings-single-electrode:** the statement gives mean trial counts (311, 492, 388) that had no quote or expected values. I added both, from Results, Behavior and recordings.
- **fig2b-example-concordant-tuning:** "prefers up and left" had no measure. I added a reading taken from the Figure 2B legend (near/fast conditions, rate 50 ms before the go cue) and labelled it as a reading.
- **fig2ce-example-opposing-tuning:** the criterion only used the 7 far/fast conditions. The paper doesn't say which conditions these correlations used, so I added the 28-condition reading as well.
- **fig4abc-mean-correlation-single-electrode:** the statement gives mean Spearman values that had no quote or expected values. I extended the quote and added three expected values.
- **fig6-each-dimensionality:** "almost always" rested on one threshold the first writer chose. I added a second reading (at least 90% of comparisons) and a rule for when the two readings disagree.
- **fig6e-summary-across-datasets:** the statement said task spaces are "outperformed" where the paper says "largely outcompeted", so I restored "largely". The criterion also didn't test two parts of the statement: that the gap grows with dimensionality, and that task spaces rank below the kinematic and EMG spaces. I added readings for both.
- **New claim, fig4-no-separate-populations:** a Results finding that had no claim. It says the correlations show no separate concordant and opposing groups and are centred near zero. The paper names no test, so both readings in the criterion are mine and are labelled that way.

**Still open** (recorded in `checks`)
- **fig3-maze-most-not-maintained:** r ≥ 0.72 is used as the cut-off for "similar tuning". The paper sets no threshold; 0.72 is just the one value it calls "quite high".
- **Header, M9:** when the dataset doesn't mark the end of a reach, it is taken as speed falling below 5% of peak. The paper doesn't define the end of a reach, and this choice could shift the endpoint, halfpoint and segment spaces.
- **fig7c-anterior-posterior-performance:** the paper fixes neither the dimensionality of the upper-limit space used for normalising nor what "within the spread" of the random subdivisions means.
- **fig8-model-weak-correlation:** the second part of the statement (one preparatory rate leading to opposing patterns) isn't tested. The paper shows it only by example.
- **fig4e, suppfig1, fig6-performance-vs-dimensionality, fig7a:** these turn qualitative words into thresholds the paper doesn't give. Each is labelled as a reading in its criterion.

The other paper under `paper/` (10.1038-nature11129) isn't used by any claim. Several untracked files outside `claims/` (dotfiles, `scripts`) were already in the working tree; I left them alone.
