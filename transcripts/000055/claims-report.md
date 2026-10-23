I wrote `claims/000055/10.1523-eneuro.0007-21.2021.yaml`. The quote checker reports 0 problems: 23 claims, 21 quotes, 14 statistical values.

**Text read.** The version of record as served by Europe PMC (PMC8225404): main text, Methods, figure legends, Tables 1 and 2, and the review history. There was no PDF. The Extended Data figures are EPS downloads, so only their legends are in the text.

**Code read.** `BruntonUWBio/naturalistic_arm_movements_ecog` at commit 04c6faf2 (17 March 2021). It covers spectral power, the bootstrap masking, the projection onto brain regions, the regression, and the notebooks for Figures 2 to 6. It does not cover preprocessing, pose estimation, event detection, feature extraction, the Kruskal–Wallis tests of Figure 2, the confidence intervals of Tables 1 and 2, or Extended Data Figures 5-1 and 6-2.

**Claims.**
- **Count:** 23 claims. One is a link check (`subject-days`); 22 are findings.
- **Quotes:** 21 claims have a quote. The Table 1 claim is marked `inferred`, and the link check has neither.
- **Statistics:** 4 claims carry them, 14 values in all: Kruskal–Wallis tests across subjects, the 11 per-subject recording-day tests, and the bootstrap with FDR correction for Figure 3.
- **Criteria:** all 23 have one.
- **Data:** 12 claims are marked `with_inputs` because they need the AAL atlas to place electrodes in brain regions.

**Where the Methods and the code disagree.** The Methods are the main result and the code's choice is shown as a variant:
- Band power: the Methods say "averaged" (mean); the code takes the median.
- Train/test split: 90/10 in the Methods; 80/20 with days balanced in the code.
- ΔR²: the Methods score the shuffled model on unshuffled withheld data; the code shuffles the test events too.
- Log transform: the code also log-transforms onset speed.
- Electrode selection for Figure 6b–d: the legend's R² > 0.05 is applied per band; the code selects by the low-frequency R² for both bands.

**Details the paper leaves open, and the readings named for each:**
- **Events counted:** all events in the dataset, or only those left after removing false positives and artifact segments.
- **"At movement initiation" in Figure 3:** the mean over 0 to 0.5 s, or the time bin nearest 0 s.
- **"Largest in magnitude" in Figure 3:** mean absolute power over all frequencies, per band, or over −0.5 to 0.5 s.
- **"More widespread" for low frequencies:** a count of regions, or a count of significant bins.
- **Tables 1 and 2 intervals:** whether they are for the mean or the median, crossed with mean or median band power (four readings).
- **Extended Data Figure 5-1 SD across days:** per subject in the precentral region, or per electrode.
- **Unit for the absolute 10–50 dB level:** microvolts or volts.
- **Figure 6b area assignment:** each electrode goes to the region with its largest weight, or R² is projected onto the regions.
- **Extended Data Figure 6-2 projection:** the paper gives no method; I used a weighted mean projection, as for power.
- **Words the paper gives no measure for:** "most", "bimodal", "skewed", "waking hours" and the per-subject features of Figure 4. Each criterion says how I read them, as the reader's reading and not the paper's.

**Missing from the paper.** The Extended Data figures themselves (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2):
- The per-subject electrode counts (1-1) and the per-subject confidence intervals for the features (2-3, 2-4) could not be read.
- The claims on 2-2, 5-1 and 6-2 rest on their legends and on the Results sentences that cite them.

The paper's curated data, including the projection matrices, are on Figshare and are named in the opening comment. Subjects S01 to S12 are assumed to match the dataset's subjects 01 to 12 in order; the `subject-days` link checks this against the days listed in Table 2.
