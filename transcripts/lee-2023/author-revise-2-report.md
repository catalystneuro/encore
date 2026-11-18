I made the round-2 revision. No outcome changes in this round. Four outcome changes are proposed for a third verification round, and the entry was re-run with `python tools/entry.py all entries/lee-2023`. Both notebooks pass (40 and 34 minutes), and `check` reports 0 errors.

**Proposed outcome changes (the verified outcome stays; each change is under `proposed`):**
- **fig2b-ephys-umap-subclasses**: partially reproduced → blocked (`methods_underspecified`). The only failing part passes once the paper's values for the 19 features public IPFX doesn't compute are added. That is the same reason figs2b is blocked.
- **fig5d-dbc-morph-umap**: partially reproduced → not reproduced, marked `assumed: true`. The criterion has no partial case. The assumption is that the SST population excludes SST FRZB (`Revised_subclass_label`). The paper supports this: "This assignment has been applied for subclass-level analyses." Under that label the UMAP fails on all five seeds. Under `subclass_label` the claim would hold, and that result is shown as a variant. The verifier offered blocked as the other option.
- **figs8b-firing-differs-pvalb2-only**: partially reproduced → blocked (`methods_underspecified`), because its two firing-rate readings disagree.
- **figs9-species-differences-not-culture**: partially reproduced → blocked. The verifier agreed with partially reproduced and did not ask for this. I propose it because figs9 depends on figs8b, and the protocol blocks a claim that depends on a blocked one. Its failing part (width) does not depend on the rate reading.

**UMAP numbers changed in the re-run.** With the same seeds and lock file, the UMAP results differ from the earlier run, which was on another machine. Two runs on this machine gave identical outputs. Feature-space and other non-UMAP results did not change, and no outcome moved. The largest shift was fig5d-dbc-ephys, whose UMAP ratio at the claim's seed went from 2.34 to 1.56. I rewrote every UMAP number in the conclusions and notes to the new outputs. Both summaries now say UMAP numbers can differ between machines. The fig1h numbers the verifier questioned now match the outputs as printed.

**Corrected or added:**
- Numbers in the fig3e, fig2c and fig1h conclusions, and "seven" → "nine" features below 80% in the cell-metadata-link and fig1i notes.
- fig4d now says the main reading's 2 genes (against the paper's 253) suggests the Methods' description is not the procedure the paper ran.
- New printed outputs back three findings:
  - **IPFX:** version 2.1.2, and none of the 19 missing features is named anywhere in its source.
  - **Genes_Detected:** no threshold from 0 to 5 reproduces it for any cell.
  - **Microglial calls:** the two tables' calls agree for all 778 cells.
- The 181 against 180 finding was wrong. The extra culture microglial cell is the metadata table's repeated row, and I corrected the finding.
- Two new `methods_unavailable` findings ask the paper's authors which cells Fig. 5D shows and which sweep fig. S8B's firing rate uses.
- `questions/lee-2023.yaml` has two new questions for a reader: whether figs9's "primarily" allows a weaker acute difference, and whether the rate at rheobase can count as "average firing rate" (figs8b). The figs2d question was already there from round 1.
- Round 2 is recorded under `verifications` for all 46 claims. The `entry.yaml` and README runtimes are updated.

**Not done:**
- Cell-level QC (seal and access resistance) is still not recomputed. It would change the cell sets of every claim at the final round, and the verifier says it doesn't change an outcome.
- mouse-label-link has still not been checked by a second reader. Only a claims-check run can do that, and this run can't start one.
- The fig3 Patch-seq part and fig6b are still not run.

There are untracked files in the checkout that I didn't create (`.bashrc`, `.idea`, `scripts/` and others), and I left them alone.
