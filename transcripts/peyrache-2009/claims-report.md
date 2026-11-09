I wrote `claims/crcns-pfc-6/10.1038-nn.2337.yaml`. It has 29 claims, and every one has a quote. All quotes pass the checker. The checker still flags 3 p-values as not found: 1e-5 in `fig2b-pre-weaker`, 1e-10 in `fig5b-spwr-triggered` and 1e-5 in `replay-in-delta-spindle-periods`. The extracted text prints these as "10�5" and "10�10"; I checked each by reading (text lines 266, 493 and 622). Nothing is committed.

**Text read:** the version of record (PyMuPDF text of the journal PDF): main text, legends and Online Methods. Also the supplement (MOESM12): the Supplementary Discussion, the legends of Supplementary Figs 2 to 13, and Supplementary Table 1. The legend of Supplementary Fig 1 (histology) did not come through in the extracted text, and no claim needs it. I could not render PDF pages here because poppler is not installed. The extracted text turns some signs into other glyphs ("P o" is <, "P 4" is >, "n 1⁄4" is =, "B" before a number means "about"); the opening comment explains this. The paper links no code, so none was read.

**Statistics and criteria:** 26 claims carry statistics, with 27 entries holding 19 p-values. 23 claims have expected values. 28 claims have a criterion; `fig7b-controls` is one of them and is the only claim with both statistics and expected values. Every claim uses the default `data: dataset`.

**Details the paper leaves open, with the readings named:**
- **Z-transform scope for rest epochs:** over the whole epoch, or over its SWS bins only. This applies to all reactivation claims.
- **Counts of 1,692 cells and 63 sessions:** before or after the inclusion rule.
- **Rule learned:** criterion counted within a session, or across consecutive sessions with the same rule.
- **Learning point and learning sessions:** two readings for where the 80% performance window starts, and two for which sessions count.
- **Test for post greater than pre:** the paper does not name it. Readings are a paired t-test or a Wilcoxon signed-rank test. The order of the group sizes 10, 40 and 273 is also open.
- **Reactivation versus encoding strength:**
  - which bins: all post SWS bins, or only those outside SPWRs (Supplementary Fig 7A);
  - slope test: a linear-model interaction, or a bootstrap;
  - correlation test: Fisher z, or Steiger's test for dependent correlations.
- **Skewness test (n = 10 to 40):** the two highest encoding groups, or all three.
- **Fraction of reactivation from the strongest events (40 to 50%):** computed per group with bins pooled, or per component and then averaged.
- **Cross-correlograms between components:** what counts as chance, either Pearson correlation (chance 0) or the correlogram over the product of means (chance 1).
- **Shuffle control:** the number of shuffles for Supplementary Fig 11D (1000 used); the pre-post test is not named.
- **SPWR bins:** the ripple-peak bin alone, or that bin and the next.
- **Baseline for the SPWR-triggered average:** ±2 to 4 s, or the whole window.
- **Strong replay episodes:** defined by the 99th or the 95th percentile.
- **DOWN states:** total silence for at least 80 ms, or the population rate below a fifth of its SWS mean.
- **Fig 6d:** which of the r values 0.79, 0.53 and 0.96 belongs to which event.
- **Fig 7b ANOVA:** run on per-trial means, or on trial by spatial bin. The Methods (multinomial intervals) and the legend (two-way ANOVA then t test) also describe the test differently.
- **Fig 7d factor analysis:** the 15 components, or all 30.
- **Supplementary Fig 12 trial length:** trials pooled, or session means paired.
- **Smaller standard choices, stated as such:** the autocorrelogram bins and fit range, and the correlogram lag range.

**Missing from the paper:** no analysis code. The data descriptor lists no LFP, no ripple, delta or spindle times, and no tetrode for each cell. So the SPWR claims (Figs 5 and 7, Supplementary Table 1) and the delta, spindle and same-tetrode claims are probably not testable, though they are kept as the paper's findings. Fig 1a and 1c (single-session examples) got no claims.
