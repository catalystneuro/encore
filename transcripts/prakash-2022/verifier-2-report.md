**Round-2 verification: Prakash et al. 2022 (prakash-2022-01)**

**1. Outcomes**

The claims file has 26 claims and the attempt record has 26 outcomes: 13 reproduced, 3 partially reproduced, 2 not reproduced and 8 blocked. I agree with all 26. No outcome in the record carries `assumed: true`, so there are no assumptions to judge.

- **fig6f-nonfunctional-opsin-no-response (blocked, `other`).** I agree. In round 1 I said blocked as data_missing. The author used `other` because the claims file puts this data in the article's Supplementary Data, and the registry does not allow data_missing there. That is reasonable.
  - Cell 91 runs the test on the Fig. 5c 21-value column and gets p = 0.534. Neither published column gives the paper's 0.7870.
  - It also runs the legend's own Wilcoxon test, before against after SB + CTZ (n = 49), and gets p = 1.6e-9.
- **fig7d-contacts-exceeding-baseline (not reproduced).** I agree under the criterion as written. The reading in the claims file matches the Methods ("the bootstrapped 95th confidence interval of the mean of the baseline period"). The block-bootstrap variant gives 0 of 8 readings (cell 29).
- **fig7f-mua-electrodes (not reproduced).** I agree. The record says openly that this depends on the onset of interlum_ctrl_4 (cell 53).
- **fig7e-gamma-events-mice and fig7f-mua-mice-not-significant (blocked, methods underspecified).** I agree. Even with the union kept set alone, the readings still disagree:
  - events: U = 9 in 29 of 32 union readings, U = 8 in 3 (cell 44);
  - MUA: U is 6, 7 and 8 across the union rows (cell 50).
- **fig6c-green-light-abolishes (reproduced).** I agree. It holds under both readings (see section 2).

**2. Sentences the numbers do not support**

- **README and cell 0:** "takes about 40 minutes". Cell 13 prints "in vivo pipeline: 49.7 min" for the main pipeline step alone. The "40 GB" figure cannot be checked: cell 3 prints 49.1 GB for all six files, images included.
- **Cell 89, and the attempt record's fig6c notes:** "reading (b) … holds no SB + CTZ test". Reading (b) in the claims file only changes how green light is paired. The SB + CTZ test is the same under both readings. Under (b) the claim also holds: p = 0.0375 higher, and green light p = 0.0011 lower (cell 88). The outcome is unchanged; the description of the criterion is wrong.
- **Record finding on the bootstrap:** "25 to 29 per mouse". Cell 29 shows per-mouse counts from 22 to 31. 25 to 29 is roughly the range of the group means.
- **Record, fig7e-gamma-events-electrodes deviation and fig7e-gamma-events-mice notes:** "asked of the authors". Nothing in the materials shows that the authors were contacted. The questions appear only as findings.
- **Record inputs:** "No outcome uses it" (Supplementary Data 7). The fig7f-mua-electrodes notes use it to argue that the chosen onset is "the one the paper's data support". That is a slight tension and does not change any outcome.

I checked every other sentence of the Result conclusions, the Summary, the README and the record's notes against the printed outputs, and the numbers support them.

The record's verification block gives my round-1 reasons faithfully and in my own words for every claim, including problems 2, 3, 4, 5, 7, 8, 9 and 10, each folded into the relevant claim.

**3. Round-1 points**

Resolved:
- **Problem 1 (fig6f):** sheet printed in full, Fig. 5c column tried, outcome blocked.
- **Problem 2 (bias in P):** shown on white noise (−0.426 dB) and stated in the conclusion.
- **Problem 4 (onset):** a sensitivity check was added (cell 53) and its effects are stated.
- **Problem 5 (probe orientation):** all probe metadata is printed (cell 32). It cannot be settled from the files.
- **Problem 8 (direction check):** now uses medians throughout.
- **Problem 11 (claim count):** cell 0 now says 10 claims.
- **Problems 6, 7, 9 and 10:** recorded as findings or notes. None affected a conclusion.

Remaining points that bear on a conclusion:
- **fig7d-contacts-exceeding-baseline (problem 3, partly resolved).** The outcome no longer depends on whether the bootstrap treats steps as independent or uses blocks. It still depends on the criterion's confidence-interval-of-the-mean rule. Cell 20 shows the paper's own Fig. 7d sheets are centred on baseline (within 0.005 dB of 0). The right panel, Opsin (−) by the legend, has per-contact group means up to 0.34 dB after onset. So most Opsin (−) contacts rise in the paper's data too, and its 2.7 contacts per mouse probably come from a wider rule than the one described. The not_reproduced outcome may therefore reflect the rule and not the data. The record's methods_unavailable finding asks the right question, but the notes do not cite this evidence.
- **fig7d-superficial-layers.** Still blocked. One avenue was not tried: print the paper's per-contact Fig. 7d profile (contacts 1 to 25) next to this attempt's profile by z. That would show which end of the probe the paper's numbering starts from. It would settle the claim only together with the depth axis of the published figure.
- **fig7f-mua-electrodes and fig7f-mua-mice-not-significant.** Both depend on the onset of interlum_ctrl_4. That onset comes 8 s before the recorded infusion start, and the second-rise onset changes the electrode-level p to 0.012 to 0.15. The record states this. Which onset is right still cannot be determined from the files.
