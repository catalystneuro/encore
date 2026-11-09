I checked and corrected the claims file for DANDI:001845. It is ready for an attempt, though three claims rest on the supplement, which is not in the text and should be supplied. Nothing is committed or pushed; only the claims file was changed.

**Checker:** `35 claims, 35 quotes, 86 statistical values, 2 problems`. The two problems are values the checker could not find in the text: fig3e p = 1.410e-10 and fig7b p = 0.2407586. I found both printed in the figure legends, so they are correct.

**Changes, by claim**
- **fig1h:** The criterion's "3 of 5 pairs" threshold isn't in the paper. Since the Results say this of both genotypes' pairs, every pair is now required, with 3 of 5 counting as partial. Which rat's sequence is shifted is a method detail, so the result must now hold either way.
- **fig1j and fig3d:** These counted as reproduced if any one reading of an open method detail matched. The protocol requires every reading to agree, otherwise the claim is blocked as methods_underspecified; both now say that.
- **fig2b:** Added the genotype × condition interaction as the test for the "no genotype difference" part of the statement.
- **fig2e:** The statement overstated the paper. Performance rises with sessions only at 100%, and the Results' "slower learning" in Fmr1 rats is not supported by the reported interaction tests. Corrected, and the interaction statistics added.
- **fig2f:** Added the legend's session-wise mixed models, in which the genotype effect on latency is not significant (p = 0.058 and 0.064). They are reported but don't decide the outcome.
- **fig3c:** Replaced an invented comparison with chance level by the fraction of two-arm alternation triplets. "Predominantly" is read as more than half, and the file says that is a reading.
- **fig3d:** The statement said WT entropy falls more with learning, but the genotype × session interactions are not significant. Statement corrected, and the interactions recorded.
- **fig4d:** Both contingencies are now judged, not just 100%.
- **fig4eg:** The comparison with shuffled controls is now reported, not judged, because the paper gives no test for it.
- **fig5d:** Noted that a genotype mean near 0.5 is guaranteed by construction in same-genotype pairs.
- **fig5e:** Added the Results' point that the difference disappears later in training.
- **fig7e:** Added the legend's Holm-corrected post hoc tests and the absence of genotype interactions to the criterion.
- **figs2:** The Mann-Whitney test is now named as the claim-writer's stand-in, not a test the paper uses.
- **figs3:** Its tests were made up. The claim is now blocked as methods_underspecified until Figure S3 is read.
- **fig8d:** Fixed the garbled statistic "U = 4.25 × 106" to 4.25 × 10^6.

**Still open**
- The supplement (Figures S1–S3, Tables S1–S2) is not in the paper text. Claims figs1, figs2 and figs3 depend on it and should be revised once it is supplied.
- fig1g, fig7c, fig7g, fig7h and fig8e still pass on any one reading. Their readings are about what the reported numbers mean, which the protocol allows, but some also change the method, so an attempt should show every reading.
- fig6 is a simulation with no recorded data. It is marked `with_inputs` so it is counted separately, and several of its parameters are not given in the paper.
- The legends say "Two-way RM ANOVA", but the degrees of freedom fit an ordinary two-way ANOVA. The file already runs both and blocks the claim if they disagree.

All of this is recorded in the `checks` entry at the end of the file.
