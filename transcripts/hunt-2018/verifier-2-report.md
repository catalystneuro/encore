**Round 2 verification: Hunt, Malalasekera et al. (2018), CRCNS pfc-7, attempt hunt-2018-01**

The claims file has 40 claims. The attempt record has 40 outcomes, one for each claim id: 37 reproduced, 2 partially_reproduced, 1 not_reproduced. One outcome is marked `assumed: true`, chose-on-partial-information. The verification block has 40 results and marks one disagreement, figs5c.

**1. Outcomes**

I agree with every stated outcome, but the stated reason for figs5c clashes with the label on figs1ab (point 3 below).

- **The assumed outcome (chose-on-partial-information).** The assumption is stated: the record names the passage, says the paper does not define "evaluated", and takes the script's joystick-corrected count. That is reasonable, since it is the only one of the three counts the paper's own code computes for this number. The record also says, correctly, that the other two counts fall outside the tolerance (cell 24: 54.23/42.56 and 95.59/92.25).
- **Outcomes resting on a minority of readings.** Three outcomes pass only under some readings, and the criterion allows that (one reading suffices). All three are stated honestly in their conclusion cells, though the Summary table shows them as plain "reproduced":
  - fig6e: 12 of 72 readings, including the scripts' own choices (cell 117).
  - fig8-spatial: 2 of 24 readings, and 1 with the exact binomial test (cell 141). In both passing readings the DLPFC action fraction is 7.5–9.0%, against the sibling claim's ~18%.
  - fig7a: 4 of 12 readings, and no chi-square test is below 0.05 (cell 120).
- **neuron-counts.** This rests on the stored `average_firing_rate`, a third reading the claims file does not list. It is stated, and the scripts settle it, so it is not an assumption.
- **fig8-action.** partially_reproduced is right. The authors' stored flags would meet the full criterion, but they are not a result computed here, so not counting them is correct.

**2. Sentences the printed outputs do not support**

- **Cell 71 and the record's fig4-t75 notes** say all nine t75 values equal the paper's at a 1 ms step "over -100 to 500 ms, and over -200 to 600 ms" (record: "over both ranges"). Cell 70 prints DLPFC left/right value = 358 at 1 ms over −100 to 500 ms (paper 369). Only the −200 to 600 ms range gives all nine exactly. The outcome is unaffected, because 358 is within tolerance.
- **Cell 97 and the record's fig5k notes** call the Fisher p-values "the paper's values", ending "< 0.0001" against ACC. Cell 96 gives z = −4.357, which is p ≈ 1.3e-5. The paper reports 0.00013, so that one value is ten times smaller than the paper's. The other five match.
- **The record's fig8-action notes** say "The tests all hold in six readings … the exact binomial test changes none of this." In cell 138, reading (b, iii, b, 0.05) passes with the script's formula but fails the exact test ("tests hold True (exact False)"). With the exact test, five readings pass. The conclusion about tolerance is unaffected.
- **The record's figs5c notes** say "The t75 point estimates follow the paper's order in every region." Cell 70 prints point estimates only for the nine claimed variables. Cell 73's significant set also includes stimulus identity in ACC and DLPFC and accept/reject in DLPFC, whose point estimates are not printed.
- **The record's figs5c notes** give the change to not_reproduced as "the criterion names no partial outcome". The figs1ab criterion names no partial outcome either, yet figs1ab stays partially_reproduced. The two labels need one consistent rationale.
- **The README** lists "…early choices | Reproduced" without the "(assumed)" that the Summary (cell 153) and the record carry.

Everything else checks out against the printed outputs, sentence by sentence: the other "**Result:" cells, the Summary, the README counts (37/2/1, 549 units, 1.6e-06 / 3.3e-07 / 2.6e-07, run time 11.3 min) and the record's notes. Section 2 lists the exceptions.

**My round-1 reasons in the record.** They are restated accurately and attached to the right claims: points 1, 2, 6 to fig6c/6e, 3 to fig5gj, 4 to fig5k, 5 to fig8-spatial, 7 to chose-on-partial-information, 8 to figs1ab, 9 to neuron-counts, the chance-level note to fig8-action, and the section C items to fig8-cue1 and the "reviewed" text. figs5c is correctly recorded as a disagreement with partially_reproduced. Most reasons are close paraphrases of my text, not new wording, but none misstates what I said.

**3. Round-1 points**

Resolved:
1. **Projection design.** The Methods' two-column projection now runs for every combination. fig6c and fig6d hold in 36 of 36; fig6e holds in 6 of 72 (cells 111, 114, 117).
2. **Action bin.** The −200 ms bin now runs. fig6e holds in 16 of 72, a superset of the 12 that pass at −210 ms (cell 117).
3. **Cross-correlation maps.** All nine epoch blocks are computed as the script does (lines printed in cell 11), with 8-connected clusters, plus a 183 × 183 variant. The criterion holds under both (cell 93).
4. **Unit exclusions.** A variant with units 87 and 653 restored and the paper's n gives the same result: 5 of 6 comparisons at p < 0.05 (cell 96).
5. **Binomial test.** The exact test is added (cells 135, 138, 141).
6. **Random halves.** The record now uses the scripts' stored halves, plus halves drawn once per session; both agree (cell 111).
7. and 8. **Claims-file gaps.** Each is recorded and passed to a reader as a question. The gaps in the claims file remain for the reader.
9. **Supplementary Table 1.** Compared session by session: 53 of 53 sessions match when every unit is counted, 26 of 53 at ≥ 1 Hz (cell 18).
10. **`conv_same_200` offset.** The docstring now explains it, and by index arithmetic it matches MATLAB `conv2 'same'` (inputs k−99 to k+100).
- **Section C.** The script lines are now printed (cell 11). The cue 1 regression (3.3e-07) and the Figure 6 weights (2.6e-07) are now checked against stored outputs.

What remains that bears on a conclusion:
- **figs1ab vs figs5c labels.** The rationale needs reconciling (section 2). I would keep both outcomes and restate the figs5c reason: its single test fails in two of three regions under every reading. In figs1ab, one component fails, in one monkey.
- **fig5gj, the criterion's literal reading.** The single 183 × 183 map passes by narrow margins (1105 vs 1083 and 817 vs 810, cell 93), with thresholds from the 99.9th percentile of only 1000 permutations. Another seed could flip it. The main reading follows the script and passes by a wide margin, so the outcome stands.
- **Still not checked against stored output.** The RSA (the data set holds no stored RSA output) and the Figure 6 projections themselves (`info_gathering_ramp_to_choice.mat` not read). Only the weights the projections use are validated.
