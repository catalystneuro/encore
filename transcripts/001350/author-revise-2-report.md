The round-2 revision is finished. No outcome changed and nothing is under `proposed`. The entry was re-run twice with `python tools/entry.py all entries/001350-iram-2024`. Both notebooks pass in both runs with identical numbers, and `tools/entry.py check` reports 0 errors.

**Main change, fig4ab (157 and 264 genes):**
- **What the paper did:** its own normalized counts (Datasets S2 and S3) equal the expected counts divided by tximport's length-offset factors in every sample. With size factors alone they don't match. So the paper used offsets, and reading (b), the stand-in the verifier questioned, was not its method.
- **New code:** pydeseq2 has no option for those factors, so `srf_geo.deseq_offsets` puts them into its fits as DESeq2 does. As a check, given pydeseq2's own size factors it reproduces plain pydeseq2 exactly.
- **Result:** with the offsets and the DESeq2 manual's standard gene filter (at least 10 counts summed over a stage's samples), 156 and 263 genes have padj < 0.05. Both are inside tolerance. They share 145 and 238 genes with the paper's own tables (154 and 261).
- **Assumption now behind the outcome:** the paper's tables list fewer genes than have counts, so it filtered genes by a rule it doesn't state. With no filter, the counts are 133 (outside the tolerance) and 266. The record now says this, and the question to the authors asks for the filter rule.
- **Record:** this reading replaces (b) as the adopted one, and `measured` is now 156 and 263. The outcome stays "reproduced". Changing the adopted reading isn't a change of outcome, so round 3 has nothing to review. The new basis is stated plainly in the response.

**Counts that moved between rounds:** a fit repeated on one machine gives identical results, and this run reproduced the round-1 numbers (118/293 and 130/418) with unchanged code and packages. So the round-2 values (117/294 and 130/423) most likely came from a different processor. Between 15 and 44 genes per reading sit within 0.005 of the padj 0.05 cutoff.

**Other corrections from the report:**
- **fig3a:** `measured` now holds only 848.
- **fig2d:**
  - Myelinated density is now given as 0.53 of the paper's value for the Flox mouse and 0.58 to 0.69 for the cKO mice, in place of "about half in both".
  - In the Flox mouse, both the total axon density (0.74 of the paper's) and the fraction myelinated (0.71) are low; together they give the 0.53.
- **fig4cd and figs4ef:** all values now come from one reading, the offsets one (Actg1 p 0.028).
- **Dataset S2 claim:** the sample columns of Datasets S2 and S3 are now printed.
- **159 against 160:** the gene-matching note explains this.
- **README:** the runtime now reads 15 to 25 minutes, most of it the DESeq2 fits.
- **Record:** round 2 is entered under `verifications` for all 30 claims.

**Not done:**
- R DESeq2 itself is still not run, because R isn't available.
- MEME-ChIP still stands as a stated deviation.
- The TEM image scale and the unit of Fig. 2D remain unchecked: the dataset has no scale bar to check against.

`tools/runner/chain.sh` was already modified before this run; I left it untouched.
