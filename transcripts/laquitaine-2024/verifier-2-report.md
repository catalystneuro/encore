**Verifier report, round 2: Laquitaine et al. (doi:10.1101/2024.12.04.626805) on DANDI:001250 v0.251012.1648**

The claims file has 39 claims, and the attempt record has 39 outcomes covering the same IDs: 7 reproduced, 6 partially reproduced, 11 not reproduced, 15 blocked. No outcome carries `assumed: true`.

### 1. Outcomes

**I agree with these without reservation:**
- **ground-truth-neuron-counts** (not reproduced).
- **fitted-trace-maximal-amplitude** (reproduced). It is no longer fragile: over 600 s under reading (a), NS is 331.1 against a bound of 324.9 (cell 18).
- **fig2m, fig2np, supp2, fig3e, fig3c** (as recorded).
- **fig2q** (not reproduced). Over 600 s, all four models are outside their in vivo ranges (cell 27).
- **fig2r** (not reproduced) and **fig2s** (partially reproduced, the alpha part fails).
- **fig3fg** (not reproduced). NS gives 7 to 12 clusters across every seed and variant. M gives 6 under the main reading but 5 under two variants. The outcome turns on NS, so it is robust (cell 42).
- **fig4a-yield, supp4, supp6, fig6gh** (all not reproduced).
- **fig5cd** (reproduced).
- **fig5a-dense-probe-more-multi-units** (reproduced). DS lacks depth 1, but the result is robust. The paper's DS has 562 units against 481 here, so depth 1 adds about 81. Even if all or none of them were single units, NS against DS gives p ≥ 0.12 on the code's test (my calculation from the counts in cell 45).
- **All 15 blocked outcomes.** For fig6c-f, the criterion's partial outcome requires the sign of spatial extent, which cannot be computed, so blocked is correct.

**These outcomes rest on assumptions that are not flagged:**
- **E is the paper's evoked recording.** This decides fig4a-lognormal (not reproduced) and fig5a-evoked-more-units (not reproduced), and it is also behind fig4-median, fig4bc and fig5cd.
  - The criteria say to run both evoked recordings. For fig5a-evoked the criterion says "the claim holds under either", so a failure on E alone does not rule out E40, which has no sorting.
  - The evidence for E is strong. The E sorting matches E's ground truth (250 units reach 0.5) and not E40's (0 units) (cell 8). The deposited E also reproduces the code's printed 0.655.
  - So the assumption is reasonable, but it should be marked `assumed: true`, and the notes should say that E40 cannot be tested.
- **"Partial" used for "the tested parts hold, the rest cannot be tested".** This applies to fig4-median, fig4bc, fig5a-single-unit-fraction-differs, fig5a-single-unit-counts and fig5b. The criteria do not provide for it:
  - fig4-median, fig5a-fraction and fig5a-counts name no partial outcome.
  - fig4bc defines partial as "medians or variances part alone". Here both hold and the S part cannot be tested.
  - fig5b's second part holds under reading (b), so the only thing stopping a full reproduction is DS's theoretical yield. The notes do not say this.
  - In fig5a-fraction, the only computable fraction reading, (i), fails (0.354). Reading (iii), which the paper's own counts favour, needs NS-2X.
  - In fig5a-counts, both tests are substitutes:
    - M against NS is run two-way, while the criterion's test is three-way with NS-2X.
    - H against DS uses an incomplete DS. It gives p = 0.061, but 0.024 as deposited, which is below 0.05 and would make the claim not reproduced.

  I accept "partial" only if this convention is stated as an assumption. Otherwise these claims are blocked for their missing parts.

### 2. Statements the outputs do not support

