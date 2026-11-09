## Round 3 verification: Daume et al. (2024), DANDI:000673

The attempt record proposes two outcome changes; no other claim carries one. I checked both against the re-executed `reproduce_daume_2024_lfp.ipynb`. Every number quoted in the two proposals matches the printed outputs, apart from two rounding slips noted below.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig2f-rt-single-trial-pac | blocked (methods_underspecified) | Yes, with reservations | — | See below (lfp cell 27) |
| fig3h-pac-category-firing | reproduced | Yes | — (keep `assumed: true`) | See below (lfp cell 44) |

### fig2f-rt-single-trial-pac (lfp cell 27)

**Why I agree**
- **Load coding.** Making load 3 the reference level follows Supplementary Table S2: its term is named "Load1" and it says "Load 1 are tested against load 3 trials". The choice does not depend on the outcome.
- **Dropping RT in seconds.** This rests on evidence that does not depend on the outcome either:
  - With RT in seconds, the intercept is 1.697 against the paper's 0.38, and the Load1 term is −0.285 against −0.48.
  - Table S2 gives the same Load1 term (−0.48) for the hippocampus and the amygdala, which points to a standardised RT.
- **The two O5 readings disagree on both scales that fit Table S2:**
  - RT z-scored within session: the intercept is 0.279 and Load1 is −0.315.
    - Under O5 (a) the hippocampal term is −49.39 (t = −4.19, p = 2.8e-5), but the amygdala term is also significant (p = 0.0152), so the criterion fails.
    - Under O5 (b) the criterion is met: hippocampus p = 0.0294, amygdala 0.201, vmPFC 0.577.
  - log10 RT gives the same split: under O5 (a) the amygdala has p = 0.036; under O5 (b) the hippocampus has p = 0.0045, the amygdala 0.22 and vmPFC 0.87.
- The criterion as written says "methods_underspecified when the readings disagree", so blocked (methods_underspecified) follows.

**Reservations**
1. **The claims file leaves the RT scale open.** The criterion just says "RT". The natural reading is RT in seconds, and under it both O5 readings fail, which would give not reproduced. The change of scale goes beyond the criterion. I accept it only because of the intercept and Load1 evidence above.
2. **Possible misreading in the claims file.** Table S2's PAC estimate of −49.07 can only come from an unstandardised single-trial MI. A z-scored PAC under O5 (b) gives estimates around −0.02 to −0.03 here, while O5 (a) with z-scored RT gives −49.39. So Table S2 seems to settle O5 for this claim as reading (a), yet the claims file leaves O5 open. If O5 were fixed as (a), the outcome would be not reproduced, because the amygdala term is p = 0.015 here against the paper's 0.48. I am reporting this, not correcting it.
3. **One fit looks anomalous.** The amygdala fit with z-scored RT under O5 (a) has an intercept of −1.695e-11, which is essentially zero and implausible. That is the fit that decides the failure under O5 (a). The split still holds without it: RT in seconds gives amygdala p = 0.027 and log10 RT gives p = 0.036.
4. **The outcome rests on artefact reading (a), but the record does not mark it `assumed: true`.** Under artefact reading (b), every scale and both O5 readings meet the criterion, which would give reproduced. The claim should carry `assumed: true`.
5. **Rounding slip.** The record says the amygdala has "p >= 0.48" under artefact reading (b); the minimum is actually 0.4787.

### fig3h-pac-category-firing (lfp cell 44)

**Why I agree**
- Load 3 as the reference follows Supplementary Table S3's wording, as for fig2f.
- That coding is supported by the other terms under O5 (b) on all trials, which are close to Table S3:

  | Term | Here | Paper |
  |---|---|---|
  | Intercept | −0.0565 | −0.044 |
  | Load1 | 0.0779 | 0.076 |
  | SC × Load1 | −0.00485 | −0.004 |

- **Under artefact reading (a), all four readings of the criterion meet it.** The hippocampal SC (spike count) term is positive with p < 0.05 in each:

  | Trials | O5 reading | Hippocampal SC p |
  |---|---|---|
  | all | (a) | 2.3e-10 |
  | all | (b) | 0.0020 |
  | preferred | (a) | 0.0020 |
  | preferred | (b) | 0.031 |

  The amygdala SC term has p of 0.90, 0.33, 0.80 and 0.92 across the same four readings. That meets the criterion as written.

**Caveats**
- The outcome rests on artefact reading (a), as the record already marks with `assumed: true`. Under reading (b), preferred trials with O5 (b) give p = 0.056, which would make this claim methods_underspecified. One amygdala fit under (b) did not converge.
- **Rounding slip.** The record says the amygdala has "p >= 0.33"; the minimum is actually 0.3263.
- Here the scale of Table S3 matches O5 (b), the z-scored PAC, whereas Table S2 matches O5 (a). The paper may use a different single-trial PAC in its two tables. This does not change fig3h, because every reading passes.
