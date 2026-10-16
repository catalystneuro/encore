The notebook's own results support 16 of the 22 claims. Four are partially reproduced, one is not reproduced (angle-bimodal), and one is blocked because the data are missing (demographics). I took the count of 22 claims from the claims file. The outcomes below are mine, from the notebook outputs and each claim's criterion. I saved the paper's full text (PMC8225404) under `paper/`. I did not re-run the notebook or download the dandiset.

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| subjects-days-hemispheres | reproduced | Cell 23: 12 subjects with 3 to 5 days each, all within days 3 to 7. 5 right and 7 left hemisphere, and the event wrist is contralateral in every subject. |
| demographics | blocked (data_missing) | The NWB subject group holds only `species` and `subject_id` (cell 3). I checked the archive myself: each subject's asset `wasAttributedTo` has only identifier and species, and the version metadata never mentions sex or age. No part can be tested. |
| electrode-counts | partially_reproduced | Cell 26: surface 84.8 (paper 87.0 ± 8.7) and depth mean 23.7 (paper 23.2 ± 2.32) are within tolerance under both readings. The number of subjects with depth electrodes is 7 under (a) and 6 under (b), against 5 in the paper. |
| bad-electrodes | partially_reproduced | Cell 28, reading (a): surface 4.83 is within 4.9 ± 0.49, but depth is 4.29 against 1.0 ± 0.1. Readings (b) and (c) fail on both values. |
| event-counts | partially_reproduced | Cell 30, reading (a): min 211, max 996, median 770.5; only the max is within tolerance (852 to 1042). Reading (b) is similar (208, 986, 748). |
| features-differ-subjects | reproduced | Cell 32: Kruskal-Wallis p < 0.001 for all 10 features. |
| days-one-dominant | reproduced | Cell 34: reading (a) fails, because subject 04's largest day is only 0.381 of its events. Reading (b) holds: 04, 05 and 09 are the three largest one-day shares. |
| duration-magnitude-small | reproduced | Cell 36: 91.7% of events last under 2 s and 91.5% cover under 200 px; both hold in 12 of 12 subjects. |
| angle-bimodal | not_reproduced | Cell 38: the two most populated bins are 10 and 11, both at the upward end. Bin 0 (downward) has 514 events, fewer than bins 8 to 10, so the pooled part fails. The per-subject part holds (11 of 12), but the criterion gives no partial credit for that case. The distribution is skewed upward, not bimodal. |
| feature-correlations | partially_reproduced | Cell 40: 5 of 6 correlations are within tolerance and all are positive. Magnitude against duration is r = 0.231, just below the lower bound of 0.234. |
| bimanual-skew | reproduced | Cell 42: median ratio 0.137 (below 0.5), median overlap 0.467 s (below half the median duration, 0.55 s), 72.6% of events bimanual. The four highest median ratios are 04, 07, 05 and 02, which include 02, 04 and 05. |
| projection-link | reproduced | Cell 44: the density threshold gives the paper's 8 regions. In 12 of 12 subjects the extra matrix rows are all zero, and the closeness score (0.917 to 0.967) is far above the shuffled maximum (at most 0.143). |
| group-pattern-rois | reproduced | Cell 46: LFB is below 0 and HFB above 0 in precentral, postcentral and inferior parietal. Their absolute sums (1.04 to 1.39) are all larger than the largest temporal one (0.34). This rests on 15 to 25 events per subject. |
| precentral-subject-ci | reproduced | Cell 49: 22 of 24 means and 20 of 24 medians fall inside Table 1's intervals; the threshold is 20. |
| precentral-subjects-differ | reproduced | Cell 52: Kruskal-Wallis H = 802 (LFB) and 1244 (HFB), p underflows to 0. |
| precentral-day-effects | reproduced | Cell 54: 23 of 24 calls agree with the paper. The one disagreement is S05 LFB, p = 0.054 here against 0.013 in the paper. |
| baseline-reduces-day-variability | reproduced | Cell 56: the day-to-day SD is lower with baseline subtraction in 9 of 12 subjects for LFB (exactly the threshold; 03, 06 and 11 go the other way) and 12 of 12 for HFB. It stays above 0 everywhere. |
| regression-r2-max | reproduced | Cell 60: the largest mean test R2 is 0.141, under the 0.275 limit; the stored maximum is 0.255. No recomputed model comes near the paper's 0.25, so the bound passes easily but is not closely matched. |
| regression-r2-sensorimotor | reproduced | Cell 62: the top region is precentral for LFB and postcentral for HFB. The frontoparietal mean is above the temporal mean in both bands (-0.006 against -0.018, and -0.008 against -0.017), though all values are near or below 0. |
| regression-angle-day-top | reproduced | Cell 64: 12 electrodes pass R2 > 0.05, all from subjects 01, 03 and 11. Angle (0.0645) and day (0.028) have the largest Delta R2 in LFB, and the same holds in every variant. |
| regression-angle-coefficient | reproduced | Cell 66: the mean angle coefficient is -1.07 for LFB (12 of 12 negative) and +0.21 for HFB. Cell 9 confirms that after negation, positive angles are upward reaches. |
| regression-angle-retained | reproduced | Cell 68: angle is retained in 0.641 of models, the highest; the next is onset speed at 0.386. |

