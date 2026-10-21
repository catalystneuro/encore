I haven't written the claims file. The write was stopped by a safety classifier, and I won't retry that content, so `claims/001414/` is still empty and there is nothing to check or commit.

**What was read:**
- **Version:** the published PNAS version, as served by Europe PMC (PMC12260423).
- **Main text:** Results, Discussion, Materials and Methods and all figure legends.
- **Supplement:** the SI Appendix PDF from the PMC Open Access supplement, as extracted text. It holds the SI Materials and Methods, the legends of Figs. S1–S6 and Tables S1–S4.
- **Not there:** the main-text PDF was not supplied, so I could not see the main figures.
- **Code:** the paper links none. It says the analysis was done with custom MATLAB scripts after ImageJ preprocessing, and the statistics in Prism 10.
- **Dataset:** the archive's title and description only name the paper.

**What I had drafted** (planned at about 50 claims, all quoted, none `inferred`; none written, so there are no final counts):
- **Statistics:** the tests reported in the legends of Figs. 1–6, S1, S2, S3, S4, S5 and S6, recorded with their F/t values and p-values.
- **Expected values:** the means ± SEM in Tables S1–S4, with the SEM as tolerance, and the single values in Table S3.
- **Criteria:** each one referred to a common method taken from the SI Image Data Analysis section.

**Details the paper leaves open, and the readings it allows:**
- **80% decay time:** the time to fall to 80% of the peak (the Fig. 1E legend's wording), or the time to fall by 80% (which fits "decayed to baseline").
- **Start of the post-LED window:** LED onset or LED offset.
- **Units of the area under the curve and the maximum dilation rate:** sum over frames or integral over seconds, in percent or as a fraction.
- **Dilation duration:** clipped at the end of the analysis window or not.
- **Delay between cAMP and dilation:** peak to peak of the two derivative traces, onset to onset, or cAMP derivative peak to dilation onset.
- **Time-to-peak:** measured from LED onset, or from the cAMP peak.
- **Excluding "large" vasomotion (Figs. 4 and 6):** no threshold is given.
- **Arterioles seen in more than one recording:** averaged into one value, or each recording counted.
- **Tests for bPAC against control cAMP and Ca²⁺:** none is named. By the Methods it would be an unpaired t test, per recording or on each mouse's mean.
- **Correcting bleaching across recordings:** the form of the fit is not stated.
- **Fig. 4G–I:** df = 34 does not fit 41 + 34 arterioles, so Student's and Welch's t test are both possible readings.

**Gaps and contradictions in the paper that the claims needed:**
- Without the main figures, I can't tell which pairs are starred in Figs. 1G–J, 2D, 2G–H and S1P.
- Fig. 2D prints "F = 0.0041, P = 0.0041".
- Table S1 says "recordings #1 and 6" for the 25 ms stimulation, but each session had only four recordings.
- The Results say shorter LED stimulation gave faster Ca²⁺ rise times, but Table S4 shows the opposite.
- The text calls the Ca²⁺ peak "markedly reduced" in IP3R2⁻/⁻ mice, but the paper's own genotype test gives P = 0.1247.
- The n of the two-photon Mlc1-PinkFlamindo experiment (Fig. S1K) is not given.

The claims file needs a new reader run.
