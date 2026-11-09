**Verifier report, round 2: Namima et al. 2025 on DANDI:001357 (0.261006.2007)**

The claims file has 27 claims and the attempt record has 27 outcomes: 10 reproduced, 3 partially reproduced, 8 not reproduced and 6 blocked. I did not download the data or re-run the notebook; all checks are against the printed outputs and the helper module. Cell indices below are those of the current notebook.

### 1. Outcomes and assumptions

**Outcomes.** I agree with all 27 stated outcomes. The two that changed after round 1 now follow their criteria:
- **ex-m1p12-no-cluster** is not reproduced. Cell 35 gives 4 neurons with a significant intercept (1 positive, 3 negative), and the criterion allows at most 2. The partial rule needs that count to hold.
- **pop-significant-isimilarity** is not reproduced. The criterion has no partial rule, and no reading in cell 41 matches.

Four outcomes carry conditions:
- **ex-m2p6-invariance** and **pop-recording-density** match only under reliability reading (a):
  - ex-m2p6-invariance: 22 under (b), outside 19 ± 1.9 (cell 32).
  - pop-recording-density: r = 0.296–0.336 under (b), outside 0.236 ± 0.024 (cell 62).
  - The criterion accepts either reading, so the outcomes stand, and the notes say so.
  - In round 1 I wrote that each such claim "also has a match under (b) or another reading". That was wrong for these two.
- **pop-contrast-invariance** matches only under reliability (b) with unreliable values counted as 0 (cell 50).
- **position-examples-invariant** is not reproduced only under the claims file's 10% rule, which makes the files' p12 the M2p9 session (see section 3, point 5).

**Assumptions.** No outcome carries `assumed: true`. One should:
- **position-optimal-consistent** rests on the inferred aggregate RF centre, and that is not marked as an assumption.
  - The criterion needs every reading to give r > 0 with p < 0.0001.
  - With file position 4 as the centre under reliability (a), r = 0.279 with p = 2.1e-4, which fails (cell 80).
  - So "reproduced" assumes the centre is not position 4. That is reasonable but unverifiable, since the files do not label the centre.

The other choices the outcomes rest on are claims-file readings, or were shown not to matter:
- the spindle `stim_ID`: all 15 were tried (cell 68);
- the five suspect texture files: leaving them out changes no outcome (cells 71, 74, 77).

### 2. Sentences the printed numbers do not support

- **Cell 19:** "Most neurons without a line under (b) are in small penetrations, where few other neurons exist."
  - Nothing printed supports this, and the outputs contradict it.
  - Cell 18 shows 100.0% of finite shape-pair intervals are reliable under (b).
  - Cell 41 shows only one penetration has fewer than 6 neurons.
  - So most of the 64 neurons without a line must come from undefined (NaN) similarities: `nc_corr` returns NaN when the bias-corrected variance is ≤ 0. They cannot come from small penetrations.
- **Cell 84 and the record's notes for position-examples-invariant:** "M2p28 (the files' p28) fails both readings".
  - The cell 83 table and the cell's own last sentence show reading (a) holds for p28 with position 0 as the centre under reliability (b).
- **Cell 84 and the record:** "the claim fails on M2p28 whichever session is M2p9".
  - This is true only of reading (b).
  - With p09 as M2p9, position 0 as the centre and reliability (b), reading (a) holds for both penetrations while (b) fails (cell 83 table). The criterion calls that case "blocked", not "not reproduced".
- **Cell 84 and the record:** "With the files' label p09 for M2p9 … both readings hold for M2p9".
  - Under reliability (a), reading (a) holds only with position 1 as the centre (cell 83 table).
- **Record notes, position-optimal-consistent:** "so every reading gives a positive r and one is within tolerance".
  - This leaves out the criterion's p < 0.0001 condition, which position 4 under (a) fails (p = 2.1e-4, cell 80).
- **Record notes, pop-dark-bright-consistent:** "either contrast 1,847 neurons with a line, the paper's n".
  - The paper's 1,847 is the count with a line at both contrasts (cell 17).
  - Under (b) the both-contrast count is 1,757 (cell 18), so the match is to a different quantity.
- **Record finding (metadata_insufficient):** "The penetration with the largest population response is position 1 in 12 files".
  - This is a wording slip: it should say the position with the largest response.
- **Cell 69 and the record:** "horizontal … (0 to 500 um)".
  - The horizontal bins are 0–5, which cover 0–599 µm (cell 68). This is minor.

All other "**Result:" sentences, the Summary, the README and the record's notes agree with the outputs. That includes:
- the "about a third" reduction with shared noise subtracted (31–39%, cell 21);
- 152 of 159 files passing the clock check (cell 10);
- the README's run time: the files load in 233 s, and the analyses take about 100 s more.

**My round-1 reasons** are stated in my words. Some have clauses added from my round-1 problem list, which are fair paraphrases. However, their cell numbers are from the round-1 notebook, which has since shifted (for example, round-1 cell 13 is now cell 15, and 17 is now 26). A reader following them will land on the wrong cells.

### 3. Round-1 points

**Resolved**
- **2.** The five texture files have a variant without them, and no outcome changes.
- **3.** ex-m1p12-no-cluster now uses the two-sided count.
- **4 (mostly).** Every position is now tried as the centre under both reliability readings.
- **6.** The bootstrap caveat is stated in the deviations.
- **7.** There is now a shared-noise variant, and it flips no outcome.
- **8.** The minimum of 4 neurons per penetration is stated.
- **10.** The data-model limits are in the findings.
- **C.** These checks are now in the notebook:
  - the `cond_ID` cross-tabulation (cell 8);
  - the full column lists (cell 8);
  - the reliability leniency table (cell 18);
  - the position variants (cells 80 and 83).

**Remaining, bearing on a conclusion**
- **1, reliability reading.**
  - ex-m2p6-invariance and pop-recording-density are reproduced only under (a), which the paper's own counts argue against. The question to a reader is open.
  - The new evidence in cell 18 also weakens the argument for (b): the 64 shape neurons without a line under (b) come from undefined similarities, not from the reliability rule. So the gap to the paper's 2 points to a difference in the estimator or its NaN handling, not only to the reading.
- **4, position centre.** position-optimal-consistent rests on the centre not being position 4. It should be marked `assumed: true`, and the notes should state the p condition.
- **5, M2p9.** Under the claims file's rule, plus the reader's answer, the outcome is not reproduced. Two caveats remain:
  - With p09 as M2p9 (the files' label) and position 0 as the centre under reliability (b), the readings disagree and the criterion gives "blocked".
  - For p12 under reliability (a), reading (a) fails because only 0–1 of 120 pairs are reliable. That is a non-test, not evidence that the patterns differ.
- **C, shape source.** The three shape-image blocks (orientation-sf-isimilarity, apc-peaks-sparse-clustering, apc-example-m2p51) rest on the author's search for a public, pinned copy of the Pasupathy & Connor shapes. The record lists where it looked, but no new search was run and I have not verified it.
