Both questions led a reader to amend a claim. I re-ran both claims as amended, and both go from partially reproduced to reproduced. No other claim depended on what changed.

**1. fig4b-shared-down-sets** (earlier: partially reproduced, now: reproduced)
- **What the answer changed:** the criterion now has a new reading (a) for "36": the sets significant in both treatments, in either direction (the Venn intersect). The two old readings are kept as (b) and (c). The expected value of 2 and the rule "within 10% of 36 under one reading" did not change.
- **Result:** exactly 2 sets are down-regulated in both treatments, organelle inner membrane and mitochondrial inner membrane. Under reading (a) the count is 36, the paper's number. Readings (b) and (c) give 122 and 646, which is why the claim was only partially reproduced before.

**2. fig4fgh-chronic-up** (earlier: partially reproduced, measured 101 / 321 / 133; now: reproduced, measured 82 / 314 / 128)
- **What the answer changed:** the statement now says the heatmaps hold the 82, 308 and 128 sets. The criterion now has two readings: (a) all chronic-OA sets with positive NES, and (b) those sets that are not down-regulated under acute-OA, which is what the deposited script passes to simplifyEnrichment. A pass under one reading is enough. Expected values and the named families did not change.
- **Result:** reading (b) gives 82 cellular component (CC), 314 biological process (BP) and 128 molecular function (MF) sets, all within tolerance. Reading (a) still gives 101 CC, which is outside 82 ± 8.2. Under both readings, all 10 named families have at least one up-regulated term.

**What I updated:**
- **Notebook:** both sections now print the count under each reading, with a within-tolerance check. The fig4fgh section also matches the families under each reading. I rewrote both "**Result: ...**" conclusions and the two rows of the summary table.
- **README:** the outcome table now lists Fig. 4B and Fig. 4F to 4H as reproduced. Only the PCA (Fig. 4A) remains partially reproduced.
- **Record (`attempts/allen-2026-01.yaml`):** both outcomes, their measured values and notes are updated. Each claim's notes say what the reader's answer changed and what the outcome was under the earlier readings. In the fig4fgh deviation I added that reading (b) counts the sets passed to simplifyEnrichment, since its filter cannot be run here.

**Checks:** `lock` passed, and the lock file did not change. `all` reported 0 errors, and the notebook passed in 75 s. The executed numbers match the conclusions above. I ran `handover`, which wrote `executed/allen-2026/handover/`. I did not verify my own work, and I did not commit or push.

The changes to `tools/build_site.py` and `tools/site_assets/list.js` were already in the working tree when I started, and I left them alone.
