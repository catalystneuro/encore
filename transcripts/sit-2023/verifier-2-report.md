**Verifier report, round 2: Sit & Goard (2023) on DANDI:000483 (attempt 000483-sit-2023-01)**

The claims file has 24 claims and the attempt record has 24 outcomes: 2 blocked, 5 reproduced, 11 partially reproduced, 6 not reproduced. Ten of them rest on an assumption.

The main new problem is that most of the written conclusions don't match the notebooks they sit in. The printed outputs of `single_cue`, `axons`, `somata`, `directions` and `decoding` reproduce my round-1 numbers exactly: 485 selected cells, 165 passing the shuffled control, 202/67/1150 cells per class, V = 743.5 for fig5e. The "**Result:" cells, the Summaries and the attempt record instead quote another run that I haven't been given: 486, 166, 194/75/1150, V = 743.2. The record says the re-run differs only slightly, between machines. In most places that is true, and no outcome changes. In two places, though, the text states the opposite of what the notebook prints (part 2a).

**1. Outcomes**

| Claim | Outcome in the record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| fig1-free-heading-fraction | blocked (data_missing) | Yes | n/a |
| fig1g-rotation-heading-fraction | reproduced | Yes: the printed 485 / 15.26% is within tolerance | Centred fit: yes |
| selection-shuffled-control | not_reproduced | Yes: the printed 5.19% is above the 1% limit | Trials shifted once before the test: yes |
| fig1h-preferred-headings-tile | partially_reproduced | Yes | Centred fit, and the cue position is unknown: yes |
| fig2f-head-chamber-same-preference | partially_reproduced | Yes, though generously: matched ROIs are no closer than random pairs in any pair (cell 9) | Mirroring the chamber-rotation heading and using 5 of 7 pairs: stated, not checked against data |
| fig3c-coherent-remapping | partially_reproduced | Yes | Centred fit: yes |
| fig4-axons-light-on-shape | reproduced | Yes (reading b) | n/a |
| fig4-axons-light-off | partially_reproduced | Yes | n/a |
| figs5-rotation-direction | reproduced | Yes, but fragile: by mouse only SKKS125 passes (p = 0.044), and the pooled random pairs cross files | n/a |
| figs6-arena-control | not_reproduced | Yes, which changes my round-1 view. Without the 6-bin pair p = 0.9, and no pair passes alone (p 0.781 to 1). The pooled pass comes from mixing files. | Leaving that pair out: yes |
| fig5-three-classes | not_reproduced | Yes. The printed variant does peak at k = 3, but the criterion only reports the variant. | n/a |
| fig5-class-proportions | not_reproduced | Yes | n/a |
| fig5e-alignment-peaks-coregistered | partially_reproduced | I now accept this instead of not_reproduced. Against the random-pairing null a small excess remains (share 0.002; 29.2% vs 26.2% within 18°). "Always" fails. | n/a |
| fig5f-heading-flip-unchanged | partially_reproduced | Yes (printed p = 0.141) | n/a |
| fig5gh-landmark-alignment-flip-drop | partially_reproduced | Yes | n/a |
| fig5i-axons-in-clusters | partially_reproduced | Yes | n/a |
| fig5k-visual-cue-only | blocked (metadata_insufficient) | Yes. No other file shares the ROI count, and the blocks differ only in direction (directions cell 12). data_missing could equally be argued. | n/a |
| fig6a-population-light-on | not_reproduced | Yes | n/a |
| fig6a-population-light-off | partially_reproduced | Yes: 0.569 is outside 0.44 ± 0.10 | Bayes decoder: stated; reasonable but weak (see part 3) |
| fig6b-heading-cells | partially_reproduced | Yes | Bayes decoder: as above |
| fig6b-landmark-cells | partially_reproduced | Yes | Bayes decoder: as above |
| fig6b-alignment-cells | not_reproduced | Yes. For dF/F the paired p is 0.011 but the unpaired p is 0.053; the "between the other classes" condition fails anyway. | n/a |
| fig6b-180-errors | reproduced | Yes, under Bayes | Bayes decoder: as above |
| fig6-heading-below-population | reproduced | Yes | n/a |

**Places where the claims file misreads its sources (reported, not corrected):**
- **Trial rule:** the opening comment paraphrases the code's rule `any(90 - abs(prctile(h,[25,75])) > 50)`, which drops segments with |p| < 40, as "more than 50 degrees from ±90". That wording would also drop |p| > 140. `rsc.py` follows the code.
- **selection-shuffled-control:** the criterion names both "before the test" and `calculateHeadDirection_shuff`, which re-shuffles in every iteration. Those are two different procedures, and the second cannot fail.

