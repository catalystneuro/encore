I checked the claims file for DANDI:001828 against the paper. It is ready for an attempt, with the open points below.

**Checker:** `38 claims, 37 quotes, 55 statistical values, 0 problems` after my edits. Before them it read 56 values, also with 0 problems; the drop is the entry I removed from fig5c.

**Changes, by claim**
- **fig1b-anxa1-downregulated-rnaseq:** the criterion had picked DESeq2 as "the one standard reading", but the paper names no analysis pipeline. It now uses the paper's own results if GEO holds them; otherwise it runs DESeq2 and edgeR and judges the claim only where they agree.
- **fig1e, fig2c, fig2f, fig2i, figs2:** the paper gives no measure or test for these, so each criterion now says its rule (or, for figs2, its time windows) is set here. figs2 also gets a paired test, since the text doesn't say whether dCP and cCP came from the same mice.
- **fig1h-mp-early-anxa1-loss:** the statement includes the drop in the ventral-tier count (Figure 1G), which has no test in the text. That part is now reported and not judged.
- **fig1j-ipsc-anxa1-reduced:** the legend names no test. I added the Methods' multiple t-tests with Holm-Sidak adjustment as a second reading.
- **fig1m-6ohda-anxa1-loss:** the printed F(2,9) with 4 mice means side was the repeated factor and subtype a between factor. That layout is used, with the fully repeated one as a variant.
- **figs1-6ohda-partial-th-loss:** the text doesn't say how the mice are combined, so pooled counts are added beside the per-mouse mean.
- **fig3fg-auc-change-from-baseline:** the statement said all three listed changes rise, but the legend marks only the dLight-cCP second window as significant; it now says that. I removed a made-up rule that p must be "within a factor of two". The Bonferroni family is open: both 8 and 4 tests fit the single asterisk, so both are run.
- **fig5c-tetx-locomotion:** I removed the statistics entry. It was the legend's asterisk key, which the text never ties to a specific comparison.
- **fig5e-early-models-locomotion:** the statement and criterion said middle-stage MitoPark mice are more impaired, which the cited text doesn't say. They now give the paper's own reading: a bradykinetic, not akinetic/rigid, profile.
- **fig6j-reaching-accuracy:** the printed F(2,14) fits 17 mice, not the 18 in the legend. This is recorded as open: all 18 are used, and dropping each mouse in turn is a variant.

**Still open**
- **Supplement and figures:** Figures S1 to S6 and the figures themselves are not in the text, so the VTA tests, the Th loss and the evoked release rest on the main text alone. The window edges for Figure 3D are still open, with two readings.
- **Paper's code:** the Zenodo record that lists it was not read, as the first reader also reported. I did not try it again.
- **Asterisks:** the paper's asterisks don't match its printed p-values consistently (for example, p = 0.0131 is unstarred while p = 0.004 is starred). I did not use them to decide which tests were corrected.

**Ready:** yes. I added a `checks` entry recording all of this, marked `ready: true`. Nothing is committed.
