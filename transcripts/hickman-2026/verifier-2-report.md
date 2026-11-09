**Verification report, round 2: Hickman et al. 2026 against DANDI:000774 (0.260520.1753)**

The claims file has 42 claims. The attempt record gives 42 outcomes: 11 reproduced, 7 partially reproduced, 3 not reproduced and 21 blocked. Five outcomes are marked `assumed: true`: fig4f, fig5j, fig5i, figs6b and fig6f. The cell numbers below are 0-based indices into the re-executed notebook.

### 1. Outcomes

**I agree with these 34 outcomes:**
- **The 21 blocked claims.**
- **Reproduced (8):** fig4d, figs3cd, fig4h-extent-constant, fig4j, fig5bc, fig5ef, fig6g and fig4i. For fig4i, see point N2 below.
- **Partially reproduced (3):** fig4h-distance-decreases, fig6e and figs9. Each of their criteria has a partial clause.
- **Not reproduced (2):** fig4h-ks-distinct and fig6d.
- **fig5-fsrs (not reproduced):** no reading gets the four proportions within tolerance (cell 43). The criterion has no partial clause, so not reproduced is right.

**I disagree with four outcomes: fig4f, fig5i, figs3e and fig6c, all recorded as partially reproduced.**
- None of their criteria has a partial clause.
- The record changed fig5-fsrs to not reproduced "as the criterion has no partial clause". The same rule makes all four of these not reproduced:
  - **fig4f:** RS at 5 µA is 0.400, against 0.333 ± 0.033 (cell 16).
  - **fig5i:** RS at 5 µA is 0.400 (cell 49).
  - **figs3e:** the 100 µA proportions are 0.058 and 0.106, against 0.092 and 0.175 (cell 34).
  - **fig6c:** the criterion requires every reading to hold. Under reading c the region term has p = 0.457 (cell 57).
- In round 1 I accepted partial for figs3e and fig6c. I revise that so one rule is applied throughout. If the protocol does allow partial outcomes without a clause, then the reason given for changing fig5-fsrs is wrong instead. Either way, the record must use one rule.

