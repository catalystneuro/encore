**Round-2 verification: Chaunsali et al. 2025 (doi:10.1002/alz.70813), DANDI:001702 0.260216.2323**

The claims file has 51 claims, and the attempt record gives 51 outcomes: 45 blocked, 1 partially reproduced, 5 reproduced. The notebook summary table, cell 43, adds up to the same 51.

**1. Outcomes**

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| 22 IHC claims (Figs 1, 3B, 3G, 5I, 5 M PNNs, S1 to S6, S9) | blocked, data_missing | yes | Cell 3: 0 of 481 NWB files hold any data object. |
| 19 behaviour claims | blocked, metadata_insufficient | yes | Cells 6 to 8. |
| fig4a-7m-social-memory-deficit | blocked, data_missing | yes | |
| fig4b-3m-degs | blocked, methods_underspecified | yes | Cell 13: reproduced, not reproduced, partially reproduced and not reproduced across the four readings, at both alphas. |
| fig4c-7m-degs | partially_reproduced | yes | Cell 16: under all four readings and both alphas, up is 284 to 320 and down is 0 to 7. None is within 6 ± 0.6. |
| fig4d-3m-go-memory-terms-down | blocked, methods_underspecified | yes | Cell 21: 2, 5 and 9 readings. The readings disagree even within one term-size limit (10 to 500: 3,3,0,0,1,2,1,1; none: 0,0,0,0,1,0,0,0), so the size choice doesn't decide the outcome. |
| fig4e-7m-go-immune-terms-up | reproduced | yes | Cell 24: 5 to 8 terms in all 16 readings; minimum top-10 z is 4.47. |
| fig4fg-ecm-go-terms | blocked, methods_underspecified | yes, with a caveat | Cell 27: 15 readings give not reproduced and 1 gives partially reproduced (0.048). See the note below. |
| fig4h-pnn-synthesis-genes | reproduced | yes | Cell 32: 6 of 6 under every reading. |
| fig4i-3m-remodeling-genes-up | reproduced | yes | Cell 35: 13 of 13 positive. |
| fig4i-7m-remodeling-genes-up | reproduced | yes | Cell 38: 7 of 7 positive. |
| fig4i-common-and-7m-vs-3m-up | reproduced | yes | Cell 41: 12 of 12 positive. |

**Assumptions:** no outcome in the attempt record is marked `assumed: true`. The fig4fg outcome still rests on one choice: running the GO term-size limit as a reading. The claims file's criterion lists only backgrounds (a) and (b), and its READINGS rule covers readings the criterion lists.
- With the 10 to 500 limit only, all 8 readings give not reproduced.
- With no size limit, the readings disagree.

The choice is stated as a deviation and is reasonable, since the paper names no enrichment tool. It is the change I asked for in round 1. But it is an extension of the claims file, and the record should mark it `assumed: true`.

The deciding value, 0.048, also comes from the pydeseq2 shrunken reading. That reading stands in for R's apeglm and was never compared with R.

**2. Statements the printed numbers don't support**

- **Cell 14 (fig4b conclusion):**
  - "With one model per contrast and unshrunken fold changes the counts are 95 up and 136 down". Cell 13 prints 98 and 137 at alpha 0.1.
  - "With shrunken fold changes they are 88 and 45 (separate)". Cell 13 prints 91 and 45.
  - "Filtering at pydeseq2's alpha 0.05 gives 98 and 137 for the separate unshrunken reading". This implies the alpha 0.1 count differs, but cell 13 prints 98 and 137 under both alphas.
  - The per-reading outcomes are unaffected.
- **The same wrong numbers elsewhere:**
  - Record, fig4b notes: "gives 95 up and 136 down" and "shrunken fold changes give 88 and 45 (separate)".
  - Record, fig4b round-1 response: "the separate unshrunken counts become 95 and 136".
  - Record, methods_unavailable finding: "One model per age reproduces 95 and 136 at 3 M".
  - README: "With one model per age and unshrunken fold changes the 3 M DEG counts are 95 and 136".
- **Cell 36 and the record's fig4i-3m notes:** "only Mmp2 in the separate model has adjusted p below 0.05 (0.038)". Cell 35 prints 0.0389, which rounds to 0.039.
- **Cell 22:** "Without a size limit, larger terms such as synaptic signalling fill the top 10". The no-limit top 10s in cell 21 are filled by broad terms such as "behavior", "system process", "G protein-coupled receptor signaling pathway" and "regulation of biological quality". "synaptic signaling" (453 genes) appears only in the 10 to 500 lists. The count stated in the same sentence ("no reading has more than one") is correct.
- **Record, fig4h notes:** "no PNN gene listed in the notebook is a DEG at either age". Cell 32 checks the 12 PNN genes under reading (b)(c) only. For the six named genes, the record's "None of the six is a DEG" holds under every reading.

Everything else matches the printed outputs: all other "Result:" sentences, the cell 43 summary, the rest of the README, and the record's notes.

**Round-1 reasons in the record:** they reproduce my round-1 table text and outcomes faithfully, including agrees: false for fig4b and fig4d and not_reproduced for fig4fg. The `reviewed` paragraph summarises my remaining points correctly. It does not mention the second half of round-1 problem 5: the fig4c down-count tolerance of 0.6 requires exactly 6 genes.

**3. Round-1 points**

Resolved:
- **Problem 1:** cell 10 now applies the READINGS rule, and each claim prints the outcome under every reading.
- **Problem 2 (alpha):** the code now uses alpha 0.1 (`FILTER_ALPHA`, passed to `DeseqStats`), with 0.05 shown as a variant, and no outcome changes.
- **Problem 3:** the term-size limit is now run as a reading under both limits.
- **Problem 4:** the possible misreading is sent to a reader, and the claim is tested as written.
- **Problem 6:** recorded as a finding.
- **Section C:**
  - Every top-10 list is now printed, with each term marked as matching the pattern or not.
  - Per-reading outcome tables are now printed.
  - The decoded-card table was declined with a stated reason. I accept that, since the scored times are missing either way.

Remaining, bearing on a conclusion:
- **The wrong 3 M DEG numbers:** 95/136 and 88/45 appear in cell 14, the README, the fig4b notes and response, and the methods_unavailable finding. They must be corrected to 98/137 and 91/45. The outcome itself stands.
- **fig4fg depends on one marginal reading:**
  - The blocked outcome depends on a single reading: separate model, pydeseq2 shrinkage, all annotated genes as background, no size limit, adjusted p 0.048.
  - That reading uses the unverified pydeseq2-for-apeglm substitution and the GO release choice.
  - With R's apeglm or another GO release, it could fall above 0.05, and the outcome would become not_reproduced.
  - The record should mark the term-size reading `assumed: true` and say how marginal the deciding value is.
- **No comparison with R DESeq2:** still not done. It cannot change fig4b, fig4d or fig4c, because the readings either disagree widely or are uniformly off. It can change fig4fg, as above.

Not bearing on a conclusion: the Mmp2 rounding, the cell 22 wording, the fig4h "PNN genes" scope, and the fig4c tolerance point from round-1 problem 5.
