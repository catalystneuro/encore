# 001702, Chaunsali et al. 2025

No claim reproduced, none partially, none not reproduced and 42 blocked, 23 for
missing data and 19 for insufficient metadata; no outcome rests on an
assumption. Of the 51 claims, 42 are on the dandiset and nine, on the bulk
RNA-seq counts, use data in GEO (GSE317499) and are counted apart: five
reproduced, one partially and three blocked as methods underspecified. The
first verification round agreed with 49 of the 51 outcomes as they stood and
the second with all 51, and nothing was proposed after the second, so there was
no third round. It pins version 0.260216.2323, the only published version; the
paper cites none, and the draft has the same 656 assets. The paper, Chaunsali
et al., "Degradation of perineuronal nets in hippocampal CA2 explains the loss
of social cognition memory in Alzheimer's disease", reports the loss of
perineuronal nets (PNNs) in CA2 of 5XFAD mice from immunohistochemistry
(Figures 1, 3B, 3G, 5I, S1 to S6 and S9), social memory and object recognition
in these mice and after aggrecan knockout, chondroitinase ABC and GM6001
(Figures 2, 3, 5, S7 and S8), and the bulk RNA-seq of CA2 at 3 and 7 months
(Figure 4). The claims were written from the version of record in Europe PMC
(PMC12541281) without a PDF, so the figures were not seen, and without the
Supporting Information (Figures S1 to S9, Tables S2 to S4), which holds every
exact p-value and the RNA-seq analysis, or the published correction (e71098);
the paper links no code. The check made six corrections and left four points
open. Only the nine RNA-seq claims could be tested, on the GEO counts pinned by
their SHA-256, with pydeseq2 0.5.4 in place of R's DESeq2 1.44, which R could
not be pinned to check. Reproduced are `fig4e-7m-go-immune-terms-up` (5 to 8
immune or defense terms in the top 10 under all 16 readings, smallest z 4.47),
`fig4h-pnn-synthesis-genes` and the three Figure 4I claims, which the criteria
judge by sign only, so near-zero changes count (Adam10 +0.003, Timp2 +0.07 with
adjusted p 0.92). Partial is `fig4c-7m-degs`: the up count (284 to 320) is
within 314 +/- 31.4 under every reading and the down count (0 to 7) never
within 6 +/- 0.6, a tolerance that admits only exactly 6. Blocked as methods
underspecified are `fig4b-3m-degs`, where one model per age with unshrunken
fold changes gives 95 up and 136 down, one model on all 16 samples gives 51 and
141, and shrunken fold changes give 88 and 45 and 39 and 37;
`fig4d-3m-go-memory-terms-down`, reproduced in 2 of 16 readings, partial in 5
and not reproduced in 9; and `fig4fg-ecm-go-terms`, where one of 16 readings
(separate model, shrunken, all annotated genes, no term-size limit) gives an
ECM term at adjusted p 0.048 and the other 15 none below 0.05. That block rests
on running the term-size limit as a reading, which the claims file does not
list: with one DEG fewer the value would be 0.113, release 2024-01-17 gives
0.046 and release 2025-03-16 gives 0.052, where all 16 readings give not
reproduced. The author's first run adopted one reading where readings
disagreed and gave fig4b and fig4d partially reproduced and fig4fg not
reproduced, all on an assumption. The author asked no questions of a reader,
and `questions/001702.yaml` did not exist, so the answer and author-answers
runs changed nothing. Round 1 disagreed with fig4b and fig4d, which the claims
file's READINGS rule blocks, and found that pydeseq2 filters at alpha 0.05
where R uses 0.1, that the 10 to 500 term-size limit was the author's choice
and decides fig4d, and that the fig4fg criterion's adjusted p < 0.05 may be
stricter than the legend; in reply the three GO and DEG claims were blocked,
the filtering was set to 0.1 with 0.05 as a variant, the term-size limit was
run as a reading, every reading's outcome and top 10 were printed, a tie-break
by term ID was added, and the fig4fg point was filed in `questions/001702.yaml`,
after the reader's run. Round 2 agreed with all 51 and asked that the 3 M
counts be corrected to 98 and 137 and 91 and 45 and that fig4fg be marked as
resting on an assumption; the author found that these are the counts at alpha
0.05 and kept 95 and 136 after refitting twice, and, as the schema does not
allow `assumed` on a blocked outcome, stated the term-size reading as a
deviation and added the two further GO releases. The author's run took about 1
h 20 min (10:26 to 11:43 UTC); the first full execution failed at the video
probe because remfile fails when PyAV reads past the end of a file, which a
wrapper fixed, and a helper that rounded fold changes before taking their sign
was fixed before recording; the notebook ran in 562 s at first, 452 s after
the author-answers run, about 10.5 minutes after round 1 and 663 s at the end.

None of the 481 NWB files holds data: each is 185,480 bytes and holds only
file-level metadata, and the identifiers name the image files of Figures 1, 3,
5, S1 to S6 and S9, but no image, ROI, table or measurement is deposited,
although the description says the dandiset includes the imaging data, so all
22 IHC claims are blocked, with `fig4a-7m-social-memory-deficit`, for which no
video or table belongs to the 7 M RNA-seq cohort. The 175 behaviour videos are
MP4 files outside NWB, named only by figure panel and trial number, with no
subject, genotype, treatment, DPI or trial-type label; several arenas share
each video, the counts do not match the paper's mice (15 videos for the 16 mice
of Figure 2B, 33 for the 26 of Figure 5E), and the scored interaction and
exploration times are not deposited, so none of the 19 behaviour claims can be
tested. The object recognition videos are deposited four times, under Fig 2I,
Fig 2J, Fig 2K and Sup Fig 7, and in each set Trial 6 and Trial 7 are the same
file, so 28 assets hold 6 distinct recordings. The NWB subject is a group label
(82 subject_ids for 481 files, up to 31 sharing one), so slices cannot be
grouped by mouse, sex is U in 476 of 481 files and session descriptions give
the region as Unknown. The description says the dandiset includes the bulk
RNA-seq data, which are only in GEO GSE317499, and keeps a placeholder sentence
naming "GSEXXXXX". In GEO, sample GSM9473154 has library name 20790 where its
run name carries 20690; the count matrix column matches it by sample number,
age and genotype. Questions are put to the paper's authors: which DESeq2 design
gave the DEG counts of Figure 4B and 4C and whether fold changes were shrunken,
and which enrichment tool, background, term-size limits and GO release gave
Figures 4D to 4G.

The author's points on the protocol: the claims file's READINGS rule blocks a
claim whose readings disagree while step 1.6 of pilot-13 allows adopting the
best-supported reading, and the first run followed pilot-13; only reader runs
write the claims file, yet step 4 and `entry.py` expect the author to mark
`data: elsewhere`, so `data` and `where` were added to the nine RNA-seq claims;
the paper never names GEO, which the dandiset's metadata names, and GEO was
treated as the authors' own deposit; `archives.md` has no GEO section and GEO
files have no version or DOI, so the counts were pinned by SHA-256; nothing
covers non-NWB assets such as MP4 videos; the GO annotations are a method input
step 4 does not cover, and were pinned by Zenodo DOI under `inputs`; the
protocol does not say whether a port of the paper's software is acceptable, and
pydeseq2 was recorded as a deviation; the `measured` rule covers only matching
readings, so the adopted reading's values were recorded where none match; and
the clock check does not apply, as the dataset has no time series.