**2. Sentences the printed numbers don't support**

**(a) Statements that contradict the printed output:**
- **somata cell 11, attempt record fig5-three-classes (notes and response):** "The reviewer-code variant … has none either (selective 0.450, 0.036, 0.007)". The printed values are {2: 0.1136, 3: 0.3926, 4: 0.0043} (cell 10), which is a local maximum at 3.
- **decoding cell 23, attempt record fig6b-landmark-cells:** "The light-off intervals exclude 0.18 (by 0.001 for spikes)". The printed spikes interval is [0.175, 0.199], which includes 0.18 (cell 22). The outcome is unaffected, because light-on fails anyway.
- **Attempt record, fig6a-population-light-off:** "HeadingDecoder … intervals including chance". The printed intervals are [0.101, 0.178] and [0.112, 0.176] (cell 16), which include neither 0.10 nor 0.18.
- **somata cell 17:** the heading-like and landmark-like random-pairing shares are given as "0.368 and 0.510". Printed: 0.677 and 0.230 (cell 16).
- **axons cell 12:** reading (a) is given as "medians 0.143 … Mann-Whitney p = 0.074 … 40 of 135 … Fisher p = 2.8e-07". Printed: 0.134, p = 0.15, 39/135, Fisher p = 5.4e-07 (cell 11). Reading (b) is given as "p = 0.3 … 94 of 1084 … Fisher p = 0.026". Printed: 0.35, 93, 0.035.

**(b) Other numbers that don't match the printed outputs** (no outcome changes):
- **single_cue:**
  - Cell 17: 486 / 15.29% (printed 485 / 15.26%); 394 / 12.39% (printed 393 / 12.36%); 5.22% (printed 5.19%).
  - Cell 21: 166 / 5.22%, 481 reliable (printed 165, 5.19%, 478).
  - Cell 25: 486; 40.5% (printed 0.404); Rayleigh p = 1.7e-05 (printed 2e-05); 40.1% (printed 0.400). "SKKS090 and SKKS091 peak near +90 to +120": SKKS091 peaks at +60 to +90 (cell 23).
- **rotation_remapping cell 10:** "0.21 to 0.998" (printed minimum 0.222); "53 to 83%" (printed 52%); "12 degrees in a chamber-rotation file": one chamber-rotation file shifts 1° (cell 9).
- **axons cell 9:** −0.206 (printed −0.207).
- **somata:**
  - Cell 11: silhouettes 0.274/0.023/0.039 and 0.189/0.143/−0.054 (printed 0.272/0.019/0.032 and 0.190/0.120/−0.052).
  - Cell 14: 12.4/8.8/78.9%, 12.2/8.6/75.3%, and counts 194/75 (printed 13.5/7.6/78.9, 13.3/7.4/75.3, and 202/67).
  - Cell 17: 743.2, 669.4, 706.9, 727.7, 29.1% (printed 743.5, 669.5, 707.2, 728.4, 29.2%).
  - Cell 20: n = 194, 0.374/0.282, F(1,386) = 1.8, p = 0.18, variant p = 0.14; landmark n = 75, F(1,148) = 47.3, p = 6.0e-12 (printed n = 202, 0.378/0.279, F(1,402) = 2.2, p = 0.141, variant p = 0.116; n = 67, F(1,132) = 44.3, p = 2.8e-11).
  - Cell 23: 88.9/86.8%, 71.9/61.9%, 84.8 to 96.2%, 79.8 to 91.5%, LDA 83.7% (printed 88.1/83.0, 72.4/55.5, 84.3 to 96.2, 81.0 to 92.5, 85.2).
- **directions:**
  - Cell 7: 0.211/0.122, p = 0.165, 0.046/0.114/0.697 (printed 0.210/0.118, 0.16, 0.044/0.119/0.699).
  - Cells 10 and 14: n = 382, median 0.026 vs −0.031, p = 0.034, (a) p = 0.912; without the pair n = 270, p = 0.969/0.903, 0.090 vs 0.104 (printed 381, 0.027 vs −0.011, 0.026, 0.889; 269, 0.973/0.9, 0.093 vs 0.086).
