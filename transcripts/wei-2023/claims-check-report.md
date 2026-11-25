I checked and corrected `claims/wei-2023.yaml`, and the file is ready for an attempt. Nothing was committed.

**Checker result line:** `claims/wei-2023.yaml: 49 claims, 48 quotes, 32 statistical values, 1 problems`. That one problem is `figs4-rs-spread 3.34e-11`. The Fig S4 legend prints it as "p = 3.34*10-11", which the checker can't parse; I read it and the value is right.

**Changes, by claim**
- **fig6d-sst-asymmetric-morphology:** this was a real misreading. The file had the two t-tests as Pvalb against Sst, above the soma (p = 0.45) and below it (p = 0.03). The Results say the comparison is above against below within each class. The Source Data reproduces this: 0.455 for Pvalb and 0.030 for Sst, against 0.21 and 0.83 for the between-class tests. I rewrote the statement, statistics and criterion.
- **fig3d-rs2-gamma-locking:** the expected phase range was 190 ± 28 (162 to 218), but the criterion said 162 to 220. Changed to 191 ± 29 so they match.
- **figs5-depth-distribution:** the reading that placed layer 4 by the brain atlas (CCF) is not the paper's method, which uses the first CSD sink. It is now only a variant.
- **fig3c-fs-more-phase-locked:** the reading that averaged two LFP channels doesn't fit the text, which pairs each unit with one channel. Replaced it with the nearest LFP channel on the other side of the peak channel.
- **figs6c-fs-stronger-across-depth:** the "p < 0.05 in at least 12 of 15 cells" rule was made up. Now all 15 must be significant to count as reproduced. I also named both measures shown in Fig S6c (kappa and the percentage phase-locked) as readings.
- **figs6d-rs3-supragranular-beta:** the statement left out the low-gamma half of the sentence it quotes. Added it.
- **Five three-group claims** (figs4-rs1-faster-above, fig3a-rs1-excitability, fig3a-rs23-visual-responses, fig3a-fs-visual-absent, fig6a): the criteria used a procedure that can switch to ANOVA. They now use the Kruskal-Wallis test the legends name, with Holm-corrected Mann-Whitney follow-up tests.
- **fig7g:** now uses the t-test the legend names. On the Source Data it gives p = 0.012, as the paper reports.
- **fig7d:** the paper never says how opto-tagged units are placed in FS or RS. I marked this open and added a second reading, the nearer wild-type cluster centre.
- **fig7e:** the period over which spike rate is taken is now named as open, with its readings.
- **fig6a:** the Results call the symmetry index a ratio, which differs from Methods eq. 1. Eq. 1 is followed and the ratio is a variant.
- **fig6g:** named the legend's test (Mann-Whitney).
- **fig3a-rs23:** stated how "higher sensitivity and selectivity" is read (all three metrics higher), and that the Source Data medians agree.
- **New claim, figs6c-granular-phase:** FS spikes earlier than RS only in the granular region, in beta and gamma. This finding is in the Results and Discussion and had no claim.

Every count, percentage and median the file took from the Source Data matches the workbook.

**Open**
- In figs4-rs-spread, "RS3 has a faster infragranular velocity" can't be decided, because the sign convention of 1/V below is not stated. It stays reported, not judged.
- Several details are still covered by named readings that neither the paper nor the code settles:
  - for all phase-locking claims: the LFP channel, band filter, 10,000-spike cap and what "kappa" means;
  - the depth region boundaries;
  - the unit isolation criteria;
  - the firing-rate period.
- Paragraph numbers in sources could not be checked, because the text file has no paragraph breaks.
- A few minor findings still have no claim: the alpha-band dip in coupling (Fig S6c), the infragranular RS1 to RS3 phase differences (Fig S6d), and the SP1 to SP3 propagation and amplitude differences (Fig 5a,b).

All of the above is recorded in the `checks` entry at the end of the file.
