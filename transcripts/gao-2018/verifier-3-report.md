Round 3 verifier report for gao-2018-02 (doi:10.1038/s41586-018-0633-x)

The attempt record `gao-2018-02.yaml` has 46 outcome entries. One of them carries a `proposed` block: fig3f-alm-selectivity-abolished-by-cn-inhibition. Its recorded outcome is partially_reproduced and the proposal is not_reproduced. The record's two other matches for "proposed" are in the response text at lines 1402–1403, not in a `proposed` block.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig3f-alm-selectivity-abolished-by-cn-inhibition | not_reproduced | Yes | — | The claims file's criterion requires two things under one window reading: control selectivity above zero, and photo-inhibition selectivity not distinguishable from zero (its bootstrap 95% interval over neurons includes zero). In cell 74 (computed in cell 72), 336 neurons pass, from 4 mice. Control selectivity is above zero in every reading. Photo-inhibition selectivity fails the zero test in every reading: whole delay 0.39 [0.19, 0.60], last 500 ms 0.27 [0.02, 0.53], and with the 5-screening-trial variant 0.37 [0.17, 0.57] and 0.32 [0.06, 0.56]. The criterion has no partial condition, so the 73% to 82% drop in selectivity does not count as partial reproduction. |

Checks behind the agreement:

- **Numbers come from the data.** Cell 72 builds `selstim` from the session files with `G.pref_selectivity` and `G.boot_mean_ci` (`gao2018.py:459`, `gao2018.py:483`). The preferred trial type is chosen from screening control trials. Control selectivity is then measured on the remaining control trials, and photo-inhibition selectivity on photostimulation type 6, "CN inhibition delay 1.3 s" (`gao2018.py:83`). The interval is a 10,000-resample bootstrap over neurons. The values printed in cell 74 match the result text in cell 75 and the numbers in the record.
- **No choice was made to reach the result.** The 10 screening trials follow the criterion and the Methods. The 5-trial variant (from the deposited script) gives the same verdict. The neuron selection is the one the criterion names: selective by E2 on correct trials, and more than 3 trials of each type in every condition. The whole delay matches the 1.3 s photo-inhibition period. The last-500-ms reading is the criterion's reading (b). No window or variant in the notebook gives an interval that includes zero.
- **Criterion applied as written.** The windows are the readings set out for fig3c-cn-selectivity-abolished, which this claim points to. I found no place where the claims file misreads the paper. It reads "abolished" in the quoted main-text sentence (paragraph 14, Fig. 3f) as "not distinguishable from zero", and that reading is reasonable.

This agrees with the not_reproduced outcome I gave for this claim in rounds 1 and 2.
