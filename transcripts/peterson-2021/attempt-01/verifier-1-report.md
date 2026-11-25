**A. Outcomes** (all 25 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| subject-days | reproduced | All 12 subjects have exactly the Table 2 days, 55 subject-days (cell 23). |
| roi-projection-link | reproduced | Rows match electrodes for 12 of 12 subjects. The top weight is at the nearest centroid for 0.59 to 0.79 of electrodes, against about 0.2 when the order is shuffled (12 of 12). The eight regions with density > 3 are the ones the claims file names (cell 25). |
| cohort | partially_reproduced | 12 subjects, surface mean 84.8 (87.0 ± 12.9), depth mean 23.7 (23.2 ± 12.1) and 5 right hemisphere all pass. Subjects with depth electrodes is 7 against an exact 5, so that part fails. Sex and age are not in the files or the archive metadata (I checked the asset metadata), so they are not testable (cell 27). |
| fig2-event-counts | not_reproduced | Reading a gives fewest 211, most 996, median 770.5. Reading b gives 211, 979, 739. The fewest and the median are outside tolerance under both readings (cell 29). Reading b could not drop the false positives (see B3). |
| fig2-features-differ-across-subjects | reproduced | All ten Kruskal-Wallis p < 0.001 under both readings; the largest is 1e-34 (cell 31). |
| fig2-reach-shape | partially_reproduced | The duration and magnitude part holds pooled and in 12 of 12 subjects. The angle part holds in 0 of 12 subjects and not pooled: peaks are near ±70° (cell 33). See B2: the criterion's angle test is biased against this claim. |
| fig2-bimanual-skew | reproduced | The ratio, overlap and class parts hold pooled and in 12 of 12 subjects. S02, S04 and S05 are among both "five" sets, under both readings (cell 36). |
| extfig2-1c-contralateral-larger | reproduced | The contralateral peak exceeds the ipsilateral peak in 12 of 12 subjects under both readings. The smallest ratio is 1.08 (S05) (cell 38). |
| extfig2-2-feature-correlations | partially_reproduced | 5 of 6 correlations are within tolerance. Magnitude vs duration is r = 0.233 against 0.26 ± 0.026, under both readings (cell 40). |
| fig2-days-and-waking | partially_reproduced | The busiest day holds more than half of the events for S05 (0.605) and S09 (0.517) but not S04 (0.379), and for no unnamed subject. The waking part holds in 12 of 12 subjects. Only one of the two parts holds (cell 42). |
| fig3-group-lfb-decrease-hfb-increase | reproduced | Masked 4-30 Hz power is below 0 and 50-120 Hz power above 0 in precentral, postcentral and inferior parietal under both readings (cell 44). |
| fig3-sensorimotor-largest | reproduced | Under readings a, b and c the named three are the top three, and every temporal region is below them (cell 47). |
| fig3-lfb-more-widespread | blocked (methods_underspecified) | Reading a gives 7 regions against 7, so low frequency is not larger. Reading b gives 35.2 against 25.9 bins per frequency, so it is. Supramarginal and superior temporal do have low-frequency decreases (cell 49). The disagreement rests on a few marginal bins from one bootstrap seed (B4). |
| fig4-precentral-subject-variability | reproduced | Parts 1 to 3 hold. Part 4 holds only after a tie-break: four subjects tie at 3 bins, ranked alphabetically. The author's interpolated-width tie-break also puts S04 and S08 in the narrowest three (cell 51; B5). |
| fig5-band-power-differs-across-subjects | reproduced | p = 1.3e-163 (LFB) and 7.1e-264 (HFB) with the band mean; the median variant agrees (cell 53). |
| table1-subject-band-power-ci | partially_reproduced | The best reading (mean of the band mean) puts 23 of 24 values inside the paper's intervals. S06 HFB is 1.78 against 2.02 to 2.37, and the attempt's own bootstrap interval (1.64 to 1.92) does not overlap the paper's. Other readings give 21, 21 and 20 (cell 55). |
| fig5-recording-day-effects | reproduced | With the band mean, all 24 subject and band pairs agree with the paper. The median variant gives 23, missing LFB S05 (cell 57). |
| extfig5-1-baseline-reduces-day-variability | reproduced | The SD is lower with the baseline subtracted in 9/12 (LFB) and 12/12 (HFB) subjects, and for 92% and 90% of good electrodes. 11 day effects remain (cell 59). |
| discussion-day-changes-small | reproduced | The largest day change is 1.01 dB (limit 2.2). Levels without baseline are 12.4 to 36.3 dB in microvolts, inside 9 to 55 (cell 61). |
| fig6b-best-models-sensorimotor | blocked (other: not run) | The notebook says "too large", but its own estimate is 3.1 h on one core and 0.8 h on 4 cores (cell 63). All inputs are in the dataset and already computed in the notebook. |
| fig6-r2-at-most-025 | blocked (other: not run) | Same as above. The dataset's electrode tables hold the paper's own R2 (max 0.149 LFB, 0.255 HFB). That fits the claim, but it is the paper's output, not a reproduction. |
| fig6c-angle-and-day-most-informative | blocked (other: not run) | Same as fig6b. |
| extfig6-2-angle-most-retained | blocked (other: not run) | Same as fig6b. |
| fig6d-upward-reaches-enhance-pattern | blocked (other: not run) | Same as fig6b. |
| fig6d-angle-and-day-largest-coefficients | blocked (other: not run) | Same as fig6b. |

**B. Problems**

1. [affects a conclusion] Cells 62–63: the six regression claims are blocked as `too_large` without good reason. The notebook's own timing gives 3.1 h on one core and 0.8 h on 4 cores for the main analysis, and roughly 4× that with the three variants. That is the same order as the 24 min ECoG step it already ran. The per-event electrode band power (`el`), the features and the good flags all exist in the notebook. None of the six claims was tested.
2. [affects a conclusion; this is in the criterion, reported and not corrected] fig2-reach-shape, cell 33 `bimodal`. The criterion requires KDE peaks within 15° of ±90. A Gaussian KDE without boundary correction cannot place peaks there for data bounded at ±90. On synthetic folded angles whose true density peaks at exactly ±90, Scott's bandwidth puts the KDE peaks at ±72 to ±74° (n = 250 and 900). The observed peaks near ±70° fit that artifact, so the angle part's failure, and with it the partial outcome, does not count as evidence against the paper.
3. [affects a conclusion] Cells 18 and 29: reading b cannot drop false positives because the files do not mark them. The files hold 8088 events. The data descriptor (paper/10.1038-s41597-022-01280-y.txt) says 6931 verified events and 17.8 ± 9.9% removed as false positives or occlusions. That gap could account for the count mismatch (a median of 739 at about 14% removal is about 635), so fig2-event-counts is not_reproduced only under reading a in full. Every other "reading b" analysis also includes these events. Where both readings were run, a and b agree.
4. [affects a conclusion] Cell 44 `boot_sig_mask`, `rng_fig3`: one bootstrap seed. Reading a of fig3-lfb-more-widespread ties at 7 against 7 because of 4 and 10 marginal positive high-frequency bins in middle and inferior temporal (unmasked means 0.011 and 0.034 dB). If either region loses them under another seed, low frequency is more widespread and the claim would be reproduced. Seed stability was not checked.
5. [does not affect a conclusion] Cell 51, part 4: `sorted(..., key=(width, s))` breaks a four-way tie (S03, S04, S05, S07 at 3 bins) by subject ID. The interpolated width in Hz is the author's own measure, not the criterion's. It also passes (S04 at 14.4 Hz is second narrowest), but S11 is 16.8 Hz against S05 at 16.9 Hz. Under a strict reading of the tie, part 4 is indeterminate and the claim would be partial (3 of 4).
6. [does not affect a conclusion] Cell 27: depth electrodes are taken as groups whose description contains "depth". The data descriptor's Table 2 gives S10 86 surface + 40 depth (notebook 78 + 48) and S11 106 surface + 0 depth (notebook 88 + 18). With the descriptor's counts the surface mean is exactly 87.0 ± 12.9 and 6 subjects have depth electrodes (23.3 ± 12.0). The "subjects with depth = 5" part fails under both, so the outcome stands. The descriptor's own table contradicts the paper's "five".
7. [does not affect a conclusion] Cell 16: bad electrodes are taken from each subject's first file, and good flags differ between files for all 12 subjects (cell 5). The helper attributes this to the code, which I could not check. The descriptor marks bad electrodes per day.
8. [does not affect a conclusion] Helper `segment_quality`: the summary of segment power for the 0 dB and 3 SD rules is an assumption, and the SD is taken per subject where the Methods say "all segments". Cell 64 shows the main ECoG results barely move without the rule (Table 1 inside: 22 against 23; the same day effects).
9. [does not affect a conclusion] Helper `ecog_offset`: the three short files are assumed to end at midnight. This is supported by `ReachEvents` matching to 0.001 s and by the neural response (cell 21; S04 day 3 is weak either way).

Other checks I ran on the helpers came out correct: `fold_angle` on synthetic angles, band and time bin indices (LFB 11–31 Hz, HFB 76–96 Hz, 6 time bins), `band_values` on a known array, `segment_power` on an 81 Hz sine (peak at 81, no edge effect), and `boot_sig_mask` (2 of 2275 bins significant under the null; all 150 bins of an injected effect detected).

**C. Not checked, and the output that would settle it**

- Whether `intervals/reaches` has any column marking false positives or verified events: print `s["reach_columns"]` for every file.
- The depth classification: print `group_desc` for every group, beside Table 2 of the data descriptor.
- Seed stability of the fig3 masks: rerun `boot_sig_mask` with about 10 seeds and report the significant-bin counts per region for claims fig3-lfb-more-widespread and fig3-group-lfb-decrease-hfb-increase.
- The regression claims: the full regression run (main analysis and variants), and at least the per-electrode R2 table.
- How much of the angle-peak result is KDE boundary bias: the same KDE with boundary reflection, as a sensitivity output alongside the criterion's version.
- Which code produced the first-file bad-electrode choice and the region weights: these rest on the paper's code, which I did not have.
