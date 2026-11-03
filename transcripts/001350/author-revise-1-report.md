The round-1 revision is done. Two outcomes changed, the five TEM claims got a new blocking reason, and both notebooks re-ran cleanly with `python tools/entry.py all entries/001350-iram-2024` (0 errors; TEM notebook 117 s, GEO notebook 1126 s). The round is recorded under `verifications`, with all 30 claims. Nothing is committed.

## Outcome changes
- **fig3a-chip-peaks: reproduced → partially reproduced**, as the verifier gave it. The 848 matches, but it is only a count of the deposited file. The 329 matches only with "a majority of replicates": 312 or 316 peaks. "All replicates" gives 204 to 206 and "at least two" gives 404 to 409. I no longer adopt the majority reading.
- **figs4ef-assembly-not-disassembly-genes: reproduced → partially reproduced** (still resting on an assumption). I added 26 standard actin assembly genes (Arp2/3 subunits, formins, profilins and so on). Only Actb changes. In oligodendrocytes one assembly gene and one disassembly gene (Cfl1) change, so "SRF mainly regulates assembly genes" holds only through actin itself. The verifier had agreed with "reproduced"; this change came from the new test, and round 2 will review it.
- **The five corpus callosum TEM claims:** still blocked, but now as `data_missing` instead of `other`. The masks cover one of the five SRF-Flox mice, so the per-mouse measurements the test needs are missing.

## What I added or corrected
- **The paper's Datasets S1 to S3.** These are the supplementary peak lists and the paper's own DESeq2 tables, read from Europe PMC and listed under `inputs`. They are used only to check which method the paper used; no result is computed from them.
  - S1 lists 800 peaks by cell group, not the 329, so it does not settle fig3a.
  - The paper's tables hold 154 and 261 differentially expressed genes, where the text says 157 and 264. I added this as a `paper_inconsistency` finding.
  - Their values are on the scale of raw expected counts. That suggests the paper adjusted for gene length inside DESeq2, which pydeseq2 cannot do. The length-scaled counts I use (reading b) are therefore a stand-in, though they are the closest of the three readings to the paper's tables. fig4ab stays reproduced, resting on that assumption.
- **TEM notebook:**
  - Mask outlines on raw image crops, one per genotype. By eye, the masks look complete.
  - Total axons per µm² against what the paper's Fig. 2C and 2D imply together. The totals are close (3.6 against 4.9 for the Flox mouse); the low myelinated density comes from a lower fraction myelinated.
  - The conclusions now discuss the density gap and the reversed g-ratio and diameter directions.
  - A variant without the pixels that sit in both masks: no mouse's percent myelinated moves by more than 0.02 points.
  - The scipy precision warning is noted, and the image counts and sizes are corrected.
  - The text says why the dandiset's segmentation model is not used: the paper does not rely on it, it was trained on these same masks, and it needs a GPU this runner lacks.
- **GEO notebook:**
  - The no-IgG reading is now in the fig3a table.
  - The CArG motif enrichment holds after comparing like-for-like GC content (odds ratio 2.14 with the JASPAR SRF matrix, 2.75 with the strict CArG consensus).
  - The text says the one-mismatch motif is my own reading.
  - fig3d is also run on the paper's own peak lists (42 shared genes, against 60).
  - I added a listing of the snRNA-seq files in GEO: count matrices only, with no cluster labels.
- **Numbers that moved:** rounded counts now give 117 and 294 genes (was 118 and 293), and the joint model 423 (was 418). The notebook text and the record use the new numbers.
- **Packaging:** I added `matplotlib` and `openpyxl` to the requirements and re-locked. The GEO notebook's runtime is now 19 minutes in `entry.yaml`, and the README table is updated.

## Not done
- **DESeq2 with tximport length offsets (the reading the verifier asked for):** not run. pydeseq2 cannot take per-gene offsets and R is not available here.
- **MEME-ChIP motif discovery:** not run, as there is no way to run it in the locked environment. It stays a deviation.
- **Questions file:** no question added. The verifier reported no misreading. The Fig. 3D Venn diagram (33, 60 shared, 34) confirms the claims file's 60 is the shared count.
- **Runner URL:** not updated, as I don't know this run's URL. The record still points to an earlier run.
