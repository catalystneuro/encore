I'm stopping without writing a claims file. The paper's statistics are in a supplementary table that isn't under `paper/`, and the protocol says to stop when a supplement the results rest on is missing.

**Text read:** `paper/10.1038-s41586-020-2728-4.txt`, the NIH author manuscript (PMC7606611) as served by Europe PMC. It has the main text, the full Methods, the Extended Data legends 1 to 10 and the legends for Figures 1 to 4. There is no PDF.

**What is missing: Supplementary Table 1 (`1606924_Supp_Tab1`).** The text only names it. The Figure 1 legend, which applies to all figures, says: "Exact p-values and statistical tests used are reported in Supplementary Table 1." The paper reports its significance results only through that table:
- **Tests not named elsewhere:** the main text and legends mark results as "significantly" or "not significantly different" without saying which test. The Methods' Statistics section mentions only the t-test and the asterisk levels. The legends name a test only for Fig. 1l and ED 3j (repeated-measures ANOVA), ED 3h (linear regression) and ED 4d (paired t-test).
- **Absence claims can't be written:** the protocol requires the paper's own test and threshold for a claim of absence. Without the table that can't be done for several findings:
  - the TetTox peak response "was not affected" (Fig. 1q);
  - freezing, jumping and velocity "not significantly different from controls";
  - no thigmotaxis from lingering odour (ED 2);
  - velocity unchanged by iC++ (ED 3b).
- **Comparative findings have no statistics:** the following findings would have no `statistics` entry and no test for their criterion:
  - rat responses stronger and longer-lasting than mouse or toy rat (Fig. 1e, g, h);
  - iC++ silencing of thigmotaxis and avoidance (Fig. 1j, m, n);
  - faster decay with TetTox (Fig. 1r);
  - population decay constants (Figs. 2d and 3b);
  - above-chance decoding (Fig. 3m).

The text alone gives only a few numbers. The rat-evoked decay constant is 26.7 ± 2.2 s. Of the imaged cells, 74.4% responded to at least one stimulus, 43.6% of those to only one, and over 70% to two or fewer. Imaging covered n = 5 mice, with 187.3 ± 8.1 cells per day and 78 cells tracked across days.

**Not done:** I did not read the linked code (github.com/DJALab/VMHdm_persistence) or look at the dataset's archive entry, since no claims were going to be written.

**Counts:** 0 claims, 0 quotes, 0 statistics, 0 criteria. No open details or readings were named. Nothing was written under `claims/001182/`.

**To proceed:** add Supplementary Table 1 to `paper/` (it's in the Nature supplementary information, or as `1606924_Supp_Tab1` in PMC7606611). The published PDF would also help for reading values off the figures, though the protocol doesn't require it. Then re-run the reader.
