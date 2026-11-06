I wrote the claims file at `claims/crcns-ssc-3/10.1371-journal.pcbi.1004858.yaml`. The quote checker passes it: 14 claims, 14 quotes, 1 statistical value, 0 problems.

**Text read.** The version of record (PMC4861348, from Europe PMC's full-text XML). That includes the Methods, Results, Discussion, the figure legends, Table 1 and the legend of S1 Fig, which is the only supplement and is a figure. No PDF was supplied. The paper links no code. The data descriptor was read only to see what the dataset holds.

**Claims.**
- All 14 have quotes; none rests on an inferred note.
- Only one has statistics: Fig 7D, Mann-Whitney with FDR correction, p < 0.001. The Fig 5 binomial probabilities and the Fig 6 fit intervals appear only in the figures.
- One claim has expected values: the dataset counts (25 recordings, 7735 neurons, 309.4 per recording, 2.10 Hz), all at 10% tolerance.
- All 14 have criteria. They cover the TE weight distribution (4A/C), heavy-tailed degree (4B/D), out-degree tail longer than in-degree, in-degree uncorrelated with synergy (5A, a claim of absence judged on the paper's binomial skew test), out-degree positively correlated (5B), correlations beyond the null, pooled trends (5C/D), information gain (Fig 6), the Table 1 PID examples, and four model claims (7B, 7C, 7D/E, S1).

**Details the paper leaves open, and the readings named:**
- **TE time scales.** Either bins of 1.6 and 3.5 ms with delays of 1 to 4 bins, or whatever reference [44] (Timme et al. 2014) gives. Combining across delays: maximum or sum.
- **Jitter width for the surrogates.** The width [44] gives, or two widths an order of magnitude apart.
- **Building the sub-networks.** 50 random neurons plus either their 75 strongest connections or 75 random ones. A second choice is whether the analysis runs on the sub-networks or on the full networks.
- **Correlation type.** Pearson or Spearman.
- **Information gain.** n runs from 2 to 6, or from 1 to 6.
- **Firing rate.** Spikes over each recording's length, or over 60 min.
- **Model MI.** How many runs the mutual information is estimated from.
- **"N data = 40".** The paper has 25 recordings and two time scales, which makes 50; it does not say which 40. The count is reported, not tested.
- **No thresholds given.** The paper sets none for "roughly log-normal", "heavy-tailed", "nearly all significant", "qualitatively matched" or "almost uniformly". Each criterion fixes a threshold of its own and says so.

**Missing from the text.**
- The flattened text has lost every displayed equation (Eqs 1 to 24). The information measures can be rebuilt from the prose, and each criterion says how it reads them.
- The feedforward model cannot be rebuilt. The binary-signal currents (Eqs 16 to 19), the form of the rewiring score (Eq 20) and the fitted score equations (Eqs 22 to 24) are given only as equations. So the four model claims need those equations from the version of record, or its PDF, before anyone can test them.
- Values shown only in figures could not be read, so they are not claimed: the binomial skew probabilities in Fig 5, the exponents and their 95% ranges in Fig 6, and the means in Fig 7.
