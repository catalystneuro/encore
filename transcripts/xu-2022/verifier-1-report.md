**A. Outcomes** (39 claims in the claims file: 20 reproduced, 5 partially reproduced, 3 not reproduced, 11 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| ephys-unit-counts | partially_reproduced | Cell 21 finds 57 sessions and 1578 single units (allowed 1383–1691). Multi-units are 339, above the allowed 273–333. The total of 1917 is within 10% of 1840. |
| fig3-session-counts | reproduced | Cell 23: 8/9/13/5 sessions. Every one has units and at least 10 selected trials in each direction. |
| fig3-units-per-session | reproduced | Cell 25, reading (b): 33.6 ± 13.0. Reading (a), the 35 sessions the regressions actually use, gives an SD of 14.4, just above the 14.3 limit. That reading alone would be partial. |
| fig3a-trial-count | reproduced | Cell 27, reading (a): 2886 trials (allowed 2416–2952). |
| fig3c-length | reproduced | Cell 31: 0.568/0.423/0.117/0.032, all within tolerance, order holds. The trial-fold variant also passes. |
| fig3c-velocity | reproduced | Cell 33: 0.361/0.326/0.081/0.019, all within tolerance, order holds. |
| fig3c-angle | reproduced | Cell 35: S1BF 0.111 is below the other three, whose spread is 0.049. All four within tolerance. |
| fig3c-identity | reproduced | Cell 37: 0.693 > 0.412 > 0.270 > 0.113, all within tolerance. With trial folds, S1BF is 0.049, below the allowed 0.09–0.19, so that variant would only be partial. |
| fig3c-time | reproduced | Cell 39: 0.637 > 0.440 > 0.198 > 0.087, all within tolerance. |
| ed5b-variables-uncorrelated | reproduced | Cell 41: the largest mean \|r\| is 0.118 (theta–I). No pair reaches 0.3. |
| ed5e-variance-explained | reproduced | Cell 43: median ratio 0.454, inside 0.45–0.55 by only 0.004. |
| ed5f-axes-orthogonal | partially_reproduced | Cell 45: one pair, L′–theta, has mean \|cos\| 0.302, just over 0.3. The reference for random directions is 0.154. |
| fig3e-cca | reproduced | Cell 47: all 5 comparisons hold (p 0.0002 to 0.023). |
| fig3f-backtracking-svm | partially_reproduced | Cell 49: ALM (0.740) and M1TJ (0.734) decode, but so do S1TJ (0.595) and S1BF (0.556), each above its null 95th percentile (about 0.52). Chance is 0.50, as the paper states, and accuracy before 0.1 s is 0.49–0.52 in every region. ALM n = 6 matches the Fig. 3f legend. |
| fig4g-zigzag-context | reproduced | Cell 51: 6 sessions from 3 mice. All four comparisons decode (0.79–0.86 against a null 95th percentile of about 0.51). |
| ed7f-target-position-alm | reproduced | Cell 53: ALM 0.271 is the highest mean. Mann-Whitney p = 0.0025/0.0007/0.0014; the trial-fold variant gives 0.02–0.047. |
| ed7h-no-time-coding | reproduced | Cell 55: every region's mean R2 is ≤ 0.034. |
| ed4m-active-neuron-counts | partially_reproduced | Cell 57, reading (a): ALM 351 and M1TJ 223 are within tolerance; S1TJ 155 is not (allowed 107–131). Reading (b) has 0 of 3 within. |
| ed4l-alm-initiation | partially_reproduced | Cell 59: ALM's fraction (0.259) is higher than both other regions. Against S1TJ p = 0.0006, but against M1TJ p = 0.136. |
| ed4o-rhythmicity | reproduced | Cell 61: medians are S1TJ 0.201 and M1TJ 0.156 against ALM 0.093, with p = 2.5e-36 and 4.1e-24. |
| ed6-alm-reward-drop | reproduced | Cell 63: in ALM, 188 neurons decrease and 92 increase (binomial p = 5e-9). |
| ed1h-sequence-duration | reproduced | Cell 65, reading (a): 0.992 s over 17 mice and 25438 trials. The paper (ED1f) has 17 mice and 25683 trials. |
| ed1l-learning-curves | reproduced | Cell 67: 15 mice, 14 of 15 improve on both measures; Wilcoxon p = 0.0004 and 0.004. |
| ed1l-proficiency-1500 | not_reproduced | Cell 69: (a) 200 trials, (b) 1100 trials; the allowed range is 1350–1650. |
| ed2-backtracking-counts | not_reproduced | Cell 71: no reading has 2 or more of the 4 values within tolerance. Reading (c) gives 55 sessions, 9 mice, 10365 standard and 3839 backtracking trials. |
| ed2e-missed-licks | reproduced | Cell 73: 1.854 missed licks in backtracking trials (allowed 0.9–2.2) against 0.113 in standard trials, p ≈ 0. |
| ed6b-consummatory-licks | not_reproduced | Cell 75: the medians are 6 (a), 4 (b) and 7 (c); none is in 4.5–5.5. The two main readings sit either side of 5. |
| ed7b-correct-side | reproduced | Cell 77: 11 of 11 mice are above 0.5, also with the 5° margin. The pooled fraction is 0.714. |
| fig2b-s1tj-angle-variability, fig2b-almm1tj-angle-length, fig2c-almm1tj-initiation, fig2c-termination, ed3lm-half-power | blocked (metadata_insufficient) | The archive metadata confirms the session descriptions say only "2s 5V", "2s 2.5V" or "efficiency". The structure matches the paper: 7 mice with 5 sessions at 5V, 5 mice with 5 at 2.5V, consistent with one session per each of the 5 regions. The region of each session is still missing. The trigger point (cue, middle touch or water) could be derived from opto_times, but each claim is about a specific region. |
| ed3f-inhibition-efficiency | blocked (data_missing) | The 414 units of the efficiency sessions match the n = 414 of ED3e. There are no waveforms (so no pyramidal/FS split) and no fibre distance. Only a light-on/light-off rate change pooled over all units could be computed. |
| ed1i-earplug | blocked (metadata_insufficient) | The archive has 5 mice with 2 "earplug" sessions each, matching the paper's 5 mice with one earplug and one control session. It does not say which is which. The no-effect claim could still be partly tested without labels, by checking that the two sessions of each mouse have similar missed-lick counts. The notebook does not do this. |
| ed1j-odor-masking | blocked (metadata_insufficient) | There are 6 single "air" sessions (paper: n = 6). Nothing marks when the air flow was on within a session. |
| ed1k-tongue-numbing | blocked (metadata_insufficient) | 5 mice have 2 "numbing" sessions each (paper: n = 5). Lidocaine and saline are not labelled. A consistent difference between each mouse's two sessions could be checked without labels; its direction could not. |
| ed1f-lick-force | blocked (metadata_insufficient) | The notebook reports the force data only as volts. It never prints the TimeSeries `conversion` attribute. The paper text gives no slope for the ED1d calibration. |
| ed4j-nnmf-clusters | blocked (methods_underspecified) | Acceptable, but a consistency measure that needs no label matching (how often pairs of neurons stay in the same cluster) would allow an approximate test. |

**B. Problems**

1. [affects a conclusion] `unit_quality`: the 1 s bins, a censored period of 0, and an active time T that counts spikes outside the trial span are all choices made here. On synthetic units the contamination estimate is accurate at low contamination but overestimates at high contamination (true 0.15 → 0.174, 0.30 → 0.388). The multi-unit count of 339 is sensitive to these choices: a 20% contamination cut gives 295. This affects ephys-unit-counts and reading (a) of ed4m.
2. [affects a conclusion] Several outcomes sit within 0.01 of a threshold, from a single seed and fold assignment:
   - ed5e: 0.454 against a bound of 0.45.
   - ed5f: 0.302 against 0.3.
   - fig3-units-per-session, reading (a): SD 14.4 against 14.3.
   
   Each could flip with a different seed (`fig3_session` seed=3, `enet_cv_r2` one-SE choice).
3. [affects a conclusion] ed2-backtracking-counts, cell 71: the touch-duration variant drops 8 sessions. That is the number of sessions the Methods exclude, and it leaves exactly 47 sessions with 8 mice (the paper's ED2d has n = 8 mice). With that, only the trial counts disagree, both about 19% high. No trial-level filter (initiation under 1 s, video present) was tried.
4. [affects a conclusion] ed6b, cell 75: reading (b) stops a bout at 1.5 × the median touch interval. Consummatory licks do not all register a touch, so bouts end early and (b) is biased low. Because the medians are integers, a ±0.5 tolerance in practice requires exactly 5.
5. [affects a conclusion] ed1l-proficiency, cell 69, assumes the first learning file is the start of training, and this is never checked. Several mice are already fast in their first 100 trials (initiation time MX170903 0.47 s, MX180201 0.37 s). If early training is missing, reading (b) would be an undercount. MX200101 returns NaN without comment because its last 500 trials contain no standard trials.
6. [does not affect a conclusion] `enet_cv_r2` assigns samples to folds at random by default. This leaks within-trial autocorrelation into the test folds, especially for targets that are constant within a trial (I, TP). On a synthetic label unrelated to the rates, random folds give R2 0.06 and trial folds give −0.23. This follows the paper and the criterion, and the orderings survive trial folds. The size of the R2 values does not.
7. [does not affect a conclusion] The standardisation of inter-lick intervals is not applied anywhere: PETHs, CCA trial averages, trial selection. It is documented as a deviation. Effects on ed4m and ed4o were not quantified.
8. [does not affect a conclusion] `backtrack_session` and `zigzag_session` fit the PCA on all trials before cross-validation. This uses no labels. The 20 shuffles give a coarse 95th percentile, but the observed accuracies are well above it.
9. [does not affect a conclusion] fig3f: after the trigger, behaviour differs between classes (1.85 against 0.11 missed licks, cell 73). Decoding in S1TJ and S1BF in 0.2–0.4 s may reflect that. The paper's statement about S1TJ refers to later times (ED5g).
10. [does not affect a conclusion] ed4l, cell 59: the peak windows have unequal lengths (0.5, 2 and 1.2 s), which favours the mid-sequence window. S1BF's initiation fraction (0.309) is above ALM's, which contradicts the claim's wording "than the other regions", though S1BF is outside the criterion.
11. [does not affect a conclusion] ed7f, ed4o and ed6 treat sessions or neurons as independent: ALM's 13 sessions come from 8 mice. ed7f's trial-fold p values (0.02–0.047) are the closest to the threshold.
12. [does not affect a conclusion] Cell 17 checks the clock shift with L; the paper's ED5a uses θ. `zigzag_session` aligns trials on touches, not on the θ cross-correlation shift and θ-based trial selection of the Methods; the criterion allows this. `video_on_grid` maps frames at about 400.1 Hz to a 400 Hz grid by nearest frame, which adds noise to L′.
13. [does not affect a conclusion] The learning file of MX181003 shows a reversed learning curve (cell 67) and duplicates a file of MX181002 (cell 5). It is probably mislabelled. Its learning curve is not excluded and it is the one mouse that fails, but 14 of 15 still pass.
14. [does not affect a conclusion] For the blocked claims, the notebook relies on DANDI's truncated session description ("… se") and on trial-table columns. It never shows the distinct values of the `opto` column, `general/optogenetics`, the NWB session_description or notes fields, or the force `conversion` attribute.

**C. What I could not check**

- **Fig. 3b targets:** the R2 means and SDs are only inside the figure image, which I did not view, so I could not verify them.
- **Seed sensitivity** (ed5e, ed5f, units SD): needs a cell that repeats `fig3_session` with 3–5 seeds and reports the range.
- **ed2 trial counts:** needs counts after the initiation-under-1 s filter and the video filter, on the 47-session variant.
- **ed1l-proficiency:** needs, for each mouse, the first file's date against the first ephys or opto date, and the posIndex patterns of its first file, to check whether training starts with the files.
- **ed6b:** needs the distribution of reading (a) (fraction of trials at 4, 5, 6, 7), and a touch bout threshold based on video lick intervals.
- **Blocked opto and control claims:** needs `np.unique` of the `opto` column, the contents of `general/optogenetics` and `stimulus`, the full NWB session_description, and the force TimeSeries `conversion`. For ed1i and ed1k, the per-mouse missed licks of each of the two sessions would allow the label-free check.
- **ephys-unit-counts:** needs the single/multi split per session to compare with ED4d. I installed no NWB reader beyond the synthetic tests and did not stream any file, per the instructions.
- **Greedy trial selection (`select_trials`):** I could not check whether it finds the true minimum-distance subset. A comparison with exhaustive search on one small session would settle it.

The full text was taken from the PMC author manuscript (PMC9109820) and is saved as `paper/pmc9109820.xml` and `paper/pmc9109820.txt`.
