The round-1 revision of lee-2023-01 is finished. Both notebooks rerun cleanly with `tools/entry.py all`: the main one takes 28 min and the new human-against-mouse one 21 min. The two final runs gave identical outputs, and every conclusion matches the numbers. Nothing is committed.

**Outcome changes**
- **figs1a:** reproduced → partially reproduced. On the `Genes_Detected` column (the source the claim names, and what the paper's code plots), the median is below the acute median at days 2, 3, 8 and 11. The correlation part still holds.
- **fig2b and fig2c:** not reproduced → partially reproduced, as the verifier proposed. PVALB is the most distinct subclass everywhere, but separability misses for some subclasses. For fig2b, adding the paper's values for the 19 features public IPFX can't compute makes it pass, so the narrow miss may come from those missing features.
- **fig5d-dbc-morph-umap:** reproduced (seed-sensitive) → partially reproduced. SST now uses `Revised_subclass_label`, the claims file's default. Feature space passes and the UMAP fails on all five seeds.
- **fig5d-dbc-ephys-intermingled:** stays not reproduced under the revised label (feature-space ratio 2.54, limit 2).
- **fig4a:** blocked → partially reproduced. Two of the four traits were testable on the morphology table: one holds and one fails, which already rules out a full reproduction. The two L1 traits remain untested.
- **figs1-microglial-signature:** now run, with a Python substitute for Seurat. Its two readings disagree, so it is blocked as `methods_underspecified`, as its criterion says. figs1de follows it.
- **Mouse claims, previously blocked:** I found the mouse t-type labels in the Allen specimen table. The Allen URL has no version, so I used a public copy pinned at a commit and checked its hash. I added a link claim, mouse-label-link, which is reproduced: all 4435 rows match the DANDI:000020 files. In the new notebook `species_lee_2023.ipynb`:
  - fig6e: reproduced.
  - figs8b: partially reproduced (holds with the firing rate at rheobase + 40 pA, fails with the rate at rheobase).
  - figs9: partially reproduced (the Pvalb 2 width difference is also present in acute cells).
  - fig6c: not reproduced (Sst 5 human cells are not separated from mouse).

**Other additions and corrections**
- Four non-physical values (negative input resistance, zero widths) are now set missing before every test.
- fig1l: added the sampling rate by condition (all 200 kHz files are culture cells), a 50 kHz-only test (width still differs), and the bound with correction over all 84 features (9.9e-05). The claim stays blocked.
- fig1i, fig2b, fig3c and fig5d: added variants on the paper's 84-feature table. fig1i stays not reproduced; with the paper's own table it passes narrowly (0.51).
- fig3c: z-scoring is now over SST and PVALB cells only, as the criterion says, and the chance levels are printed. Still reproduced.
- Smaller additions:
  - fig2g: within-condition tests.
  - figs5: the list of virus labels.
  - fig5b: the Patch-seq cortical layers (SST CALB1 mostly L2, SST ADGRG6 mostly L3).
  - fig4d: a RESULT line and the upper-bound caveat.
  - figs2d: the code's lines that show which way the p-values are adjusted.
- The record now has the round-1 verifications (45 claims, with the verifier's reasons and my responses), new inputs, and a finding that the paper's own microglial calls flag a larger fraction of acute (0.418) than culture (0.385) cells.
- I added a reader question in `questions/lee-2023.yaml` about how the figs2d criterion reads the adjustment.

**Not done**
- **Verifier's choice of block reason:** I kept my block reasons where the verifier suggested `data_missing`. The registry's check does not allow `data_missing` for claims whose data are in another archive, and the disagreement is recorded for each one.
- **fig3-frzb-transcriptome:** the Patch-seq-only parts were not run, for time.
- **Cell-level QC:** seal and access resistance are still not recomputed.
- **entry.yaml runtimes:** they still say 40 and 20 min. Changing them would have invalidated the run stamp.
