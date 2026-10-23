**A. Outcomes (31 claims in the claims file)**

| Claim | My outcome | Reason |
|---|---|---|
| pt-types-transcriptomic | reproduced | Cell 25: the criterion's counting rule gives 27 clusters, and the PT cells fall in Slco2a1, Hpgd and Npsr1 only. |
| pt-upper-thalamus-projection | reproduced | Cell 28: reading (c) gives 8 of 12, the same 8 as the thalamus group. Readings (a) and (b) give 11. A match under one reading is enough. |
| pt-lower-medulla-projection | reproduced | Cell 28: reading (c) gives 4 of 12, and all 4 of the medulla group reach the intermediate reticular nucleus. |
| pt-types-shared-targets | part 1 reproduced; part 2 blocked (methods_underspecified) | Superior colliculus 12 of 12 (cell 28). Part 2 can only be tested on the bulk-labelling images, and the paper gives no method for them. The test on the reconstructions is only a variant. |
| pt-retrograde-sublaminae | blocked (methods_underspecified) | Anatomy.zip holds 657 jpgs and no counts (cell 34). The counting method is open, and no folder holds superior colliculus labelling. |
| pt-projection-cluster-mapping | reproduced | Cell 30, reading (b): medulla 62 of 62 in Slco2a1; thalamus 72 + 19 = 91 of 94. |
| pt-types-account-for-all-pt | partially_reproduced | Cell 28: superior colliculus 17 of 18 under both readings (AA0134 has 0 termini and 0 mm there); 0 of 18 lack both thalamus and medulla. The criterion has no partial rule, so this is my label for one part holding. |
| pt-marker-genes | blocked (data_missing) | Confirmed: no smFISH data in the dandiset or in Anatomy.zip. |
| pt-bulk-sc-fold-change-correlation | reproduced | Cell 32: r = 0.874 (0.87 ± 0.087). I checked the replicate columns against the sample key. |
| pt-tagged-units | not_reproduced | Cell 36: 44 PTupper and 56 PTlower (code rule) or 42 and 63 (session rule), against 61 ± 6.1 and 69 ± 6.9; mice 8 and 4 match. The cause is missing data: on the processed data the same rule gives 61 and 69, and the dandiset lacks 11 sessions (cell 11). |
| pt-depth | reproduced | Cell 38: 636 µm against 1004 µm, and 636 against 892 µm without the right hemisphere. |
| pt-spike-rates-similar | not_reproduced | Cell 40, main reading: the peak t-test gives p = 0.030 (< 0.05). PTlower medians are also out of tolerance (6.69 Hz baseline, 20.96 Hz peak). |
| pt-lower-heterogeneous-rates | reproduced | Cell 42: PTlower variance is larger. Bartlett and F test: baseline p = 0.002, peak p < 1e-4. |
| pt-lower-bursting | partially_reproduced | Cell 44: Fisher p = 0.035; PTlower 19.6% is in tolerance, PTupper 4.5% (2 of 44) is not. With 44 units, 3.3 ± 0.33% cannot be reached (one unit is 2.3%). |
| pt-selective-any-epoch | not_reproduced | Cell 46: 99 (or 96–100 under other readings) against 122 ± 12.2. The fraction is 0.99 against the paper's 0.94; the count fails because units are missing. |
| pt-variance-explained | reproduced | Cell 48, main reading: maximum ratio 1.08 (PTupper) and 1.23 (PTlower), both ≤ 1.3. The session-rule variant exceeds the bound for PTlower (1.36). |
| pt-preparatory-activity | partially_reproduced | Cell 51: part (b) holds under every reading. Part (a) counts are 29 and 38, against 40 ± 4 and 44 ± 4.4; as fractions, 66% and 68% against 66% and 64%. |
| pt-upper-early-preparatory | methods_underspecified | Cell 53, main reading: "larger" holds under rule (i) and fails under (ii); "more consistent" fails (PTupper spread 0.31 against PTlower 0.25). That is partial under (i) and not reproduced under (ii). |
| pt-upper-persistent | not_reproduced | Cell 55: reading (a) fails (68 to 165 of 420 bins not significant); reading (b) gives p = 0.053 and 0.058. Close to the threshold; the processed-data variant passes. |
| pt-lower-cdearly-decay | reproduced | Cell 57: p from 0.30 to 0.40 under every reading (main 0.348; paper 0.34). |
| pt-cd-stability | reproduced | Cell 59: PTupper is higher under both measures and every reading (r 0.49 against 0.18; inner product 0.46 against 0.22). |
| pt-single-neuron-early-selectivity | reproduced | Cell 61, measure (a), unit range: 0.410 and 0.237, both in tolerance; t-test p = 0.0012, Mann-Whitney p = 0.0041. |
| pt-upper-decoding | partially_reproduced | Cell 63: means 64.3% and 58.7% in tolerance; Mann-Whitney p = 1e-4; PTlower count 3 matches. PTupper count is 9 against 15 ± 1.5, and 8 (not 10) of the top 10 are PTupper. |
| pt-upper-decoding-rectified | partially_reproduced | Cell 65: Mann-Whitney test holds, PTlower 0 reach 70%, PTupper mean 61.8% in tolerance. Out of tolerance: PTupper count 8 (15 ± 1.5), top 21 has 16 PTupper (20 ± 2), PTlower mean 56.20% (needs at least 56.3%). |
| pt-lower-late-and-motor | reproduced | Cell 69: CDlate, larger (a and b), faster and longer all hold under all 16 readings. |
| pt-cdgo-onset | partially_reproduced | Cell 67: PTlower is earlier under every reading, but the onsets are 30–45 ms and 75–85 ms, against 24 ± 5 and 48 ± 5. |
| reaction-time | blocked (data_missing) | Confirmed in the archive: the files hold lick times only and no video. Lick latency (median 0.122 s, cell 7) measures something else. |
| pt-cd-change-at-go-cue | methods_underspecified | Cell 73: level 0.5 meets the criterion (PTlower shorter and PTupper ≥ 0.2 s); level 0.75 gives PTupper 0.19 s < 0.2 s, so only partial. |
| pt-lower-movement-termination | methods_underspecified (at best partial) | Cell 76: CDlate selectivity stays significant after the last lick under every reading (5–29 bins). CDgo passes only with window (a) and the subject reading of a mouse, so the windows and mouse readings give partial against not reproduced. |
| pt-cohort-control | partially_reproduced | Cell 81, main reading: the CDgo onsets agree within the PT difference, but the PTlower-cohort CDearly median (9.82) lies above the PTupper-cohort 95th percentile (8.86). |
| pt-types-differ-in-timing | partially_reproduced | Of the six claims it depends on, single-neuron early selectivity (PTupper side) and late-and-motor (PTlower side) are reproduced; persistent, early-preparatory and onset are not. |

