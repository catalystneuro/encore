**Round-2 verifier report: Semenov et al. 2025 (DANDI:001274 and related dandisets)**

Counts come from the files. The claims file has 26 claims and the attempt record has 26 outcomes, with the same IDs. Of these, 14 are blocked, 10 not_reproduced, 1 partially_reproduced and 1 reproduced. Only one outcome is marked `assumed: true`: fig1-max-rate-ceiling. I found no place where the claims file misreads the paper.

## 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| fig1-pure-sine-excites-all | not_reproduced | Yes, by the criterion. It is marginal: the 20-kHz count is 15/17 under all four readings (cell 23). In cell 24, sub-10-4 at 324 V/cm shows about 8 regularly spaced events of about 3% on a falling trace, which look like small APs. Counting them would give 16/17 (94%) and a pass. The record states this. |
| fig1-onset-delay | not_reproduced | Yes. The median is 64 ms under reading a and 67 ms under reading b; the bracketed-threshold variant also gives 67 ms (cell 27). |
| fig1-max-rate-ceiling | not_reproduced, assumed | Yes. The assumption is stated and reasonable. The claims file's literal reading (a) counts about 18 noise "APs" per 250 ms on a plateau (cell 18). The unchanged reading (b) gives 42.9 Hz, also outside 54–99 Hz. The revised (a) does miss low-amplitude oscillations (cell 37: sub-12-1 a1 vs b23, sub-8-2 a2 vs b21). Reading (b) covers those cases, and its median is still out of range. |
| fig1-excitation-block | not_reproduced | Yes: 3 of 42 under every reading (cell 36). |
| fig2d-20khz-twofold-threshold | not_reproduced | Yes. The calibration sentence is wrong (section 2), and correcting it makes the outcome stronger. |
| fig2d-modulated-thresholds-higher | partially_reproduced | Yes: 2 of 3 pairs reach p < 0.05 under both readings (cell 43). |
| threshold-2khz-unmodulated | not_reproduced | Yes, as pooled: 75.6 / 74.8 V/cm, and 151 under the full-voltage reading (cell 46). The result depends on pooling the three dandisets (section 3). |
| fig2-modulated-locks-to-beats | not_reproduced | Yes. Part (iii) fails on 001032/sub-2-1 at 198 V/cm, which ends at 5.9% against −0.2% at its near-threshold session; the plateau is visible in cell 51. |
| fig2c-pure-more-aps | reproduced | Yes (cell 54). |
| fig3c-sustained-firing-2s | not_reproduced | **No, I now disagree; this reverses my round-1 view.** Parts (i) and (ii) hold for c7. Part (iii) fails only on 5 events under (a) and 1 under (b) on the 6.7% plateau over 0.25–2 s (cells 57–58). The notebook's own test (cell 18) gives 1.2 (a) and 0.8 (b) false APs per 250 ms on a 6% plateau at 0.83% noise. That predicts about 8 and 6 such events over 1.75 s, and more on a bleaching-corrected (differenced, so noisier) trace. In cell 58 the events are isolated and irregular. I would score c7 reproduced. At the least, the outcome should be marked `assumed: true`, since it rests on treating noise-level detections as APs. |
| figs1-di8-anepps-control | not_reproduced | Yes: block is 0/3 under every reading (cell 61). blocked (data_missing) would also be defensible, as the record says. |
| figs2-ttx-blocks-depolarization | not_reproduced | Yes: before tetrodotoxin, last-100-ms dF is above 5% in only 1 of 6 neurons (cell 64). |
| fig3b and the 12 strobe claims (Figures 4, 5, 6, S3) plus threshold-depolarization-estimate (14 blocked in all) | blocked | Yes. |

## 2. Sentences the numbers do not support

- **fig2d calibration.** The record (fig2d-20khz notes and response), cell 41 and cell 47 all say: "the 20-kHz factor would have to be 0.64 to 0.97 times the 2-kHz one for the ratios to fall within tolerance". No single factor puts all four ratios in 1.8–2.2:
  - under reading (a) it would need to be at least 1.8/2.27 = 0.79 and at most 2.2/2.82 = 0.78;
  - under reading (b) the bounds are 0.79 and 0.78 again.
  The ratios differ among themselves by a factor of 2.82/2.27 = 1.24, more than the 2.2/1.8 = 1.22 the tolerance band allows. So calibration cannot rescue this claim, and the record should say so.
- **Cell 30 and the fig1-onset-delay notes:** "the other five, at 10 to 16 ms, are isolated APs". In cell 29, sub-11-1, sub-14-1 and sub-10-1 each show the first of 4 regular APs, not isolated APs. Their lowest tested field was already above threshold.
- **Cell 25 and the fig1-pure notes:** "Neither neuron is dimmer than the others (bright half over dim half 1.68 and 1.52, median 1.47)". That ratio measures contrast, not brightness.
- **Cell 52:** "0.04 do in every modulated session when the beats are shifted". The 0.04 is pooled over all modulated sessions (cell 20), not true of every session.
- **fig2-modulated notes and cell 52:** "under the first version of reading a, 12". This number does not appear in this notebook's outputs; it is a round-1 figure.
- **README:** "ROIs rebuilt from the paper's RATIO image". They are rebuilt from a RATIO image the notebook computes by the Methods' recipe, not from the paper's own image.
- **Finding on frame counts:** "2 have 1,400 and 1,800" should read one each (cell 14).

Everything else I checked against the outputs is supported. That covers the remaining Result cells, the Summary (cell 73), the README table and the record's notes and findings.

The record states my round-1 reasons faithfully. The reasons for the four Figure 5 / S3 claims are expanded from "Same as above" but are accurate.

## 3. Round-1 points

**Resolved:**
- Problems 1 (reading (a) counts plateau noise), 3 (summary scoring), 4 (full block test in part iii), 5 (001034 duplicate), 6 (TTX disclosure), 7 (strobe variants), 8 (redundant variant) and 10 (bleaching note).
- Problem 2 (calibration) is addressed, but the fig2d estimate is wrong, as shown in section 2.
- Problem 9 (c7's trace used as the bleaching reference for the other neurons) is unchanged; it does not bear on a conclusion.
- All six "could not check" items now have outputs: AP overlays, short-latency traces, the field cross-check, the traces of the two neurons never excited at 20 kHz, the gluconate series check, and the strobe frame timing.

**What still bears on a conclusion:**
1. **fig3c (iii):** the failure rests on detections at the detectors' own false-positive rate (section 1).
2. **fig2d calibration:** the statement must be corrected. The corrected version strengthens not_reproduced.
3. **Pooling across dandisets:**
   - 001035 alone gives a 2-kHz threshold of 58.3 V/cm, inside 57.7 ± 3.6 (cell 46), and a near-threshold latency median of 101 ms, inside 90–220 ms (cell 27).
   - So the outcomes of threshold-2khz-unmodulated and fig1-onset-delay depend on pooling 001032, 001033 and 001035. That pooling follows the claims file's "where".
   - 001035 has no modulated sessions (cell 14), so Figure 2D cannot come from 001035 alone. Which neurons the paper used therefore cannot be settled.
   - The fig1-onset-delay notes should say the outcome depends on pooling.
4. **fig1-pure-sine-excites-all:** the outcome turns on one neuron, sub-10-4, whose events at 324 V/cm look like attenuated APs (cell 24). It is disclosed, and the outcome is correct under the criterion.
