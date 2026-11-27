I updated `claims/pelot-2020.yaml` to protocol pilot-18 for all seven datasets. The quote checker passes: 43 claims, 43 quotes, 21 statistical values, 0 problems.

**Text read.** The version of record from Europe PMC (PMC7672126), flattened from JATS XML: abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was supplied, so no figure was read. The paper links no code, so none was read.

**What is missing from the paper text**
- **Eqs. 1 to 4** (the perineurium thickness fits) were lost when the text was flattened. Only the R2 values and fascicle counts survive, so the fit form and coefficients are open. The PDF would settle them.
- **The whole supplement** is absent. The paper's own numbers are all in the main text, so I wrote claims, but three claims cannot be fully decided without it:
  - Supplement 4 holds the literature values for `literature-comparison-human-pig` and `rat-literature-comparison`.
  - Supplement 6 holds the age trends for `no-age-trend`.
- **The reference list is empty.** I matched each dataset to the paper's citations (Pelot et al. 2020a to g) from the dataset titles and the legends that cite each one: 60 = g, 16 = e, 65 = a, 61 = c, 64 = f, 82 = d, 89 = b.

**Counts**
- 43 claims, all with quotes and criteria; 5 are link claims.
- 9 claims carry statistics.
- 1 claim is `elsewhere` (the Sunderland and Bradley reanalysis) and has no `datasets`, since it rests on none of the seven.
- 2 are `with_inputs` (the two literature comparisons).

**What changed**
- **Data fields:** claims on human and pig data now rest on sparc-65, 64 and 89 through `datasets`; they were `elsewhere` or `with_inputs` before. Every claim except the Sunderland one lists its datasets.
- **New link claims:** `human-sample-set`, `pig-mt-sample-set`, `pig-if-sample-set`, and `mt-micrograph-collections` (covering sparc-16, 61 and 82).
- **New finding claims:** `pig-oblong-human-round`, `human-subdiaphragmatic-fatty-tissue`, `pig-cervical-cell-bodies`, and `pig-if-endoneurium-lower`.
- **Mixed-model criteria:** they now name the JMP settings. REML with Kenward-Roger degrees of freedom is taken from JMP, the software the paper names. Whether variance components are bounded at zero is run both ways.
- **`rat-carotid-sheath-bundles`:** its criterion no longer contradicts itself. It is now tested on the rat micrographs in sparc-16, with the counting rule named as open. This touches a question still open in `questions/pelot-2020.yaml`, which I did not mark answered.
- **Smaller changes:** an R2 reading for the Sunderland fit, a quartile method, and the two ways of forming the human and pig means.
- **Old check removed:** the check of 2026-11-18 applied to the earlier file, so I did not carry it over; its changes are kept.
- **Ids:** all old ids are kept.

**Details the paper leaves open, with the readings named**
- **Variance components in the mixed models:** unbounded (JMP's default) or bounded at zero.
- **Tukey contrasts printed with one p for both levels:** main-effect contrast, with per-level contrasts as a variant.
- **Perineurium fit form:** linear with intercept, through zero, or another model linear in its coefficients.
- **Rat fascicles in the perineurium fit:** all segmented fascicles, or only the largest per sample.
- **"Largest" rat fascicle:** by outer area, with inner area shown if it picks another fascicle.
- **Human and pig fascicle means:** pooled over all fascicles, or the mean of per-sample means.
- **Rat tissue in the Discussion's ratios:** the largest fascicle, or all fascicles. The paper's 0.68 diameter ratio conflicts with its own 0.52.
- **Pig IF against MT comparison:** all MT samples, or the same four samples per level.
- **Words with no measure in the paper.** The rules I named are choices of the file, and the outcomes rest on them:
  - "approximately ten times": a ratio between 5 and 20.
  - "clearest": relative difference, or difference over pooled SD.
  - "more consistent": coefficient of variation, or ranges.
  - "oblong": aspect ratio, or circularity.
  - "many": at least half, or at least a third.
  - "similar": within a factor of two.
  - "for a given diameter": fits compared over the common range, or at 250 µm.
- **The two absence claims with no stated test:**
  - Level difference in the perineurium relationship: overlapping confidence bounds, or an F-test.
  - Age trends: Pearson, or Spearman.
- **Judged by eye:** fat, cell bodies and carotid-sheath bundles, as the paper gives no rule.
- **Sunderland R2:** centred or uncentred.

**Inconsistencies in the paper, recorded for the author:** the rat diameter ratio (0.68 against 0.52), and the pig cervical sample count (21 stated, 22 implied by the Methods' own description).
