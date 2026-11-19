The claims file is fit for an attempt (`ready: true`). After my edits the checker still reports: `claims/lesica-2007.yaml: 38 claims, 38 quotes, 21 statistical values, 0 problems`. I couldn't render the PDF figures (no PDF renderer is installed here), so anything shown only in a figure is still unread.

**Changes, by claim**
- **Paragraph numbers in sources:** the writer had treated a page break inside paragraph 7 of the first Results section as a new paragraph, so every paragraph after it was numbered one too high. Corrected:
  - Paragraph 7: `fig3c-surround-correlations`, `fig3d-temporal-width-contrast`, `fig3d-temporal-width-correlations`, `surround-temporal-correlation`.
  - Paragraph 8: `fig4b-gain-*`, `fig4c-*`.
  - Paragraph 9: `fig4d-*`.
  - Paragraphs 10 and 11: `fig5-within-trial-contrast`.
- **`fig5-within-trial-contrast`:**
  - The 0.27 to 0.43 range is over a 150 s segment, and the top and bottom thirds are taken over the whole movie (Figure 5A legend). The statement and criterion now say so.
  - The second cell is named as OFF-center X (Figure 5 legend).
  - The legend calls the measure "temporal contrast averaged over the spatial RF". The old readings were only a spatial SD per frame, so I added readings that start from the legend's wording.
- **Reading P1 (c)** treats "increased by X%" as a ratio of X/100. I limited it to increases above 100%; for the 89% and 90% increases it would mean a decrease. `fig4b-gain-contrast`, `fig4b-gain-correlations` and `fig4d-normalized-offset-correlations` now match.
- **`fig7c-effective-contrast`:** the source now gives the Discussion section's full name and adds its paragraph 1, which cites Figure 7C. The criterion now cites the Figure 7A and 7B legends for the averaged RF and its unit-variance scaling.

The other claims check out against the text: statements, statistics and expected values agree with it, and the open method details are named with their readings. Every main finding has a claim, and every claim comes from this paper.

**Still open**
- **Figure marks not read:** which Figure 6 bars carry ** or *** (so the reliability claims are judged at p < 0.01), whether Figure 6B marks any sparseness change, and whether Figure 3B marks the change in spatial width with correlations (its p < 0.001 is inferred from the legend's only level).
- **"No significant effect" claims:** the paper gives no significance level. The file uses p < 0.05, with the legends' p < 0.001 as a variant.
- **`celltype-off-wider-temporal`:** it uses 10% tolerances instead of the paper's ±0.4 ms. The writer reads that spread as a standard error, but the paper doesn't say which it is.
- **No claim, by choice:** the Discussion says the raw (unscaled) offsets for low-contrast movies and high-contrast white noise are very different. I left it out because it's a supporting remark, not a main finding.

I made no commit or push.
