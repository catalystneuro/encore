**Verifier report, round 1: Peterson et al. 2021 on DANDI:000055 (0.261123.1703)**

The claims file has 25 claims and the notebook tests all 25. My outcomes: 14 reproduced, 9 partially reproduced, 1 not reproduced, 1 blocked. I checked the archive API: the version exists and holds 55 files, 845.87 GB, which matches cell 2. I ran the helper functions on synthetic inputs and they behave as documented: the angle folding, the day-balanced splits, the band statistics, the one-hot design matrix and the Morlet bank (a sine at 11, 76 and 121 Hz peaks at its own frequency, and every wavelet spans ±0.2 s).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| subject-days | reproduced | Cell 17: subjects 01–12 have exactly the paper's days, 55 subject-days. |
| roi-projection-link | reproduced | Cells 7–8: after the code's row rule, the rows equal the electrodes with positions in all 12 subjects. The largest-weight region is the nearest centroid for 36–55% of electrodes, against a shuffle maximum of 8–14, for every seed. For S03 and S12 the criterion's "rows = electrodes" holds only when electrodes without positions are left out (problem 6). The eight regions with density > 3 match the claims file. |
| cohort | partially_reproduced | Cell 19: six of seven quantities are within tolerance. The dataset has 7 subjects with depth-labelled groups; the paper says 5. |
| fig2-event-counts | not_reproduced | Cell 21: the minimum is 211 (reading a) and 210 (reading b) against 151 ± 15.1. The median is 770.5 under reading a (outside tolerance) and 691 under reading b (inside). |
| fig2-features-differ-across-subjects | reproduced | Cell 23: every p is below 1e-32 under both readings. |
| fig2-reach-shape | partially_reproduced | Cell 25: the duration and magnitude parts hold in 12 of 12 subjects and pooled. The angle part holds in 0 of 12: the KDE peaks sit near ±60–75°, outside the 15° window. |
| fig2-bimanual-skew | reproduced | Cell 28: ratio, overlap and class each hold in 12 of 12 subjects and pooled. S02, S04 and S05 are in both top-5 sets. |
| extfig2-1c-contralateral-larger | reproduced | Cell 30: holds in 12 of 12 subjects under both readings. The ratio is only 1.06–1.30 for S04 and S05, which the criterion does not judge. |
| extfig2-2-feature-correlations | partially_reproduced | Cell 32: 5 of 6 correlations are within tolerance. Magnitude vs duration is r = 0.229 against 0.26 ± 0.026. |
| fig2-days-and-waking | partially_reproduced | Cell 34: the busiest day holds more than half of the events for S05 and S09 but not S04 (0.40), so the day part fails. The waking part holds in all 12 subjects. |
| fig3-group-lfb-decrease-hfb-increase | reproduced | Cell 36: holds in all three named regions under both readings, for all 5 seeds and also unmasked. |
| fig3-sensorimotor-largest | reproduced | Cell 39: under readings a, b and c the top three regions are postcentral, precentral and inferior parietal, and the temporal regions are below all three, for all seeds. |
| fig3-lfb-more-widespread | blocked (methods_underspecified) | Cell 41: the readings disagree. Under (a) the region counts are 7 vs 7, or 6–8 vs 8 across seeds, so low frequencies are never more widespread. Under (b) the bin counts are 34.2 vs 23.9, so low is larger. The criterion says to block when the readings disagree. |
| fig4-precentral-subject-variability | partially_reproduced | Cell 43: parts 2, 3 and 4 hold. Part 1 fails for S09, whose HFB value is −0.030 dB. |
| fig5-band-power-differs-across-subjects | reproduced | Cell 47: p ≈ 0 in both bands, for both band statistics. |
| table1-subject-band-power-ci | partially_reproduced | Cell 49: the best reading (mean of band mean) puts 21 of 24 inside the paper's intervals. S03 HFB, S06 LFB and S06 HFB fall outside. |
| fig5-recording-day-effects | partially_reproduced | Cell 51: 20 of 24 pairs agree with the band mean, exactly at the threshold, and 19 of 24 with the median variant. S01 LFB, S01 HFB and S06 HFB are significant where the paper says not; S10 HFB is not significant (p = 0.10) where the paper says it is. |
| extfig5-1-baseline-reduces-day-variability | reproduced | Cell 53: the SD drops with baseline in 10/12 (LFB) and 11/12 (HFB) subjects, and in 91% and 90% of electrodes. Day effects remain (cell 51). |
| discussion-day-changes-small | reproduced | Cell 55: the largest day deviation is 1.48 dB (limit 2.2). Levels are 12.2–36.5 dB in the µV² reading. |
| fig6b-best-models-sensorimotor | reproduced | Cell 61: under (a), 14 of 14 (LFB) and 13 of 14 (HFB) models with R² > 0.05 are frontoparietal, and the sensorimotor median R² exceeds the temporal one. Under (b), the top three regions are frontoparietal in both bands. Both medians are negative. |
| fig6-r2-at-most-025 | reproduced | Cell 59: the largest R² is 0.177 (0.184 with the 80/20 split). This is an upper-bound claim, so it is easy to pass. |
| fig6c-angle-and-day-most-informative | reproduced | Cell 63: in LFB the top two are day and angle (n = 14), and they are also the top two in HFB and in every variant that was run. |
| extfig6-2-angle-most-retained | partially_reproduced | Cell 65: the angle part holds in all 6 region–band cells. The order part fails under both readings because speech ratio ranks second. |
| fig6d-upward-reaches-enhance-pattern | reproduced | Cell 67: the median angle coefficient is −0.70 for LFB and +0.54 for HFB. Cell 13 confirms the sign convention against the pose. |
| fig6d-angle-and-day-largest-coefficients | reproduced | Cell 69: day and angle are the top two under both readings, in both bands and both selections. |

