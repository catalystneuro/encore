**Verifier report, round 2: Tarduno, Cottrell & Zhou 2024 (FIGSHARE:24639285 v1)**

The claims file has 17 claims and the attempt record has 17 outcomes. Three are marked `assumed: true`: table2-fit-statistics, fig1-linear-components and fig2-changing-field.

### 1. Outcomes and assumptions

I agree with all 17 outcomes:

- **reproduced (12):** glass-specimen-set, glass-success-rate, table2-no-fit, fig1-linear-components, fig2-changing-field, glass-af-no-change, table1-max-intensity, baseline-range, fig3-nrm-consistent, fig3-590-inconsistent, fig3-alteration-check-inconsistent, crystal-14053g1-400c-stable, no-alteration-recording-efficiency.
- **partially_reproduced (3):** table2-fit-statistics, glass-directions-not-random, example-14053g1-threshold.
- **blocked (1):** interpretation-impact-no-dynamo.

example-14053g1-threshold changed to partially_reproduced after round 1, which matches my round-1 outcome.

All three assumptions are the same one: the repeated measurements of a step are averaged as vectors. Each record entry states it as a deviation, shows the first-measurement alternative and its result (38% for table2-fit-statistics; ss43 R2 0.99; ss41/ss22 R2 0.16/0.44), and asks the authors about it in a finding. The assumption is reasonable, because the mean reproduces Table 2 far better than the first measurement does (23 vs 11 of 29, cell 15). One sentence of the justification overstates the evidence; see section 2, item 1.

### 2. Sentences the printed numbers do not support

1. **Cell 18, and the record's table2-fit-statistics deviation.**
   - Cell 18: "the mean is adopted because it gives the printed MADs to the printed digit for six specimens".
   - Record: "the reading under which the MADs of six specimens match Table 2 to its printed digit".
   - Cell 14 shows that only ss19 (30.10 vs 30.1) and ss22 (35.36 vs 35.4) round to the printed value. ss43 10.25, ss41 24.06, ss6 21.18 and ss34 11.95 are within 0.3° but do not round to it.
   - The supported wording appears elsewhere in cell 18 itself: "6 of them within 0.3 deg".
2. **Cell 30.** "median line MAD 24 to 27 deg, near those of ss41 and ss22".
   - ss22's line MAD is 35.4° (cell 28), above the null medians, so the "near" applies to ss41 only.
   - The nulls in cell 29 are for 4 and 5 vectors, but ss41's range has 3 field-off directions (cell 28), so no printed null matches ss41's case. The record's notes repeat "sequences of 4 and 5 vectors" without saying this.
3. **Cell 54.** "1.0e-10 to 6.0e-10 emu … several times the 8e-11 emu threshold".
   - The low end is about 1.3 times the threshold.
   - The Summary's "all above the 8e-11 emu threshold" is supported (cell 47: 37/37).
4. **README.** "It runs in under a minute." No output prints a run time, so I could not check this.

I checked every other "**Result:" sentence, the Summary, the README and the record notes against cells 1–54, and the numbers support them. This includes the 23/29, 22/29 and 14–19/29 scores, the ss9/ss10 scatter, the 11 two-group steps in 7 sheets (9 in range), the 11/11, 9/11 and 8/8 counts, the curvatures, 8/22, 9/22 and 7/18, 8/10, 24/24, the 4/12 and 10/12 rounding, 0.200–0.500, k 78 and p 0.0003, and 0.77–1.17 and 1.54–2.35.

The record's `verifications` section states my round-1 reasons in my own wording and against the right claims. One reason no longer holds, and I withdraw it. Under no-alteration-recording-efficiency (and in my problem 5) I wrote that reading (a)'s 8e-11 emu allowance is "below the replicate scatter". Cell 53 shows the per-crystal standard deviation of the 590.0 moments is 0.6–6.3e-11 emu, which is below 8e-11. What lies above the threshold is the level of the moments, not their scatter. One consequence: 14053g1's 590.3 excess (9.8–12.1e-11) is about 6–7 times its 590.0 standard deviation (1.6e-11), so its failure under reading (a) is not a noise artifact. The outcome still holds, because it rests on reading (b).

### 3. Round-1 points

**Resolved:**
- **Problem 1 (synthetic sheets):** reported in a finding, the README, the notes and the counts without them.
- **Problem 2 (averaging):** `assumed: true`, deviations and an author question. The overstated sentence is in section 2, item 1.
- **Problem 3 (ss6 250.1):** the score with ss6 counted as a miss (22/29), plus a scan of all steps for two direction groups.
- **Problem 5:** handled, with my correction above.
- **Problem 6:** null rates and an Arai curvature added.
- **Problem 7:** TRM40/TRM20 printed, a deviation added and the question put to a reader.
- **Problem 8:** fixed-reading pTRM scores printed.
- **Section C outputs:** all five requested outputs are now printed.

**Remaining:**
- **table2-fit-statistics (bears on the conclusion):** the score is 23/29. One more match (24/29, 83%) would cross the 80% bar. The deposit PDF "SupplFig1 - other Thelliers March 2024.pdf" would show which steps the authors fitted for ss9 and ss10, but it is still unread. The partial outcome therefore depends on the unknown fitting details for those two specimens. It also counts ss6's R2 as a match even though one averaged step has no physical meaning.
- **Problem 4 (does not affect a conclusion):** Table 1's M590 equals |590.1| exactly for 12 of 12 crystals (cell 38), while the Methods define TRM as a vector difference. The notes mention this, but the record has no paper_inconsistency finding or author question for it.
- **fig2-changing-field (does not affect a conclusion):** no null rate for 3 vectors (ss41). Both readings stay weak tests.
- **table2-no-fit (does not affect a conclusion):**
  - Under reading (a), ss29's only fall is 0.6% (6.36 to 6.32, cell 20), below its median standard error of 2.5% (cell 21). Without it, (a) is 10/11, still at least 9.
  - The "trend out of origin" condition rests partly on ss39, a synthetic two-step sheet.
- **Figures 1–3 (not checkable):** still not seen, so the nominal paleointensities and the arrow-marked step ranges remain unchecked.
