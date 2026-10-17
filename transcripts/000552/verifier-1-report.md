# Verifier report, round 1: Huszar et al. 2022 (doi:10.1038/s41593-022-01138-x), DANDI 000552 v0.230630.2304

The claims file has 35 claims. The notebook tests 12 and blocks 23. Of the 12 tested, I find 4 reproduced, 5 partially reproduced and 3 not reproduced. I accept 22 of the 23 blocks; I disagree with the reason given for fig7fg. Paper text: PMC10807234 (author manuscript), saved in `paper/`. No claim involves decoding, so no chance level applies.

## A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| cohort-birthdates | reproduced | 17 mice and the birthdate counts 4/3/6/4 match (cell 22). The notebook's 13 M / 4 F comes from taking each mouse's first file. The sex field differs between files of the same mouse: e13_1f1 is Male in 2 files and Female in 3; e13_1m1 is Male in 9 and Female in 3 (cell 7, and the DANDI asset metadata I queried). Taking each mouse's majority gives 12 M / 5 F, which matches. |
| sessions-durations | partially_reproduced | Count, median and range all pass: 104 files is within 10% of the 96 in Fig. 7f, the median is 319.6 min (309.1 ± 30.9), and all durations lie in 102.3–523.2 min (cell 24). Leaving out e15_13f1 and e16_3m2 gives exactly 96 sessions, the Fig. 1e per-birthdate counts, and the paper's range of 113.7–475.6 min. It is partial because the criterion also requires non-REM sleep in every session, and two files (e13_1f1_200305 and _200307) hold a single Awake interval. |
| spwr-duration | reproduced | The median is 36.0 ms under both readings, against 36.4 ± 3.64, and every ripple lies within 20–199.2 ms (cell 26). |
| unit-count | not_reproduced | 8,201 units against a lower bound of 8,524 (cell 28). The cause is missing data: 6 mice (39 files) have no units in the archive, while Fig. 7f reports pyramidal pairs from 96 sessions of 15 mice. |
| maze-cohort | reproduced | Reading (b) matches exactly: 11 maze mice, minus e15_13f1 and e16_3m2, gives 9 mice at E13.5–E16.5 = 2/2/2/3, and 3 mice have novel recordings (cell 30). |
| maze-task | not_reproduced | Trial length (median 204.1 cm) and tracking rate (30 Hz) pass. Only 38/65 sessions (visited arm) or 22/65 (expected arm) have at least 10 trials per arm, and only 59/65 have at least 20 trials, the fewest being 12 (cell 32). That also fails the partial condition. |
| novel-explorations | partially_reproduced | 3 mice but only 9 novel recordings with trials and position: 3 recordings of about 164 cm and 6 linear tracks of 100 or 110 cm (cell 34). The notebook's "9 + 7 = 16" counts epochs without position, which the criterion excludes. No open field has position, and the paper used three open fields. |
| fig5e-pv-decorrelation | partially_reproduced | Stem 0.937 is within tolerance. Turn 1 0.547, arm 0.492 and turn 2 0.465 are all above tolerance. Kruskal–Wallis H = 7632.7, p ≈ 0, with the stem highest (cell 36). The bin counts (4218/2109/4218/1140) equal the paper's exactly, so the session set matches. |
| fig6c-theta-rate-preserved | reproduced | Spearman rho = 0.734 ≥ 0.664, p ≈ 0, n = 2,038 (cell 41). Each mouse gives 0.72–0.76 and the variants 0.76–0.81. The rate is a running-speed proxy for the paper's theta-cycle rate. |
| fig6c-novel-ratemap-corr-higher | not_reproduced | Familiar −0.053 is within tolerance. Novel −0.036 falls outside 0.018–0.078, and the rank-sum p = 0.67 (cell 43). Within each session the novel median is higher in 9 of 9, but it stays negative and far below 0.048. Open-field explorations are missing from the data. |
| fig6d-info-lower-novel | partially_reproduced | Novel is lower (0.270 against 0.631 bits/s, p = 1.5e-59), but both medians fall below tolerance (cell 45). |
| fig6d-rate-lower-novel | partially_reproduced | Novel is lower (0.799 against 0.958 Hz, p = 7e-6), but both medians are above tolerance (cell 47). This may be partly the `running_rate` bug in B1. |
| ed2, fig1e, fig1f, fig1g, fig1h, fig2b, fig2c, fig2d, fig2f, fig2g, fig3c, fig3e, fig5b, fig5c, fig5f, fig6e, fig6f | blocked (data_missing) | Confirmed against the archive. The units tables hold only clu_id, group_id, spike_times and unit_name (cell 8). The archive's variableMeasured lists no optogenetic or stimulus type for any asset (my API query), and stimulus/acquisition groups are empty in the processed files. |
| fig5d, fig7b, fig7ce | blocked (data_missing) | Need light-responsive labels; fig5d also needs shank positions, which the unit group_id does not reliably give. |
| fig4d-model-fit | blocked (depends on fig3e) | Agreed. |
| fig1c-radial-depth | blocked (data_missing) | Agreed. The depths come from tdTomato histology (Methods, "Quantification of normalized cell depth"), which is not in the archive. |
| fig7fg-convergence-cofiring | blocked, but partly testable | The stated reason (no cell types) is inconsistent with the rest of the notebook, which classifies pyramidal cells by rate alone. Using the same rule, units above 5 Hz as interneurons, plus CCG monosynaptic detection on spike times, the share of pyramidal pairs with nonzero convergence and the trend of ratemap overlap with convergence could be computed on 65 of 96 sessions. |

