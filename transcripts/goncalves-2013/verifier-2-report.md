**Verifier report, round 2: Goncalves et al. 2013 (doi:10.1038/nn.3415), CRCNS ssc-8**

The claims file has 28 claims, and the attempt record gives an outcome for each of the 28. Of the 11 tested claims, 5 are reproduced, 3 partially reproduced and 3 not reproduced. The other 17 are blocked: 16 by data_missing and 1 by metadata_insufficient. Cell indices below are those of the re-executed notebook.

### 1. Outcomes and assumptions

I agree with all 28 outcomes.

- **group-sizes: not reproduced.** Agree (cell 11).
- **fig1d: partially reproduced.** Agree (cells 14–15). The criterion has no partial outcome; my reasoning is unchanged from round 1. The new test on the 16 mice with all three bins gives the same pattern.
- **fig1e: reproduced.** Agree (cell 18).
- **genotype-pooled-ages and pearson-genotype: partially reproduced.** Agree (cells 21, 24).
- **fig1ef: not reproduced.** Agree (cells 27–28). Student p is 0.057, and the variance tests now printed support using Student's test.
- **p30-40-no-difference: reproduced.** Agree (cell 31).
- **fig2b: reproduced.** Agree (cell 34). All six readings give p ≥ 0.13.
- **fig2c: not reproduced.** Agree (cell 37). All twelve readings give p ≥ 0.052. The seed caveat in section 3 applies.
- **imaging-firing-rate and unanesthetized-p14-16-values: reproduced.** Agree (cells 40, 43).
- **The 17 blocked claims.** Agree. suppl4a is now metadata_insufficient, with data_missing named as also possible, as I suggested.

**Assumptions (`assumed: true`).** Four outcomes carry the flag: fig1d, genotype-pooled-ages, pearson-genotype and fig1ef. Each assumes that the outcome under the deposited rates (T-a) also holds for the paper's trace. The assumption is stated in each claim's deviations. It is reasonable, because T-a reproduces the paper's P14-16 values and its P30-40 WT value. It carries most weight for fig1ef, where p = 0.057 sits next to the threshold, and the notes say the result is fragile. unanesthetized-p14-16-values rests on reading the rates as Hz (U-a). It is not flagged, but it needs no flag: the criterion accepts one reading of rate unit, and the notes say the argument for U-a is partly circular.

### 2. Sentences the outputs do not support

- **Cell 35 (fig2b conclusion):** "does not differ between genotypes under any of the four readings (p = 0.13 to 0.64)". There are now six readings, and cell 34 gives p = 0.82 and 0.96 for the two new R-b/U-b readings, so the range is 0.13 to 0.96. The same paragraph then reports those 0.82 and 0.96 values itself.
- **Attempt record, fig2b notes:** "No reading finds a difference (p = 0.13 to 0.64)." This is the same stale range; it should be 0.13 to 0.96.
- **Attempt record, findings, methods_unavailable (peaks of synchrony):** "every reading gives proportions above the paper's 0.300 and 0.380". This is false. In cell 37, R-b (rates in Hz) with Q-a gives WT 0.133–0.141 and KO 0.170–0.171, which are below the paper's values.
- **Cell 22 (genotype-pooled-ages conclusion):** "those over mice (0.024 to 0.030) are not". For this claim the per-mouse s.e.m. in cell 21 are 0.024 and 0.026 for pairs under 100 µm, and 0.021–0.026 over all readings. 0.030 is the Pearson value from cell 24, carried over from my round-1 range, which covered both claims. The attempt record's "0.024 and 0.026" is correct.
- **Attempt record, fig1ef notes:** "so it is not largest at P14-16; as a ratio it is (1.21 against 1.17 and 1.13)". The word "largest" is missing. Cell 29 has the intended sentence, which also marks the ratio as a variant the criterion does not use; the record omits that.
- **Outside the scope of this check, cell 13 (markdown before fig1d):** "Six mice (P9-11) have no pairs over 200 um, or few". Cell 15 shows 5 mice with none, 1 at P9-11 and 4 at P14-16, and only a few P9-11 mice with under 50 such pairs.

Everything else checks out against the outputs:
- the other "**Result:**" paragraphs (cells 12, 16, 19, 25, 29, 32, 38, 41, 44, 47);
- the Summary (cell 48), including its tables and the "How the analysis differs" and "What was found" paragraphs;
- the README;
- the rest of the attempt record's notes and findings.

**My round-1 reasons in the attempt record.** The `verifications` results restate my round-1 reasons accurately and in my own terms. Each of problems 1–7 and each item of section C is attached to the right claim or to `reviewed`. Nothing is misattributed or overstated.

### 3. Round-1 points

**Resolved:**
1. **R-b with rates per frame (rate ≥ 1).** Now run for fig2b and fig2c (cells 34, 37). The outcomes stand.
2. **Rate unit.** The unit-signature check was run (cell 4). The values do not show the unit, and cell 5 and the notes now say that the choice of Hz is partly circular.
3. **Student versus Welch for fig1ef.** The variance tests, per-mouse values and leave-one-out p values are printed (cell 28), and the fragility is stated.
4. **fig1d bin over 200 µm.** The pair counts are printed, and the post hoc on the 16 mice with all three bins is added (cell 15).
5. **Mean of the age means (M-b).** The point is now stated in cells 22 and 25 and in the notes.
6. **suppl4a variant.** It is restricted to the 2160-frame recordings, with the brightness-step ratio of each printed (cell 46). KO entry 4, at 1.08, is marginal, but the variant decides nothing.
7. **Process.** The Summary now has a cell of its own (cell 48).

From section C:
- The per-mouse P14-16 values are now printed.
- Which mice differ from the paper cannot be resolved without metadata the data set lacks; the record says so.
- T-b and cross-correlation at the peak lag were not run, with stated reasons. Both lie outside the claims file.

**What remains that bears on a conclusion:**
- **fig2c seed sensitivity (new).** Under R-b/U-b with Q-a, p = 0.052 (S-a) and 0.053 (S-b). These thresholds come from 100 seeded shuffles, and only one seed per reading was run. If another seed gave p < 0.05 with KO higher, the test would hold. Both means are outside tolerance, so the outcome would then be partially reproduced, not not reproduced. Re-running this reading over several seeds would settle it.
- **fig1ef fragility.** It is stated, but it cannot be resolved. The outcome depends on p = 0.057, on the one WT P14-16 mouse that is missing from the data set, and on the assumption that T-a stands for the paper's trace.
- **The fig2b p range (cell 35, attempt record notes) and the false sentence in the findings.** Both need correcting. They do not change any outcome.
