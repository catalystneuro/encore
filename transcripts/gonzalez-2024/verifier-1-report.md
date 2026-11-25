**A. Outcomes** (30 claims in `gonzalez-2024.yaml`)

| claim | outcome | reason |
|---|---|---|
| fig1d-task-performance | partially_reproduced | Cell 15: accuracy 73.0% is within 72.6 ± 7.26, but trials per session are 152.0 against 110 ± 11. The repository's perf_table gives the same 152, so the gap comes from which sessions are counted, not from the computation. |
| fig1-switch-performance | partially_reproduced | Cell 17: Switch accuracy 73.8% is within tolerance, and non-Switch accuracy is 2.4 points away (inside the assumed 10-point threshold). Switch trials per session are 69 against 54 ± 5.4, so that value fails. |
| fig1-training-to-criterion | blocked (data_missing) | I checked the archive: all 276 assets are recorded OF or T3* sessions (133 + 143), and none is a pre-surgery training session. |
| fig2c-cue-error-coding | reproduced | Cell 23, isolated units: left 0.60 > stem 0.29 > right −0.23. LRT 89.3 (p = 4e-20), Wald 89.0 (p = 5e-20); the paper gives 85.25 and 90.45. |
| fig2d-cue-remapping | reproduced | Cell 25: mean −0.54 (isolated) and −0.55 (all units), CIs exclude 0, within −0.67 ± 0.44 for every seed. |
| fig2e-unit-remap-behaviour | reproduced | Cell 27, isolated units: tau −0.261 to −0.269 and slope −0.142 to −0.147, both within tolerance; LRT p ≈ 1e-10. With MUA, tau −0.23 is out of tolerance. |
| fig2f-session-remap-behaviour | partially_reproduced | Cell 29: LRT p < 1e-4, slope negative, tau −0.42 (isolated) within tolerance, and \|tau\| is larger than at unit level. The slope is −0.385 (isolated) / −0.384 (all), outside −0.22 ± 0.11 under both readings. |
| fig2g-population-remap-behaviour | reproduced | Cell 32: slope −0.10, LRT p = 6e-7. |
| fig2h-subject-remap-behaviour | reproduced | Cell 35: tau is negative in 5 of 5 subjects, which meets the "at least 4" criterion. The paper's "all but one" is therefore not matched literally; Ca (fewest units) is the weakest at −0.14. |
| fig2-remap-behaviour-controls | reproduced | Cell 38: 12 of 12 controls give LRT p < 0.05 with a negative slope. |
| fig3d-cue-rate-remapping-model | reproduced | Cell 59: LRT p ≈ 1e-260; in the U_Z reading Z+C beats Z (+0.85) and ZxC (−1.02). Mean Z+C R2 of isolated units is 0.123, within 0.12 ± 0.012. |
| fig3e-zone-decoder-cue | blocked (other) | The decoder was not run (cell 67). The data needed are in the dandiset, so this is not a data block. |
| fig3f-decision-decoder | blocked (other) | Same as fig3e. The paper's chance level (BAC 0.5) was never compared. |
| fig3g-decoder-tracks-behaviour | blocked (other) | Same as fig3e. |
| fig4c-reward-error-coding | reproduced | Cell 40, isolated units: 357, 326 and 374 of 510, each within tolerance and above half. LRT p = 1e-10. |
| fig4d-reward-remapping | reproduced | Cell 42: −1.02 (isolated), CI (−1.54, −0.50); stable across seeds. The variant null balanced for correct gives −0.61, also within tolerance. |
| fig4ef-reward-remap-behaviour | partially_reproduced | Cell 44: both LRTs are significant with negative slopes. Under neither unit set are all four values in tolerance: isolated units fail on unit tau (−0.242) and session tau (−0.359); all units fail on unit tau (−0.239) and session slope (−0.41). |
| fig4gh-reward-remap-population-subject | reproduced | Cell 46: population slope −0.107, p = 1e-10; 5 of 5 subjects negative. |
| fig4-reward-remap-behaviour-controls | reproduced | Cell 48: 12 of 12 controls pass. |
| fig5-reward-rate-remapping-model | reproduced | Cell 61: LRT p ≈ 1e-177; Zi+R beats Zi (+0.97) and ZixR (−0.81). The pairwise fixed effects alone have p of 0.07 and 0.13. |
| fig4s5-cue-reward-remap-correlated | reproduced | Cell 50: unit, session and population taus are all positive with p < 1e-6. |
| fig4s6-incorrect-coding-overlap | partially_reproduced | Cell 52: both Fisher tests have p < 0.05 with incorrect overlap greater (isolated strict p = 0.0028). The "no KS difference" part holds only for isolated units with the claim seed (0 of 12 tests at p < 0.05). It fails with all units (5 of 12) and on 2 of the 4 other seeds for isolated units. |
| fig4s7-error-signal-persists | reproduced | Cell 55, isolated units: all four LRTs are p < 0.05 in the stated direction (0.043, 0.0012, 5e-7, 0.042). Two of them are close to 0.05, and one fit needed a Powell refit. |
| fig6cd-of-aggregate-model | reproduced | Cell 66: the aggregate model has the highest test R2 (0.096) and r_p (0.41); both LRTs have p ≈ 0, for 20 s and 30 s blocks. |
| fig7b-matched-units | blocked (data_missing) | I checked the archive: the HDF5 trees hold only acquisition/{firing_rates, track_data, unit_table, trial/event tables}, with no units table, spikes or waveforms. So matching cannot be recomputed. |
| fig7de-hd-speed-tradeoff | blocked (other) | Blocked only through fig7b. Clustering could be run on the paper's matches (see problem 1). |
| fig7f-tuning-metrics-match | blocked (other) | Testable with the paper's clusters and the open-field data in the dandiset; not run. |
| fig7g-hd-cluster-remaps-more | blocked (other), wrongly | The claim says `data: with_labels` and takes clusters from the paper's unit_table.csv. It is testable. |
| fig7h-hd-cluster-encoder-scores | blocked (other), wrongly | Same as fig7g. |
| methods-lookahead-encoder-best | not_reproduced | Cell 63: Z50 has the highest mean R2 only among isolated units (0.114 against 0.109 for Z0); for MUA, Z0 is higher. In the U_Z reading, Z50 against Z0 gives p = 0.98 (isolated) and the sign reverses with all units. No pairwise test was run for the mean-R2 reading. |

