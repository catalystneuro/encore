I've addressed every point in the round-1 report. No outcome changed. The entry re-ran cleanly with `tools/entry.py all` (0 check errors, notebook passes in 639 s), every conclusion matches the new numbers, and round 1 is recorded under `verifications`. Nothing is committed.

**Outcomes:** all stay as the verifier gave them. Four main-reading numbers moved slightly because of the bias fix below:

| Claim | Outcome | Main-reading p |
|---|---|---|
| AP waveform, spinal cord vs cortex | reproduced | 0.00011 (36 vs 24 cells) |
| AP waveform, spinal cord vs cerebellum | reproduced, recorded as weak | 0.029 (36 vs 9 cells) |
| Tau, cortex vs spinal cord | partially reproduced | 0.0077 (24 vs 36 cells) |
| Tau, cortex vs cerebellum | partially reproduced | 0.0025 (unchanged) |

The four sequencing claims stay blocked, but with corrected reasons:
- **`snrnaseq-single-cluster`** is now blocked as `methods_underspecified`. The criterion needs a silhouette score at K = 1, which is undefined for a single cluster, and the paper doesn't say how it computed one. I added a `methods_unavailable` finding asking the authors.
- **The other three stay `not_runnable`.** They all start from the paper's selection of 4,743 nuclei, made in R (Seurat, Harmony); the entry's locked Python environment can't run that.

**What I changed in reply to each problem:**
1. **Bias current:** the NWB files contain the acquisition software's (MIES) lab notebook, and the entry now reads it. Where holding is on, the bias value always equals the applied holding level (2,433 of 2,433 sweeps). For the 18 cells with no sweep within ±100 pA, holding and autobias were on and the baseline sat within 1.5 mV of the autobias target. So the bias was really applied, and the Methods' rule rightly excludes those cells.
   - Fixing this also caught a bug: 17 sweeps recorded with holding off have no bias value and had been treated as failing. They now count as 0 pA, which adds one spinal cord cell (1392357828) to the main reading. That cell sat at about −22.7 mV with holding off; the notes say so.
   - The bias count is now 18 cells (it was 19), and the paper's table has values for 16 of them.
2. **Input resistance source:** already shown not to matter; nothing changed.
3. **The 8 wild-type cells:** I refitted the PCA without them; it gives the same verdicts as just leaving them out. None of the 8 has a transcriptome.
4. **k-mer counting:** NeMO has no aligned counts for the Patch-seq cells. Instead I compared the method with STAR on 60 retro-seq nuclei from the same paper. Spearman r is 0.98 to 0.995, and the four-marker call is the same in all 60. Neither method finds Slc32a1 there, so its reads in the Patch-seq libraries are real reads, not matching errors.
5. **NeMO collection:** the notebook now lists col-p9d5w39's five child collections and the shapes of the 16 count files (37.7 million unfiltered barcodes). None of the files marks the paper's 4,743 nuclei.
6. **Negative seal values:** IPFX averages six test pulses, and one pulse can drive the mean negative. The median over pulses is now reported beside it.
7. **Donor check:** it now compares the two columns for real (96 of 96 match), and the mapping's file URLs match the asset IDs.
8. **Collection membership:** all 128 files are in col-s96tk9a's manifest with matching MD5 sums. The NeMO API itself files them under a snapshot collection instead; I added that to a finding.

The verifier also asked for the rheobase sweep chosen per cell, the five largest tau disagreements with sweep counts, and the IPFX version (2.1.2); these are now printed.

**Other fixes:** a test run lost 7 FASTQ downloads, and the old code silently counted those cells as "not detected". Downloads now retry and check MD5, and the notebook stops if any library still can't be read. Adding the retro-seq check required the `rdata` package, so the lock file changed and the runtime is now about 12 minutes.

**Not done:**
- I didn't reimplement the paper's R nucleus selection in Python to test the three pseudospace and retro-seq claims.
- I didn't fetch the MERFISH data or run MapMyCells (reading (c) of the identity claim).
- I added no reader questions: the verifier reported no place where the claims file misreads the paper.
