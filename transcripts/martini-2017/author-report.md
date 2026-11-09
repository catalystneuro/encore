The attempt is recorded, the entry runs cleanly, and the verifier's package is built. Of the 18 claims, 7 are reproduced, 5 partially reproduced, 1 not reproduced and 5 blocked. `entry.py check` reports 0 errors, the notebook passes `entry.py all` in a clean environment (1484 s), and the handover is in `executed/martini-2017/handover/`. Nothing was committed.

### 1. Outcome per claim
| Claim | Outcome |
|---|---|
| dataset-size | partially reproduced (assumed) |
| stimulus-set | partially reproduced |
| fig2ab-example-neuron | blocked, metadata_insufficient |
| responsive-fraction | not reproduced (assumed; 44.7% against 45.2 to 55.2%) |
| fig2de-tuned-fraction | reproduced (assumed; 78.4% non-tuned) |
| fig2e-all-categories | reproduced (assumed) |
| tuning-consistency | reproduced (assumed; 99.5% and 86.5%, all neurons as denominator) |
| shuffle-significance | reproduced (assumed; the barrel-map parts untested) |
| fig3b-example-correlation | blocked, metadata_insufficient |
| fig3c-correlation-above-shuffle | partially reproduced (test holds; means outside tolerance) |
| neuropil-correlation | partially reproduced (0.61 against 0.179) |
| fig3d-example-correlation-distance | blocked (depends on fig3b) |
| fig3e-correlation-falls-with-distance | partially reproduced (true median within tolerance, shuffled median outside) |
| correlation-gradient-beyond-200um | reproduced (assumed; p = 0.459) |
| fig3f-example-si-distance | blocked (depends on fig3b) |
| fig3g-si-no-spatial-organization | reproduced (assumed; p = 0.614) |
| fig4c-barrel-septum-tuned | blocked, metadata_insufficient |
| fig4d-border-distance-by-feature | blocked (depends on fig4c) |

### 2. The dataset, assumptions, questions
**What the data set holds.**
- It is one 8 GB `data.tar.gz`. A gzipped tar can't be opened in place like a zip, so the notebook reads it once as a stream and reduces each field to ROI traces as it goes.
- There are no ROIs, traces or tuning labels: everything was rebuilt from the raw movies. My automatic ROI detector finds 2626 ROIs, against the paper's 1054 neurons.

**Findings recorded about the dataset.**
- Mice (10), fields (49) and movies per field (4) match the paper.
- Six movies have no stimulus file.
- Each complete stimulus file holds 89 deflections; the smallest position stimulus is presented 9 times, not 10.
- 188 of 190 stimulus files hold the same deflection order, so the order was not randomised between recordings.
- Two stimulus files are incomplete (52 and 87 deflections).
- Nine stimulus files start just after the first frame pulse. I put one frame before the file's start; the onset phase then matches every other file.
- The description gives 3 to 6 fields per mouse; the data hold 3 to 8.
- The description and the tar's README call the data set "ssc-5".
- The histology PDFs don't locate the fields or their neurons on the barrel map.

**Version.** CRCNS has no versions, so it is recorded as `unversioned` with the data set's DOI and the file's MD5, which the notebook checks against the live checksums.

**Assumptions.**
- ROI detection: a blob detector with soma-sized area limits, in place of Caltracer with manual supervision. Most outcomes rest on it.
- The main tuning reading: separate regressions, fdr_bh's default 'pdep', FDR family of all p-values in a field, two-sided slope test.
- Halo and vessel-background sizes.
- One ROI set serves all four movies of a field.

**Questions for the paper's authors** (one `methods_unavailable` finding):
1. How were the 1054 neurons selected?
2. What counts as a neuron that "responded"?
3. Which FDR variant and family were used, and did negative slopes count as tuning?
4. What scale was SI computed on, and which 26 fields entered Figure 3G?
5. Which mouse and field hold the example neuron and the example field?
6. Where is each field on the barrel maps?

**Questions to a reader:** none.

### 3. Where the protocol was unclear or didn't fit
1. Streaming a single tar.gz isn't covered by the CRCNS section of archives.md, which assumes zip files. I read it once as a stream (`tarfile` mode `r|gz` over fsspec), holding at most one field in memory.
2. Raw movies with no ROIs aren't anticipated. The protocol has no guidance on whether a re-implemented segmentation is an acceptable "method from the paper". I treated it as an assumption and marked every outcome that rests on it `assumed: true`.
3. "Develop on a subset" plus "run once on the whole" doesn't say whether a cached extraction may be used for development. I developed against a pickled extraction outside the entry; the notebook streams everything itself, and its outputs matched the cached run exactly.
4. The protocol doesn't say how to treat a claim of absence whose expected values (field counts, medians) miss while its test passes. I judged on the test, as the protocol says for absence claims, and gave the misses in the notes.
5. `tools/entry.py lock` writes `python: "3.13"` into entry.yaml, and the entry schema then rejects it. I removed the line, and check passed. The working-tree `tools/entry.py` was already modified before this run.
6. The protocol doesn't say how far to go in matching example neurons or fields to figures by eye. I didn't attempt it and blocked those claims with the reason.

### 4. Runtime and failures
- The run took about 2 h 05 min, 19:19 to 21:22 UTC.
- The notebook takes about 25 min (15 to 17 of them streaming), with a peak of 2.3 GB memory.
- An empty folder, `entries/martini-2017/.claude/.cc-writes`, was left in the entry directory by the agent tool. Removing it needed approval, which this session can't give, so it is still there; delete it before committing.
- Nothing else failed.
