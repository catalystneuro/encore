## Round-2 verifier report: Peron et al. 2020 (CRCNS ssc-11), attempt peron-2020-01

Counts come from the files themselves. The claims file has 31 claims and the attempt record has 31 outcomes with the same IDs: 18 reproduced, 6 partially reproduced, 5 not reproduced, 2 blocked. Six outcomes are marked `assumed: true`, all of them model claims. Cell indices below are positions in the current notebook, counted from 0.

### 1. Outcomes

**The 24 data claims.** I agree with all 24 stated outcomes. The three where I disagreed in round 1 (touch-ablation-size, whisking-ablation-size, per-mouse-table) are now partially reproduced, which matches my round-1 outcomes. They rest on these outputs:
- **touch-ablation-size:** cell 19, rank rule 79.3 ± 27.1.
- **whisking-ablation-size:** 4.43% of the touch neurons per barrel column, and percentiles of 75.4 and 75.8.
- **per-mouse-table:** cell 69, 23 of 24 rows match under the Methods cylinder.

The other 21 are unchanged from round 1 and still agree with the printed numbers.

**Model claims.**

| Claim | Stated | My view |
|---|---|---|
| model-amplification-increases | reproduced (assumed) | **Agree.** Every 0.4 sweep strength (15–50) is below every 0.2 strength (150–400), so the direction does not depend on the calibration (cell 74). Reading (c) cannot be tested: 0.17 is more than the input-recipient share of 200/1,700 = 0.118, so the criterion's "under each reading" is met only for (a) and (b). |
| model-equal-connectivity-ablation-increases | not_reproduced (assumed) | **Do not agree as it stands.** The outcome depends on the attempt's own choice to count inhibitory neurons (about 250 of the 415 neurons per network, cell 80). With excitatory neurons only, scores rise in 30 of 30 networks (p = 1.9e-09), the claimed direction, with values outside tolerance. By the record's own rule for the Pconn 0.4 claim, that is partially reproduced. The printed counts argue against the all-neuron reading. The paper reports 3,466 and 3,779 neurons above 0.25. Here (cell 91) all neurons give 7,078 and 7,815, about twice that, and excitatory neurons give 4,058 and 4,327. |
| model-increased-connectivity-ablation-decreases | partially (assumed) | **Agree.** The decline holds under every reading (cell 80) and no reading gives values within tolerance. |
| model-all-or-none-robust | blocked, methods_underspecified | **Agree, with a note.** The extrapolation gives −9.8 and −12.0 (cell 74). The negative value comes from this attempt's calibration, an amplification of 7.7 to 10, which is far above the paper's Fig. 1c. The Methods also omit the matched strengths and the reset pulse, so the reason given is fair. |
| model-more-ablation-larger-decline | partially (assumed) | **Not settled.** The criterion is met under two readings (cell 85). Calibration (b), a claims-file reading, with all neurons and the 0-ablation networks left out gives R = −0.678 (p = 2e-13), with the decline growing at each size. Calibration (a) with excitatory neurons and the 0-ablation networks included gives −0.590. The record sets (b) aside because its KS minimum is the weakest strength tried. That is a reason to extend the sweep, not to drop the reading. |
| model-slow-input-sensitive | partially (assumed) | **Agree.** No reading gives both grand medians within tolerance; the closest is (b) set anew at 0.110 → 0.102 (cell 88). |
| model-response-similarity | not_reproduced (assumed) | **Agree.** It fails under every reading and population (cell 91). |

**Assumptions.** All are stated in the record and in cell 71.
- **Background PSP (0.39 / 1.4 mV):** fitted to the Methods' 0.5 and 10 Hz (cell 72). Reasonable.
- **Inhibitory PSP of −1 mV:** reasonable.
- **Input strength as the peak current:** reasonable.
- **Same noise in the run before and after ablation:** reasonable.
- **Calibration:**
  - Reading (b) is not actually determined. The KS minimum sits at the bottom edge of three of the four sweeps (touch input at 0.2 and 0.4, slow input at 0.4).
  - Reading (a) is weakly set at Pconn 0.2: the fraction above 0.1 moves only from 0.106 to 0.109 between strengths 200 and 225, with two networks per point. This affects how large the amplification is, not its direction.
- **Counting inhibitory neurons among the "all neurons" of the Methods:** stated, but contestable. It decides model-equal-connectivity, and the printed neuron counts favour excitatory-only.

