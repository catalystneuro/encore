I didn't write `claims/wang-2019.yaml`. A safety classifier stopped my attempt to write the file, so the tool call never ran and nothing was saved. I won't regenerate that content, so this run produced no claims file, no quote check and no criteria.

**Text read.** `paper/10.1113-jp278016.txt` is the PMC author manuscript (PMC6675632, accepted version). It has the abstract, Introduction, Methods, Results and Discussion. There is no PDF and no supplement.

**Missing from the paper text.** The text has **no figure legends**. Almost every finding is shown only in Figures 1 to 9, so the number of hearts per panel, the test and p-value per panel, and the plotted values cannot be read.
- The Results report only three counts of hearts: repolarization reversed in 8 of 9 rabbits, was unchanged in 7 of 8 mice, and fully reversed in 1 of 8 mice.
- The APD values for the mouse's rise-then-fall response (50.9, 60.6 and 46.5 ms) appear only in the abstract, so the protocol bars them as expected values.
- The Methods give the test only in general terms: repeated measures ANOVA or paired t-tests, P<0.05.

These legends should be supplied before claims are written.

**Code.** The paper links only the download pages for the two groups' published heart-cell models (the Bers lab page and the Grandi lab page). Neither gives a repository or commit. The paper links no analysis code; the optical maps were analysed in Optiq, which is commercial software. So no method detail can come from code.

**What I had planned.**
- **Claims:** 26, covering Figures 1 to 9 and the Discussion's simulations. All would have quotes from the Results or Discussion.
- **Statistics:** one entry (the heart-rate increase).
- **Expected values:** only the three counts of hearts.
- **Criteria:** one for every claim.

**Details the paper leaves open, with the readings I would have named:**
- **Time point during stimulation:** end of stimulation, peak, or each point of the time course.
- **Baseline:** the beats just before stimulation, or paced without stimulation.
- **Which test:** repeated measures ANOVA, or paired t-tests against baseline.
- **Base and apex regions:** top and bottom thirds, or quarters, of the field of view.
- **Reversal of repolarization:** the base-minus-apex timing difference changes sign, or the fitted gradient turns by more than 90°.
- **Hearts per panel:** which hearts enter each panel and which stimulation frequency is used.
- **Figures 5 and 7:** one representative heart or a group.
- **Simulations:** how the decay time constant τ is fitted and how the swapped APD course is scaled.

**To finish:** re-run the reader with the figure legends added under `paper/`. If the classifier stops the write again, the file may need to be written by hand or in smaller parts.