**B. Problems**

1. [does not affect a conclusion] `ajile.chunk_index` and `fetch_windows`: the docstring says "The notebook checks it against h5py on sample chunks", but no cell does this. The reader also assumes float32 little-endian samples and gzip as the only filter, and neither is ever checked. The movement-locked responses (cell 20) and the Table 1 matches support the reader indirectly.
2. [does not affect a conclusion] `ajile.regression_model` and `ajile.design`: forward selection and standardisation run once on all events, test events included. This leaks test data into the models. It follows the paper's code, but the Methods describe a 90/10 split before pruning. The leak inflates test R2 and could bias Delta R2 and the retained fractions. The R2 bound still passes with margin.
3. [does not affect a conclusion] Cell 58: regression electrodes are drawn only from set P, so subject 02 has 5 and subject 06 has 7, not the eight the criterion asks for.
4. [does not affect a conclusion, but close] Cell 50: without the three late-starting files, only 19 of 24 medians fall inside Table 1's intervals, which would be partial under the median reading. The mean reading was not shown for this variant.
5. [does not affect a conclusion] Cell 20: the clock check fails to separate true from shifted event times for subjects 01 and 02, and is ambiguous for 04 day 3. Some shifted-window medians reach ±1.4 dB, so this check has little power at 15 to 25 events.
6. [does not affect a conclusion] Cells 46 and 47: the eight-region claim uses 5 events per file, and the notebook gives no uncertainty for it. The margin is large (1.04 against 0.34).
7. [does not affect a conclusion] `bad-electrodes`, reading (a): the `good` flag also marks unlocalised electrodes as bad (all 16 depth electrodes of subject 03, and 8 in subject 12). So the flag does not measure only the paper's SD and kurtosis rejection. Without subject 03, depth is 2.33, still outside tolerance.
8. [does not affect a conclusion] `reach_features`: time of day is assumed to start at each file's local midnight, contrary to the stated `session_start_time`. This rests only on the sleep-label histogram (cell 11). In the dandiset, 328 durations are below 0.5 s, so its events are not exactly the paper's selection.
9. [does not affect a conclusion] `design`: the time-of-day bins include both ends, so an event at exactly 8 or 16 h gets two one-hot columns. This copies the paper's code and affects almost no events.

Synthetic tests of `fold_angle`, `covering`, `log_power`, `subtract_baseline`, `band_values`, `day_balanced_split`, `forward_select` and `design` all behaved as documented. For example, an amplitude step of 3x at 21 Hz gave LFB +9.54 dB, HFB 0, and the peak at the right frequency. No claim states a chance level, so there was none to compare.

**C. What I could not check**

- Whether the custom ECoG reader returns the same samples as h5py. An output comparing `fetch_windows` with h5py slices on a few chunks and channels, plus the dataset's dtype and filter pipeline, would settle it.
- The paper's own statistic for regression-r2-sensorimotor, which is about where the largest-R2 models are, not regional means. A list of the top-N stored R2 electrodes per band with their dominant region would test that directly.
- Whether the angle skew comes from the dandiset's events or from the folding. A per-subject histogram of the stored, unfolded angle would show which.
- How much the regression results depend on the leakage in problem 2. A variant with forward selection inside each training split would show it.
- How firm the 9 of 12 LFB count is in baseline-reduces-day-variability. Per-subject bootstrap intervals on the two day-to-day SDs would show that.