- **Attempt record, fig6gh notes:** "The measured values are … the largest interneuron ratio of Kilosort 1 to 2.5 with the 1-hour sortings", with measured 8.07.
  - Cell 89 prints Kilosort2.5 over 1 hour at 9.978 (INH L4 cSTUT, 1 unit), so the largest is 9.98.
  - Cell 90's list, "8.07 … 4.12 … 4.01 and 2.90", leaves out that ratio and the 10-minute Kilosort ratio of 13.3 (324 of 17 L5 cNAC). Both are outside 2.6 to 8.9.
  - The interneuron part still holds ("at least one" sorter qualifies), and the outcome is unchanged.
- **Attempt record, fig3e notes:** "one electrode within 25 um and one in each 25 um band to 100 um."
  - Cell 39 shows no electrode in 25–50 µm under reading (i).
  - Under reading (ii) there is none within 25 µm (the nearest is at 25.5).
- **The DS3 lag scan is described as covering more than it does.** Cell 8 scans lags for Kilosort4 only; the other sorters get only the 0 and 50 ms check. Yet these places generalise to all sortings or all sorters:
  - The round-1 response for fig6-dense says "The clock check now covers every sorter and a scan of lags … against all three dense probe ground truths".
  - The finding and fig6-dense notes say "the depth 3 sortings match none … at any lag".
  - The Summary (cell 96) and cell 9 say the same.
- **fig5a-single-unit-counts, attempt record notes and cell 66:** "the fractions do not differ on the code's test (… H against DS p = 0.061)". That p is on depths 2 and 3 only, and as deposited it is 0.024 (cell 65), so "do not differ" is not established.
- **Cell 93:** "its weights are close to those of the identified refit". In the evoked fit, synapse class is 0.40 against 0.23, and bAC is +0.08 against −0.03 (cell 92). This is minor.
- **Cell 78 (method text):** it says the tags are "computed among the single units". The code (cell 79) and cell 80 compute them over every sorted unit, so this text is stale.
- Everything else checks against the printed outputs: the other "**Result:**" sentences, the Summary table, the README counts (24 tested: 7 / 6 / 11; 15 blocked) and the other notes.
- **My round-1 reasons** are given faithfully in my own words. Several have the matching problem text from my report added (fig3fg, supp4, fig5a-fraction, fig5a-evoked, fig5cd, fig6-dense, fig6c-f, fig6gh). The `agrees: false` entries match my three disagreements.

### 3. Round-1 points

**Resolved:**
- Problem 1: the maxima and ANR extremes are now taken over 600 s.
- Problem 2: the DS part of fig5a-counts is now called incomplete, and the dense-probe claim is robust (above).
- Problem 3: the DS3 caveat is stated, apart from the overstatement above.
- Problem 4: the Kilosort2 sorting of E ends at 240.0 s and is now scored over 240 s.
- Problems 5 to 10: the `qualify_units` fix (Kilosort4 numbers unchanged), the whole-file silent count (0), the removed print, the "for those that differ" rule, the printed "within: False", and WaveMap now using the nearest sites.
- Problem 11: the 19-feature model is run.
- Problem 13: recorded as a finding.
- What I could not check before: the first and last spike of every sorting are printed; the filter matches SpikeInterface's to 1.4e-5 µV (cell 13); the E sorting belongs to the 1-hour recording.

**Remaining, bearing on a conclusion:**
1. The assumption that E is the evoked recording (problem 12) decides fig4a-lognormal and fig5a-evoked and is not flagged. A reader has been asked, but the outcomes should carry `assumed: true`.
2. The partial-for-untestable convention behind fig4-median, fig4bc, fig5a-fraction, fig5a-counts and fig5b needs to be stated, or those claims reclassified as blocked. For fig5a-counts, the H against DS test is also undetermined (0.061 against 0.024).

**Possible misreading in the claims file (reported, not corrected):** For Figs 4 and 5, the claims file treats the evoked recording as open and describes the code's "npx_evoked" config as 10 minutes. The deposit points to the first 10 minutes of the 1-hour recording (cell 8; the 0.655 match). "10 minutes" there may mean the sorting duration, not E40.
