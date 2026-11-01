**Verifier report, round 2: Semenov et al. 2025 on DANDI:001271 (0.250805.1352)**

This round I had the right claims file (`claims/001271`). It has 20 claims, and the attempt record has 20 outcomes: 3 reproduced, 2 partially_reproduced, 4 not_reproduced and 11 blocked. Two of the outcomes are `assumed: true`. The notebooks now print each criterion next to its test.

## 1. Outcomes

**I agree with 18 of the 20.**
- **figs2-neurons-tested** (reproduced): 6 TTX neurons and 11 vehicle neurons.
- **figs2-depolarization-reversible** (blocked: other): no session meets the claims file's sustained-depolarization rule (O4).
- **figs2-ttx-abolishes-aps** (blocked: methods_underspecified): this follows the header's rule. O1(a) gives a different outcome over every common field than at the highest one (cell 43), and O1(b) is split between its two AP heights.
- **figs2-ttx-blocks-sustained-depolarization** (blocked: other): the criterion's own blocking clause applies.
- **figs2-vehicle-keeps-response** (blocked: methods_underspecified): the readings disagree (cell 58).
- **ap-amplitude-duration** (blocked: methods_underspecified): 1 of 32 readings falls within the paper's values.
- **fig3-not-heating** (blocked: methods_underspecified): the criterion's ratio clause applies.
- **fig1-pure-sine-excites-all, fig1-20khz-needs-twice-the-field, fig2d-modulated-thresholds-higher** (not reproduced): every reading fails.
- **fig2-modulated-locks-to-beats** and **fig2c-pure-more-aps** (reproduced, assumed).
- **fig3b-low-conductivity-halves-threshold** (blocked: metadata_insufficient).
- **figs1-di8-same-as-fluovolt** (not reproduced). One caveat: this rests only on the deposit holding 3 neurons. The comparison of effects found no difference (p = 0.72–0.93), and the three pattern claims were not run, so "not reproduced" does not mean the effects differ.
- **fig4-pooled-time-constants, fig4-orientation-and-poles, fig6-sine-less-than-pulse, threshold-depolarization-estimate** (blocked: other, not attempted).

**I disagree with two.**
- **figs2-before-firing-then-depolarization**, recorded as partially_reproduced. Every one of the 24 claims-file readings returns "not reproduced" (cell 26), and the criterion has no partial outcome. The "firing part" the record says holds also depends on the reading:
  - with O1(a) and the 5‑SD height, only 18 or 19 of 20 neurons have APs;
  - with O1(b) and the 5‑SD height, only 1 of 7 does.

  The outcome should be not_reproduced, with the note that the claims file's measure cannot detect plateaus of this size.
- **fig3c-sustained-firing-2s** (nb3), recorded as partially_reproduced. The notebook's own tally is "not reproduced" in 48 of 48 readings (cell 11). The first two parts hold only with the O1(a) ROI: with O1(b) and the 5‑SD height no cell meets the first part. The third part fails everywhere. The same correction applies.

**Assumptions.** Both `assumed: true` outcomes state their assumption, and both are reasonable:
- **fig2c-pure-more-aps** reads "the threshold" as the 1‑AP threshold, with support from the Methods.
- **fig2-modulated-locks-to-beats** lets the 5‑SD height decide. The 9_2 session's pre-onset SD is 9.8%, and none of its peaks reaches its own 5‑SD level (cell 25).

Three further assumptions are not marked, but none of them changes an outcome:
- the change point of each vehicle neuron (that claim is blocked anyway);
- extending O3's before-change level to O4 (no pair qualifies);
- the scale of 18 V/cm per V (fig2d fails at both 18 and 36).

## 2. Sentences the printed numbers do not support

- **Firing in figs2-before-firing-then-depolarization.** The attempt record says "Firing holds … under every combination of the claims file's readings (O1 to O4)", and main notebook cell 33 says "So the firing part holds". Cell 26 contradicts this for the 5‑SD height: 18 or 19 of 20 neurons under O1(a), 1 of 7 under O1(b).
- **Main notebook Summary (cell 73).** It says the empty O1(b) masks drive "most of the disagreements between readings". In all three methods_underspecified claims on 001271, O1(a) disagrees with itself: O5(a) against O5(b) in cells 43 and 58, and 1 within against 7 outside in cell 67.
- **ap-amplitude-duration (cell 68 and the record).** They say "with the O1(b) ROI … peaks are 16.3 to 18.9%". Cell 67 has 15.79% (O1(b), last 20 ms, 5‑SD height).
- **fig2d-modulated-thresholds-higher (nb2 cell 22 and the record).** They say modulated thresholds are "higher on average in every comparison that can be made" (record: "wherever they can be compared"). Cell 21 shows the reverse for O1(b) with the 5‑SD height at 20 kHz and 1 AP: 12.00 V unmodulated against 11.00 V modulated, and 11.93 against 11.00.
- **fig2-modulated-locks-to-beats (nb2 cell 28 and the record).**
  - "92% of 212 APs": cell 25 prints 213 APs and a share of 0.91.
  - "14 of 14" sessions with 5 APs or more (record: "all 14 sessions"): cell 25 has 15 of 15.
  - "Eight clear APs of about 13%" in the unmodulated session is shown only in a figure. No printed output supports it.
