The claims file is ready for an attempt. I corrected 11 claims against the paper and noted what remains open in a new `checks` entry. Only `claims/crcns-hc-16/10.1016-j.neuron.2017.12.043.yaml` was edited; nothing is committed.

**Checker result:** `32 claims, 31 quotes, 104 statistical values, 6 problems`. All quotes match the text. The six problems are p-values printed as powers of ten (fig1ab 1e-8, fig1cd 1e-6, fig3b-phase-preference 1e-7, fig3d 1e-10 and 1e-7, overdispersion-passes 1e-6). I found each one in the text at lines 289, 332, 714, 731, 736 and 756, so they are correct.

**Changes, by claim:**
- **fig1ab-baseline-transmission, fig1cd-potentiation:** the criterion treated the unit (slice or mouse) as open and picked the slice. The 42 error degrees of freedom with six groups give 48 units, which is the 22 WT and 26 Fmr1-null mice in the Methods. The unit is now one value per mouse.
- **figs3-nonspatial-properties-similar:** removed "in any cell class" from the statement. The paper only tests the genotype effect.
- **tables1-place-cell-properties-similar:** added the interneuron firing rate to the statement, since the statistics and the quote already include it. Added the missing Table S1 in-field rates and interneuron rates to `expected`.
- **figs4-remapping-similar:** the criterion required the box and arena recordings to be on the same day. The paper never says that, and Table S2 dates them differently. Same-day pairs and pairs from any date are now both readings.
- **fig3b-place-cell-modulation-similar:** the Methods give wavelets from 2 to 100 Hz and the code 2 to 250 Hz. The Methods range is now used, with the code's range as a variant. Which recordings to use is now marked open and given readings: 169 degrees of freedom imply 171 place cells, not the 162 in Table S1.
- **fig3b-phase-preference:** the 36° tolerance and the "four of six means" rule were both made up. Tolerances are now the paper's printed ± values, and all six means must match.
- **fig3d-stereotypy:** the number of phase bins is not in the paper, so 20 and 36 bins are now equal readings.
- **fig4cd-kendall-place-cells:** "a pair counts once, from its first session" is now marked as not stated in the paper, with counting per session as the other reading.
- **locomotion-similar:** the paper prints no test for speed or path linearity and never defines linearity. The criterion now says that part of the statement is not judged.
- **fig6-covariance-sem-predicts-errors:** `expected` was written as a mapping; it is now a list like the other claims.
- **fig6-avoidance-behavior:** the session effect has 3 degrees of freedom, so four sessions. These are read as the shock-on sessions (Train 1–3 and Retrain).

**Still open (noted in `checks`):**
- **fig2:** the place-field definitions (above the mean rate, or above 20% of peak, with at least 9 pixels) are not in the paper.
- **overdispersion-cells:** the minimum pass counts (2, 10, 30) are not stated in the paper.
- **figs1 and figs5a:** these claim "no difference" but the paper prints no test, so the tests used are borrowed from elsewhere.
- **figs6:** reading "similar for the two genotypes" as a non-significant interaction is our interpretation, and the paper does not say which measure was log-transformed.
- **Not covered:** Figure S6C (one significant t49 comparison; the extracted text doesn't say which) and the upper and lower 50% insets in Figures 4B and 4C have no claims. Neither is a main finding.

The paper's main findings all have claims, and no claim comes from another source.
