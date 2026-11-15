**Round 2 verification: Peyrache et al. 2015 on DANDI:000056 (version 0.261106.1949)**

Counts are taken from the claims file (35 claims) and the attempt record (35 outcomes: 34 tested, 1 blocked). The notebook has been renumbered since round 1, so cell indices below are for the round-2 `reproduce_peyrache_2015.ipynb` (R) and `glm_peyrache_2015.ipynb` (G).

### 1. Outcomes and assumptions

I agree with 33 of the 35 outcomes. The two exceptions:

- **fig5e-readout-windows, blocked (too_large): I disagree.** The block rests on the GLM run taking "21.1 minutes", with the longest session at 952 s. G cell 2 prints "analysed 26 sessions in 12.2 min", and G cell 4 gives 561 s as the longest session. At the record's own factor of 3.3, the denser grid would take about 40 minutes, which is under the 60-minute limit. The printed outputs do not support the block.
- **fig4d-ole-near-bayesian, not_reproduced: I agree only provisionally.** The first part now holds in ADn (25 of 25 ensembles, p = 6.0e-8). In PoS all 5 ensembles also favour the covariance OLE, but p = 0.0625, which is the lowest p a test on 5 pairs can give. This is because only hd-a ensembles were decoded. Under hd-b, 11 PoS sessions would qualify (R cell 58), and that could make the outcome partially_reproduced.

Changes from round 1 that I now accept:

- **fig2e-decoded-speed, partially_reproduced: I now agree.** The criterion allows "one of the two holds" per structure. The PoS REM ratio is 0.93 under (a, w-a) and also 1.00 under (b, w-a), and the (b, w-a) reading does not need the sub-degree interpolation. It rests on 4 ensembles.
- **ensemble-sizes, partially_reproduced: I agree.** It follows the criterion, but it is fragile: the PoS mean of 5.22 depends on Mouse20's 3 PoS sessions, which have no HD cells. Without them the mean is 6.00 and falls outside tolerance. The record states this.

Outcomes marked `assumed: true`:

- **fig6a-fast-oscillation and fig6b-adn-synchrony (analytic jitter null):** stated, and reasonable.
- **fig7c-adn-triggered-pos-lfp (one 14-minute LFP chunk per session):** stated, and reasonable.
- **fig4d-ole-near-bayesian and fig4e-ole-covariance (the OLE estimator):** stated, but the reading now adopted is the less reasonable of the two. In the main reading the signal Q comes entirely from the tuning curves, with no noise variance on its diagonal (`ole_fit`, diag="signal"). The resulting signal decoder errs by up to 99 to 103° in some ensembles, worse than the 90° expected by chance (R cell 58), with a median of 46°. It is close to a non-working decoder, so the fig4e ratio of 0.25 measures that failure rather than the paper's gain. The variant, which puts the observed variances on the diagonal (independent neurons), is the usual signal-only OLE. Under it the ratio is 0.99, so both outcomes are still not_reproduced.

Possible misreadings in the claims file (reported, not corrected):

- **fig4d:** it takes the signal Q "from the tuning curves read at the head direction". The paper says "tuning curve covariances (i.e., signal correlation only)", which excludes noise correlations, not the cells' own variances. This wording invited the reading that does not work.
- **recording-sample:** the criterion defines only "reproduced", so partially_reproduced is the author's judgement. It is reasonable.

### 2. Statements the printed numbers do not support

- **The GLM timing:** "about 21 minutes" in G cell 0, G cell 11 and the README; "took 21.1 minutes … longest session Mouse28-140313 at 952 s" in the record's fig5e-readout-windows notes; "about 70 minutes" in R cell 85 and G cell 11. The printed figures are 12.2 min (G cell 2) and 561 s (G cell 4).
- **R cell 15:** "the 8 of 10 needed is out of reach by at most one count". Under hd-b, 5 of the 9 testable counts are within tolerance. Even if Mouse32 passed, that would be 6, so 2 more would be needed. The sentence is wrong as written; the record's own wording ("the outcome would be the same with Mouse32 left out") is correct.
- **R cell 86 (Summary):** "Recorded unit counts match Supplementary Table 1 in the thalamus-only mice and in PoS". Mouse20 has 48 against 49 (R cell 14).
- **R cell 76:** "The direction holds: binomial p = 0.064 (17 of 24 against one half)". At 0.064 the first binomial reading fails; only the second reading (p = 0.0009) holds.
- **Record, fig6b-adn-synchrony:** `measured: 1320` is the all-pairs waking count. The deciding sample is the pairs on different shanks: 492 per state, 1476 pooled (R cell 72).
- **Record notes for fig2f-sws-tenfold-faster and fig2f-rem-similar-to-wake, and R cells 39 and 43:** "no fitted speed is 0" is true only literally. Every state has fits at 1.5e-14 deg/s (R cell 38), which are effectively 0. The medians are not affected.
- **R cell 46 and the record's fig3a-packet-60-degrees notes:** "Under rate-a the PoS-PoS tests reach only p = 5.5e-6 to 7.2e-5". This holds only under hd-a; under hd-b rate-a all 9 tests pass. With the cosine of the offset, p reaches 1.3e-4.

Every other "**Result:**" sentence, the rest of the Summary, the README and the record's notes match the printed outputs. That includes the 34 tested and 1 blocked counts, and the 1007 of 1064 cells on which the file's HD labels agree with hd-a.

The record states my round-1 reasons faithfully in its own wording, with small omissions. For example, my fig3b-packet-coherence reason in the record leaves out the qualifier "with the mean summary and every reference and distance".

### 3. Round-1 points

**Resolved:**

- 1: ensemble-sizes under hd-b.
- 3: fig2e reading (a), now located below the 1° grid.
- 4: the plain signal-OLE reading has been run.
- 5: Mouse20 now follows the files' labels throughout.
- 6: Mouse32 is reported as untestable.
- 7: the supfig5 grouping.
- 8: infinite and zero speeds.
- 9: the coherence shuffle control.
- 10: the monotonicity column, the 4765-pair maximum and Mouse28-140314.
- 11: fig5d-adn-predicts-pos-reliably and fig5e-adn-predicts-pos are now tested.
- The open checks: the wake/open-field overlap (0.9998 to 1), the Mouse20 electrode groups, the speed-fit quality, the fig7 pairs per session and the GLM per-session timing.

**Remaining, and bearing on a conclusion:**

- **Round-1 point 2 (decoding uses hd-a ensembles only):** in round 1 I marked this as not affecting a conclusion. It now does. With 5 PoS ensembles, the fig4d PoS test cannot reach p < 0.05, and the fig4e Mann-Whitney test has little power. Decoding the hd-b ensembles (27 ADn, 11 PoS) could change fig4d, and possibly fig4e, to partially_reproduced.
- **fig5e-readout-windows:** the block as too_large is contradicted by the printed timing. It should be run with the denser window grid, or the block justified with timing the notebook actually prints.
- **fig4d and fig4e:** the adopted signal OLE performs at or worse than chance in some ensembles. Under the observed-variance variant (the usual signal-only OLE), the ADn part of fig4d fails (p = 0.156). The outcome should be described as resting on that variant, not on the degenerate decoder.
- **Borderline results:**
  - adn-pos-hd-information: the PoS mean is 1.004 against a lower bound of 0.999.
  - fig7e-driven-pos-hd-information: p = 0.040 with the Methods' baseline, 0.075 with the jitter baseline.
  - fig4d-ole-near-bayesian: covariance/Bayes is 1.264 against the 1.25 margin.
  - ensemble-sizes: the PoS mean depends on Mouse20's sessions.
