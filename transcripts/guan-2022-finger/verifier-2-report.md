**Verifier report, round 2: Guan et al. 2022, DANDI:000252 @ 0.230408.2207**

Counts come from the claims file and the attempt record. The claims file has 19 claims. The record has 19 outcomes: 11 tested and 8 blocked (data_missing).

### 1. Outcomes and assumptions

I agree with all 19 outcomes in the record.

| Claim | Outcome | Agree | Note |
|---|---|---|---|
| tenfinger-recording-counts | reproduced | yes | Counted before the exclusion (cell 10), which is one of the criterion's readings, so no assumption is needed. |
| tenfinger-pooled-npcc-neurons | reproduced | yes | 1114 against 1111 ± 111. |
| tenfinger-discriminative-fraction | not_reproduced | yes | Robust. The uncorrected p < 0.05 shares are 56.1 / 46.5 / 68.8% (cell 13). N-PPC and J-PPC are below their bounds (59.4 / 51.3%) even with no correction, so no FDR choice can reach the paper's values. |
| tenfinger-decoding-accuracy | reproduced | yes | |
| tenfinger-error-structure | reproduced | yes | |
| fig8b-matching-closer | reproduced, `assumed: true` | yes | The assumption (precision of the partition mean, ×5) is stated in the deviations, in cell 19 and in the Summary. It is reasonable, because rsatoolbox documents that input for a list of noises. It is also the only reading that matches the paper's magnitudes, and that dependence is disclosed. |
| fig8a-npcc-index-distinct | reproduced | yes | Holds in all 18 readings. |
| fig8e-hand-ccgp | reproduced | yes | The result is the same under both populations for the standard accuracy, so it needs no assumption. |
| fig8e-finger-ccgp | reproduced | yes | Passes under O9 (b), which is a claims-file reading, so it needs no assumption. |
| jppc-finger-ccgp-low | partially_reproduced, `assumed: true` | yes | See below. |
| figs11-jppc-lower-matched-size | reproduced | yes | Now holds in all 8 readings. |
| 8 blocked claims | blocked (data_missing) | yes | Cell 36: every file is the ten-finger task, with no No-Go condition and no decoder-output column. |

**The jppc-finger-ccgp-low assumption** (standard accuracy computed on the same pseudo-population as the CCGP) is stated in the record, in cell 27 and in the Summary.
- **For it:** the Methods say "We pooled neurons across sessions … into a pseudo-population … Standard, within-condition decoding accuracy provided an upper bound on CCGP." Also, the N-PPC CCGP exceeds the per-session accuracy (ratio 1.15–1.31).
- **Against it:** the paper's 65% is matched by the per-session within-hand accuracy (0.680–0.690). The pseudo-population gives 0.828–0.890 (cell 29).
- **My view:** the choice is defensible, but calling it "the better-supported choice" (record and cell 31) is a judgement call. The other population gives "reproduced" (cell 29, row 16), and the record says so.
- **Whichever population is used,** the outcome rests on one reading of eight (O1 b / O6 a / SVM), where p sits at the 1/1002 floor.

### 2. Sentences the printed outputs do not support

- **Record, tenfinger-decoding-accuracy notes:** "with shuffled labels per-session accuracies are 0.07 to 0.17." Cell 7 prints a minimum of 0.04 (P1 2015-08-14) and also 0.06 several times. The range is 0.04–0.17. This does not affect the outcome.
- **Cell 14, and the record's tenfinger-discriminative-fraction notes:** "FDR per session gives no more." Cell 13 shows the per-session FDR mean is slightly higher than pooled FDR in some rows: N-PPC none 40.7 vs 40.4, J-PPC none 37.9 vs 37.6, J-PPC a 38.4 vs 38.1. The J-PPC value of 38.4 also exceeds the stated maximum of 38.1. The differences are at most 0.3 points, and the outcome is unaffected.
- **README:** "It takes about fourteen minutes." Cell 36 prints "notebook run time so far: 8.3 min", and that is the last code cell.
- **Summary (cell 37) and the record's fig6-online-bmi notes and data_missing finding**, on what DANDI:000147 contains ("10 files of subject P1 from 2018 … BCI finger-press task … cites the eLife paper of ref 46"). No notebook cell prints this. Cell 3 prints only the `dcite:Continues DANDI:000147` relation. The statement may be true, but nothing in the notebook backs it.
- **Minor, not a sentence:** cell 21 prints "N-PPC mean RDM range 0.00 to 3.90", but cell 22 and the text give 0.57–3.90. The 0.00 apparently comes from the diagonal. The text uses the correct off-diagonal figure.

I checked every other number in the "**Result:**" cells (11, 14, 18, 23, 26, 31, 34), the Summary, the README table and the record's notes against cells 10, 13, 16, 20–22, 25, 28, 29 and 33. All of them agree. This includes the 1 s window (60.8 / 56.8 / 82.9%), the sweep maxima (47.8 / 43.5 / 72.2%), the RDM ranges, the synthetic ratios (5.17 / 1.03), the null counts (0–37), and the ratio and accuracy ranges.

**The verifications block** states my round-1 reasons accurately. It includes the 5.46× synthetic figure, the window-sweep request, the request for null counts, and the 000147 remark, all as I gave them. Its statement that my round-1 outcomes all agree with the record is correct.

**Claims file:**
- Its readings match the paper, except for one point. The Methods say BH corrects "for m = N … neurons for each participant", but the criterion of tenfinger-discriminative-fraction corrects J-PPC and J-MC separately. Its justification comes from legends of the alternating-cues task. This departs from the Methods' wording, but it cannot change the outcome, because even uncorrected p fails.
- The O4 (a) gap I raised in round 1 is still there: the criterion does not mention the noise scaling.
- O11 (Go window only) is a fair reading of "Except when otherwise specified, … 500-millisecond window".

### 3. Round-1 points

**Resolved:**
- **Problem 2:** the per-session accuracy is now run under every O1 × O7 combination, next to every O6 row (cell 29).
- **Problem 5:** figs11 is now run under O1 b.
- **Problem 6:** the unused `Psh` is removed.
- **Problem 7:** cell 11 now notes that the counts are before the exclusion while the analyses use the excluded units.
- **Section C:**
  - The exact null counts are printed, so p = 1/1002 is confirmed.
  - The window sweep was run.
  - DANDI:000147 was checked according to the record, though the notebook prints none of it.
- **Problem 4:** stated, not fixed. It does not bear on a conclusion.

**Still open, bearing on a conclusion:**
1. **fig8b-matching-closer magnitude (problem 1).** "Reproduced" depends on the ×5 precision-of-the-mean scaling. Without it the result is partially reproduced (N-PPC 0.28–0.36 against 1.56). This is properly flagged as `assumed: true` and as a question for the authors. The paper's text cannot settle it.
2. **jppc-finger-ccgp-low (problems 2 and 3).** The outcome changes with the population used for the standard accuracy: partially reproduced on the pseudo-population, reproduced per session. Under either population, p < 0.001 holds in only one of eight readings, where 0 of 1001 null values reach the CCGP. The other readings have p = 0.002–0.038, so the claimed significance is fragile.
3. **tenfinger-discriminative-fraction.** A 1 s window from the Go cue brings all three arrays within tolerance (cell 13). The outcome correctly stays not_reproduced under O11. Which window and test the paper actually used remains an open question for the authors, and it is the likely explanation of the gap.
