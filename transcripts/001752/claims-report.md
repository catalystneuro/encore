I wrote `claims/001752/10.1038-s41556-026-02009-4.yaml`. The quote checker reports 32 claims, 32 quotes, 8 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (Nat Cell Biol 28, 1742–1757; PMC13457102, via Europe PMC): main text, figure and Extended Data legends, Methods, and the data and code statements. There was no PDF, so p-values printed only inside figures could not be read. The Supplementary Information (Supp. Figs 1–17, Supp. Tables 1–12) and the Source Data were not in the text. The findings this dataset can test (Fig. 5a–c) rest only on the main text, the Fig. 5 legend and the Methods, so I went ahead. Claims that cite supplementary tables rest on the main text and say so.

**Code read.** github.com/RFLiu2021/AIC_proj at commit 44cd8a6. It holds per-figure MATLAB and Python scripts, per-cell tables of postsynaptic-current (PSC) results, and a table naming the deposited NWB files. The event detection itself is not in the code: it was done in miniAnalysis.

**Claims.**
- **Counts:** 32 claims, all with quotes; 4 with statistics, 25 with criteria, 9 with expected values.
- **Testable on this dataset (8):** for each of sEPSC, sIPSC, mEPSC and mIPSC, one claim that frequency is lower in VENs than in PCs, and one absence claim that amplitude does not differ. The test is a two-tailed Wilcoxon rank-sum on per-cell values.
- **Elsewhere (24):** the paper's other findings, each with its archive and identifier: DANDI:001746, 001750 and 001751, GEO, MetaboLights, NeuroMorpho, and the GitHub tables at the pinned commit.

**Details the paper leaves open, and the readings named:**
- **Event threshold:** the Methods say "maximus root mean squared noise level (5 pA)". The readings are (a) a fixed 5 pA and (b) each recording's own RMS noise. No other miniAnalysis setting is given, so a standard detector is named as a standard choice.
- **Duration analysed:** the Methods say the whole stable recording, at least 5 min. The code's mIPSC table uses 30 s per cell, which is shown as a variant.
- **sEPSC PC group:** the paper's n = 11 entries contain one cell (20201126s1c2) twice. The readings are (a) the 11 entries and (b) 10 distinct cells.
- **IPSC event polarity:** the Methods hold IPSCs at −60 mV, but the code names the sIPSC files "+20mV". Events are detected in the direction implied by the holding potential each file records.
- **Alpha:** none is printed for Fig. 5b,c, so p < 0.05 is used as the conventional reading.
- **Fig. 3c:** the two-way ANOVA's second factor is not named. The readings are slice or animal.
- **Absence claims:** these are judged at the Methods' 5 pA threshold, with the other readings shown as variants.

**Code against deposit metadata.** For the mEPSCs, the paper's analysis sheet labels the cells VEN/PC the opposite way from the code's metadata for the deposited files. The sheet's eighth PC (S02C0321) is missing from that metadata, which lists 7 VENs where the paper reports 8. The mEPSC claims use the dataset's labels and report the sheet's labelling as a variant.

**Missing from the paper that a claim needed.** Three claims are marked blocked unless the material is supplied:
- `scrna-no-sex-difference`: its test is in Supplementary Fig. 3.
- `ven-firing-rate-variability`: its values and tests are in Supplementary Tables 1 and 2, and the measure of spike-timing variability is not named.
- `fig2d-f-l23-it-tau-width`: its adjusted p-values are in Supplementary Table 2.

The paper also does not say which dandiset holds the Fig. 4a–c and Fig. 4j recordings; I pointed to DANDI:001746 as the main electrophysiology deposit, and to the code's tables where they hold the values.
