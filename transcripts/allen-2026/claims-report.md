I wrote `claims/allen-2026.yaml` (not committed). It has 31 claims; the quote checker passes everything except one confidence-interval bound, which I confirmed by eye.

**Text read:** the version of record (Communications Biology PDF and its extracted text) with its one supplement: Supplementary Figs 1 to 5 and Supplementary Tables 1 to 5. I opened PDF pages 3 and 7 to 10 only to read the significance letters of Figs 1B–F, 2D and 2H and the axes of Fig. 3C and 3D. I read no code: the paper links no repository and says its scripts are in the Dryad deposit, which I did not open.

**Claims:** 31 in all.
- **Quotes:** 30 have one. The seawater chemistry claim (Supplementary Table 5) is marked `inferred` because no sentence states those numbers.
- **Statistics:** 16 claims record them.
- **Expected values:** 20 claims have them.
- **Criteria:** all 31 have one.
- **Data elsewhere:** 10 claims are `data: elsewhere`. These are the RNA-seq results, whose data are in NCBI SRA PRJNA1204452 and TSA GLBY01000000.
- **Checker:** `tools/claims_check.py` reports one problem: it cannot find the bound −1655.776 for the acute-OA against chronic-OA PCO2 difference. The value is printed in Supplementary Table 2; the checker rounds it to six significant digits before searching.

**Details the paper leaves open, and the readings named:**
- **Which number in the Results "±":** SD or SEM is not stated, and the Fig. 2 legend's "SEM" cannot be right for hunt duration. Tolerances are 10% of each mean, with both SD and SEM to be reported.
- **Logistic regression coding:** the pH and time coding is not given. Readings: nominal pH with time as days in the rearing condition, nominal pH with time as days of acidification, or either with the measured tank pH. The reported deviances and AIC identify which one.
- **Zone percentages:** the denominator is either all 0.1 s samples or tracked samples only.
- **Left and front zone tests:** Supplementary Table 3 labels them log(Y), but their sums of squares are on raw percentages. Raw is the main reading and log a variant.
- **Mean depth:** height above the bottom, or distance below the surface.
- **Acute 3-D group:** 8 squid (Fig. 2A, the ANOVA df) or 9 (Supplementary Fig. 1, Fig. 2B legend).
- **CFF definition:** the highest frequency with a ratio of at least 0.9 is the main reading, which Fig. 3D supports; linear interpolation is a variant. Which squid enter Fig. 3D is also open: it shows 3 to 6 per group against 8, 8 and 9 in Fig. 3C.
- **ERG analysis:** the FFT window and the length of the no-stimulus period are not given. The amplitude measure is either spectral power at the stimulus frequency or the peak-to-peak amplitude.
- **Body size:** which squid enter the 90-day mass and mantle length (all, control only, or control plus chronic).
- **Prey velocity:** whether the two-way ANOVA treats time as a repeated measure.
- **Strike attempts:** "majority" read per group or overall.
- **Seawater:** the blood PCO2 and HCO3− equations need the constants of ref. 65, which the paper does not print.
- **RNA-seq:**
  - The expression filter's wording allows two readings.
  - How sva batch effects were removed: estimated surrogate variables or known batches.
  - What "36" GO sets counts: down-regulated sets in either treatment, or all sets in the Venn diagram.
  - Which GO terms count as acid-base or ion regulation.
  - The nAChR claim reads "down" either as core-enrichment membership or as a negative fold change.

**Missing from the paper:** the supplementary data files "DET Results" and "GSEA results" are not under `paper/`. Only `chronic-nachr-subunits-down` rests on them (the alpha-7, alpha-10 and beta-4 subunits), and its criterion says so.

**Inconsistencies in the paper:**
- The Results cite Fig. 3E and 3F where they mean Fig. 2E and 2F.
- The Methods give the footage as 5 frames per second, but coordinates are recorded every 0.1 s.
- The blood spreads differ slightly between the Results and Supplementary Table 2.
- The acute blood group has 6 squid in Supplementary Table 2, while the Fig. 1 legend gives 7 to 9 per group.
- The Results call the higher CFF variance not significant; the Discussion calls it significant.