No paper chance levels apply to these selections.

### B. Problems

1. [affects a conclusion] `session_spectral` and cell 10 build region power with each file's own good-electrode flags. The claims header says the bad-electrode zeroing and renormalisation are per subject, and the regression (cell 57) uses electrodes good in every file. In the dataset the flags differ a lot between days (S04: 17 bad on day 3, 2 on day 6). So the precentral electrode mix changes from day to day, which can create or hide day effects. The subject-level reading was not run for fig5-recording-day-effects (which sits exactly at 20/24), table1, extfig5-1 or discussion-day-changes-small.
2. [does not affect a conclusion] Cell 4 prints `ReachEvents timestamps = reaches start_time (max diff, s): 86400.0` and nobody follows it up. ECoG and pose windows use the ReachEvents timestamps, while time of day and duration use `start_time`. Since time of day goes up to 24.01 h, some events were probably cut with ECoG from the wrong day. The notebook does not count them; they are likely few.
3. [does not affect a conclusion] `session_spectral` sets non-finite dB (from a single zeroed electrode) to 0 before weighting and does not renormalise. `allzero` only flags samples that are zero on every good electrode, so partly zeroed segments pass with biased region power. The notebook does not count these.
4. [does not affect a conclusion] Required variants are missing. The bad-electrode variant (claims for fig6c and both fig6d) was never run; `include_bad=True` is never called. The log(onset speed + 1) variant was not run. Seed sensitivity for the regression covers R² only: at seed + 4000 the LFB selection drops to 12 models, and the Delta R² rankings were not refit.
5. [does not affect a conclusion] Forward selection runs on all events before the train/test splits, which leaks test data into model selection. This is the code's choice and the claims file prescribes it, so it is not the author's error. It inflates R² slightly for every Figure 6 claim.
6. [does not affect a conclusion] Cells 7–8 and `match_projection` drop all-zero rows and the first non-zero (density) row, then map the remaining rows in order onto electrodes with positions. The notebook never checks that the zero rows in S03 and S12 sit at the indices of the electrodes without positions. The counts suggest it (97 = 1 + 96), but it is not verified. The full-permutation null also could not detect a shift of one or a few rows. The claims file describes the code's rule as "drop all-zero rows" only, which misreads the code (it also drops the first non-zero row).
7. [does not affect a conclusion] Cell 36 runs Benjamini-Hochberg only over the bins computed, −1.5 to +1.0 s. The criterion says all time bins of the region, and the paper's spectrogram range may be wider. With about 60% of bins significant in the named regions, this does not change any outcome.
8. [affects a conclusion; this is a claims-file issue, not the notebook's] fig2-reach-shape: the criterion's Scott KDE is evaluated on the folded −90 to 90 range with no boundary correction. That pulls peaks of mass sitting at ±90 inward, so the "within 15° of ±90" test can fail by construction. This failure decides the partial outcome.
9. [does not affect a conclusion; claims-file gap] fig2-event-counts: the Methods keep only events lasting 0.5–4 s. The dataset's durations go down to 0.233 s (cell 4), but this filter is not one of the criterion's readings. It would lower counts but is unlikely to bring S09 (211) down to 151.
10. [does not affect a conclusion] cohort: depth electrodes are identified from group descriptions. The paper's 5 depth subjects with 1.0 ± 1.4 bad depth electrodes each cannot be matched to the dataset's 7. The notebook comments a "grid only as surface" variant but does not run it.

### C. What I could not check

- How many events have the 86400 s timestamp mismatch, and whether they are kept in reading b. A per-file count of `|event_times − start_time| > 1` would settle problem 2.
- Region-level results (cells 45–55) recomputed with electrodes good in every file, for fig5-recording-day-effects, table1 and extfig5-1 (problem 1).
- Whether the all-zero projection rows of S03 and S12 line up with the electrodes that have no position (problem 6).
- How many kept events have −inf or zero samples on individual good electrodes in the segment (problem 3).
- Event counts per subject after a 0.5–4 s duration filter (problem 9).
- Delta R² and coefficient rankings under the other seeds and with bad electrodes included (problem 4).
- The KDE plots in cell 26 exist only as images. A printed table of density at ±90, ±75 and 0 per subject would show how close the angle part comes to passing.
