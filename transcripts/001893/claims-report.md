I wrote `claims/001893/10.1038-s41586-026-11026-0.yaml`. The quote checker passes: 29 claims, 29 quotes, 29 statistical values, 0 problems.

**Text read.** The version of record, from Crossref and the publisher's HTML (stored 2026-10-21): main text, Methods, figure legends and the Extended Data Fig. 1–15 legends. Supplementary Tables 1–3 are a PDF and are not in the text. The paper cites them only for injection coordinates, volumes and model priors, and no result rests on them. I also read the bioRxiv preprint v1, only to compare. The paper is titled "Topographic structure and function of locus coeruleus noradrenaline neurons"; "Patch-seq profiling of mouse locus coeruleus norepinephrine neurons" is the dataset's title on DANDI.

**Code read.**
- The linked index repository at commit 43f7083.
- `LCNE-patchseq-figures` at 79fa20a. It builds Extended Data Fig. 11j,k from dandiset 001893 version 0.260817.1647: 96 NWB files, with projection target and donor from `participants.tsv`.
- `LCNE-patchseq-analysis` at 1190697.

**Claims.** 29 in total, all with quotes; 16 have statistics, 29 have criteria and 12 have expected values.
- **Testable here (6 Patch-seq claims):**
  - Cell and mouse counts per projection target (96 cells, 28 mice).
  - Identity of each cell as noradrenergic. The transcriptomes are marked as held elsewhere, in NeMO collection col-p9d5w39.
  - Action-potential waveform, spinal cord against cortex (p < 0.01) and spinal cord against cerebellum (p < 0.05).
  - Membrane time constant, cortex longer than spinal cord and than cerebellum (both p < 0.001).
- **Not in this dataset (23 claims):** whole-brain anatomy, single-neuron reconstructions, MAPseq, retrograde tracing, snRNA-seq, MERFISH, retro-seq, in vivo recordings during behaviour, axonal photometry, and extracellular waveforms. The paper names where its data are only as a GitHub index, NeMO and a Code Ocean collection, without saying which data each holds.

**Details the paper leaves open, and the readings named:**
- **Which action-potential measure:** the legend names none. The code settles it, so the criterion follows the code: PC1 of the averaged rheobase spike waveform, with its windows, normalisation and spike detection, tested with a two-sided Welch t-test per cell.
- **Sweep inclusion for the waveform:** the Methods give a sweep quality rule that the code does not apply. Readings: (a) the code's, with no further rule; (b) the Methods' rule, applied where the files hold the values it needs.
- **Membrane time constant:** the code does not compute it; it reads a frozen IPFX value, missing for 14 of the 96 cells. Main reading: compute it with IPFX at default settings from the dataset, as the Methods say. Variant: the code's frozen table, which is an outside input.
- **How cell identity was confirmed:** not stated. Readings: (a) Dbh detected; (b) all four markers (Dbh, Th, Slc6a2, Slc18a2) detected; (c) the cell maps to the LC-NE type.
- **Go-cue responses:** the paper gives no threshold for counting a cell as responding. Readings: (a) paired t-test p < 0.05 with a higher rate after the cue; (b) a higher mean rate after the cue.
- **Outcome responses in space:** the test behind P = 3.0 × 10⁻⁴ is not named. The criterion uses the LDA trend test, which the Methods give for categorical labels.

**Inconsistencies in the paper, recorded in the file:**
- Fig. 3e gives χ²₂ = 29.9 with bootstrapped P = 10⁻⁴; Extended Data Fig. 15c gives the same statistic with p = 3.25 × 10⁻⁷.
- The preprint says "paired t-tests" for the Patch-seq comparisons; the version of record says two-sided Welch's t-tests. I followed the version of record.

**Missing from the paper.** Nothing the Patch-seq claims need. The only gaps are the details above that the code did not settle: how the time constant was computed, sweep inclusion, and how identity was confirmed.
