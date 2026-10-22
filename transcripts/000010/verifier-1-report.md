**Verifier report, round 1: Li et al. 2015 (doi:10.1038/nature14178) on DANDI:000010 v0.220126.1905**

The claims file lists 27 claims. I was not given an attempt record, so the claim count comes from the claims file alone. My outcomes: 8 reproduced, 3 partially reproduced, 5 not reproduced, 11 blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| behaviour-performance | reproduced | Under reading (b), the mean over sessions in the extracellular sessions with tagging-light trials left out, per cent correct is 75.8% (x) or 76.5% (y), inside 70.56–86.24. Early licks are 11.6%, under the 14.3% limit (cell 17). Readings (a) and (c) fail on early licks (14.5% and 14.7%). |
| fig1d-delay-inhibition-ipsi-bias | blocked (data_missing) | I checked the archive: 23 subjects, 19 ephys mice (Sim1, Rbp4, Tlx and three Ai32 crosses) and 4 imaging mice. There are no VGAT-ChR2 or PV×ReaChR mice and no photoinhibition trials. |
| fig1d-sample-inhibition-smaller | blocked (data_missing) | Same as above. |
| units-classification | partially_reproduced | Units 1,369, sessions 99, mice 19, fast-spiking 124 and pyramidal 1,245 are all within tolerance. There are 0 intermediate units against 39 (cell 19). Since 1,369 = 1,408 − 39, the intermediate units were simply not deposited. |
| fig2-selective-fraction | reproduced | Reading (a)(i)(t1) gives 912 of 1,245 (0.733). Reading (t2) gives 870 (0.699), also within tolerance (cell 21). |
| fig2d-preparatory-perimovement | not_reproduced | "Peri-movement only" is 272–294 against 350–428 under all 8 readings. No reading puts all three counts in tolerance (cell 23). |
| fig2c-selectivity-time-course | reproduced | Under both steps and both light readings: (1) the sample-epoch count reaches 248–280, above the binomial limit of about 72, while pre-sample windows average about 60; (2) the delay count rises from 273–326 to 377–408; (3b) the maximum starts 0.2–0.35 s after the go cue. (3a) fails (cell 25). |
| fig2c-population-dynamics | reproduced | With t1 all 24 correlation readings hold (r_sample < r_delay < 1) and population selectivity stays above 0 through the delay. With t2, 2 readings fail (all neurons, variance, difference vector, gs and gc). The claims file lets either light reading decide (cell 27). |
| ed2c-error-trials-predict-choice | reproduced | Delay r is −0.25 to −0.32 and response r is −0.30 to −0.38 under both minimum-trial readings and both light readings. Sample r is about 0 (cell 29). |
| fig2e-no-contra-bias-spikes | reproduced (fragile) | (a)(i) gives P = 0.82 (t1) and 0.52 (t2). Under (b)(delay)(t2), P = 0.060 and the modulation is 7.97%, inside 7.2–8.8. Only 419 of 912 selective neurons are contra-preferring, so there is no contralateral excess. But all four 570 ms-window tests give P < 0.05 with a contralateral excess (cell 31; see B1). |
| ed1-fast-spiking-properties | not_reproduced | Baseline rates hold (FS median 4.4–4.5 against 1.5 spikes/s). Selectivity is not lower for FS: fraction selective is 0.75 against 0.73, and mean absolute difference is 1.46 against 0.62 (cell 33). The criterion requires both under every reading. |
| tagging-counts | partially_reproduced | PT 45 and IT 27 match exactly. The dataset has no label for the failed-collision or untested neurons (unit labels are FS, IT, PT, Pyr only; cell 35). |
| antidromic-latencies | partially_reproduced | PT latency is below IT latency in all 18 readings. All four measurable values are within tolerance in 1 reading (8 ms window, r, ±0.5 ms). The four failed-collision values cannot be measured (cell 37; see B3). |
| fig3e-pt-it-both-activity-types | reproduced | Every reading has at least one preparatory and at least one peri-movement neuron in each type, for example PT 17/24 and IT 13/13 (cell 39). |
| fig3f-pt-contra-preferring | reproduced (fragile) | Under (a)(t1), PT is 30/45 with P = 0.0098 and IT is 13/27 with P = 0.58. PT fails under (b) (P = 0.09) and under t2 (P = 0.14–0.30) (cell 41; see B2). |
| fig3f-pt-contra-selectivity | not_reproduced | The PT t-test never gives P < 0.05 (range 0.12–0.36). No onset can be found under any reading. Some modulation readings land in tolerance (PT 34.5%, IT −18.7%), but both tests are required (cell 43). |
| imaging-selectivity-counts | not_reproduced | 0 of 16 readings put every value in tolerance. The closest, (1.5 s, a, mean, non-early), has 1,417 selective cells against a lower bound of 1,417.5. Readings (b) give 3,104–3,134 task-related cells, above 3,014 (cell 45). |
| fig4f-spatially-intermingled | not_reproduced | 57 of 64 test rows have P < 0.05, including all 32 rows with the all-cells neighbour set. The 7 rows with both P ≥ 0.05 have both preferences in only 57–58 of 59 fields of view (cell 47). |
| fig4h-pt-contra-imaging | blocked (metadata_insufficient) | No plane depth in the notebook's metadata check, and none in the asset metadata on the API. The claims file calls the all-labelled-cells population a substitute. In that variant, 0 of 16 readings pass, and chi-squared P is never below 0.001 (smallest 0.0016). |
| reaction-time | blocked (methods_underspecified) | The free threshold moves the mean across mice from 40 to 166 ms. One reading (z, last 0.5 s, 3 s.d.) gives 59–62 ms, but the s.d. across mice is 29–51 ms against 10.5 under every reading (cell 51). |
| fig5b-pt-delay-activation-contra-bias | blocked (data_missing) | The Ai32 files are named `behavior+ecephys` with no `ogen` and have no stimulus series. No trial table has a photostimulation column. |
| fig5b-pt-sample-activation-contra-bias | blocked (data_missing) | Same as above. |
| ed6b-pt-dose-response | blocked (data_missing) | Same as above. |
| ed6d-it-activation-inconsistent | blocked (data_missing) | Same as above. |
| ed3e-high-power-contra-licking | blocked (data_missing) | Same as above; there are also no untrained mice and no vibrissal motor cortex trials. |
| ed7-pt-activation-persistent | blocked (data_missing) | There is one Sim1×Ai32 mouse (218693) with 3 sessions and 57 units, against the paper's 2 mice, 8 sessions and 91 neurons, and it has no light record. Neither part can be tested. |
| ed3-anatomy-it-pt-separate | blocked (data_missing) | There is no histology in any asset. |