- **fig2c-pure-more-aps (nb2 cell 32 and the record).** They give "p = 2.3e-10 to 7.8e-07". Cell 31 prints 4.7e-10 to 7.8e-07.
- **fig1-20khz-needs-twice-the-field (nb2 cell 18 and the record).** They say "1 to 3 neurons" have modulated 20‑kHz thresholds. Cell 17 has rows with 0.
- **fig3c-sustained-firing-2s (nb3 cell 15).** It says "with the 5-SD height 1 to 3 cells meet each part". With the smoothed bleaching reference, 4 cells meet the "rises" part (cell 11).
- **The record's verification block** says ten of my round‑1 ids are also in the 001271 file. Eleven are: fig1 ×2, fig2d, fig2-modulated, fig2c, fig3b, fig3c, fig4 ×2, fig6 and threshold-depolarization-estimate.

Everything else checks against the outputs: the remaining Result sentences in all three notebooks, both other Summary sections, the README, and the record's notes and findings. That includes 6/11/3 neurons, 210 of 287 empty masks, the medians 2.63/7.29/4.93%, 1.15–6.01 points, 246 of 262, the p values 9.5e‑7, 1.6e‑7 and 0.00054, 334/327 APs, 8 of 11 neurons, the heating numbers, the 18 V/cm match, and 74.1 V/cm.

**My round‑1 reasons in the record** are faithful paraphrases, and the claims-file mix-up is explained. Two entries record "agrees: true" with an outcome I did not give for that id: figs1-di8-same-as-fluovolt and figs2-ttx-blocks-sustained-depolarization. Both are fair inferences from what I wrote.

**Where the claims file departs from the paper.** O4 requires no AP in the last 100 ms. The paper describes APs that "coalesced into low-amplitude oscillations on top of a continuous depolarization". A detector at 5% counts those oscillations as APs (9 of 20 neurons at their highest field, cell 28). So O4 rules out by construction the state the paper describes. Together with its levels (5 SD, or half the AP height, against plateaus of 2–5%), this decides four outcomes: figs2-depolarization-reversible, figs2-ttx-blocks-sustained-depolarization, figs2-before-firing-then-depolarization and fig3c-sustained-firing-2s.

## 3. Round‑1 points

**Resolved**
- **B1:** the right claims file is used, and its criteria are printed.
- **B2:** the level after TTX is the claims file's O3. The plot and the count at the session's own 5‑SD level show the single AP after TTX is noise.
- **B3 (wording):** the notebook and the record now say the measure cannot detect the plateaus.
- **B5:** the smoothed bleaching reference corrects c7; its last-250-ms mean of 7.0% is still below every O4 level.
- **B6:** the sensitivity to 13_20240801's change point is shown.
- **B7:** the field scale is now a finding, and both scales fail fig2d.
- **B9:** the gap to the next lower voltage is reported.
- **All four items of section C:** the Figure S2 traces, the 9_2 and TTX plots, the per-neuron depolarization table and the per-neuron vehicle table were added.

**Remaining, bearing on a conclusion**
- **The outcome labels from B3.** figs2-before-firing-then-depolarization and fig3c-sustained-firing-2s are marked partial where their criteria give not_reproduced (section 1).
- **B4, now a claims-file issue.** The O1 readings do not suit 16×16 crops. O1(b) is empty in 210 of 287 sessions, and O1(a) can be a single pixel: the one AP after TTX comes from a one-pixel ROI with an SD of 11.8%. These readings decide the three methods_underspecified outcomes on 001271. The attempt is right to run them as written; the claims file should revise them.
- **The O4 issue above,** which the claims file should revise.

**Remaining, not bearing on a conclusion**
- **B8:** in 001032, 13_1's 20‑kHz sessions show 14_1's cell (correlation 0.997), but they are still counted as a separate neuron in the threshold tests.
- **B10:** the stimulus timing is confirmed from the images in only 4 of 282 sessions.
