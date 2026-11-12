I've written `claims/rich-2014.yaml`: 27 claims, every one with a quote. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** The version of record (Science 345:814–817) and its full supplement: Materials and Methods, Supplementary Text, and Figs. S1 to S18 with legends. I rendered PDF pages only to read Fig. 3 and Figs. S5, S7, S15 and S17. The paper links no analysis code, so I read none.

**Missing from the paper.** The last page of the supplied PDF (p. 817) is damaged. Its text columns survive, but Fig. 4, its legend, refs 30–31 and the acknowledgments don't render and aren't in the text. The main text, Methods and supplement are otherwise complete, so I went ahead. Three claims rest on Fig. 4:
- **Fig. 4A:** the legend would say which correlation gives r = 0.45, so the readings are Pearson, Pearson on log rates, or Spearman. With n = 253, r = 0.45 matches a Pearson p of about 5e-14.
- **Fig. 4B:** the range of environment sizes it plots is unknown.
- **Fig. 4C:** what it plots is unknown, so how to compare the two models' results is left open.

**Counts.**
- 27 claims, 27 quotes, none inferred.
- 10 claims carry statistics, 17 entries in all.
- 17 claims have expected values.
- All 27 have criteria.

**Details the paper leaves open, with the readings named for each:**
- **What counts as a pass through a field** (for the 50% firing rule): a full traversal of the field, or any visit to it in that direction.
- **Open-field speed and occupancy thresholds:** the track's values (5 cm/s, 0.001 s per bin), or no speed threshold.
- **Anderson-Darling test for exponential intervals:** with the mean estimated, or with the cell's mean plugged in. The set for the false discovery rate adjustment is open too: the 61 location tests and 61 interval tests apart, or all 122 together.
- **Comparing Fig. 2B/C with the null:** a two-sample KS test, or a KS test on per-cell percentiles.
- **Overdispersion test:** index of dispersion, or a likelihood ratio of negative binomial against Poisson.
- **Recruitment KS surrogates:** fixed fitted parameters, or refitted per surrogate (the approach of ref. 37).
- **Sidedness of p in Fig. S11:** two-sided or one-sided.
- **Section-boundary test (Fig. S11):**
  - Piece length: a 7 m piece does not fit twice in the 12 m section 3.
  - Shuffle: swap two pieces per cell, or permute all three.
- **Fig. S10:** bin widths and what counts as a corner are not given, so I used standard choices and marked each as a deviation. The test is open: count of bins outside the shuffle interval, or a Spearman trend.
- **Fig. S12:** KS against the null, or the mean against the null interval.
- **Memoryless curves (Fig. 3E):** start points every 5 m or every 10 m.
- **Size and rate of merged fields (Fig. S14):** the union of the two directions, or their mean.
- **Fig. S16 correlation:** Pearson or Spearman.
- **"In the environment" for silent-cell firing rates:** novel-section time only, or all RUN1 time on the track.
- **Fig. S17 window at the track's end:** wrap around, or only starts where it fits.
- **Fig. 4C environment sizes:** spaced on a log or a linear scale.
- **Recomputed fields:** fields are recomputed by the Methods. If the dataset holds the paper's own detected fields, they're shown as a variant.

**Conflicts with the paper's own numbers.** Working from the rounded parameters printed in the paper (r = 0.57, p = 0.14), two results don't match the text. I recorded both in the criteria without changing the expected values:
- 90% recruitment comes at about 436 m, against the paper's "~500 m".
- The single-field proportion is about 16% at 48 m, not 5–10%. It falls inside 5–10% only at about 200–600 m (and near 1 m).

Values read only from figures have the figure named in the claim:
- the per-animal means in Fig. S7A;
- the Fig. S17 correlations, about 0.41 and 0.22, with tolerances taken from the 95% intervals as read off the figure.
