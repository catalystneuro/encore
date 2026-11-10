**Verifier report, round 2: Timme et al. (2016), CRCNS hc-8**

The claims file has 28 claims, and the attempt record gives an outcome for each of them: 13 reproduced, 3 partially reproduced, 9 not reproduced and 3 blocked. Neither the record nor the claims file sets `assumed: true` anywhere, so no outcome rests on a flagged assumption.

### 1. Outcomes

I agree with all 28 outcomes as the criteria are written. Four need a caveat:

- **fig12a-swap-preserves-complexity (reproduced; it was not_reproduced in round 1).** The change follows the criterion: corrected p is 0.836 and Pearson r is 0.775 (complexity_culture.ipynb cell 15). The result is fragile, though:
  - It is a claim of absence, decided on only 40 recordings.
  - Each recording's estimate is noisy, with a median coefficient of variation of 0.78 across draws (cell 4).
  - r clears 0.7 only because of a few large values; Spearman is 0.533.
  - The 180-recording run in round 1 found a significant 65% decrease.

  The outcome could flip with more recordings.
- **fig5f-network-state-poisson-keeps-complexity (not_reproduced).** The miss comes from the estimator, not the data. Identical network states give draws up to 0.675 away from their own mean (models.ipynb cell 13), so no data could meet a 5% bound. The record says this.
- **figs9-complexity-fit-range-correlation (not_reproduced).** With n = 40 the standard error of r is about 0.15. The size-range value, 0.060 against 0.296, is only about 1.6 SE away. The result says little beyond "not clearly 0.3".
- **fig7d-cb-branching-ratio-near-1 (not_reproduced).** I agree. This is the judgment I asked for in round 1.

Places where the claims file misreads the paper or sets an unworkable test (reported, not corrected):

- **fig5f.** The criterion calls 5% "the residue of the random subset draws". With the toolbox's cut, the draw-to-draw residue is far larger (above), so the test cannot tell a change from no change.
- **figs8 and figs9.** A tolerance of 10% of r is narrower than the sampling error of r even across all 435 recordings (SE about 0.045).
- **eq4-relation-randomized.** The criterion cites "fig10-randomization-markers", which is not a claim in the file.
- **fig10c.** The criterion defines no partial outcome. The record's partially_reproduced follows fig11bd's rule, which I find reasonable.

### 2. Sentences the printed outputs do not support

- **complexity_culture.ipynb cell 20 (Summary), and the record's fig10a deviation:** "took 34.2 min for 40 recordings". Cell 1 prints 42.4 min.
- **README timings:** "about 42 min" for culture_criticality and "about 38 min" for complexity_culture. The printed run times are 37.3 + 2.0 min for culture_criticality (cells 1 and 16) and 42.4 + 4.2 min for complexity_culture (cells 1 and 4). The two figures look swapped.
- **README:** "behave as the paper reports, with some exceptions under the weakest randomization". 10-bin jitter is also an exception: alpha is not significant (corrected p 0.401, culture_criticality.ipynb cell 46). And fig10b passes only under susceptibility reading (b) with Benjamini-Hochberg (cell 36).
- **culture_criticality.ipynb cell 14:** "Layout reading b ... is run on four recordings below". Cell 16 runs it on one.
- **culture_criticality.ipynb cell 48 (Summary):** it lists a deviation, "jitter proposes all moves at once instead of one spike at a time", that the attempt record does not list under any claim that uses jitter.
- **Minor:** "78-fold" (record, fig10a). The printed relative change of 77.7 is a 78.7-fold rise.

Every other Result sentence, Summary sentence and attempt-record note I checked against the printed outputs agrees with them. The development timing of 134 s per complexity call, used in fig7ab, fig7a and figs2, is not printed and so cannot be checked.

The attempt record states my round-1 reasons faithfully, close to my own wording, and the verification summary describes B1 and B2 correctly.

### 3. Round-1 points

**Resolved:**

- **B1 (10 subsets per size).** Resolved as asked: the analysis now uses 100 subsets. The new spread check (cell 4) shows the instability remains on the real cultures even at 100 subsets: the cut keeps a median of 8 to 10 sizes, and the coefficient of variation is 0.78 against 0.86 at 10 subsets. So the problem lies with the toolbox's cut on these data, not with the number of subsets. The record states this and puts the question to the authors.
- **B2.** fig7ab is now not_reproduced, and fig7d is judged against it.
- **B4, B5, B6, B7.** Each is acknowledged, and none changes a conclusion.
- **fig2e question (section C).** Answered: the log10 histogram shows 43 of 435 recordings within half a decade of 10,000, with a median of 10^4.92.
- **Cortical branching model diagnostics (section C).** The one-step ratio and mean avalanche size are now printed against 4·p_trans.

**Remaining, and bearing on conclusions:**

1. **Recordings in the complexity notebook (B3, now worse).** It runs 40 recordings, down from 180 in round 1. This decides fig12a and weakens figs9. Running only the real and swapped conditions, about a quarter of the cost, on more recordings would settle fig12a.
2. **Port fidelity, still unchecked.** Neither the `complexity.m` cut nor `cbmodel.m` has been compared with the MATLAB toolbox. The author has the toolbox zip. The port puts B_new closest to 1 at p_trans 0.28, gives a one-step ratio of 0.937 where 4·p_trans = 1, and has a susceptibility with no peak; these bear on fig6, fig7ab, fig7c and fig7d. One p_trans and one recording run through both the toolbox and the port would settle it.
3. **Jitter implementation.** The unlisted deviation (section 2) touches exactly the comparisons that fail under 1-bin jitter: fig10c, fig11bd, fig10b reading (a) and fig10a. Printing the fraction of spikes held in place, or porting the toolbox's one-at-a-time version, would show whether it matters.
4. **fig8-exponents-match-literature.** It is blocked because the reference values were not retrieved in time, not because they are unobtainable: they are in the three cited papers.
