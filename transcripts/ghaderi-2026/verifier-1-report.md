**Verifier report, round 1: Ghaderi et al. 2026 on DANDI:001530 (0.260605.0601)**

The claims file has 30 claims. The notebooks test 26 of them and mark 4 as blocked (fig5d, fig8b, figs18 and, through the decoding notebooks, none of the others).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig1c-lick-probabilities | reproduced | Cell 16: all five means are within tolerance (78.18, 9.90, 13.08, 1.05, 14.64; n = 35, or 34 for No-tone). |
| fig1f-movement-latencies | partially_reproduced | Cell 18: both readings give partial. (a) whisker 54.4 and jaw 115.3 are in, tongue 192.4 is out. (b) whisker 94.6 and jaw 142.9 are out. The order whisker < jaw < tongue < spout holds under both, and the lick latency is 330.1 ± 20.2 ms. |
| quiet-trials-half | partially_reproduced | Cell 21: the Methods rule rejects 55.06% of completed trials and 56.72% of all trials, just outside 45–55 but inside 30–70. Fragile: leaving out the 343 trials with no video gives 54.22%, which is within tolerance (problem 3). |
| fig2-auditory-window | reproduced | Cells 23–24: in absolute points, A1 38.9, wM2 33.0, wS2 26.0 and wS1 19.5 are all within tolerance. The significance pattern after FDR matches at both 1,000 and 10,000 iterations, with ALM and fpS1 not significant. |
| fig2-delay-window | reproduced | Cell 24: wM2 44.5, ALM 32.1 and wS1 16.0 are within tolerance; A1, wS2 and fpS1 are not significant (wS2 p_FDR 0.076–0.09). |
| fig2-whisker-window | reproduced | Cell 24: all five values are within tolerance, those five areas are significant (A1 p_FDR 0.007 or 0.012) and fpS1 is not (0.118). |
| fig2-wm2-vs-alm-auditory | reproduced | Cell 27: 33.0 against 7.8. Reading (a) gives p 0.006 or 0.0024 and reading (b) 0.002 or 0.0008, wM2 larger in both. |
| fig2-other-trial-types | not_reproduced | Cell 29: reading (a) finds 18 of 72 changes significant (threshold 7). Reading (b) finds a largest change of 19.0 points (threshold 13). Neither reading holds. |
| units-recorded | reproduced | Cell 31: exact counts, 780, 1938, 2064, 2749 and 2763, total 10,294. Probe sessions and mice match. wS2 has CCF units in only 19 sessions and 9 mice, against the paper's 24 and 11. |
| fig3a-activity-maps | reproduced | Cell 33: 4 of 4 rankings hold under both pre-whisker baselines and under the code variant. |
| fig3b-delay-and-response-psth | partially_reproduced | Cell 35: (i) holds for both pairings in wM2 and ALM. In (ii), wS2 Hit against No-tone Whisker CR fails at 1.3–1.5 s (p 0.114); it holds in the 1.0–1.5 s variant. |
| fig3c-delay-modulation-wm2-alm | partially_reproduced | Cell 38, Methods rule: up 13.8 against 11.7 and down 11.1 against 13.9. All four fractions are out of tolerance, but both χ² tests give p < 0.05 in the stated direction for all 3 seeds. With the code's mean-MAD rule the fractions match (16.0/14.3, 14.0/17.0), but the up test gives p 0.047–0.077. |
| fig3d-wm2-infragranular-delay | partially_reproduced | Cell 40: wM2 infragranular 0.95 ± 0.12 Hz is out of tolerance (1.1–1.3); supragranular −0.05 is in; p = 1.6e-6. No layer pair in A1, wS2 or ALM is significant. The code-MAD variant gives 1.13. |
| fig4-29-clusters | not_reproduced | Cell 10 of decoding_clusters_whisker: the Methods pipeline puts the BIC minimum at k = 44 (k = 39 ties it), outside 20–38. The code variant gives 36. Low confidence: 5 GMM initialisations against the paper's 1,000, on a very flat BIC curve (problem 6). |
| fig4b-named-clusters | blocked (methods_underspecified) | Cell 44: parts (2)–(4) hold. Cluster 1 is "mostly A1" under reading (b), largest share 30.5%, but not under (a), more than half. So reading (b) gives reproduced and reading (a) partial; by the criterion's all-readings rule that is blocked. Partial is the floor either way. |
| fig5a-single-neuron-context | partially_reproduced | Cell 46, Methods rule: the four fractions are out (wM2 up 17.9, down 11.5; ALM up 14.5, down 12.9) and the four Hz values are in. wM2 has the largest up fraction, and wM2 and ALM have more modulated neurons than A1, wS1 and wS2. The code-MAD variant puts 8 of 8 within tolerance. |
| fig5b-context-decoding-delay | partially_reproduced | decoding_delay cell 6: the code reading puts 2 of 5 within tolerance and the Methods reading 3 of 5. wM2 is 62.0 (code) or 63.1 (Methods) against 64, and ALM 58.9 or 58.5 against 61. All five tests give p < 0.05 and the ordering holds under both readings. |
| fig5b-decoding-time-course | reproduced | decoding_delay cell 8, code reading: (1) baseline about 50%; (2) A1 is highest in both cue windows (70.3 and 65.6); (3) holds in all five areas under both windows; (4) holds at every neuron count. The Methods reading covers only (4), at 5, 25 and 50 neurons; it was not run on the cue bins (problem 9). |
| fig5c-cluster-removal | blocked (methods_underspecified) | Cell 6. Code reading: the four decreases are within tolerance and significant, and one other pair is significant (cluster 24, A1), which gives partial. Methods reading: cluster 25 is not significant after FDR (p 0.085 in both wM2 and ALM) and cluster 11 is significant in wS1, which gives not reproduced. The two readings differ. |
| fig5d-null-space-decoding | blocked in the notebook; testable | See B10. The inputs (spike times, continuous C2 whisker angle, trials) are all in the processed NWB files the helper already reads. Only the subspaceID optimisation would have to be re-implemented. |
| fig6a-pca-delay-states | partially_reproduced | Cell 48, Methods rule: the geometry holds in every area; 3 of 10 explained variances are out (wS1 PC1 9.8, wM2 PC1 15.0, ALM PC2 6.8). The code-MAD variant puts all 10 within tolerance. |
| fig6b-context-coding-direction | reproduced | Cell 51: in wM2 and ALM all 6 comparisons give Hit higher with Bonferroni p < 0.05, under every split, rule and seed run. |
| fig6c-temporal-correlation | reproduced | Cell 53: all 6 wM2 and ALM comparisons hold (corrected p ≤ 0.004). |
| fig7b-early-whisker-response | reproduced | Cell 56: wS1 has significant negative bins at 1.015 and 1.020 s, wS2 at 1.010–1.025 s. All 5 areas have significant positive bins from 1.030 s, under both FDR families. |
| fig7c-no-whisker-cd-change | reproduced | Cell 58: Kruskal–Wallis p > 0.3 in every area under all 4 variants. |
| fig7d-context-decoding-after-whisker | blocked (methods_underspecified) | Cell 8. Code reading: wM2 is persistent from 1.025 s and ALM from 1.035 s, and A1, wS1 and wS2 start later, so the criterion holds. Methods reading (cut down to 2 baseline bins and 1 run): wM2 from 1.040 s, after ALM at 1.035 s, so it fails. |
| fig8a-wm2-lick-divergence | partially_reproduced | Cell 60: in wM2, Kruskal–Wallis p 0.005, Go-tone lick against no lick p 0.004, Nogo-tone p 0.28; A1, wS1 and wS2 show nothing. ALM (reported, not judged) is significant in both contexts with a stronger Kruskal–Wallis, which goes against "ALM weaker". |
| fig8b-lick-coding-direction | blocked in the notebook; likely testable | See B11. |
| figs18-later-lick-coding | blocked in the notebook; likely testable | See B11. |
| cluster-label-link | reproduced | Cell 42: all 10,294 labels map to distinct units, with matching area, CCF label and layer, and all are analysed units. |

