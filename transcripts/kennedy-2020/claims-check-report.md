I checked the file against the paper and corrected eleven things. The last check marks it ready for an attempt (`ready: true`).

**Checker result:** `claims/kennedy-2020.yaml: 39 claims, 38 quotes, 107 statistical values, 2 problems`. Both problems are p-values the checker could not find in the text: 1.8e-05 in fig1km-thigmotaxis and 5.2e-05 in fig1lmn-silencing-before. I found them by reading Supplementary Table 1, ED 3a, where they are printed as 1.80E-05 and 5.20E-05 with a non-standard hyphen. Every other recorded statistic matches that table.

**Changes, by claim:**
- **fig1de-toy-weaker / ed1-urine-looming:** I moved the ED 1k rat-against-toy test from ed1-urine-looming to fig1de-toy-weaker, since it is about the toy. I also removed "shorter decay than to the rat" from ed1-urine-looming: the paper never gives the direction, and the table's intervals are signed differently from row to row.
- **ed2abc-no-lingering-odor:** the paper names no test, so the t-test is now stated as a choice made here. The averaging window is named as open, with two readings.
- **ed3fi-kinetics-track-thigmotaxis:** the "no difference" part now names the paper's paired t-test (ED 3g).
- **fig1j-silencing-reduces-avoidance:** removed "the zone near the rat"; the paper does not say where zone 1 is.
- **ed3b-velocity-unchanged:** noted that the two printed p-values look swapped, given their t and DF. They are kept as printed; the outcome is the same either way.
- **ed3j-eyfp-control:** removed "during and after the rat" and "reduces"; the legend gives neither the timing nor the direction.
- **ed6-ephys-heterogeneous:** removed "spread over tens of seconds", which the paper does not say. The criterion now names as open which trials count toward a unit being responsive. It marks reusing the imaging peak-time definitions as an assumption, and adds a threshold of its own for "heterogeneous", as fig2jo-diverse-peak-times does.
- **ed9-persistent-decoding:** source changed to ED Fig 9b and 9c. ED Fig 8, which the text cites, shows correlations, not decoders.
- **fig4e-models-dynamics:** the Methods compute model correlations every 10 ms, not at 11 Hz. The criterion now says so and reads them at the frame times for the score.

**Still open (recorded in `checks`):**
- I did not reread the paper's code. What the criteria say the scripts do is the first reader's reading.
- In several rows, sample sizes and DF in Supplementary Table 1 disagree with the figure legends. They are recorded as printed.
- Many criteria set thresholds of their own where the paper gives no number or test. Each says so, and those outcomes rest on them.
- I added no claim for the text's remark that freezing, jumping and slowing did not differ from controls; the paper shows no figure or test for it.

Nothing is committed or pushed.
