The claims file for DANDI:000402 is fit for an attempt (`ready: true`) after my corrections. Nothing is committed, and only `claims/000402/10.1038-s41586-025-08790-w.yaml` was changed.

**Checker:** `36 claims, 36 quotes, 0 statistical values, 0 problems`. It passed both before and after my edits. The paper reports no tests or intervals, so there are no statistics to check.

**Changes, by claim:**
- **Opening comment:** it said the perfusion date and age disagree with the birth date. They agree (16 March 2018 is P87). Only the structural stack entry is wrong: 21 March 2018 is P92, not P83.
- **scans-14-p75-p81:** removed the expected "6 imaging days, tolerance 0". The 6 days refer to all 19 completed scans, not the 14 kept, and the criterion already allowed 6 or fewer.
- **scan-configurations:** the depth-span tolerance (265 to 435 µm) disagreed with the criterion's widened range (270 to 440 µm). I set the value to 355 so they match. Judging on the median scan was the other agent's choice, so I named two readings: every scan, or the median scan.
- **monet2-directions:** dropped the requirement of 22.5° spacing. The paper says only "16 unique directions"; the spacing is now just reported.
- **fig3f-oracle-reliability:** the outcome rested on a measure the paper does not give (pairwise correlation between repeats, over 100 units per percentile). The paper's measure of consistency is the oracle score itself, so the outcome is now based on it. The pairwise measure is kept as a variant.
- **fig3g-direction-tuning:** the unit ranking and a split-half check were made up and decided the outcome. The outcome is now that each of the 16 directions is preferred by at least 5 units; the made-up checks are kept as a variant.
- **manual-coreg-19181:** removed a 95% threshold the paper does not give.
- **ed4-matched-higher-signal-correlation:** marked "all pairs of scans per neuron" as a choice made by the other agent, not the paper.
- **fiducial-transform-residual:** the tolerance on the fiducial count is now 2, because the paper gives both 2,934 and 2,936. Corrected reading (b): the 3.9 µm residual comes from the first step of the third transform group, not the whole group.
- **fig6f-outputs-mapped:** replaced a made-up "90% of neurons" rule with two readings: every neuron, or the mean of each cell class.
- **fig6k-target-responses:** replaced a made-up 90% threshold with "every matched target", and missing targets are to be listed.
- **fig7abc-laminar-connectivity:** "more than 900,000" is a lower bound, so the count now holds at 810,000 or above, with no upper limit. The old symmetric tolerance passed the paper's code's own lower count of 812,686. The same-layer share and its 10-point threshold were invented; the paper gives no measure or test of the laminar differences, so that part is now recorded as `methods_underspecified`.

**Still open:**
- **area-split-half-visp:** the 15-point tolerance on "roughly 50%" is the other agent's (reason given). The paper does not say whether the share is of volume or of neurons.
- **synapse-detection** and **dendrite-input-precision:** these list readings the paper does not give (how detections are matched, which version counts as before proofreading). They can only be tested if the needed annotations are public.
- **fig3f** and **fig3g:** the percentile and table choices said to come from the paper's code were not re-checked against the repository.
- **Coverage:** the abstract's "more than 200,000 cells" in the EM volume has no claim. Every other main finding has one, and all claims come from this paper.
