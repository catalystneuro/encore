The checker now reports `34 claims, 34 quotes, 14 statistical values, 0 problems`. Before my changes it reported 33 claims, 33 quotes, 8 statistical values and 0 problems.

**Changes, by claim:**
- **The Fig. 5d–i claims (this dataset):** the counts, rates, distances and reference 50 (Seeman et al. 2018) match the Results, the Fig. 5 legend and the Methods, and the connection counts add up (24 + 1 + 2 + 4 = 31). Two claims needed fixes:
  - **fig5-pair-distances:** the quote now includes the sentences that give the PC-IN and VEN-IN distances, which the statement and expected values already used.
  - **fig5fg-example-slice:** the statement listed the types of all six cells, but those come from the code, not the paper. I moved them to the criterion and named their source; the paper's legend types only cells 2, 4 and 6.
- **fig5c-psc-amplitude:** the criterion said "per-cell mean", which the paper does not give. Mean and median are now named as readings.
- **fig4ac-ap-width-amplitude:** one statistics entry stood for two tests, so I split it into amplitude and width.
- **fig4i-peak-index-ais-distance:** the printed F(1, 93) = 1.07 gives p ≈ 0.30, which matches neither printed P. The criterion now says it is unclear which term it belongs to.
- **fig4g-model-ais-distance-ap-shape:** added the Extended Data Fig. 7b slope tests as statistics. The criterion now notes that the PC model's AP also widens a little (p = 0.0013), so only amplitude separates the two models.
- **fig4j-eepsp-latency / fig4j-eepsp-amplitude:** added the Methods' rule for selecting monosynaptic eEPSPs, which the criteria left out. For amplitude, ordinary and repeated-measures two-way ANOVA are now named as readings.
- **fig6-ven-subtype-morphology:** basal height and basal field size are now each a reading. The test that VEN-S does not differ from PCs is now stated explicitly.
- **fig6h-subtype-markers:** added the comparison groups the Results give (VEN-L, VEN-S and L5/6 CT).
- **ven-subtypes-similar-physiology:** added the Extended Data Fig. 9f ANOVA (p = 0.9852) to the statistics and the criterion, and widened the source to Extended Data Fig. 9c–f.
- **fig7c-tau-rna-distance:** the 1 − r reading is now backed by the Results' own term, "correlation distance".
- **New claim, fig3ab-ven-axon-from-basal-dendrite:** a main finding (Fig. 3a,b) that had no claim.

**Still open (recorded in `checks`):**
- The paper gives no rule for calling a connection. The Fig. 5 claims therefore depend on annotations, from the dataset or the code's table, and are blocked as `methods_underspecified` when neither is available.
- The Fig. 5i comparison of each VEN rate with a PC rate of the same partner class is one reading of "compared with PCs"; the paper reports no test.
- The second factor of the Fig. 3c two-way ANOVA is not named.
- I did not open the code, so the code details in the opening comment (the table tallies and the plotting script) are unverified.
- Some secondary findings have no claim: the Fig. 2 type differences, Extended Data Fig. 7g–j, Fig. 7d–k and Fig. 8b,c.

**Ready:** yes. I set `ready: true`. Nothing was committed.
