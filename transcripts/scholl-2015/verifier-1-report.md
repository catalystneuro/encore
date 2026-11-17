**A. Outcomes**

The claims file has 25 claims. The notebook tests none of them and marks all 25 blocked (cell 0, cell 19). No attempt record was among my materials, so the counts come from the claims file and the notebook.

| Claim | Outcome | Reason |
|---|---|---|
| fig1e-pv-tdtomato-colocalization | blocked (data_missing) | I checked the bucket listing: 221 keys, and no histology anywhere. The criterion itself says the claim cannot be tested without histology. |
| cell-counts-responsive | blocked (data_missing) | `live/` holds raw movies, stimulus tables and 50 example masks with no cell type (cells 3, 10). It has no masks or PV labels for the paper's cells. `original/to_remove/binocmonocinds*` holds index lists for all 6 mice. They sum to 109 PV and 769 non-PV (cell 12), but what they index is not documented. |
| fig3abc-pv-more-binocular-fraction | blocked (data_missing), partly testable | The published folder has no per-cell ODI. `to_remove` has non-PV and PV structs with fields `peaks`, `dsi`, `disparitypref` and `xy` for mice 8, 9 and 10, and for mouse 7 PV only (cell 12). |
| fig3c-contralateral-bias | blocked (data_missing), partly testable | Same as above. |
| fig3-pv-lower-monocularity | blocked (data_missing), partly testable | Same as above. |
| mi-per-animal | blocked (data_missing), partly testable | Same as above, but only 3 animals have both populations, against the paper's 6. |
| fig3def-pv-weaker-disparity-selectivity | blocked (data_missing), partly testable | `dsi` is present for mice 8–10 in `to_remove`. |
| mi-dsi-relation | blocked (data_missing), partly testable | Same as above. |
| pv-larger-dff-low-dsi | blocked (data_missing), partly testable | `peaks` and `dsi` are present for mice 8–10 in `to_remove`. |
| figs3-pv-distinct-from-neuropil | blocked (data_missing) | `to_remove` has per-cell `neuropilpeaks` and `dsineuropil` fields. Whether these match the paper's "nearby neuropil" for the 28% figure is not established. |
| fig4ag-salt-and-pepper | blocked (data_missing), partly testable | `xy`, `xyshft` and `depth` exist per session for mice 8–10 in `to_remove`. |
| fig4d-pv-od-matches-local-50um | blocked (data_missing), partly testable | Same as above. Needs PV and non-PV cells from the same session, so mice 8–10 only. |
| fig4f-pv-od-spatial-decay | blocked (data_missing), partly testable | Same as above. |
| fig4f-od-length-constant | blocked (data_missing), partly testable | Same as above. |
| fig4ef-pvminus-od-unrelated | blocked (data_missing), partly testable | Same as above. |
| figs6ab-pvminus-pv-like-od | blocked (data_missing), partly testable | Same as above. |
| figs4-same-plane-control | blocked (data_missing), partly testable | Same as above. Per-entry `depth` gives the focal plane. |
| figs5-neuropil-no-relation | blocked (data_missing) | Nothing in the bucket identifies the paper's cell-sized neuropil patches as individuals. |
| fig5-camkii-responsive | blocked (data_missing) | The bucket listing has only mouse5 to mouse10, and the descriptor says all 6 are PV-Cre. No CaMKIIa animals anywhere. |
| fig5e-camkii-od-unrelated | blocked (data_missing) | Same as above. |
| fig4i-pv-disparity-matches-local | blocked (data_missing), partly testable | Same `to_remove` coverage as fig4d. |
| fig4k-pv-disparity-length-constant | blocked (data_missing), partly testable | Same as above. |
| fig4jk-pvminus-disparity-weak | blocked (data_missing), partly testable | Same as above. |
| figs6cd-pvminus-pv-like-disparity | blocked (data_missing), partly testable | Same as above. |
| fig5f-camkii-disparity-unrelated | blocked (data_missing) | No CaMKIIa animals. |

