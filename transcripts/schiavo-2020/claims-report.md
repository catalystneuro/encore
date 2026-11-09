I wrote `claims/000249/10.1038-s41586-020-2807-6.yaml`. The quote checker passes it (44 claims, 44 quotes, 90 statistical values, 0 problems), and it has no em dashes, no "rather" and no ": " in plain scalars. Nothing was committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC7677212), not the version of record: main text, Methods, the four main figure legends and the ten Extended Data legends. There is no separate supplement, and I used no PDF. The source-data Excel sheet the paper mentions is not available, and no claim needs it.

**Code.**
- **Link fails:** the paper's code and data DOI (`10.35092/yhjc.c.5037737`) did not resolve on doi.org, DataCite or the figshare API.
- **Collection checked instead:** the dandiset links figshare collection `c.5043830.v6`. Its only code is "Behavior code" (`13054076.v1`), MATLAB that runs the operant task: 30-minute sessions, with a touch time written at each polling sample.
- **No analysis code:** none was deposited, so every method detail comes from the Methods and the legends.

**Claims.** 44 in all (1 link check, 43 findings). All 44 have quotes and none needed `inferred`. 41 have statistics, 13 have expected values with tolerances and 41 have criteria. 10 use whole-cell or operant data on figshare (`elsewhere`), one needs the ISI distribution as an input, and the link claim needs subject labels. The dandiset holds only the two-photon imaging; the rest are behaviour or ISI-distribution claims whose data the dandiset does not seem to hold.

**Details left open, with the readings named:**
- **Imaging method (in the opening comment):**
  - ROIs were drawn by hand; any other segmentation counts as a deviation.
  - The 1.5 SD rule: SD of baseline frames, or SD of trial-wise baselines.
  - The peak shift of the window: one shift per cell, or one per stimulus.
  - Tuning width with or without the prototype: this cannot change any test, so I made a standard choice.
  - Slope: two-point, or least squares over 375, 575 and 975 ms.
  - Population tuning: mean of single-cell curves, or normalized from the raw mean.
  - Normalized ΔF/F when P+M ≤ 0: used as computed, and the count reported.
- **Per-claim readings:**
  - Fig 1c: the family for FDR correction.
  - Fig 1f: the ANOVA design.
  - ED 6c: the Bonferroni family.
  - ED 2b: whether prototypes are in the 75–375 ms bin.
  - ED 3e: ~16% as a mean over mice, or over pooled neurons.
  - ED 3m and ED 4c: the sample unit (mice or tuning curves).
  - ED 4d: raw or normalized ΔF/F.
  - Fig 1g: the ANOVA factors.
  - Fig 1i: the gap that ends a press, and which sessions are compared.
  - Fig 3f: naive against +24 h, or against pooled post-onset sessions.
  - Fig 3h: which "retrieving" session.
  - ED 6d and Fig 4g: which mice make up the stated counts.
  - ED 3b,c: which regions were neuropil-corrected.
  - Whole-cell: the largest 5 or the largest 10 trials.

**Missing from the paper:**
- Fig 1g and Fig 2f print no p-value, only asterisks. I recorded p < 0.05.
- Neither the dandiset description nor the text says whether the dandiset holds ROIs or stimulus identity per presentation. The link claim tests this.
- The fig1a claim's "fewer than 1% of ISIs at 550 ms or more" stands in for the paper's "essentially never". That bound is mine and is flagged as such in the criterion.
