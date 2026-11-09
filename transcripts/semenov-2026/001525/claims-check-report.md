The claims file is ready for an attempt. I corrected ten things and left three problems open, none of which blocks an attempt.

**Checker:** `claims/001525/10.1016-j.bioelechem.2026.109283.yaml: 27 claims, 27 quotes, 9 statistical values, 0 problems`. I got the same result before and after my edits.

**Changes, by claim**
- **Header:** Section 3.7 also writes 570 V/cm once, so the note on strength labels now says so.
- **fig7a-test-pulse-cosine-up-to-1000:** I dropped the reading "amplitude within 10% of the benchmark". The paper puts the 1000 V/cm response at about 80% of control and still calls it a cosine, so that reading would fail on the paper's own data. The readings now use the gray s.e. outline from the Fig. 7A legend, or the Fig. 7B t-test.
- **fig7b-test-pulse-unchanged-to-760:** the per-cell one-sample test against 100% doesn't fit the Fig. 7B legend, which draws the control as a band with its own spread. The readings are now a paired and an unpaired two-sided t-test, and the one-sample test is a variant. If the readings disagree, the claim is methods_underspecified; the earlier rule let a reading the writer chose decide.
- **fig7b-test-pulse-reduced-1200-1400:** reading names updated to match.
- **fig7c-full-reseal-mild-residual-strong:** residual conductivity is now also judged at 1000 V/cm, as in Fig. 7C and the abstract. The pole comparison now cites Results 3.4, and an unpaired test is added as a variant.
- **fig2b-di8-climbs-then-declines-in-set:** I removed the requirement that the within-set decline be significant at p < 0.05. The paper reports no such test and calls the same kind of decline in Fig. 2C not significant. The pole is now named as open, with two readings.
- **fig2d-lasting-drop-after-1000:** added the legend's "≤20%" as a second reading beside the text's "about 20%".
- **fig4c-equator-follows-cosine:** the old measure averaged IMP over both sides of the equator, which cancels to about zero, so it could not decide. It is now the slope of measured IMP against calculated IMP, fit through the origin as in Results 3.3.
- **fig5a-gd-cathodic-no-higher-but-no-decline:** I removed "electroporation starts above 500 mV" from the statement, since it is an interpretation the criterion never tests. The made-up s.e. threshold in part 3 is replaced by reporting the size of each fall.
- **fig6a-ca-single-pulse:** added an unpaired t-test against the 0 V/cm group as a second test reading. The writer's rule that one reading decides the 780 V/cm absence part is replaced by methods_underspecified when readings disagree.

**Still open**
- **fig5b-conductivity-calibration:** Eq. (2), as read from the garbled text, gives a 1.3% IMP reduction for a 10-fold conductivity rise, against the paper's "~2%". That is outside the claim's 1.5 to 2.5 tolerance. The 100-fold case gives 11.9%, which matches the paper's 12%. I couldn't render the PDF here (pdftoppm isn't installed) to confirm the equation, so I added the computed values to the criterion and left the claim unchanged.
- **0.3 µs threshold:** the abstract gives 1000 V/cm as the threshold for 0.3 µs pulses. The Results show it only through the Fig. 4D legend, and no claim tests it.
- **No stated measure:** the paper gives none for "follows a cosine", "linear" or "stable" (claims fig7a, fig4c, fig3-nonlinear, fig2a-stable). Their readings and bands are the claim writer's choices and are labeled as such.

Every main finding has a claim, and none comes from outside this paper.

**Ready:** yes. The `checks` entry is recorded with `ready: true` and 13 change lines. Nothing is committed.
