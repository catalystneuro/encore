## Report: DANDI:001785, Fujimoto et al. 2026 (author run)

The entry is in `entries/001785-fujimoto-2026/` and the record in `attempts/001785-fujimoto-2026-01.yaml`. `entry.py all` passed (0 errors, notebook runs in 351 s) and the handover package is built. Nothing is committed. I pinned version 0.260615.1835: the paper cites no version of 001785, this is the latest published one, it has the same files as 0.260522.2215, and it adds 13 EM images over the April versions.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| link-fc-voxels, link-fa-voxels (added by me) | reproduced |
| link-if-counts (added by me) | partially reproduced (counts match in 2 of 4 regions) |
| ed1-behavior-increase (data in 001773) | reproduced (F = 34.61 and 17.35, as reported) |
| ed1-sham-no-behavior-change | not reproduced (foraging in D falls, p = 0.023) |
| fig2a-cb-fa-increase, fig2a-no-other-tract-change, ed2, fig2b, fig6a, fig6b (FA) | reproduced |
| fig3c, ed5 (cell counts, MCC-CB) | reproduced under all four counting readings |
| ed6a-dacc-cb-no-change | not reproduced (ratio p = 0.006 to 0.013 under all readings; the paper's own counts give p = 0.09) |
| ed6b-uf-fm-no-change, fig6c-sham-cc1-no-change | reproduced, resting on an assumption |
| fig5a-pre, fig5b decreases and increases, ed7, fig5-bilateral, fig5c network and SMN, motor, VIS, SAN, fig6d, fig6e (seed maps, 12 claims) | reproduced |
| fig3f-gratio-decrease | blocked: not_runnable |
| fig4a, fig4b, fig4c, fig4-control, ed10c, fig5a-control-group-no-reduction | blocked: data_missing |

### 2. Dataset, assumptions, questions

**What the dataset holds**
- The files are NIfTI and TIFF (BIDS-like), not NWB, and `dataset_description.json` is not valid JSON.
- The FC files are not EPI data. Each is a single normalized seed map per session. They match the paper's source data voxel for voxel once the AFNI coordinates are read as RAI.
- The FA maps hold every per-voxel FA value the paper listed, but the dataset has no tract or ROI masks. I located the tract voxels by matching values (6332 of 6332 found).
- Because the voxel labels come from 001773, the FA and seed results repeat the paper's statistics on the dataset's values. They show the data are there, not that the masks would be found again.

**Other findings**
- The dataset has no cell counts and no g-ratio measurements, only the images.
- `TR-1-8r.tif` is a byte-identical copy of `TR-1-8.tif`.
- There is an extra UF-FM field (N122 RW6) that the paper's sheet does not use.
- The paper's FA voxel lists repeat some voxels, so its voxel n counts some twice.
- The FA maps reach values above 1.
- The IF TIFFs have no pixel size and no channel names.

**Changes I made to the claims file.** I added three link claims and added them to `depends_on` of the claims that use them. I set `data: with_labels` on four FA claims (fig2a, fig2a-no-other, ed2, fig6a) because their tract labels come from outside the dataset. Statements, expected values and criteria are unchanged.

**Assumption.** The paper gives no size filter for counting cells. I assumed a smallest object of 10 pixels, because its counts match the level of the paper's counts. At 50 pixels, ed6b reaches p = 0.0500 and fig6c reaches p = 0.044, so both outcomes rest on this choice and are marked `assumed`.

**Question for the paper's authors** (recorded as a `methods_unavailable` finding): which threshold method, size filter and watershed were used for counting cells in FIJI?

**Questions to a reader:** none.

### 3. Where the protocol was unclear or missing something

1. **The `data` field.** The protocol does not say whether the author may change a claim's `data` field when labels turn out to come from outside the dataset. I changed it on four claims and recorded each change as a deviation.
2. **Link criteria written after seeing the data.** For a link claim, the protocol gives no rule for when its criterion is written relative to the analysis. I wrote the link-if-counts criterion after first computing the counts, and said so in the criterion.
3. **The clock check.** "Show every data stream shares the clock of the trial tables" has no counterpart for static images and maps. I skipped it.
4. **Choosing which outside data count as measurements.** The claims file allows 001773 only for links. Its group-average connectivity matrices and per-axon measurements are outputs of the paper. I treated them as not usable as data: the matrix claims are blocked as `data_missing` and fig3f as `not_runnable`. The protocol's `elsewhere` rule could be read the other way.
5. **Hand measurements.** The protocol has no blocked reason that fits a method done by hand, such as manual g-ratio measurement. I used `not_runnable`.

### 4. Runtime and failures

- The run took about 40 minutes by the clock (18:07 to 18:47 UTC), and a full notebook run takes about 6 minutes.
- An automatic EM segmentation, tried outside the notebook, found few of the paper's axons, so I dropped it and blocked fig3f.
- In scipy, Tukey-Kramer p-values stop at about 1.4e-11; smaller values are reported as being at that floor.
- Nothing else failed.
