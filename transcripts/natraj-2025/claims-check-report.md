**Checker result:** `52 claims, 52 quotes, 125 statistical values, 1 problems`. The one problem is figs7i's p = 3.2442e-12, which the checker could not find. It is in the Figure S7I legend, printed as "p = 3.2442 × 10 - 12"; I confirmed it by reading. The count of statistical values went from 127 to 125 because I removed two threshold entries.

**Changes, by claim**
- **Readings of method details:** these criteria accepted a match under any single reading of a method detail. The protocol requires the outcome all readings give, or the claim is blocked as methods_underspecified. Fixed in:
  - fig1g, fig1h (channel neighbourhood)
  - fig1kl (Pearson or Spearman)
  - fig2i, and the claims that use its autoencoders (reconstruction loss, augmentation)
  - fig2j (variance scaling)
  - fig3c and figs7cd (CKA inputs and shuffling)
  - fig4cd-day-decodable (how day labels enter)
  - fig4fg (robust weighting)
- **fig2e-above-chance, fig3c:** removed the "p < 0.05, FDR" statistics. They are thresholds used to count sessions and layers, not results.
- **fig2e-above-chance:** the main binomial reading went against the Methods. The Methods' Binomial(N, K/N), area 0 to N/m, is now the main reading; the usual upper tail is a variant.
- **fig1mn:** the statement said the clustering groups actions by effector, which no sentence of the paper says; it now follows the Results. The permutation test was made up by the writer, so it is now a variant only and the claim is recorded as methods_underspecified.
- **fig6g-velocity-covariation:** the 20° and 0.3 thresholds were also made up by the writer. They are now a variant only, and the claim is recorded as methods_underspecified.
- **figs5bc:** the 0.8 threshold was the writer's. It is now 0.79: the paper's own "preserved" map has r = 0.88 (Fig. 4B), less 10%.
- **figs5:** the Methods do not say whether the SD is taken on reconstructed or input features; this is now named as open. The made-up "7 of 9 within tolerance" is now all 9.
- **figs6gh:** B1's feature space is open (96 pooled or 384 unpooled features); both readings are now named.
- **figs7i:** removed n = 48 and 18 trials. With those counts a Mann-Whitney z cannot exceed about 6.2, but the paper reports 6.967. The criterion now says so and does not expect z or p to match.
- **fig4fg:** the printed slope is identical for B1 and B3, and the paper does not say whose it is. The slope value can now match either participant; the header note is updated.
- **figs8ab:** how a trial's label is formed from its samples is open; max vote and per-sample accuracy are now both named.
- **fig4i:** the 64-unit width is now called a standard choice, with other widths as variants.
- **fig6g-ibid-angular-error:** this is a claim of absence, so it is judged on the paper's test as written, over all time points.
- **figs8g:** the binomial test is now tied to the paper's own decoder test (Methods, Action decoding), with 5 classes.

**Still open**
- fig1ij: reading (b), every significant channel with a majority rule, was built by the writer. The paper identifies its two channels only in the figure.
- figs4hi: "important" and "most informative" are read as comparisons of median accuracy; the paper gives no test.
- The paragraph numbers in sources could not be checked, because the text has no paragraph breaks.

Every main finding has a claim, and every claim comes from this paper.

**Ready:** yes. The checks entry is recorded with `ready: true`. Only `claims/001535/` was changed; nothing is committed.
