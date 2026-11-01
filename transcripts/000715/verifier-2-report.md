**Round 2 verification: Yemini et al. 2021 (NeuroPAL), DANDI:000715 v0.241009.1514**

**1. Outcomes**

The claims file holds 32 claims and the attempt record gives 32 outcomes, one per claim:
- 4 reproduced
- 5 partially reproduced
- 4 not reproduced
- 19 blocked: 16 not attempted, plus fig7bc-ventral-ganglion-lowest, ms1-calibration and fig6de-asj-ric-stimulus-specific

My round-1 count of 31 claims was wrong. That error carries into the record's verification entry, which says I "did not review the 15 claims"; it should be 16.

| Claim | Record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| fig2cd-variability-differs | partially | Yes | Yes. The gauge fix and 20 alternations are stated, with 6 variants, all at ratio ≥ 9.39 |
| fig2c-ollr-more-variable-than-olll | reproduced | Yes | Yes. Same assumption; SD ratio 2.00 to 2.33 across variants |
| fig7bc-identification-accuracy | not reproduced | Yes, but the margin is thin (see 3) | Yes |
| fig7bc-ventral-ganglion-lowest | blocked (data_missing) | Yes | – |
| fig7b-eight-labels-above-90 | not reproduced | Yes. Even the rotated start gives 79% | Yes |
| ms1-uncertain-first-faster | partially | Yes | Yes |
| ms1-position-only-accuracy | not reproduced | Yes. The paper's alignments give 20 to 27%; rotated 43.1 to 44.0% | Yes |
| ms1-detection-accuracy | partially | Yes | – |
| ms1-calibration | blocked (methods_underspecified) | Yes | – |
| ms2-neuropal-color-violations | reproduced | Yes, under the amended criterion | – |
| fig7de-optimal-coloring-violations | partially | Yes under the criterion's reading, but it is not robust (see 3) | – |
| fig6d-ase-nacl-asymmetry | reproduced | Yes | – |
| fig6ef-nacl-novel-interneurons | reproduced | Yes | Storey λ = 0.5 is not flagged as an assumption; see 3 |
| fig6de-asj-ric-stimulus-specific | blocked (methods_underspecified) | Yes | – |
| tables6-tail-pvq-and-post-stimulus | partially | No. I would give blocked (methods_underspecified) | 10 s post-stimulus window: stated and reasonable |
| figs1h-avf-cyclic-activity | not reproduced | Yes | Peak rule: stated, with three prominences and a spectral check |
| The 16 claims not attempted | blocked | Yes | – |

The tables6 disagreement is about consistency. `wholebrain_zenodo.ipynb` cell 5 states the rule "a claim whose outcome differs between them is blocked". tables6 gives full, full and partial under the three removal readings (cell 14), so under that rule it is blocked. The alternative, "the outcome every reading supports", would make fig6de partially reproduced: ASJ to NaCl and 2-butanone, RIC to 2,3-pentanedione, and the overlap of responding sets all hold under every reading. One rule should be applied to both claims.

Claims-file misreadings still stand:
- fig7de takes 7,500 runs to be for the single 3-reporter setting. Methods S2 Figure 1 spreads 7,500 simulations across several settings. The record has put this question to a reader.
- ms2 and fig7de: the shortfall measure was chosen because the Methods share is far from the target. The record states this openly.

**2. Text against printed outputs**

Most sentences match the outputs. These do not:

- **Attempt record, ms1-uncertain-first-faster notes:** "a gap of 4 to 10 points over the range". In `reproduce_yemini_2021.ipynb` cell 33, the gaps between the means over the range are 3.5 to 7.8 points (52.0−48.5 up to 86.8−79.0). "1 to 3 points at eight" is fine (0.9 to 3.3).
- **Attempt record, fig7b-eight-labels-above-90:** "No held-out worm exceeds 90% with these alignments (the best, 86.2%)". Per-worm values are printed only for the CELL_ID alignment with the entropy ranking (cell 31). The zero counts above 90% are supported; "the best, 86.2%" is supported for that one run only.
- **Cell 26 and the record (fig7bc):** "the class-level readings fall inside the tolerance under three of the four variants". Under the no-gauge variant only the mean-per-worm class reading is inside (77.43); the pooled class reading (77.35) is outside (cell 25).
- **Cell 41 Summary:** the rotated-start variant "changes no outcome". This is true only on the main atlas, where 77.38 against a bound of 77.4 misses by 0.02 points (cell 24). Under three of the four atlas variants it would put fig7bc inside the tolerance (cell 25).
- **Attempt record, fig7de notes:** "The second value is outside the tolerance at every sparsity tried, so the outcome does not depend on this choice." The first half is correct. The conclusion does not follow: the best value goes from 8.38% at sparsity 2000 to 12.36% at 3000 (`optimal_coloring.ipynb` cell 10), across the 9.45 to 11.55% band. Sparsity 3000 had only 1,000 runs.
- **Attempt record, data_missing finding:** "Eight of the claims tested here need the tails". The record's own notes mark nine as head-only or head-atlas-only: fig2cd, fig7bc, ventral ganglion, uncertain-first, position-only, detection, calibration, ms2 and fig7de.

Everything else matches: the README, both other notebooks' results and summaries, and the other record notes.

My round-1 reasons are given faithfully in the verification entry. They are close to my wording, with my numbered problems folded into the matching claims. The only error is the count of 15.

**3. Round-1 points**

Resolved:
- 1, orientation: measured (DV heads at 92.6 to 102.7°, LR at 1.8 to 12.9°), with a rotated-start variant, grouping by view, a 4-distinct-starts check, and a code_mismatch finding.
- 3, docstring: replaced with the counts, and fig6de is now blocked.
- 7: the forward regression is run.
- 8: the ventral ganglion's head part is reported.
- 9: the ridge is stated.
- 10: the filter and pooling are stated.
- 11: annotations of all 10 heads are compared with Zenodo.
- Sinkhorn equivalence: largest difference 0.0013 (cell 21).

Partly resolved:
- 2, fig7de sparsity: more sparsities were run, but see below.
- 4, SLSQP: 2,046 of 2,065 fits converge, and the effect of the optimiser is still not measured. It no longer bears on the outcome, which is partial either way because the tail is missing.

Remaining points that bear on a conclusion:
- **tables6 against fig6de:** the two claims use inconsistent rules for readings that disagree (section 1).
- **fig7de, 3-reporter value:**
  - The outcome turns on two open details: the sparsity (between 2000 and 3000 the best value crosses the band, and 3000 had only 1,000 runs) and how many runs the paper's best was taken from. The best of 100 runs lands in the tolerance 66% of the time (cell 9).
  - On the paper's own data.mat adjacency, the port gives 8.71% for 3 reporters, below the tolerance. It also gives 1.99% for exactly 39 reporters, above it (cell 12).
  - The outcome holds under the criterion as written, but the note that it does not depend on the sparsity should go.
- **fig7bc and position-only, margin:**
  - With orientation corrected, fig7bc misses by 0.02 points on the main atlas and is inside under three atlas variants (class readings).
  - With perfect alignment it reaches only 77.7 to 80.2%, which supports not reproduced. The record should state the 0.02-point margin plainly.
  - The position-only rotated start (43.1 to 44.0% against a 45% bound) is not shown under the atlas variants.
- **Storey π0, could not check:** AVF q 0.041, AVJ q 0.039 and RIC-to-NaCl q 0.044 are close to 0.05. The notebook does not print π0 or the q-values under another π0 estimate. A smaller π0 could move fig6ef or fig6de.
