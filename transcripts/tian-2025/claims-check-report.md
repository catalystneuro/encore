I checked all 21 claims against the paper text and corrected seven of them. The file is ready for an attempt, with three problems I could not settle.

**Checker result** (the same before and after my edits): `claims/001559/10.1021-acssensors.5c01093.yaml: 21 claims, 21 quotes, 0 statistical values, 0 problems`

**Changes, by claim**
- **fig4d-evoked-increase**: The criterion passed the claim if any one combination of response window and test passed. Both are method details the paper leaves open, so the protocol requires them all to give the same outcome, or the claim is blocked as methods_underspecified. Now only the "which mice" reading can be satisfied by either option. The paper gives no test, and a signed-rank test cannot reach p < 0.05 with fewer than 5 trials, so I added a one-sample t-test as a second reading.
- **fig4d-4ma-single-trials**: The windows and the k = 2 or 3 threshold now have to agree, for the same reason. I removed the requirement that more trials be detected at 4 mA than at 2 mA, because the paper does not say that. The 2 mA fraction is now only reported.
- **fig5-brep-minimal**: This claim of absence had no criterion. I added one: the paper has no test of BREP on its own, so the claim is judged on the paper's eBRIC-against-BREP t-test.
- **fig5-double-bric**: The criterion said the earlier BRIC data came from Tian et al. 2022, which the paper does not say. It now names that paper and the bioRxiv preprint listed in the paper's notes as candidates, and leaves the choice to the author.
- **fig2b-hela-5fold** and **fig3-neurons-7p3fold**: I removed the p < 0.05 condition. The text only claims the fold values, and the P values are printed only inside the figures, which could not be read without the PDF. For fig3 I also stated that 7.3 is read as the mean over cells of each cell's maximal response.
- **fig2c-hek-3p5fold**: I added a criterion with the two ways the 3.5-fold value can be read: the peak of the mean trace, or the mean of each cell's maximum.

The claim statements, quotes, expected values and the BRIC and Orange CaMBI references matched the paper. Each of the paper's main findings has a claim, and none comes from outside the paper.

**Still open** (recorded under `checks`)
- **fig4d-steady-baseline**: the paper gives no measure of a steady baseline. The criterion's drift threshold and 5-s baseline window were chosen by the agent that wrote the file, not taken from the paper.
- **fig4d-4ma-single-trials** and **fig4d-electrode-timing**: the "more than half of trials" rule, the k × s.d. detection threshold, the half-peak rise time and the peak window are also not from the paper. They are labeled as such in the criteria.
- **Supplement and figures**: there was no PDF or Supporting Information. So the figure P values, the electrode colours in Figure 4D, Figures S1 to S3 and Table S1 were not read, and the paragraph numbers in the sources could not be checked against the published layout.

**Ready**: yes, recorded as `ready: true`. Only the claims file was changed, and nothing was committed.
