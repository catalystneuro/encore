I've worked through every point in the round-2 report. No outcome changed and nothing is under `proposed`. The verifier agreed with all 48 outcomes, and I found nothing that should change. The counts stay at 23 reproduced, 7 partially reproduced, 11 not reproduced and 7 blocked. The final `python tools/entry.py all entries/crcns-ear-1-farrell-2020` run passes with 0 errors, and its numbers are the same as before.

**Sentences the verifier said the outputs don't support, now corrected:**
- **fig3a-xe991-fit (cell 59 and the record):** the "all 20 cells" values come from 18 fitted cells, because y-1 leaves out the same bin. The comparison against CL - 4.82 pF now gives both bin-edge readings: 0.0432 V is outside, and 0.0538 V and 0.0498 V are within. It also says that comparison decides nothing. The record now says the outcome rests entirely on the dVmin limit.
- **fig4d-cleq-two-limits (cell 86 and the record):** two of the three upper groups are single cells (1.29 and 1.02 aF); the third has 9 cells (0.83 aF). The text also says the outcome sits on a knife-edge.
- **Summary (cell 105):** it now says only the Fig. S4 fit without XE991 comes within tolerance, since the R2 of the XE991 fit fails. The cell count now reads "17 against 15" (Table 1), dropping the wrong "15 or 16".
- **README:** the partially reproduced row now says why each Table 1 claim is partial. For table1-pigmented-no-xe991 that is p = 0.0010, not < 0.0001.

**Added or clarified:**
- **New output in cell 85:** the number of cells behind each C_Leq limit, and the limits from groups of two or more cells only. The lower limit stays at 0.6496 aF; the upper drops to 0.834 aF, which is outside.
- **mean-slope-half:** the conclusion and notes now say the criterion's own reading gives −0.402 (not reproduced). The reading under which fig3a-eq3a-fit passes would give −0.432, which is within tolerance.
- **two-hyperpolarized-states:** the text now says that under y-1 no tier of the criterion fits. Partial is kept as a judgement, and the record notes that the round-1 judgement was made when the C_Leq limits still passed.
- **y-1 deviation (every claim that uses it):** it now says the dVmin limit is not in the claims file and that it decides four outcomes. It also explains why the limit applies to bins and not cells: in Fig. S4 the two are the same, and for Fig. 3a the paper does not say. The cell-level version would fail fig3a-eq3a-fit (Vd 0.0299 V). The fig3a-eq3a-fit notes say the same.
- **figs1-example-cell:** the deviation and conclusion now say the outcome does not rest on the assumed CLn rule, because the other reading gives 26.69 pF, also within tolerance. So I did not add an `assumed` flag.
- **Round 2 under `verifications`:** recorded for all 48 claims, with the verifier's reasons in its own words and my response to each.

**Not done:**
- **No question added to `questions/crcns-ear-1.yaml`:** the verifier reported the y-1 limit as a method detail missing from the claims file, not as a place where the claims file misreads the paper.
- **Two points stay open, stated in the record:**
  - Round-1 point B4: the plateau fraction was chosen to give 62 cells, and the SD of the capacitance difference is 2.42 pF against the paper's 1.32 pF. I found no rule in the paper to replace it, so it stays an assumption.
  - The stereocilia capacitance rule from Corbitt et al. (2012) still can't be checked against that paper's constants.
- **Left alone:** `tools/runner/run_requests.py` was already modified before this run started; I didn't touch it. Nothing was committed, as the workflow does that.