### 2. Sentences the outputs do not support

- **Cell 18 (markdown):** the percentile text still reads "(1 when none exceeds it)". The output contradicts this: cell 19 gives 0.01 for a score above all 100 neurons. The record's response to round 1 says "the markdown is corrected"; only the docstring in cell 19 was changed.
- **Cell 0 and the README:** "the full pass takes about 17 minutes" and "(128 GB)". Cell 1 prints "streamed 16 archives in 648 s", about 11 minutes, and the archive sizes it prints add up to 120.9 GB.
- **Record finding ("77 GB of the 128 GB are ablation logs"):** 77.1 GB is the uncompressed size of the logs inside the archives. The uncompressed members total 166.7 GB (cell 4), and the 128 GB figure is compressed.
- **Cell 20:** "applied by the authors at targeting time, on other data". No output supports "other data".
- **Cell 38:** "about half the paper's". That holds only for the touch ablations. For whisking ablations it is 0.008 / 0.009 against 0.081 / 0.069 (cell 37), about a tenth.
- **Cell 94, Summary:**
  - "outcomes are the same under both [cylinders]" is false for per-mouse-table: 23 of 24 rows match under one rule and 24 of 24 under the other (cells 69–70).
  - "per-ablation score changes equal Extended Data Table 1" is too strong. Under the main reading, 23 of 24 rows match within 0.005, and several rows differ by 0.001–0.002 (cell 69).
- **Cell 93:** "encoding scores of the input-recipient neurons are about twice the paper's (0.55…)". The paper gives no score for input-recipient neurons. 0.55 is the median of excitatory neurons above 0.1 (cell 74), which is about 2.3 times the 0.237 grand median.
- **Record, response-similarity-touch-ablation:** "exactly the paper's values, with the point fit or the bin-mean fit". This holds only for the bin-mean fit. In cell 54, with the right-trial average and the code's cylinder, the point fit gives 4 of 9 whisking slopes negative with p = 1.000, and 2,824 touch neurons rather than 2,768.
- **Record finding (proximity question):** "this attempt adopted the code's rule for the table". This contradicts the per-mouse-table outcome and cell 70, which use the Methods cylinder as the main reading.

All other "**Result:**" sentences, the README table and the other notes agree with the printed numbers.

**Round-1 reasons in the record.** They are stated faithfully, in my own words. One note: for the seven model claims the record has `agrees: true, outcome: blocked`. My round-1 reason says the block had no allowed reason. The reason text carries that, but `agrees: true` alone understates it.

### 3. Round-1 points

**Resolved:**
- **B1:** the model was built and run.
- **B2:** the criterion's rank rule is now computed. Only the cell 18 markdown remains wrong (see section 2).
- **B3:** the trial-type order is printed for all 201 files (cell 51).
- **B4:** the missing trial averages for 278939 are stated (cells 55, 61).
- **B6:** touch-property lengths are checked against the event edges (cell 51).
- **B7:** the MAD definitions are compared (cell 37).
- **B8:** the NYU attempt logs are reconciled with the curation files (cell 66).
- **B9:** the 75-frame files are listed (cell 55), and no neuron with a NaN event rate is a member (cell 11).
- **B11:** the rank swap is shown (cell 41).
- **Archive members:** the full listing (cell 4) contains no histology.

**Still open, but stated and not bearing on a conclusion:**
- **B5:** the 50 ms burst rule.
- **Extended Data Table 1 transcription:** I could not check it; no PDF renderer was available.

**Remaining that bears on a conclusion:**
1. **Inhibitory neurons in the counted population.** This decides model-equal-connectivity-ablation-increases, and the printed neuron counts argue for counting excitatory neurons only.
2. **The (b) calibration sweep never brackets its minimum.** This bears on model-more-ablation-larger-decline, which meets its criterion under (b), and on model-slow-input-sensitive. It is also why (a) was adopted, so the (b) results should either be settled by a lower sweep or not be used to reject anything.
3. **Claims-file points referred to a reader** (my round-1 B10, the percentile rule, the rounded "approximately 4%", the right-trial-only average, paired against rank-sum tests). These bear on touch-ablation-size, whisking-ablation-size, behaviour-unchanged and the three response-similarity outcomes. They are correctly reported rather than corrected.
