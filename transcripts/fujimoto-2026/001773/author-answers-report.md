There was one question, and its answer changed one claim's outcome basis and one blocked claim's wording. The entry is locked, checked (0 errors) and ran clean from a fresh environment in 24 s. The handover is in `executed/001773-fujimoto-2026/handover/`. I did not verify my own work, and nothing is committed or pushed.

## Question: `fig4b-roi-changes-counts` (questions/001773.yaml)

I asked whether the criterion should include the test and threshold from the paper's Fig. 4 script. The script runs a rank-sum of each ROI's changes against zeros and counts an ROI at P < 0.05/123. I also asked whether "of the 122 ROIs" was right, given that the deposited connectomes have 123 ROIs.

**What the answer changed.** The reader said yes to both and amended the claim:
- The criterion now judges only the script's test, with the diagonal excluded and P < 0.05/123.
- The Methods' threshold (P < 0.01 Bonferroni), the pre-against-post rank-sum and the signed-rank test are kept as reported variants. They no longer decide the outcome.
- The statement and the header now say 123 ROIs, and so does the criterion of `fig4c-network-sorted-reduction`.
- The expected counts (69 and 44) did not change.

**What I updated.**
- **Notebook:** the fig4b section quotes the amended statement and describes the new criterion and the variants. It now prints the judged count against the tolerance and the thresholds. The Result line and the summary row now say "reproduced", without "resting on an assumption".
- **README:** the matching row no longer has the qualifier.
- **Attempt record:** `assumed: true` and the assumption deviation are removed, and both claims' notes say what the answer changed. I kept the `code_mismatch` finding, because the Methods' "P < 0.01" still disagrees with the script.

## Outcome per affected claim

| Claim | Earlier outcome | Outcome now |
|---|---|---|
| fig4b-roi-changes-counts | reproduced, resting on an assumption (`assumed: true`) | reproduced, no longer resting on an assumption: 69 (DBS) and 44 (controls), both within tolerance |
| fig4c-network-sorted-reduction | blocked (methods_underspecified) | blocked (methods_underspecified), unchanged: going from 122 to 123 ROIs does not give the ROIs network labels |

For fig4b, the largest P counted as significant is 3.88e-04 in both groups, which matches the 3.9e-4 in Supplementary Tables 1 and 2. None of the variants puts both counts in tolerance:

| Variant | DBS (target 62.1 to 75.9) | Controls (target 39.6 to 48.4) |
|---|---|---|
| Same test at the Methods' 0.01/123 | 62 | 36 |
| Pre-against-post rank-sum | 10 to 44 | 4 to 15 |
| Signed-rank of the changes | 60 to 85 | 27 to 49 |

No other claim was affected, and its outcome did not change. The executed notebook's numbers for `fig4-nonsurgical-no-pattern` are unchanged, including the controls' count of 44.
