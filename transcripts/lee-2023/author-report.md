I finished the attempt: the entry, the notebook and `attempts/lee-2023-01.yaml` are written, the checks pass, and the handover package is built in `executed/lee-2023/handover/`. Nothing is committed.

## 1. Outcomes (45 claims)

| Outcome | Claims |
|---|---|
| Reproduced (20) | cell-metadata-link, fig1b, figs1a, fig1d, fig1c (rests on an assumption), fig1g, fig1h, fig2e, fig2g, fig2h, fig3c, fig3e, figs6, fig3g, fig4c (rests on an assumption), fig5a, figs7a-dbc-regions, figs7a-dbc-markers, figs5, fig5d-dbc-morph-umap (depends on the seed: two of five seeds fall below the threshold) |
| Partially reproduced (3) | dataset-composition (LAMP5/PAX6 count is 64, the paper says 75), fig2f (LAMP5/PAX6 peak highest, but not significantly against every other subclass), fig5c (6 of 8 DBCs above the comparison median under reading a) |
| Not reproduced (5) | fig1i (feature space ratio 0.43, the criterion needs 0.5), fig2b (VIP excess 0.193, needs 0.2), fig2c, fig4d (2 genes, the paper says 253), fig5d-dbc-ephys-intermingled |
| Blocked (17) | figs2b, fig1l, figs2c, fig5e: methods underspecified. figs2d, fig5b: other. Five Seurat claims, fig4a, fig6b: not runnable. Four mouse ephys claims: data missing |

## 2. Dataset, assumptions and questions

**Dataset.** I pinned version 0.241120.0510, the only published version; the paper cites none.
- The 706 NWB files carry no cell type, region, layer, condition or days in culture. All labels come from the code repository (commit 5eb357a), linked by its `nwb_id` column.
- 684 of 704 metadata rows with electrophysiology have a file. 16 files have no metadata row.
- Features recomputed with IPFX match the paper's table: rheobase, input resistance, sag and AP width at rheobase agree within 10% for 92 to 99% of cells.
- The archive summary says 616 cells for 706 one-cell files.
- 79 files have sweeps at 200 kHz, where the Methods say 50 kHz.
- Species is spelled two ways, the metadata table repeats one row, and the repository's Genes_Detected column does not match its own expression matrix.

**Assumptions.**
- fig1c: genes are ranked within the Patch-seq cells, because the snRNA-seq reference is not in the repository.
- fig4c: my ISI adaptation ratio definition matches the paper's table for only 27% of cells. The paper's own values put the morphology types in the same order.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which sweep's ISI and width Fig. 1L and fig. S2C use.
- The 19 features computed by unreleased IPFX code.
- The gene filter (`keepGenes`), which needs data the repository lacks.

**Questions for a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. The prompt and the claims file mention the bioRxiv preprint, but `paper/` held only the version-of-record text. I relied on the claims file for the preprint details.
2. MERFISH (fig5b) has no public location, but the claims file marks it `elsewhere`. The protocol says such data should be `data_missing`, and `entry.py check` rejects that for `elsewhere` claims. I used `other` and explained why in the notes.
3. Several criteria say "block when readings differ", while protocol step 1.6 allows adopting the best-supported reading. I followed the claims file (fig1l, figs2c).
4. The protocol has no rule for a count over a feature set that can only be partly computed (figs2b: 65 of 84 features). I computed bounds on the full count (39 to 61). They contain the whole tolerance band, so I blocked the claim.
5. The mouse t-type labels (Gouwens et al. 2020) have no pinned source, though the recordings are at DANDI:000020. I blocked the four `with_inputs` mouse claims as `data_missing`, and fig6b (`elsewhere`) as `not_runnable`.
6. Seurat (R) cannot be installed in an entry's locked Python environment. I blocked the five Seurat claims as `not_runnable`.
7. Seeded UMAP and shuffle results depend on the order of rows. My development cache was in a different order, so these numbers moved slightly in the real run, with no outcome changing. The protocol could warn about this.
8. Any edit to the entry forces a full 30-minute re-run, and the "**Result:**" text lives in the notebook. Correcting two sentences cost two extra full runs.
9. The link criterion can be read per feature or for all four features together. Both pass (joint reading: 90.6%).

## 4. Runtime and failures

- The notebook takes 30 minutes, almost all of it streaming the 706 files; a worker peaks at 4.3 GB.
- The run went from 09:12 to 13:17 UTC.
- The first full run failed at the duplicate check (pandas 3 keeps missing values as floats after `astype(str)`).
- A test in the locked environment timed out on figs2d, because `multipletests` takes about 18 ms per call there; I replaced it with a vectorized Holm adjustment.
- Both were fixed, and the final run passed.