### B. Problems

1. **[affects a conclusion]** fig2e, cell 30/31: The notebook rests the absence result on reading (a)(i), but the claims file sets no rule for which reading decides. In the 570 ms window, which is where the paper reports the same P = 0.13 for task-selective neurons, all four tests give P between 0.022 and 0.04999 with a contralateral excess. That is the criterion's "not reproduced" condition. On proportions, the binomial test gives P = 0.016 and the bootstrap gives 1 − P = 0.007 for an *ipsi* excess (t1). The criterion allows that, but it goes against "equal proportions". Any rule that requires absence under all readings flips this claim to not reproduced.
2. **[affects a conclusion]** fig3f-pt-contra-preferring, cell 41: The PT result rests on keeping the tagging-light trials. The pons light evokes antidromic PT spikes, and the notebook never checks whether light trials are balanced between lick-right and lick-left trials. An imbalance would bias exactly this PT spike-count comparison.
3. **[affects a conclusion]** antidromic-latencies, cell 37 / `antidromic_latencies`: The only passing reading keeps spikes within ±0.5 ms of the histogram peak, which caps the s.d. at 0.5 ms or less. The jitter matches (0.115 and 0.197 ms) are therefore partly forced by the reading. The 5/8/10 ms windows and the 0.5/1 ms peak widths are the author's choices; 1 of 18 combinations passes. Under (w), PT jitter is 0.31–0.64 ms. The outcome stays partially reproduced.
4. **[affects a conclusion]** imaging-selectivity-counts, `plane_trials` / `classify_plane`: The result misses by half a cell. 3,403 of 4,706 included ROIs reach F ≤ 0 after neuropil subtraction, so DF/F has a near-zero F0 in some trials, and contra preference is taken from mean DF/F. Imaging files carry no early-lick flags, so "correct" and "non-early" include early-lick trials. None of these sensitivities was checked, and with a 0.5-cell margin any of them could flip the outcome.
5. **[does not affect a conclusion]** fig2c-population-dynamics, cell 27: Under reading (ge) the reference bin [−0.2, 0) is inside the delay mask, so r = 1 enters r_delay. Under "10 in all", if all 10 preference trials fall in one type, the other side is compared against 0. The neuron selection under (a) uses the same trials as the selectivity estimate. Reading (gs) and the all-neurons population avoid these problems and still hold.
6. **[does not affect a conclusion]** fig4f, `spatial_tests`: The "across" shuffle mixes labels between planes that have different contra fractions, which is not a spatial null. The within-plane rows still mostly give P < 0.05.
7. **[does not affect a conclusion]** reaction-time, cell 51: In 15 sessions (6 mice) the mean signal *falls* after the cue, but the z reading detects only upward crossings. Mouse 219248 comes out at 179 ms.
8. **[does not affect a conclusion]** behaviour-performance, cell 17: `behaviour()` does not apply the 2.6 s timing filter used everywhere else (66 trials). The 1,540 trials without events, including the 1,447 placeholder trials, are correctly left out.
9. **[does not affect a conclusion]** Claims file, ed1: selectivity reading (ii) is an unnormalised rate difference, which favours units with high rates such as FS units. Reading (i) fails as well, so the outcome is the same. I found no other place where the claims file misreads the paper; the "about a quarter" mismatch in fig4h is already noted in the file.
10. **[does not affect a conclusion]** fig2d: 681 neurons are significant in the response epoch, close to the paper's 693 (389 + 304), but 628 are preparatory against the paper's 523. The mismatch is in the preparatory class as the Methods define it (sample or delay), not in the response epoch.