### B. Problems

1. [affects a conclusion] Quiet rule (affects fig3c, fig5a, fig6a, fig3d, and by extension fig5b). The claims file's choice to judge on the Methods' median absolute deviation turns several outcomes from reproduced into partial. Under the code's mean absolute deviation, the paper's numbers come back almost exactly: fig5a 8 of 8, fig3c values, fig6a 10 of 10, fig3d 1.13 Hz. That strongly suggests the published figures used the mean absolute deviation. The notebook follows the claims file correctly; I report this, not correct it. The Methods text (paper, "Quantification of orofacial movements") does say "median absolute deviation".
2. [does not affect a conclusion, but the claims file requires it] decoding_delay and decoding_clusters_whisker never run the code-MAD variant. `session_classes` is always called with `rule="median"`. Given problem 1, the shortfall of about 2 points in wM2 and ALM in fig5b may come from that.
3. [affects a conclusion: borderline] quiet-trials-half (cells 7–8 and 21). The 343 trials with no video are counted as not quiet, justified as "the code would"; that is not verified. If MATLAB `median` without `omitnan` is used, one NaN would make every trial in the session non-quiet. Excluding those trials gives 54.22%, which is within tolerance, so the outcome depends on this one assumption.
4. [affects a conclusion] Reduced repetitions near the decision boundaries: 5 subsets against 100 for the code decoder, 1 for the Methods decoder; Fig. 7d with 1 run and, for the Methods decoder, only 2 of 10 baseline bins; fig5c with a single decode per session. The fig5c Methods p values (0.034 before FDR, 0.085 after) and the fig7d Methods onsets (wM2 1.040 against ALM 1.035) are the ones that flip those two claims to methods_underspecified, and Monte-Carlo noise could easily move them. The notebook should show the spread across seeds.
5. [affects a conclusion] fig5c, reading (a) (Methods) runs only clusters 11 and 25. The "no other cluster" condition is untested under that reading.
6. [affects a conclusion] fig4-29-clusters (`bic_scan`, `embed`):
   - The GMM uses 5 initialisations against the paper's 1,000. The BIC differences across k = 30–44 are about 100–400 on about 1.1e6, and k = 39 and 44 are tied, so the arg-min is unstable. No seed check is run.
   - `reg_covar=1e-6` is absolute, while the embedding components have variance of order 1/N ≈ 1e-4, so it may shape the BIC.
   - `cluster_matrix` centres each neuron's own row (`X - X.mean(axis=1)`), not each bin across neurons as PCA usually would.
   - It takes the unscaled left singular vectors U as the 17 PCs.

   None of these choices is checked against Data_Clustering.ipynb.
