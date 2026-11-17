I wrote `claims/simmons-2026.yaml`, and the quote checker passes it: 38 claims, 38 quotes, 36 statistical values, 0 problems. Nothing is committed.

**Text read.** The version of record (Science Advances, 9 September 2026) with full Results, Methods and legends, plus the supplement (Figs. S1 to S9). I opened PDF pages for Figs. 2 to 7 and S6 to read panels. Nothing the claims need was missing.

**Code read.** The code deposit (doi:10.5281/zenodo.10855006, now record 17297995) is one Mathematica notebook, "Code Sample.nb". It computes:
- spike rate per episode as spike count divided by episode length;
- a cell's rate as the median over a "stable" window that is chosen by eye;
- a PSTH.

Every window, bin and dropped episode in it is a placeholder. Spikes were detected in Clampfit, with no settings given anywhere.

**The file.**
- All 38 claims have a quote and a criterion; 31 have statistics and 12 have expected values.
- 15 are claims that a drug had no effect, each judged on the paper's own test.
- Two use outside data (`data: elsewhere`): Fig. 6D uses Dopabase, and Fig. S5 is a table from Gonzalez-Rodriguez et al. 2021.
- The opening comment names the paper's raw-data deposit on Zenodo (doi:10.5281/zenodo.10850896), but no claim's `data` field points to it.

**Details left open, with the readings named:**
- **Stable window (M1):** (a) all episodes of each condition; (b) for a drug, episodes from 6 min after application starts, which is when the Fig. 7G time courses level off.
- **Percent changes (M2):** (a) mean of per-cell changes; (b) change in group means; (c) median of per-cell changes. Only (a) and (b) where the paper says "mean".
- **Sidedness of tests:** not stated. Two-sided is used (the Prism default), with one-sided shown as a variant.
- **Unnamed tests (Figs. 6C, 7D, 7E, 7H, S3, S4D):** paired t test, with Wilcoxon as a variant.
- **Paired-pulse ratio (Fig. 1E):** the second peak measured either from the baseline before the first pulse, or from the current just before the second pulse.
- **IPSC amplitude (Figs. 1C, 4A):** not defined; peak from the pre-stimulus baseline is used and stated as a standard choice.
- **Fig. 2C percent inhibition:** basal rate from 0 to 2 s and train rate from 2 to 4 s, read from the figure; the PSTH value is the main one and a per-sweep median is a variant.
- **Fig. 2B waning:** the paper reports no test; I fixed 0.5-s windows at the start and end of the train.
- **Fig. 5D control group:** either the cells recorded alongside the shRNA experiments, or the same 18 control cells as Fig. 5F.
- **Fig. S2B test:** Student's unpaired t test, with Welch's as a variant.
- **Fig. 7F, quinpirole in SNAP-5114:** judged on Welch's test as the paper wrote it (an unpaired test on before and after values), with a paired t test as a variant.
- **Fig. S9:** which vigabatrin acquisitions count, and how the percent oligomycin- and 2-DG-sensitive parts are computed.
- **Fig. 4A "similar magnitude":** the paper gives no measure, so I fixed a margin of 10 percentage points.
- **Spike detection settings:** given nowhere.

**Where the text and the legends disagree** (both values are recorded, and a claim holds if the result matches either):
- Fig. 3B: n = 10 in the text, 45 in the legend.
- Fig. 3D: P = 0.13 in the text, 0.06 in the legend.
- Fig. 4A: P = 0.02 in the text, P < 0.01 in the legend.
- Fig. 4B: P = 0.19 in the text, 0.16 in the legend.
- Fig. S4E: the legend says 30 °C, the Methods say 32 to 33 °C.

**Missing from the paper:**
- Concentrations for NPPB, NNC-711 and CNO.
- The n for the Fig. 7F quinpirole test.
- How the Aldh1a1 KO mice in Fig. S6 were made, and which test was used there (the panels only say n.s.).
- The rule for calling an astrocyte D2R-positive (Fig. 7A).
- An accession or version for Dopabase and for the Fig. S5 source.

Two of the paper's P values sit right at the 0.05 threshold (Fig. 5E and S4D), so the size of each change is to be reported in full. The dandiset lists only voltage-clamp series, so the imaging, RNAscope and FSCV claims may not be testable on it; finding out is the author's job.
