# Round 3 verifier report: Wei et al. 2023 on DANDI:000021 (version 0.251116.2246)

The claims file has 49 claims and the attempt record has 49 outcomes. Two outcomes carry a `proposed` change: figs3b-fs-faster and figs5-depth-distribution. I reviewed only those two.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| figs3b-fs-faster | not_reproduced | **Yes** | — | See (1) below. |
| figs5-depth-distribution | partially_reproduced | **No** | reproduced, with `assumed: true` | See (2) below. |

**(1) figs3b-fs-faster: I agree with not reproduced.**
- **The numbers come from the data.** Rates are spike count over time, computed by the helper (`wei2023.py:707-710`). The first 5-min gray-screen rate equals the code's `fr_5min` for all 618 units in the code's tables (cell 6, median difference 0.0000 Hz).
- **No choice was made to reach the result.** Cell 20 prints every period reading under all three isolation readings, plus the Source Data labels.
- **The criterion's only outcome clause is not met.** It needs both medians within tolerance (FS 4.365–5.335 Hz, RS 1.845–2.255 Hz) under one reading, with Mann-Whitney p < 0.001. No row of cell 20 does this:
  - (c) first 5 min: FS 4.50 Hz is in tolerance, RS 2.38 Hz is not.
  - (a) all gray screen: FS 5.04 Hz is in, RS 1.40 Hz is not.
  - (b) whole session: RS 2.07 Hz is in, FS 5.36 Hz is not.
  - Source Data labels, first 5-min gray screen: FS 4.55 Hz is in, RS 2.50 Hz is not.
- **The direction holds everywhere.** FS is faster under every reading (p from 1.3e-05 to 2.3e-64), but the criterion has no partial clause that this could satisfy.

**(2) figs5-depth-distribution: I disagree with partially reproduced. I would give reproduced, with `assumed: true`.**
- **The depth method follows the criterion.** The helper takes the second spatial derivative of the flash-averaged VISp LFP and puts the layer 4 centre at the earliest sink, i.e. the first channel to reach half the minimum within 0–150 ms (`wei2023.py:760-784`).
- **The test is run under the attempt's usual rule.** The attempt decides all downstream claims on its own reading (c) clusters, and it fixed that rule before this claim. With the depth above, the Kruskal-Wallis test across the six clusters gives:
  - p = 0.044 under reading (c);
  - p = 0.011 under reading (a);
  - p = 2.0e-08 under reading (b).
- **That meets the criterion as written:** "Reproduced when it gives p < 0.05" (cell 41). The record's own notes say so too.
- **The criterion has no partial clause.** "The effect holds in part" is not one of its outcomes. The record's reason for figs3b is that the criterion decides and has no partial clause; that reason applies equally here, so proposing partial for figs5 is inconsistent with it.
- **Same treatment as the sibling claims.** fig6a-fs1-symmetric and figs4-fs-spread-absent are also recorded as reproduced on the clusters found here with FS forced to K = 3, while the Source Data labels give a weaker result. I agreed with both in round 2.
- **The outcome is fragile, which is why `assumed: true` must stay.** It rests on:
  - FS forced to K = 3;
  - a CSD centre that has not been validated. It differs from the code's centre by -420 to +340 µm per probe, and one probe's first sink is at 83 ms (cell 41).
- **The other variants all fail (cell 41):**
  - the paper's own labels on the same depth give p = 0.36;
  - the code's per-probe centre gives p = 0.25 (reading c), 0.29 (reading a) and 0.34 (Source Data labels).
- **The other defensible reading is not reproduced.** If "the six clusters" is read as the paper's own clusters, i.e. the Source Data labels, the outcome is not reproduced, not partial.
- **A further gap.** The helper also computes a second CSD centre, the position of the CSD minimum (`depth_csd_min`), but cell 41 never runs the test on it.
- **This changes my round-2 view.** In round 2 I proposed partially reproduced here. I now hold to the rule I applied to figs3b: the criterion decides the outcome, and it gives no partial clause.

I found no place where the claims file misreads the paper on these two claims.
