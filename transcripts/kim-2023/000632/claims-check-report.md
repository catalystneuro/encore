I checked the claims file for DANDI:000632 against the paper, made corrections in the claims file only, and the file is ready for an attempt. Nothing is committed.

**Checker:** `claims/000632/10.3390-ijms241310921.yaml: 12 claims, 11 quotes, 0 statistical values, 0 problems` (the result was the same before and after my edits).

**Changes, by claim:**
- **Opening comment:** I added two details the paper leaves open.
  - **How Figure 2 is normalized.** The single-pulse controls were separate samples, so the percentage could be a ratio per experiment, averaged, or a ratio of the group means.
  - **The angle of each ROI.** It comes from a simulation whose values the text does not give, and the text gives no electrode spacing for the triangle. If the dataset holds neither, the `fig2-*` claims are blocked.
- **fig3-770khz-co-above-cross:** the `inferred` note said Figure 3 shows p-values for this pair. The text only says p-values were calculated, not which pairs they compare, so I corrected the note.
- **fig3-no-area-dependence:** I added that the Discussion cites Figure 2 for the same conclusion. fig2-facilitation-plateau is reported alongside but does not decide the outcome.
- **fig2-180-cancellation, fig2-crossover-angle, fig2-60-fold-co-counter:** the criteria counted a claim as reproduced if it held under either background reading. Background subtraction is a method detail, so under the protocol both readings must agree, or the claim is blocked as `methods_underspecified`. I also added the ways the reported numbers can be read: which ROI counts as "at 180°" (the one nearest the base, or the one with the lowest uptake) and the two normalizations. For the 60-fold claim, I noted that reading (b) matches the paper's own arithmetic (3-fold × 20 = 60).
- **fig2-facilitation-plateau:**
  - The expected angle range was wrong: 90 to 100° widened by 10% of each bound is 81 to 110°, so I changed 95 ± 15 to 95.5 ± 14.5.
  - I removed one plateau test the reader had invented ("no ROI differs from the level by more than its s.e."). With n = 3 it would fail about one ROI in three even on a true plateau.
  - The remaining slope test and the 10% rule for where the plateau starts are now labelled as standard choices, since the paper defines neither.
  - I added two readings of the three-fold level: the ROIs between 90 and 100°, or the ROIs from 100° to the apex.
- **fig4-unipolar-pattern:** one ROI placement put the ROIs 0.5 mm from the electrode centre. That is inside the needle's 0.75 mm radius, where cells are shielded from the field. I replaced it with ROIs 200 µm outside the electrode edge. I also noted that the field map is not given as numbers.

**Still open:**
- fig3-770khz-co-above-cross is my reading of two sentences, not a finding the paper states. Whether Figure 3 prints a p-value for this pair can't be checked: no PDF was supplied, so the figure values (the Figure 3 p-values, the Figure 2 curves) were not read.
- Reference 17 (Kim et al. 2023), which the Methods cite for the analysis details, was not read. It may settle the background correction.
- The two "no difference" claims are judged with background subtraction, which the Methods name as the correction for spontaneous uptake without saying how it is applied. The paper also does not say whether its t-test is paired.

The main findings each have a claim, and every claim comes from this paper.

**Ready:** yes. The check entry under `checks` has `ready: true`.
