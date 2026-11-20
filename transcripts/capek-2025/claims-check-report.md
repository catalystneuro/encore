The claims file is ready for an attempt. I made six corrections and left four problems open; all are recorded in a new `checks` entry at the end of `claims/capek-2025.yaml`. Nothing is committed.

**Checker:** `claims/capek-2025.yaml: 37 claims, 36 quotes, 61 statistical values, 1 problems`. That one problem is not an error: the checker can't find ed7-additional-strains-behaviour p = 0.0063, but the legend prints it as "6.30e-3" and the recorded value is correct. The checks entry itself passed the schema.

**Changes, by claim:**
- **Sources (paragraph numbers):** the writer counted page breaks inside a paragraph as new paragraphs, so these sources pointed one paragraph too far. I corrected them to the paragraph that holds each quote: fig1d, fig4e, ed4, fig4i, ed5a, ed5e, ed5f, ed6, ed7-additional-strains-behaviour, fig5c, fig5d, fig5e-mettleri-anterior-lh, fig5e-mettleri-laca-intermediate, fig5g.
- **fig5d-mettleri-threshold:** the statement said the 30.1 C threshold lies between 27.5 and 30 C. The paper only predicts a threshold in that range and calls the measured value "very close" to it. Statement corrected.
- **ed5e-tlhon2-silencing:** reading (c) was a one-way ANOVA per temperature, which the legend's "2-way ANOVA" doesn't allow. I replaced it with the effect of genotype at each temperature within the two-way ANOVA, and reworded the criterion so it works under all three readings.
- **fig2a-exon-d-divergent:** the paper gives a source for only 2 of the 25 sequences (D. persimilis and D. mojavensis, via GenBank), so 23 have none, not 22. Corrected.
- **ed6-olfactory-lh-conserved:** "LH architecture is conserved" softened to "largely conserved", which is what the paper says.

All other statements, quotes, p-values, sample sizes and expected values match the paper. Every main finding has a claim except Fig. 2f,g (heat-evoked current, shown only as example traces; see below).

**Open:**
- **fig2a and fig3ab:** these depend on Gr28b sequences and a D. mojavensis genome whose source the paper doesn't name. They stay as dataset claims and will likely be blocked unless the author finds the sources.
- **ed5f-tlhon2-optogenetic-avoidance:** in the paper's Source Data spreadsheet, the Gal4/+ control rows are identical to the Gal4 > CsChrimson rows, so the printed control p = 0.440 can't be recomputed from it. The claim's outcome will turn on that spreadsheet error.
- **ed3e-com-link:** this is a link claim written by the reader, but the protocol gives link claims to the author. I left it for the author to keep or replace.
- **Fig. 2f,g:** the heat-evoked current in cells expressing the D. melanogaster channel has no claim. It is shown only as example traces and the recordings aren't deposited, so I didn't add one.
