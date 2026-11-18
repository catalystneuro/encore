I've done steps 1 to 6 of the author protocol. All 27 claims come out blocked: the three c-Fos claims were run on the data, and the other 24 need data the dandiset doesn't hold. Lock, check and the clean run all passed, the notebook took 35 min, and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig5-dg-fos | blocked: methods_underspecified |
| table4-lenient-regions | blocked: methods_underspecified (depends on fig5-dg-fos) |
| table4-region-values | blocked: methods_underspecified (depends on fig5-dg-fos) |
| 24 claims on behaviour, qPCR, sections, RNAscope/HCR, body weight, telemetry | blocked: data_missing |

- **fig5-dg-fos:** under the 20 readings the criterion names (5 thresholds × 2 region sizes × 2 outlier rules), DG-sg and DG-po are both significant after correction in 12, one of them in 3, and neither in 5. The criterion says to block when these readings disagree, so I blocked it. PACAPko is higher under every reading: DG-sg at 200–239% of control (paper 224%), DG-po at 261–547% (paper 326%). With density and within-genotype outliers, both regions are significant at every threshold.
- **The two Table 4 claims:** each gives "partially reproduced" under every reading. They are blocked only because they depend on fig5-dg-fos.

## 2. The dataset, assumptions and questions

The dandiset is BIDS (OME BigTIFF and TSV), not NWB. I streamed it with remfile and tifffile at version 0.260923.2152. The paper cites no version; this is the latest, and the other published version has the same blobs.

It holds only the whole-brain c-Fos experiment:
- **Hemispheres:** 22 hemispheres from 13 mice, where the paper used 19 from 12. Nothing marks which were analysed.
- **Count tables:** they exist for only 13 of the 22 hemispheres. They count every connected component, not the 9–900 voxel objects the Methods describe; those objects make up only 43–65% of the table totals.
- **FRST threshold:** the threshold the authors used is not recorded anywhere.
- **Region list:** the paper's 431 regions can't be rebuilt from the label table (I get 438).
- **Metadata errors:**
  - The README says the stacks are 25 µm isotropic, but they are 3.7×3.7×5 µm. It also links a different CATNIP repository and a 2024 preprint.
  - The heatmaps give 3.7×3.7×5 µm voxels in their image metadata but 25 µm in their sidecar files.
  - The strain is spelled two ways in participants.tsv.
  - The archive summary lists no species.

So I recounted cells for all 22 hemispheres from the deposited segmentations. Counting every component this way matches the dataset's own tables to a median 1.25% per region.

- **Assumptions** (none decides an outcome):
  - 26-connectivity for the components.
  - Excluded regions identified from the Allen colours in the label table.
  - Linear interpolation for the quartiles.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): which threshold was used per hemisphere, which 19 hemispheres were analysed, how the outlier rule was grouped, what region size the counts were divided by, which connectivity was used, and the list of 431 regions.
- **Questions to a reader:** none.

## 3. Where the protocol was unclear or didn't fit

1. The prompt says to stream NWB files, but the dataset has none. I streamed the TIFF and TSV files instead.
2. The fig5 criterion says to block when readings disagree, while protocol step 1.6 allows adopting the best-supported reading as an assumption. I followed the criterion and gave the best-supported result in the notes.
3. The dependency rule blocks the two Table 4 claims even though each gives the same outcome under every reading. I followed the rule and put their results in the notes.
4. The protocol aims for notebooks under 10 minutes, but recounting about 45 GB of segmentations takes about 27 minutes. I ran it at 35 minutes, under the 60-minute limit; the protocol says nothing about caching derived counts.
5. The criterion asks for "every threshold the derivatives hold", but hemispheres hold 11 or 19 thresholds and running them all wouldn't fit. I ran the 5 that all 22 share.
6. It's ambiguous whether the 13 hemispheres with count tables are "marked as used". I treated them as not marked and showed them as a variant. I also showed every choice of hemispheres matching the paper's counts (48) as a variant.
7. Step 2's clock check doesn't apply to image data with no time series. I said so in the notebook.
8. The lenient-regions criterion doesn't cover the case where SNr, STN and IGL all pass but the region count is out of tolerance. I judged that partial; it never occurred.
9. The protocol doesn't say whether blocked outcomes need `measured`. I left it out and put the numbers in the notes.
10. After the last run I fixed a miscount in the summary table ("25 claims" should be 24) and a docstring in `fos.py`. I applied the summary fix to both the committed and executed notebooks without re-running; no computed output changed.

## 4. Runtime and failures

About 3 h 30 min in total (07:38 to 11:10 UTC). That includes one 51-minute development recount and three clean runs of about 36 minutes each. Nothing failed in the final run; one bug found while developing (a read-only array) was fixed before it.
