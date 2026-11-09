I wrote `claims/001326/10.1126-science.adt3971.yaml` with 50 claims. The quote checker reports 50 quotes and 39 statistical values with 0 problems. Nothing is committed.

**Text read**
- The accepted author manuscript from Europe PMC (PMC12286656, NIHMS2090574), not the version of record: main text and Methods.
- The Supplementary Materials PDF: Supplemental Note 1, figs. S1 to S38, and tables S1 to S3. Table S3 holds the statistics.
- The MDAR checklist.
- Nothing a claim needed was missing.

**Code read**
- The mouse analysis code, `analysis.py` (Zenodo 10.5281/zenodo.14876694). It has the analysis functions but not the script that calls them.
- brainwide-npix at commit 97cdf58 (tag v0.1).
- The human and mouse-behavior code (Zenodo 14920570), read only for the eye-closure and human coding-dimension windows.

**Claims**
- **Count:** 50 claims, all with quotes. 24 have statistics, 27 have expected values and 44 have criteria.
- **Human and mouse behavior-only (22 claims):** these data are in DANDI:001347, so the claims are marked `data: elsewhere`.
- **Mouse electrophysiology (28 claims):** these are tested on 001326. They cover:
  - eye closure in the recorded mice;
  - the twelve response clusters and which regions they over-represent;
  - regional rise and decay times;
  - the emotion-like dimension (Fig. 5D/E) and the first-order model with its alternatives;
  - fast and persistent coding dimensions, intrinsic timescale and coupling (Fig. 6D/F/H/J);
  - the tone controls (fig. S34);
  - correlation structure and retrosplenial oscillations under ketamine (figs. S29, S30).
- **Tolerances:** 1.96 × the s.e.m. given in table S3 (the paper plots means ± 1.96 s.e.m.), otherwise 10%.

**Details left open, and the readings named**
- **Which mouse was excluded** (13 sessions from 10 mice down to 11 from 9): the paper doesn't name it. Every mouse with two sessions is a reading, and the outcome must hold under all of them.
- **Trial epochs:** the Methods say ketamine is trials 22–32 and post is 34–40. The code and table S3 give trials 23–32 (10 trials) and 35–40 (6 trials). The code is the main reading; the literal Methods numbers are a variant.
- **Emotion-like dimension window:** the Methods put it 5–6 s after the last puff. The code's indexing implies 3–4 s. The weights are divided by each unit's variance in the Methods but by a pooled variance in the code, and scaled to a unit vector versus a sum of absolute values. That scaling affects the expected values in Fig. 5E.
- **Fast coding dimension reference window:** 1 s before the puff in the Methods, 70 ms before in the code.
- **Persistent projection (Fig. 6D):** the code uses the first puff of each series only; all eight puffs is a variant.
- **Intrinsic timescale:** one fit per trial then averaged (Methods, table S3) versus one fit to the trials joined together (code). The pre trials used differ: 11–20 in the code. For the human version, the baseline period is 8 minutes in the Methods and 10 in table S3.
- **Coupling (Fig. 6J):** mean signed r among neurons with the top 10% of absolute weight (Methods) versus median absolute r among neurons with large positive weight, over joined windows (code).
- **Regional d' threshold:** 1.3 in the Methods and code, 2 in table S3.
- **Region labelling threshold for fig. S31B:** 0.05 in the Methods and code, 0.01 in table S3.
- **Cluster numbering:** table S3 numbers clusters by size, while the figure numbers them in a reordered sequence. Which one the text's "clusters 0, 1 and 2" uses is open.
- **Other small gaps:**
  - The code's minimum-activity filter on units has units the code doesn't fix.
  - For the CADSS correlation, the change is ketamine minus the mean of pre and post in the legend but ketamine minus pre in table S3.
  - The tone-series trial counts differ between table S3 and the code.
- **No test in the paper:** several claims rest on figures alone (Fig. 4B, 4G, 4H/I, 5B, 5D, fig. S29, S30, S34C/F, Fig. 6B). For these, the criteria use the paper's own 95% intervals or its stated measures, and they say so. Thresholds that had to be read from words like "dozens", "not substantial" or "tens of seconds" are named as readings in the criteria.
- **Recorded-mouse eye closure:** the paper's data statement places mouse behavior in 001347, but the electrophysiology code reads it. Whether 001326 holds it is for the author to check.
