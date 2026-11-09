**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| dataset-holds-paper-sessions | not_reproduced | Cell 17 finds none of Table 2's subject or session IDs in 000336, which holds 16 subjects recorded 2022–2023. I checked all 2356 paths of 000336 against the archive API myself: no ID matches. The two subjects the notebook never opened (690226, 698808) were recorded Oct–Nov 2023. |
| table1-subjects | reproduced | Cell 19: 13 mice, split 3/3/4/3 across the four groups, 7 male and 6 female, at least 3 sessions each. Sex, line, plane and date of birth agree with Table 1 for every mouse. |
| table2-sessions | reproduced | Cell 21: 50 sessions. Reading (a) gives 2 mice (411400, 412933); (b) gives 3, and is reported. Sessions 1–3 that passed QC: 33 files. |
| session-schedule | reproduced | Cell 23: under readings (a) and (ii), all 13 mice have 3 distinct local dates spanning 3–6 days. Durations are 70.23–70.53 min by reading (x) and 70.06–70.37 min by (y). Local dates equal Table 2's in 50 of 50 sessions. |
| imaging-planes | partially_reproduced | Cell 25: rate is 30 Hz (30.08–30.15 Hz from timestamps) and images are 512 × 512. But the depth matches Table 2 in only 47 of 50 sessions: the three 433414 files say 60 µm where Table 2 says 75. The criterion requires every session to match. |
| roi-counts-per-session | reproduced | Cell 27: reading (a) gives exactly 15–224 (somatic) and 159–1636 (dendritic), and every session's count equals Table 2 (50 of 50). |
| tracked-rois-per-plane | reproduced | Cell 29: counts are 254/261/516/129, exact. Reading (a) gives 32.9–75.0%, inside 28.8–82.5%. |
| fig8-example-matches | reproduced | Cell 31: 413663 has 136 tracked ROIs and 411771 has 47. The conflict counts cannot be tested, as the criterion says. |
| fig8-ordering-variation | reproduced | Notebook 2, cell 4: the mean somatic variation (range/mean 0.0039, SD/mean 0.0020) is below the dendritic one at 10% (0.137 / 0.057), at 20% (0.160 / 0.076) and with no threshold (0.038 / 0.015). Caveats are in B2 and B3. |
| stimulus-durations | reproduced | Cell 34: all 33 sessions are within tolerance. Gabor 34.03–34.13 min, flow 17.01–17.04 min, grey 29.98–30.04 s. |
| inconsistent-event-fraction | reproduced | Cell 36: Gabor 6.93% and flow 4.65% under both (a) and (b). Under reading (i) the mean is 31.5 Gabor and 32.2 flow blocks. On the 1.5 s / 1 s grids that the Methods state, every duration is in range; raw durations miss by at most 0.215 s. |
| fig5-stimulus-responses | reproduced | Cell 38: under all four reading pairs, every plane shows at least one stimulus with a difference. The flow comparisons carry it in every plane. Gabor shows no difference in L2/3-S under either selection. |
| fig6-behaviour | reproduced | Cell 41: in all 33 sessions and 11 mice, running (cm/s) and pupil (mm) traces span the session. |
| fig7a-snr-high-stable | reproduced | Cell 44: the smallest group 25th percentile is 2.32, so (a) and (b) hold. (i) and (ii) hold in all four planes, with a largest deviation of 4.8%. See B1: this result is guaranteed by how SNR is defined. |
| fig7b-signal-stable | reproduced | Cell 46: (i) and (ii) hold in all four planes. L5-D is close to the limit at 9.4% deviation against 10%. |
| fig7c-correlations-similar | blocked (methods_underspecified) | Cell 48: reading (i) holds in 5 of 6 comparisons and (ii) in 6 of 6. In L5 session 3 the dendritic median is 0.0186 against a somatic 25th percentile of 0.0190. By the criterion, readings that disagree mean blocked. |
| high-correlation-pairs | not_reproduced | Cell 51: (a) 0.0178%, (b) 0.0175%, (c) 0.0211%. All three are outside the 0.005–0.015% tolerance. |
| fig9-onset-offset-transients | reproduced | Cell 53: both readings find transients at onset and offset in 12 of 12 groups. The Gabor-only variant is weaker; see B6. |

**B. Problems**