"Partly testable" means a subset of animals could be analysed from the processed structs in `original/to_remove/`, if the protocol allows that folder (see B1). On the published folder alone, all 25 are blocked. Re-identifying cells from the raw movies would also hit methods_underspecified: the paper says cells "were identified by hand". It would hit too_large as well: 252 GB, about 5.2 h to stream at the measured rate (cell 18).

**B. Problems**

1. [affects a conclusion] Cells 0, 11 and 12 set aside `original/to_remove/` because it "cannot be pinned". That reason does not hold.
   - The S3 listing gives an ETag for every file. Most are single-part MD5s, for example `binoc9.mat` 0189cb6da7943af59e7cb0b0b8fcbc2c, last modified 2026-02-11.
   - The structs hold the per-cell data the descriptor says the data set contains: `peaks`, `dsi`, `disparitypref`, `xy`, `xyshft`, `masks`, `sampleG`, `sampleR` and `neuropilpeaks`.
   - Complete non-PV and PV structs exist for mice 8, 9 and 10. Mouse 7 has a PV struct only. All three mouse-7 non-PV files are truncated, and mice 5 and 6 have no structs.
   - So a 3-animal partial test of the ODI, MI, DSI and local-network claims was possible. It would be clearly labelled as coming from an unlisted folder. Whether the protocol (docs/archives.md) allows unlisted folders is for the coordinator to decide. Either way, the notebook should state the decision and its basis, and should not rest it on pinning.
2. [affects a conclusion] Cells 0 and 19 say "no responses or measures per cell" and "none of these is in the published data set". That is true of `live/` only.
   - The descriptor, quoted in cell 2, promises per-cell measures. The notebook found them in `to_remove` (cell 12) and never reconciles the two.
   - The reason code should say these data are missing from the published listing and present, unpublished and partial, in `original/to_remove`.
3. [does not affect a conclusion] Cell 12 dates the structs to "November 2014", but no output prints the `date` field. It also does not report what one entry is (cell or plane), or the shapes of `peaks` and `dsi`. So "partly testable" above rests on field names and per-entry depth counts only.
4. [does not affect a conclusion] Cell 14 takes the 0.5 s window as 15 frames at 30 Hz. Cell 6's own output implies 26.2–26.6 frames/s for five of six mice, if a cycle is the stimulus plus a 3 s blank. The notebook prints this conflict and leaves it unresolved. The cell is a data check only.
5. [does not affect a conclusion] Cell 14 finds the peak on the average of all 50 masks, which is per plane. The claims file's plain reading is per cell. The responsiveness index is then computed on the same data used to place the window, which is circular. Again a data check only.
6. [does not affect a conclusion] Cell 6 shows mouse 10 with 4–5 repeats per condition, and single planes of mice 6 and 8 with 5. The paper says 6–7. Cell 4 shows mouse 10 down to 125 µm; the paper says 150–460 µm. The notebook does not comment on either.
7. [does not affect a conclusion] Helper functions. I tested `trial_dff` and the arithmetic of `mask_traces` on synthetic inputs, and both are correct: the 1-based onset is handled, Fo comes from the 10 preceding frames, edge trials become NaN, and the mask mean is right. Cell 3 has a redundant conditional in `folder` that does no harm.

The claims file: I found no place where it misreads the paper on the points I checked. Those were the cell counts, the neuropil wording and the CaMKIIa passages.

**C. What I could not check**

- What the `binocmonocinds*` indices select. If they are cells passing the joint criterion, 109 PV against the paper's 115 is within tolerance and 769 non-PV against 944 is not. Two added outputs would settle it: the index contents next to each struct's entry count, and the `peaks` shape per entry.
- Whether a struct entry is one cell, and whether `xy` is in pixels or µm. An added output printing, for one struct, the shapes and first values of `xy`, `peaks`, `dsi`, `masks` and `date` would answer this, plus the full pixel-to-µm question for the local analyses.
- Whether the `to_remove` per-cell counts for mice 8–10 match the paper's per-animal composition. That needs a per-mouse count of entries with `dsi` and `peaks`, split into PV and non-PV.
- How the data were posted. I took this from cell 12 and the listing, without downloading anything: the mouse-7 non-PV files are truncated copies (stored_eof 1,425,407,117 bytes against 0.72–1.40 GB present), and no struct exists for mice 5 and 6.
