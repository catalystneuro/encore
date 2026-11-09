**Verifier report, round 2: Churchland et al. 2010 (doi:10.1016/j.neuron.2010.09.015) on DANDI:000138 v0.220113.0407**

**1. Outcomes**

The claims file has 15 claims and the attempt record has 15 outcomes: 2 blocked, 1 partially reproduced, 2 not reproduced and 10 reproduced. I agree with all 15.

| Claim | Record | Agree | Assumption stated and reasonable? |
|---|---|---|---|
| fig4abc | blocked (data_missing) | yes | n/a |
| fig4d | partially_reproduced, assumed | yes | Stated. The readings (concatenated profile, mean proto-trial, the table's onset, tuning as a range) are defensible. The result is fragile: onset (b), a median 14 ms later, gives p = 0.166 (cell 23), and a ratio of 1.25 gives p = 0.069 (cell 24). The notes give the range of readings. |
| fig4e | not_reproduced | yes | None needed: all 8 readings give 0.129 to 0.218 at onset. |
| results-ap-location-no-effect | reproduced, assumed | yes | Stated: the array of each unit comes from the id prefix. Reasonable, and p does not depend on which prefix is which array. |
| supp-preparatory-dimensionality | reproduced, assumed | yes | Stated (concatenated selection). The value sits at the bound, and the record calls the outcome fragile. |
| fig6-peri-movement-space-best | reproduced | yes | The criterion asks for one combination of readings, so no assumption is needed. |
| fig6-each-dimensionality | reproduced, assumed | yes | Stated. It now holds under fold=refit too (21 of 22, cell 43). |
| fig6-dimensionality-trend | reproduced, assumed | yes | Stated: it holds in 91% of combinations with fold=once and 6% with refit. "Once" is a reasonable reading, but the outcome rests on it. |
| fig6-pd-adequate-all-spaces | reproduced, assumed | yes | Stated. |
| fig6e-summary-rank | blocked (data_missing) | yes | n/a |
| fig7a-shuffled-space-poor | reproduced, assumed | yes | Stated. |
| fig7b-window-start-onset | reproduced, assumed | yes | Stated. |
| fig7c-anterior-posterior | not_reproduced, assumed | yes, but see 3 | The assumption that the upper-limit space leaves out the unit being fit is stated, but I now find it weakly supported (see 3, B2). The outcome does not depend on it under fold=once: with the unit included, the main reading gives 0.963 and 0.615 (cell 58), which still fails. The criterion's 10% bound is narrower than the random-half SD of 0.190, so this not_reproduced is weak evidence. The record says so. |
| fig7d-pd-consistency | reproduced | yes | Holds in all 16 variant and scaling combinations. |
| fig8-oscillator-model | reproduced | yes | Holds under all 4 readings. |

On the claims file: I found no misreading of the paper. The 1.5× criterion, the epochs, the inclusion thresholds, the Figure 7C legend and the 25-condition draws all match the text.

**2. Sentences the numbers do not support**

- Cell 25: "mean Spearman r 0.147 to 0.212". Cell 23 prints 0.146, and the record says 0.146.
- README: "It takes about ten minutes". Cell 67 prints "Notebook run time: 3.2 min".
- Summary (cell 66): "no test segment repeats a training interval sequence". Cell 13 checked only the first 20 of 122 units, using sampled runs of 5 intervals (0 of 1503).
- Record, fig7a notes: "as the latter collapses at high k". The peri-movement curve under combine=each is never printed. Cell 52 shows only `below_peri_every_k False` and a best of 0.150.
- Cell 62 ("so consistency here is higher than it would be with 108 conditions in both kinds of space") and the record's fig7d deviation ("which raises consistency in both kinds of space"): this is reasoning, not a measurement. Only the overlap (16.5 distinct conditions per draw, 10.1 shared) is printed.

Every other number in the Result cells, the Summary, the README table and the record notes matches the printed outputs.

The record's round-1 reasons are in my own words, with the B and C points merged into the right claims. One small inaccuracy in the record's "reviewed" text: it says the conclusion cells and summary were removed, but my round-1 report noted that cell 0 still held the author's outcome table, which I did not use.

**3. Status of my round-1 points**

Resolved:
- B3: every variant now uses 20 draws (cells 52 and 58).
- B4: the dataset difference and the draw overlap are stated (cell 61).
- B5, B6, B7 and B8: each is now stated in the conclusions and the record.
- C, fig7c spread: the random-half SD and percentiles are printed (cell 58).
- C, fold=refit: the curves and comparisons won are printed (cells 40 and 43).
- C, trial counts: per-condition counts under every reading are printed (cell 15).
- My round-1 remark that fig6-each "flips under refit" was wrong. With the main reading it meets the criterion under refit.

Resolved by documentation, but the conclusion still rests on them:
- B1 (fold reading) for fig6-dimensionality-trend. The record states it and puts it to the authors as a question.
- Which session this is, and which id prefix is which array. Neither can be settled from the files, and the record lists both as findings.

Remains and bears on a conclusion:
- B2 (fig7c upper limit). I overstated this in round 1, and the author adopted it. The paper describes the upper-limit space as "derived from the preparatory activity of all neurons (T was c×n with each row containing the mean preparatory activity for every neuron)". For the peri-movement space, the Methods state the exclusion explicitly: "all neurons except the neuron whose preparatory activity we were trying to capture". No such exclusion is stated for the upper limit.
  - With the unit left out, the "upper limit" is exceeded: the random-half normalised performance reaches a 95th percentile of 1.252, the main-reading posterior/random ratio reaches 1.273 under fold=refit, and the random-half mean under `each` is −0.826 with SD 10.8 (cell 58).
  - With the unit included, every value stays below 1, and anterior comes out better than posterior, as the paper reports.
  - Leaving the unit in is at least as well supported as leaving it out, so the record should not describe the included rows as "not counted" on the paper's authority. Under the main fold=once reading fig7c fails either way, so the outcome stands. The 2 rows that pass need both fold=refit and the unit included.
- fig7a under fold=refit passes by 0.001 (shuffled 0.159 against kinematic 0.160, cell 52), which is within the noise of 20 draws. This does not affect the main-reading outcome.
