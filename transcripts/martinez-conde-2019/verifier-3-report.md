**Verifier report, round 3: martinez-conde-2019-02**

The claims file has 19 claims and the attempt record has 19 outcomes. Two of those outcomes have a proposed change, table1-edge and table1-s90. I reviewed only those two.

| Claim | Proposed outcome | Agree? | My outcome | Reason |
|---|---|---|---|---|
| table1-edge | partially reproduced (now not reproduced) | No | not reproduced | See below |
| table1-s90 | partially reproduced (now not reproduced) | No | not reproduced | See below |

**The numbers are correct.** They come from the data, and the criterion is applied as written.
- **table1-edge, centred squares (cell 54):** reading (a) puts 3 of 5 values within tolerance (maximum 30.24, mean 17.31, midpoint 19.10), and reading (b) also puts 3 of 5 (mean, median, midpoint).
- **table1-s90, centred squares, reading (a), halves (i) (cell 60):** 3 of 5 (maximum 13.80, mean 7.84, median 7.90). The mean is 1.38 from 9.22 with tolerance 1.61, and the median is 1.41 from 9.31 with tolerance 1.62.
- **The "nearest" reading (cell 87)** gives the same values. Cell 88 is right that no other outcome changes under it.
- **How the placement was chosen:** the rule picks, for each stimulus, the placement that agrees better with `BaseActivity` (cell 27). It does not look at the Table 1 results. Taking the centred squares for every stimulus also gives 3 of 5 for both claims (cell 87), so choosing per stimulus is not what produces the change.
- **The criterion:** the baseline placement is an assumption, not one of the criterion's readings. Under the centred squares, "at least three of five under one reading" holds, so the rule itself is applied correctly.

**Why I disagree.** The case for the centred squares is no stronger than the case for the squares inside the corners, and the paper's text slightly favours inside. A change of outcome needs a reason that clearly outweighs the current one.

1. **The paper says the baseline was measured inside the ROIs.** Results, "Strength of neuronal responses", paragraph 1: "We also calculated the neuron's baseline activity inside the ROIs". The Fig 2 legend calls the baseline frames "1x1 DVA ROIs". For Square and Edge, the centred squares are up to 19% outside the ROI, and the inside squares are entirely within it (cells 25 and 26).
   - In round 2 I called the ROI-border reason weak, because I had only the Methods sentence to go on. This sentence, which neither the record nor I cited, is direct textual support for the inside placement. The record has also removed the ROI-border reason from the helper, notebook and record.
2. **The `BaseActivity` evidence points both ways under the same wording.** The Methods say "at the corners of the circumscribing square" for both Square and Edge and Star.
   - For Star, `BaseActivity` favours the inside squares: 8 of 10 files, p = 0.020 (cell 27).
   - For Square and Edge, the evidence for centred rests on 9 files: 7 of 9, p = 0.027. That p-value is uncorrected across the two stimuli tested; Bonferroni over two tests gives about 0.054.
   - So `BaseActivity` does not settle which reading of "at the corners of" the authors used.
3. **`BaseActivity` itself, the record's own evidence, gives not reproduced** for both claims (cells 54 and 60):
   - Edge: 0 of 5.
   - S90: at most 2 of 5.

   This is on 9 neurons only.
4. **The proposal adds no new data or analysis.** It weights the same two placements that in round 2 I called a toss-up. Point 1 tips that balance slightly toward inside.

The record and README already say that these two outcomes depend on the placement of the squares and give the centred result. That disclosure is enough; I would keep the outcomes as they are.

**Claims file:** I found no misreading of the paper. The paper gives the circumscribing square as 8.84 DVA, which is 141 DU at 16 DU per DVA, but writes 138 DU. That inconsistency is in the paper itself and does not affect either outcome.
