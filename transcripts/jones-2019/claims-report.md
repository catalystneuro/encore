I stopped without writing any claims, because Table S2 of the supplement is missing. No `claims/jones-2019.yaml` was created.

**Text read:** `paper/10.1016-j.celrep.2019.10.056.txt` is the version of record with its supplemental information: main text, STAR Methods, Figures S1 to S4, and Tables S1, S3 and S4. The text and the PDF both have 28 pages, and Table S2 is in neither. The supplement goes straight from Table S1 (page 26) to Table S3 (page 27). Since S2 is the only table skipped, it was most likely published as a separate file, probably a spreadsheet, at https://doi.org/10.1016/j.celrep.2019.10.056.

**Why it is needed:** the Results cite Table S2 four times, and these findings rest on it:
- **The screen itself:** "88 comparisons, 9 of which were significant with a = 0.05 ... (p < 0.00032, binomial test; see Table S2)". This screen is how the paper picked the metrics that make up the MWM learning and memory precision scores.
- **Robustness:** "All relationships remained significant regardless of the frequency band (150–250 Hz versus 125–250 Hz) or threshold (3 SD versus 5 SD) used for SWR detection (Table S2)."
- **Negative result:** "SWR-associated SG power in CA1 and in DG did not consistently and significantly predict memory performance (Table S2)."
- **apoE3-KI mice:** "some predictive relationships ... in the screen cohort of aged apoE3-KI mice (Table S2), the majority did not replicate".
- **Missing numbers:** the R and p values for the MWM correlations in both cohorts (Figure 2B to 2R) are not printed in the legends, which give only F. They would be in Table S2, and the expected values for the Figure 2 claims depend on them. The text extraction also left no R values from the Figure 2 artwork.

**Not done:** no claims, quotes, statistics or criteria were written, no open details were named, and the quote checker was not run. I did not read the linked code (github.com/emilyasterjones/SWR-predictions) or look at the dataset.

**To continue:** add Table S2 under `paper/` and rerun the reader.