## B. Problems

1. [affects a conclusion] `huszar.running_rate`: running stretches are built from consecutive samples of `pos`, and `pos` is the trial samples concatenated. If the animal is running at the end of one trial and the start of the next, the stretch spans the gap between them. Spikes in the gap are counted, but the gap's time is not. On synthetic data with a 1 Hz cell and 10 s gaps the function returns 3.5 Hz. The 5 s start-area delay between figure-eight trials makes this likely in the real data. It can inflate both medians in fig6d-rate (and possibly the familiar median beyond tolerance); rho in fig6c is probably robust.
2. [affects a conclusion] Cells 3 and 22: sex is taken from each mouse's first file. The notebook flags the e13_1f1 name mismatch but misses that the sex field varies between files within e13_1f1 and e13_1m1. A majority over files gives 12 M / 5 F.
3. [affects a conclusion] Cell 34: the count of 16 explorations includes position-less epochs picked post hoc (10–50 min, not the last epoch). The criterion counts only recordings with trials and position, which gives 9.
4. [affects a conclusion] `PYR_MAX_RATE_HZ` (cells 36, 39): 87.8% of units pass the ≤5 Hz rule, against 78.3% pyramidal in the paper, so some interneurons are included. The PV medians move strongly with the threshold: all units give 0.94 on the arm, ≤2 Hz gives 0.29. The outcome of fig5e depends on this unvalidated choice.
5. [affects a conclusion] Cell 43: the rank-sum test pools about 570k pairs across sessions, so sessions with many pairs (e15_13f1) dominate. Per session the novel median is higher in 9 of 9, yet the pooled test gives p = 0.67. The criterion fixes the test, so the outcome stands, but the pooled test hides the per-session direction.
6. [does not affect a conclusion] Cells 36 and 45: Kruskal–Wallis on smoothed, adjacent bins and rank-sum on pooled cells treat dependent values as independent. The paper does the same.
7. [does not affect a conclusion] Cell 15 says no raw file has a stimulation or TTL channel. `raw_file_info` only reads two fixed keys and never lists the contents of the raw files. The asset metadata and the 64/128 channel counts (equal to the probe sizes) support the statement, but the notebook does not show it. The paper says raw data were clipped around pulses. Pulse times might therefore be recoverable from the 11 wideband files (4 mice, about 1.5 TB), which would make a partial ed2 test possible but too_large.
8. [does not affect a conclusion] `skaggs_information` weights by unsmoothed occupancy but divides by smoothed occupancy. On synthetic maps it is otherwise correct (a uniform map gives 0; a single bin gives log2(1/p)·λ). The 9-cm FWHM smoothing is also correct.
9. [does not affect a conclusion] `mean_rates` divides by `end_s`, which is 1–5 s short of the last spike in 57 files. This is negligible.

## C. What I could not check

- How large B1 is: an output of the gaps between consecutive trials and the speed at the first and last sample of each trial, or the fig6c/6d rates recomputed with stretches cut at trial boundaries.
- Whether `unit_name` or `clu_id` encode a cell type or an opto tag: printing example values from a few files would settle it.
- Whether the raw files hold any stimulation channel or clipped (zeroed) segments: a listing of all groups in one raw file, and a scan of one channel near the session end for zero runs.
- fig7fg feasibility: a per-session count of units above 5 Hz and a CCG-based connection count on one session.
- Whether the 7 position-less epochs are the open-field explorations: any position or video series in those epochs; the asset metadata suggests there is none.
- Per-file sex values: an output tabulating sex per file for each mouse would have shown problem B2 directly.