No chance level is stated in the paper for any selection tested here.

**B. Problems**

1. [affects a conclusion] Archive (cells 11–14): the dandiset lacks 11 processed sessions, holding 17 included PTupper and 13 included PTlower units, plus their unidentified units (232 against 495, 430 against 511). This alone explains the failures of pt-tagged-units and of the counts in pt-selective-any-epoch, pt-preparatory-activity (a), the two decoding claims and pt-cohort-control. All 117 tagged units the dandiset does hold agree with the processed data on cell type, inclusion and depth.
2. [affects a conclusion] Claims file: these criteria judge raw counts and percentages from the paper's 130 units, which cannot be reached on 100 units: pt-selective-any-epoch, pt-preparatory-activity (a), the 70% counts and top-10/top-21 in the decoding claims, and the PTupper percentage in pt-lower-bursting. The fractions agree well (29/44 and 40/61 are both 66%). I am reporting this, not correcting it.
3. [does not affect a conclusion] `binned_counts` (cells 9, 10): a trial's spikes are taken by time window on the file's clock. At least 11.65% of baseline-epoch spikes belong to the previous trial, which inflates baseline rates, the baseline subtraction of projections and the rectification threshold. Cell 11 shows the stored order is trial by trial, so spikes could have been assigned by order, but the notebook does not do this. The borderline results (pt-upper-persistent p = 0.053; rectified PTlower mean 56.20%) do not change outcome, because other conditions already decide those claims.
4. [does not affect a conclusion] Cell 77: the criterion accepts the rebuilt last lick only if the outcome is unchanged when disagreeing trials are left out. The notebook's own check prints "Same holds/fails … False": subject, projection (a), CDgo, window (a) flips from True to False. The claim is methods_underspecified either way.
5. [does not affect a conclusion] `binned_counts` with `align`: lick-aligned rates contain only spikes up to 3.0 s after the go cue, so later post-lick bins count as zero rate. This biases toward "selectivity ceases". It is not quantified, and the claim fails on CDlate anyway.
6. [does not affect a conclusion] Claims file, pt-lower-movement-termination: the window readings fail for CDlate even on the paper's own processed units and licks (cell 76 variant). So the readings likely do not capture what the paper claims.
7. [does not affect a conclusion] Claims file, pt-cohort-control: the CDearly test fails because the PTlower cohort is more selective than the PTupper cohort, the opposite direction to the PT-type difference. The criterion does not test whether the cohorts explain that difference.
8. [does not affect a conclusion] pt-cdgo-onset (cell 67): the onsets are also out of tolerance on the paper's own units (37.5 and 57.5 ms, about 13 ms late for PTlower). That points to a systematic difference in the onset or projection method, which the notebook does not look into.
9. [does not affect a conclusion] pt-cd-change-at-go-cue (cell 73): at level 0.5 the main reading separates the types by one bin (0.3675 against 0.3725 s), on a median with no uncertainty, and PTlower's 0.37 s is hardly "rapid". The code variant gives 0.07 s.
10. [does not affect a conclusion] Cell 11: the processed data hold 150 tagged units, not the paper's 143; the notebook does not reconcile the two.

I tested the helpers on synthetic inputs: `smooth`, `trial_means`/`bins`, `onset`, `first_run_end`, `isi_burst_fraction`, `roc` (against a brute-force search, including ties), `_boot_dprime` (against `dprime`) and `unit_draws`. All behave as documented. The statistical tests are the ones the criteria name: Student's t, two-sided Fisher, two-sided Mann-Whitney, Bartlett and F. I found no train/test leakage; the single-unit accuracy is in-sample, which is the paper's own method.

**C. What I could not check**

- How much the storage contamination (problem 3) moves results. Needed: per-unit baseline rates and the bootstrap with spikes assigned to trials by stored order, or the processed-data variant restricted to the 100 units the dandiset holds. The second would also separate the effect of missing units from the effect of the file format, for every claim.
- Why AA0134 has no superior colliculus node. Needed: a list of the structures its axon nodes fall in.
- The cause of the onset offset. Needed: the q5 curves from 0 to 0.1 s for the dandiset and the processed data.
- How often the lick-aligned window is truncated. Needed: the fraction of correct trials whose last lick comes more than 2.5 s after the go cue.
- Whether the Anatomy.zip H2B stacks (BL648) would allow the thalamus–medulla co-labelling count. Needed: a sample image and its resolution.
- The Figshare sequencing and axon files themselves, which I did not download; I relied on the notebook's outputs for them.
