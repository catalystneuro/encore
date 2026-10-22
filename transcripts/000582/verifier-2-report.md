## Verification report, round 2: Sargolini et al. 2006 on dandiset 000582 (0.251111.2151)

The claims file has 21 claims, and the attempt record gives an outcome for each:
- 5 reproduced
- 1 partially reproduced
- 3 not reproduced
- 12 blocked: 9 as methods_underspecified and 3 as data_missing

Cell numbers below are this notebook's, which differ from round 1's.

### 1. Outcomes

| Claim | Record | Agree? |
|---|---|---|
| layer2-grid | partially_reproduced | Yes |
| grid-all-layers | reproduced | Yes |
| gridness-range-similar | blocked, methods_underspecified | Yes |
| grid-stable | blocked, methods_underspecified | Yes |
| spacing-dorsoventral | blocked, data_missing | Yes. The electrodes table, now printed in cell 3, has location "MEC" and no coordinates. |
| fieldsize-dorsoventral | blocked, data_missing | Yes |
| grid-phase-orientation | blocked, methods_underspecified | Yes, now. 88 of 224 readings hold (cell 33). |
| hd-layers | not_reproduced | Yes |
| hd-with-grid-colocalized | blocked, methods_underspecified | Yes |
| hd-tuning-breadth-layers | blocked, methods_underspecified | Yes |
| hd-full-range | reproduced | Yes |
| hd-colocalized-distributed | reproduced | Yes |
| hd-stable-trials | reproduced | Yes |
| hd-rates | not_reproduced | Yes |
| deep-hd-conjunctive | not_reproduced | Yes |
| gridness-hd-continuous | reproduced | Yes |
| conj-tuning-similar | blocked, methods_underspecified | Yes |
| cue-rotation-coherent | blocked, data_missing | Yes |
| speed | blocked, methods_underspecified | Yes. Split 119 / 325 / 4 across 448 combinations of method details (cell 71). |
| speed-slope-steeper | blocked (depends on `speed`) | Only if the protocol blocks a claim whose parent is blocked; I cannot see docs/protocol.md. On its own criterion all 448 readings give partially_reproduced (cell 75). |
| speed-intercept | blocked (depends on `speed`) | Same condition. On its own criterion all 896 rows give not_reproduced (cell 78). |

The two dependent claims need a separate remark:
- **Their own analyses agree under every reading.** `speed` is blocked because its cell-counting readings disagree, and neither dependent claim uses that count.
- **Their label names the wrong cause.** `blocked_by: methods_underspecified` does not describe a block that comes from the dependency.

The record states my disagreement correctly.

### 2. Statements the outputs do not support

- **Cell 68 and the record's `conj-tuning-similar` notes:** "The t-test finds a difference … under 98 of 112 readings." Cell 67 prints "t-tests finding a difference: 96 of 112". The outcome does not change.
- **Cell 27 and the record's `gridness-range-similar` notes:** "The Kruskal-Wallis difference lies among the deeper layers." No pairwise test is printed. In cell 26 the layer III median is above the layer II median in every one of the 56 rows (for example 0.632 against 0.316). So layer II against layer III contributes to the difference; it is not confined to the deeper layers.
- **Cell 80 (Summary) and the README:** "every grid and head-direction claim with each (rat, depth, hemisphere, name) counted once (no outcome changes)". That variant was run for only four claims: `layer2-grid`, `hd-layers`, `deep-hd-conjunctive` and `hd-colocalized-distributed` (cells 20, 38, 61, 50). It was not run for:
  - `grid-stable`
  - `grid-phase-orientation`
  - `hd-with-grid-colocalized`
  - `hd-tuning-breadth-layers`
  - `hd-stable-trials`
  - `hd-rates`
  - `conj-tuning-similar`
  - `speed`
  - the other grid claims
- **Cell 80:** "an outcome line for every tested claim". Cells 23 (`grid-all-layers`), 26 (`gridness-range-similar`) and 44 (`hd-tuning-breadth-layers`) print no outcome line.
- **Cell 62 and the record's `deep-hd-conjunctive` notes:** "Without those files … p 2.4e-07 to 0.00033, which would be partially reproduced". Cell 61 computes this for chi-square reading (a) only. Reading (b), whose four-layer p reaches 0.23 on all files, is not computed for that variant. So "partially reproduced" is supported for reading (a) only, and the readings might disagree.
- **Cell 21 and the record's `layer2-grid` notes:** the numbers are correct, but one consequence is not stated. Above the 95% point of the time-shifted gridness, layer III (0.419) exceeds layer II (0.408) (cell 20). The layer order that underlies "partially reproduced" therefore does not survive a stricter grid threshold. This does not decide the outcome, but it belongs in the conclusion.
- **Record finding, and cell 16:** "against 2.6 to 8.4 cm in the other 69 two-LED files". The 8.4 cm is printed nowhere; cell 5 prints only the overall range of 2.6 to 36.0 cm.

All other numbers I checked match the outputs. That covers every other "**Result:**" cell, the Summary table, the README table, and the record's notes, measured values and findings.

**My round-1 reasons in the record.** They are stated faithfully, in close paraphrase, for all 21 claims, with problems 2 to 9 attached where they belong. One discrepancy is mine: the `grid-phase-orientation` reason repeats my figure that layer VI fails under "22 to 33 of 56". The current output (cell 33) gives 21 and 32 (35 and 24 holding). The outcome is unaffected.

### 3. Round-1 points

**Resolved:**
- 1: `grid-phase-orientation` is relabelled.
- 2: The tracking of rat 11265's two files is shown and looks normal. The two outlier LED files are identified and recorded as a finding. `hd-layers` and `deep-hd-conjunctive` are recomputed without them.
- 3: A time-shifted control was added. 0.297 of shifted maps have gridness above 0, consistent with my synthetic 27.5%. It is discussed in the conclusion.
- 5: The sign test now enters the `speed` outcome.
- 6: Answered: the criterion judges each layer, and the 20 of 487 pairs that cross layers are reported.
- 8: Added as a deviation.
- 9: The cells I listed now print outcome lines.
- My requests for a per-rat table counting each cell once and for the electrodes table are met.

**Remaining, bearing on conclusions:**
- **Problem 4 is only partly addressed.** Cells are counted once in only four claims (see section 2). The Summary and README overstate this.
- **The `hd-layers` "without rat 11265's files" variant is weaker than presented** (cell 38). The 17 remaining layer II cells are all from rat 11278, and 11 of them are in `sub-11278_ses-31080502`, whose LEDs are more than 15 cm apart in 62% of samples. So the "0 of 17" rests on only 6 layer II cells with plausible tracking. The conclusion should say so.
- **The stricter-threshold control reverses the layer II / III order** (cell 20, see section 2). This bears on how much weight `layer2-grid`'s partial outcome can carry.
- **Problem 7 remains.** The effect of the 11% rescaling on the 0–3 cm/s rates is still untested. It cannot plausibly explain rates about 40% low, so the dependent outcome stands either way.
- **The third questionable-LED file is never discussed against `hd-stable-trials`.** `sub-11025_ses-06050501` has 17.8% of samples above 15 cm (cell 5). It is a two-trial file of one of the three rats behind `hd-stable-trials`, and that claim never discusses it.
- **The dependent-claim label** for `speed-slope-steeper` and `speed-intercept` (section 1) still needs the protocol text to confirm the rule. If the rule holds, the `blocked_by` value should name the dependency rather than methods_underspecified.
- **Which LED is red** cannot be settled from the files. It is recorded as a finding and the assumption is stated.
