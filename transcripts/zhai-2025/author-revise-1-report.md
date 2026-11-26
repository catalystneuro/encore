No outcome changed in this revision. The entry re-ran cleanly with `python tools/entry.py all entries/zhai-2025` (0 errors, 396 s), and every conclusion, note and finding now uses the new numbers. The attempt record passes its schema check, and I recorded round 1 under `verifications` for all 45 claims.

**Fixes for the verifier's problems**
1. **Dendritic background bug:** fixed. `_site_trace` now subtracts 55 from red and 161 from green. The effect is small, and every dendritic outcome stays the same:
   - link-dendritic-cells still has a median difference of 0.027.
   - fig1i-sch: P goes from 0.079 to 0.066, still not reproduced. Without the 2019-04-11 cell it is 0.027; the conclusion now says this exclusion only shows where the difference comes from.
   - fig3f-sul stays at P = 0.0545.
   - fig1i-on P = 0.0058, fig3f-on 0.0073, fig6d 0.023, fig7f KO 0.31.
2. **Last-sweep variant:** it now really takes the last sweep (`per_cell_somatic(keep="last")`). A per-cell table of the 14 cells with a repeated step shows no rheobase changes and only one cell's summed spikes changes, by 1. So the rheobase claims of absence come out the same under it.
3. **fig4h sweeps:** I added two readings, the last 10 sweeps (P = 0.064) and the 10 consecutive sweeps whose count is nearest the paper's for each cell (P = 0.064). Only the first 10 sweeps gives P = 0.049.
   - I kept **reproduced**, marked as resting on the nearest-run reading, which the paper's own per-cell counts support, and recorded the disagreement.
   - The verifier would give partially reproduced. I did not use that, because a claim of absence is judged only by whether the paper's test finds the difference.
4. **Somatic link:** now reports that 9 paper rows are the best match for 20 cells, 6 cells tie between rows, and the rheobase and F-I sheets agree row by row in 115 of 124 rows.
5. **GRAB link:**
   - Counted per mouse, 1 of 11 match; with a one-to-one assignment of regions, 15 of 34.
   - The frame interval is the same within every condition (0.1996 s), so one interval per condition is safe.
   - The notebook now lists the trials of 2024-04-02 Slice1Roi2. The conflict with the dandiset description is stated in the finding; the files cannot settle it.
6. **Figure 6D letters:** the paper's identifiers follow the files' cell numbers (all 16 found). Reading the letter as the cell's place among the group's cells finds 14 of 16. I kept the cell number and wrote a deviation saying why.
7. **Other added outputs:**
   - fig8bc on the 18 mice that are also in the paper: still reproduced.
   - fig7e with an unpaired test: KO P = 0.89, close to the paper's 0.91.
   - The group labels of each Zenodo sheet: "-M1R" is MCI-Park with M1R deletion, 9 mice.
   - One spine file per cell type and group, opened: image stacks only, nothing under processing or analysis.
8. **Claims-file question:** the link-grab-rois criterion says "mouse" where the paper's unit is the region. I added this as a question in `questions/zhai-2025.yaml` and did not change the claim.

**Not done, and why**
- **Blocked reasons:** I kept `not_runnable` for the six spine claims. The verifier suggested `other` for the five 2PLSM claims and `data_missing` for fig4k. The protocol gives `not_runnable` when the paper's software (AutoQuant, NeuronStudio, Imaris) cannot run here, and does not allow `data_missing` for data that are public elsewhere. I recorded this under each claim's `response`.
- **Event detector:** it stays a stand-in for TaroTools, stated as an assumption. The verifier marked this as not affecting a conclusion.
- **Paper listing:** the paper should also be listed on Zenodo record 17260198 (`ZENODO:17260198`), the authors' raw-data deposit. It holds the confocal spine images, and I did not use it because counting them needs Imaris.

Nothing was committed.
