I checked `claims/000467/10.1016-j.cell.2023.05.025.yaml` against the paper, corrected what was wrong, and marked the file ready. Nothing is committed.

**Checker result** (the same before and after my edits): `32 claims, 32 quotes, 36 statistical values, 0 problems`. The Table S2 differences, confidence intervals and p-values, the Table 1 efficiencies and the Figure S7C p-values all match the paper.

**Changes, by claim**
- **M4 (opening comment):** it required PGa not to respond to 4-methyl-3-heptanone. The Results define PGa only by its heptanol and hexanol responses, so a heptanone response now only decides between two candidates.
- **fig1cd-new-pheromones-leave-nest:** the spacing of the scored timepoints is now named as open; this paper leaves it to Lopes et al. 2023.
- **fig1e-categorical-response:** the trial counts come from Table S2's n for the same bioassays. Marked as such, since the text gives no counts for Figure 1E.
- **fig1f-hexanol-like-native** (and the two other Figure 1F claims, which refer to it): the Šidák family was six comparisons; Table S2 has nine, including the vehicle. The adjusted p-values depend on this.
- **table1-transgenesis:** the statement called the last treatment's line stable. The paper says only the line from the first four rows gave a stable population.
- **fig2cd-gcamp-in-osns:** reading "great majority" as more than half is now stated as the reader's own choice, and the fraction is reported.
- **ablation-al-volume-trend:** removed a made-up upper bound (p < 0.1). It is now a claim of absence on the paper's test at 0.05; whether the t-test is one- or two-sided is named as open.
- **fig3f-general-odorants-unique:** odorant pairs are now those each ant was given, since each odorant was tested in only 2 to 6 ants.
- **fig4-no-decreases:** the criterion used a minimum projection that the paper never uses. It now uses the per-plane peak fold change maps, which is how the Methods decided that all responses were positive.
- **fig4-large-lasting-responses:** removed the expected value 1.5, a midpoint the paper never reports (it gives a range of 1 to 2). Both ROI-value readings must now hold.
- **figs5b-shared-glomerulus, figs5c-mho-rarely-overlaps:** added a 48% reading (Figure 6, 8 ants), since the text names no concentration.
- **fig5c-s6-tuning:** the criterion said "seven named combinations"; there are six.
- **figs7a-6g-extended:** added odor offset (8 s) as a reading of "after odor presentation". The 90% and 80% plateau levels are marked as the reader's own.
- **fig5d-stereotyped-positions:** how the centres and the plane are chosen are method details, so every reading must now agree, and the claim is blocked as `methods_underspecified` if they don't. Before, one reading was enough.

**What remains open** (recorded under `checks`)
- Eight criteria use rules the reader made up, because the paper judged these findings by eye: fig3f, fig3fg, figs4a, fig4-no-decreases (the -0.2 level), fig4-large-lasting-responses, figs5a-concentration, fig5ab (middle third of the depth) and fig5c-6g-slow. Each says so in its criterion, and the paper offers nothing to replace them.
- The paper drew the ROIs (M2) and chose the single-glomerulus planes (M3) by eye. The readings listed for them are the reader's and could change the counts.
- Two secondary findings have no claim of their own: the similarity across ants for alarm pheromones (Figure 4D) and the stability of responses over a session (Figure S4B-C). Two existing claims cover them in part: fig5ab-focal-glomeruli and fig5d-stereotyped-positions.

**Ready:** yes (`ready: true`). Every claim comes from this paper, and each main finding has a claim.