7. [does not affect a conclusion] `g.bin_index(0.8, 1.0)` returns 21 bins (179–199, covering [0.79, 1.0)), as the helper says the code's nearest-label rule does. Cell 38 and cell 46 use 20 bins (180–199) instead. A 10 ms inconsistency across claims.
8. [does not affect a conclusion] `decode_bin` z-scores over all balanced trials before the cross-validation folds, and before the inner grid search under reading (a). Normalisation statistics leak from test to training data. It follows the code and the effect is small, as my synthetic null run was about 50%.
9. [affects a conclusion: completeness] fig5b-decoding-time-course: the claims file says to run both SVM readings, but the Methods reading was never run on the baseline-to-cue bins needed for parts (2) and (3). The outcome rests on the code reading alone for those parts.
10. [affects a conclusion] fig5d is blocked although the data are in the archive. Spike times, the continuous C2 whisker angle and the trials are in the processed NWB files the notebook already loads. Only the subspaceID orthogonal-subspace optimisation (Hasnain et al.) is missing, and it can be re-implemented on the Stiefel manifold. Its stated reason was removed with the summary, so I could not check it.
11. [affects a conclusion] fig8b and figs18 are blocked, but the archive metadata (API, asset 77fbb94d…) lists `BehavioralEvents` and `BehavioralTimeSeries` in each processed file. The helper already reads the session-long `Jaw_Coordinate` and says the files hold the piezo lick trace. Data_Clustering.mat and Area_list.mat were already read from the Zenodo record by range requests, and `data_helpers/Lick_times.mat` sits on the same record. At least a version with lick times derived from the archive could have been run.
12. [does not affect a conclusion] Data notes the notebook reports correctly:
    - The opto files give 7 ALM mice where the Methods say 8.
    - 12 opto sessions have the genotype C57BL/6JRj but still show inactivation effects.
    - wS2 has CCF-filtered units in 19 sessions, not 24.
    - One session has 11 trials of `trial_type` 0, and PG076 has no No-tone trials.
13. [does not affect a conclusion] I tested the helpers on synthetic data, and `bh_fdr`, `auc_si`, `roc_test`, `kruskal_lsd`, `_counts` and `paired_bootstrap_p` all behave correctly:
    - `bh_fdr` equals scipy's `false_discovery_control`.
    - `auc_si` equals 2·(sklearn AUC − 0.5).
    - `roc_test` has a null rejection rate of 0.043.
    - `kruskal_lsd` gives the same H and p as scipy.
    - `_counts` uses left-closed bins.
    - `paired_bootstrap_p` has a null rate of 0.063, slightly liberal.
    - `decode_session` gives about 50% under the null and about 85% with a separation of 0.8 SD.

### C. What I could not check

- **The paper's code (Zenodo/GitHub).** I could not confirm the code-derived choices: the nearest-label bin convention, the 30% coding-direction split, the dropped "fourth A1 session", the clustering details in problem 6, MATLAB's NaN handling in the quiet rule, and whether Decoding_clusters_random_dropout.m really is "all against without" rather than a random-dropout control. Printing the relevant code lines next to each choice would settle this.
- **Contents of `BehavioralEvents` and the lick time series in the NWB files.** A cell listing the processing/behavior groups and their time ranges would settle the fig8b and figs18 blocks.
- **Robustness of the Monte-Carlo-limited outcomes.** Helpful additions:
  - BIC arg-min over several GMM seeds, or with more initialisations;
  - fig5c and fig7d Methods reading over several seeds, with all 10 baseline bins;
  - fig5b at 100 subsets, or at least the spread across seeds;
  - the code-MAD variant for every decoding claim.
- **Quiet-trial NaN handling.** A per-session count of trials whose baseline or pre-stimulus movement mean is NaN, under both MATLAB-style treatments.
- **The blocked-claim reasons.** The summary was removed, so I could not read the notebook's stated reasons for fig5d, fig8b and figs18.