Checks that passed: the helper functions gave correct results on synthetic inputs (spike width, bootstrap, antidromic readings, first crossing, counts). Every number in the notebook comes from the loaded files. Epoch windows and units are as the claims file sets them. The fraction of pre-sample windows that test significant is about 4.4–6.4%, consistent with the 5% expected by chance. The paper states no chance level for the selections.

### C. Not checked

- **Light-trial balance (affects fig3f-pt-contra-preferring and the t1/t2 split):** a crosstab of light × instruction per session, and per PT unit's sessions, would settle it.
- **Imaging plane depth (fig4h):** the notebook printed only the plane description and location. The full `ImagingPlane` attributes and `session_description` of each imaging file would settle whether depth is recorded; I did not open the files.
- **Placeholder trials:** whether the 1,447 trials marked right/hit/5.5 s are the removed photostimulation trials, and whether any fall in the Ai32 mouse 218693 (which matters for ed7). A per-subject breakdown of those trials would show this.
- **Imaging F0 sensitivity:** the F0 distribution, and the counts with ROI-trials with F0 near 0 left out, would show whether imaging-selectivity-counts is robust.
- **Lick trace:** I could not confirm it is the photodiode mouth-movement signal; there is only the file's description.
- **Figure-only values:** the Fig. 1d and 5b stars, the Fig. 3f, j insets and the Fig. 2c curves were not read, as the claims file notes.