**The five assumed outcomes:** each assumption is stated in the record.
- **fig5j and figs6b (the code's 0.4 ms threshold classes):** reasonable. With the code's coordinates, the threshold classes give the paper's F = 8.04 and 4.10 exactly (cell 46). The k-means reading is shown over 20 runs (cell 55):
  - fig5j's waveform term is never significant, so fig5j rests on the assumption.
  - figs6b holds at all four amplitudes in 9 of the 20 runs and in the lowest-WCSS run, so it depends on the assumption less.
- **fig4f and fig5i (same assumption):** stated, but the outcome does not depend on it.
  - In fig4f, k-means RS fractions also fail at 5 µA (0.520) and pass the other three.
  - In fig5i, k-means does worse: FS is 1.000 at 5 µA, from n = 2.
  - The outcome of both turns on the contact coordinates, not on the classes.
- **fig6f (the code's peak rule, with no 4 ms width filter):** stated, and reasonable.
  - The criterion says its peaks come "from the code", and the code applies no width filter.
  - The paper's r values (−0.03 and 0.09) fit the code's rule (r = −0.001 and 0.047) better than the width-filtered rule (r = 0.131 and −0.115; cell 66).
  - It does contradict the criterion's literal "width at least 4 ms". Under that wording the outcome is not reproduced. The claims file probably mis-transcribed the code here; I report this and do not correct it.
  - In round 1 (B9) I said the width filter does not affect the conclusion. That was wrong: applying it flips the outcome.

**N2. fig4i: an interpretation that is not marked as an assumption.** The outcome rests on reading (c), which the notebook computes as the raw CCF distance signed like `norm_distance` (cell 2). The criterion says "raw CCF distance" without a sign. The claim that the code's `distance` column is signed this way is not shown in any output, and the unsigned version was not run. Readings (a) and (b) fail the values at 50 and 100 µA (cell 28). The near-exact match with the code's coordinates (F = 5.41, p = 0.0201) supports reading (c).

### 2. Text against the printed outputs

These sentences are not supported by the outputs:
- **Cell 61, and the attempt record's fig6d notes:** "460 units, of which 273 are CA1". The number 273 is printed nowhere. Cell 60 prints 315 Field CA1 units, but over all nine recordings, while the 460 come from the seven cathodal recordings.
- **Attempt record, fig6d:** "349 units, of which 151 are superior colliculus or dentate gyrus units". 151 is the nine-recording count (68 + 43 + 36 + 4, cell 60); the 349 are from seven recordings.
- **README, the attempt record's coordinate finding, and the Summary (cell 74):** "with the code's coordinates the distance results match the paper exactly". Two printed values contradict this:
  - The 50 µA extent is 868, against the paper's 965 ± 96.5, so it is just out of tolerance (cell 19).
  - The 50–100 µA adjusted KS p is 0.8245, against the paper's 0.083 (cell 25).
  - Cell 20 likewise calls 1179, 884, 868 and 522 "the paper's values".
- **Attempt record fig4j, and the Summary:** "the number of good stable units per condition … equals that of the code's intermediate table direct_df.csv". Cell 8 prints the counts, but no output compares them with direct_df.csv.
- **Attempt record, figs9:** the values are "about a quarter of the paper's … 0.104 and 0.107 at 100 uA". At 100 µA, 0.0159 against 0.104 is about one sixth (cell 69).
- **Attempt record fig5-fsrs, fig5j and figs6b:** "20 k-means runs from other seeds". One of the 20 (`points 0`) is the original run: it has the same 470 FS units and the same class p = 0.028 (cell 55).
- **Attempt record, fig6e:** "the Results' cathodal values are F region 40.14 and interaction 15.61". The Results print these next to F amplitude = 175.18 and do not call them cathodal.
- **Cell 44, a minor case:** "class p … 0.821 within the evoked potential" holds only under reading (c). Readings (a) and (b) give 0.983 and 0.608, which are also not significant.

Every other sentence I checked matches the outputs. That covers every "Result:" cell, the rest of the Summary and README, and the record's notes.

**My round-1 reasons:** the attempt record's `verifications` block states them faithfully and in my own words. It correctly records `agrees: false` for fig5ef and fig5-fsrs.

### 3. Round-1 points

**Resolved:**
- **B1:** the fig5ef assignment search was added (cell 40).
- **B2:** fig4f, fig4i, fig5i and fig5-fsrs reading (b) were run with `EP_distances.pkl`.
- **B3:** the legend's subcortical groups now include CA1 (cell 60). The 273 and 151 figures remain unprinted (section 2).
- **B4:** k-means stability was checked over 20 runs.
- **B6:** each recording has one cathodal contact for monopolar pulses (cell 4). The layer 5 reading takes the same trials, and the second run was added as a variant.
- **B11:** the ZETA text was corrected and each run's trial composition printed (cell 63). The jlh53concat problem was found and run as a variant.
- **B10, partly:** the pre-stimulus spread is now printed (cell 72).

**Remaining points that bear on a conclusion:**
- **N1, partial against not reproduced:** fig4f, fig5i, figs3e and fig6c are labelled inconsistently with fig5-fsrs (section 1).
- **B5, coordinates:** the dataset and the code disagree on the stimulation contact coordinates of jlh31 and jlh32. This alone decides fig4h-ks-distinct, the 25 µA mean of fig4h-distance-decreases, and the 5 µA RS fraction in fig4f and fig5i. Only the authors can settle it.
- **B9, fig6f:** the outcome rests on the code's peak rule against the criterion's literal text (section 1).
- **N2, fig4i:** the signed raw distance in reading (c) is unstated and unverified. Running the unsigned distance would settle it.
- **B10, fig6g:** at 5 µA the 0–20 ms rise (1.024) does not exceed the pre-stimulus maximum (1.079). The claimed rise "at 5, 25 and 50 µA" therefore stands out from baseline only at 25 and 50 µA. The criterion does not ask for this comparison, so the outcome stands; the notes now say so.
- **B11 remainder, fig6e:** the full Amplitude × Polarity × Region model is fitted only on the cached p-values. The outcome is partial either way.

**Not bearing on a conclusion:** B7 (fig4d's "across parameters") and B8 (fig5bc's lax "some assignment" clause) are claims-file questions; the record now asks them of a reader. B12 (figs9 under nDRP) and B13 (seven recordings) are stated in the notes.
