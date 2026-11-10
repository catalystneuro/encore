I ran steps 1 to 5 of the Author section and built the handover. The entry check passes with 0 errors. One part did not finish: the second reading of open detail (2), clipping each variable in place of dropping out-of-range bins, was stopped by a time limit and is not in the entry.

**1. Outcomes per claim**

| Claim | Outcome |
|---|---|
| headfixed-session-link (link claim I added) | reproduced |
| fig4f eye movement ranges | reproduced (8 of 8 values) |
| fig4j eye-encoding cells | reproduced (718 of 2861; paper 711), with folds in turn; random folds give 614 |
| fig4k conjunctive coding | reproduced |
| fig5a nasal/temporal | partially reproduced (all-cells test holds; the hemisphere tests can't be run) |
| fig5b up/down | reproduced |
| fig5 eye position stability | partially reproduced (Ev median out of tolerance) |
| fig5av Eh linear most stable | reproduced |
| fig5bv Ev low-order more stable | partially reproduced (tests hold, 1 of 2 required medians) |
| fig6 linear, nasal | partially reproduced (tests hold, counts high) |
| fig6 nonlinear, temporal | not reproduced |
| fig6 eye velocity stability | not reproduced (Ev dot is not less stable than body speed) |
| fig6v asymmetric more stable | partially reproduced (vertical part only) |
| fig7ab contributions | reproduced under reading (c) |
| fig7c model fit | reproduced (2140 cells, median 0.0513 in compute_llh.m's units) |
| fig7e no clustering | not reproduced (3 of 30 combinations give P < 0.005) |
| supp7e velocity extrema | partially reproduced (horizontal only) |
| 19 freely moving claims (Figs 1 to 3, supp3, supp4, supp5, supp9) | blocked, data_missing |
| fig8c, fig8e | blocked, data_missing (no no-landmark track) |
| methods-hemispheres-similar | blocked, metadata_insufficient |
| supp12 | blocked, too_large |

**2. What I found about the dataset**
- **No pitch or roll:** the open field files have none, so all freely moving claims are blocked. The paper put those data on figshare (Dataset 1).
- **Which head-fixed files are the paper's:** the dandiset holds 20 head-fixed files and doesn't say which are the paper's 11. I matched them through the paper's figshare deposit (Dataset 3) by subject, unit count and frame count. Behaviour and spikes in the matched files are identical to the deposit.
- **Broken spike index (format error):** in two files (npI3 0420, npI4 0421) the first unit's index entry wrapped at 2^16. Unit 0 is missing 65536 spikes and unit 1 starts with them. The helper detects this from the data and repairs it.
- **Wrong or missing metadata:** eye position is labelled metres and eye velocity "unknown"; the values are in % of eye width. Hemisphere is not recorded.
- **Duplicates:** 10 behaviour-only files repeat head-fixed sessions. Two probe insertions were each converted twice.
- **Gaps:** two sessions have timestamp gaps of up to 308 s, and npI3 0420 is missing 66% of its eye samples.
- **Assumption:** positive horizontal eye values are nasal and positive vertical values are upward. I took this from the Methods' shuffle-comparison section and the Supp. Fig. 4 axis labels. It only matters for the fig6 nasal and temporal claims.
- **Questions for the paper's authors** (recorded as a `methods_unavailable` finding):
  - How were the 10-s sections assigned to folds? In turn gives 718 eye cells, at random 614.
  - How was the contribution normalized? The literal wording ("subtracted from 1") inverts the paper's order of variables.
  - What rule separates symmetric from asymmetric velocity cells? Neither rule I ran gives the paper's 147 asymmetric Eh dot cells.
- **Question to a reader** (`questions/mallory-2021.yaml`): should the pitch and roll claims be `data: elsewhere`, pointing at figshare Dataset 1?

**3. Where the protocol was unclear, wrong or missing something**
1. Data that are public elsewhere but not marked `elsewhere` in the claims file have no fitting blocked reason, since `data_missing` means "not public anywhere". I used `data_missing` and asked a reader.
2. The rule "a claim that depends on a blocked claim is blocked" blocked the Cohort 2 head-velocity count, which could have been tested. I followed the rule.
3. The protocol has no place for deciding which files are the paper's sessions. I added a link claim marked `with_labels`, and added `depends_on` to fig4f and fig4j. This edits the claims file beyond adding the link claim, though no statement, expected value or criterion changed.
4. Several criteria name no partial outcome (fig5bv, supp7e). I used `partially_reproduced` where the effect held in part.
5. The conclusions have to be written after the run, but the run is the costly step and can't be repeated in time. I added the "**Result:**" markdown cells to both the source and the executed notebooks after execution. No code changed.
6. The protocol doesn't say how a run longer than the tool's 2-hour command limit should be done. Running everything in the foreground lost the third notebook.

**4. Runtime and failures**
- `entry.py all`: the main notebook took 47.7 min and the random-folds notebook 35.4 min.
- The clipping notebook was still running when the command hit the 2-hour limit, and was killed. I removed it from the entry and recorded that reading as not run. `result.json` was never written.
- Peak memory was 3.9 GB. About 2 hours went on fitting speed (an exact Newton fit sharing per-fold Hessians), the gap binning, and the index repair.

Nothing was committed.
