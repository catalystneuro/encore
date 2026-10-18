**Round 2 verification: Schwab et al. 2020 on dandiset 000947**

I saved the paper text (JATS XML and a text extract) and `Fig5_S14.m` (from Zenodo record 4000719) under `paper/`. Cell numbers below are from the re-executed notebook. Round-1 cell numbers are 6 lower.

**1. Outcomes**

The claims file lists 21 claims, and the attempt record gives 21 outcomes: 7 reproduced, 4 partially reproduced, 7 not reproduced, 3 blocked. I agree with all 21.

- **unit-link, table1-unit-counts, table1-rest-rate, table1-ap-width, mvt-responsive-fraction, increases-most-common, monophasic-more-in-vla, integrated-change-positive, fig3a, fig3c, gating-conflict-fraction, directional-units, fig4-ccf-rare, fig4-noise-corr-rare, and the three blocked claims:** I agree. Each follows from its criterion and the printed numbers.
- **hold-period-ramps (partially reproduced):** I agree. The criterion defines no partial outcome, and the record says so.
- **fig3b (reproduced):** I agree under the criterion. It is fragile: the GPi median of −29.5 ms is 0.2 ms inside its tolerance, and Isis alone gives p = 0.055. With the paper's records the GPi median is −36 ms, which is also outside tolerance (cell 53).
- **behavior-rt-mt (now reproduced, was partially reproduced):** I agree. It is the defensible file set, since the test uses the files that hold the analysed units. The reaction-time animal effect still depends on which files are used:

  | Files | Animal effect p |
  |---|---|
  | 165 files with analysed units | 0.89 |
  | 162 files of the paper's records | 0.053 |
  | all 250 files | 1.1e-4 |
  | trials pooled | 2.5e-59 |

  The paper's F[1,452] implies about 456 observations, and none of these sets matches that.
- **fig5-vla-decrease-after-gpi-bursts (not reproduced):** I agree under the criterion, but it is weak evidence because the burst detector does not match the paper's (bursts of 67 ms here against 24 ms).

**2. Sentences the numbers do not support**

- **README and Summary (cell 84) undercount the outcomes that depend on unit selection.**
  - README: "two outcomes (monophasic responses, Fig 3A) would differ with it". Cell 84: "With the paper's list, monophasic-more-in-vla and fig3a-vla-leads-gpi would meet their criteria, so those two outcomes depend on the selection".
  - Two more outcomes would change with the paper's records:
    - hold-period-ramps would be reproduced: 99.5% and 98.8%, slope p = 0.187 (cell 35).
    - fig3b would be partially reproduced: GPi −36 ms is outside −29.7 to −24.3 (cell 53).
  - Cell 84 also says only that the fig3b GPi median "leaves its tolerance" with one record per presumed neuron. It leaves it with the paper's records too.
- **Cell 54** says the GPi median "is outside its tolerance" only for the per-neuron variants. It does not say that the paper's-records median (−36 ms) is also outside. The fig3b notes in the attempt record have the same gap.
- **README:** "It takes about 13 minutes". Cell 83 prints 14.0 min.
- **Cell 4:** "the post-MPTP files name a different preprint". Only pre-MPTP files are loaded and printed.
- **Cell 4 and the format_error finding:** that I-160616-4 has "no curated units" (and "no raw data") is not printed for that file. Only its missing trials table is printed (cell 3).
- **Attempt record data_missing finding:** "for example G-140813-2 … their sorted clusters are in processing/ecephys/units, which has no channel or sort letter". No output shows this.
- **Attempt record metadata_insufficient finding:** "as the column description says". The column description is never printed; only the notebook's own label "z ventral positive" appears (cell 80).

Every other sentence in the Result cells, the Summary, the README table and the attempt-record notes matches the printed outputs. I spot-checked every number. The paper-sourced numbers I checked against the paper match: Table 1 latencies of −76 and −95.5 ms, 11.6% significant burst-onset pairs, 24 and 195 ms burst and pause durations, and the F[1,452] interaction p = 0.002. `Fig5_S14.m` loads `Data_Fig5` and plots it, with no burst detector, as the record says.

**My reasons in the attempt record:** they are stated in my own words, nearly verbatim, with the relevant problems attached. Three small gaps:
- Problem 3 (pseudo-replication) is not attached to fig4-ccf-rare, although I named the CCF movement p = 0.045.
- Problem 1 (detector chance level) is not attached to increases-most-common, although I said it weakens the form claims.
- The reasons cite round-1 cell numbers, which no longer match this notebook.

**3. Round-1 points**

Resolved:
- **1:** the chance level is measured on the real data (cell 20).
- **2:** the slope test's chance level on the real data is 98.4% and 99.0%.
- **3:** variants with one record per presumed neuron and one value per presumed neuron are added.
- **4:** the c0 ≤ 0.3 variant, the lags of significant peaks, and the same-sample count (11,376 against 11,435 expected) are added.
- **5:** detrended counts and per-pair-target shuffles are added; the excess remains.
- **7:** the behaviour test now uses the files of the analysed units.
- **8:** spike times are on the sample grid.
- **11, 12, 13, 14:** disclosed or added.
- **9, 10:** acceptably left as they are.

What remains that bears on a conclusion:
- **Decrease detector (fig3c, fig3a, increases-most-common):** chance is now measured but not corrected for. With random alignment, 33.7% of VLa unit-directions have a decrease, against 44.2% in the data, and chance onsets fall at −8 ms. The detector also finds more decreases than the paper's stored output (330 against 286). Part of the fig3c failure, and VLa's −67 ms in fig3a, may come from the method, not the data.
- **fig5:** the burst detector still does not match the paper's (67.1 against 24 ms). The per-pair test runs at chance (47–48%). More than half the pairs, 157 of 307, are excluded as noisy, and the conclusion does not report this. The not-reproduced outcome therefore says little about the paper.
- **Pair claims (fig4-ccf-rare, fig4-noise-corr-rare, fig5):** none has a paper's-records variant, although the claims file promises one for every claim. Pair counts also differ from the paper's (338 here against 427 for the whole-recording CCF), with no explanation.
- **behavior-rt-mt:** the reaction-time animal effect depends on the file set (paper's files p = 0.053), and the paper's 452 degrees of freedom are not reproduced by any file set.
- **hold-period-ramps and fig3b:** both outcomes depend on unit selection, and the README and Summary do not say so (see section 2).
