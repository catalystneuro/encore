I worked through all eleven points in the verifier's round-1 report. One outcome changed: **tables3-oak-wmr-diameter** goes from reproduced to blocked (methods_underspecified). The final `python tools/entry.py all` passes with 0 errors (the notebook runs in 237 s), and nothing is committed.

**Why the one outcome changed (points B1 and B2).** The claims file does not say which group of contrasts the mixture-against-monoculture p-values are adjusted over. So I now run two readings:
- **A1:** each contrast tested alone, as before.
- **A2:** single-step adjustment over the model's eight treatment-and-year contrasts (four for the both-years contrast).

With A2, the one result that made this claim pass has p 0.16 (it was 0.023 under A1). That result also only lands within 1.4 ± 0.14 because S3 drops the negative increments: over all trees the difference is +1.69 under every reading. Since the claim holds only for one choice of two details the claims file does not fix, it is blocked until a reader answers. A2 changes no other outcome: it only raises p, and the absence claims stay blocked. Totals are now 14 reproduced, 3 partially, 7 not reproduced and 15 blocked.

**Other outputs I added, as the report asked:**
- **Phenology regressions, P1 refitted with a random intercept per treatment and year (B8):** two claims would not pass on this variant. In fig1cd-development-duration the oak slope has p 0.11, and in fig1-oak-steeper-advance the interaction has p 0.097. This variant is not a reading in the claims file, so both outcomes stay reproduced, and the notes now say each rests on P1 as the claims file gives it.
- **Table S6 F values against the paper's (B6):** the closest reading is 2020 and 2021, monocultures, both species pooled, marginal F tests (largest gap about 1.0). That is the reading under which the "no seasonal variation" absence holds, but nothing matches exactly, so the claim stays blocked.
- **How the dataset describes Growth_length, GDD and Chill_days (B3, fig2):** printed from Metadata.csv and the workbook's README sheet. Neither defines Growth_length, and the Dryad README.md describes no column.
- **Header table (B11):** it now shows only which claims are tested and which are blocked, with no outcomes.

**Three new questions** in `questions/dryad-4j0zpc8hz.yaml`:
1. Which group of contrasts the adjustment covers, and which trees the S3 difference is taken over.
2. Whether the claims file's reading of Eqs. 3 and 4 is right (B4). As read, the complementarity effect is always exactly twice the net biodiversity effect, and the selection effect is 0 by construction under one reading.
3. Whether fig1ij should use the deposited Growth_length or bud swelling to onset of senescence, as the criterion defines it.

**Updated text:** the notebook conclusions and summary, the record's notes and deviations, the entry README, and a `verifications` round 1 in the attempt record. That round has all 39 claims, each with `agrees: true`, the verifier's outcome, its reason, and my `response`.

**What I did not change, and why:**
- **fig1ij-growing-season stays reproduced, with the deposited column.** On the criterion's literal definition the claim would fail (slopes 1.09 and 2.16). The verifier accepted reproduced because the deposited column matches the paper's slopes within 0.04. The disagreement is in the notes, and question 3 asks a reader to settle it.
- **B5 and B7: no change.** B5 (Table S1 F tests) was already asked and answered in the first round of questions. B7 (campaign-level tests treated as independent) is a reading the claims file names, and the outcome is the same on yearly means.
- **B9: no change.** The data quirks were already recorded as findings or deviations.
