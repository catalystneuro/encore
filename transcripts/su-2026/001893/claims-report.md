I've written the claims file for DANDI:001893 at `claims/001893/10.64898-2026.04.10.717727.yaml`. Nothing is committed. The quote checker passes all 25 quotes. It also reports two "VALUE NOT FOUND" lines: both are p = 3.0e-4 (fig5g, fig6a), which the text prints as "3.0 × 10 −4". I confirmed both by reading the text; the checker just doesn't match that format, the same issue recorded in 001950's checks.

**Text read:** the bioRxiv preprint, version 1, from the JATS XML: Results, Discussion, Methods, and the legends of Figures 1–6 and S1–S18. There is no separate supplement file and no PDF, so the supplementary figures exist only as legends and no panel was seen. The extraction lost the Methods' equations and the contents of Table 1; nothing in the Patch-seq claims needs either.

**Code read:**
- The index repository, `locus_coeruleus_norepinephrine_neurons` at commit 43f7083.
- `LCNE-patchseq-figures` at commit 79fa20a, which makes Figure S14j/k directly from DANDI:001893 version 0.260817.1647.
- `LCNE-patchseq-analysis` at commit 1190697.

**Dataset:** it holds the Patch-seq experiment only: 96 cells from 28 mice, labelled from frontal cortex (27), cerebellum (15) or spinal cord (54). That is Figure S14j/k and Results paragraph 5.

**Claims:** 25, all with quotes. 15 have statistics entries (18 values) and 12 have expected values. 6 have criteria, all on the Patch-seq experiment:
- cohort counts
- action potential waveform, spinal cord against cortex
- action potential waveform, spinal cord against cerebellum
- membrane time constant, cortex against spinal cord
- membrane time constant, cortex against cerebellum
- each cell's identity as an NE neuron, marked `data: elsewhere`

The other 19 cover the paper's anatomy, transcriptomics and in vivo findings without criteria, since this dataset is not described as holding those data.

**Details the paper leaves open, and the readings named:**
- **Test:** the S14k legend says "paired t-tests", which can't apply to different cells in groups of unequal size. The code uses two-sided Welch t-tests per cell; I follow the code, with Student's t-test as a variant.
- **Waveform measure:** the paper says only "action potential waveforms". The code fixes it as PC1 of averaged spike waveforms (rheobase sweep, −10 mV peak detection, −5 to 10 ms window, min-max normalisation over −2 to 4 ms, PCA over −3 to 6 ms). I follow the code.
- **Sweep inclusion:** the Methods give inclusion criteria; the code applies none. The Methods are the main reading and the code's choice is a variant.
- **Membrane time constant:** the Methods say IPFX, but give no version or settings. The code reads frozen per-cell values from Allen's internal database, missing for 14 cells. The main reading is IPFX defaults, recorded as a deviation, with the frozen table as a variant to compare cell by cell.
- **NE identity:** the paper doesn't say how identity was confirmed. Readings are (a) Dbh detected, or (b) all four markers it names (Dbh, Th, Slc6a2, Slc18a2) detected.

**Missing:**
- The paper names no archive for the Patch-seq transcriptomes. The code's README names a NeMO collection (col-p9d5w39), pinned only by that identifier and described as not used for the paper's figures. The identity claim points there.
- The paper gives no direction for the waveform difference, so those two claims test difference only.
