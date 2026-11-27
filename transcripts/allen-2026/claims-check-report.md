I checked `claims/allen-2026.yaml` against the paper, made 9 corrections and added a `checks` entry. I marked the file ready (`ready: true`), with two points left open.

**Checker result:** `claims/allen-2026.yaml: 31 claims, 30 quotes, 44 statistical values, 1 problems`. The one problem is a false alarm. The flagged value (fig1e-blood-pco2, −1655.776) is printed exactly that way in Supplementary Table 2. The checker only fails to find it because it formats the number as "-1655.78". All quotes match.

**Changes, by claim:**
- **fig1f-blood-bicarbonate:** the three pairwise Dunnett's T3 tests were one entry with no intervals. Each pair now has its own entry with the 95% confidence intervals from Supplementary Table 2.
- **fig2f-front-back-unchanged:** the Methods call zones EF the front and GH the back, and only put the upper/lower and left/right divides at the halfway point. Splitting front from back at halfway is now labelled as an assumption.
- **fig2g-attack-willingness:** the criterion said the deviances and AIC show how pH and exposure time were coded. They can't: with two terms and three groups, every coding gives the same deviance 127.58, AIC and ROC area 0.6992. Working from the paper's counts, only one coding gives the printed coefficients exactly (2.734246 and 0.008351): nominal pH, with time as days in the condition (90, 7, 90). That is now the main reading and the other two are variants. The printed intercept does not follow from it, so it is reported and not judged.
- **fig2i-strike-attempts:** the paper says "the majority of examined squids", which is an overall count. The test is now the overall majority, not a majority in every group.
- **fig3d-cff-variance:**
  - The tolerance is now 4.55 ± 0.95, so it matches the stated range of 3.6 to 5.5.
  - The source now points to Discussion paragraph 11, not 8.
- **rnaseq-assembly:** the assembly was built from other tissues and whole juvenile squid, not from the optic lobes. The statement is fixed, and the 902,413 transcripts it cites are now an expected value.
- **fig4d-acute-tree:** added the organelle and protein localization pathways named in the same paragraph.
- **fig4e-chronic-synaptic-down:** the statement names cell adhesion and prefoldin complex, but the criterion did not test them. Both are now tested.
- **optic-lobe-no-ion-regulation:** the source now points to Discussion paragraph 4, not 3.

Everything else checked out against the text and Supplementary Tables 1 to 5: p-values, statistics, confidence intervals, group sizes, fold changes and percentages, and the attack counts against the 64.7% and 42.3% reductions. Every main finding has a claim, and every claim comes from this paper.

**Still open:**
- I could not open the PDF figures here (pdftoppm is not installed). So I did not confirm the significance letters the writer read from Figures 1B, 1C, 2D and 2H, or the CFF values in Fig. 3D. The text agrees with them where it says anything, but it says nothing about acute-OA in 1B or chronic against acute in 2H.
- The paragraph numbers given for the Results section on metabolism and blood (fig1c to fig1f) could not be confirmed, because the extracted text does not show paragraph breaks there.

Nothing was committed or pushed.
