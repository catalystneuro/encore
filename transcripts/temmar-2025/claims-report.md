I've written `claims/temmar-2025.yaml` and the quote checker passes: 24 claims, 24 quotes, 0 problems. Nothing is committed.

**Text read:** the version of record (the NeurIPS 2025 Datasets and Benchmarks proceedings PDF, as text), including the checklist, plus the supplement from OpenReview: Appendices A to C and Figures S1 to S6. Nothing the claims need is missing. I also read the paper's code, github.com/chesteklab/LINK_dataset at commit 5e1c36a.

**Claims:** 24, all with quotes and none marked `inferred`.
- **Statistics:** none. The paper reports no statistical test or confidence interval for any finding.
- **Expected values:** 6 claims carry them:
  - the dataset counts, with zero tolerance because they count the deposit itself;
  - the SBP slope of -0.033 µV per month;
  - the participation-ratio slope of -0.07 per month;
  - four per-bank SBP slopes and two active/inactive slopes;
  - the shuffled-data R² values (RR -0.166, LSTM -0.156).
- **Criteria:** all 24 have one. Where the paper judges something by eye ("appears", "visually separable", "relatively stable"), I set a decision rule and the criterion says it is not the paper's.

**Details the paper leaves open, with the readings named:**
- **SBP unit in the NWB files:** either scale by 0.25, as the code does, or use the file's stated unit. This could change the slopes by a factor of 4.
- **Figure S4/S5 slopes:** the line is fit either to every channel-day value or to per-day group means. The unit is read as µV/day, and the code for these figures is not in the repository.
- **"Active" channels in the supplement:** it says "< 1 Hz", which I read as a typo for > 1 Hz. It also says the inactive-channel slope is positive, which contradicts the main text's "all categories decreased".
- **"10 dimensions" capturing most of the variance:** read as a participation ratio of at most 10, or the top 10 PCs explaining more than 50%, or more than 80%.
- **Fitts' law throughput:** the formula is only cited (Nason et al.). Three forms are named: with or without the hold time, and Euclidean distance versus a per-finger sum.
- **"Small" circular IQR of tuning angle:** read as under 45° or under 90°, counting all channels or only active ones.
- **Figure 4D:** day offsets signed or absolute, and test-day normalization either held from the training day or refit on the test day (the code makes both).
- **Shuffled baseline:** the session is not named, so I judge it on the median over all sessions.
- **Figure 5B:** the no-fine-tuning comparison is read as either the single-session curve of Figure 5A or the LSTM curve of Figure 4D.

**Where the Methods and the code disagree:** I followed the Methods and named the code's choice as a variant.
- RR inputs: the Methods z-score them; the code does not.
- Movement onset: 1 SD in the Methods, 2 SD in the code, with a different trimming window.
- Fig. 5A: the Methods exclude the first 10 sessions and hold the training-day normalization fixed. The code excludes only the first 5, splits each session 90/10, refits normalization on the test data and adds no training noise.
- Fig. 5B: the code refits the input normalizer each day, which conflicts with the Methods sentence about Figure 5.
- Test set: the code's ends one trial short (74 trials, not 75).

**Missing from the paper:**
- No statistical tests for anything.
- The phrase "long-term decay is not significantly affected" (Fig. 5A) names no test. The criterion uses overlap of the fitted decay rates' confidence intervals, which is my choice, not the paper's.
- The Fig. 5A multi-day training depends on an outside library ("neuraldecoding") that is not in the repository.
