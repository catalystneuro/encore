The file is ready for an attempt. I corrected three wrong paragraph references and five method details that were stated as fact or invented, and recorded them all under `checks`. Nothing was committed.

**Checker result** (it passed both before and after my edits): `claims/figshare-24949470/10.1038-s41597-024-03777-0.yaml: 18 claims, 17 quotes, 0 statistical values, 0 problems`

**Changes, by claim**
- **collection-window**: I removed the "partially reproduced at 99% of rows inside the window" rule, because the paper gives no such share. The time zone of the timestamps is now marked open, with two readings: dates as given, or UTC converted to Slovak time. That matters because the day a response near midnight falls on depends on it.
- **party-self-placements**: the source is paragraph 4 of "Party selection and coding", not paragraph 3.
- **coder-agreement-kappa**: the source is paragraph 3, not paragraph 2.
- **uni-and-landscape-placements**: the criterion said "No Opinion" party positions are left out, but the paper doesn't say how they are handled. I marked it open, with two readings: left out, or scored as 50.
- **party-clustering**: the source is paragraph 7 of "Content validation", not paragraph 6 (paragraph 6 is the factor analysis). Which party positions were clustered (final or expert-coded) is now marked open.
- **table2-gender, table2-age, table2-education**: I added a reading that counts only rows where gender, age and education are all given. The gender, age and education sections of Table 2 each add up to the same 107,965, which points to that. The gender statement now says "of the responses counted in Table 2" instead of "with gender given".

I found nothing to correct in the other claims. The paper's main findings each have a claim, and every claim comes from this paper.

**Still open**
- **R code not read.** The paper's R code sits in the same Figshare item as the data, so I didn't open it. It may settle which rows Table 2 counts, the factor-analysis settings, how the party positions were recoded for clustering, and how the dimension scores were computed. The author should read it.
- **efa-loadings-consistent** depends on cut-offs the paper never gives: what counts as a "strong" loading (0.4 or 0.5) and "consistent" results (at least 35 of 39 statements). The file says these are its own choices, so any outcome there rests on an assumption.
- **Supplementary Table 1 and Figs. 2, 3 and 7** are not in the text I read. The expected party placements and the clustering result have to be read from the published figures.
