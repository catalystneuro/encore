I've revised the attempt for every point in the round-1 report. One outcome changed, and the final run of `python tools/entry.py all entries/000008-scala-2021` passes all three notebooks, with every conclusion matching its numbers. Nothing is committed.

**Outcomes**
- **cohort-cells-mice: partially reproduced → reproduced**, as the verifier gave it. The claims file counts distinct recorded cells, and the three duplicated recordings belong to six distinct cells: they differ in read counts, genes detected and depths, and four of the six are on different slices. The notebook now prints those differences. The shared recordings (1,325 recordings for 1,328 cells) stay a finding. `measured` is now 1328 and 266.
- **ed6-physiological-temperature and fig4e-pvalb-axon-shape:** I kept them as blocked for `methods_underspecified`; the verifier said `data_missing`. The protocol does not allow `data_missing` for a claim whose data are in another public archive, and here the data are public (DANDI:000035 and the Brain Image Library). What blocks both claims is that the paper gives no measure to test. The disagreement, which is about the reason only, is recorded.
- Every other outcome matches the verifier's.

**Corrected**
- **Layer (ed6-it-et-room-features, fig4b-sst-rebound):** the layer now follows the claims file's opening comment: depth cut at the Nissl boundaries, or the targeted layer when there is no depth. The files' own layer field and the paper's µm depths are shown as variants.
  - ed6: the same four features come first under all three layer definitions.
  - fig4b: r = 0.339, p = 0.0113 (it was 0.347, p = 0.0094).
  - Neither outcome changed.
- **Metadata link:** fields are now compared exactly, with no rounding; all 1,328 cells still agree on every field.
- **Leiden entropy function:** it no longer reads a global variable; the numbers are unchanged.
- **Wrong statement fixed:** the notebook and the duplicate-recordings finding said every duplicated pair came from different slices. One pair shares a slice.
- I deleted a stray profiling file (`prof`) that the earlier author run had committed to the entry.

**Outputs added at the verifier's request**
- The full list of file metadata fields: none holds a hold time or cDNA yield, so hold-time-yield uses only the paper's table.
- A cross-tabulation of first and largest current step: 87 of the 90 cells starting at −100 pA end at 1,480 pA.
- fig3d-morph-combined: the code cells each step follows are now cited, and the all-cells result is printed. With all cells, 628 have both, which is the claims file's count.
- fig5c reading (b): two library-size normalizations, with ρ = 0.068 and 0.016. Neither makes the reading hold.
- fig5d: the cells above the median. No cell sits at the median (32.5).
- fig2-rrr: the cross-validation folds are printed.
- morph-reconstructions: a cell that tries to list the Brain Image Library folder. It timed out again on 2026-10-21.

**Not done, and why**
- I did not change the boundary handling in the layer function. A depth exactly on a boundary keeps the targeted layer, which is exactly what the paper's code does. The docstring now says so.
- fig1a-ttype-coverage stays partially reproduced. The claims file doesn't say whether its allowance for the one missing cell also covers the one t-type only that cell represents. I added that question to `questions/000008.yaml` and did not change the claim.
- fig5b-ttype-variability and ed8-leiden-entropy are unchanged; their notes already show how fragile each result is.
- The fig5d question about judging reading (b) by the exact p-value is still open, waiting for a reader's answer.
- No listing of the reconstructions could be added, because the archive's server never answered.
