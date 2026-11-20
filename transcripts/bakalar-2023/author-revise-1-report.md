## Report on round 1 of 001362-bakalar-2023

No outcome changed. The main notebook now takes 66 minutes, over the 60-minute limit, so the entry's run will fail until it is split. Thresholds 28000 to 40000 were not run, for time.

**Outcomes**
- **fig5-dg-fos:** still blocked as `methods_underspecified`. The verifier agrees. At 4000 to 12000 the 20 readings still give 12 reproduced, 3 partial and 5 not. At 14000 to 26000, on the 18 hemispheres that have those thresholds, 55 of 56 analyses find neither region significant.
- **table4-lenient-regions** and **table4-region-values:** still blocked, and the disagreement is recorded. The verifier would give partially reproduced. Both claims list fig5-dg-fos under `depends_on`, and the protocol blocks a claim whose dependency is blocked. The new higher thresholds support the verifier's concern: for table4-lenient-regions, 54 of 56 analyses at 14000 to 26000 are not reproduced. For table4-region-values, 2 of 112 there are not reproduced (LRN in the wrong direction).
- **The 24 claims with no data in the dandiset:** the verifier agrees with all of them.

**Added or corrected, by verifier point**
1. **Thresholds:** a new notebook runs 14000 to 26000 on the 18 hemispheres. Those 18 are 8 PACAP fl/fl from 6 mice, the paper's fl/fl numbers, and 10 PACAPko from 6 mice. A new "own series" variant counts the 4 re-segmented hemispheres at each of their own thresholds: 133 of 220 analyses give both regions, 37 one, 50 neither.
2. **Artifact mask:** the corrected heatmaps set 54,467 voxels (45670ko L) and 1,095,526 voxels (45925flox L) to 0. They are in atlas space, and the dataset has no atlas-space label image, so the excluded regions cannot be found. I recorded this as a finding and a deviation. A variant without those 2 hemispheres gives 7 readings with both regions, 6 with one and 7 with neither.
3. **Region list:** the 438 included regions and the 59 labels excluded besides tracts, nerves and ventricles are now printed.
4. **Masked vs unmasked labels:** each hemisphere is now also counted on the unmasked labels in the same pass. DG cell counts are the same on both. Where a masked image exists, DG densities on the unmasked labels are 0% to 17% lower. On unmasked labels the 20 readings give 14 with both regions, 3 with one and 3 with neither. I added a finding about the 6 hemispheres with no masked labels.
5. **Slab edges:** I added a synthetic check against `scipy.ndimage.label`. Every component of up to 48 planes is counted exactly. The "dropped" number counts pieces, so it is now reported as an upper bound.
6. **Count-table variant:** the notes now say it has little power (smallest possible p is 1.2e-03) and is not evidence against the claim.
7. **Claims file:** the verifier found no misreading, so no question was added.

The `verifications` round is recorded, and the notes, deviations, findings, notebook conclusions, summaries and README are updated. `tools/entry.py check` reports 0 errors, and the handover package is built.

**Not done**
- **Runtime:** in the full run, the main notebook took 66 minutes, against 37 before. Its recount cell alone took 52 minutes. There was no time to re-run after splitting it, so the next revision needs to move part of the counting into another notebook.
- **28000 to 40000:** the full run hit the 2-hour tool limit while that third notebook was running. I removed the notebook from the entry, and the record says this range was not run.
- **Run result:** because the run was cut off, `executed/.../result.json` was not written.

I left `tools/runner/chain.sh` alone: it was already modified before this run. Nothing is committed.