- **decoding:**
  - Cell 20: 175 cells used, 0.425/0.372, 0.407/0.344, p 0.31 to 0.97, HeadingDecoder 0.127 to 0.148 (printed 179; 0.429/0.377; 0.415/0.341; 0.170 to 0.964; 0.130 to 0.146).
  - Cell 23: 54 cells used; 0.210 [0.195, 0.223]; 0.192 [0.181, 0.205]; light-on 0.397/0.395; HeadingDecoder 0.207 (printed 50; 0.207 [0.192, 0.220]; 0.187 [0.175, 0.199]; 0.396/0.383; 0.201).
  - Cell 26: 0.721/0.579, 0.712/0.579, heading-like 0.425/0.407, landmark-like 0.397/0.395, p = 0.010.
  - Cell 29: 11.9/13.7%, 7.1%, 0.105, range 0.105 to 0.158 (printed 0.120/0.136, 0.070, 0.104, 0.104 to 0.159).
  - Cell 32: the heading-like intervals.
  - Cells 14 and 17: spikes intervals [0.677, 0.745] and 0.571 [0.537, 0.606] (printed [0.678, 0.746] and 0.572 [0.535, 0.608]).
- **Attempt record:**
  - `measured` values: fig1g (15.29, 486), fig5-class-proportions (8.8, 12.4), fig6b-heading/landmark/alignment.
  - The notes and responses for fig1g, selection-shuffled-control, fig4-axons-light-off, figs5, figs6, fig5-three-classes, fig5-class-proportions, fig5e, fig5f, fig5gh and fig5i repeat the run that isn't shown.
  - The selection-shuffled-control finding says "5.22%", while the centring finding says "15.26%", the printed value. The record therefore mixes the two runs.
- **Stale cell 0 tables:** `axons.ipynb` lists the fig5 claims and says fig5k and Figure 6 are "recorded in the attempt record". `somata.ipynb` lists the fig4 claims.
- **Checked and found consistent:** the README outcome table matches the attempt record.

**(c) Do the round-1 reasons appear in my own words?** Yes. All 24 `reason` entries summarise my round-1 points faithfully.

**3. Round-1 points**

**Resolved:**
- **B2:** the outcome is now not_reproduced under the "once" reading.
- **B3:** both nulls added; I accept the partial outcome.
- **B5 and B6:** acknowledged; the outcomes that inherit the classes are downgraded.
- **B8:** reading (a) added.
- **B10:** run without the 6-bin pair shown; outcome changed.
- **B11:** `rsc.py` matches the code.
- **B12:** stated as an assumption.
- **B14:** that pair enters only the "either" readings.
- **B15:** recorded as a finding.
- **fig5k and fig6:** now tested.

**Remaining, and bearing on a conclusion:**
1. **Which run the conclusions describe (new).** The conclusions, Summaries and attempt record describe a run whose outputs aren't in the notebooks. Two statements are reversed by the printed output (somata cell 11; decoding cell 23 and the fig6a-light-off note). The notebooks need re-executing on the machine that produced the text, or the text rewriting from the printed outputs.
2. **B1, the selection test passes noise.** This is now quantified (4.7% of synthetic untuned cells; 5.19% of shuffled real cells) but not fixed. About a third of the selected cells could pass by chance, and every downstream claim inherits this.
3. **B4 and B7, fig2f.** Derotation artefacts are not excluded: head-rotation files show 52 to 83% selective cells and up to 3.19 spikes/s. The timing alignment of heading and activity is not established: the lag is −6 in one of the four files. Matched ROIs do no better than random pairs. The outcome rests on mirroring the chamber-rotation heading and using 5 of 7 pairs, neither checked against data. A further oddity: SKKS112-PlatformRotation-002 barely rotates (median step 0.12°/frame).
4. **Decoder choice.** The Bayes reading, on which 4 outcomes rest, is chosen partly because the reimplemented HeadingDecoder "decodes near chance". In fact its light-on accuracy is 0.20 to 0.22, twice chance, with intervals that exclude 0.10. The lab's own decoder performing this poorly points more to a reimplementation problem than to the decoder being the wrong reading, and that isn't checked.
   - Separately, training on even and testing on odd heading-resampled bins, about 1.8° apart and interpolated from the same frames, risks leakage between training and test data. That would inflate the Bayes accuracies.
5. **B9, fig1h.** The cue's position in the heading frame is still unknown, so the overrepresentation part of the claim cannot be judged.
