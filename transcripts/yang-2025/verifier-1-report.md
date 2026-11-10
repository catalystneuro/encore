**A. Outcomes (19 claims in the claims file; the notebook tests 14 and blocks 5)**

| Claim | My outcome | Reason |
|---|---|---|
| tables1-network-stable-short-term | reproduced | With self-pairs included (reading d, once, BIC or AIC), intra-group r exceeds inter-group r with MW p < 0.05 in 7/7 rats, and 11/14 means are within tolerance (cell 15). Without self-pairs only 5/7 rats hold: in R4 intra is below inter (0.154 vs 0.208, p = 0.24) and R7 gives p = 0.15. So the outcome depends on the r = 1 self-pairs. |
| fig2-r1-target-shifts | partially_reproduced | With out−in sign and AIC order, 3 of 4 top nodes match (base0 gives CA1, the paper ANT). BIC gives 2/4 and the in−out sign 0/4 (cell 17). |
| figs2-target-assignment | partially_reproduced | Best reading (out−in, AIC, top node): 20/28 baseline groups match, which is ≥ 18. Only 21/28 labels agree and the counts are 9 target / 19 non-target, not 8/20 (cell 19). BIC gives 16, which is below the partial bar. |
| fig3a-target-reduces-each-rat | not_reproduced | 3 of 8 target groups are below zero in the main run, 2 to 4 across the variants; 6 are needed (cell 23). R2 DG is +0.18 and R5 ANT +0.12. |
| fig3a-nontarget-can-lengthen | reproduced | 11 of 20 non-target groups are positive (9 to 12 across variants; cell 25), 6 of them the same groups the paper shows. This bar is easily met when there is no effect: 5 of 8 target groups are also positive. |
| fig3a-per-rat-site-differences | partially_reproduced | The best reading (unadjusted Dunn) finds 5 of the 11 paper pairs, which meets the partial clause as written (cell 27). The same reading also finds 4 to 6 pairs in R1/R6, and the Kruskal-Wallis p is about 0.6 in R5 and R7. |
| fig3a-target-vs-nontarget-total | not_reproduced | Target −0.037 vs non-target 0.003, MW p = 0.93. Target is never lower at p < 0.05 under any normalization, unit or variant (cell 29). |
| fig3a-some-nontarget-shorten | partially_reproduced | Under the one-sample t reading, 3/5 named groups are significantly shorter (R2 ANT, R3 CA1, R7 CA3) and 3/5 are less effective than the rat's target (R4 CA1, R5 CA3, R7 CA3) (cell 31). This meets the letter of the partial clause, but in R4 and R5 the comparison holds only because the target group lengthened seizures. |
| fig3b-same-site-target-vs-nontarget | not_reproduced | 0 of DG, CA3, ANT are significant under any reading (cell 33). CA1 is not significant, so the CA1 part holds. |
| seizure-duration-proportion | blocked (data_missing) | The archive confirms there are no recording durations (see 4 below). |
| fig3c-frequency-no-difference | blocked (data_missing) | No recording hours, so there is no rate in times/h. |
| fig4b-psd-target-bands | not_reproduced | Alpha and gamma hold together in 0 of 96 readings, and alpha holds in none (cell 37). |
| fig4b-psd-other-bands-unchanged | not_reproduced | High gamma has KW p ≤ 0.005 in every reading. Delta, beta and theta are also significant in nearly all readings (cell 39). |
| fig5b-iis-post-seizure | reproduced | Reading (b) with 1 s bins gives target 0.178 vs non-target 0.286 /s, paired t p = 7.8e-10 (cell 41). This is fragile: reading (a) gives p = 0.005, the per-seizure version p = 0.03, and target is higher than non-target in R3, R4 and R5. The pooled difference is mostly R7's non-target groups (1.117 /s). See problem 4. |
| fig5c-interictal-iis-no-difference | blocked (data_missing) | No interictal segments. |
| fig5d-iis-seizure-correlation | blocked (data_missing) | No interictal segments and no recording time. |
| fig6cd-interictal-hfo-no-difference | blocked (data_missing) | No interictal segments. |
| fig6e-ictal-ripples-no-difference | reproduced | Paired (by rat) target vs non-target p = 0.09 to 0.95 in all four variants (cell 45). This is weak evidence for an absence: there are 7 pairs, the detector is not the HFO App, and the means are +0.4 to +10 against the paper's −0.16 and −0.04. |
| fig6f-ictal-fast-ripples-reduced | not_reproduced | The target mean is above both baseline and non-target in 3 of 4 variants, and every paired p is ≥ 0.19 (cell 47). |

**B. Problems**

1. **[affects a conclusion] Seizure onset and end come from the author's own line-length rule (`detect_seizure`).** The paper gives no rule, and the rule is stated as an assumption, but it is not validated beyond the train-latency contrast.
   - All duration claims (fig3a-\*, fig3b) rest on it.
   - Median durations are flat across conditions (41 to 45 s).
   - The first train comes a median 15 to 17 s after the detected onset in R4 and R5 (cell 10), although Methods C says stimulation starts immediately at detection.
   - The threshold variants move the target-below-zero count between 2 and 4.
   - In stimulation clips, train windows bridge the run (`lo | stim`), so the seizure end can be set by when the device stopped stimulating.
   - One reading was never examined: detected onsets cluster at a median of 301 s (cell 10). The clips may have been cut around the authors' own onset at 300 s, which would in effect be deposited seizure times (claims reading a).

