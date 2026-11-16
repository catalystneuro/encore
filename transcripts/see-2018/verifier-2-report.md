**Round 2 verification: See et al. 2018 (doi:10.7554/elife.35587) on CRCNS ac-3, attempt see-2018-01**

The claims file has 31 claims and the attempt record has 31 outcomes with the same IDs: 14 reproduced, 2 partially reproduced, 10 not reproduced and 5 blocked by missing data. I agree with 30 of them. The exception is fig10c. Its stated p-values, and those of fig10b, do not match the re-executed notebook. In this run the fig10c criterion is not met under any reading.

## 1. Outcomes

| Claim | Record | Agree? | Note |
|---|---|---|---|
| fig2bd, fig2eg, fig4s3, fig5a, fig6-member, fig7b, fig7-negative-weights, fig7c, fig7f, fig11d | not_reproduced | yes | Each follows from its printed output. For fig5a, the held-out check (cell 65) shows the miss does not come from in-sample MI bias. |
| fig4, fig4s2, fig5b, fig5c, fig7-totals, fig7a, fig7d, fig10b, fig11c | reproduced | yes | fig10b passes under all four readings in this run (p 8.0e-12 to 5.6e-4, cell 76), although the stated p-values are wrong (section 2). |
| fig10s1 | reproduced | yes | Passes with 500 groups (PTD p 3.7e-4). The PTD part fails with 100 groups on one other seed (p 0.0023, cell 82), which the notes say. |
| fig6j, fig11ef | partially_reproduced | yes | |
| fig8, fig9c, fig9s1, fig9s2, fig11ab | blocked (data_missing) | yes | |
| fig6c | reproduced, assumed | yes, changed from round 1 | The assumption (STRF PWC made non-negative by subtracting its minimum) is stated. It is reasonable: two more readings, absolute value (iii) and overlap-normalised (iv, which removes the taper I raised), agree. Rejecting clipping (i) rests on the paper's description of STRF PWCs as "broad". Both criterion parts pass under (ii) to (iv): 58.4 to 76.2% of cNE pairs, MWU p ≤ 1.1e-39 (cell 54). |
| fig7e | reproduced, assumed | yes | The assumption is the claims file's choice of test. It is stated and reasonable. |
| fig11s3b | reproduced, assumed | yes | The 5-ms PR bin is stated and reasonable. The notes also report that 10-ms bins fail (0.645). |
| fig10c | reproduced, assumed | **no** | In this execution the linear projection with event reading (a) gives p = 0.00153 (cell 79), above the 0.001 bound. The other three readings give 0.0076, 0.049 and 0.185, so none passes. Across all five subsampling draws, the reading passes in 2 (cell 79 prints `'linear, a': 2` for the four extra seeds). The held-out MI passes clearly (p ≤ 1.6e-8), but the criterion asks for the in-sample MI. On the printed output the outcome is not_reproduced. Choosing the linear projection because it is the reading that passes is also a weak basis for the assumption. |

## 2. Sentences the printed numbers do not support

These cells and record notes appear to have been written from an earlier execution:

- **Cell 77 and the fig10b record note:** "signed-rank p = 3.5e-12 … 1.9e-09 … 5.0e-04 … 1.3e-05". Cell 76 prints 8.01e-12, 3.75e-09, 0.000559 and 2.43e-05. The outcome holds.
- **Cell 80 and the fig10c record note:**
  - "only the linear projection with event reading (a) reaches p < 0.001 (p = 6.4e-04); the others give 0.0098 …, 0.044 … and 0.15". Cell 79 prints 0.00153, 0.00757, 0.0485 and 0.185.
  - "with four other seeds the linear (a) reading gives p = 4.2e-06, 0.012, 0.0029 and 4.9e-06, so it passes in 3 of 5 draws". Cell 79 prints 7.7e-06, 0.0012, 0.0036 and 1.5e-05, which is 2 of 5.
  - "59 to 65% of pairs, p = 2.2e-15 to 6.7e-08". Cell 79 prints 59.7 to 63.1% and p = 2.67e-14 to 1.6e-08.
- **Summary (cell 99), README and record:** "fig10c … reproduced, resting on an assumption (linear projection; 3 of 5 draws)" and "cNE STRFs have a higher MI than members' | Reproduced (on an assumption)" are not supported, for the reasons above.
- **The record's response to my fig10c reason:** "this run 6.4e-4". The re-executed notebook gives 1.53e-3. That is the same value as the author's first run, so the result changes from one execution to the next with fixed seeds. The record does not mention this.
- **Cell 66 and the fig5a record note:** "0.074 bits against 0.073 at 8 to 15 ms". Cell 65 prints 0.075 at 5 ms against 0.072 to 0.074. "2857 or 3362 at 2 ms": cell 65 prints 3360. "0.059 to 0.082 bits": the printed range is 0.058 to 0.082. "a tenth to a fifth as large" holds roughly for reading (a). Under (b) the ratio runs from about 0.04 to 0.27. None of these change the outcome.
- **Cell 55 and the fig6c record note:** "p = 2.0e-76". Cell 54 prints 2.43e-76. This is minor.
- **fig11c record note:** "a sampled run reproduces the real 5-ms covariances (… slope 0.66 to 1.04)". The covariance slopes are 0.657 at site 1 and 0.712 at site 16 (cell 86), so the DG sample under-reproduces covariances by about a third there. "Reproduces" overstates this. The outcome does not depend on it.

Everything else in the conclusions, the summary, the README and the record notes matches the outputs.

The verification block states my round-1 reasons accurately and in my own terms. It includes the fig6c and fig10c disagreements, and it folds in the relevant problems from my round-1 list and the "not checked" items.

## 3. Round-1 points

**Resolved:**
- Point 1, PWC sharpness scale: the mismatch is stated, variants are added and it is raised as a finding.
- Point 2, fig6j pair set: the both-members variant gives the same 14 and 12 of 16. I still think the claims file probably misreads the paper's non-cNE pair set. The record now raises this as a question for a reader.
- Point 3, fig6c: covered by readings (iii) and (iv).
- Point 4, fig5a: the held-out MI and the distinct-bin counts are added.
- Points 6 to 11: point 7 now uses 500 groups, point 10 now uses stimulus-period spikes, and the rest are stated.
- Section C checks: the DG fit, the PR spikes dropped and the ICA iteration counts are all printed now.

**Still open, and bearing on a conclusion:**
- **fig10c (round-1 point 5, now worse).** The printed run fails the criterion. The result also depends on the execution, not only on the seed. Either change the outcome to not_reproduced, or find and remove the source of the run-to-run variation and rewrite cells 77, 80 and 99, the README and the record against a single execution.
- **fig10b.** The outcome is unaffected, but its stated p-values must be replaced with the printed ones.
- **fig6c and fig6-member.** Spike PWC sharpness on the raw ±50 ms histogram remains off the paper's scale (12 ms against about 2). The fig6c comparison is therefore between two measures that are both off scale. The record states this as a question for the authors. It is a caveat on fig6c, not a reason to change its outcome.
