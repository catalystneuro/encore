**Round 2 verification: Funamizu, Kuhn & Doya (2016) on DANDI:001605 (attempt 001605-funamizu-2016-01)**

**1. Outcomes**

The claims file has 40 claims, and the attempt record has 40 outcomes: 11 reproduced, 2 partially_reproduced, 9 not_reproduced and 18 blocked. No outcome now carries `assumed: true`. The four assumptions I objected to in round 1 (B1: O1 a, trace a, chance a, 4.2-cm bins) are withdrawn, and the claims that depended on them are blocked as methods_underspecified, as the claims file's header directs.

I agree with 38 of the 40 outcomes, including:
- **The 2 partially_reproduced:** supp6 and fig4e.
- **The 9 not_reproduced:** behaviour-timing, lick-goal-correlation, neuron-classes, fig2d-task-relevant-proportions, supp9, fig5a-map-decreases-without-sound, fig5-layer3-steeper-than-layer2, supp13 and lognormal-decoder-better.
- **The 16 blocks for data_missing or methods_underspecified.**

Each matches the printed outputs and the claims-file criterion.

The 2 others are fig3b-distance-over-time and svm-correlations, both blocked as too_large. I agree that neither was run. The record cites a protocol rule (estimated compute over the notebook limit) that I cannot see. Two problems remain:
- The estimates quoted in the text are not the ones the notebook printed (see 2).
- For svm-correlations, the printed estimate is 1.3 h for reading (a), on one thread. The notebook already runs 4 worker processes, which would bring this to about 20 min, under the 60-minute limit. Reading (b) has no estimate. So for svm-correlations the too_large block is not shown. For fig3b it holds even in parallel: 27.6 h ÷ 4 is about 7 h.

Places where the claims file may misread the paper (reported, not corrected):
- **supp1, O9 zone reading (a):** the notebook quotes Supp. Fig. 1 panel titles that name only zone (b). These titles are drawn in the figure image, not in the paper text, and I still could not render the PDF to check them.
- **fig4-above-chance, chance reading (b):** a decoder trained on distance traces permuted across trials still decodes distance, because every trace still falls toward the goal. It is not a chance level.
- **supp9, group reading (b):** in cell 60, the group sizes under reading (a) match Supp. Fig. 9a much more closely (summed share difference 0.63, against 3.09 for (b)). The paper's groups therefore look like equal quarters. The outcome is unaffected, since reading (a) is the one that fails.

**2. Sentences the printed numbers do not support**

- **Cell 119, the fig3b and svm conclusion:** "one three-basis fit on 19,586 frames took 0.66 s … about 36.6 h per reading of O6, 146 h for the four … one linear SVM took 0.23 s … about 1.2 h". Cell 118 printed 0.50 s, 27.6 h, 110.4 h, 0.24 s and 1.3 h.
  - The same wrong numbers appear in cell 0 ("about 37 h per reading", "about 1.2 h"), in the record's fig3b and svm notes, and in the record's responses to round 1.
- **Cell 74, fig4d:** "8 to 11 of 16 bins differ overall." Cell 73 prints 9 to 11. The record's fig4d note repeats "8 to 11".
- **The record's sound-responsive-layer3 note and its metadata_error finding:** "sound_on_off and speaker_on_matrix are on in exactly 150 frames". The notebook never reads `speaker_on_matrix` (funamizu.py reads only `Sound/sound_on_off`). Only the `sound_on_off` half is printed (cell 6).
- **Cell 109:** it says the width is profiled over a grid "in place of an optimizer" and does not mention the bounded refinement. Cell 116, the record and `fit_single` all say the widths are refined. This contradicts the code, but not any number.
- **The record's fig1d note:** "The paper's data page … was fetched (HTTP 200); its text names no file". No notebook output shows this, so I cannot verify it.

Every other sentence I checked matches the printed outputs: all the "**Result:**" cells, the Summary, the README, and the other record notes.

The record states my round-1 reasons in my words, condensed, with the B-point cross-references merged in. I found no misstatement.

**3. Round-1 points**

Resolved:
- **B1:** the assumptions are withdrawn and the claims blocked.
- **B4:** NaN trials are dropped; layers 3 and 5 now print 83% and 94%.
- **B5:** a k-means-per-session variant is shown. It changes no outcome.
- **B6:** widths are now refined with a bounded optimizer. tuning-similar-ppc-pm is still blocked: under O1 a with frames O6 b, width P is 0.083 to 0.21.
- **B7:** the `speaker_presentations` structure and the frame sums are printed for all 94 files.
- **B9:** supp11 zone reading (a) now drops the always-sound frames. PPC still passes 3 of 3.
- **B12:** no change was needed.

Partly resolved:
- **B11 (lick onset):** the form of the lick frequency is now printed, and the 'change' onset is justified. lick-goal-correlation is still a near-miss under an approximation the data force: r is 0.218 and 0.227 against the 0.232 bound.

Still bearing on a conclusion:
- **B8:** fig3b and svm-correlations are blocked as too_large. The svm estimate ignores the 4 workers and is not shown to exceed the limit. The quoted timings do not match the printed ones.
- **B2:** whether supp1 would be reproduced turns on the Supp. Fig. 1 panel titles. I cannot verify them, and the question is with a reader.
- **B3:** fig4-above-chance would be reproduced under the flat-prior chance (reading a) alone. The question is with a reader.
- **B10 (residual):** fig5a-map-decreases-without-sound and fig5-layer3-steeper-than-layer2 both turn on the MAP being held at 0 cm, the lower end of the decoded range. This happens in 51.6% of frames and in 18 to 29% of trials, in intermittent 1 at 8.4 to 0 cm. The 0.84-cm grid is ruled out as the cause. But the 67 to 0 cm range is the claims file's O8, and a decoder whose range extends past the goal was not tried. The failure may come from that choice rather than from the data.
