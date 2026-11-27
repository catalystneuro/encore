I wrote `claims/russo-2025.yaml` (not committed). It has 39 claims, and every one has a word-for-word quote, so none needed an `inferred` note. The checker passes everything except one p-value: the paper prints "p = 1.11e-04" in the Figure 4E legend and the checker only looks for "1.11e-4". I confirmed that value by reading the legend and left the checker alone.

**Text read.** The version of record from PubMed Central (main text, Methods, legends), the supplement PDF as text (Figures S1 to S14 and Table S1), and the Source Data spreadsheet. No PDF page was opened. Nothing the claims needed was missing from the paper.

**Code read.** The mouse analysis on figshare (doi:10.6084/m9.figshare.28047749 v1). It is a copy of AllenInstitute/tbd_eeg at commit ef9aa65 plus the paper's notebooks; I read the relevant cells of MainScript.ipynb and the wheel-speed notebook. I also read the human scripts (figshare 25595829 and 25595871). I did not read the model code or the simulated-data analysis.

**Claims**
- **Data:** 22 claims use the dandiset (1 of them is a `link` check against the Source Data). 17 are `data: elsewhere`:
  - 6 human claims: only the per-subject values in the Source Data file are public.
  - 3 optogenetics claims: the processed data are on figshare (article 28440311).
  - 5 simulation claims: the model on GitHub plus the figshare analysis code.
  - 1 human claim (Figure 5A, human against mouse traces) has no public data, so it is untestable unless the author finds the human grand averages.
- **Statistics:** 36 claims record the paper's tests, 81 p-values in all.
- **Expected values:** 15 claims carry numbers to match. Tolerances are the paper's SDs where it gives them, otherwise 10%.
- **Criteria:** all 39 have one.

**Details the paper leaves open, with the readings named**
- **Unit and intensity for Figure 1C (mouse EEG):** (a) high intensity only, one value per session; (b) high and medium intensity as separate sessions, which is what the code does. The same choice applies to the LFP and CSD panels.
- **EEG channel and trial exclusion:** the paper uses visual inspection and the code a lab spreadsheet that isn't deposited. Readings: (i) keep all channels and trials; (ii) drop any the dandiset flags as bad.
- **EEG rectified amplitude:** the Methods (absolute value of the averaged response) are followed. The code's version (average of absolute single trials after baseline z-scoring) is a variant.
- **Unit of the rest against active unit tests (Figures 3A and 3E):** the Methods say Wilcoxon signed-rank; the code uses rank-sum on per-trial or per-session values. Readings: (a) per trial with rank-sum, as in the code; (b) per unit or per mouse with signed-rank, as in the Methods.
- **Window for the evoked ISI, onset variability and response frequency:** (a) 150 to 250 ms, from the Methods; (b) 75 to 250 ms, from the code.
- **HF against LF in Figure S11D:** the paper names a signed-rank test, but HF and LF are different units. Readings: per-mouse pairs, or rank-sum on units.
- **Mixed-model transforms (Figure S13):** raw values, or the code's logs and centring.
- **How the 127.8 ms off period was measured:** neither the paper nor the code says. I named two readings of my own, based on the Results wording.
- **Speed thresholds "up to 5 cm/s":** the grid of 0.1, 0.5, 1, 2 and 5 cm/s is my choice and is stated as such.
- **Quality thresholds for sorted units:** the paper only cites Siegle, Jia et al. Readings: units as deposited, or filtered by any quality labels the dandiset carries.
- **Pearson or Spearman for the human early against late correlation:** the text and the legend disagree, so both are run.

**Where the claims can't use the paper's own test**
- The human iEEG mixed models need per-contact values, which aren't public. Those claims fall back to tests on the five per-subject Source Data values, recorded as a deviation.
- The lab spreadsheet behind the code's session flags and bad channels or trials isn't in the deposit, so those selections stay open as named above.
