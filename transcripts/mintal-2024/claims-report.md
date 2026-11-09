I wrote `claims/figshare-24949470/10.1038-s41597-024-03777-0.yaml` and the quote checker passes it: 18 claims, 17 quotes, 0 problems.

**Text read:** the version of record from Europe PMC (PMC11374779). That covers the main text, Methods, Technical Validation, Usage Notes, and Tables 1 and 2. There is no PDF.

**Counts:**
- **Claims:** 18.
- **Quotes:** 17. The gender rows of Table 2 have no sentence stating them, so that claim has an `inferred` note instead.
- **Statistics:** 0. The paper reports no tests or intervals. Its kappa, means and SDs are recorded as expected values with the default 10% tolerance. Counts fixed by the design (39 statements, 429 positions, 11 parties, 4 self-placements, 11 factors) get tolerance 0, with the reason given.
- **Criteria:** all 18 claims have one.
- **Outside data:** 2 claims use `data: elsewhere`. One is the official 2023 election results; the other is the platform's 270,836 website views.

**Missing from the paper:**
- **Supplementary Table 1** (the 39 statements, with their dimensions and polarities) is named but not in the text. No expected value rests on it. The uni-dimension and landscape claim needs its assignments. The factor analysis needs its list of reversed statements, but reversing items cannot change the factor count.
- **Figure content:** without a PDF, Figs. 2, 3, 4 and 7 are titles only. The two claims on party placements and the clustering dendrogram say the expected result must be read from the published figures.
- **Code not read:** the paper's R code sits in the same Figshare item as the data, so I did not open it, following the precedent in claims/001773. It may settle several of the open details below, and the author should read it.

**Details left open, with the readings named:**
- **Which rows Table 2 counts:** each block sums to 107,965, not 134,699. Readings are (a) cleaned rows with the variable not NA, or (b) raw rows with the variable not empty.
- **Age–education mismatches (40 and 400):** which rows, cleaned or raw. Also whether "university-level" means (i) the university category only, or (ii) both higher-education categories.
- **S2–S5 statistics:** which rows, cleaned or raw, with "no opinion" left out in both. For "more than n = 17,435" (and 23,344 for S5), the readings are (i) the count is about that number, or (ii) the count exceeds it.
- **Weighted kappa:** (a) linear or (b) quadratic weights; "No Opinion" either (i) dropped or (ii) scored as Neutral. The claim also needs each coder's separate positions in the dataset, which the author has to confirm.
- **Uni-dimension and landscape scoring:** the euandi formula is not given. Readings are (a) the mean of polarity-adjusted positions, or (b) a start at 50 moved by polarity-adjusted deviations.
- **Clustering recode:** "No Opinion" either (a) set to 50, or (b) left out of each distance.
- **Factor analysis:**
  - "No opinion" either (a) set to 50, or (b) treated as missing, pairwise.
  - The parallel-analysis settings are taken as psych's defaults, and the seed is reported.
  - "Strong loading" (reading (i) 0.4, (ii) 0.5) and "consistent" (the same top factor for at least 35 of 39 items) are thresholds I chose. They are marked as assumptions in the file.
- **Collection window:** Table 1's sample timestamp (2023-10-09) falls after the stated window. The time zone is not stated. The 99% share that counts as partial reproduction is my choice, not the paper's.

Nothing was committed.