1. [does not affect a conclusion] fig7a, `calculate_snr`. I ran the helper on pure Gaussian noise. It returns an SNR of about 2.06 at median 0, 2.56 at median +0.5σ, and 1.56 at median −0.5σ. So SNR > 1 holds by construction for almost any trace, and the observed 5th percentiles of 2.27–2.41 sit close to this noise floor. The paper's dashed line at 1 ("noise level") does not mark noise for this measure, and the claims file adopts it. The outcome follows the criterion, but the claim is uninformative. The notebook does not report the noise floor.
2. [does not affect a conclusion] fig8-ordering-variation, `ordering_counts`. The notebook reads the 10–20% overlap as intersection over union (IoU), which it states as an assumption. It also requires all three pairwise IoUs of a 3-way match to come from direct pairwise matches. A 3-way match built from two links gets IoU 0 for the missing pair and is dropped. The result is that dendritic counts fall well below the deposited tracked counts: 433414 gets 18–21 against 118, 433448 gets 19–26 against 112. With no threshold, counts are about twice the deposited ones. The rerun therefore does not approximate the paper's dendritic matching. Somatic counts are within 1 of the deposited ones. The somatic-below-dendritic result also holds with no threshold, so the outcome stands.
3. [does not affect a conclusion] `ordering_counts` / `_pair_job` rebuild the package's `run()`: each directed pairwise job is computed once, then reused to build the n-way table and prune it. The notebook never checks this against a direct `NwayMatching.run` on one ordering. It also uses the max projection in place of the average projection, which is a stated assumption.
4. [does not affect a conclusion] fig5, `fig5_measures`, selection (b).
   - For Gabor, ROIs are selected on their D (consistent) responses for both conditions. The Fig. 5b legend selects on inconsistent sequences ("Same as a., but for inconsistent sequences").
   - For flow, ROIs are selected on after-minus-before above the 75th percentile, and then after is tested against before. That is circular, but it is the claims file's own definition.
   - Reading (a) passes in every plane independently, so the outcome is unchanged.
5. [does not affect a conclusion] inconsistent-event-fraction, cell 36. The block count is judged on the session mean. Per-session counts range from 29 to 34 (Gabor) and 29 to 35 (flow), so some sessions fall outside 27–33. One run sits 0.387 s from its grid value (about 12 frames), which is never explained.
6. [does not affect a conclusion; possible claims-file misreading] fig9, cell 53. The Fig. 9a/b legends name Gabor onset and offset only. On that variant, offsets show a transient in only 7 of 12 groups (2 SEM reading) and 9 of 12 (Wilcoxon). Under the legend's reading, the outcome would be blocked, not reproduced. The claims file chose both stimuli from the text and the code.
7. [does not affect a conclusion] high-correlation-pairs, cell 51. The fraction rests on 134 pairs, 116 of them from mouse 413663's sessions 1–2. Per-session values span 0.0018% to 0.046%; mouse 433414 alone gives about 0.003%. The result does not reproduce under any of the readings regardless.
8. [does not affect a conclusion] Cell 17 reads subject metadata for only 14 of 000336's 16 subjects. The other two have no `_ophys` files, so the printed date range leaves them out. I checked them myself; they do not change the result.
9. [does not affect a conclusion] I checked the helper module's Tables 1 and 2 against the paper text: they match exactly (50 of 50 rows of Table 2). The helper functions `stimulus_events`, `window_means`, `rolling_mean` and `_median_pairwise_corr` behave correctly on synthetic inputs. There is no train/test split, so leakage does not apply, and the units are correct.

**C. What I could not check**

- **Equivalence to the paper's code.** I could not confirm that `calculate_snr`, `rolling_mean` and the correlation step match the paper's code (OpenScope_CA_Analysis and util). Printing the reference implementation's output on one session's traces next to the helper's would settle it.
- **The matching reconstruction.** Whether it equals the public package is unverified. A count from a direct `NwayMatching.run` on one ordering of one somatic and one dendritic mouse would settle it. A per-mouse table of how many 3-way matches are dropped only for lacking a direct pairwise link would show how much of the dendritic reduction comes from the IoU rule.
- **The 433414 depths.** The raw `location` strings of the three files are not printed, and neither is the code table's depth for all sessions, so I could not tell whether 60 µm is the deposited value or a parsing artefact.
- **`mouse_df.csv`.** Its content is not shown. Only its agreement with Table 2 on QC status is printed, not its session numbering.
- **Fig. 5 selection (b).** Per-session selected ROI counts and percentile thresholds are not printed.
- **The SNR noise floor.** A pure-noise control for the SNR measure (B1) is absent from the notebook.
