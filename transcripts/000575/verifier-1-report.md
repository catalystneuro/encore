**Verifier report, round 1: Boran et al. (2022), DANDI:000575 version 0.231010.1811**

The claims file has 17 claims and the notebook tests all 17. None is treated as blocked.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| behavior-accuracy-by-set-size | reproduced | Cell 17: pooled 97.8/97.9/84.3/72.6%, all 88.2%, all within tolerance; order holds. F(3,45) = 89.78 against the paper's 89.79, permutation p = .0002. |
| behavior-capacity | reproduced | Cell 19, reading (a)(i): KP median 3.23 (range 2.25–5.00), KC median 3.00 (range 2.11–4.50). Per session (b)(i) also passes, and its KC range 1.92–4.50 matches the paper's. |
| table1-capacity-and-neurons | reproduced | Cell 21: all 13 Kmax values and all 13 neuron counts equal Table 1 exactly. |
| behavior-rt-set-size | partially_reproduced | Cell 23: 2678 correct trials; RT rises in 16 of 16 sessions; median-RT F = 48.47 (exact), p = .0002. No slope reading in the criterion reaches 118±11.8 (68.8–76.2 ms/item). The slope of the median RTs per set-size step gives exactly 118.1 ms (problem 2). The criterion has no partial clause. |
| neurons-recorded | partially_reproduced | Cell 25: total 809, per session 50.6 ± 25.4, range 11–96, all within tolerance. Region counts fail under both readings: (a) Ent 168 against 209, (b) Hipp 361 and Amg 226. No partial clause in the criterion. |
| spike-sorting-quality | not_reproduced | Cell 27: ISI < 3 ms is 0.79 ± 1.77% (SD outside 1.54 ± 0.154), majority below 0.5% holds (62.5%). SNR 5.93 ± 2.31 against 3.81 ± 0.82. ISI reading (i) and SNR reading (b) cannot be tested: the data hold spikes only inside trials and no sorter noise level. |
| firing-rates-by-period | reproduced | Cell 29: all five medians and ten quartiles are within 10% under both trial readings (a) and (b), with trial extent (i). |
| fig2c-maintenance-neurons | partially_reproduced | Cell 31: all regions p = .002. Counts by tip location are 62/20/16 paired (Hipp out of tolerance) and 55/19/13 unpaired (Amg out). Electrode-name counts are all off. No single reading puts all three counts in tolerance. |
| fig2d-workload-modulated-maintenance-neurons | not_reproduced | Cells 33–35: under every reading, increase and decrease counts are 0–3 per region and at null level (p = .04–1). The cluster reading gives 1/1/0. The paper reports 10, 5 and 6. |
| maintenance-neurons-correct-vs-incorrect | not_reproduced | Cell 37: correct 42–57 and incorrect 13–19 (paper 30). The difference is at null level, p = .33–.71, under all four readings; subsampling gives 11.5–16.9. |
| fig3b-test-neurons | partially_reproduced | Cell 39: main reading (a) gives 86 or 79 against 46. Reading (b) paired gives 42 in total (within tolerance) but region counts 23/10/9 or 20/18/4 are off. Every region is significant. No partial clause in the criterion. |
| fig4a-dpca-separates-set-sizes | not_reproduced | Cells 42–43: kernel (a) without regularization gives 32.9% for dPCs 2–4 and 81.4% for the first 15, both within tolerance. The shuffled-label test fails: p = .27 for dPCs 2–4, .35 for set-size variance, .53 for maintenance distance. |
| fig4b-speed-lowest-in-maintenance | reproduced | Cell 47: encoding is highest; maintenance is below encoding and test, p = .001, under both subsampling readings. Fixation is lowest, which the criterion excludes from the claim. |
| fig4c-distance-largest-in-maintenance | partially_reproduced | Cell 49: maintenance exceeds encoding (p = .001), but fixation is the largest period, so only the first condition holds. See problem 4 on what this measure reflects. |
| fig4d-decode-workload-all | not_reproduced | Cells 51–52: accuracy 0.44–0.49 under every reading combination, p ≥ .53. Leave-one-out quartiles are 0.44–0.47 against the paper's 85.7–87.6%. |
| fig4d-decode-workload-regions | not_reproduced | Cell 54: Hipp, Ent and Amg give 0.45–0.53, p ≥ .30, under both region readings. |
| decode-performance-not-significant | reproduced | Cell 56: no group reaches p < .0125 (p = .27–.77). Accuracies (0.46–0.54) are within tolerance. See problem 10 on how much weight this carries. |

Chance level: the paper's decoding chance is 50% (scrambled labels), and the notebook's scrambled medians are 0.47–0.51, so they agree.

**B. Problems**