**B. Problems**

1. [affects a conclusion] Cell 67 blocks fig7de, fig7f, fig7g and fig7h because they depend on fig7b. But fig7g and fig7h take clusters from the paper's `metadata/unit_table.csv` (`data: with_labels`), and that file has `cl_name_T3`, `cl_name_OF` and uuids, which match the `cl_name` and `uuid` columns of the dandiset's unit tables. I checked: 274 of its 306 rows have both sessions in the dandiset. fig7f can use those clusters plus the open-field data. fig7de could cluster the aggregate coefficients of the paper's matched units. Four claims were left untested that could have been tested.
2. [affects a conclusion] fig3e, fig3f and fig3g are marked "blocked, other" because the decoder was not ported in time. The notebook itself says the data are present. This is an analysis that was not done, not a limit of the data, and no chance level was compared for fig3f.
3. [affects a conclusion] `enc_lmem` (cells 57 and 63): the fixed-effect p-values test each level against 0, not one model against another. For methods-lookahead-encoder-best, the mean-R2 reading therefore has no Z50-vs-Z0 or Z50-vs-Z-50 test. The criterion needs one, so that reading could not be judged.
4. [does not affect a conclusion] The LRT degrees of freedom are the number of levels minus one (2, 2, 2, 3). The paper reports chi2(3) for fig2c and fig5 and chi2(4) for fig6cd. That pattern points to a different null model, for example `~ 0`, or a different df convention. Every p is far below 0.05 either way.
5. [does not affect a conclusion] `tma.session_perf`: `pct_sw_correct` divides by all Switch trials, including change-of-mind trials that have no correct flag. On synthetic input it gives 1/3 where the answer is 1/2. `pct_correct` correctly leaves those trials out. This biases Switch accuracy slightly downward.
6. [does not affect a conclusion] Claims file, fig1d: it says fig1.ipynb prints 110.25 as the median of five subject medians. That is impossible with integer trial counts: each subject median is a whole or half number, and the median of five values is one of them. The file's description of how the paper aggregates is probably wrong. Reported, not corrected.
7. [does not affect a conclusion] `tma.speed` takes speed from unsmoothed frame-to-frame differences, and the speed control blanks a median 45% of samples (cell 38). Whether the paper's `compute_velocity` smooths first was not checked. The controls passed anyway.
8. [does not affect a conclusion] Cell 52, liberal Fisher test: every unit has a nonzero coding score for both cue and reward. So "incorrect in one only" and "correct in one only" are the same set of units by construction (609 = 609; 186 = 186). The test then compares only units incorrect in both against units correct in both, which mostly reflects how common incorrect coding is, not overlap beyond chance. This follows the claims file's reading of the table.
9. [does not affect a conclusion] fig4s7 (cell 54): units are kept if they have more than 5 incorrect outbound trials with a stem rate, while the legend says at least 5 incorrect trials per session. All 1744 units pass, so the selection does nothing. The two LRTs near p = 0.04 make the outcome fragile.
10. [does not affect a conclusion] fig3d: the claim is judged on the raw mean R2 of units (0.123). The LMEM estimate is 0.107, just below the 0.108 tolerance bound.
11. [does not affect a conclusion] `pop_remap_score`: the isolated-unit population score uses n = all units × zones. This is a variant only; the main reading uses all units.
12. [does not affect a conclusion] Data scope: the dandiset lacks 12 sessions that the repository's session table lists (224 units, 65 of them isolated). That leaves 510 isolated units against the paper's roughly 565. The notebook states this.

**C. Not checked, and what would have let me**

- Which angle column the head-direction model uses (`hd` or `ha`), and its unit, in the open-field data. An output of the hd and ha ranges per open-field file would have settled it.
- The size of the speed and reward blanking against the paper's code. A per-session distribution of blanked fractions, plus speed computed with and without smoothing, would have helped.
- Pairwise Wald contrasts on the mean-R2 LMEM (Z50−Z0, Z50−Z−50, Z+C−Z, Zi+R−Zi) were not printed; with them I could have judged that reading for methods-lookahead-encoder-best.
- Whether the fig1d and fig1-switch gaps (152 and 69 against 110 and 54) come from session selection. A table of trial counts per subject alongside perf_table.csv, with candidate filters (for example task version, or n_cells ≥ 1), would have shown it.
- fig7 cluster counts in the dandiset subset: the number of paper-matched units by `of_cluster_id` that map to dandiset units, which the fig7g and fig7h tests would need.
