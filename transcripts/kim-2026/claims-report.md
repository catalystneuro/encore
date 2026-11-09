I wrote `claims/001868/10.64898-2026.06.05.730421.yaml`. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, from its JATS XML. It has the main text, the legends of Figures 1 to 7 and the Methods. There is no PDF.

**Missing from the paper text:** the supplement (figs. S1 to S9 and their legends). Its "Supporting information" section is empty. I went ahead because the main findings rest on Figures 2 to 6, which are in the text. Ten claims rest on supplementary figures (S2, S3D, S4, S5, S6, S7, S8, S9). Each quotes the main-text sentence that states the finding and takes its method from the paper's code for that figure; the figures themselves could not be read.

**Code read:** github.com/XieLuanLab/icms-activation-plasticity at commit d1922d16 (Zenodo 10.5281/zenodo.19561006). It holds the Python figure scripts for the electrophysiology, the MATLAB scripts for the imaging and the upstream processing pipeline. It settled most method details the Methods leave open: how weeks are numbered, the unit filters, the pulse-locking test and its null, the modulation score, the psignifit settings, the KL bootstrap, the cluster test and population coupling.

**Claims:** 36. All 36 have quotes and criteria, 18 record statistics and 12 have expected values. All are `data: dataset`. The paper's Zenodo deposits are named in the opening comment, but no claim needs them.

**Quote check:** the checker passes every quote. It flags one value, p = 2.0e-4 in `fig4i-pyramidal-modulation-increase`, which it cannot match in that format. I confirmed by reading that the text prints exactly that value (line 93).

**Details left open, with the readings named:**
- **Which sessions count for thresholds (Fig. 2A):** every session with a threshold, or only sessions where 4, 5 and 6 µA were all given on that channel.
- **Form of the exponential fit (Fig. 2A):** with or without an offset.
- **The representative animal (Fig. 2B):** not named; every animal and channel at 4 µA is searched.
- **Animals in Fig. 2E:** the legend says all 6; the script uses the first 5.
- **Week-0 comparison group (Fig. 3N):** the legend says all tracked neurons at week 0; the code uses the high-intensity subgroup at week 0.
- **High-intensity subgroup threshold (Fig. 3J):** a per-animal threshold on each neuron's last value (the processing code) is the main reading; the pooled weeks 3 and 4 threshold (the figure script) is a variant.
- **Fig. 3D to F test:** the legend and one script use a Wilcoxon signed-rank test; another script uses a rank-sum test, kept as a variant.
- **Unit-level PL label behind "265 PL and 219 NPL":** the two-step majority rule, or PL if any of the unit's responses is pulse-locked.
- **Group-level modulated-unit test (Fig. 4G):** the paper names none; read as the same one-sided test at each of 4, 5 and 6 µA.
- **Firing-rate traces for the hit-miss cluster test (Fig. 6D):** built outside the repository; 10 ms bins with 20 ms smoothing, or 2 ms bins with 5 ms smoothing. The code takes the last significant cluster's onset; the first is also reported.
- **Movement-onset definition (fig. S5):** not in the Methods or the repository code.
- **Imaging short-window measures (fig. S6):** read as recruitment count and subgroup amplitude.
- **Jitter (fig. S4):** read as the SD of latency, with its square as a variant.
- **Control spike threshold (fig. S7):** the code uses 15 spikes against 50 in the Methods; 50 is the variant.

**Problems in the paper and code:**
- The text says newly recruited neurons had "shorter" spike onset than week 0 at p = 0.479, which is not significant. That part is reported but not judged.
- The paper's data statement and the code README give different Zenodo DOIs (17727762 and 21382755).
- Whether the dandiset holds the control mice is for the author to find. The two control claims and the control part of the fig. S9 claim are blocked if it does not.