2. **[affects a conclusion] Three outcomes depend on one reading that is unstable.**
   - tables1 reaches reproduced only when self-pairs (r = 1) are included.
   - fig2 and figs2 reach partial only with AIC order, and AIC hits the author-chosen cap of 20 in 422 of 2403 windows (cell 13). So the AIC result partly depends on that cap; a higher cap was not run.

3. **[affects a conclusion] The HFO detector does not follow the claims file (`hfo_events`).** The fig6cd criterion, which fig6e and fig6f refer to, says to use the HFO App defaults; the module says that app's code was not read and substitutes a Gardner-style detector.
   - The threshold is a whole-clip percentile, which in stimulation clips includes the train artefact.
   - Dividing by short pre windows gives means of 4 to 16 against the paper's −0.25 to 0.2.
   - 48 to 290 seizures are dropped because they have zero events in the pre window (cells 45 and 47).

4. **[affects a conclusion] Stimulation artefact is not removed from the post-seizure IIS window (`process_clip`, IIS block).** On synthetic data, a 5 s train of 130 Hz pulses at 8 times the noise SD produced 20 false spikes in `detect_iis` and none elsewhere. Trains run until the device stops detecting seizure activity, and the pause between trains reaches 256 s (cell 8). So trains can fall 15 to 45 s after the detected end, and more often in groups where stimulation works less well (non-target). The notebook never counts this.

5. **[affects a conclusion] PSD and HFO window artefacts (`psd_windows`).**
   - The post window (t1, t1 + 5 s) is not checked for the next train; the pause can be as short as 0.75 s.
   - The train end is known only to about 0.25 s.
   - At 1 kHz the 130 Hz harmonics fold onto multiples of 10 Hz (40, 50, 80, 90, 220, 260, 310, 390 Hz and so on), inside the gamma, high gamma, ripple and fast-ripple bands.
   - The pre window runs from the detected onset to the first train, up to 314 s; 67 of 248 latencies exceed 15 s, so many pre windows include pre-ictal signal (fig4b, fig6e, fig6f).

6. **[does not affect a conclusion] Group order.** Normalization uses the dataset's group order, which differs from Figure S2 for R5 and R6 (6 groups; cell 19), and no variant with the Figure S2 order was run. From the baseline means printed in cell 21, using the Figure S2 order keeps R5 ANT positive (+0.25) and leaves R6 CA3 unchanged. Separately, under the dataset order R6 ANT-stim follows a baseline whose Figure S2 target is ANT, which shows the data and Figure S2 are inconsistent there.

7. **[does not affect a conclusion] Wording of the fig3a-per-rat partial clause (cell 27).** As written, the partial clause does not require R1 and R6 to be free of significant pairs. The notebook does not print which 5 pairs pass with unadjusted Dunn.

8. **[does not affect a conclusion] One-sided tests (cell 31).** fig3a-some-nontarget-shorten uses one-sided tests. Two-sided tests leave the count at 3 (R2 ANT p ≈ 0.018, R7 CA3 p ≈ 0.004).

9. **[does not affect a conclusion] Mixed units (cells 37 and 39).** Under the "stimulated channel" PSD reading, baseline seizures keep all 4 channels while the stimulation conditions keep one.

10. **[does not affect a conclusion] Tolerance on the wrong scale (cell 29).** The z-score and difference readings are compared against tolerances given in relative units.

11. **[does not affect a conclusion] Helpers verified.** On a synthetic VAR where ANT drives two nodes, `conditional_gc` and `cfw` (out−in) recover ANT as the driver. The notebook's `dunn` matches scikit-posthocs' Bonferroni-adjusted Dunn's test to 6 decimal places. The claim that the two window-combination readings give the same cf_w is correct, because cf_w is linear in the GC matrix.

**4. Blocked claims, checked on the archive.** The API for 0.241023.0931 lists 56 assets. Their only measured variables are ElectricalSeries and ElectrodeGroup, and the description gives no recording hours. The notebook's file check found empty intervals, processing and stimulus groups.
- **seizure-duration-proportion, fig3c:** cannot be tested in the paper's unit. A seizures-per-calendar-day proxy from clip names and dates could be run for fig3c's absence claim only by assuming continuous recording and that every seizure was deposited. Neither assumption holds safely: "at least 6 seizures" suggests a selection, and R2 CA1-stim has 9 clips all from one day.
- **fig5c, fig5d, fig6cd:** each clip has about 300 s before onset, and Methods F requires segments at least 1 h from any seizure, so no clip qualifies. Blocked is right.

**C. What I could not check, and the output that would have let me**

- Whether the clips are aligned to the authors' onset: a histogram of detected onset times and of the absolute time of the first train in stimulation clips.
- Whether the onset and end rule is sound: example plots of LFP and line-length score with the detected onset, end and trains (the notebook has no figures).
- Train contamination: by condition, how many trains start after the detected seizure end and fall 15 to 45 s after it, and how many PSD or HFO post windows overlap a train or lie within 0.5 s of one.
- Sensitivity to the AIC cap: the AIC results for figs2 and fig2 with a cap of 30 or more.
- The per-group computed targets for the BIC readings, and which pairs pass under unadjusted Dunn for fig3a-per-rat-site-differences.
- The fig5b result per rat, and with R7 left out.
