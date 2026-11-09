I wrote `claims/001266/10.1038-s41467-025-55819-9.yaml` with 55 claims. The checker passes every quote but exits with one problem: it cannot find the p-value 5.0 × 10⁻⁴ in figs24-drugs-selective. The Fig. S24 legend prints it as "p = 5.0 x 10-4", a form the checker doesn't recognise. I confirmed it by reading and left both the quote and the checker as they are. Nothing is committed.

**Text read.** The version of record (PMC11794848, Europe PMC full text) with its Methods. Also read: the Supplementary Information (Figs. S1 to S25), the Peer Review File and the Description of Additional Supplementary Files. The Reporting Summary had no extracted text. The other file under `paper/` is an earlier bioRxiv preprint with a different title, so I did not use it.

**Code.** The paper links no analysis code; the analysis was done in MATLAB and not published. Its only code is two simulation packages from the journal site (no repository or commit exists), and I recorded their sha256 hashes:
- **Supplementary Software 1:** the NEURON CA1 model.
- **Supplementary Software 2:** the two-compartment Izhikevich model. Its script differs from the Methods in two values (somatic reset −65 against −55, initial dendritic u −18 against −13). The Methods' values are the main reading and the script's are a variant.

**Outside material.** The dandiset's description points to the paper's Source Data file, which maps DANDI file names to figure panels and gives per-cell values. I pinned it by URL and sha256 and read only its index sheet. The dandiset appears to hold mainly example recordings for each panel. Whether it holds the pooled recordings is for the author to find.

**Claims.** 55 in total: one link claim (the Source Data index) and 54 findings.
- **Quotes:** all 55 have one, so none needed `inferred`.
- **Statistics:** 14 claims carry 20 statistical entries.
- **Expected values:** 30 claims have them. Tolerances are the paper's s.e.m. or s.d. where it gives one, otherwise 10%.
- **Criteria:** every claim has one.
- **Data:** 34 use the dataset, 17 use it with the Source Data index as labels, and 4 are model claims that use the paper's simulation code.

**Details the paper leaves open, and the readings named:**
- **High-pass filter for spike detection:** a 20 ms moving median, or a zero-phase Butterworth at 20 Hz.
- **dSpike threshold:** at the trough of the bimodal distal amplitude histogram, as Figs. 2b and S10c show. Pairing distal events with bAPs (within 5 ms) and the somatic threshold are standard choices.
- **AUC integration window:** until the cumulative area stops rising, or to the end of the stimulus epoch.
- **Which files are which panels:** the legend's labels and the file names differ (Fig. 2 "D1" is file D3; Fig. 3 "D2" could be file D2 or D4). Files are matched to panels by the legend's trial and event counts, and both readings for D2 are run.
- **Length constant (255 µm):** which 93 spikes, and whether the exponential fit has an offset.
- **Peak distance (313 µm):** ratio of averages, or average of single-trial ratios.
- **bAP velocity:** a line fitted to distance against delay, or the mean of segment velocities.
- **Fig. 3i:** stimulus distance as the eYFP centroid or the nearest point of the stimulus polygon; plateau as the logistic asymptote or the mean beyond 300 µm.
- **Ramp 92%:** text says 188 ramps, the Fig. S13 legend says 225 bAPs; both readings run.
- **Fig. 4b window times:** per-trial first and last dSpike, or binned pooled fractions.
- **Fig. 5d:** the fit forms, with the sign of the time offset read from the legend's fit ranges.
- **Fig. 5f and 5h:** the text gives 7 cells and the legends 8; both are run.
- **Fig. S18e:** which Ni²⁺ concentration it pools.
- **Fig. S24:** which response its p-values compare.
- **Fig. S25:** "dSpike probability by any bAP" as a fraction of bAPs or of trials.
- **Undefined measures:** the noise-equivalent voltage and the ~130 pA CheRiff current estimate have no stated method.
- **No test given:** for claims such as bimodality, "two motifs" and the 15 ms rule, the criteria name a test and say that it is not the paper's.

**Places where the paper disagrees with itself (recorded as found):**
- 4-AP: the text gives p < 0.001 and the legend p = 0.001.
- Temperature, any bAP: the text gives p = 0.02 and the legend p = 0.03.
- Fig. 5f and 5h: n = 7 in the text and n = 8 in the legends.

**Missing from the paper:** nothing that would stop the claims file. The gaps that matter are the missing analysis code and the unspecified filter, threshold and integration window. These are named as open in the criteria, with the readings listed above.