1. [affects a conclusion] Cell 8 assigns regions by reading (a), the tip contact's atlas label. 133 units sit on tips labelled "unspecific" or "FuG", and the author's own fallback puts all of them in Hipp by electrode name. Reading (a) gives 495/168/146 and the paper gives 454/209/146. The excess and the deficit are both 41 (495 − 454 = 209 − 168), so moving 41 of the fallback units to Ent would reproduce the paper's region counts exactly. No other assignment of those units was tried. This affects neurons-recorded, fig2c, fig3b and the region decoding.
2. [affects a conclusion] Claims file, behavior-rt-set-size: all three of its slope readings regress RT on the set-size value (1, 2, 4, 6). Regressing the median RTs printed in cell 23 on the condition step (1, 2, 3, 4) gives 118.1 ms, the paper's number. The mean RTs give 129.9 ms that way. This is a misreading in the claims file; I report it and have not corrected it.
3. [affects a conclusion] Cells 13–15 test the alignment of spikes with trial labels. Every analysis that depends on per-trial labels fails, while within-trial contrasts (firing rates, maintenance and test neurons) roughly hold. Workload decoding at k = 0 is consistently below chance: 0.44–0.46 in every leave-one-out run, against a null of 0.50. On synthetic data the decoder gives 0.50 with no signal and 1.0 with signal (I tested `decode` under both readings c and d), so the decoder is sound. The label-dependent not_reproduced outcomes may therefore reflect a defect in the deposited data. The notebook leaves this open: k = 3 was chosen from the same data, the best k per session ranges from −9 to 9, and the scan has no per-session null.
4. [affects a conclusion] Cells 46 and 49, fig4c: the largest distance is in fixation, before any stimulus. Cell 43 shows the maintenance distance equals the shuffled-label null (p = .53). The "maintenance > encoding" result that earns the partial outcome therefore reflects period-dependent noise, not separation by set size.
5. [does not affect a conclusion] Cell 42: dPCs 1–4 are all time components, so the claims file's test of dPCs 2–4 against shuffled set-size labels cannot detect set-size information. The notebook's added set-size variance test covers this. Cell 41 also uses 10 ms bins where the paper uses 1 ms, which is negligible after 167–200 ms smoothing.
6. [does not affect a conclusion] Repetitions are below what the criteria specify:
   - decoding uses 50–100 runs and 100–200 nulls instead of 500 and 1000 (cells 51, 54, 56);
   - fig3b(b) uses 99 repetitions × 200 permutations (cell 39);
   - the cluster reading uses 99 shuffles (cell 34);
   - fig4b(b) uses 100 runs (cell 46).
   
   In the regional k = 3 variant (cell 54), 60 nulls make the minimum possible p .016, which is above .0125, so that variant cannot reach significance. It is a variant only.
7. [does not affect a conclusion] Cell 31: the claims file promises a check of fig2c at 5000 permutations, and the notebook does not show it.
8. [does not affect a conclusion] `welch_t` uses unequal variances. statcond's unpaired t may pool variances, which changes little in a permutation test. My synthetic test of `perm_ttest` gave false-positive rates of 0.03–0.08 and full power.
9. [does not affect a conclusion] Cells 51 and 56: the paper's 145–169 training trials equal 95% of each session's correct trials (153–178 in cell 3). That points to decoding on each session's whole unbalanced correct-trial set. Neither reading (c) nor (d) does that, and the notebook does not print the training-set size it used. Accuracy is below chance under both readings, so this is unlikely to change the outcome.
10. [does not affect a conclusion] Cell 56: the claim of absence is reproduced by a pipeline that also fails to detect workload, which the paper decodes at 87.5%. With 13 folds of one trial per label, the test has little demonstrated sensitivity, so the reproduced outcome carries little weight.
11. [does not affect a conclusion] behavior-rt-set-size, neurons-recorded, fig2c and fig3b: the criteria define no partial outcome. Partial is my judgment there, based on the parts that hold.

**C. What I could not check, and the output that would settle it**

- Whether a natural group of 41 among the 133 fallback units recovers 454/209/146. A crosstab of those units by bundle, participant and the atlas labels of their contacts 2–3 (cell 8) would show it.
- Whether spikes and labels are displaced, and from which trial on. Three outputs would settle this:
  - a per-session alignment scan with a label-permutation null;
  - the scan split by sessions with 192 trials against sessions with fewer;
  - the source's trial numbering, if the files hold it.
- The pseudo-trials per fold and the training-set size in each decoding run (cells 51, 54, 56).
- The fig2c counts at 5000 permutations (cell 31).
- The marginalization of dPCs 2–4 in the shuffled fits (cell 43).
- I did not view the plotted images; I relied on the printed ranges.
- On the archive side, version 0.231010.1811 lists 18 assets, including two pairs of identical-size sub-12 files, which agrees with the notebook. I did not stream any file.
