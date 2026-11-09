I finished steps 1 to 6: the entry passes `tools/entry.py all` (0 errors), the notebook runs in 562 s from a clean environment, and the handover is built in `executed/001702-chaunsali-2025/handover/`. I pinned DANDI:001702 at 0.260216.2323. The paper cites no version, and that is the only published one; the draft has the same 656 assets. Nothing is committed.

## 1. Outcomes (51 claims)

| Claim | Outcome |
|---|---|
| fig4b-3m-degs | partially reproduced, assumed (51 up / 141 down; one model per age gives 98 / 137) |
| fig4c-7m-degs | partially reproduced (320 up; down count 0 to 7 across the four readings, never within 6 ± 0.6) |
| fig4d-3m-go-memory-terms-down | partially reproduced, assumed (1 to 2 memory terms in the top 10; 3 with one model per age) |
| fig4e-7m-go-immune-terms-up | reproduced under every reading |
| fig4fg-ecm-go-terms | not reproduced, assumed (no ECM term significant at 7 M against control) |
| fig4h, fig4i-3m, fig4i-7m, fig4i-common | reproduced (every named gene changes in the stated direction; most changes are small and not significant) |
| 22 immunohistochemistry claims (Figures 1, 3B, 3G, 5I, S1 to S6, S9, and PNNs at 5 M) | blocked, data_missing |
| 19 behaviour claims (social memory in Figures 2, 3, 5, S8; object recognition in Figures 2I to 2K, S7) | blocked, metadata_insufficient |
| fig4a-7m-social-memory-deficit | blocked, data_missing |

## 2. What was found about the dataset

- **No data in the NWB files.** All 481 files are 185,480 bytes and hold only file-level metadata; acquisition, processing and analysis are empty, and the stimulus groups have no members. The images are named in the identifiers but not deposited.
- **Behaviour videos can't be linked to the paper's groups.** The 175 MP4 files sit outside NWB with no subject, genotype, treatment or trial labels. Each frame shows several arenas, and the counts don't match the paper's mice (for example 15 videos for 16 mice in Figure 2B). The scored interaction and exploration times are not deposited.
- **Duplicates.** The object recognition videos are deposited four times (Fig 2I, 2J, 2K, Sup Fig 7), and Trial 6 and Trial 7 are the same file in each set: 28 assets hold 6 recordings.
- **Description errors.** The description says the dandiset includes RNA-seq data; it holds none, and the counts are only in GEO GSE317499. It also keeps a placeholder sentence naming "GSEXXXXX".
- **Subjects are group labels, not animals.** There are 82 subject_ids for 481 files, and sex is "U" in 476 of them.
- **GEO metadata.** Sample GSM9473154's library name (20790) differs from its run name (20690).

**Assumptions:**
- One DESeq2 model on all 16 samples with unshrunken fold changes, following the DESeq2 vignette's advice to fit all groups together.
- GO terms limited to 10 to 500 genes (clusterProfiler's defaults).
- GO release 2024-06-17 as a standard choice.

**Question for the paper's authors** (recorded as a methods_unavailable finding): which DESeq2 design, shrinkage, enrichment tool, background, term-size limits and GO release they used.

**Questions to a reader:** none.

## 3. Protocol points

1. The claims file's READINGS rule (written under pilot-10) blocks a claim as methods_underspecified when readings disagree. Step 1.6 of pilot-13 allows adopting the best-supported reading as an assumption. I followed pilot-13.
2. The protocol says only reader runs write the claims file, yet step 4 and the `entry.py` check expect the author to mark `data: elsewhere`. I added `data` and `where` to the nine RNA-seq claims and left statements, expected values and criteria unchanged.
3. The paper itself never names GEO; the dandiset's metadata does, and GEO links the paper's PubMed ID. I treated GEO as the authors' own deposit (`elsewhere`).
4. `archives.md` has no GEO section and GEO files have no version or DOI. I pinned the counts file by its SHA-256.
5. Nothing covers non-NWB assets such as MP4 videos. I read them with PyAV over remfile, behind a small wrapper because remfile fails when PyAV reads past the end of a file.
6. The GO annotations are a method input that neither the paper nor the claims file names, which step 4 doesn't cover. I pinned them by Zenodo DOI and listed them under `inputs`.
7. The protocol doesn't say whether a port of the paper's software is acceptable. I used pydeseq2 0.5.4 in place of R's DESeq2 1.44 and recorded it as a deviation.
8. The `measured` rule only covers readings that match. Where none do, I recorded the adopted reading's values.
9. The clock check of step 2 doesn't apply: the dataset has no time series. The notebook says so.

## 4. Runtime and failures

- The run took about 1 h 20 min (10:26 to 11:43 UTC); the notebook takes about 9.5 min, mostly the six DESeq2 fits.
- The first full execution failed at the video probe (the remfile problem above); the wrapper fixed it.
- I caught a bug before recording: the gene-direction helper rounded values before taking their sign. That made a positive Mmp3 change of 0.0003 count as zero.
- Nothing failed in the final run.
