I wrote `claims/001708/10.64898-2025.12.15.693905.yaml`. The checker passes every quote. It flags one value, explained under "Checker result" below.

**Text read.** The bioRxiv preprint, version 4 (June 4, 2026), with its 13-page Supplementary Information. The supplement was missing in the earlier run and is now in `paper/`; it holds Tables S1–S11, Figures S1–S11 and the supplementary notes. The PDF's title is "Multi-timescale dynamics organize descending pain modulation". The task's title is the title of the code repository, and the DOI and dataset reference match.

**Code read.** `nox-lab/multi-timescale-rhythmic-dynamics-in-rvm-neurons` at commit e12f3ee771f4b5506e5db0bac09762ba6044a4d6: the analysis package and the notebooks with their outputs.

**Counts.** 33 claims, all with quotes and criteria, none inferred. 12 claims carry statistics: 54 values, a mix of 97% HDIs and permutation-test p-values. 20 claims have expected values.

**Checker result.** One flag: the ON switch-time HDI bound −0.27 s. The paper prints it as "0.27–0.095 s before" withdrawal, so −0.27 is the right value and I left it.

**Details the paper leaves open, and the readings named:**
- **Model comparison (ELPD):** estimated by PSIS-LOO or WAIC. "Significantly" is read as a gap of more than 1 or more than 2 standard errors of the difference.
- **Ongoing NEUTRAL cells in the GP fits:** a 1500 s cut (the code) or the whole recording (the Methods). For the 960 s cells the train/test split is at 660 s (notebook) or 700 s (`params.json`). The training run is 10000 iterations (`params.json`) or 100 (the notebook's last call).
- **FWHM in seconds:** the paper does not say how it converted from Hz. Three conversions are named. The code's stored results (peaks at 288.9 s and 303.3 s, about 17.8 s and 11.4 s FWHM) do not all match the text (286.86/16.92 s and 298.33/16.12 s).
- **What counts as a "clear minimum" or "flat" NLML profile:** a local minimum within 10% of the period on profiles normalized per cell. I set the bounds for "near" and for the one NEUTRAL exception.
- **Coherence:** cells counted if coherent at any frequency (the code) or below 0.01 Hz ("low-frequency" in the text). Counts at other surrogate seeds are also reported.
- **Heart-rate peaks (Fig. 6d):** "multiples" read as harmonics or subharmonics of 300 s. The beat train is taken over the 1500 s segment or the whole recording.
- **Absence claims with no test in the paper:** the NEUTRAL PSTHs (Fig. S3) and phase against latency (Fig. S2) are only inspected visually. I named the tests (Wilcoxon signed-rank over 2 s windows; Spearman and circular-linear correlation) as open.
- **Averaging:** latency and heart-rate means over trials or recordings, or over animals.
- **Cell and animal counts:** two groupings, the Methods' and Table S11's.

**Where the Methods and the code disagree** (the Methods are the main reading, the code a variant):
- Prior on the OFF slope k: on k itself (Methods) or on log k (code).
- Inducing points: 200 or 100.
- Outlier contamination term: 0.001 or 0.01.
- Edge trim in the period scan: 2 s or 4 s.
- Period-scan range: the Methods say 0.1–500 s, but the Results and code say 0.1–1500 s. I used 1500 s, because a 500 s scan cannot show the reported minima at 600 and 900 s.

**Inconsistencies inside the paper:**
- The text's HDIs for the switch times differ from those in Tables S3 and S7.
- Animal counts: 53 + 30 in the Methods, 103 in Table S11.
- Units for the sigmoid slope k (s⁻¹ in one place, spikes per bin in another).
- The code's own output gives the linear Gaussian CDF model a higher ELPD (−6263.78) than the matching sigmoid model (−6264.95), against the text's "significantly worse".

**Missing:** no code for the heart-rate power spectrum (Fig. 6d) is in the repository, so that criterion rests on readings of the supplement alone. Nothing else a claim needed was missing.
